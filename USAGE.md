# Doc to Markdown - Usage Guide

PDF 技術規格書轉 Markdown 工具，用於 RAG 知識庫建置。

## Installation

```bash
pip install marker-pdf PyMuPDF anthropic click Pillow
```

**Note:** marker-pdf 首次執行會自動下載 OCR 模型（約 2GB），需要網路連線。

## Environment Setup

設定 Anthropic API Key（Vision API 品質檢查和描述生成需要）：

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Windows:
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

## Basic Usage

```bash
# 最基本的用法 - 一行搞定
python -m doc_to_markdown.main input/your_spec.pdf

# 指定輸出目錄
python -m doc_to_markdown.main input/your_spec.pdf -o output/my_output

# 使用不同的 Vision API 模型
python -m doc_to_markdown.main input/your_spec.pdf --model claude-sonnet-4-20250514

# 全 Vision 模式（跳過 Marker，所有頁面用 Vision API）
python -m doc_to_markdown.main input/your_spec.pdf --full-vision

# 從上次中斷處繼續
python -m doc_to_markdown.main input/your_spec.pdf --resume

# 只重新生成 Description（已有 chapters/ 的情況下）
python -m doc_to_markdown.main input/your_spec.pdf --desc-only
```

## Pipeline Steps

工具執行 8 個步驟：

| Step | Name | Description |
|------|------|-------------|
| 1 | PDF Parse | 解析 PDF 結構、偵測章節邊界、分析圖片/表格區域 |
| 2 | Marker Convert | 使用 Marker 開源工具轉換所有頁面 |
| 3 | Quality Rules | 規則掃描：亂碼、空表格、缺圖、內容過短、格式錯誤 |
| 4 | Quality Sampling | 抽樣 ~30 頁送 Vision API 比對品質 |
| 5 | Vision Redo | 問題頁重做 + 圖片描述生成 |
| 6 | Merge | 按章節合併為 .md 檔案 |
| 7 | Descriptions | 為每份 .md 生成 description 和 keywords |
| 8 | Catalog | 產出 catalog.json 和 README.md |

## Output Structure

```
output/<pdf_name>/
├── chapters/           # 按章節分割的 .md 檔案
│   ├── 01_introduction.md
│   ├── 02_architecture.md
│   └── ...
├── descriptions/       # 每份 .md 的 description JSON
│   ├── 01_introduction.json
│   └── ...
├── images/             # 擷取的頁面圖片
├── marker_cache/       # Marker 轉換中間結果（可刪除）
├── catalog.json        # 所有檔案的 description 總索引
├── quality_report.json # 品質檢查報告
├── progress.json       # 斷點續跑進度檔
├── conversion_log.json # 轉換記錄
└── README.md           # 本次轉換結果摘要
```

## catalog.json Format

```json
{
  "total_files": 24,
  "files": [
    {
      "file": "01_introduction.md",
      "title": "Introduction",
      "description": "UFS 4.0 規格書簡介，涵蓋規格目的、適用範圍...",
      "keywords": ["UFS", "scope", "terminology"],
      "page_range": "1-12"
    }
  ]
}
```

直接將 `files` 陣列匯入 RAG 知識庫的 description 欄位即可。

## Resume / 斷點續跑

如果執行中斷（API rate limit、網路問題、手動中止），進度會自動存在 `progress.json`。

```bash
# 續跑
python -m doc_to_markdown.main input/your_spec.pdf --resume
```

## Cost Estimation

以 542 頁 PDF、約 200 頁需 Vision API 處理為例：

| Model | Estimated Cost |
|-------|---------------|
| Claude Sonnet 4 | ~$7-10 |
| Claude Opus 4 | ~$35-50 |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ANTHROPIC_API_KEY not set` | 設定環境變數 |
| `Rate limit exhausted` | 等幾分鐘後用 `--resume` 繼續 |
| `PDF is encrypted` | 先用其他工具解鎖 PDF |
| Marker 下載模型很慢 | 首次需下載 ~2GB，請耐心等待 |
| 記憶體不足 | Marker 需要 ~5GB RAM/VRAM |
| 章節數 > 100 | 調整 `config.py` 中的 `MAX_CHAPTER_PAGES` |
