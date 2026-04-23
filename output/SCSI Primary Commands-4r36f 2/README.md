# SCSI Primary Commands-4r36f 2 Conversion Results

- Total pages: 1012
- Total chapters: 102
- Marker converted: 1012 pages
- Vision API redo: 0 pages
- Vision image descriptions: 0 pages

## Chapters

### ASC & ASCQ (pages 154-154)

**File:** `01_asc_ascq.md`

SPC-4 前置小節，開啟 Additional Sense Code / Additional Sense Code Qualifier 的完整定義。ASC/ASCQ 是 SCSI sense data 的錯誤細分標識，所有 SCSI device 共用。

**Keywords:** asc, ascq, sense-code, error-reporting, sense-data

### Default Bookmark (pages 154-174)

**File:** `02_default_bookmark.md`

SPC-4 前段落內容（版權、引言、基本術語、一般原則章節）。包含 scope、normative references、conventions 與 SCSI model 基本概念的一部分。

**Keywords:** spc-4-intro, scope, normative-references, conventions, preface

### 5.3.2 Suspending and resuming device-specific background functions (pages 175-180)

**File:** `03_532_suspending_and_resuming_device-specific_background_funct.md`

定義 host 如何暫停 / 恢復 device-specific background function（例如 garbage collection、background scan）以避免影響前景 IO latency。搭配對應 log/mode pages 使用的行為規則。

**Keywords:** background-function-control, suspend-resume, latency-management, io-priority

### 5.5.2 Retrieving error history with the READ BUFFER command (pages 181-182)

**File:** `04_552_retrieving_error_history_with_the_read_buffer_command.md`

用 READ BUFFER 搭配 error history mode 下載 device 保存的錯誤歷史 log（類似 firmware debug dump）的流程。做 RMA 分析、failure diagnostic 時用。

**Keywords:** read-buffer, error-history, firmware-dump, diagnostic-data, rma-analysis

### 5.5.4 Clearing error history with the WRITE BUFFER command (pages 183-186)

**File:** `05_554_clearing_error_history_with_the_write_buffer_command.md`

用 WRITE BUFFER 在 error history mode 下清除 device 的錯誤歷史紀錄或將 history export / import。搭配 READ BUFFER 完成 error history 生命週期管理。

**Keywords:** write-buffer, clear-error-history, error-history-management

### 5.11.2 REQUEST SENSE pollable sense data (pages 187-192)

**File:** `06_5112_request_sense_pollable_sense_data.md`

REQUEST SENSE 命令的 pollable (asynchronous) sense data 模型：host 可週期性 poll device 取得最新狀態、pending deferred error、background condition。autosense 機制的基礎。

**Keywords:** request-sense, pollable-sense, deferred-error, autosense

### 5.12.8 Power condition state machine (pages 193-199)

**File:** `07_5128_power_condition_state_machine.md`

完整電源狀態機：Active、Idle_a/b/c、Standby_y/z、Stopped 之間的所有合法 transition，以及 timer 觸發、命令驅動、error 回復的 state 變換規則。所有 SCSI device 的通用電源模型。

**Keywords:** power-state-machine, active, idle, standby, stopped, power-transitions

### 5.13.1 Persistent Reservations overview (pages 200-205)

**File:** `08_5131_persistent_reservations_overview.md`

Persistent Reservation 架構總覽：reservation type（Write Exclusive、Exclusive Access、各種 Registrants Only / All Registrants 變體）、reservation key、holder、PERSISTENT RESERVE IN/OUT 的基本機制。cluster shared storage、WSFC、VMware 的 fencing 基礎。

**Keywords:** persistent-reservation, reservation-type, cluster-fencing, scsi-3-pr, mpio

### 5.13.5 Preserving persistent reservations and registrations (pages 206-208)

**File:** `09_5135_preserving_persistent_reservations_and_registrations.md`

在 bus reset / power cycle / LUN reset 等事件下 reservation 與 registration 是否保留的規則。APTPL (Activate Persist Through Power Loss) 旗標行為。高可用性 cluster 設計必須理解的持久性語意。

**Keywords:** persistent-reservation, aptpl, persist-through-power-loss, bus-reset, high-availability

### 5.13.7 Registering (pages 209-215)

**File:** `10_5137_registering.md`

Initiator 如何用 REGISTER / REGISTER AND IGNORE EXISTING KEY service action 建立 reservation key。key 唯一性、SA_KEY 更換流程、registration 衝突的處理。

**Keywords:** reservation-key, register, registrants, sa-key, reservation-setup

### 5.13.11 Releasing persistent reservations and removing registrations (pages 216-224)

**File:** `11_51311_releasing_persistent_reservations_and_removing_registr.md`

RELEASE、CLEAR、PREEMPT、PREEMPT AND ABORT 各 service action 的語意差異、對其他 initiator 的影響、unit attention 通知規則。failover 時搶奪 reservation 的正確順序。

**Keywords:** release-reservation, preempt, preempt-and-abort, unit-attention, failover

### 5.14.1 Security goals and threat model (pages 225-226)

**File:** `12_5141_security_goals_and_threat_model.md`

SCSI layer 的安全目標與 threat model：authentication、confidentiality、integrity、replay protection 對應的攻擊場景。啟動 IKEv2-SCSI / ESP-SCSI / CbCS 等安全協定前的背景說明。

**Keywords:** scsi-security, threat-model, authentication, confidentiality, integrity

### 5.14.2 Security associations (pages 227-231)

**File:** `13_5142_security_associations.md`

Security Association (SA) 概念：兩個 endpoint 之間共享的密鑰、演算法、序號狀態。SA 生命週期、SA identifier、lifetime、rekey 的機制。SCSI 加密 / 驗證的共通基礎元件。

**Keywords:** security-association, sa, key-lifetime, rekey, scsi-sa

