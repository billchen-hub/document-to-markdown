# Doc to Markdown — Usage Guide

詳細操作指引。快速概覽看 [README.md](README.md)。

## Installation

```bash
pip install -r requirements.txt
```

**Note:** marker-pdf 首次執行會自動下載 OCR 模型（約 2GB）到 `~/.cache/`，需要網路連線。

## 決定用哪個模式

```
  ┌─────────────────────────────────┐
  │  這份 PDF 是機密 / 內部文件嗎？   │
  └─────────────────────────────────┘
           │                │
          Yes               No
           │                │
           ▼                ▼
    API Mode          CLI Mode
  （公司地端 AI）   （免 API、Claude CLI 直接看）
```

| 考量 | CLI Mode | API Mode |
|------|---------|---------|
| 資料外流風險 | ❌ 無（零網路呼叫） | ⚠️ 有（送到 API endpoint） |
| 費用 | 0 | 依供應商 |
| 依賴 Claude Code session | ✅ 需要 | ❌ 不需要 |
| 能批次無人工跑 | ❌ 需要 Claude session 接手 | ✅ 完全自動 |
| 品質 | 很高（Claude 多模態） | 依選的模型而定 |

---

## Workflow A: CLI Mode（公開文件）

### 1. 啟動 pipeline

```bash
python -m doc_to_markdown.main "input/your_spec.pdf"
```

Marker 會跑完所有頁（約 15-20 秒 / 頁）。跑完後進入 Step 5 會暫停並印出：

```
======================================================================
CLI MODE: Pipeline paused at Step 5.
  Manifest: output/<pdf>/need_vision.json
  Pages rendered to: output/<pdf>/pages_for_vision
  Total tasks: 42

Claude Code: please process each task in the manifest by reading
the PNG and writing the resulting markdown to the path in
`output_md`. When every task has its output_md populated,
re-run this command with --resume to continue.
======================================================================
```

### 2. Claude Code session 接手補強

**在同一個 Claude Code session 裡**，請 Claude（我）：

> 請讀 `output/<pdf>/need_vision.json`，依照指示把每一頁 PNG 轉成 markdown。

Claude 會：
1. 讀 manifest
2. 對每個 task 用 Read 看 PNG
3. 用 Write 寫 markdown 到 `output_md` 指定路徑
4. 完成後告訴你可以 `--resume`

### 3. Resume pipeline

```bash
python -m doc_to_markdown.main "input/your_spec.pdf" --resume
```

Step 5 會驗證所有 task 的 `output_md` 都存在且非空，然後繼續 Step 6 (merge)。

### 4. Description 階段也類似

到 Step 7 會再暫停一次，由 Claude 讀每章 Markdown 寫 description JSON。再 `--resume` 完成 Step 8。

**或** 一口氣要 Claude 把 need_vision.json 和 need_desc.json 都做完，再 `--resume` 一次即可。

---

## Workflow B: API Mode（機密 / 地端 AI）

### 情境 1：Anthropic 公開 API

```bash
export VISION_PROVIDER=anthropic
export VISION_API_KEY=sk-ant-xxx
export VISION_MODEL=claude-sonnet-4-20250514

python -m doc_to_markdown.main "input/spec.pdf" --mode api
```

完全自動跑完，不需 Claude Code session 介入。

### 情境 2：公司地端 AI（OpenAI-compatible）

大多數公司地端 AI 服務（Qwen、LLaMA、自訂 gateway）都支援 OpenAI-compatible 的 `/v1/chat/completions` endpoint。

```bash
export VISION_PROVIDER=openai-compatible
export VISION_BASE_URL=https://your-company-ai.internal/v1
export VISION_API_KEY=your-company-token
export VISION_MODEL=qwen-vl-max

python -m doc_to_markdown.main "input/機密規格.pdf" --mode api
```

**如何測試地端 AI 是否可用？** 先用 curl 測試：

```bash
curl "$VISION_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $VISION_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'$VISION_MODEL'",
    "messages": [{"role":"user","content":"Say hello"}],
    "max_tokens": 20
  }'
```

返回 200 + 合理回應 = OK。

---

## Resume / 斷點續跑

