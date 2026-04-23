# Doc to Markdown - Project Instructions

## Project Overview

PDF 技術規格書轉高品質 Markdown 的 CLI 工具，專為 RAG 知識庫建置設計。

**Triple-layer 架構**：
1. **Text-first**（`--text-first`）：PyMuPDF 直接抽 embedded text layer，對 native-digital PDF（例如 SCSI spec）最快、零成本
2. **Marker OCR**：預設基底，用 surya 模型轉換每頁
3. **Vision 補強**：對品質不佳頁面做高品質重做

視覺模型可為：
- 當前 Claude Code CLI session（CLI mode，免 API）
- 遠端 Vision/LLM API（API mode，支援 Anthropic 或 OpenAI-compatible 地端 AI）

**GitHub:** https://github.com/billchen-hub/document-to-markdown

## Architecture

```
doc_to_markdown/
├── config.py                # 設定、模式、API provider 設定
├── main.py                  # CLI 入口 + 8 步驟 pipeline 控制器（雙模式 branch）
├── pdf_parser.py            # PDF 拆頁、圖片擷取、章節偵測 (PyMuPDF)
├── marker_converter.py      # Marker OCR 基礎轉換
├── vision_converter.py      # Vision API 轉換（支援 Anthropic + OpenAI-compatible）
├── text_extractor.py        # --text-first 模式：PyMuPDF 抽 embedded text + 分類頁面
├── cli_vision_handler.py    # CLI mode 任務清單產出 + 載入 Claude 補強結果
├── quality_checker.py       # 品質檢查（規則掃描 + API mode 抽樣比對）
├── merger.py                # 按章節合併最終 Markdown
├── desc_generator.py        # Description + keywords 生成器（API mode）
```

## Key Commands

```bash
# CLI mode（預設，無 API key）
python -m doc_to_markdown.main "input/your_spec.pdf"
# Step 5 暫停 → Claude 依 need_vision.json 補強 → --resume 繼續
python -m doc_to_markdown.main "input/your_spec.pdf" --resume

# API mode — Anthropic 公開 API
export VISION_PROVIDER=anthropic
export VISION_API_KEY=sk-ant-xxx
python -m doc_to_markdown.main "input/spec.pdf" --mode api

# API mode — 公司地端 AI（OpenAI-compatible）
export VISION_PROVIDER=openai-compatible
export VISION_BASE_URL=https://your-company-ai.internal/v1
export VISION_API_KEY=token
export VISION_MODEL=qwen-vl-max
python -m doc_to_markdown.main "input/confidential.pdf" --mode api

# Text-first — 對 native-digital PDF（SCSI spec 類）最推薦
python -m doc_to_markdown.main "input/spec.pdf" --mode cli --text-first
# 只有 sparse / scanned 頁會進 need_vision.json，其餘直接抽文字

# 其他：
python -m doc_to_markdown.main "input/spec.pdf" --desc-only
python -m doc_to_markdown.main "input/spec.pdf" --full-vision
```

## Implementation Status

**2026-04-23 新增：**
- **`--text-first` 模式**：`text_extractor.py` 用 PyMuPDF 抽 embedded text + 自動偵測 running header/footer 濾除 + 頁面分類（text / hybrid / vision）
- **實測**：
  - SBC-4 (447 頁) → 246 純文字 + 201 hybrid + 1 vision → 幾秒完成，0 vision API cost
  - SPC-4 (1012 頁) → 590 純文字 + 422 hybrid + 0 vision → 幾秒完成
- **意義**：native-digital PDF 不用跑 Marker OCR、不用燒 vision token，只在必要時 escalate 到 Claude vision
- 兩份 SCSI spec 完整 output（76 + 102 章、全部 description）push 上 git

**2026-04-21 新增：**
- **雙模式架構**：`--mode cli` / `--mode api`
- **CLI mode**：Marker 跑完後產出 `need_vision.json` 任務清單 + render PNG 到 `pages_for_vision/`，pipeline 暫停讓當前 Claude Code session 接手
- **地端 AI 支援**：`VisionConverter` 支援 OpenAI-compatible endpoint（Anthropic + on-prem Qwen/LLaMA）
- 新檔 `cli_vision_handler.py`：封裝 CLI mode 的 manifest 產出 / 驗證 / 載入

**已完成（2026-03-27）：**
- 全部 8 個 Python 模組實作並通過 229 個 unit tests
- PDF 解析：UFS 4.1（542 頁, 73 章）、SBC-4（447 頁, 76 章）、SPC-4（1012 頁, 102 章）
- 品質檢查：5 項規則掃描 + Vision API 抽樣比對
- CLI 選項：`--mode`, `--resume`, `--full-vision`, `--desc-only`, `--model`, `-o`

## TODO / Known Issues

- [ ] 完整 pipeline 對 SBC-4 / SPC-4 在 CLI mode 下的實跑驗證（進行中 2026-04-21）
- [ ] marker-pdf 要求 anthropic<0.47，但我們用 0.86（功能不衝突，pip 會警告）
- [ ] Marker CPU 慢（~15s/頁，447 頁 ~2h）— 考慮 GPU 加速文件

## Agent Teams

此專案未使用 agent teams 配置。

## Tech Notes

- **API key 存放**：
  - `VISION_API_KEY` / `ANTHROPIC_API_KEY` 環境變數（推薦）
  - `.claude/settings.local.json` 的 `env` 區塊（專案級，`.gitignore` 已擋）
  - 切勿 commit 到 git
- Marker 首次執行自動下載 surya OCR 模型到 `~/.cache/`（~2GB）
- Marker 需要 ~5GB RAM/VRAM
- 斷點續跑透過 `output/<name>/progress.json`

## CLI Mode Handoff Protocol

當 pipeline 在 CLI mode 下暫停時（Step 5 或 Step 7），Claude 接手的 SOP：

**Step 5（vision redo）— 讀 `output/<pdf>/need_vision.json`：**
1. 對每個 task 用 Read 看 `png` 檔
2. 依 `action` 分派：
   - `convert_to_markdown`：轉換整頁為 markdown（保留標題、表、文字、圖描述），Write 到 `output_md`
   - `append_image_description`：讀既有 `output_md`，追加 `\n\n[Image Description: ...]`，Write 回去
3. 所有 task 完成後執行 `python -m doc_to_markdown.main <pdf> --resume --mode cli`

**Step 7（descriptions）— 讀 `output/<pdf>/need_desc.json`：**
1. 對每個 task 用 Read 看 `chapter_file`
2. 生成 `{file, title, description(繁中 2-3 句), keywords(英文 3-6 個), page_range}` JSON
3. Write 到 `output_json`
4. 完成後 `--resume` 即可

## Slides / 投影片

`docs/slides/doc_to_markdown_deck.html` — 12 張 HTML 投影片，介紹整套架構給技術主管/工程師。
離線可開（只需瀏覽器）。Space / 方向鍵 / 右側 dots 導航。
