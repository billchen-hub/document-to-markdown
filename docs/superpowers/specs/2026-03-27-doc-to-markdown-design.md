# Doc to Markdown - 設計規格書

## 概述

將技術規格書 PDF（如 UFS 儲存裝置 SPEC）轉換為高品質 Markdown 檔案，供公司地端模型做 RAG 使用。採用 Hybrid 方案：Marker 開源工具為主、Claude Vision API 補強品質不佳的頁面。

## 目標

- 將 PDF 規格書（含表格、圖片）轉為結構化 Markdown
- 按章節拆分輸出，控制在 100 份以內（預期 20-40 份）
- 圖片轉為文字描述（最利於 RAG 檢索）
- 自動生成每份文件的 description，方便匯入 RAG 知識庫
- 設計為可重複使用的 CLI 工具，換 PDF 只需一行指令

## 整體架構

```
doc_to_markdown/
├── config.py              # 設定檔（閾值、路徑、預設模型）
├── main.py                # CLI 入口 + 主流程控制器
├── pdf_parser.py          # PDF 拆頁、圖片擷取、章節偵測
├── marker_converter.py    # Marker 基礎轉換
├── vision_converter.py    # Claude Vision API 轉換
├── quality_checker.py     # 品質檢查（規則 + 抽樣比對）
├── merger.py              # 按章節合併最終 Markdown
├── desc_generator.py      # Description 生成器
├── requirements.txt
├── USAGE.md               # 使用手冊
├── input/                 # 放 PDF 原檔
└── output/
    └── <pdf_name>/        # 自動以 PDF 檔名建立
        ├── chapters/      # 按章節輸出的 .md
        ├── descriptions/  # 每份 .md 的 description JSON
        ├── images/        # 擷取的頁面圖片（供 Vision API 用）
        ├── catalog.json   # 總索引
        ├── quality_report.json
        ├── conversion_log.json
        ├── progress.json  # 斷點續跑進度
        └── README.md      # 本次轉換結果摘要
```

## 主流程（Pipeline）

```
1. PDF 解析 → 拆頁、偵測章節邊界、擷取圖片區域位置
2. Marker 轉換 → 全部頁面跑一遍
3. 品質檢查-規則 → 掃描每頁：亂碼率、空表格、圖片區域缺文字
4. 品質檢查-抽樣 → 隨機抽 ~30 頁送 Vision API 比對
5. Vision 補強 → 問題頁重做 + 圖片頁描述
6. 合併輸出 → 按章節組合成最終 .md
7. Description 生成 → 為每份 .md 生成摘要與關鍵字
8. 文件生成 → 產出 catalog.json、README.md
```

每一步都會產出中間結果並儲存，支援斷點續跑。

## CLI 介面

```bash
# 基本轉換（一行搞定）
python main.py input/ufs_spec.pdf

# 指定輸出目錄
python main.py input/ufs_spec.pdf -o output/ufs_v4

# 調整 Vision API 模型（預設 claude-sonnet-4-20250514）
python main.py input/ufs_spec.pdf --model claude-sonnet-4-20250514

# 全 Vision 模式（跳過 Marker）
python main.py input/ufs_spec.pdf --full-vision

# 從斷點續跑
python main.py input/ufs_spec.pdf --resume

# 只重新生成 Description
python main.py input/ufs_spec.pdf --desc-only
```

設定優先順序：CLI 參數 > config.py 預設值

API Key 從環境變數 `ANTHROPIC_API_KEY` 讀取，不存放在程式碼中。

## 章節拆分策略

- 以 PDF 目錄（TOC）的頂層章節為主要切分點
- 如果某章節超長（超過 50 頁），按次級標題拆分
- 如果某章節過短（不到 2 頁），與相鄰章節合併
- 附錄（Appendix）各自獨立一份
- 預期產出：20-40 份 .md

如果章節數超過 100 份，發出警告並建議調整拆分粒度。

## Description 生成

每份 .md 自動生成對應的 description JSON：

```json
{
  "file": "01_introduction.md",
  "title": "Chapter 1: Introduction",
  "description": "UFS 4.0 規格書簡介，涵蓋規格目的、適用範圍、術語定義、參考標準列表。適合在需要了解 UFS 規格的整體範圍或查詢特定術語定義時使用。",
  "keywords": ["UFS", "scope", "terminology", "references"],
  "page_range": "1-12"
}
```

生成方式：用 Claude API 讀取每份 .md 內容，一次 prompt 產出 description + keywords。

彙整為 `catalog.json`，包含所有檔案的 description，方便一次匯入 RAG 知識庫。

## 品質檢查機制

### 第一層：規則掃描（本地，不花 API）

| 規則 | 判定條件 | 動作 |
|------|---------|------|
| 亂碼偵測 | 非 ASCII 可印字元比例 > 5% | 標記重做 |
| 空表格 | 偵測到表格區域但 Markdown 表格為空或只有 header | 標記重做 |
| 圖片區域 | PDF 中有圖片但 Markdown 無對應內容 | 標記需 Vision 描述 |
| 內容過短 | 某頁 PDF 有內容但輸出不到 50 字 | 標記重做 |
| 格式破損 | Markdown 語法錯誤（未閉合表格、斷裂的標題） | 標記重做 |

