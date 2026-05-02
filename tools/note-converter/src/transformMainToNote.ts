/**
 * main 形式 → note 形式の Markdown 変換（旧 transform_note_reusable.py と同等）。
 * インライン $...$ → $${...}$$、見出しから数式区切り除去、式ブロック整形、式内 * → \ast
 *
 * note.com のディスプレイ数式は `\\` を「ブロック全体の改行」にも使うため、
 * `pmatrix` 等の行区切り `\\` が誤解釈され列ベクトルが横並びになることがある。
 * 行列環境内だけ `\\`（および `\\[…]`）を `\cr` に置き換える（main 側の `\\` は不変）。
 *
 * note.com の TeX では `\,`（thin space）がカンマとして誤って表示されることがあるため、
 * note 向け出力では `\,` を通常スペースに置き換える（main 原稿の `\,` はそのまま）。
 * 同様に `\;`（medium space）が数式を途中で切り、続きを本文扱いにして `_` 添字が壊れることがあるため、
 * note 向けでは `\;` も通常スペースに置き換える。
 *
 * note.com の引用（`> …`）はブロックの文字色が背景と同化し「真っ白」に見えることがあるため、
 * `【ここまでのチェックポイント】` で始まる引用ブロックだけを**通常の箇条書き**に直す。
 * `注 （…）` で始まる注釈の引用ブロックも同様に、**`【注】（…）` の独立行**＋本文（`#` は使わない）に直す。
 * 本文との境界が分かるよう、注釈ブロックの前後に `---`（前は先に本文があるときだけ）を挟む。
 * 見出しの `#`・行単独の `**…**` も環境によっては消えるため、タイトルは **【…】のみの独立行**（プレーンテキスト）にする。
 *
 * note / 拡張の簡易 MD パーサは `**…**` 内に `*` があると太字に失敗し `**` が残る。
 * また太字が `$${…}$$` をまたぐと解釈が壊れることがあるため、
 * 数式をまたぐ太字は `**文**$${…}$$**字**` に分割する（`findClosingBoldDoubleStar` は数式をスキップして閉じ `**` を探す）。
 *
 * ブラウザ用の同一ロジックは `viewer/static/note-export-transform.js`（API 未実装時のフォールバック）。
 * ここを変えたらそのファイルも同期すること（`stripStrongHtmlFromNote` を含む）。
 */

const AST_PH = "__AST_PLACEHOLDER__";

/** 行内の $$...$$ を保護しつつ $...$ を $${...}$$ に（$ はエスケープ可） */
export function transformInlineEquations(line: string): string {
  const parts = line.split(/(\$\$[\s\S]*?\$\$)/);
  const out: string[] = [];
  for (let i = 0; i < parts.length; i++) {
    let part = parts[i]!;
    if (i % 2 === 0) {
      part = part.replace(
        /(?<!\\)\$([^$\n]+?)(?<!\\)\$/g,
        (_m, content: string) => `$$\{${content}\}$$`
      );
    }
    out.push(part);
  }
  return out.join("");
}

/**
 * $$ 単独行ブロックと単行 $$...$$ に対応。
 * さらに、開始 `$$` と終了 `$$` が別行にある複行ブロック（`$$\n式\n…\n$$`）も
 * note 向けに $$\n式\n$$ に正規化する（開始 `$$` 直後の改行が無いと note で本文と一体化しやすい）。
 * note ではブロック数式は開始 `$$` の直後に改行が必要なため、1 行に潰さず常に
 * $$\n式\n$$ 形式にする。
 *
 * インラインを note 形へ直した行は `$${…}$$` で始まり、先頭が `$$` に見える。
 * これを表示ブロックの `$$` と誤認すると `{df}` だけの壊れたフェンスになるため、
 * `$${` で始まる行はそのまま通す。
 */