### 5.14.3 Key derivation functions (pages 232-234)

**File:** `14_5143_key_derivation_functions.md`

SCSI 安全協定使用的 KDF：從 shared secret 導出 encryption key、integrity key、child SA key 的方法。基於 HMAC-SHA-256、PRF+ 結構。IKEv2-SCSI 的 crypto primitives。

**Keywords:** kdf, key-derivation, hmac-sha-256, prf-plus, crypto-primitives

### 5.14.4 Using IKEv2-SCSI to create an SA (pages 235-262)

**File:** `15_5144_using_ikev2-scsi_to_create_an_sa.md`

IKEv2-SCSI 建立 SA 的完整流程：IKE_SA_INIT、IKE_AUTH、CREATE_CHILD_SA 訊息交換對應的 SECURITY PROTOCOL IN/OUT 操作、payload 格式、Diffie-Hellman 交換。SCSI 安全通道建立的核心章節，篇幅較長。

**Keywords:** ikev2-scsi, security-protocol, diffie-hellman, sa-negotiation, authentication

### 5.14.6 Command security (pages 263-285)

**File:** `16_5146_command_security.md`

對 SCSI 命令本身做 integrity / confidentiality 保護的機制：ICV (Integrity Check Value)、ESP (Encapsulating Security Payload)、key 綁定命令序號。讓 command 本身無法被竄改 / 竊聽的能力。

**Keywords:** command-security, icv, esp-scsi, integrity-check, encrypted-command

### 5.14.7 ESP-SCSI for parameter data (pages 286-301)

**File:** `17_5147_esp-scsi_for_parameter_data.md`

ESP-SCSI（參考 IPsec ESP）應用於 SCSI parameter data 的 encrypted / authenticated 傳輸：encapsulation format、IV、ICV、SPI 識別。保護 Data-In/Data-Out buffer 的機密性。

**Keywords:** esp-scsi, encrypted-parameter-data, iv, icv, spi

### 5.15.4 Self-test modes (pages 302-305)

**File:** `18_5154_self-test_modes.md`

SEND DIAGNOSTIC 啟動的 self-test 分類：default test、background short/extended self-test、foreground self-test。各模式執行時間、對 IO 的影響、結果存放位置。SMART self-test 的 SCSI 實作。

**Keywords:** self-test, send-diagnostic, short-test, extended-test, smart

### 5.16.2 Asymmetric logical unit access (pages 306-312)

**File:** `19_5162_asymmetric_logical_unit_access.md`

ALUA (Asymmetric Logical Unit Access) 模型：target port group、Active/Optimized、Active/Non-Optimized、Standby、Unavailable 等 state，以及 Implicit/Explicit ALUA 切換。Enterprise storage array 多 controller 路徑優先權的核心規範。

**Keywords:** alua, asymmetric-access, target-port-group, multipath, explicit-alua, implicit-alua

### 5.17.2 Copy manager model (pages 313-316)

**File:** `20_5172_copy_manager_model.md`

Copy manager（負責 EXTENDED COPY 與 third-party copy 的角色）模型：在 source 與 destination 間移動資料而不經 host。copy manager function、capabilities、concurrent copies 規則。ODX、VAAI XCOPY 的底層角色定義。

**Keywords:** copy-manager, third-party-copy, extended-copy, odx, xcopy, server-side-copy

### 5.17.4 Third-party copy command usage (pages 317-321)

**File:** `21_5174_third-party_copy_command_usage.md`

Third-party copy 命令族（EXTENDED COPY、POPULATE TOKEN、WRITE USING TOKEN、RECEIVE COPY RESULTS）的搭配用法、常見 use case 序列（VM clone、snapshot、cross-array migration）。

**Keywords:** third-party-copy, extended-copy, populate-token, receive-copy-results, cross-array-migration

### 5.17.6 RODs and ROD tokens (pages 322-334)

**File:** `22_5176_rods_and_rod_tokens.md`

ROD (Representation of Data) 與 ROD token 的完整模型：token format、ROD type code、POINT IN TIME / BLOCK ZERO / BLOCK UNCHANGED 等 ROD 語意、token lifetime、inactivation。ODX 底層資料結構核心章節。

**Keywords:** rod, rod-token, point-in-time, block-zero, odx, token-format

### 5.17.7 The EXTENDED COPY command (pages 335-346)

**File:** `23_5177_the_extended_copy_command.md`

EXTENDED COPY (opcode 83h) 架構描述：LID1 / LID4 兩種 variant、parameter list 結構（CSCD descriptor + segment descriptor）、同步 / 非同步執行、進度回報。VAAI XCOPY 的實際命令。

**Keywords:** extended-copy, xcopy, cscd, segment-descriptor, lid1, lid4, vaai

### 6.2.1 CHANGE ALIASES command introduction (pages 347-349)

**File:** `24_621_change_aliases_command_introduction.md`

CHANGE ALIASES 命令：管理 device 的 alias entries（替代命名）。用於 device identification 有多重視角（protocol-independent / protocol-specific）時的統一 alias 管理。

**Keywords:** change-aliases, alias-entry, device-identification, alias-management

### 6.2.4 Alias entry protocol independent designations (pages 350-352)

**File:** `25_624_alias_entry_protocol_independent_designations.md`

Protocol-independent alias designation 格式：EUI-64、NAA、iSCSI name 等通用 identifier 的 alias entry 欄位定義。用於跨協定環境統一 device 識別。

**Keywords:** alias, protocol-independent, eui-64, naa, iscsi-name

### 6.4.2 EXTENDED COPY(LID4) parameter data (pages 353-354)

**File:** `26_642_extended_copylid4_parameter_data.md`

EXTENDED COPY 的 LID4 (List Identifier 4-byte) 變體 parameter list 結構，支援大於 LID1 的 copy operation、更長的 CSCD list、完整 PI 欄位。現代 storage array 做 cross-LUN 複製的主流變體。

