# SCSI Block Commands - 4 (SBC-4) Rev 22 Conversion Results

- Total pages: 447
- Total chapters: 76
- Marker converted: 447 pages
- Vision API redo: 1 pages
- Vision image descriptions: 0 pages

## Chapters

### Points of contact (pages 2-2)

**File:** `01_points_of_contact.md`

列出 INCITS T10 技術委員會的聯絡資訊，包含 T10 Chair、Vice-Chair、秘書處地址、郵件反映器與標準購買管道。屬於行政資訊頁，對 RAG 查詢標準制定單位、聯絡窗口或提交 proposal 的流程時有用。

**Keywords:** incits, t10-committee, contacts, secretariat, standards-body

### Abstract (pages 3-4)

**File:** `02_abstract.md`

SBC-4 規格摘要：定義 SCSI Block Commands - 4 的功能需求，允許 rigid disk 等 SCSI block 邏輯單元連接電腦並提供使用定義。與 SBC-3 (INCITS 514-2014) 保持高度相容。包含 ANSI 正式核准說明、版權聲明與專利告知。

**Keywords:** sbc-4, abstract, ansi-approval, backward-compatibility, sbc-3, logical-unit

### Revision History (pages 5-10)

**File:** `03_revision_history.md`

SBC-4 從 Revision 0 (2014-02) 到 Revision 22 的全部修訂紀錄，逐版列出被合併的 proposal 編號與變更內容，包含 WRITE SAME、SANITIZE、unmap、zoned block、protection information 等關鍵功能的演進。查「某個功能什麼時候加入」時查這裡。

**Keywords:** revision-history, change-log, sbc-4-proposals, version-tracking, working-group

### Contents (pages 11-22)

**File:** `04_contents.md`

SBC-4 文件目錄，依章節編號列出所有 clause、subclause 的標題與頁碼，涵蓋 scope、definitions、direct access block device model、命令定義、mode/log pages、VPD pages 等全部主題。可作為全書導覽索引。

**Keywords:** table-of-contents, index, clause-listing, navigation

### Tables (pages 23-30)

**File:** `05_tables.md`

SBC-4 全文件的表格清單索引，列出所有表格編號、標題與所在頁碼。適合快速查找特定資料格式表格（例如 CDB 欄位表、sense code 表、VPD page 格式表）的位置。

**Keywords:** table-index, list-of-tables, navigation, figures-reference

### SCSI standards family (pages 31-33)

**File:** `06_scsi_standards_family.md`

說明 SBC-4 在整個 SCSI 標準家族中的定位，包含 SAM-6 架構模型、SPC-6 共用命令集、Device-type 特定命令集 (如 MMC-6、ZBC、SSC)、transport protocols (SPL、FCP) 與 interconnects (SAS、Fibre Channel) 的層級關係。Clause 1 Scope 與 Clause 2 Normative references 也在此章。

**Keywords:** scsi-architecture, sam-6, spc-6, standards-hierarchy, normative-references, scope

### Definitions, symbols, abbreviations, keywords, and conventions (pages 34-52)

**File:** `07_3_definitions_symbols_abbreviations_keywords_and_conventions.md`

SBC-4 用到的所有術語定義（atomic write、LBA、CDB、logical block、protection information 等百餘個）、符號、縮寫、關鍵字（shall/should/may）與編輯/數字/狀態機表示慣例。查技術名詞含意時首選此章。

**Keywords:** definitions, terminology, glossary, conventions, keywords, state-machine-notation

### 4.6 Physical blocks (pages 53-56)

**File:** `08_46_physical_blocks.md`

描述 physical block 與 logical block 的關係，說明 SBC-4 如何處理 512e/4Kn 等 512-byte logical block 對應 4096-byte physical block 的 alignment、offset 與 performance 影響。在做 advanced format 硬碟或做對齊分析時參考此章。

**Keywords:** physical-block, logical-block, advanced-format, alignment, 512e, 4kn

### 4.7 Logical block provisioning (pages 57-73)

**File:** `09_47_logical_block_provisioning.md`

SBC-4 thin provisioning 模型核心章節。定義 mapped / deallocated / anchored 三種 LBA 狀態、unmap 操作、WRITE SAME 觸發 unmap 的條件、LBPRZ（deallocated 讀回零）行為、與 Logical Block Provisioning VPD/log pages。做 TRIM、thin-provisioned SSD、或 storage array 時最常參考。

**Keywords:** thin-provisioning, unmap, deallocated, anchored, lbprz, trim

### 4.11 Sanitize operations (pages 74-76)

**File:** `10_411_sanitize_operations.md`

