# Translation Pipeline (ja → en)

日本語原稿を英語に翻訳するパイプライン。

## Setup

```bash
cd tools/translate
pip install -r requirements.txt
```

## Configuration

1. リポジトリルートの `.env` ファイルに DeepSeek API キーを設定:
   ```
   DEEPSEEK_API_KEY=sk-...
   ```
   （`.env` は `.gitignore` で Git 管理外になっています）

2. （オプション）モデル名を変更する場合:
   ```
   DEEPSEEK_MODEL=deepseek-chat
   ```

## Usage

### Automatic translation (DeepSeek API)

```bash
python tools/translate/ja_to_en.py manuscript/ja/ch01/ch01.md --auto
```

優先順位:
1. DeepSeek API (`DEEPSEEK_API_KEY` が設定されていれば)
2. ローカル ollama (フォールバック)
3. プロンプトのみ出力 (どちらも失敗した場合)

### Manual translation (prompt-only)

```bash
python tools/translate/ja_to_en.py manuscript/ja/ch01/ch01.md
# → manuscript/en/ch01/ch01.prompt.txt が生成される
```

生成されたプロンプトを ChatGPT / Claude / DeepSeek に投げ、結果を保存:

```bash
python tools/translate/ja_to_en.py manuscript/ja/ch01/ch01.md --apply manuscript/en/ch01/ch01.prompt.response.txt
```

## Output

- `manuscript/en/chXX/chXX.md` — 英語版原稿
- `manuscript/en/chXX/chXX.prompt.txt` — LLM 用プロンプト（手動翻訳時）

## Preserved Elements

翻訳時に保持される要素:
- YAML frontmatter
- Code fences (```)
- Display math ($$, \\[...\\])
- Inline math ($...$)
- LSP annotations (<!-- concept-scope: ... -->)
- HTML tags (<strong>, etc.)
