# Doc to Markdown - Project Instructions

## Project Overview

PDF 技術規格書轉高品質 Markdown 的 CLI 工具，專為 RAG 知識庫建置設計。
Hybrid 架構：Marker OCR 為主力 + Claude Vision API 自動補強品質不佳頁面。

**GitHub:** https://github.com/billchen-hub/document-to-markdown

## Architecture

```
doc_to_markdown/
├── config.py              # 設定檔（閾值、路徑、預設模型）
├── main.py                # CLI 入口 + 8 步驟 pipeline 控制器
├── pdf_parser.py          # PDF 拆頁、圖片擷取、章節偵測 (PyMuPDF)
├── marker_converter.py    # Marker OCR 基礎轉換
├── vision_converter.py    # Claude Vision API 轉換 + 圖片描述
├── quality_checker.py     # 品質檢查（規則掃描 + 抽樣比對）
├── merger.py              # 按章節合併最終 Markdown
├── desc_generator.py      # Description + keywords 生成器
```

## Key Commands

```bash
# 基本轉換
python -m doc_to_markdown.main input/your_spec.pdf

# 從斷點續跑
python -m doc_to_markdown.main input/your_spec.pdf --resume

# 只重新生成 Description
python -m doc_to_markdown.main input/your_spec.pdf --desc-only

# 全 Vision 模式
python -m doc_to_markdown.main input/your_spec.pdf --full-vision
```

## Implementation Status

**已完成 (2026-03-27)：**
- 全部 8 個 Python 模組已實作並通過驗證
- PDF 解析：542 頁 UFS spec，73 章節，全部 <= 50 頁
- 品質檢查：5 項規則掃描 + Vision API 抽樣比對
- CLI：所有選項可用（--resume, --full-vision, --desc-only, --model, -o）
- 已推送至 GitHub

## TODO / Known Issues

- [ ] 完整 pipeline 尚未實際跑過（marker 模型需首次下載 ~2GB）
- [ ] marker-pdf 要求 anthropic<0.47，但我們用 0.86（功能不衝突，pip 會警告）
- [ ] 轉換品質尚需實際 PDF 跑完後驗證
- [ ] 測試用例覆蓋度可再提升（目前有基礎 unit tests）

## Tech Notes

- API key 在 `.claude/settings.local.json`（不進 git）
- Marker 首次執行自動下載 surya OCR 模型到 `~/.cache/`
- 需要 ~5GB RAM/VRAM
- 斷點續跑透過 `output/<name>/progress.json`