Sanitize（安全清除）功能模型，定義 overwrite、block erase、crypto erase、exit failure mode 四種服務動作的語意，以及 sanitize 期間裝置的行為限制（disallow I/O、AUSE 旗標、失敗恢復）。合規需求如 NIST 800-88 purge 對應 SCSI 實作時查此章。

**Keywords:** sanitize, secure-erase, crypto-erase, block-erase, overwrite, data-destruction

### 4.13 Medium defects (pages 77-79)

**File:** `11_413_medium_defects.md`

定義 primary defect list (PLIST)、grown defect list (GLIST)、certified list (CLIST) 的概念、REASSIGN BLOCKS 的 remapping 機制、以及 automatic/manual read/write reassignment 的行為。做硬碟壞軌處理、defect 統計分析或 RAID 重建診斷時用此章。

**Keywords:** defect-list, plist, glist, reassign-blocks, bad-sector, remapping

### 4.15 Caches (pages 80-83)

**File:** `12_415_caches.md`

定義 logical unit 的 read cache、write cache 行為、FUA (Force Unit Access) 位元對 cache bypass 的影響、SYNCHRONIZE CACHE 命令的語意、以及 cache 與 volatile/non-volatile 儲存的關係。效能調校（WCE mode page、write-back vs write-through）與資料一致性相關問題看此章。

**Keywords:** cache, write-cache, read-cache, fua, synchronize-cache, wce

### 4.17 Reservations (pages 84-85)

**File:** `13_417_reservations.md`

SBC-4 對 persistent reservations 的特定補充（主體定義在 SPC-6），說明在 direct access block device 上 reservation hold 時哪些命令被 allowed / conflict。做 cluster shared storage、failover、I/O fencing 時用此章確認命令行為。

**Keywords:** persistent-reservation, i-o-fencing, cluster-storage, reservation-conflict

### 4.18 Error reporting (pages 86-92)

**File:** `14_418_error_reporting.md`

block device 特有的錯誤回報機制：sense key、additional sense code (ASC/ASCQ) 組合、INFORMATION field 用法（存 LBA）、deferred error 的處理、以及 error recovery flags (PER、DCR、DTE) 的行為。debug SCSI 錯誤時第一站。

**Keywords:** sense-data, asc-ascq, deferred-error, error-recovery, per, dte

### 4.19 Rebuild assist mode (pages 93-95)

**File:** `15_419_rebuild_assist_mode.md`

定義 rebuild assist mode — 當 RAID array 重建時，device 回報「哪些 LBA 尚有可讀性」讓 RAID controller 只重建必要的範圍，加速重建並避免 read hard errors 干擾。配合 GET LBA STATUS 使用。做 RAID controller、storage array 或 proactive failure handling 時用此章。

**Keywords:** rebuild-assist, raid-rebuild, get-lba-status, read-hard-error, proactive-failure

### 4.20 START STOP UNIT and power conditions (pages 96-107)

**File:** `16_420_start_stop_unit_and_power_conditions.md`

SBC-4 電源管理狀態機：定義 Active、Idle_a / Idle_b、Standby_y / Standby_z、Stopped 等狀態、對應的計時器與 transition 條件，以及 START STOP UNIT 命令與 Power Condition mode page 的互動。做省電策略、drive spin-up/spin-down、PCIe PM 整合時必看。

**Keywords:** power-conditions, start-stop-unit, idle, standby, power-management, spin-up

### 4.21 Protection information model (pages 108-118)

**File:** `17_421_protection_information_model.md`

T10 PI (Protection Information / DIF) 完整模型：每個 logical block 附 8 bytes 的 guard (CRC)、application tag、reference tag，定義 Type 1/2/3 的差異、CHECK 欄位行為、PI interval、以及 end-to-end data integrity 的保護範圍。做 enterprise storage、PI-capable HBA、DIX 整合時核心參考。

**Keywords:** protection-information, t10-pi, dif, dix, data-integrity, guard-tag, crc

### 4.23 Background scan operations (pages 119-123)

**File:** `18_423_background_scan_operations.md`

背景媒體巡檢機制：device 在閒置時自動 scan 整個 medium 尋找潛在 grown defect，並把結果寫入 Background Scan Results log page。搭配 Background Control mode page 設定 scan 行為。做 proactive disk health、predictive failure 分析或實作 DST (drive self-test) 整合時用此章。

**Keywords:** background-scan, media-scan, proactive-health, background-scan-log, dst

### 4.26 Referrals (pages 124-126)

**File:** `19_426_referrals.md`

Referrals 機制允許 logical unit 把 LBA 範圍的實際資料位置「轉介」到另一個 target port 或 logical unit，給多路徑、分層式 storage 使用。定義 user data segment、segment multiplier、referral sense code 行為。實作 virtualised storage、thin fabric 時會用到。

**Keywords:** referrals, data-location, user-data-segment, multipath, virtual-storage