**Keywords:** extended-copy-lid4, parameter-data, list-identifier, large-copy-operation

### 6.4.3 Shared EXTENDED COPY parameter list fields (pages 355-359)

**File:** `27_643_shared_extended_copy_parameter_list_fields.md`

LID1 與 LID4 共用的 parameter list header 欄位：LIST IDENTIFIER、PRIORITY、G_SENSE、IMMED、LIST ID USAGE 等，以及 Target Descriptor List Length、Segment Descriptor List Length 的結構。

**Keywords:** extended-copy, parameter-list-header, priority, list-id-usage, immed

### 6.4.5 CSCD descriptors (pages 360-374)

**File:** `28_645_cscd_descriptors.md`

CSCD (CoPy Source and Destination Descriptor) 格式：identify 一個 copy 的來源 / 目的 logical unit。含 Fibre Channel、SAS、iSCSI、Parallel SCSI、Identification 各種 CSCD type 的具體欄位。

**Keywords:** cscd, copy-source-destination, target-descriptor, extended-copy

### 6.4.6 Segment descriptors (pages 375-412)

**File:** `29_646_segment_descriptors.md`

EXTENDED COPY 的 segment descriptor 類型：Block Device to Block Device、Block to Stream、Stream to Block、以及 embedded data、write filemarks 等 stream 相關 descriptor。本章是 SPC-4 最長章節之一，涵蓋所有複製 segment type 的完整格式。

**Keywords:** segment-descriptor, block-to-block, stream-copy, extended-copy, copy-segment

### 6.6.2 Standard INQUIRY data (pages 413-428)

**File:** `30_662_standard_inquiry_data.md`

INQUIRY 命令回傳的 standard data 結構：PERIPHERAL QUALIFIER / DEVICE TYPE、RMB、VERSION、RESPONSE DATA FORMAT、ADDITIONAL LENGTH、旗標欄位(NORMACA, HISUP, SCCS, ACC, TPGS, 3PC, PROTECT, ENCSERV, MULTIP 等)、T10 VENDOR ID、PRODUCT ID、PRODUCT REVISION LEVEL、VERSION DESCRIPTORS。做 device discovery 時每個 driver 都會解析此章定義的資料。

**Keywords:** inquiry, standard-inquiry-data, peripheral-device-type, vendor-id, version-descriptors, tpgs

### 6.6.3 SCSI Parallel Interface specific INQUIRY data (pages 429-430)

**File:** `31_663_scsi_parallel_interface_specific_inquiry_data.md`

傳統 SPI (SCSI Parallel Interface) 特定的 INQUIRY 欄位，主要為相容舊硬體保留。現代 SAS / FC / iSCSI 已不使用。

**Keywords:** inquiry, spi, parallel-scsi, legacy-inquiry

### 6.7.1 Introduction (LOG SELECT / LOG SENSE) (pages 431-432)

**File:** `32_671_introduction.md`

LOG SELECT (opcode 4Ch) / LOG SENSE (opcode 4Dh) 命令簡介：log parameter 架構、SP / PCR / PC / PAGE CODE 欄位語意、cumulative / threshold parameter。所有 log page 存取的共通介面。

**Keywords:** log-select, log-sense, log-parameter, page-code, cumulative-threshold

### 6.7.2 Processing LOG SELECT when the parameter list length is zero (pages 433-438)

**File:** `33_672_processing_log_select_when_the_parameter_list_length_is.md`

LOG SELECT 帶 parameter list length = 0 時的特殊行為（reset / clear log parameter）、PCR (Parameter Code Reset) 旗標意義。做 log 清除時的正確用法。

**Keywords:** log-select, zero-parameter-list, pcr, log-reset

### 6.9.2 Management protocol information description (pages 439-446)

**File:** `34_692_management_protocol_information_description.md`

MANAGEMENT PROTOCOL IN / OUT 命令的 protocol info payload 格式，用於 SCSI 層級的管理訊息（例如 SAS IO expander 管理）。protocol-specific management channel。

**Keywords:** management-protocol, management-protocol-in, sas-management

### 6.13.6 Initial responses (pages 447-450)

**File:** `35_6136_initial_responses.md`

PERSISTENT RESERVE IN 的 initial response 格式：PRgeneration、Additional Length、Key List 或 Reservation Descriptor。查詢 reservation 狀態時 host 解析的主要資料結構。

**Keywords:** persistent-reserve-in, initial-response, prgeneration, reservation-descriptor

### 6.15.3 READ RESERVATION service action (pages 451-454)

**File:** `36_6153_read_reservation_service_action.md`

PERSISTENT RESERVE IN 的 READ RESERVATION service action：回傳目前 logical unit 上的 active reservation（type、holder key、scope）。查詢誰持有 reservation 的命令。

**Keywords:** read-reservation, persistent-reserve-in, reservation-holder, reservation-status

### 6.15.4 REPORT CAPABILITIES service action (pages 455-458)

**File:** `37_6154_report_capabilities_service_action.md`

PERSISTENT RESERVE IN REPORT CAPABILITIES：回傳 device 支援的 PR 能力（type mask、allow commands、SIP_C、CRH、ATP_C、SPEC_I_PT、PTPL_A、PTPL_C 等旗標）。實作 PR client 前檢查 device 能力。

**Keywords:** report-capabilities, pr-capabilities, ptpl, crh, type-mask

### 6.15.5 READ FULL STATUS service action (pages 459-460)

**File:** `38_6155_read_full_status_service_action.md`

PERSISTENT RESERVE IN READ FULL STATUS：回傳所有 registered / reservation holder 的完整清單，每筆含 reservation key、reservation holder 旗標、scope、type、transport ID。debug cluster reservation 糾紛時最實用。

**Keywords:** read-full-status, full-reservation-status, transport-id, cluster-debug