export function transformEquationBlocks(content: string): string {
  const lines = content.split("\n");
  const result: string[] = [];
  let i = 0;
  const n = lines.length;

  while (i < n) {
    const stripped = lines[i]!.trim();
    if (stripped === "$$") {
      i += 1;
      const body: string[] = [];
      while (i < n && lines[i]!.trim() !== "$$") {
        body.push(lines[i]!);
        i += 1;
      }
      if (i < n) {
        i += 1;
      }
      const eqContent = body.join("\n").trim();
      result.push("", "$$", eqContent, "$$", "");
    } else if (stripped.startsWith("$${")) {
      result.push(lines[i]!);
      i += 1;
    } else if (
      stripped.startsWith("$$") &&
      stripped.endsWith("$$") &&
      stripped.length > 4
    ) {
      const eqContent = stripped.slice(2, -2).trim();
      result.push("", "$$", eqContent, "$$", "");
      i += 1;
    } else if (stripped.startsWith("$$")) {
      const firstLine = lines[i]!;
      const openIdx = firstLine.indexOf("$$");
      let rest = firstLine.slice(openIdx + 2);
      const body: string[] = [];
      const closeOnFirst = rest.indexOf("$$");
      if (closeOnFirst !== -1) {
        body.push(rest.slice(0, closeOnFirst));
        const eqContent = body.join("\n").trim();
        result.push("", "$$", eqContent, "$$", "");
        i += 1;
      } else {
        body.push(rest);
        i += 1;
        while (i < n) {
          const L = lines[i]!;
          if (L.trimEnd().endsWith("$$")) {
            const lastClose = L.lastIndexOf("$$");
            body.push(L.slice(0, lastClose));
            i += 1;
            break;
          }
          body.push(L);
          i += 1;
        }
        const eqContent = body.join("\n").trim();
        result.push("", "$$", eqContent, "$$", "");
      }
    } else {
      result.push(lines[i]!);
      i += 1;
    }
  }

  return result.join("\n");
}

/** 見出し行から $...$ / $$...$$ の区切りだけ外す */
export function transformHeadings(line: string): string {
  if (!line.startsWith("#")) {
    return line;
  }
  let s = line.replace(/\$\$(.*?)\$\$/g, "$1");
  s = s.replace(/\$(.*?)\$/g, "$1");
  return s;
}

const MATRIX_ENV_NAMES = new Set([
  "pmatrix",
  "bmatrix",
  "Bmatrix",
  "vmatrix",
  "Vmatrix",
  "matrix",
  "array",
]);

/** 行間スペース指定 `\\[dim]` の `[dim]` を削除すべき環境 */
const ALIGN_LIKE_ENV_NAMES = new Set([
  "aligned",
  "alignedat",
  "gathered",
]);

function findMatchingEndEnv(
  s: string,
  env: string,
  start: number
): number {
  const beginTok = `\\begin{${env}}`;
  const endTok = `\\end{${env}}`;
  let depth = 1;
  let pos = start;
  while (pos < s.length && depth > 0) {
    const nb = s.indexOf(beginTok, pos);
    const ne = s.indexOf(endTok, pos);
    if (ne === -1) {
      return -1;
    }
    if (nb !== -1 && nb < ne) {
      depth += 1;
      pos = nb + beginTok.length;
    } else {
      depth -= 1;
      if (depth === 0) {
        return ne;
      }
      pos = ne + endTok.length;
    }
  }
  return -1;
}

/**
 * 行列環境内の行区切り `\\` を `\cr` に（note.com 向け）。
 * aligned / alignedat / gathered では `\\[dim]` の `[dim]` を削除する。
 * ネストした `\begin{pmatrix}` 等も再帰処理する。
 */
export function replaceMatrixRowSeparatorsForNote(text: string): string {
  let pos = 0;
  let out = "";
  while (pos < text.length) {
    const idx = text.indexOf("\\begin{", pos);
    if (idx === -1) {
      out += text.slice(pos);
      break;
    }
    const rest = text.slice(idx);
    const m = rest.match(/^\\begin\{([^}]+)\}/);
    if (!m) {
      out += text.slice(pos, idx + 1);
      pos = idx + 1;
      continue;
    }
    const env = m[1]!;
    const beginTok = m[0]!;
    const isMatrix = MATRIX_ENV_NAMES.has(env);
    const isAlignLike = ALIGN_LIKE_ENV_NAMES.has(env);
    if (!isMatrix && !isAlignLike) {
      out += text.slice(pos, idx + beginTok.length);
      pos = idx + beginTok.length;
      continue;
    }
    out += text.slice(pos, idx);
    const innerStart = idx + beginTok.length;
    const innerEnd = findMatchingEndEnv(text, env, innerStart);
    if (innerEnd === -1) {
      out += text.slice(idx);
      break;
    }
    const inner = text.slice(innerStart, innerEnd);
    const innerRec = replaceMatrixRowSeparatorsForNote(inner);
    let innerFixed: string;
    if (isMatrix) {
      innerFixed = innerRec.replace(/\\\\(\[[^\]]*\])?/g, "\\cr$1");
    } else {
      innerFixed = innerRec.replace(/\\\\\[[^\]]*\]/g, "\\\\");
    }
    const endTok = `\\end{${env}}`;
    out += beginTok + innerFixed + endTok;
    pos = innerEnd + endTok.length;
  }
  return out;
}