### 4.27 ORWRITE commands (pages 127-129)

**File:** `20_427_orwrite_commands.md`

ORWRITE (16/32) 命令模型：把 Data-Out Buffer 的位元與 medium 上既有資料做 bitwise OR 後寫回，可用於合併 bitmap、無鎖更新旗標欄位等情境。搭配 expected initial logical block reference tag 驗證。適合 cluster 檔案系統或 dedup metadata 維護。

**Keywords:** orwrite, bitwise-or, atomic-bit-set, bitmap-merge

### 4.28 Block device ROD token operations (pages 130-132)

**File:** `21_428_block_device_rod_token_operations.md`

ROD (Representation of Data) token 子模型：block-device 如何建立 / 使用 ROD token 做 offloaded 資料搬移，包含 POPULATE TOKEN 與 WRITE USING TOKEN 的交互、token 存活期、inactivate 規則。Windows ODX / VMware XCOPY lite 的底層 SCSI 定義。

**Keywords:** rod-token, odx, offloaded-copy, populate-token, xcopy, token-lifecycle

### 4.29 Atomic writes (pages 133-135)

**File:** `22_429_atomic_writes.md`

Atomic write 模型：定義 maximum atomic transfer length、atomic alignment / granularity / boundary、atomic transfer length granularity 規則，以及單一命令內 all-or-nothing 寫入的保證。資料庫引擎（InnoDB、Postgres）與 journaling 檔案系統參考此章。

**Keywords:** atomic-write, all-or-nothing, atomic-boundary, database, torn-write

### 4.31 Background operation control (pages 136-137)

**File:** `23_431_background_operation_control.md`

Advanced background operations（例如 SSD garbage collection、wear leveling）的控制機制：透過 Background Operation Control mode page 啟用 / 暫停 / 查詢狀態，並由 Background Operation log page 回報進度。實作 host-controlled background tasks 時使用。

**Keywords:** advanced-background-operation, garbage-collection, wear-leveling, background-control-mode-page

### 4.32 Stream control (pages 138-139)

**File:** `24_432_stream_control.md`

Multi-stream 模型：host 用 STREAM CONTROL 命令開 / 關 stream，對 WRITE 命令帶 STR_ID 欄位讓 SSD 按 stream 分群存放。降低 write amplification、延長 SSD 壽命的關鍵功能。做 tiered storage、workload-aware SSD 時必看。

**Keywords:** streams, multi-stream, str-id, ssd-lifetime, write-amplification, data-placement

### 4.33 Format operations (pages 140-143)

**File:** `25_433_format_operations.md`

FORMAT UNIT / FORMAT WITH PRESET 命令的行為模型：format progress、cancel、failure mode、FMTDATA / IP / FMT_PINFO 欄位語意、以及如何在 format 過程中處理 defect list、logical block length、protection information。做工廠 format 或 re-provision 時核心章節。

**Keywords:** format-unit, format-preset, logical-block-length, fmtdata, protection-information-setup

### 4.35 Scattered writes (pages 144-146)

**File:** `26_435_scattered_writes.md`

WRITE SCATTERED 命令的模型：單一命令指定多個不連續 LBA range 做 vectored write，每個 range 可獨立設 protection information，並由 LBA range descriptor 描述。適合 snapshot restore、VM disk clone 等 sparse 寫入場景。

**Keywords:** scattered-write, vectored-write, lba-range-descriptor, sparse-write

### 4.36 Storage element depopulation and restoration (pages 147-151)

**File:** `27_436_storage_element_depopulation_and_restoration.md`

Depopulation 功能讓多碟片硬碟把部分故障的 head / platter 停用、保留剩餘容量繼續使用，避免整顆硬碟報廢。定義 REMOVE ELEMENT AND TRUNCATE / RESTORE ELEMENTS AND REBUILD 命令、depopulation revocable / persistent 狀態機。hyperscale 資料中心壽命延伸的關鍵功能。

**Keywords:** depopulation, remove-element, restore-elements, hyperscale, failure-recovery, multi-head-drive

### 5 Commands for direct access block devices (pages 152-156)

**File:** `28_5_commands_for_direct_access_block_devices.md`

Clause 5 總述：列出 SBC-4 定義的所有命令（opcode + service action）、CDB 長度、CDB 共同欄位（LOGICAL BLOCK ADDRESS、TRANSFER LENGTH、CONTROL、GROUP NUMBER），以及命令類別（READ / WRITE / VERIFY / UNMAP / ADMIN）。查命令對照表時用此章。

**Keywords:** command-reference, cdb, opcode, service-action, group-number

### 5.3 COMPARE AND WRITE command (pages 157-158)

**File:** `29_53_compare_and_write_command.md`