### 6.16.1 PERSISTENT RESERVE OUT command introduction (pages 461-463)

**File:** `39_6161_persistent_reserve_out_command_introduction.md`

PERSISTENT RESERVE OUT (opcode 5Fh) 命令簡介：service action 分類（REGISTER、RESERVE、RELEASE、CLEAR、PREEMPT、PREEMPT AND ABORT、REGISTER AND IGNORE EXISTING KEY、REGISTER AND MOVE）、CDB 欄位、scope/type 組合。cluster / failover 操作的核心命令。

**Keywords:** persistent-reserve-out, service-action, register-and-move, pro-command

### 6.16.3 Basic PERSISTENT RESERVE OUT parameter list (pages 464-468)

**File:** `40_6163_basic_persistent_reserve_out_parameter_list.md`

PRO 基本 parameter list 欄位：RESERVATION KEY、SERVICE ACTION RESERVATION KEY、APTPL、ALL_TG_PT、SPEC_I_PT 旗標、transport ID 陣列。設定 reservation 時 host 必填的資料。

**Keywords:** pro-parameter-list, reservation-key, aptpl, all-tg-pt, spec-i-pt

### 6.16.4 Parameter list for PERSISTENT RESERVE OUT with REGISTER AND MOVE (pages 469-470)

**File:** `41_6164_parameter_list_for_the_persistent_reserve_out_command_w.md`

REGISTER AND MOVE service action 特殊 parameter list：transferring reservation 到另一個 I_T_L nexus，包含 target port 與 relative target port 的指定。跨 port failover 或 live migration 場景。

**Keywords:** register-and-move, transfer-reservation, relative-target-port, live-migration

### 6.17.1 READ ATTRIBUTE command introduction (pages 471-475)

**File:** `42_6171_read_attribute_command_introduction.md`

READ ATTRIBUTE (opcode 8Ch)：查詢 Medium Auxiliary Memory (MAM) 存的 attribute (tape 及 enclosure 多用)，包含 ATTRIBUTE IDENTIFIER、ELEMENT ADDRESS、LOGICAL VOLUME NUMBER、PARTITION NUMBER 等欄位。

**Keywords:** read-attribute, mam, medium-auxiliary-memory, attribute-identifier

### 6.18.1 READ BUFFER command introduction (pages 476-480)

**File:** `43_6181_read_buffer_command_introduction.md`

READ BUFFER (opcode 3Ch) 總覽：MODE 欄位分類（data、descriptor、vendor specific、read data with ECHO、error history、download microcode status、data from echo、3rd party copy）。firmware update 進度查詢、debug dump 下載的主要命令。

**Keywords:** read-buffer, mode, firmware-dump, microcode-status, error-history

### 6.18.9 Error history mode (1Ch) (pages 481-508)

**File:** `44_6189_error_history_mode_1ch.md`

READ BUFFER mode 1Ch (error history) 的完整 payload 格式：error history directory、buffer ID、offset、每個 error event 的 header/body 結構。debug 端解析 device 長期錯誤紀錄的細節章節。

**Keywords:** read-buffer-1ch, error-history-directory, buffer-id, error-event-format

### 6.27.1 RECEIVE CREDENTIAL command description (pages 509-511)

**File:** `45_6271_receive_credential_command_description.md`

RECEIVE CREDENTIAL 命令：從 device 取得 capability-based security credential（CbCS 協定），含 CREDENTIAL TYPE、NONCE、CHALLENGE 欄位。儲存 capability-token 分發的 SCSI 介面。

**Keywords:** receive-credential, cbcs, capability-based-security, nonce, credential-token

### 6.27.2 RECEIVE CREDENTIAL parameter data (pages 512-523)

**File:** `46_6272_receive_credential_parameter_data.md`

RECEIVE CREDENTIAL 回傳的 parameter data 結構：capability descriptor、signing algorithm、valid time、allowed operations 等欄位。CbCS credential 的完整資料格式定義。

**Keywords:** credential-parameter-data, capability-descriptor, signing-algorithm, cbcs

### 6.32.1 REPORT IDENTIFYING INFORMATION command overview (pages 524-525)

**File:** `47_6321_report_identifying_information_command_overview.md`

REPORT IDENTIFYING INFORMATION (opcode A3h / SA 05h)：取得 device 的 logical unit 識別資訊（UNIT、LOGICAL UNIT、TARGET PORT、TARGET DEVICE 各種 type 的 identifying information）。做 asset 管理或 device tracking 時用。

**Keywords:** report-identifying-information, device-tracking, asset-management

### 6.32.3 IDENTIFYING INFORMATION SUPPORTED parameter data (pages 526-531)

**File:** `48_6323_identifying_information_supported_parameter_data.md`

回報 device 支援哪幾種 identifying information type 的 parameter data 格式、SET IDENTIFYING INFORMATION 可寫性。識別資訊 discovery 階段用。

**Keywords:** identifying-information-supported, supported-types, set-identifying-information

### 6.35.1 REPORT SUPPORTED OPERATION CODES command introduction (pages 532-534)

**File:** `49_6351_report_supported_operation_codes_command_introduction.md`

REPORT SUPPORTED OPERATION CODES (opcode A3h / SA 0Ch)：列出 device 支援的所有 opcode + service action、CDB 長度、command timeouts。做 driver capability discovery 時最常用的命令之一。

**Keywords:** report-supported-operation-codes, opcode-discovery, cdb-usage-data, capability-discovery

### 6.35.3 One_command parameter data format (pages 535-536)

**File:** `50_6353_one_command_parameter_data_format.md`

REPORT SUPPORTED OPERATION CODES 的 one_command 模式（查單一 opcode）parameter data 格式：CTDP（command timeout descriptor present）、CDB USAGE DATA、usage bitmap。

**Keywords:** one-command-format, ctdp, cdb-usage-data, support-query

