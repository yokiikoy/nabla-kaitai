# Elixir + Fly.io ポータル母艦 仕様書

## 1. 背景

`nabla-kaitai` は現在、Markdown 原稿から HTML/PDF を生成し、GitHub Pages と GitHub Release Assets で公開している。これは書籍配信だけを考えれば十分に軽く、単なる静的配信の置き換えとして Elixir + Fly.io を導入する必然性は弱い。

一方で、Project Co-Vector Space / ナブラ解体新書の周辺には、今後 Discord 運営、visitor 管理、メール認証、支援導線、翻訳補助、資料管理などの小さな運営ツールが増える可能性がある。Elixir + Fly.io は、これらを同じ運用面に載せるための「部室インフラの母艦」として位置づける。

## 2. 目的

初期目的は、Fly.io 上に Elixir 製の小さなポータルアプリを置き、生成済み HTML/PDF を配信できる状態を作ることである。ただし、この段階では GitHub Pages を本番の正本として維持し、Fly.io 版は staging として運用する。

将来目的は、同じアプリに以下の機能を段階的に載せられる構成を作ることである。

- Discord 数式 bot
- Discord visitor ロールの期限管理
- visitor 再取得用のメール認証
- Stripe / PayBot まわりの状態確認補助
- Discord 通知 bot
- 翻訳 bot
- 資料管理 bot
- LP と Discord 運営情報の動的表示
- 将来的な部室内ツール

## 3. 非目的

初期実装では、以下は行わない。

- Markdown / HTML / PDF 生成パイプラインの Elixir 移植
- DB 導入
- Discord bot 本体の実装
- Stripe / PayBot 連携の実装
- GitHub Pages の即時廃止
- 本番ドメインの即時切り替え

## 4. 基本方針

生成系は既存の Python パイプラインを維持する。

```text
python3 tools/build_html.py
python3 tools/build_pdf.py
```

Elixir 側は、生成済みファイルを `priv/static` に置き、Phoenix または Plug/Bandit で配信する。初期段階では Phoenix `--no-ecto` を標準案とする。理由は、将来 LiveView、認証、管理画面、worker を追加する余地があり、Fly.io の Elixir/Phoenix 公式導線も利用しやすいためである。

DB は初期導入しない。ただし、将来 visitor 管理を追加する段階で SQLite または Postgres を足せる構成にする。

静的配信だけなら、Fly.io を本番化しない。Elixir + Fly.io は、visitor 管理、メール認証、bot などの動的機能が必要になった段階で本番化を検討する。

## 5. 役割分担

ドメイン、DNS、静的配信、動的機能の責務を分ける。

```text
Cloudflare Registrar:
  covectorspace.xyz のドメイン管理

Cloudflare DNS:
  DNS 管理

GitHub Pages / Cloudflare Pages:
  初期の静的ポータル本番
  LP、PDF、規約、支援案内の安定公開

Fly.io:
  Elixir アプリの staging
  将来の Discord 運営ツール母艦
  数式 bot、visitor 管理、メール認証、管理画面などの動的機能
```

初期公開は GitHub Pages または Cloudflare Pages を優先する。Fly.io は最初から本番導線にしない。

## 6. フェーズ計画

### Phase 0: GitHub Pages を正本として維持

LP 公開と書籍配信を優先する。

この段階で公開されていればよいものは次である。

- PDF
- 正誤表
- Discord 案内
- GitHub 導線
- 利用規約
- 執筆支援・支援導線まわりの約束事

GitHub Pages または Cloudflare Pages を正本にし、Fly.io はまだ本番導線にしない。

### Phase 1: Elixir ポータルの最小実装

`portal_app/` または `phoenix_app/` に Elixir アプリを作る。

候補:

```text
mix phx.new portal_app --no-ecto
```

初期ルーティング:

```text
/
  redirect または language selector
/jp
/jp/pdf
/jp/rules
/jp/support
/en
/en/pdf
/en/rules
/en/support
/downloads/nabla-kaitai.pdf
/downloads/unmasking-div-grad-curl.pdf
/assets/*
```

初期責務:

- LP を返す
- 日本語 LP / 英語 LP を返す
- 日本語 PDF / 英語 PDF の導線を返す
- Discord 利用規約を言語別に返す
- 執筆支援・支援導線まわりの約束事を言語別に返す
- 生成済み静的ファイルを配信する

`money` は URL としては使わない。支援導線は `/jp/support`, `/en/support` を標準とし、必要に応じて `/jp/writing-support`, `/en/writing-support` を検討する。

### Phase 1b: Discord 数式 bot の最小 backend