COMPARE AND WRITE (CAW, opcode 89h) 命令：先比對 Data-Out Buffer 前半與 medium 既有資料，相同才寫入後半資料，等同 SCSI 層級的 CAS (compare-and-swap)。VMware VAAI ATS (Atomic Test and Set)、cluster lock 使用。失敗會回傳 MISCOMPARE。

**Keywords:** compare-and-write, caw, ats, vaai, compare-and-swap, cluster-lock

### 5.4 FORMAT UNIT command (pages 159-166)

**File:** `30_54_format_unit_command.md`

FORMAT UNIT (opcode 04h) 完整 CDB 與參數列表格式、FMTDATA / CMPLST / DEFECT LIST FORMAT 欄位語意、IP / PIE / PI_EXPONENT 對 protection information 的設定、long / short header 格式差異。實作 low-level format、改變 logical block length、或設定 PI Type 時用此章。

**Keywords:** format-unit, cdb, fmtdata, protection-information-type, defect-list-format

### 5.5 FORMAT WITH PRESET command (pages 167-168)

**File:** `31_55_format_with_preset_command.md`

FORMAT WITH PRESET (opcode 38h) 命令：用 PRESET IDENTIFIER 套用預先定義的 format profile（logical block length、PI type、LBPRZ 行為等），不用手動指定所有參數。適合 device 有多組預設 configuration 的情境。

**Keywords:** format-with-preset, preset-identifier, format-profile, reformat

### 5.6 GET LBA STATUS (16) command (pages 169-172)

**File:** `32_56_get_lba_status_16_command.md`

GET LBA STATUS (16) (opcode 9Eh / SA 12h)：回報指定 LBA 起的 provisioning 狀態（mapped / deallocated / anchored），用於 thin-provisioning 客戶端查詢實際配置情形。包含 parameter data format、PROVISIONING STATUS 欄位、COMPLETION CONDITION。

**Keywords:** get-lba-status, provisioning-status, mapped, deallocated, thin-provisioning-query

### 5.7 GET LBA STATUS (32) command (pages 173-174)

**File:** `33_57_get_lba_status_32_command.md`

GET LBA STATUS (32) (opcode 7Fh / SA 0012h) 是 16-byte 版本的 32-byte variable-length 擴展，支援 protection information 欄位 (LBAT / LBATM / EATM) 的過濾比對。用於需要 PI 驗證的 LBA 狀態查詢。

**Keywords:** get-lba-status-32, variable-length-cdb, protection-information-filter

### 5.8 GET PHYSICAL ELEMENT STATUS command (pages 175-178)

**File:** `34_58_get_physical_element_status_command.md`

GET PHYSICAL ELEMENT STATUS (opcode 9Eh / SA 17h)：查詢多片 HDD 內每個 physical element（head/platter）的健康狀態、已 depopulate 與否、physical element ID。搭配 depopulation 功能。

**Keywords:** physical-element-status, physical-element-health, depopulation-query, multi-head-drive

### 5.9 GET STREAM STATUS command (pages 179-181)

**File:** `35_59_get_stream_status_command.md`

GET STREAM STATUS 命令：列出目前 logical unit 上開啟中的 stream ID 清單、每個 stream 的 status。用來在 stream 配額滿時決定該關哪個 stream、或重建 host 對 stream 的狀態。

**Keywords:** get-stream-status, stream-id-list, open-streams, stream-management

### 5.10 ORWRITE (16) command (pages 182-188)

**File:** `36_510_orwrite_16_command.md`

ORWRITE (16) (opcode 8Bh) 的完整 CDB 欄位：LOGICAL BLOCK ADDRESS、TRANSFER LENGTH、ORPROTECT、DPO、FUA、EXPECTED ORWGENERATION、ORWGENERATION。執行 bitwise OR 與 expected generation 驗證的命令定義。

**Keywords:** orwrite-16, cdb, orwgeneration, bitwise-or, orprotect

### 5.11 ORWRITE (32) command (pages 189-190)

**File:** `37_511_orwrite_32_command.md`

ORWRITE (32) (opcode 7Fh / SA 000Eh)：ORWRITE 的 32-byte variable-length CDB 版本，支援 PI 欄位與 expected initial reference tag 的完整比對。給需要 end-to-end PI 保護的 bit-set 操作使用。

**Keywords:** orwrite-32, variable-length-cdb, expected-reference-tag, pi-protected-or

### 5.12 POPULATE TOKEN command (pages 191-197)

**File:** `38_512_populate_token_command.md`

POPULATE TOKEN (opcode 83h / SA 10h) 建立 ROD token 代表一組來源 LBA 範圍的資料快照。CDB 欄位、LIST IDENTIFIER、ROD TYPE、inactivation timeout、block device range descriptor 格式。後續用 WRITE USING TOKEN 實現 server-side copy。

