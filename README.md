# Document to Markdown

PDF 技術規格書轉高品質 Markdown 的 CLI 工具，專為 RAG 知識庫建置設計。

採用 **Hybrid 架構**：[Marker](https://github.com/VikParuchuri/marker) 開源 OCR 做每一頁的基礎轉換，再自動挑出品質不夠好的頁面、交給「視覺模型」補強。視覺模型可以是：

- 你當前的 **Claude Code CLI session**（免 API、免費）— 公開文件推薦
- 任何 **Vision/LLM API**（Anthropic、地端 Qwen、公司內部 AI gateway）— 機密文件推薦

## Features

- **兩種補強模式** — CLI mode（免 API）/ API mode（可接公司地端 AI）
- **智慧品質檢查** — 規則掃描 + 可選的抽樣比對，自動標記需補強頁面
- **章節自動拆分** — 依 PDF 目錄結構，控制在合理份數（20-100）
- **RAG 最佳化** — 自動生成每份文件的 description + keywords，輸出 `catalog.json`
- **斷點續跑** — `--resume` 從上次中斷處接回
- **圖片文字化** — 圖表轉為文字描述，提升 RAG 檢索命中

## Quick Start

```bash
# 1. 安裝
pip install -r requirements.txt

# 2. 把 PDF 放進 input/
cp your_spec.pdf input/

# 3. 轉換（預設 CLI mode，不用 API key）
python -m doc_to_markdown.main "input/your_spec.pdf"
```

Pipeline 跑到需要補強的頁面時會「暫停」並印出任務清單，由當前 Claude Code session 讀 PNG 寫 Markdown，然後 `--resume` 繼續：

```bash
python -m doc_to_markdown.main "input/your_spec.pdf" --resume
```

## 兩種補強模式

### 🟢 CLI Mode（預設；適用公開文件）

不呼叫任何外部 API。pipeline 跑到品質補強階段時：

1. 把需要補強的頁 render 成 PNG 到 `output/<pdf>/pages_for_vision/`
2. 產出 `output/<pdf>/need_vision.json` 任務清單
3. 退出 pipeline，提示 Claude Code 接手
4. Claude（你當前 session 的模型）讀 PNG、寫 Markdown
5. `--resume` 繼續合併、生 description

```bash
python -m doc_to_markdown.main "input/spec.pdf" --mode cli
# pipeline 暫停 → Claude 補完 → 繼續
python -m doc_to_markdown.main "input/spec.pdf" --mode cli --resume
```

### 🔒 API Mode（適用機密文件 / 公司地端 AI）

所有品質檢查和補強都走 API。支援兩種 provider：

#### a) Anthropic 公開 API

```bash
export VISION_PROVIDER=anthropic
export VISION_API_KEY=sk-ant-xxx
export VISION_MODEL=claude-sonnet-4-20250514

python -m doc_to_markdown.main "input/spec.pdf" --mode api
```

#### b) OpenAI-compatible 地端 AI（公司內部）

公司地端 AI 通常都提供 OpenAI-compatible endpoint（Qwen、LLaMA、自家 gateway 常見做法）。

```bash
export VISION_PROVIDER=openai-compatible
export VISION_BASE_URL=https://your-company-ai.internal/v1
export VISION_API_KEY=your-company-token
export VISION_MODEL=qwen-vl-max   # 或你們部署的模型名

python -m doc_to_markdown.main "input/機密規格.pdf" --mode api
```

## API Key 填哪裡？

三種方式任選一種：

### A. 環境變數（推薦）

**Windows PowerShell:**
```powershell
$env:VISION_PROVIDER = "openai-compatible"
$env:VISION_BASE_URL = "https://your-company-ai.internal/v1"
$env:VISION_API_KEY  = "your-token"
$env:VISION_MODEL    = "qwen-vl-max"
```

**macOS / Linux:**
```bash
export VISION_PROVIDER=openai-compatible
export VISION_BASE_URL=https://your-company-ai.internal/v1
export VISION_API_KEY=your-token
export VISION_MODEL=qwen-vl-max
```

### B. `.claude/settings.local.json`（專案級，Claude Code 自動載入為 env）

```json
{
  "env": {
    "VISION_PROVIDER": "openai-compatible",
    "VISION_BASE_URL": "https://your-company-ai.internal/v1",
    "VISION_API_KEY": "your-token",
    "VISION_MODEL": "qwen-vl-max"
  }
}
```

⚠️ 此檔已在 `.gitignore`，不會被 commit。**切勿把 API key 放進會被 commit 的檔案。**

### C. `.env` 檔（需搭配 python-dotenv，本專案預設不載入）

略。

## 支援的環境變數

| 變數 | 用途 | 預設 |
|------|------|------|
| `DOC2MD_MODE` | 轉換模式 `cli` / `api` | `cli` |
| `VISION_PROVIDER` | `anthropic` / `openai-compatible` | `anthropic` |
| `VISION_BASE_URL` | OpenAI-compatible endpoint URL | 空 |
| `VISION_API_KEY` | API token | 空 |
| `VISION_MODEL` | 模型名稱 | `claude-sonnet-4-20250514` |
| `ANTHROPIC_API_KEY` | 向後相容，會 fallback 到 `VISION_API_KEY` | 空 |

## CLI Options

```
Usage: python -m doc_to_markdown.main [OPTIONS] PDF_PATH

Options:
  --mode [cli|api]     轉換模式（default: cli）
  -o, --output TEXT    輸出目錄（default: output/<pdf_name>/）
  --model TEXT         Vision API 模型名（api mode 用）
  --full-vision        跳過 Marker，所有頁面走 vision
  --resume             從上次斷點續跑
  --desc-only          只重新生成 description
  --help
```

## Pipeline 8 步驟

```
Step 1: PDF Parse      → 解析章節、圖片/表格分佈
Step 2: Marker Convert → 每頁 OCR → Markdown
Step 3: Quality Rules  → 規則掃描（亂碼、空表、缺圖、格式錯）
Step 4: Quality Sample → api mode: 抽樣比對；cli mode: 跳過
Step 5: Vision Redo    → 補強品質不佳的頁面
                         - cli mode: Claude 讀 PNG 寫 md
                         - api mode: 呼叫 Vision API
Step 6: Merge          → 依章節合併 .md
Step 7: Descriptions   → 每章生成 description + keywords
                         - cli mode: Claude 讀章節寫 JSON
                         - api mode: 呼叫 LLM API
Step 8: Catalog        → catalog.json + README
```

## Output Structure

```
output/<pdf_name>/
├── chapters/            # 合併後章節 .md（給 RAG）
├── descriptions/        # 每章 description JSON（給 RAG）
├── catalog.json         # 全部 description 索引（給 RAG 匯入）
├── marker_cache/        # Marker 每頁 md（含 Claude 補強結果）
├── pages_for_vision/    # CLI 模式補強用 PNG（renderable pages）
├── need_vision.json     # CLI 模式補強任務清單
├── need_desc.json       # CLI 模式 description 任務清單
├── quality_report.json
├── progress.json        # 斷點續跑狀態
├── conversion_log.json
└── README.md            # 本次轉換摘要
```

## 與其他工具比較（技術 spec PDF）

| 工具 | 表格品質 | Heading/Layout | 圖片 | 技術 spec 合適度 |
|------|---------|---------------|------|----------------|
| **本工具（Marker + Claude 補強）** | 高 | 好 | Claude 描述 | ✅ 為此場景設計 |
| MinerU | 高（HTML 表） | 好 | 偶爾切不完 | ✅ 最強但需 GPU |
| Marker 獨用 | 中 | 好 | 高品質 | 🟡 OK 但表格弱 |
| Microsoft MarkItDown | 差（純文字） | 差（無 heading） | 基本 | ❌ 不適合 |

詳細比較：[Jimmy Song 2026 評測](https://jimmysong.io/blog/pdf-to-markdown-open-source-deep-dive/)

## Requirements

- Python 3.10+
- ~5GB RAM（Marker 模型；GPU 加速建議但非必須）
- 首次執行下載 ~2GB Marker 模型到 `~/.cache/`
- API mode：一把 API key

## 安全提醒

- ⚠️ 絕對不要把 API key commit 到 git。本 repo `.gitignore` 已擋 `.claude/settings.local.json`、`.env`、`*.key`
- ⚠️ 若不慎洩露 key，立刻到供應商後台撤銷並產新的
- ✅ 公開文件用 CLI mode 最安全（零 API 呼叫、零資料外洩風險）
- ✅ 機密文件走 API mode 時務必用 **公司內部地端 AI**，不要送到公開雲端

## License

MIT