### 6.35.4 Command timeouts descriptor (pages 537-582)

**File:** `51_6354_command_timeouts_descriptor.md`

Command timeouts descriptor 格式：NOMINAL COMMAND PROCESSING TIMEOUT、RECOMMENDED COMMAND TIMEOUT、command specific information。讓 host 知道每個命令預期 / 最壞執行時間。配合 REPORT SUPPORTED OPERATION CODES 使用。跨多條 mode 的長章節。

**Keywords:** command-timeouts-descriptor, nominal-timeout, recommended-timeout, ctdp

### 6.49.15 Download application client error history mode (1Ch) (pages 583-586)

**File:** `52_64915_download_application_client_error_history_mode_1ch.md`

WRITE BUFFER mode 1Ch：讓 application client download error history / debug log 進 device 的模式。與 READ BUFFER 1Ch 互補的上行管道。

**Keywords:** write-buffer-1ch, download-error-history, application-client-log

### 7.2.2 Diagnostic page format and page codes for all device types (pages 587-588)

**File:** `53_722_diagnostic_page_format_and_page_codes_for_all_device_typ.md`

所有 SCSI device 共用的 diagnostic page 格式（PAGE CODE + PAGE LENGTH + data）與 page code 對照表。SEND DIAGNOSTIC / RECEIVE DIAGNOSTIC RESULTS 命令的 payload 格式基礎。

**Keywords:** diagnostic-page-format, page-code, send-diagnostic, receive-diagnostic-results

### 7.2.4 Supported Diagnostic Pages (pages 589-591)

**File:** `54_724_supported_diagnostic_pages.md`

Supported Diagnostic Pages (page code 00h)：回傳 device 支援的所有 diagnostic page code 清單。做 diagnostic capability discovery 時第一個查詢的 page。

**Keywords:** supported-diagnostic-pages, page-00h, diagnostic-discovery

### 7.3.2 Log page structure and log parameter structure for all device types (pages 592-600)

**File:** `55_732_log_page_structure_and_log_parameter_structure_for_all_d.md`

Log page 共通結構：PAGE CODE、SUBPAGE CODE、PAGE LENGTH 與 log parameter（PARAMETER CODE、DU、TSD、ETC、TMC、FORMAT AND LINKING、PARAMETER LENGTH、PARAMETER VALUE）的統一格式。所有 log page 共用的 framing。

**Keywords:** log-page-format, log-parameter-format, page-code, subpage-code, parameter-structure

### 7.3.3 Application Client log page (pages 601-602)

**File:** `56_733_application_client_log_page.md`

Application Client log page (0Fh)：application 可自定義 log parameter 寫入 device 的 log buffer。給上層軟體 instrument trace data 用的 generic log channel。

**Keywords:** application-client-log, page-0fh, user-defined-log, trace-data

### 7.3.4 Buffer Over-Run/Under-Run log page (pages 603-605)

**File:** `57_734_buffer_over-rununder-run_log_page.md`

Buffer Over-Run / Under-Run log page (01h)：記錄 device 發生 buffer 溢出 / 不足事件的次數、cause、count。調校 buffer 大小或 IO queue depth 時參考。

**Keywords:** buffer-over-run, buffer-under-run, page-01h, performance-diagnostic

### 7.3.5 Cache Memory Statistics log page (pages 606-613)

**File:** `58_735_cache_memory_statistics_log_page.md`

Cache Memory Statistics log page (19h)：讀 / 寫 cache hit rate、bytes read from cache、bytes written to cache 的 counter。做 cache 效能分析、hit-ratio 監控用。

**Keywords:** cache-statistics, cache-hit-ratio, page-19h, cache-performance

### 7.3.6 General Statistics and Performance log pages (pages 614-619)

**File:** `59_736_general_statistics_and_performance_log_pages.md`

General Statistics and Performance log page (19h subpage 01h)：讀/寫 IO 次數、total bytes、IO latency histogram、queue 等 device 級 performance counter。做 device-level IO profiling 的主要資料來源。

**Keywords:** general-statistics, performance-log, page-19h-01h, io-counters, latency

### 7.3.7 Group Statistics and Performance (n) log pages (pages 620-626)

**File:** `60_737_group_statistics_and_performance_n_log_pages.md`

Group Statistics and Performance log pages（依 GROUP NUMBER 分桶）：按 QoS group 分別追蹤 IO 統計，讓 multi-tenant / noisy-neighbor 分析成為可能。對應 CDB 的 GROUP NUMBER 欄位。

**Keywords:** group-statistics, group-number, qos-analysis, multi-tenant-io

### 7.3.8 Informational Exceptions log page (pages 627-628)

**File:** `61_738_informational_exceptions_log_page.md`

Informational Exceptions log page (2Fh)：SMART-like 預測性失敗通知的 log。device 觸發 exception 時（threshold 超標、impending failure）寫入此 page。SMART trip 的 SCSI 版本。

**Keywords:** informational-exceptions, smart-trip, page-2fh, predictive-failure

### 7.3.9 Last n Deferred Errors or Asynchronous Events log page (pages 629-630)

**File:** `62_739_last_n_deferred_errors_or_asynchronous_events_log_page.md`

Last n Deferred Errors log page (0Bh)：保留最後 n 筆 deferred error / async event 的記錄。讓 host 可以回溯 device 最近發生但未直接 return 的錯誤事件。

**Keywords:** last-n-deferred-errors, async-events, page-0bh, error-replay

### 7.3.10 Last n Error Events log page (pages 631-632)

**File:** `63_7310_last_n_error_events_log_page.md`

Last n Error Events log page (07h)：保留最後 n 筆 error event 的通用記錄。每筆包含 timestamp、sense data、相關 LBA。做 RMA 診斷、post-mortem 分析用。

**Keywords:** last-n-error-events, page-07h, error-log, rma-diagnosis