**Keywords:** populate-token, rod-token-create, xcopy-source, odx, server-side-copy

### 5.16 READ (10) command (pages 198-201)

**File:** `39_516_read_10_command.md`

READ (10) (opcode 28h) — 最常用的讀取命令：4-byte LBA + 2-byte TRANSFER LENGTH，CDB 包含 RDPROTECT、DPO、FUA、RARC、GROUP NUMBER 等欄位。定義 protection information check 規則、cache 行為、recovery 策略。幾乎所有 host-initiated read IO 的基礎。

**Keywords:** read-10, cdb, rdprotect, fua, dpo, rarc

### 5.17 READ (12) command (pages 202-205)

**File:** `40_517_read_12_command.md`

READ (12) (opcode A8h)：4-byte LBA + 4-byte TRANSFER LENGTH（支援更大單命令傳輸）。欄位與 READ (10) 相同但 transfer length 上限更大。也同時介紹 READ (16) / READ (32) 的對應差異。適合大區塊讀取場景。

**Keywords:** read-12, read-16, read-32, large-transfer, cdb

### 5.20 READ CAPACITY (10) command (pages 206-207)

**File:** `41_520_read_capacity_10_command.md`

READ CAPACITY (10) (opcode 25h)：回傳 logical unit 的最後 LBA 與 block length。受限於 32-bit LBA（2 TiB 上限）。超過則回 FFFFFFFFh 指引 host 改用 READ CAPACITY (16)。相容性命令。

**Keywords:** read-capacity-10, last-lba, block-length, capacity-query, 32-bit-lba-limit

### 5.21 READ CAPACITY (16) command (pages 208-209)

**File:** `42_521_read_capacity_16_command.md`

READ CAPACITY (16) (opcode 9Eh / SA 10h)：64-bit LBA + logical/physical block length、alignment、protection type、P_I_EXPONENT、LBPME / LBPRZ 旗標。是現代大容量 device 的標準 capacity query，也回傳 thin-provisioning / PI 支援狀態。

**Keywords:** read-capacity-16, 64-bit-lba, logical-physical-block, lbpme, lbprz, p-i-exponent

### 5.22 READ DEFECT DATA (10) command (pages 210-211)

**File:** `43_522_read_defect_data_10_command.md`

READ DEFECT DATA (10) (opcode 37h)：回傳 primary / grown defect list。DEFECT LIST FORMAT 欄位選 block / bytes from index / physical sector 三種格式。偏向舊款相容命令，大容量 drive 建議用 (12) 版本。

**Keywords:** read-defect-data-10, defect-list, plist, glist, defect-format

### 5.23 READ DEFECT DATA (12) command (pages 212-214)

**File:** `44_523_read_defect_data_12_command.md`

READ DEFECT DATA (12) (opcode B7h) 擴展版：4-byte allocation length 支援大量 defect 回傳、ADDRESS DESCRIPTOR INDEX 可做分頁查詢。做 full-drive defect 掃描統計與長壽 HDD 分析時使用。

**Keywords:** read-defect-data-12, defect-list-paging, address-descriptor-index, large-defect-list

### 5.24 REASSIGN BLOCKS command (pages 215-218)

**File:** `45_524_reassign_blocks_command.md`

REASSIGN BLOCKS (opcode 07h)：讓 host 主動要求 device 把一組 LBA 重 map 到備用區塊。LONGLBA / LONGLIST / DEFECT LIST 欄位語意，以及 reassign 失敗後的 sense data。修復已知壞軌或 refresh 磁性衰弱區塊的手動介入命令。

**Keywords:** reassign-blocks, manual-remap, bad-block, spare-block, longlba

### 5.25 RECEIVE ROD TOKEN INFORMATION (pages 219-223)

**File:** `46_525_receive_rod_token_information.md`

RECEIVE ROD TOKEN INFORMATION (opcode 84h / SA 07h)：查詢 POPULATE TOKEN 建立的 token 目前狀態、進度、complete 與否。offloaded copy 的進度回報機制。

**Keywords:** receive-rod-token-information, token-status, odx-progress, xcopy-status

### 5.28 REPORT REFERRALS command (pages 224-225)

**File:** `47_528_report_referrals_command.md`

REPORT REFERRALS (opcode 9Eh / SA 13h)：回傳 logical unit 上所有 referrals（即 LBA 範圍被 redirect 到其他 target 的對應表），給 multipath / virtualization layer 建 routing 表使用。

**Keywords:** report-referrals, multipath, lba-redirect, virtual-storage-routing

### 5.29 RESTORE ELEMENTS AND REBUILD command (pages 226-227)

**File:** `48_529_restore_elements_and_rebuild_command.md`