/**
 * note.com 向け: LaTeX の `\,`（thin space）がカンマとしてレンダリングされることがあるため、
 * `\,` を半角スペースに置換する。`\\,`（行区切り直後の thin space 等）は `\,` とみなさない。
 */
export function replaceThinSpaceForNote(content: string): string {
  return content.replace(/(?<![\\])\\,/g, " ");
}

/**
 * note.com 向け: `\;`（medium space）が数式の続きを本文扱いにして添字が壊れることがあるため、
 * 通常スペースに置き換える。`\\;` は `\,` と同様にそのまま（行末 `\\` との誤マッチ防止）。
 */
export function replaceMediumSpaceForNote(content: string): string {
  return content.replace(/(?<![\\])\\;[ \t]*/g, " ");
}

/**
 * note.com 向け: `$$` 表示数式ブロック内で、行頭の `-` が箇条書きと誤解釈されるのを防ぐため、
 * `-` → `{-}` に置き換える。`$${…}$$`（インライン数式）は対象外。
 */
export function replaceLeadingMinusInNoteMath(content: string): string {
  let pos = 0;
  let out = "";
  while (pos < content.length) {
    const a = content.indexOf("$$", pos);
    if (a === -1) {
      out += content.slice(pos);
      break;
    }
    out += content.slice(pos, a);
    if (content[a + 2] === "{") {
      let depth = 1;
      let j = a + 3;
      while (j < content.length && depth > 0) {
        const c = content[j]!;
        if (c === "\\") {
          j += Math.min(2, content.length - j);
          continue;
        }
        if (c === "{") depth += 1;
        else if (c === "}") depth -= 1;
        j += 1;
      }
      if (depth !== 0 || content.slice(j, j + 2) !== "$$") {
        out += "$$";
        pos = a + 2;
        continue;
      }
      out += content.slice(a, j + 2);
      pos = j + 2;
      continue;
    }
    const b = content.indexOf("$$", a + 2);
    if (b === -1) {
      out += content.slice(a);
      break;
    }
    const body = content.slice(a + 2, b);
    const newBody = body.replace(/^(\s*)-/gm, "$1{-}");
    out += "$$" + newBody + "$$";
    pos = b + 2;
  }
  return out;
}

/**
 * `$$ … $$` と `$${ … }$$` の数式断片にだけ行列用 `\cr` 置換をかける。
 */
export function applyMatrixRowSeparatorFixForNote(content: string): string {
  let pos = 0;
  let out = "";
  while (pos < content.length) {
    const a = content.indexOf("$$", pos);
    if (a === -1) {
      out += content.slice(pos);
      break;
    }
    out += content.slice(pos, a);
    if (content[a + 2] === "{") {
      let depth = 1;
      let j = a + 3;
      while (j < content.length && depth > 0) {
        const c = content[j]!;
        if (c === "\\") {
          j += Math.min(2, content.length - j);
          continue;
        }
        if (c === "{") {
          depth += 1;
        } else if (c === "}") {
          depth -= 1;
        }
        j += 1;
      }
      if (depth !== 0 || content.slice(j, j + 2) !== "$$") {
        out += "$$";
        pos = a + 2;
        continue;
      }
      const inner = content.slice(a + 3, j - 1);
      out += "$${" + replaceMatrixRowSeparatorsForNote(inner) + "}$$";
      pos = j + 2;
      continue;
    }
    const b = content.indexOf("$$", a + 2);
    if (b === -1) {
      out += content.slice(a);
      break;
    }
    const body = content.slice(a + 2, b);
    out += "$$" + replaceMatrixRowSeparatorsForNote(body) + "$$";
    pos = b + 2;
  }
  return out;
}