執行中斷（手動 Ctrl+C、網路問題、CLI 階段暫停）時，進度自動存在 `progress.json`：

```bash
python -m doc_to_markdown.main "input/spec.pdf" --resume
```

## Desc-only（只重生 description）

已完成章節但想重跑 description：

```bash
# CLI mode
python -m doc_to_markdown.main "input/spec.pdf" --mode cli --desc-only

# API mode
python -m doc_to_markdown.main "input/spec.pdf" --mode api --desc-only
```

## --full-vision（跳過 Marker）

讓 vision 模型處理**所有頁面**，不跑 Marker。品質最高但成本/時間也最高。

```bash
# CLI mode：所有頁都由 Claude CLI 看（耗 context）
python -m doc_to_markdown.main "input/spec.pdf" --mode cli --full-vision

# API mode：所有頁都呼叫 API（耗錢）
python -m doc_to_markdown.main "input/spec.pdf" --mode api --full-vision
```

## Output Structure

```
output/<pdf_name>/
├── chapters/                  # 按章節分割的 .md
│   ├── 01_introduction.md
│   └── ...
├── descriptions/              # 每章 description JSON
├── images/                    # 擷取的頁面圖片
├── marker_cache/              # Marker 每頁 md（含 Claude 補強結果）
├── pages_for_vision/          # CLI mode 補強用 PNG
├── need_vision.json           # CLI mode 補強任務清單
├── need_desc.json             # CLI mode description 任務清單
├── catalog.json               # 全部 description 總索引（給 RAG）
├── quality_report.json
├── progress.json
├── conversion_log.json
└── README.md                  # 本次摘要
```

## catalog.json Format

```json
{
  "total_files": 24,
  "files": [
    {
      "file": "01_introduction.md",
      "title": "Introduction",
      "description": "SCSI Block Commands-4 規格簡介，涵蓋...",
      "keywords": ["SCSI", "SBC-4", "block commands"],
      "page_range": "1-12"
    }
  ]
}
```

直接把 `files` 陣列匯入 RAG 的 description 欄位即可。

## CLI 模式 — Claude 接手任務的 JSON 範例

`need_vision.json`:
```json
{
  "mode": "cli",
  "stage": "vision_redo",
  "total_tasks": 42,
  "tasks": [
    {
      "page_0based": 15,
      "page_1based": 16,
      "png": "pages_for_vision/page_0015.png",
      "action": "convert_to_markdown",
      "output_md": "marker_cache/page_0015.md",
      "reason": "empty_table"
    },
    ...
  ]
}
```

`need_desc.json`:
```json
{
  "mode": "cli",
  "stage": "descriptions",
  "total_tasks": 24,
  "tasks": [
    {
      "chapter_file": "chapters/03_introduction.md",
      "title": "Introduction",
      "page_range": "1-12",
      "output_json": "descriptions/03_introduction.json"
    },
    ...
  ]
}
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ANTHROPIC_API_KEY not set` | 用 CLI mode（`--mode cli`），或設定 `VISION_API_KEY` |
| `Invalid API key` | 檢查 `VISION_API_KEY` / `VISION_BASE_URL` |
| `Rate limit exhausted` | API mode 下等幾分鐘後 `--resume` |
| `PDF is encrypted` | 先用其他工具解鎖 |
| Marker 下載模型很慢 | 首次 ~2GB，請耐心等 |
| 記憶體不足 | Marker 需 ~5GB RAM/VRAM |
| 章節數 > 100 | 調整 `config.py` 的 `MAX_CHAPTER_PAGES` |
| CLI mode 產出空白章節 | 檢查 `need_vision.json` 裡還有 task 的 `output_md` 沒寫完 |

## Cost Estimation

### CLI Mode
- **$0**（不用 API）

### API Mode (~500 頁技術 spec，約 200 頁需補強)
| Provider / Model | Estimated Cost |
|-----------------|----------------|
| Anthropic Claude Sonnet 4 | ~$7-10 |
| Anthropic Claude Opus 4 | ~$35-50 |
| 公司地端 AI（Qwen-VL） | 依公司計算，通常 ≈ 0 |