RESTORE ELEMENTS AND REBUILD (opcode 9Eh / SA 19h)：把先前 depopulated 的 physical element 重新啟用並重新 rebuild logical capacity。CDB 欄位與執行期間的限制。depopulation 配對命令。

**Keywords:** restore-elements-and-rebuild, depopulation-reverse, physical-element-restore, rebuild-capacity

### 5.30 SANITIZE command (pages 228-231)

**File:** `49_530_sanitize_command.md`

SANITIZE (opcode 48h) 完整 CDB：SERVICE ACTION (OVERWRITE / BLOCK ERASE / CRYPTO ERASE / EXIT FAILURE MODE)、AUSE / ZNR / IMMED 旗標、parameter list 格式。做資料抹除合規實作（NIST 800-88 purge）的實際命令定義。

**Keywords:** sanitize-command, cdb, service-action, ause, znr, immed, secure-erase

### 5.31 START STOP UNIT command (pages 232-234)

**File:** `50_531_start_stop_unit_command.md`

START STOP UNIT (opcode 1Bh) CDB：POWER CONDITION、POWER CONDITION MODIFIER、LOEJ、START、NO_FLUSH 欄位。驅動 device 在 Active / Idle / Standby / Stopped 間切換的實際命令。

**Keywords:** start-stop-unit, cdb, power-condition, loej, no-flush, spin-control

### 5.32 STREAM CONTROL command (pages 235-236)

**File:** `51_532_stream_control_command.md`

STREAM CONTROL (opcode 9Eh / SA 14h)：host 發 OPEN / CLOSE action 建立或關閉 stream，device 回傳分配的 stream ID。multi-stream SSD 的控制面命令。

**Keywords:** stream-control-command, open-stream, close-stream, stream-id-allocation

### 5.33 SYNCHRONIZE CACHE (10) command (pages 237-239)

**File:** `52_533_synchronize_cache_10_command.md`

SYNCHRONIZE CACHE (10) (opcode 35h)：強制把 write cache 中指定 LBA 範圍的資料 flush 到 medium，確保 durability。IMMED 旗標控制同步 / 非同步回應、NV_DIS 控制 non-volatile cache 行為。也包含 SYNCHRONIZE CACHE (16) 差異說明。

**Keywords:** synchronize-cache, cache-flush, durability, fsync, immed, nv-dis

### 5.35 UNMAP command (pages 240-241)

**File:** `53_535_unmap_command.md`

UNMAP (opcode 42h)：告訴 device 指定 LBA 範圍的資料不再需要，允許 deallocate 對應 physical storage。UNMAP block descriptor list 格式、granularity alignment 規則。SSD TRIM 在 SCSI 世界的對應命令，thin-provisioning 必備。

**Keywords:** unmap, trim, deallocation, unmap-block-descriptor, thin-provisioning

### 5.36 VERIFY (10) command (pages 242-258)

**File:** `54_536_verify_10_command.md`

VERIFY 命令家族（10/12/16/32）：只驗證資料可讀 / 比對 Data-Out Buffer，不回傳 logical block data 到 host。BYTCHK 欄位（0/1/3）決定純 medium check、byte-by-byte compare、或 logical block 比對模式。做 background scrub、integrity check 時用。

**Keywords:** verify-10, verify-16, bytchk, medium-scrub, integrity-check, data-compare

### 5.40 WRITE (10) command (pages 259-272)

**File:** `55_540_write_10_command.md`

WRITE 命令家族核心：WRITE (10)(opcode 2Ah)、以及 WRITE (12/16/32) 的 CDB 差異。欄位包含 WRPROTECT、DPO、FUA、FUA_NV、GROUP NUMBER。定義 protection information 寫入行為、cache 策略、overlapping range 規則。所有 write IO 的基礎。

**Keywords:** write-10, write-16, write-32, cdb, wrprotect, fua-nv, group-number

### 5.52 WRITE SAME (10) command (pages 273-276)

**File:** `56_552_write_same_10_command.md`

WRITE SAME (10) (opcode 41h)：把 Data-Out Buffer 的一個 logical block pattern 重複寫到指定 LBA 範圍，典型用途是「零填 / 格式化 free space」。搭配 UNMAP bit 或 ANCHOR bit 可觸發 unmap 或 anchor 操作。16 / 32 bit variable-length 版本也說明。

**Keywords:** write-same-10, zero-fill, unmap-bit, anchor-bit, pattern-fill

### 5.54 WRITE SAME (32) command (pages 277-278)

**File:** `57_554_write_same_32_command.md`

WRITE SAME (32) (opcode 7Fh / SA 000Dh) 是 variable-length CDB 版本，支援完整 PI 欄位（EXPECTED_INITIAL_LBAT / LBATM / EATM）與 NDOB (No Data-Out Buffer) 旗標。PI-aware zero-fill 場景使用。