### 第二層：抽樣比對（用 API）

- 隨機抽 ~30 頁（約 5-6%），送 Vision API 取得「標準答案」
- 逐頁比較 Marker 輸出 vs Vision 輸出的結構相似度（標題數、表格行數、內容長度比）
- 相似度低於 70% 視為該頁品質不合格
- 如果某類頁面（如含表格頁、含圖片頁）不合格率超過 50%，該類型頁面全部用 Vision 重做

### 品質報告

```json
{
  "total_pages": 542,
  "marker_ok": 380,
  "vision_redo": 120,
  "vision_image_desc": 42,
  "issues": [
    {"page": 15, "reason": "empty_table", "method": "vision_redo"},
    {"page": 23, "reason": "image_region", "method": "vision_describe"}
  ]
}
```

## 斷點續跑機制

### 進度檔 progress.json

```json
{
  "status": "in_progress",
  "current_step": "vision_redo",
  "pages": {
    "1": {"marker": "done", "quality": "pass", "vision": "skip"},
    "15": {"marker": "done", "quality": "fail:empty_table", "vision": "done"},
    "23": {"marker": "done", "quality": "fail:image_region", "vision": "pending"}
  },
  "stats": {
    "marker_completed": 542,
    "quality_checked": 542,
    "vision_total": 162,
    "vision_completed": 89,
    "vision_pending": 73,
    "tokens_used": {"input": 280000, "output": 120000},
    "estimated_cost": "$3.42"
  }
}
```

### 行為

- 每頁處理完即時更新 progress.json
- `--resume` 時讀取進度，自動跳過已完成的步驟和頁面
- 偵測到既有 progress.json 時提示使用者選擇續跑或重新開始
- Rate limit 時指數退避重試（最多 3 次），超過則暫停並儲存進度

### Console 輸出

```
[Step 1/8] PDF parsing: 542 pages, 24 chapters detected ✓
[Step 2/8] Marker conversion: 542/542 pages ✓
[Step 3/8] Quality check (rules): 542/542 pages ✓
           → 120 pages need redo, 42 need image description
[Step 4/8] Quality check (sampling): 30/30 pages ✓
           → 12 additional pages flagged
[Step 5/8] Vision API: 89/162 pages...
           ⏳ Rate limited, retrying in 30s...
[Step 6/8] Merging chapters: 24/24 ✓
[Step 7/8] Generating descriptions: 24/24 ✓
[Step 8/8] Writing catalog & README ✓
```

## 錯誤處理

### API 相關

| 情況 | 處理 |
|------|------|
| Rate limit (429) | 指數退避重試，最多 3 次，超過則暫停存進度 |
| API key 無效 | 啟動時即檢查，失敗直接報錯退出 |
| 回應格式異常 | 記錄原始回應，標記該頁為 error，不阻斷流程 |
| 單頁 token 超限 | 將頁面裁切為上下半頁分別處理，再合併 |

### PDF 解析相關

| 情況 | 處理 |
|------|------|
| 無 TOC / 目錄結構不清 | 退回以頁碼範圍均分章節，或偵測 heading 字型大小推斷結構 |
| 掃描型 PDF（純圖片無文字層） | 自動偵測，該頁全部走 Vision API |
| 加密 / 有密碼的 PDF | 啟動時檢查，提示使用者提供密碼或解鎖 |
| 跨頁表格 | Marker 輸出比對前後頁表格 header，嘗試合併 |

### 輸出相關

| 情況 | 處理 |
|------|------|
| 章節數超過 100 | 發出警告，建議調整拆分粒度 |
| 單一 .md 檔案過大（> 200KB） | 發出警告，建議拆分 |
| 磁碟空間不足 | 每步驟前檢查，提前報錯 |

所有錯誤記錄在 conversion_log.json，不靜默失敗。

## 技術選型

### Python 3.10+

### 核心依賴

| 套件 | 用途 |
|------|------|
| `marker-pdf` | PDF → Markdown 基礎轉換 |
| `anthropic` | Claude Vision API 呼叫 |
| `PyMuPDF (fitz)` | PDF 拆頁、圖片擷取、TOC 讀取 |
| `Pillow` | 頁面轉圖片供 Vision API |
| `click` | CLI 介面 |

### 選型理由

- Marker 而非 PyMuPDF4LLM：Marker 對表格和技術文件的還原度明顯更好
- PyMuPDF 仍需要：用於 PDF 元資訊擷取（TOC、頁數、圖片區域偵測）
- Click 而非 argparse：語法更簡潔，自動生成 --help
- 不用 LangChain / LlamaIndex：邏輯直接，不需要額外抽象層

## 成本估算

以 Claude Sonnet 4 為例（Hybrid 方案，約 200 頁需 Vision API）：

| 項目 | 估算 |
|------|------|
| Input（圖片+指令） | ~400K tokens → ~$1.2 |
| Output（Markdown） | ~300K tokens → ~$4.5 |
| Description 生成 | ~$1-2 |
| **合計** | **~$7-10** |

如果 Sonnet 品質不符預期，可升級至 Opus（成本約 5 倍，~$35-50）。使用者已同意預算可彈性調整。
