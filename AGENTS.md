# nabla-kaitai Project Notes

## Project Overview
Public GitHub repository for "ナブラ解体新書" (Nabla Kai-sai) - a mathematics textbook on vector analysis using differential forms and matrix representations.

**Repository**: https://github.com/yokiikoy/nabla-kaitai
**GitHub Pages**: https://yokiikoy.github.io/nabla-kaitai/

## Publishing Workflow

### 1. Building PDF
```bash
cd /home/yokii/dev/knowledge/work/nabla-kaitai
python3 tools/build_pdf.py
# Output: exports/manuscript.pdf (180 pages)
cp exports/manuscript.pdf ./manuscript.pdf
```

### 2. Building GitHub Pages HTML
```bash
cd /home/yokii/dev/knowledge/work/nabla-kaitai
python3 tools/build_html.py
# Output: docs/index.html
```

### 3. GitHub Pages Deployment
- GitHub Pages serves from `main` branch's `docs/` folder
- Any commit to `main` in `docs/` automatically deploys
- Branch protection requires PR to merge to `main`

### 4. Updating Release Assets
```bash
# Upload PDF
gh release upload v0.1.0 ./manuscript.pdf --repo yokiikoy/nabla-kaitai --clobber

# Upload HTML
cp docs/index.html manuscript.html
gh release upload v0.1.0 ./manuscript.html --repo yokiikoy/nabla-kaitai --clobber
rm manuscript.html
```

### 5. Merge to Main (Branch Protection)
Since `main` is protected, use PR workflow:
```bash
git checkout -b pub/update-v0.X.Y
git add <changed-files>
git commit -m "message"
git push -u origin pub/update-v0.X.Y
# Create PR at: https://github.com/yokiikoy/nabla-kaitai/pull/new/pub/update-v0.X.Y
```

## Key Files
- `tools/build_pdf.py` - PDF generation script (XeLaTeX)
- `tools/build_html.py` - GitHub Pages HTML generation (regex-based, preserves LaTeX)
- `exports/manuscript_combined.md` - Combined manuscript source
- `docs/index.html` - GitHub Pages entry point
- `manuscript.pdf` - Current PDF release

## Important Notes

### LaTeX Preservation
The `build_html.py` uses regex-based conversion (NOT Python markdown library) because the markdown library was converting `\\` to `\ ` which broke LaTeX matrices like `\begin{pmatrix}`.

### MathJax Configuration
```javascript
window.MathJax = {
  loader: { load: ['[tex]/bm'] },
  tex: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: false,
    packages: { '[+]': ['bm'] }
  }
};
```

### Branch Protection
- `main` requires PR with 1 approval
- Direct push blocked for all users including owner
- Use feature branches + PR for all changes

### Excluded Files (gitignore)
- `exports/*.aux`, `*.log`, `*.toc`, `*.fls`, `*.fdb_latexmk`, `manuscript.html` (LaTeX intermediates)
- `reference/` (large PDFs/OCR, not in git)
- `.codex`, `.env`, `__pycache__/`, `.venv/`

## Release Management
- Current release: **v0.1.0** (https://github.com/yokiikoy/nabla-kaitai/releases/tag/v0.1.0)
- Assets: `manuscript.pdf`, `manuscript.html`
- After changes: update release assets via `gh release upload`

## Common Tasks

### Add new chapter content:
1. Edit relevant file in `manuscript/ja/ch##/`
2. Run `python3 tools/build_pdf.py` to rebuild combined manuscript
3. Run `python3 tools/build_html.py` to update GitHub Pages HTML
4. Commit and create PR

### Fix MathJax rendering:
1. Check `docs/index.html` has MathJax CDN and config
2. Verify `$$\\...$$` and `$...$` are preserved (not converted)
3. Check for leftover placeholders: `grep 'MATH_INLINE\\|INLINE_MATH' docs/index.html`
4. Rebuild with `python3 tools/build_html.py`

### Update branch protection temporarily (for emergency):
```bash
# Remove protection
gh api repos/yokiikoy/nabla-kaitai/branches/main/protection -X DELETE

# Reapply protection after push
gh api repos/yokiikoy/nabla-kaitai/branches/main/protection -X PUT -f required_status_checks=null -f enforce_admins=true -f required_approving_review_count=1
```