**Keywords:** write-same-32, variable-length-cdb, ndob, pi-aware-zero-fill

### 5.55 WRITE SCATTERED (16) command (pages 279-282)

**File:** `58_555_write_scattered_16_command.md`

WRITE SCATTERED (16) (opcode 9Fh / SA 11h) 完整 CDB：BUFFER TRANSFER LENGTH、LBA RANGE DESCRIPTOR 陣列、WRPROTECT / DPO / FUA 欄位、scatter gather 風格的多區段 write 定義。

**Keywords:** write-scattered-16, cdb, lba-range-descriptor, vectored-write

### 5.56 WRITE SCATTERED (32) command (pages 283-285)

**File:** `59_556_write_scattered_32_command.md`

WRITE SCATTERED (32) (opcode 7Fh / SA 0011h)：variable-length 版本，LBA range descriptor 支援完整 PI 欄位、expected reference tag。做 PI-protected sparse write 時使用。

**Keywords:** write-scattered-32, variable-length-cdb, pi-protected-scatter

### 5.58 WRITE STREAM (32) command (pages 286-287)

**File:** `60_558_write_stream_32_command.md`

WRITE STREAM (32)：帶 STR_ID 欄位的寫入命令，讓 SSD 按 stream 分群資料放置。包含 WRITE STREAM (16)(opcode 9Ah) 與 (32) 差異。multi-stream SSD 的資料 IO 命令。

**Keywords:** write-stream, str-id, multi-stream-write, ssd-data-placement

### 5.59 WRITE USING TOKEN command (pages 288-291)

**File:** `61_559_write_using_token_command.md`

WRITE USING TOKEN (opcode 83h / SA 11h)：用先前 POPULATE TOKEN 建立的 ROD token 作為來源，把資料寫到目的 LBA。CDB 欄位、LIST IDENTIFIER、目的 LBA range descriptor 格式。ODX 的目的端命令。

**Keywords:** write-using-token, rod-token-consume, odx-destination, xcopy-write

### 6 Parameters for direct access block devices (pages 292-297)

**File:** `62_6_parameters_for_direct_access_block_devices.md`

Clause 6 總述 SBC-4 定義的所有 block device 相關 parameters，涵蓋 diagnostic、log、mode、VPD pages 四大類。列出 block-specific 參數頁的編號對照。要查某個 mode/log/VPD 頁的內容時從此章切入。

**Keywords:** parameters-overview, mode-pages, log-pages, vpd-pages, diagnostic-parameters

### 6.3 Diagnostic parameters (pages 298-302)

**File:** `63_63_diagnostic_parameters.md`

block device 的 diagnostic pages 定義：Translate Address page、Supported Diagnostic Pages、Self-Test page。SEND DIAGNOSTIC / RECEIVE DIAGNOSTIC RESULTS 命令搭配使用。做硬碟自我診斷、address translation 驗證時參考。

**Keywords:** diagnostic-pages, translate-address, self-test, send-diagnostic, receive-diagnostic-results

### 6.4 Log parameters (pages 303-339)

**File:** `64_64_log_parameters.md`

block device 所有 log pages 詳細定義，包含 Format Status、LBA Status、Logical Block Provisioning、Non-Volatile Cache、Background Scan、Background Operation、Solid State Media、Utilization、Zoned Block Device Statistics、Defect 相關 log pages。做 device 健康監控、SMART 等價查詢、long-term wear 追蹤時的主要資訊來源。本書最長的章節之一。

**Keywords:** log-pages, smart, background-scan-log, solid-state-media, utilization, lba-status-log

### 6.5 Mode parameters (pages 340-368)

**File:** `65_65_mode_parameters.md`

完整 mode pages 定義：Read-Write Error Recovery、Verify Error Recovery、Caching、Rigid Disk Geometry、Flexible Disk、Format Device、Notch and Partition、Power Condition、Application Tag、Background Control、Logical Block Provisioning、IO Advice Hints Grouping、Background Operation Control mode page。設定 device behavior tuning 的控制介面。

**Keywords:** mode-pages, caching-mode-page, read-write-error-recovery, power-condition, io-advice-hints, background-control

### 6.6 Vital product data (VPD) parameters (pages 369-392)

**File:** `66_66_vital_product_data_vpd_parameters.md`

SBC-4 定義的 VPD pages：Block Device Characteristics (B1h)、Block Limits (B0h)、Logical Block Provisioning (B2h)、Referrals (B3h)、Supported Block Lengths and Protection Types (B4h)、Block Device Characteristics Extension (B5h)、Zoned Block Device Characteristics (B6h)、Format Presets (B7h)、Concurrent Positioning Ranges (B9h) 等。INQUIRY 命令取得 device capability 的主要資料源。實作 capability discovery 必讀。