### 7.3.11 Non-Medium Error log page (pages 633-634)

**File:** `64_7311_non-medium_error_log_page.md`

Non-Medium Error log page (06h)：統計非 medium 相關錯誤（protocol error、abort、hardware error）的累計次數。跟 Read/Write Error Counter page 互補。

**Keywords:** non-medium-error, page-06h, protocol-error, hardware-error

### 7.3.12 Power Condition Transitions log page (pages 635-636)

**File:** `65_7312_power_condition_transitions_log_page.md`

Power Condition Transitions log page (1Ah)：記錄每種 power state 轉換發生次數（Active→Idle、Idle→Standby 等）。做電源策略調校、節能效果驗證用。

**Keywords:** power-condition-transitions, page-1ah, power-state-count, energy-audit

### 7.3.13 Protocol Specific Port log page (pages 637-638)

**File:** `66_7313_protocol_specific_port_log_page.md`

Protocol Specific Port log page (18h)：各 transport protocol (SAS、FC、iSCSI) 的 port 層級 statistics，例如 SAS PHY 的 invalid dword count、loss of dword sync、disparity error。實體連線品質監控。

**Keywords:** protocol-specific-port-log, page-18h, sas-phy-statistics, link-quality

### 7.3.14 Read Error Counters log page (pages 639-640)

**File:** `67_7314_read_error_counters_log_page.md`

Read Error Counters log page (03h)：Errors Corrected Without Substantial Delay、With Possible Delays、Total、Correction Algorithm Processed、Total Bytes Processed、Total Uncorrected Errors 六個標準 counter。ECC 統計分析核心。

**Keywords:** read-error-counters, page-03h, ecc-statistics, uncorrected-errors

### 7.3.15 Read Reverse Error Counters log page (pages 641-642)

**File:** `68_7315_read_reverse_error_counters_log_page.md`

Read Reverse Error Counters log page (04h)：Read Reverse 方向（主要是 tape 裝置使用）的錯誤計數器，結構與 Read Error Counters 相同。block device 很少使用。

**Keywords:** read-reverse-error-counters, page-04h, tape-read-reverse

### 7.3.16 Self-Test Results log page (pages 643-646)

**File:** `69_7316_self-test_results_log_page.md`

Self-Test Results log page (10h)：保留最近 20 筆 self-test 結果，每筆含 self-test code、result、power-on hours、address of first failure、sense code。SMART self-test 歷史查詢。

**Keywords:** self-test-results, page-10h, self-test-history, first-failure-address

### 7.3.17 Start-Stop Cycle Counter log page (pages 647-655)

**File:** `70_7317_start-stop_cycle_counter_log_page.md`

Start-Stop Cycle Counter log page (0Eh)：Date of Manufacture、Accounting Date、Specified Cycle Count Over Device Lifetime、Accumulated Start-Stop Cycles、等 drive 壽命相關參數。做 drive 老化評估、PoH 報告時核心資料。

**Keywords:** start-stop-cycle, page-0eh, device-lifetime, power-on-hours, date-of-manufacture

### 7.3.21 Temperature log page (pages 656-658)

**File:** `71_7321_temperature_log_page.md`

Temperature log page (0Dh)：Temperature parameter（current drive temperature）+ Reference Temperature（recommended max）。熱管理、資料中心 thermal 告警依據。

**Keywords:** temperature-log, page-0dh, thermal-monitoring, reference-temperature

### 7.3.22 Verify Error Counters log page (pages 659-660)

**File:** `72_7322_verify_error_counters_log_page.md`

Verify Error Counters log page (05h)：VERIFY 命令的錯誤計數器，六個 counter 結構與 Read Error Counters 相同。做 integrity check 長期統計用。

**Keywords:** verify-error-counters, page-05h, verify-statistics

### 7.3.23 Write Error Counters log page (pages 661-664)

**File:** `73_7323_write_error_counters_log_page.md`

Write Error Counters log page (02h)：WRITE 命令的錯誤計數器，六個 counter 結構同 Read Error Counters。長期 write 錯誤 trend 分析。

**Keywords:** write-error-counters, page-02h, write-statistics

### 7.4.2 Attribute identifier values (pages 665-681)

**File:** `74_742_attribute_identifier_values.md`

MAM (Medium Auxiliary Memory) attribute 完整 identifier 清單 + 格式：device attribute（Remaining Capacity、Load Count...）、media attribute、host specific attribute。主要供 tape / removable media 使用。

**Keywords:** mam, attribute-identifier, medium-auxiliary-memory, tape-attribute

### 7.5.8 Control mode page (pages 682-688)

**File:** `75_758_control_mode_page.md`

Control mode page (0Ah)：TST、TMF_ONLY、DPICZ、D_SENSE、GLTSD、RLEC、QERR、NUAR、QUEUE ALGORITHM MODIFIER、SWP、UA_INTLCK_CTRL、RAC、BUSY TIMEOUT PERIOD 等 device 全域行為控制旗標。driver 初始化時常設定此 page。

**Keywords:** control-mode-page, page-0ah, tst, qerr, swp, busy-timeout

### 7.5.10 Disconnect-Reconnect mode page (pages 689-692)

**File:** `76_7510_disconnect-reconnect_mode_page.md`

Disconnect-Reconnect mode page (02h)：Buffer Full Ratio、Buffer Empty Ratio、Bus Inactivity Limit、Disconnect Time Limit、Connect Time Limit、Maximum Burst Size 等 parallel SCSI / SAS transport 行為調校。現代系統多沿用預設值。

**Keywords:** disconnect-reconnect, page-02h, bus-inactivity-limit, maximum-burst-size

### 7.5.13 Power Condition mode page (pages 693-698)

**File:** `77_7513_power_condition_mode_page.md`

