# Document to Markdown

PDF 技術規格書轉高品質 Markdown 的 CLI 工具，專為 RAG 知識庫建置設計。

採用 **Hybrid 架構**：[Marker](https://github.com/VikParuchuri/marker) 開源 OCR 為主力轉換引擎，搭配 Claude Vision API 自動補強品質不佳的頁面，確保表格、圖片、技術內容的轉換品質。

## Features

- **一行指令轉換** — 輸入 PDF 路徑即可，自動完成 8 步驟 pipeline
- **智慧品質檢查** — 規則掃描 + Vision API 抽樣比對，自動標記問題頁面
- **章節自動拆分** — 依 PDF 目錄結構拆分，控制在合理數量（20-80 份）
- **RAG 最佳化** — 自動生成每份文件的 description 和 keywords，輸出 `catalog.json` 方便匯入知識庫
- **斷點續跑** — 中途中斷可用 `--resume` 接回，不浪費已完成的 API 呼叫
- **圖片文字化** — 圖表轉為文字描述，最利於 RAG 檢索

## Quick Start

```bash
# Install dependencies
pip install marker-pdf PyMuPDF anthropic click Pillow

# Set API key (for Vision API quality check & descriptions)
export ANTHROPIC_API_KEY="your-key-here"

# Convert a PDF
python -m doc_to_markdown.main your_spec.pdf
```

## CLI Options

```
Usage: python -m doc_to_markdown.main [OPTIONS] PDF_PATH

Options:
  -o, --output TEXT   Output directory (default: output/<pdf_name>/)
  --model TEXT        Vision API model (default: claude-sonnet-4-20250514)
  --full-vision       Use Vision API for ALL pages (skip Marker)
  --resume            Resume from last checkpoint
  --desc-only         Only regenerate descriptions
  --help              Show this message and exit
```

## Pipeline

```
Step 1: PDF Parse      → Detect chapters, images, tables
Step 2: Marker Convert → OCR-based conversion for all pages
Step 3: Quality Rules  → Scan for garbled text, empty tables, missing images
Step 4: Quality Sample → Vision API spot-check ~30 pages
Step 5: Vision Redo    → Re-convert flagged pages + describe images
Step 6: Merge          → Assemble per-chapter .md files
Step 7: Descriptions   → Generate description + keywords per chapter
Step 8: Catalog        → Output catalog.json and README
```

## Output Structure

```
output/<pdf_name>/
├── chapters/           # Markdown files split by chapter
├── descriptions/       # Per-chapter description JSON
├── catalog.json        # All descriptions (import into RAG)
├── quality_report.json # Quality check results
├── progress.json       # Resume checkpoint
└── README.md           # Conversion summary
```

## Cost Estimate

For a ~500 page technical spec (Hybrid mode, ~200 pages need Vision API):

| Model | Estimated Cost |
|-------|---------------|
| Claude Sonnet 4 | ~$7-10 |
| Claude Opus 4 | ~$35-50 |

## Requirements

- Python 3.10+
- ~5GB RAM (for Marker OCR models)
- Anthropic API key (for Vision API steps)

## License

MIT