**Keywords:** vpd-pages, block-limits, block-device-characteristics, supported-block-lengths, format-presets, concurrent-positioning-ranges

### 6.8 Logical block markup descriptors (pages 393-398)

**File:** `67_68_logical_block_markup_descriptors.md`

Logical Block Markup descriptor 格式：host 對 LBA 打標記（IO hints、tag），device 可用這些資訊做 data placement 優化。跟 IO Advice Hints 搭配的 metadata 格式。

**Keywords:** logical-block-markup, lb-markup-descriptor, io-hints, data-placement-hint

### Numeric order codes (Annex) (pages 398-400)

**File:** `68_numeric_order_codes.md`

依 opcode / service action 數值順序列出 SBC-4 所有命令的對照表，給 firmware / driver 開發做逆向查詢（看到 opcode 想知道是哪個命令）使用。

**Keywords:** opcode-table, command-code-lookup, annex-numeric-order, reverse-reference

### CRC example in C (Annex) (pages 400-403)

**File:** `69_crc_example_in_c.md`

附錄：Protection Information GUARD 欄位所用 CRC-16-T10-DIF 多項式的 C 語言參考實作範例碼。實作 PI-aware software / firmware 驗證時用來對 CRC 結果。

**Keywords:** crc-16-t10-dif, crc-example, c-code, guard-computation, annex

### Optimizing block access characteristics (Annex) (pages 403-407)

**File:** `70_optimizing_block_access_characteristics.md`

附錄：教 host / driver 如何利用 Block Limits VPD (optimal transfer length、optimal read / write granularity) 與 Block Device Characteristics VPD 的參數來優化 IO pattern、與 device preferred access pattern 對齊。效能調校實務指南。

**Keywords:** block-limits, optimal-transfer-length, io-alignment, performance-tuning, annex

### Logical block provisioning reporting examples (Annex) (pages 407-419)

**File:** `71_logical_block_provisioning_reporting_examples.md`

附錄：對 thin-provisioning 相關 log / mode / VPD / GET LBA STATUS 的實際數值範例，包含 threshold 觸發、mapped / deallocated 比例變化的報表樣本。做 LBP 客戶端實作或 debug 時對照使用。

**Keywords:** logical-block-provisioning, examples, threshold-event, lba-status-examples, annex

### Discovering referrals examples (Annex) (pages 419-423)

**File:** `72_discovering_referrals_examples.md`

附錄：用 REPORT REFERRALS 與相關 log page 發現 logical unit 上 referrals 分布、user data segment 邊界對應的操作流程範例。給 multipath / virtualization stack 實作參考。

**Keywords:** referrals, discover-examples, user-data-segment, multipath-discovery, annex

### IO advice hints usage (Annex) (pages 423-427)

**File:** `73_io_advice_hints_usage.md`

附錄：IO Advice Hints Grouping mode page 的使用範例，說明 host 怎麼對每個 IO 指定 access frequency / latency priority / cache retention 等 hint，device 如何據此調整 cache / placement 策略。效能 hint 機制的實務指南。

**Keywords:** io-advice-hints, cache-hint, access-frequency, latency-priority, annex

### SBC feature sets (Annex) (pages 427-441)

**File:** `74_sbc_feature_sets.md`

附錄：定義幾組常見「feature set」標籤（例如 BASIC、COMMAND DURATION LIMITS、ZBC 相容、THIN PROVISIONING、FORMAT PRESET），列出每組 feature set 要求實作的必要命令、mode pages、VPD pages 的清單。做相容性合規聲明時用。

**Keywords:** feature-sets, compliance, basic-feature-set, thin-provisioning-feature, mandatory-commands

### Rebuild assist using the GET LBA STATUS command (Annex) (pages 441-443)

**File:** `75_rebuild_assist_using_the_get_lba_status_command.md`

附錄：示範 RAID controller 如何結合 Rebuild Assist mode 與 GET LBA STATUS 命令，找出 failing drive 上仍可讀取的 LBA、跳過已知受損 LBA，加速 RAID rebuild。RAID 韌體工程師實用範例。

**Keywords:** rebuild-assist, get-lba-status, raid-rebuild-examples, proactive-copy, annex

### Direct access block devices with shared resources (Annex) (pages 443-447)

**File:** `76_direct_access_block_devices_with_shared_resources.md`

附錄：討論多個 direct access block device 共用底層資源（例如單一 media、SoC 共用 controller）時的命令交互、resource contention 處理、target 行為。virtualised storage enclosure / 多 LUN 裝置參考。

**Keywords:** shared-resources, multi-lun, resource-contention, virtualised-storage, annex