Power Condition mode page (1Ah)：Idle_a/b/c、Standby_y/z 的 timer condition enable 與 duration 設定。做電源管理策略調校（讓 drive 多久 idle 後轉 standby）的主要介面。

**Keywords:** power-condition-mode-page, page-1ah, idle-timer, standby-timer

### 7.5.16 Protocol Specific Port mode page (pages 699-700)

**File:** `78_7516_protocol_specific_port_mode_page.md`

Protocol Specific Port mode page (19h)：針對 SAS、FC 等 transport 提供 port-level 設定項目（例如 SAS PHY rate、transmit level）。實際欄位由 transport 標準（SPL、FCP）定義。

**Keywords:** protocol-specific-port-mode-page, page-19h, sas-phy, fc-port-config

### 7.6.2 Alias entry protocol specific designations (pages 701-708)

**File:** `79_762_alias_entry_protocol_specific_designations.md`

Protocol-specific alias designation 格式：例如 SAS address、FC WWNN / WWPN、iSCSI TargetName 等 per-transport identifier 的 alias entry 結構。

**Keywords:** alias, protocol-specific, sas-address, wwnn, iscsi-target-name

### 7.6.3 EXTENDED COPY protocol specific CSCD descriptors (pages 709-716)

**File:** `80_763_extended_copy_protocol_specific_cscd_descriptors.md`

Protocol-specific CSCD descriptor 格式：用 SAS address / FC N_Port ID / iSCSI transport ID 指定 EXTENDED COPY 的 source / destination endpoint。跨不同 fabric 做 third-party copy 時使用。

**Keywords:** extended-copy, cscd-protocol-specific, sas-cscd, fc-cscd, iscsi-cscd

### 7.6.4 TransportID identifiers (pages 717-724)

**File:** `81_764_transportid_identifiers.md`

TransportID 通用格式：在 PR、EXTENDED COPY 等命令中識別特定 I_T nexus 的結構。依 PROTOCOL IDENTIFIER 分 SAS、FC、iSCSI、SOP、USB Attached SCSI 等 variant 的具體 byte layout。

**Keywords:** transport-id, protocol-identifier, i-t-nexus, pr-transport-id

### 7.7.1 Security protocol information description (pages 725-730)

**File:** `82_771_security_protocol_information_description.md`

SECURITY PROTOCOL IN 00h (security protocol information) 的 parameter data：支援的 security protocol 清單、對應 parameter code、length。做 security capability discovery 時第一個查詢。

**Keywords:** security-protocol-information, sec-protocol-00h, capability-discovery

### 7.7.2 SA creation capabilities (pages 731-732)

**File:** `83_772_sa_creation_capabilities.md`

SA Creation Capabilities parameter：device 支援的 key exchange algorithm、encryption / integrity algorithm、hash、PRF 清單。建立 SA 前 host 查詢 device 能力。

**Keywords:** sa-creation-capabilities, supported-algorithms, key-exchange, prf

### 7.7.3 IKEv2-SCSI (pages 733-782)

**File:** `84_773_ikev2-scsi.md`

IKEv2-SCSI 完整協定規格：訊息格式、payload 類型 (SA、KE、Nonce、IDi、IDr、AUTH、CERT、ENCR、SAUTH)、協商流程、error handling、rekey、SA termination。SPC-4 安全章節中最長、最核心的一節。做 enterprise SCSI 加密實作時必讀。

**Keywords:** ikev2-scsi, payload-format, ike-negotiation, rekey, sa-termination

### 7.7.4 CbCS security protocol (pages 783-804)

**File:** `85_774_cbcs_security_protocol.md`

Capability-based Command Security (CbCS) 協定完整規格：credential、capability descriptor、signing、nonce、command authorization flow。另一套 SCSI 層級的權限控制模型。

**Keywords:** cbcs, capability-based-security, credential, capability-descriptor, command-authorization

### 7.8.5 Device Constituents VPD page (pages 805-808)

**File:** `86_785_device_constituents_vpd_page.md`

Device Constituents VPD page (8Bh)：描述由多個子 device 組成的複合 device（例如 SAS enclosure）的內部結構、子元件 INQUIRY-like data。層級化 device 探索用。

**Keywords:** device-constituents, vpd-8bh, composite-device, enclosure-constituents

### 7.8.6 Device Identification VPD page (pages 809-824)

**File:** `87_786_device_identification_vpd_page.md`

Device Identification VPD page (83h)：最重要的 VPD page，列出 device 各種 identifier（T10 vendor ID、EUI-64、NAA、iSCSI name、relative target port、target port group、logical unit group、MD5 logical unit identifier）。host multipath、udev rules、storage inventory 核心資料來源。

**Keywords:** device-identification, vpd-83h, naa, eui-64, relative-target-port, target-port-group

### 7.8.7 Extended INQUIRY Data VPD page (pages 825-828)

**File:** `88_787_extended_inquiry_data_vpd_page.md`

Extended INQUIRY Data VPD page (86h)：ACTIVATE_MICROCODE、SPT、GRD_CHK、APP_CHK、REF_CHK、UASK_SUP、GROUP_SUP、PRIOR_SUP、HEADSUP、ORDSUP、SIMPSUP、WU_SUP、CRD_SUP、NV_SUP、V_SUP、P_I_I_SUP、LUICLR、R_SUP 等旗標。查 device 支援哪些 PI / queue 能力。

**Keywords:** extended-inquiry-data, vpd-86h, spt, grd-chk, queue-capabilities

### 7.8.8 Management Network Addresses VPD page (pages 829-830)

**File:** `89_788_management_network_addresses_vpd_page.md`

Management Network Addresses VPD page (85h)：回報 device 的 out-of-band management 網路位址（通常是 IP address / URL）。datacenter 裝置盤點、自動發現時使用。

**Keywords:** management-network-addresses, vpd-85h, out-of-band-management, discovery