/** `$${ … }$$` の終端直後のインデックス。`start` が `$${` でなければ `start`。 */
export function skipPastNoteInlineMath(s: string, start: number): number {
  if (s.slice(start, start + 3) !== "$${") {
    return start;
  }
  let depth = 1;
  let i = start + 3;
  while (i < s.length && depth > 0) {
    const c = s[i]!;
    if (c === "\\") {
      i += Math.min(2, s.length - i);
      continue;
    }
    if (c === "{") {
      depth += 1;
    } else if (c === "}") {
      depth -= 1;
    }
    i += 1;
  }
  if (depth !== 0 || s.slice(i, i + 2) !== "$$") {
    return start;
  }
  return i + 2;
}

/** 表示用 `$$\n…\n$$`（`$${` で始まるインラインは除く）の終端直後。 */
export function skipPastNoteDisplayMathFence(s: string, start: number): number {
  if (s.slice(start, start + 2) !== "$$") {
    return start;
  }
  if (s[start + 2] === "{") {
    return start;
  }
  const end = s.indexOf("$$", start + 2);
  if (end === -1) {
    return start;
  }
  return end + 2;
}

function skipPastAnyNoteMathDelimiters(s: string, j: number): number {
  const afterInline = skipPastNoteInlineMath(s, j);
  if (afterInline > j) {
    return afterInline;
  }
  const afterDisplay = skipPastNoteDisplayMathFence(s, j);
  return afterDisplay;
}

/**
 * `innerStart` から数式を飛ばしつつ、太字の閉じ `**` の開始インデックス。無ければ -1。
 */
export function findClosingBoldDoubleStar(s: string, innerStart: number): number {
  let j = innerStart;
  while (j < s.length - 1) {
    const skipped = skipPastAnyNoteMathDelimiters(s, j);
    if (skipped > j) {
      j = skipped;
      continue;
    }
    if (s[j] === "*" && s[j + 1] === "*") {
      return j;
    }
    j += 1;
  }
  return -1;
}

/**
 * 太字内部を note インライン数式 `$${…}$$` だけで区切り、各テキスト片を `**…**` で包む。
 * （`}$$` を表示用 `$$` と誤認しないよう、インライン以外の `$$` はここでは扱わない。）
 */
export function splitBoldInnerAtNoteMath(inner: string): string {
  let pos = 0;
  let out = "";
  while (pos < inner.length) {
    const idx = inner.indexOf("$${", pos);
    if (idx === -1) {
      const tail = inner.slice(pos);
      if (tail) {
        out += `**${tail}**`;
      }
      break;
    }
    if (idx > pos) {
      out += `**${inner.slice(pos, idx)}**`;
    }
    const end = skipPastNoteInlineMath(inner, idx);
    if (end === idx) {
      out += inner[idx]!;
      pos = idx + 1;
      continue;
    }
    out += inner.slice(idx, end);
    pos = end;
  }
  return out;
}

/**
 * `**…**` を数式をまたがない形に直す（手貼り note 向け）。閉じ `**` は数式内の `**` と誤認しない。
 */
export function applyBoldSplitAroundNoteMath(content: string): string {
  let pos = 0;
  let out = "";
  while (pos < content.length) {
    const open = content.indexOf("**", pos);
    if (open === -1) {
      out += content.slice(pos);
      break;
    }
    out += content.slice(pos, open);
    const close = findClosingBoldDoubleStar(content, open + 2);
    if (close === -1) {
      out += "**";
      pos = open + 2;
      continue;
    }
    const inner = content.slice(open + 2, close);
    if (inner === "") {
      out += "****";
      pos = close + 2;
      continue;
    }
    if (!inner.includes("$${")) {
      out += `**${inner}**`;
      pos = close + 2;
      continue;
    }
    out += splitBoldInnerAtNoteMath(inner);
    pos = close + 2;
  }
  return out;
}

/** $$...$$ ブロック内の * を \ast に（既存 \ast は保護） */
export function replaceAsteriskInEquations(content: string): string {
  const parts = content.split(/(\$\$[\s\S]*?\$\$)/);
  const out: string[] = [];
  for (let i = 0; i < parts.length; i++) {
    let part = parts[i]!;
    if (i % 2 === 1) {
      part = part.replace(/\\ast/g, AST_PH);
      part = part.replace(/(?<!\\)\*/g, "\\ast");
      part = part.replace(new RegExp(AST_PH, "g"), "\\ast");
    }
    out.push(part);
  }
  return out.join("");
}