数式 bot を自前で動かす場合、Fly.io の実用上の理由が強くなる。LP 配信は GitHub Pages / Cloudflare Pages に残し、Bot backend だけ Fly.io に置く構成を先に試す。

最小構成:

```text
Fly.io
  Elixir app
    /health
    Discord interaction endpoint
    TeX renderer
```

初期機能:

```text
/tex <latex>
  TeX を PNG または SVG にレンダリングして Discord に返す

Render TeX
  選択メッセージから TeX を抽出し、画像として返す
```

初期段階では DB は不要である。キャッシュも必須ではない。visitor 管理を足す段階で DB 導入を検討する。

数式 bot の技術判断:

- 外部 bot は最軽量だが、停止リスク、見た目の制御、奥部屋の数式を外部へ渡す問題がある
- 自前 bot は常駐 backend が必要だが、部室独自の導線と制御を持てる
- 完全 backend なしでは、Discord 内の slash command や message command は扱えない
- 初期は `/tex` のみでよい

### Phase 2: Fly.io staging

本番前に staging app を作る。

想定名:

```text
covectorspace-staging.fly.dev
```

確認項目:

- `/` が表示される
- `/jp` が表示される
- `/en` が表示される
- `/jp/pdf` で日本語 PDF 導線が表示される
- `/en/pdf` で英語 PDF 導線が表示される
- `/jp/rules` と `/en/rules` が表示される
- `/jp/support` と `/en/support` が表示される
- `/downloads/nabla-kaitai.pdf` で日本語 PDF が取得または表示できる
- 章 HTML へのリンクが壊れない
- `assets/*` が配信される
- キャッシュ設定が妥当である
- GitHub Pages へ戻せる

Fly.io は利用量課金であり、無料前提にしない。公式料金表では Fly Machine VM の料金は CPU/RAM プリセットと追加 RAM などに基づく。staging は月数ドル程度の実験サーバーとして扱う。

### Phase 3: 本番ドメイン切り替えの判断

staging が安定してから、`covectorspace.xyz` を Fly.io に向けるか判断する。

Fly.io を本番化する条件:

- visitor 管理、メール認証、bot などの動的機能が必要になった
- 静的配信だけでは運用が詰まった
- staging で 1 か月以上安定稼働した
- ロールバック手順が確認済みである
- 月額コストが許容範囲内である

静的配信だけで足りている間は、Fly.io を本番化しない。

切り替え後もしばらく GitHub Pages 版を残す。理由は、Fly.io 側の設定、課金、デプロイ、DNS、TLS に問題が出た場合、すぐ戻せるようにするためである。

### Phase 4: Discord 運営ツールの追加

Elixir を使う意味が強く出る段階である。

優先順位:

1. Discord 数式 bot
2. visitor ロール期限管理
3. visitor 再取得用のメール認証
4. Stripe / PayBot 状態確認の補助
5. Discord 通知 bot
6. 翻訳 bot
7. 資料管理 bot

数式 bot を初手で入れる場合、Fly.io は LP の本番配信ではなく Bot backend の置き場として使う。最初は `/tex` だけでよい。

## 7. Visitor 管理の概略仕様

Visitor は、Discord の新規参加者に一定期間だけ付与するロールである。期限後に前室アクセスを外すための運用ロールであり、BAN ではない。

基本方針:

- 新規参加者に期限付き Visitor ロールを付与する
- 期限後は前室アクセスを外す
- BAN ではなく、再参加のための導線を残す
- 再 Visitor 化にはメール認証を使う
- 再取得には一定のインターバルを設ける
- 初期は手動対応でよい
- 需要が出たら Elixir 側で自動化する

自動化時に必要になる情報:

- Discord user id
- Visitor 付与日時
- Visitor 期限
- メール認証状態
- 再取得回数
- 最終再取得日時
- 管理者による例外設定

## 8. Secrets 管理

Discord、決済、メール認証に関わる秘密情報は GitHub repo に置かない。

想定 secrets:

- `DISCORD_BOT_TOKEN`
- `DISCORD_APPLICATION_ID`
- `DISCORD_PUBLIC_KEY`
- `STRIPE_SECRET_KEY`
- `PAYBOT_WEBHOOK_SECRET`
- `MAIL_PROVIDER_API_KEY`
- `SECRET_KEY_BASE`

管理方針:

- Fly.io secrets で管理する
- staging と production で secrets を分離する
- `.env` を Git に入れない
- ローカル開発用のサンプルは `.env.example` など、値を含まないファイルだけにする
- GitHub Actions を使う場合も GitHub Secrets にのみ置く

## 9. 推奨ディレクトリ構成

初期案:

```text
nabla-kaitai/
  manuscript/
  docs/
  exports/
  assets/
  rules/
  support/
  tools/
  portal_app/
    mix.exs
    lib/
      portal/
      portal_web/
    priv/
      static/
        index.html
        jp/
          index.html
          pdf/
          rules/
          support/
        en/
          index.html
          pdf/
          rules/
          support/
        downloads/
          nabla-kaitai.pdf
          unmasking-div-grad-curl.pdf
        assets/
    rel/
    Dockerfile
    fly.staging.toml
    fly.production.toml
```

`docs/` は GitHub Pages 用に残す。`portal_app/priv/static/` は Fly.io 用の配信コピー先とする。

## 10. ビルドパイプライン

初期パイプライン:

```text
1. python3 tools/build_html.py
2. python3 tools/build_pdf.py
3. docs/*.html を portal_app/priv/static/ へコピー
4. exports/manuscript.pdf を portal_app/priv/static/downloads/nabla-kaitai.pdf へコピー
5. mix test
6. fly deploy -c fly.staging.toml
```

このコピー処理は、最初は shell script または `mix` task のどちらでもよい。初期実装では、既存生成スクリプトに責務を混ぜない。

## 11. アプリケーション設計

初期は DB なしの Phoenix アプリとする。

主要責務:

- 静的ファイル配信
- Discord interaction endpoint
- 固定ルーティング
- 将来 API の名前空間確保
- 将来 worker / bot の OTP supervisor 配下への追加余地

将来の名前空間案:

```text
PortalWeb.PageController
PortalWeb.StaticController
PortalWeb.DiscordInteractionController
Portal.TeXRenderer
Portal.Visitors
Portal.Discord
Portal.MailAuth
Portal.Payments
Portal.Documents
Portal.Translation
```

初期段階では `Portal.Visitors` 以降はディレクトリだけ作るか、設計書に留める。空実装を増やしすぎない。

## 12. DB 導入方針

Phase 1 では DB を使わない。

visitor 管理が必要になった段階で、次のどちらかを選ぶ。

- SQLite: 小規模・単一リージョン・運用軽量
- Postgres: 複数機能・永続運用・将来の管理画面向き

Fly.io では Phoenix + Postgres の公式導線がある。ただし、Postgres は費用と運用対象が増えるため、visitor 管理の仕様が固まるまで入れない。

## 13. ロールバック方針

本番切り替え前:

- GitHub Pages / Cloudflare Pages を正本にする
- Fly.io は staging として運用する
- 問題が出ても公開導線には影響させない

本番切り替え後:

- DNS を GitHub Pages / Cloudflare Pages 側へ戻せるようにする
- GitHub Pages 用 `docs/` を削除しない
- Release Assets の PDF を維持する
- Fly.io のデプロイ失敗時は直前リリースへ戻す

## 14. 受け入れ条件

Phase 1 の完了条件:

- Elixir アプリがローカルで起動する
- `/`, `/jp`, `/en`, `/jp/pdf`, `/jp/rules`, `/jp/support`, `/en/pdf`, `/en/rules`, `/en/support` が応答する
- `priv/static` から生成済み HTML/PDF を配信できる
- DB なしで起動できる
- 既存の Python 生成パイプラインを壊していない

Phase 1b の完了条件:

- `/health` が応答する
- Discord interaction endpoint が署名検証できる
- `/tex <latex>` が最小の TeX 入力を画像として返せる
- DB なしで動く
- LP 本番導線に影響しない

Phase 2 の完了条件:

- Fly.io staging に deploy できる
- staging URL で HTML/PDF が見える
- 月額コスト見込みが確認されている
- GitHub Pages へのロールバック手順が文書化されている

Phase 3 の完了条件:

- 本番ドメイン切り替えの判断材料が揃っている
- GitHub Pages 版を退避先として維持している
- 切り戻し手順を実際に確認している

## 15. 初期判断の再確認

初期実装では Fly.io は本番ではなく staging とする。LP 公開と書籍配信は、GitHub Pages または Cloudflare Pages の静的ホスティングを優先する。

Fly.io の本番化は、数式 bot、visitor 管理、メール認証、Discord bot、支援導線の動的表示など、静的配信では扱いにくい運用要件が出た時点で判断する。

LP は GitHub Pages / Cloudflare Pages、Bot backend は Fly.io、という分離を初期の現実解とする。

## 16. 参考リンク

- Fly.io Elixir/Phoenix guide: https://fly.io/docs/elixir/getting-started/
- Fly.io Elixir overview: https://fly.io/docs/elixir/
- Fly.io pricing: https://fly.io/docs/about/pricing/
- Fly.io billing: https://fly.io/docs/about/billing/