### 7.8.9 Mode Page Policy VPD page (pages 831-832)

**File:** `90_789_mode_page_policy_vpd_page.md`

Mode Page Policy VPD page (87h)：列出每個 mode page 的 shared / per-I_T nexus / per-target-port 策略。多 initiator 環境下理解 mode setting 是否互相可見的依據。

**Keywords:** mode-page-policy, vpd-87h, per-it-nexus, shared-mode-page

### 7.8.10 Power Condition VPD page (pages 833-835)

**File:** `91_7810_power_condition_vpd_page.md`

Power Condition VPD page (8Ah)：回報 device 各 power state（Active、Idle_a/b/c、Standby_y/z）的預估 transition time（stopped → active、standby → active）。power management 策略做延遲預估用。

**Keywords:** power-condition-vpd, vpd-8ah, stopped-to-active, standby-to-active, transition-time

### 7.8.12 Protocol Specific Logical Unit Information VPD page (pages 836-837)

**File:** `92_7812_protocol_specific_logical_unit_information_vpd_page.md`

Protocol Specific Logical Unit Information VPD page (90h)：依 transport protocol 回報 LUN 級 information（例如 SAS TLR 能力）。由 transport 標準（SPL、FCP）延伸定義。

**Keywords:** protocol-specific-lu-info, vpd-90h, sas-tlr, per-lun-transport-info

### 7.8.13 Protocol Specific Port Information VPD page (pages 838-839)

**File:** `93_7813_protocol_specific_port_information_vpd_page.md`

Protocol Specific Port Information VPD page (91h)：依 transport 回報 target port 級 information（例如 SAS PHY info、FC world wide port name）。

**Keywords:** protocol-specific-port-info, vpd-91h, sas-phy-info, fc-wwpn

### 7.8.14 SCSI Ports VPD page (pages 840-844)

**File:** `94_7814_scsi_ports_vpd_page.md`

SCSI Ports VPD page (88h)：列出 device 上所有 target port 的 relative port identifier、target port identifiers、initiator port identifiers。做 multipath 探索、port 層級盤點時用。

**Keywords:** scsi-ports-vpd, vpd-88h, relative-port-identifier, target-port-identifiers

### 7.8.17 Third-party Copy VPD page (pages 845-865)

**File:** `95_7817_third-party_copy_vpd_page.md`

Third-party Copy VPD page (8Fh)：列出 device 支援的 third-party copy descriptor type、maximum CSCD descriptor count、maximum segment descriptor count、maximum descriptor list length、supported ROD token features。實作 XCOPY / ODX client 前查 device 能力極限。

**Keywords:** third-party-copy-vpd, vpd-8fh, xcopy-limits, odx-capabilities

### 7.8.18 Unit Serial Number VPD page (pages 866-867)

**File:** `96_7818_unit_serial_number_vpd_page.md`

Unit Serial Number VPD page (80h)：device serial number 的 ASCII 字串欄位。最常用、最簡單的 VPD page，通常是 host inventory 的第一欄。

**Keywords:** unit-serial-number, vpd-80h, serial-number, inventory

### 8.3.1 Access controls model (pages 868-883)

**File:** `97_831_access_controls_model.md`

Access Controls (ACL) 模型：ACL coordinator、access control entries、AccessID、logical unit masking by initiator transport ID。在 target 層級做 LUN masking 的另一套機制（與 SAN zoning / LUN Masking 相輔）。

**Keywords:** access-controls, acl, accessid, lun-masking, acl-coordinator

### 8.3.2 ACCESS CONTROL IN command (pages 884-904)

**File:** `98_832_access_control_in_command.md`

ACCESS CONTROL IN (opcode 86h) 命令：查詢 ACL state — REPORT ACL、REPORT LU DESCRIPTORS、REPORT ACCESS CONTROLS LOG、REPORT OVERRIDE LOCKOUT TIMER 等 service action。ACL 管理的讀取介面。

**Keywords:** access-control-in, report-acl, report-lu-descriptors, acl-query

### 8.3.3 ACCESS CONTROL OUT command (pages 905-930)

**File:** `99_833_access_control_out_command.md`

ACCESS CONTROL OUT (opcode 87h) 命令：修改 ACL state — MANAGE ACL、DISABLE ACCESS CONTROLS、ACCESS ID ENROLL、CANCEL ENROLLMENT、ASSIGN LU 等 service action。ACL 管理的寫入介面。

**Keywords:** access-control-out, manage-acl, disable-access-controls, access-id-enroll

### C.2.2 Detecting lack of progress in active copy operations (Annex) (pages 931-954)

**File:** `100_c22_detecting_lack_of_progress_in_active_copy_operations.md`

附錄 C：示範 host 如何用 RECEIVE COPY RESULTS 監控 EXTENDED COPY 進度、偵測 copy operation stall（長時間無進度），以及 abort 策略。實作穩健 XCOPY client 的範例。

**Keywords:** copy-progress-detection, receive-copy-results, copy-stall, xcopy-monitoring, annex-c

### E.3.1 Operation codes (Annex) (pages 955-964)

**File:** `101_e31_operation_codes.md`

附錄 E：SPC-4 定義的所有 opcode 對照表（排序依 opcode 數值）、支援的 device type、CDB 長度、對應的 clause。firmware / driver 開發做 opcode → 命令名 反查時用。

**Keywords:** operation-codes, opcode-table, cdb-length, annex-e

### E.3.6 Variable length CDB service action codes (Annex) (pages 965-1012)

**File:** `102_e36_variable_length_cdb_service_action_codes.md`

附錄 E：32-byte variable-length CDB（opcode 7Fh）的 service action code 對照表，列出所有已定義的 16-bit service action + 對應命令名稱。解析 32-byte CDB 時第一站。

**Keywords:** variable-length-cdb, service-action-codes, opcode-7fh, 32-byte-cdb, annex-e