/**
 * main 側の `<strong>…</strong>` を note から除去（中身は残す）。ネストにも繰り返し対応。
 * note.com 等では HTML の strong よりプレーン寄りにそろえる用途。
 */
export function stripStrongHtmlFromNote(content: string): string {
  let s = content;
  const re = /<strong>((?:(?!<\/?strong>).)*?)<\/strong>/gi;
  let prev: string;
  do {
    prev = s;
    s = s.replace(re, "$1");
  } while (s !== prev);
  return s;
}

/** 先頭行が `【ここまでのチェックポイント…】` の引用ブロックのみ、引用記号を外して表示する（note.com 向け）。 */
export function unwrapCheckpointBlockquotesForNote(content: string): string {
  const lines = content.split("\n");
  const out: string[] = [];
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]!;
    const m = line.match(/^> \s*(【ここまでのチェックポイント[^】]*】)\s*$/);
    if (!m) {
      out.push(line);
      continue;
    }
    const title = m[1]!;
    out.push(title, "");
    i += 1;
    while (i < lines.length && lines[i]!.startsWith("> ")) {
      out.push(lines[i]!.slice(2));
      i += 1;
    }
    i -= 1;
  }
  return out.join("\n");
}

/** `> 注 （タイトル）…` 形式の引用を、note.com で見えるよう **【注】（タイトル）** 行＋本文に展開する */
export function unwrapAnnotationBlockquotesForNote(content: string): string {
  const lines = content.split("\n");
  const out: string[] = [];

  const stripBlockquotePrefix = (line: string): string =>
    line.replace(/^\s*>\s*/, "");

  const lastNonEmptyLine = (arr: string[]): string | undefined => {
    for (let k = arr.length - 1; k >= 0; k--) {
      const s = arr[k]!.trim();
      if (s !== "") {
        return arr[k]!;
      }
    }
    return undefined;
  };

  const pushSeparatorBeforeBlock = () => {
    if (out.length === 0) {
      return;
    }
    const last = lastNonEmptyLine(out)?.trim();
    if (last === "---") {
      out.push("");
    } else {
      out.push("", "---", "");
    }
  };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]!;
    const firstInner = stripBlockquotePrefix(line);
    if (!/^注\s*（/.test(firstInner)) {
      out.push(line);
      continue;
    }

    const innerLines: string[] = [];
    let j = i;
    while (j < lines.length && /^\s*>/.test(lines[j]!)) {
      innerLines.push(stripBlockquotePrefix(lines[j]!));
      j += 1;
    }

    const head = innerLines[0]!;
    const parsed = head.match(/^注\s*（([^）]*)）\s*(.*)$/);
    if (!parsed) {
      pushSeparatorBeforeBlock();
      out.push(...innerLines);
      out.push("", "---", "");
      i = j - 1;
      continue;
    }
    const title = parsed[1]!;
    const restFirst = parsed[2] ?? "";
    pushSeparatorBeforeBlock();
    out.push(`【注】（${title}）`, "");
    if (restFirst.length > 0) {
      out.push(restFirst);
    }
    for (let k = 1; k < innerLines.length; k++) {
      out.push(innerLines[k]!);
    }
    out.push("", "---", "");
    i = j - 1;
  }
  return out.join("\n");
}

/** 全文を main → note 形式に変換 */
export function transformMainToNoteMarkdown(content: string): string {
  const lines = content.split("\n");
  const transformedLines = lines.map((line) => {
    let L = transformHeadings(line);
    L = transformInlineEquations(L);
    return L;
  });
  let transformed = transformedLines.join("\n");
  transformed = replaceAsteriskInEquations(transformed);
  transformed = transformEquationBlocks(transformed);
  transformed = applyMatrixRowSeparatorFixForNote(transformed);
  transformed = replaceLeadingMinusInNoteMath(transformed);
  transformed = replaceThinSpaceForNote(transformed);
  transformed = replaceMediumSpaceForNote(transformed);
  transformed = applyBoldSplitAroundNoteMath(transformed);
  transformed = stripStrongHtmlFromNote(transformed);
  transformed = unwrapCheckpointBlockquotesForNote(transformed);
  transformed = unwrapAnnotationBlockquotesForNote(transformed);
  return transformed;
}
