# E.3.6 Variable length CDB service action codes

E.3.6 Variable length CDB service action codes
Only one operation code is assigned to the variable length CDB (see 4.2.3). Therefore, the service action
code is effectively the operation code for variable length CDB uses. To allow command standards to assign
uses of the variable length CDB without consulting this standard, ranges of service action codes are assigned
to command sets as shown in table E.8.
The variable length CDB service action codes assigned by this standard are shown in table E.9.
Table E.8 — Variable Length CDB Service Action Code Ranges
Service Action
Code Range
Doc.
Description
0000h to 07FFh
SBC-3
Direct access block device (e.g., magnetic disk)
0800h to 0FFFh
SSC-4
Sequential-access device (e.g., magnetic tape)
1000h to 17FFh
SSC
Printer device
1800h to 1FFFh
this standard
Commands for all device types (see table E.9)
2000h to 27FFh
Reserved
2800h to 2FFFh
MMC-6
CD-ROM device
3800h to 3FFFh
Reserved
4000h to 47FFh
SMC-3
Media changer device (e.g., jukeboxes)
5000h to 5FFFh
Defined by ASC IT8 (Graphic arts pre-press devices)
6000h to 67FFh
SCC-2
Storage array controller device (e.g., RAID)
7000h to 77FFh
RBC
Simplified direct-access device (e.g., magnetic disk)
7800h to 7FFFh
OCRW
Optical card reader/writer device
8800h to 8FFFh
OSD-2
Object-based Storage Device
3000h to 37FFh
Reserved
4800h to 4FFFh
Reserved
6800h to 6FFFh
Reserved
8000h to 87FFh
Reserved
9000h to F7FFh
Reserved
F800h to FFFFh
Vendor specific
Table E.9 — Variable Length CDB Service Action Codes Used by All Device Types
Service Action
Code
Description
1800h
RECEIVE CREDENTIAL command
1801h to 1FF7h
Reserved
1FF8h to 1FFFh
Restricted (see FC-SB-4)


E.4 Diagnostic page codes
Table E.10 is a numerical order listing of the diagnostic page codes.
Table E.10 — Diagnostic page codes
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
Diagnostic
Page Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
Diagnostic Page Name
00h
DT LPWROMAE
KVF
Supported Diagnostic Pages
01h
E
Configuration
02h
E
Enclosure Status/Control
03h
E
Help Text
04h
E
String In/Out
05h
E
Threshold In/Out
06h
E
Obsolete
07h
E
Element Descriptor
08h
E
Short Enclosure Status
09h
E
Enclosure Busy
0Ah
E
Additional Element Status
0Bh
E
Subenclosure Help Text
0Ch
E
Subenclosure String In/Out
0Dh
E
Supported SES Diagnostic Pages
0Eh
E
Download Microcode Status/Control
0Fh
E
Subenclosure Nickname Status/Control
10h to 1Fh
SES vendor specific
3Fh
Protocol Specific diagnostic page
40h
D
W
O
Translate Address In/Out
41h
D
W
O
Device Status In/Out
80h to FFh
Vendor specific
All codes not shown are restricted or reserved.


E.5 Log page codes
Table E.11 is a numerical order listing of the log page codes.
Table E.11 — Log page codes (part 1 of 2)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
Log
Page Code
Log
Subpage
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
Log Page Name
00h
00h
DT LPWROMAE
KVF
Supported Log Pages
00h
FFh
DT LPWROMAE
KVF
Supported Log Pages and Subpages
01h to 3Fh
FFh
DT LPWROMAE
KVF
Supported Subpages
01h
00h
DT LPWRO
A
KVF
Buffer Over-Run/Under-Run
02h
00h
DT
WRO
KV
Write Error Counters
03h
00h
DT
WRO
KV
Read Error Counters
04h
00h
T
V
Read Reverse Error Counters
05h
00h
DT
WRO
KV
Verify Error Counters
06h
00h
DT LPWROMAE
KVF
Non-Medium Error
07h
00h
DT LPWROMAE
KVF
Last n Error Events
08h
00h
D
W
O
V
Format Status
09h
00h to FEh
O
Reserved to the MS59 Std. (contact AIIM C21 comm.)
0Ah
00h to FEh
O
Reserved to the MS59 Std. (contact AIIM C21 comm.)
0Bh
00h
DT LPWROMAE
VF
Last n Deferred Error or Asynchronous Events
0Ch
00h
D
Logical Block Provisioning
0Ch
00h
T
V
Sequential-Access Device
0Dh
00h
DT LPWROMAE
V
Temperature
0Eh
00h
DT LPWROMAE
V
Start-Stop Cycle Counter
0Fh
00h
DT LPWROMAE
V
Application Client
10h
00h
DT LPWROMAE
V
Self-Test Results
11h
00h
D
Solid State Media
11h
00h
T
V
DT Device Status
12h
00h
V
TapeAlert Response
13h
00h
V
Requested Recovery
14h
00h
T
V
Device Statistics
15h
00h
D
Background Scan Results
15h
00h
V
Service Buffers Information
16h
00h
D
ATA PASS-THROUGH Results
16h
00h
T
V
Tape Diagnostic Data
17h
00h
D
Non-Volatile Cache
17h
00h
T
Volume Statistics
18h
xxh
DT LPWROMAE
KV
Protocol Specific Port (see table E.12)
19h
00h
D
General Statistics and Performance
19h
01h
D
Group Statistics and Performance (1)
19h
02h
D
Group Statistics and Performance (2)
19h
03h
D
Group Statistics and Performance (3)


19h
04h
D
Group Statistics and Performance (4)
19h
05h
D
Group Statistics and Performance (5)
19h
06h
D
Group Statistics and Performance (6)
19h
07h
D
Group Statistics and Performance (7)
19h
08h
D
Group Statistics and Performance (8)
19h
09h
D
Group Statistics and Performance (9)
19h
0Ah
D
Group Statistics and Performance (10)
19h
0Bh
D
Group Statistics and Performance (11)
19h
0Ch
D
Group Statistics and Performance (12)
19h
0Dh
D
Group Statistics and Performance (13)
19h
0Eh
D
Group Statistics and Performance (14)
19h
0Fh
D
Group Statistics and Performance (15)
19h
10h
D
Group Statistics and Performance (16)
19h
11h
D
Group Statistics and Performance (17)
19h
12h
D
Group Statistics and Performance (18)
19h
13h
D
Group Statistics and Performance (19)
19h
14h
D
Group Statistics and Performance (20)
19h
15h
D
Group Statistics and Performance (21)
19h
16h
D
Group Statistics and Performance (22)
19h
17h
D
Group Statistics and Performance (23)
19h
18h
D
Group Statistics and Performance (24)
19h
19h
D
Group Statistics and Performance (25)
19h
1Ah
D
Group Statistics and Performance (26)
19h
1Bh
D
Group Statistics and Performance (27)
19h
1Ch
D
Group Statistics and Performance (28)
19h
1Dh
D
Group Statistics and Performance (29)
19h
1Eh
D
Group Statistics and Performance (30)
19h
1Fh
D
Group Statistics and Performance (31)
1Ah
00h
DT LPWRO
A
K
Power Condition Transitions
1Bh
00h
T
Data Compression
2Dh
00h
T
Current Service Information
2Eh
00h
T
M
TapeAlert
2Fh
00h
DT LPWROMAE
KV
Informational Exceptions
30h to 3Eh
00h to FEh
Vendor specific
3Fh
00h to FEh
Reserved
All codes not shown here or in table E.12
are restricted or reserved.
Table E.11 — Log page codes (part 2 of 2)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
Log
Page Code
Log
Subpage
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
Log Page Name


Table E.12 is a numerical order listing of the log page codes used by SCSI transport protocols.
Table E.12 — Transport protocol specific log page codes
F – Fibre Channel Protocol for SCSI (FCP-4)
Device Column key
. S – SAS Protocol Layer (SPL-2)
blank = code not used
.
V – Automation/Device Interface device (ADT-2)
not blank = code used
Log
Page
Code
Log
Subpage
Code
.
U – USB Attached SCSI (UAS-2)
.
.
FSVU
Log Page Name
18h
00h
S
Protocol Specific Port
See table E.11 for information on the codes not shown here.


E.6 Mode page codes
Table E.13 is a numerical order listing of the mode page codes.
Table E.13 — Mode page codes (part 1 of 2)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
Mode Page
Code
Mode
Subpage
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
Mode Page Name
01h
00h
DT
WRO
K
Read-Write Error Recovery
02h
00h
DT L
WROMAE
KVF
Disconnect-Reconnect
03h
00h
D
Format Device
03h
00h
L
Parallel Printer Interface
03h
00h
R
MRW CD-RW
04h
00h
D
Rigid Disk Geometry
04h
00h
L
Serial Printer Interface
05h
00h
D
Flexible Disk
05h
00h
L
Printer Options
05h
00h
R
Write Parameters
06h
00h
W
O
Optical Memory
06h
00h
B
RBC Device Parameters
07h
00h
D
W
O
K
Verify Error Recovery
08h
00h
D
WRO
K
Caching
09h
00h
DT L
WRO
AE
K
obsolete
0Ah
00h
DT L
WROMAE
KVF
Control
0Ah
01h
DT L
WROMAE
KVF
Control Extension
0Ah
02h
D
Application Tag
0Ah
F0h
T
Control Data Protection
0Ah
F1h
D
PATA Control
0Bh
00h
D
W
O
K
Medium Types Supported
0Ch
00h
D
Notch and Partition
0Dh
00h
D
obsolete
0Dh
00h
R
CD Device Parameters
0Eh
00h
R
CD Audio Control
0Eh
01h
V
Target Device
0Eh
02h
V
DT Device Primary Port
0Eh
03h
V
Logical Unit
0Eh
04h
V
Target Device Serial Number
0Fh
00h
T
Data Compression
10h
00h
D
XOR Control
10h
00h
T
Device Configuration
11h
00h
T
Medium Partition (1)
12h
13h
14h
00h
DT
PWROMAEBK
F
Enclosure Services Management


15h
Extended
16h
Extended Device-Type Specific
17h
18h
xxh
DT L
WROMAE
VF
Protocol Specific Logical Unit (see table E.14)
19h
xxh
DT L
WROMAE
VF
Protocol Specific Port (see table E.14)
1Ah
00h
DT L
WROMA
V
Power Condition
1Ah
01h
DT
Power Consumption
1Ah
F1h
D
B
ATA Power Condition
1Bh
00h
A
LUN Mapping
1Ch
00h
D
AE
Informational Exceptions Control
1Ch
00h
T
M
V
Informational Exceptions Control (tapes-specific format)
1Ch
00h
R
Fault/Failure Reporting
1Ch
00h
L
Informational Exceptions Control (see SSC)
1Ch
00h
W
O
Informational Exceptions Control (see SBC)
1Ch
01h
D
Background Control
1Ch
02h
D
Logical Block Provisioning
1Dh
00h
T
Medium Configuration
1Dh
00h
R
C/DVD Time-Out and Protect
1Dh
00h
M
Element Address Assignments
1Eh
00h
M
Transport Geometry Parameters
1Fh
00h
M
Device Capabilities
00h
Vendor specific (does not require page format)
20h to 29h
Device-type specific (vendor specific in common usage)
2Ah
DT L
W
OMAEBKVF
Device-type specific (vendor specific in common usage)
2Ah
00h
R
CD Capabilities and Mechanical Status
2Bh to 3Eh
Device-type specific (vendor specific in common usage)
3Fh
xxh
Return all pages and/or subpages (MODE SENSE only)
xxh
FFh
Return all subpages (MODE SENSE only)
All codes not shown here or in table E.14
are restricted or reserved.
Table E.13 — Mode page codes (part 2 of 2)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
Mode Page
Code
Mode
Subpage
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
Mode Page Name


Table E.14 is a numerical order listing of the mode page codes used by SCSI transport protocols.
Table E.14 — Transport protocol specific mode page codes
F – Fibre Channel Protocol for SCSI (FCP-4)
Device Column key
. S – SAS Protocol Layer (SPL-2)
blank = code not used
.
V – Automation/Device Interface device (ADT-2)
not blank = code used
Mode
Page
Code
Mode
Subpage
Code
.
U – USB Attached SCSI (UAS-2)
.
.
FSVU
Mode Page Name
18h
00h
FS
Protocol Specific Logical Unit
19h
00h
FS
Protocol Specific Port
19h
01h
S
Phy Control And Discover
19h
02h
S
Shared Port Control
See table E.13 for information on the codes not shown here.


E.7 VPD page codes
Table E.15 is a numerical order listing of the VPD page codes.
Table E.15 — VPD page codes
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
VPD Page
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
DT LPWROMAEBKVF
VPD Page Name
00h
DT LPWROMAEBKVF
Supported VPD Pages
01h to 7Fh
DT LPWROMAEBKVF
ASCII Information
80h
DT LPWROMAEBKVF
Unit Serial Number
81h
DT LPWROMAEBKVF
Obsolete
82h
DT LPWROMAEBKVF
Obsolete
83h
DT LPWROMAEBKVF
Device Identification
84h
DT LPWROMAEBKVF
Software Interface Identification
85h
DT LPWROMAEBKVF
Management Network Addresses
86h
DT LPWROMAEBKVF
Extended INQUIRY Data
87h
DT LPWROMAEBKVF
Mode Page Policy
88h
DT LPWROMAEBKVF
SCSI Ports
89h
D
ATA Information
8Ah
DT LPWRO
A
K
Power Condition
8Bh
T
M
Device Constituents
8Ch
D
B
CFA Profile Information
8Dh
DT
Power Consumption
8Fh
DT
P
R
B
Third-party Copy
90h
DT L
WROMAE
VF
Protocol Specific Logical Unit Information
91h
DT L
WROMAE
VF
Protocol Specific Port Information
B0h
D
Block Limits
B0h
T
Sequential-access Device Capabilities
B0h
F
OSD information
B1h
D
Block Device Characteristics
B1h
T
V
Manufacturer-assigned Serial Number
B1h
F
Security Token
B2h
D
Logical Block Provisioning
B2h
T
TapeAlert Supported Flags
B3h
D
Referrals
B3h
T
Automation Device Serial Number
C0h to FFh
Vendor specific
All codes not shown here or in table E.16 are restricted or reserved.


Table E.14 is a numerical order listing of the VPD page codes used by SCSI transport protocols.
Table E.16 — Transport protocol specific VPD page codes
F – Fibre Channel Protocol for SCSI (FCP-4)
Device Column key
. S – SAS Protocol Layer (SPL-2)
blank = code not used
.
V – Automation/Device Interface device (ADT-2)
not blank = code used
VPD Page
Code
.
U – USB Attached SCSI (UAS-2)
.
.
FSVU
VPD Page Name
90h
S
Protocol Specific Logical Unit Information
91h
S
Protocol Specific Port Information
See table E.15 for information on the codes not shown here.


E.8 ROD type codes
Table E.17 is a numerical order listing of the ROD types.
Table E.17 — ROD type codes
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device
(RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
ROD Type
Code
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
.
.
.
.
.
ROD tokens allowed
DT LPWROMAEBKVF
ROD type
Output
Input
0000 0000h
DT
Internal use ROD or unused ROD type
No
No
0001 0000h
DT
Access upon reference
Yes
Yes
0080 0000h
DT
Point in time copy – default
Yes
Yes
0080 0001h
DT
Point in time copy – change vulnerable
Yes
Yes
0080 0002h
DT
Point in time copy – persistent
Yes
Yes
0080 FFFFh
DT
Point in time copy – any
Yes
Yes
FFFF 0001h
D
Block device zero ROD token
Yes a
Yes
All codes not shown are restricted or reserved.
a Output of this ROD type code is allowed only in the ROD tokens returned by the POPULATE TOKEN command
(see SBC-3).


E.9 Version descriptor values
Table E.18 is a numerical order listing of the version descriptor values used in the standard INQUIRY data.
Each version descriptor value is computed from a coded value identifying the standard and a coded value
representing the revision of the standard. The formula is ((standard32)+revison). Table E.18 shows all three
code values and the associated standard name. The version descriptor code is shown in both decimal and
hexadecimal.
Table E.18 — Version descriptor assignments (part 1 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex
0000h
Version Descriptor Not Supported or No Standard Identified
0020h
SAM (no version claimed)
003Bh
SAM T10/0994-D revision 18
003Ch
SAM ANSI INCITS 270-1996
0040h
SAM-2 (no version claimed)
0054h
SAM-2 T10/1157-D revision 23
0055h
SAM-2 T10/1157-D revision 24
005Ch
SAM-2 ANSI INCITS 366-2003
005Eh
SAM-2 ISO/IEC 14776-412
0060h
SAM-3 (no version claimed)
0062h
SAM-3 T10/1561-D revision 7
0075h
SAM-3 T10/1561-D revision 13
0076h
SAM-3 T10/1561-D revision 14
0077h
SAM-3 ANSI INCITS 402-2005
0080h
SAM-4 (no version claimed)
0087h
SAM-4 T10/1683-D revision 13
008Bh
SAM-4 T10/1683-D revision 14
0090h
SAM-4 ANSI INCITS 447-2008
0092h
SAM-4 ISO/IEC 14776-414
00A0h
SAM-5 (no version claimed)
00A2h
SAM-5 T10/2104-D revision 4
0120h
SPC (no version claimed)
013Bh
SPC T10/0995-D revision 11a
013Ch
SPC ANSI INCITS 301-1997


0140h
MMC (no version claimed)
015Bh
MMC T10/1048-D revision 10a
015Ch
MMC ANSI INCITS 304-1997
0160h
SCC (no version claimed)
017Bh
SCC T10/1047-D revision 06c
017Ch
SCC ANSI INCITS 276-1997
0180h
SBC (no version claimed)
019Bh
SBC T10/0996-D revision 08c
019Ch
SBC ANSI INCITS 306-1998
01A0h
SMC (no version claimed)
01BBh
SMC T10/0999-D revision 10a
01BCh
SMC ANSI INCITS 314-1998
01BEh
SMC ISO/IEC 14776-351
01C0h
SES (no version claimed)
01DBh
SES T10/1212-D revision 08b
01DCh
SES ANSI INCITS 305-1998
01DDh
SES T10/1212 revision 08b w/ Amendment ANSI
INCITS.305/AM1-2000
01DEh
SES ANSI INCITS 305-1998 w/ Amendment ANSI
INCITS.305/AM1-2000
01E0h
SCC-2 (no version claimed)
01FBh
SCC-2 T10/1125-D revision 04
01FCh
SCC-2 ANSI INCITS 318-1998
0200h
SSC (no version claimed)
0201h
SSC T10/0997-D revision 17
0207h
SSC T10/0997-D revision 22
021Ch
SSC ANSI INCITS 335-2000
0220h
RBC (no version claimed)
0238h
RBC T10/1240-D revision 10a
023Ch
RBC ANSI INCITS 330-2000
Table E.18 — Version descriptor assignments (part 2 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0240h
MMC-2 (no version claimed)
0255h
MMC-2 T10/1228-D revision 11
025Bh
MMC-2 T10/1228-D revision 11a
025Ch
MMC-2 ANSI INCITS 333-2000
0260h
SPC-2 (no version claimed)
0267h
SPC-2 T10/1236-D revision 12
0269h
SPC-2 T10/1236-D revision 18
0275h
SPC-2 T10/1236-D revision 19
0276h
SPC-2 T10/1236-D revision 20
0277h
SPC-2 ANSI INCITS 351-2001
0278h
SPC-2 ISO/IEC 14776-452
0280h
OCRW (no version claimed)
029Eh
OCRW ISO/IEC 14776-381
02A0h
MMC-3 (no version claimed)
02B5h
MMC-3 T10/1363-D revision 9
02B6h
MMC-3 T10/1363-D revision 10g
02B8h
MMC-3 ANSI INCITS 360-2002
02E0h
SMC-2 (no version claimed)
02F5h
SMC-2 T10/1383-D revision 5
02FCh
SMC-2 T10/1383-D revision 6
02FDh
SMC-2 T10/1383-D revision 7
02FEh
SMC-2 ANSI INCITS 382-2004
0300h
SPC-3 (no version claimed)
0301h
SPC-3 T10/1416-D revision 7
0307h
SPC-3 T10/1416-D revision 21
030Fh
SPC-3 T10/1416-D revision 22
0312h
SPC-3 T10/1416-D revision 23
0314h
SPC-3 ANSI INCITS 408-2005
0316h
SPC-3 ISO/IEC 14776-453
Table E.18 — Version descriptor assignments (part 3 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0320h
SBC-2 (no version claimed)
0322h
SBC-2 T10/1417-D revision 5a
0324h
SBC-2 T10/1417-D revision 15
033Bh
SBC-2 T10/1417-D revision 16
033Dh
SBC-2 ANSI INCITS 405-2005
033Eh
SBC-2 ISO/IEC 14776-322
0340h
OSD (no version claimed)
0341h
OSD T10/1355-D revision 0
0342h
OSD T10/1355-D revision 7a
0343h
OSD T10/1355-D revision 8
0344h
OSD T10/1355-D revision 9
0355h
OSD T10/1355-D revision 10
0356h
OSD ANSI INCITS 400-2004
0360h
SSC-2 (no version claimed)
0374h
SSC-2 T10/1434-D revision 7
0375h
SSC-2 T10/1434-D revision 9
037Dh
SSC-2 ANSI INCITS 380-2003
0380h
BCC (no version claimed)
03A0h
MMC-4 (no version claimed)
03B0h
MMC-4 T10/1545-D revision 5
03B1h
MMC-4 T10/1545-D revision 5a
03BDh
MMC-4 T10/1545-D revision 3
03BEh
MMC-4 T10/1545-D revision 3d
03BFh
MMC-4 ANSI INCITS 401-2005
03C0h
ADC (no version claimed)
03D5h
ADC T10/1558-D revision 6
03D6h
ADC T10/1558-D revision 7
03D7h
ADC ANSI INCITS 403-2005
03E0h
SES-2 (no version claimed)
Table E.18 — Version descriptor assignments (part 4 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


03E1h
SES-2 T10/1559-D revision 16
03E7h
SES-2 T10/1559-D revision 19
03EBh
SES-2 T10/1559-D revision 20
03F0h
SES-2 ANSI INCITS 448-2008
03F2h
SES-2 ISO/IEC 14776-372
0400h
SSC-3 (no version claimed)
0403h
SSC-3 T10/1611-D revision 04a
0407h
SSC-3 T10/1611-D revision 05
0409h
SSC-3 ANSI INCITS 467-2011
0420h
MMC-5 (no version claimed)
042Fh
MMC-5 T10/1675-D revision 03
0431h
MMC-5 T10/1675-D revision 03b
0432h
MMC-5 T10/1675-D revision 04
0434h
MMC-5 ANSI INCITS 430-2007
0440h
OSD-2 (no version claimed)
0444h
OSD-2 T10/1729-D revision 4
0446h
OSD-2 T10/1729-D revision 5
0448h
OSD-2 ANSI INCITS 458-2011
0460h
SPC-4 (no version claimed)
0461h
SPC-4 T10/1731-D revision 16
0462h
SPC-4 T10/1731-D revision 18
0463h
SPC-4 T10/1731-D revision 23
0466h
SPC-4 T10/1731-D revision 36
0480h
SMC-3 (no version claimed)
0482h
SMC-3 T10/1730-D revision 15
0484h
SMC-3 T10/1730-D revision 16
04A0h
ADC-2 (no version claimed)
04A7h
ADC-2 T10/1741-D revision 7
04AAh
ADC-2 T10/1741-D revision 8
Table E.18 — Version descriptor assignments (part 5 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


04ACh
ADC-2 ANSI INCITS 441-2008
04C0h
SBC-3 (no version claimed)
04E0h
MMC-6 (no version claimed)
04E3h
MMC-6 T10/1836-D revision 02b
04E5h
MMC-6 T10/1836-D revision 02g
04E6h
MMC-6 ANSI INCITS 468-2010
0500h
ADC-3 (no version claimed)
0502h
ADC-3 T10/1895-D revision 04
0504h
ADC-3 T10/1895-D revision 05
0506h
ADC-3 T10/1895-D revision 05a
0520h
SSC-4 (no version claimed)
0523h
SSC-4 T10/2123-D revision 2
0560h
OSD-3 (no version claimed)
0580h
SES-3 (no version claimed)
05A0h
SSC-5 (no version claimed)
05C0h
SPC-5 (no version claimed)
05E0h
SFSC (no version claimed)
0820h
SSA-TL2 (no version claimed)
083Bh
SSA-TL2 T10.1/1147-D revision 05b
083Ch
SSA-TL2 ANSI INCITS 308-1998
0840h
SSA-TL1 (no version claimed)
085Bh
SSA-TL1 T10.1/0989-D revision 10b
085Ch
SSA-TL1 ANSI INCITS 295-1996
0860h
SSA-S3P (no version claimed)
087Bh
SSA-S3P T10.1/1051-D revision 05b
087Ch
SSA-S3P ANSI INCITS 309-1998
0880h
SSA-S2P (no version claimed)
089Bh
SSA-S2P T10.1/1121-D revision 07b
089Ch
SSA-S2P ANSI INCITS 294-1996
Table E.18 — Version descriptor assignments (part 6 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


08A0h
SIP (no version claimed)
08BBh
SIP T10/0856-D revision 10
08BCh
SIP ANSI INCITS 292-1997
08C0h
FCP (no version claimed)
08DBh
FCP T10/0993-D revision 12
08DCh
FCP ANSI INCITS 269-1996
08E0h
SBP-2 (no version claimed)
08FBh
SBP-2 T10/1155-D revision 04
08FCh
SBP-2 ANSI INCITS 325-1998
0900h
FCP-2 (no version claimed)
0901h
FCP-2 T10/1144-D revision 4
0915h
FCP-2 T10/1144-D revision 7
0916h
FCP-2 T10/1144-D revision 7a
0917h
FCP-2 ANSI INCITS 350-2003
0918h
FCP-2 T10/1144-D revision 8
0920h
SST (no version claimed)
0935h
SST T10/1380-D revision 8b
0940h
SRP (no version claimed)
0954h
SRP T10/1415-D revision 10
0955h
SRP T10/1415-D revision 16a
095Ch
SRP ANSI INCITS 365-2002
0960h
iSCSI (no version claimed)
0980h
SBP-3 (no version claimed)
0982h
SBP-3 T10/1467-D revision 1f
0994h
SBP-3 T10/1467-D revision 3
099Ah
SBP-3 T10/1467-D revision 4
099Bh
SBP-3 T10/1467-D revision 5
099Ch
SBP-3 ANSI INCITS 375-2004
09C0h
ADP (no version claimed)
Table E.18 — Version descriptor assignments (part 7 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


09E0h
ADT (no version claimed)
09F9h
ADT T10/1557-D revision 11
09FAh
ADT T10/1557-D revision 14
09FDh
ADT ANSI INCITS 406-2005
0A00h
FCP-3 (no version claimed)
0A07h
FCP-3 T10/1560-D revision 3f
0A0Fh
FCP-3 T10/1560-D revision 4
0A11h
FCP-3 ANSI INCITS 416-2006
0A1Ch
FCP-3 ISO/IEC 14776-223
0A20h
ADT-2 (no version claimed)
0A22h
ADT-2 T10/1742-D revision 06
0A27h
ADT-2 T10/1742-D revision 08
0A28h
ADT-2 T10/1742-D revision 09
0A2Bh
ADT-2 ANSI INCITS 472-2011
0A40h
FCP-4 (no version claimed)
0A42h
FCP-4 T10/1828-D revision 01
0A44h
FCP-4 T10/1828-D revision 02
0A45h
FCP-4 T10/1828-D revision 02b
0A46h
FCP-4 ANSI INCITS 481-2012
0AA0h
SPI (no version claimed)
0AB9h
SPI T10/0855-D revision 15a
0ABAh
SPI ANSI INCITS 253-1995
0ABBh
SPI T10/0855-D revision 15a with SPI Amnd revision 3a
0ABCh
SPI ANSI INCITS 253-1995 with SPI Amnd ANSI INCITS
253/AM1-1998
0AC0h
Fast-20 (no version claimed)
0ADBh
Fast-20 T10/1071 revision 06
0ADCh
Fast-20 ANSI INCITS 277-1996
0AE0h
SPI-2 (no version claimed)
Table E.18 — Version descriptor assignments (part 8 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0AFBh
SPI-2 T10/1142-D revision 20b
0AFCh
SPI-2 ANSI INCITS 302-1999
0B00h
SPI-3 (no version claimed)
0B18h
SPI-3 T10/1302-D revision 10
0B19h
SPI-3 T10/1302-D revision 13a
0B1Ah
SPI-3 T10/1302-D revision 14
0B1Ch
SPI-3 ANSI INCITS 336-2000
0B20h
EPI (no version claimed)
0B3Bh
EPI T10/1134 revision 16
0B3Ch
EPI ANSI INCITS TR-23 1999
0B40h
SPI-4 (no version claimed)
0B54h
SPI-4 T10/1365-D revision 7
0B55h
SPI-4 T10/1365-D revision 9
0B56h
SPI-4 ANSI INCITS 362-2002
0B59h
SPI-4 T10/1365-D revision 10
0B60h
SPI-5 (no version claimed)
0B79h
SPI-5 T10/1525-D revision 3
0B7Ah
SPI-5 T10/1525-D revision 5
0B7Bh
SPI-5 T10/1525-D revision 6
0B7Ch
SPI-5 ANSI INCITS 367-2003
0BE0h
SAS (no version claimed)
0BE1h
SAS T10/1562-D revision 01
0BF5h
SAS T10/1562-D revision 03
0BFAh
SAS T10/1562-D revision 04
0BFBh
SAS T10/1562-D revision 04
0BFCh
SAS T10/1562-D revision 05
0BFDh
SAS ANSI INCITS 376-2003
0C00h
SAS-1.1 (no version claimed)
0C07h
SAS-1.1 T10/1601-D revision 9
Table E.18 — Version descriptor assignments (part 9 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0C0Fh
SAS-1.1 T10/1601-D revision 10
0C11h
SAS-1.1 ANSI INCITS 417-2006
0C12h
SAS-1.1 ISO/IEC 14776-151
0C20h
SAS-2 (no version claimed)
0C23h
SAS-2 T10/1760-D revision 14
0C27h
SAS-2 T10/1760-D revision 15
0C28h
SAS-2 T10/1760-D revision 16
0C2Ah
SAS-2 ANSI INCITS 457-2010
0C40h
SAS-2.1 (no version claimed)
0C48h
SAS-2.1 T10/2125-D revision 04
0C4Ah
SAS-2.1 T10/2125-D revision 06
0C4Bh
SAS-2.1 T10/2125-D revision 07
0C4Eh
SAS-2.1 ANSI INCITS 478-2011
0C60h
SAS-3 (no version claimed)
0D20h
FC-PH (no version claimed)
0D3Bh
FC-PH ANSI INCITS 230-1994
0D3Ch
FC-PH ANSI INCITS 230-1994 with Amnd 1 ANSI INCITS
230/AM1-1996
0D40h
FC-AL (no version claimed)
0D5Ch
FC-AL ANSI INCITS 272-1996
0D60h
FC-AL-2 (no version claimed)
0D61h
FC-AL-2 T11/1133-D revision 7.0
0D63h
FC-AL-2 ANSI INCITS 332-1999 with AM1-2003 &
AM2-2006
0D64h
FC-AL-2 ANSI INCITS 332-1999 with Amnd 2 AM2-2006
0D65h
FC-AL-2 ISO/IEC 14165-122 with AM1 & AM2
0D7Ch
FC-AL-2 ANSI INCITS 332-1999
0D7Dh
FC-AL-2 ANSI INCITS 332-1999 with Amnd 1 AM1-2003
0D80h
FC-PH-3 (no version claimed)
0D9Ch
FC-PH-3 ANSI INCITS 303-1998
Table E.18 — Version descriptor assignments (part 10 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0DA0h
FC-FS (no version claimed)
0DB7h
FC-FS T11/1331-D revision 1.2
0DB8h
FC-FS T11/1331-D revision 1.7
0DBCh
FC-FS ANSI INCITS 373-2003
0DBDh
FC-FS ISO/IEC 14165-251
0DC0h
FC-PI (no version claimed)
0DDCh
FC-PI ANSI INCITS 352-2002
0DE0h
FC-PI-2 (no version claimed)
0DE2h
FC-PI-2 T11/1506-D revision 5.0
0DE4h
FC-PI-2 ANSI INCITS 404-2006
0E00h
FC-FS-2 (no version claimed)
0E02h
FC-FS-2 ANSI INCITS 242-2007
0E03h
FC-FS-2 ANSI INCITS 242-2007 with AM1 ANSI INCITS
242/AM1-2007
0E20h
FC-LS (no version claimed)
0E21h
FC-LS T11/1620-D revision 1.62
0E29h
FC-LS ANSI INCITS 433-2007
0E40h
FC-SP (no version claimed)
0E42h
FC-SP T11/1570-D revision 1.6
0E45h
FC-SP ANSI INCITS 426-2007
0E60h
FC-PI-3 (no version claimed)
0E62h
FC-PI-3 T11/1625-D revision 2.0
0E68h
FC-PI-3 T11/1625-D revision 2.1
0E6Ah
FC-PI-3 T11/1625-D revision 4.0
0E6Eh
FC-PI-3 ANSI INCITS 460-2011
0E80h
FC-PI-4 (no version claimed)
0E82h
FC-PI-4 T11/1647-D revision 8.0
0E88h
FC-PI-4 ANSI INCITS 450-2009
0EA0h
FC 10GFC (no version claimed)
Table E.18 — Version descriptor assignments (part 11 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


0EA2h
FC 10GFC ANSI INCITS 364-2003
0EA3h
FC 10GFC ISO/IEC 14165-116
0EA5h
FC 10GFC ISO/IEC 14165-116 with AM1
0EA6h
FC 10GFC ANSI INCITS 364-2003 with AM1 ANSI INCITS
364/AM1-2007
0EC0h
FC-SP-2 (no version claimed)
0EE0h
FC-FS-3 (no version claimed)
0EE2h
FC-FS-3 T11/1861-D revision 0.9
0EE7h
FC-FS-3 T11/1861-D revision 1.0
0EE9h
FC-FS-3 T11/1861-D revision 1.10
0EEBh
FC-FS-3 ANSI INCITS 470-2011
0F00h
FC-LS-2 (no version claimed)
0F03h
FC-LS-2 T11/2103-D revision 2.11
0F05h
FC-LS-2 T11/2103-D revision 2.21
0F07h
FC-LS-2 ANSI INCITS 477-2011
0F20h
FC-PI-5 (no version claimed)
0F27h
FC-PI-5 T11/2118-D revision 2.00
0F28h
FC-PI-5 T11/2118-D revision 3.00
0F2Ah
FC-PI-5 T11/2118-D revision 6.00
0F2Bh
FC-PI-5 T11/2118-D revision 6.10
0F2Eh
FC-PI-5 ANSI INCITS 479-2011
0F40h
FC-PI-6 (no version claimed)
0F60h
FC-FS-4 (no version claimed)
0F80h
FC-LS-3 (no version claimed)
12A0h
FC-SCM (no version claimed)
12A3h
FC-SCM T11/1824DT revision 1.0
12A5h
FC-SCM T11/1824DT revision 1.1
12A7h
FC-SCM T11/1824DT revision 1.4
12AAh
FC-SCM INCITS TR-47 2012
Table E.18 — Version descriptor assignments (part 12 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


12C0h
FC-DA-2 (no version claimed)
12C3h
FC-DA-2 T11/1870DT revision 1.04
12C5h
FC-DA-2 T11/1870DT revision 1.06
12C9h
FC-DA-2 INCITS TR-49 2012
12E0h
FC-DA (no version claimed)
12E2h
FC-DA T11/1513-DT revision 3.1
12E8h
FC-DA ANSI INCITS TR-36 2004
12E9h
FC-DA ISO/IEC 14165-341
1300h
FC-Tape (no version claimed)
1301h
FC-Tape T11/1315 revision 1.16
131Bh
FC-Tape T11/1315 revision 1.17
131Ch
FC-Tape ANSI INCITS TR-24 1999
1320h
FC-FLA (no version claimed)
133Bh
FC-FLA T11/1235 revision 7
133Ch
FC-FLA ANSI INCITS TR-20 1998
1340h
FC-PLDA (no version claimed)
135Bh
FC-PLDA T11/1162 revision 2.1
135Ch
FC-PLDA ANSI INCITS TR-19 1998
1360h
SSA-PH2 (no version claimed)
137Bh
SSA-PH2 T10.1/1145-D revision 09c
137Ch
SSA-PH2 ANSI INCITS 293-1996
1380h
SSA-PH3 (no version claimed)
139Bh
SSA-PH3 T10.1/1146-D revision 05b
139Ch
SSA-PH3 ANSI INCITS 307-1998
14A0h
IEEE 1394 (no version claimed)
14BDh
ANSI IEEE 1394-1995
14C0h
IEEE 1394a (no version claimed)
14E0h
IEEE 1394b (no version claimed)
15E0h
ATA/ATAPI-6 (no version claimed)
Table E.18 — Version descriptor assignments (part 13 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


15FDh
ATA/ATAPI-6 ANSI INCITS 361-2002
1600h
ATA/ATAPI-7 (no version claimed)
1602h
ATA/ATAPI-7 T13/1532-D revision 3
161Ch
ATA/ATAPI-7 ANSI INCITS 397-2005
161Eh
ATA/ATAPI-7 ISO/IEC 24739
1620h
ATA/ATAPI-8 ATA8-AAM (no version claimed)
1621h
ATA/ATAPI-8 ATA8-APT Parallel Transport (no version
claimed)
1622h
ATA/ATAPI-8 ATA8-AST Serial Transport (no version
claimed)
1623h
ATA/ATAPI-8 ATA8-ACS ATA/ATAPI Command Set (no
version claimed)
1628h
ATA/ATAPI-8 ATA8-AAM ANSI INCITS 451-2008
162Ah
ATA/ATAPI-8 ATA8-ACS ANSI INCITS 452-2009 w/
Amendment 1
1728h
Universal Serial Bus Specification, Revision 1.1
1729h
Universal Serial Bus Specification, Revision 2.0
1730h
USB Mass Storage Class Bulk-Only Transport, Revision 1.0
1740h
UAS (no version claimed)
1743h
UAS T10/2095-D revision 02
1747h
UAS T10/2095-D revision 04
1748h
UAS ANSI INCITS 471-2010
1761h
ACS-2 (no version claimed)
1780h
UAS-2 (no version claimed)
1EA0h
SAT (no version claimed)
1EA7h
SAT T10/1711-D revision 8
1EABh
SAT T10/1711-D revision 9
1EADh
SAT ANSI INCITS 431-2007
1EC0h
SAT-2 (no version claimed)
1EC4h
SAT-2 T10/1826-D revision 06
Table E.18 — Version descriptor assignments (part 14 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


1EC8h
SAT-2 T10/1826-D revision 09
1ECAh
SAT-2 ANSI INCITS 465-2010
1EE0h
SAT-3 (no version claimed)
1EE2h
SAT-3 T10/2126-D revision 4
1F00h
SAT-4 (no version claimed)
20A0h
SPL (no version claimed)
20A3h
SPL T10/2124-D revision 6a
20A5h
SPL T10/2124-D revision 7
20A7h
SPL ANSI INCITS 476-2011
20A8h
SPL ANSI INCITS 476-2011 + SPL AM1 INCITS 476/AM1
20C0h
SPL-2 (no version claimed)
20C2h
SPL-2 T10/2228-D revision 4
20C4h
SPL-2 T10/2228-D revision 5
20E0h
SPL-3 (no version claimed)
21E0h
SOP (no version claimed)
2200h
PQI (no version claimed)
65472
FFC0h
IEEE 1667 (no version claimed)
65473
FFC1h
IEEE 1667-2006
65474
FFC2h
IEEE 1667-2009
Table E.18 — Version descriptor assignments (part 15 of 15)
Standard
Code
Revision
Code
Version
Descriptor Code
Standard
decimal
hex


Table E.19 shows the guidelines used by T10 when selecting a coded value for a standard.
Table E.19 — Standard code value guidelines (part 1 of 5)
Standard
Code
Standard or standards family
Version Descriptor Not Supported
1 to 8
Architecture Model
SAM
SAM-2
SAM-3
SAM-4
SAM-5
9 to 64
Command Set
SPC
MMC
SCC
SBC
SMC
SES
SCC-2
SSC
RBC
MMC-2
SPC-2
OCRW
MMC-3
obsolete
SMC-2
SPC-3
SBC-2
OSD
SSC-2
obsolete
MMC-4
ADC


SES-2
SSC-3
MMC-5
OSD-2
SPC-4
SMC-3
ADC-2
SBC-3
MMC-6
ADC-3
SSC-4
OSD-3
SES-3
SSC-5
SPC-5
SFSC
SBC-4
65 to 84
Physical Mapping Protocol
SSA-TL2
SSA-TL1
SSA-S3P
SSA-S2P
SIP
FCP
SBP-2
FCP-2
SST
SRP
iSCSI
SBP-3
obsolete
Table E.19 — Standard code value guidelines (part 2 of 5)
Standard
Code
Standard or standards family


ADP
ADT
FCP-3
ADT-2
FCP-4
85 to 94
Parallel SCSI Physical
SPI and SPI Amendment
Fast-20
SPI-2
SPI-3
EPI
SPI-4
SPI-5
95 to 104
Serial Attached SCSI
SAS
SAS-1.1
SAS-2
SAS-2.1
SAS-3
105 to 154
Fibre Channel
FC-PH and FC-PH Amendment
FC-AL
FC-AL-2
FC-PH-3
FC-FS
FC-PI
FC-PI-2
FC-FS-2
FC-LS
FC-SP
FC-PI-3
Table E.19 — Standard code value guidelines (part 3 of 5)
Standard
Code
Standard or standards family


FC-PI-4
FC 10GFC
FC-SP-2
FC-FS-3
FC-LS-2
FC-PI-5
FC-PI-6
FC-FS-4
FC-LS-3
FC-SCM
FC-DA-2
FC-DA
FC-Tape
FC-FLA
FC-PLDA
155 to 164
SSA
SSA-PH2
SSA-PH3
165 to 174
IEEE 1394
IEEE 1394:1995
IEEE 1394a
IEEE 1394b
175 to 200
ATAPI & USB
ATA/ATAPI-6
ATA/ATAPI-7
ATA/ATAPI-8
USB
UAS
ACS-x
UAS-2
201 to 224
Networking
Table E.19 — Standard code value guidelines (part 4 of 5)
Standard
Code
Standard or standards family


225 to 244
ATM
245 to 260
Translators
SAT
SAT-2
SAT-3
SAT-4
261 to 270
SAS Transport Protocols
SPL
SPL-2
SPL-3
271 to 290
SCSI over PCI Express Transport Protocols
SOP
PQI
SOP-2
PQI-2
291 to 2045
Reserved for Expansion
IEEE 1667
Reserved
Table E.19 — Standard code value guidelines (part 5 of 5)
Standard
Code
Standard or standards family


E.10 T10 IEEE binary identifiers
The IEEE binary identifiers assigned to T10 standards are shown in table E.20.
Table E.20 — IEEE binary identifiers assigned by T10
IEEE Binary Identifier
T10 Standard
0060 9E01 03E0h
SBP (obsolete)
0060 9E01 0483h
SBP-2
0060 9E01 04D8h
SPC-2
0060 9E01 05BBh
SBP-3
0060 9E01 0800h
SRP revision 10
0060 9E01 0801h
ANSI SRP


Annex F
(informative)
T10 vendor identification
This annex contains the list of T10 vendor identifications (see table F.1) as of the date of this document. The
purpose of this list is to help avoid redundant usage of T10 vendor identifications. Technical Committee T10 of
Accredited Standards Committee INCITS maintains an informal list of T10 vendor identifications currently in
use. The T10 web site, http://www.t10.org, provides a convenient means to request an identification code. If
problems are encountered using the T10 web site, please contact the chairman of T10 prior to using a new
T10 vendor identification to avoid conflicts.
The information in this annex was complete and accurate at the time of publication. However, the information
is subject to change. Technical Committee T10 of INCITS maintains an electronic copy of this information on
its world wide web site (http://www.t10.org/). In the event that the T10 world wide web site is no longer active,
access may be possible via the INCITS world wide web site (http://www.incits.org), the ANSI world wide web
site (http://www.ansi.org), the IEC site (http://www.iec.ch/), the ISO site (http://www.iso.ch/), or the ISO/IEC
JTC 1 web site (http://www.jtc1.org/).
Table F.1 — T10 vendor identification list (part 1 of 16)
ID
Organization
0B4C
MOOSIK Ltd.
2AI
2AI (Automatisme et Avenir Informatique)
3M
3M Company
3nhtech
3NH Technologies
3PARdata
3PARdata, Inc. (now HP)
A-Max
A-Max Technology Co., Ltd
ABSOLUTE
Absolute Analysis
ACARD
ACARD Technology Corp.
Accusys
Accusys INC.
Acer
Acer, Inc.
ACL
Automated Cartridge Librarys, Inc.
Acuid
Acuid Corporation Ltd.
AcuLab
AcuLab, Inc. (Tulsa, OK)
ADAPTEC
Adaptec (now PMC-Sierra)
ADIC
Advanced Digital Information Corporation
ADSI
Adaptive Data Systems, Inc. (a Western Digital subsidiary)
ADTX
ADTX Co., Ltd.
ADVA
ADVA Optical Networking AG
AEM
AEM Performance Electronics
AERONICS
Aeronics, Inc.
AGFA
AGFA
Agilent
Agilent Technologies
AIC
Advanced Industrial Computer, Inc.
AIPTEK
AIPTEK International Inc.
ALCOR
Alcor Micro, Corp.
AMCC
Applied Micro Circuits Corporation
AMCODYNE
Amcodyne
Amgeon
Amgeon LLC


AMI
American Megatrends, Inc.
AMPEX
Ampex Data Systems
Amphenol
Amphenol
Amtl
Tenlon Technology Co.,Ltd
ANAMATIC
Anamartic Limited (England)
Ancor
Ancor Communications, Inc.
ANCOT
ANCOT Corp.
ANDATACO
Andataco  (now nStor)
andiamo
Andiamo Systems, Inc.
ANOBIT
Anobit
ANRITSU
Anritsu Corporation
ANTONIO
Antonio Precise Products Manufactory Ltd.
AoT
Art of Technology AG
APPLE
Apple Computer, Inc.
ARCHIVE
Archive
ARDENCE
Ardence Inc
Areca
Areca Technology Corporation
Arena
MaxTronic International Co., Ltd.
ARIO
Ario Data Networks, Inc.
ARISTOS
Aristos Logic Corp. (now part of PMC Sierra)
ARK
ARK Research Corporation
ARTECON
Artecon Inc.  (Obs. - now Dot Hill)
Artistic
Artistic Licence (UK) Ltd
ARTON
Arton Int.
ASACA
ASACA Corp.
ASC
Advanced Storage Concepts, Inc.
ASPEN
Aspen Peripherals
AST
AST Research
ASTEK
Astek Corporation
ASTK
Alcatel STK A/S
ASTUTE
Astute Networks, Inc.
AT&T
AT&T
ATA
SCSI / ATA Translator Software (Organization Not Specified)
ATARI
Atari Corporation
ATech
ATech electronics
ATG CYG
ATG Cygnet Inc.
ATL
Quantum|ATL Products
ATTO
ATTO Technology Inc.
ATTRATEC
Attratech Ltd liab. Co
ATX
Alphatronix
AURASEN
Aurasen Limited
AVC
AVC Technology Ltd
AVIDVIDR
AVID Technologies, Inc.
AVR
Advanced Vision Research
AXSTOR
AXSTOR
BALLARD
Ballard Synergy Corp.
Barco
Barco
Table F.1 — T10 vendor identification list (part 2 of 16)
ID
Organization


BAROMTEC
Barom Technologies Co., Ltd.
Bassett
Bassett Electronic Systems Ltd
BDT
BDT AG
BECEEM
Beceem Communications, Inc
BENQ
BENQ Corporation.
BERGSWD
Berg Software Design
BEZIER
Bezier Systems, Inc.
BHTi
Breece Hill Technologies
BIOS
BIOS Corporation
BIR
Bio-Imaging Research, Inc.
BiT
BiT Microsystems (obsolete, new ID: BITMICRO)
BITMICRO
BiT Microsystems, Inc.
Blendlgy
Blendology Limited
BLOOMBAS
Bloombase Technologies Limited
BlueArc
BlueArc Corporation
BNCHMARK
Benchmark Tape Systems Corporation
Bosch
Robert Bosch GmbH
Botman
Botmanfamily Electronics
BoxHill
Box Hill Systems Corporation  (Obs. - now Dot Hill)
BRDGWRKS
Bridgeworks Ltd.
BREA
BREA Technologies, Inc.
BREECE
Breece Hill LLC
Broadcom
Broadcom Corporation
BROCADE
Brocade Communications Systems, Incorporated
BUFFALO
BUFFALO INC.
BULL
Bull Peripherals Corp.
BUSLOGIC
BusLogic Inc.
BVIRTUAL
B-Virtual N.V.
CalComp
CalComp, A Lockheed Company
CALCULEX
CALCULEX, Inc.
CALIPER
Caliper (California Peripheral Corp.)
CAMBEX
Cambex Corporation
CAMEOSYS
Cameo Systems Inc.
CANDERA
Candera Inc.
CAPTION
CAPTION BANK
CAST
Advanced Storage Tech
CATALYST
Catalyst Enterprises
CCDISK
iSCSI Cake
CDC
Control Data or MPI
CDP
Columbia Data Products
Celsia
A M Bromley Limited
CenData
Central Data Corporation
Cereva
Cereva Networks Inc.
CERTANCE
Certance
Chantil
Chantil Technology
CHEROKEE
Cherokee Data Systems
CHINON
Chinon
Table F.1 — T10 vendor identification list (part 3 of 16)
ID
Organization


CHRISTMA
Christmann Informationstechnik + Medien GmbH & Co KG
CIE&YED
YE Data, C.Itoh Electric Corp.
CIPHER
Cipher Data Products
Ciprico
Ciprico, Inc.
CIRRUSL
Cirrus Logic Inc.
CISCO
Cisco Systems, Inc.
CLOVERLF
Cloverleaf Communications, Inc
CLS
Celestica
CMD
CMD Technology Inc.
CMTechno
CMTech
CNGR SFW
Congruent Software, Inc.
CNSi
Chaparral Network Storage, Inc.
CNT
Computer Network Technology
COBY
Coby Electronics Corporation, USA
COGITO
Cogito
COMPAQ
Compaq Computer Corporation (now HP)
COMPELNT
Compellent Technologies, Inc. (now Dell)
COMPORT
Comport Corp.
COMPSIG
Computer Signal Corporation
COMPTEX
Comptex Pty Limited
CONNER
Conner Peripherals
COPANSYS
COPAN SYSTEMS INC
CORAID
Coraid, Inc
CORE
Core International, Inc.
CORERISE
Corerise Electronics
COVOTE
Covote GmbH & Co KG
COWON
COWON SYSTEMS, Inc.
CPL
Cross Products Ltd
CPU TECH
CPU Technology, Inc.
CREO
Creo Products Inc.
CROSFLD
Crosfield Electronics (now FujiFilm Electonic Imaging Ltd)
CROSSRDS
Crossroads Systems, Inc.
crosswlk
Crosswalk, Inc.
CSCOVRTS
Cisco - Veritas
CSM, INC
Computer SM, Inc.
Cunuqui
CUNUQUI SLU
CYBERNET
Cybernetics
Cygnal
Dekimo
D Bit
Digby’s Bitpile, Inc. DBA D Bit
DALSEMI
Dallas Semiconductor
DANEELEC
Dane-Elec
DANGER
Danger Inc.
DAT-MG
DAT Manufacturers Group
Data Com
Data Com Information Systems Pty. Ltd.
DATABOOK
Databook, Inc.
DATACOPY
Datacopy Corp.
DataCore
DataCore Software Corporation
Table F.1 — T10 vendor identification list (part 4 of 16)
ID
Organization


DATAPT
Datapoint Corp.
DATARAM
Dataram Corporation
DAVIS
Daviscomms (S) Pte Ltd
DDN
DataDirect Networks, Inc.
DDRDRIVE
DDRdrive LLC
DE
Dimension Engineering LLC
DEC
Digital Equipment Corporation (now HP)
DEI
Digital Engineering, Inc.
DELL
Dell, Inc.
DELPHI
Delphi Data Div. of Sparks Industries, Inc.
DENON
Denon/Nippon Columbia
DenOptix
DenOptix, Inc.
DEST
DEST Corp.
DFC
DavioFranke.com
DGC
Data General Corp.
DIGIDATA
Digi-Data Corporation
DigiIntl
Digi International
Digital
Digital Equipment Corporation (now HP)
DILOG
Distributed Logic Corp.
DISC
Document Imaging Systems Corp.
DLNET
Driveline
DNS
Data and Network Security
DNUK
Digital Networks Uk Ltd
DotHill
Dot Hill Systems Corp.
DP
Dell, Inc.
DPT
Distributed Processing Technology
DROBO
Data Robotics, Inc.
DSC
DigitalStream Corporation
DSI
Data Spectrum, Inc.
DSM
Deterner Steuerungs- und Maschinenbau GmbH & Co.
DSNET
Cleversafe, Inc.
DT
Double-Take Software, INC.
DTC QUME
Data Technology Qume
DXIMAGIN
DX Imaging
EARTHLAB
EarthLabs
EarthLCD
Earth Computer Technologies, Inc.
ECCS
ECCS, Inc.
ECMA
European Computer Manufacturers Association
EDS
Embedded Data Systems
ELE Intl
ELE International
ELEGANT
Elegant Invention, LLC
Elektron
Elektron Music Machines MAV AB
elipsan
Elipsan UK Ltd.
Elms
Elms Systems Corporation
ELSE
ELSE Ltd.
ELSEC
Littlemore Scientific
EMASS
EMASS, Inc.
Table F.1 — T10 vendor identification list (part 5 of 16)
ID
Organization


EMC
EMC Corp.
EMiT
EMiT Conception Eletronique
EMTEC
EMTEC Magnetics
EMULEX
Emulex
ENERGY-B
Energybeam Corporation
ENGENIO
Engenio Information Technologies, Inc.
ENMOTUS
Enmotus Inc
Entacore
Entacore
EPOS
EPOS Technologies Ltd.
EPSON
Epson
EQLOGIC
EqualLogic
Eris/RSI
RSI Systems, Inc.
ETERNE
EterneData Technology Co.,Ltd.(China PRC.)
EuroLogc
Eurologic Systems Limited (now part of PMC Sierra)
evolve
Evolution Technologies, Inc
EXABYTE
Exabyte Corp. (now part of Tandberg)
EXATEL
Exatelecom Co., Ltd.
EXAVIO
Exavio, Inc.
Exsequi
Exsequi Ltd
Exxotest
Annecy Electronique
FAIRHAVN
Fairhaven Health, LLC
FALCON
FalconStor, Inc.
FFEILTD
FujiFilm Electonic Imaging Ltd
Fibxn
Fiberxon, Inc.
FID
First International Digital, Inc.
FILENET
FileNet Corp.
FirmFact
Firmware Factory Ltd
FLYFISH
Flyfish Technologies
FOXCONN
Foxconn Technology Group
FRAMDRV
FRAMEDRIVE Corp.
FREECION
Nable Communications, Inc.
FSC
Fujitsu Siemens Computers
FTPL
Frontline Technologies Pte Ltd
FUJI
Fuji Electric Co., Ltd. (Japan)
FUJIFILM
Fuji Photo Film, Co., Ltd.
FUJITSU
Fujitsu
FUNAI
Funai Electric Co., Ltd.
FUSIONIO
Fusion-io Inc.
FUTURED
Future Domain Corp.
G&D
Giesecke & Devrient GmbH
G.TRONIC
Globaltronic - Electronica e Telecomunicacoes, S.A.
Gadzoox
Gadzoox Networks, Inc. (now part of Broadcom)
Gammaflx
Gammaflux L.P.
GDI
Generic Distribution International
GEMALTO
gemalto
Gen_Dyn
General Dynamics
Generic
Generic Technology Co., Ltd.
Table F.1 — T10 vendor identification list (part 6 of 16)
ID
Organization


GENSIG
General Signal Networks
GEO
Green Energy Options Ltd
GIGATAPE
GIGATAPE GmbH
GIGATRND
GigaTrend Incorporated
Global
Global Memory Test Consortium
Gnutek
Gnutek Ltd.
Goidelic
Goidelic Precision, Inc.
GoldKey
GoldKey Security Corporation
GoldStar
LG Electronics Inc.
GORDIUS
Gordius
GOULD
Gould
HAGIWARA
Hagiwara Sys-Com Co., Ltd.
HAPP3
Inventec Multimedia and Telecom co., ltd
HDS
Horizon Data Systems, Inc.
Heydays
Mazo Technology Co., Ltd.
HGST
HGST a Western Digital Company
HI-TECH
HI-TECH Software Pty. Ltd.
HITACHI
Hitachi America Ltd or Nissei Sangyo America Ltd
HL-DT-ST
Hitachi-LG Data Storage, Inc.
HONEYWEL
Honeywell Inc.
Hoptroff
HexWax Ltd
HORIZONT
Horizontigo Software
HP
Hewlett Packard
HPQ
Hewlett Packard
HUASY
Huawei Symantec Technologies Co., Ltd.
HYUNWON
HYUNWON inc
i-cubed
i-cubed ltd.
IBM
International Business Machines
Icefield
Icefield Tools Corporation
Iceweb
Iceweb Storage Corp
ICL
ICL
ICP
ICP vortex Computersysteme GmbH
IDE
International Data Engineering, Inc.
IDG
Interface Design Group
IET
ISCSI ENTERPRISE TARGET
IFT
Infortrend Technology, Inc.
IGR
Intergraph Corp.
IMAGO
IMAGO SOFTWARE SL
IMATION
Imation
IMPLTD
Integrated Micro Products Ltd.
IMPRIMIS
Imprimis Technology Inc.
INCIPNT
Incipient Technologies Inc.
INCITS
InterNational Committee for Information Technology
INDCOMP
Industrial Computing Limited
Indigita
Indigita Corporation
INITIO
Initio Corporation
INRANGE
INRANGE Technologies Corporation
Table F.1 — T10 vendor identification list (part 7 of 16)
ID
Organization


Insight
L-3 Insight Technology Inc
INSITE
Insite Peripherals
integrix
Integrix, Inc.
INTEL
Intel Corporation
Intransa
Intransa, Inc.
IOC
I/O Concepts, Inc.
iofy
iofy Corporation
IOMEGA
Iomega
IOT
IO Turbine, Inc.
iPaper
intelliPaper, LLC
iqstor
iQstor Networks, Inc.
iQue
iQue
ISi
Information Storage inc.
Isilon
Isilon Systems, Inc.
ISO
International Standards Organization
iStor
iStor Networks, Inc.
ITC
International Tapetronics Corporation
iTwin
iTwin Pte Ltd
IVIVITY
iVivity, Inc.
IVMMLTD
InnoVISION Multimedia Ltd.
JABIL001
Jabil Circuit
JETWAY
Jetway Information Co., Ltd
JMR
JMR Electronics Inc.
JOLLYLOG
Jolly Logic
JPC Inc.
JPC Inc.
JSCSI
jSCSI Project
Juniper
Juniper Networks
JVC
JVC Information Products Co.
KASHYA
Kashya, Inc.
KENNEDY
Kennedy Company
KENWOOD
KENWOOD Corporation
KEWL
Shanghai KEWL Imp&Exp Co., Ltd.
Key Tech
Key Technologies, Inc
KMNRIO
Kaminario Technologies Ltd.
KODAK
Eastman Kodak
KONAN
Konan
koncepts
koncepts International Ltd.
KONICA
Konica Japan
KOVE
KOVE
KSCOM
KSCOM Co. Ltd.,
KUDELSKI
Nagravision SA - Kudelski Group
Kyocera
Kyocera Corporation
Lapida
Gonmalo Electronics
LAPINE
Lapine Technology
LASERDRV
LaserDrive Limited
LASERGR
Lasergraphics, Inc.
LeapFrog
LeapFrog Enterprises, Inc.
Table F.1 — T10 vendor identification list (part 8 of 16)
ID
Organization


LEFTHAND
LeftHand Networks (now HP)
Leica
Leica Camera AG
Lexar
Lexar Media, Inc.
LEYIO
LEYIO
LG
LG Electronics Inc.
LGE
LG Electronics Inc.
LION
Lion Optics Corporation
LMS
Laser Magnetic Storage International Company
LoupTech
Loup Technologies, Inc.
LSI
LSI Corp. (was LSI Logic Corp.)
LSILOGIC
LSI Logic Storage Systems, Inc.
LTO-CVE
Linear Tape - Open, Compliance Verification Entity
LUXPRO
Luxpro Corporation
Malakite
Malachite Technologies (New VID is: Sandial)
MarcBoon
marcboon.com
Marner
Marner Storage Technologies, Inc.
MARVELL
Marvell Semiconductor, Inc.
MATSHITA
Matsushita
MAXELL
Hitachi Maxell, Ltd.
MAXIM-IC
Maxim Integrated Products
MaxOptix
Maxoptix Corp.
MAXSTRAT
Maximum Strategy, Inc.
MAXTOR
Maxtor Corp.
MaXXan
MaXXan Systems, Inc.
MAYCOM
maycom Co., Ltd.
MBEAT
K-WON C&C Co.,Ltd
MCC
Measurement Computing Corporation
McDATA
McDATA Corporation
MCUBE
Mcube Technology Co., Ltd.
MDI
Micro Design International, Inc.
MEADE
Meade Instruments Corporation
mediamat
mediamatic
MEII
Mountain Engineering II, Inc.
MELA
Mitsubishi Electronics America
MELCO
Mitsubishi Electric (Japan)
mellanox
Mellanox Technologies Ltd.
MEMOREX
Memorex Telex Japan Ltd.
MEMREL
Memrel Corporation
MEMTECH
MemTech Technology
MendoCno
Mendocino Software
MERIDATA
Oy Meridata Finland Ltd
METHODEI
Methode Electronics India pvt ltd
METRUM
Metrum, Inc.
MHTL
Matsunichi Hi-Tech Limited
MICROBTX
Microbotics Inc.
Microchp
Microchip Technology, Inc.
MICROLIT
Microlite Corporation
Table F.1 — T10 vendor identification list (part 9 of 16)
ID
Organization


MICRON
Micron Technology, Inc.
MICROP
Micropolis
MICROTEK
Microtek Storage Corp
Minitech
Minitech (UK) Limited
Minolta
Minolta Corporation
MINSCRIB
Miniscribe
MiraLink
MiraLink Corporation
Mirifica
Mirifica s.r.l.
MITSUMI
Mitsumi Electric Co., Ltd.
MKM
Mitsubishi Kagaku Media Co., LTD.
Mobii
Mobii Systems (Pty.) Ltd.
MOL
Petrosoft Sdn. Bhd.
MOSAID
Mosaid Technologies Inc.
MOTOROLA
Motorola
MP-400
Daiwa Manufacturing Limited
MPC
MPC Corporation
MPCCORP
MPC Computers
MPEYE
Touchstone Technology Co., Ltd
MPIO
DKT Co.,Ltd
MPM
Mitsubishi Paper Mills, Ltd.
MPMan
MPMan.com, Inc.
MSFT
Microsoft Corporation
MSI
Micro-Star International Corp.
MST
Morning Star Technologies, Inc.
MSystems
M-Systems Flash Disk Pioneers
MTI
MTI Technology Corporation
MTNGATE
MountainGate Data Systems
MXI
Memory Experts International
nac
nac Image Technology Inc.
NAGRA
Nagravision SA - Kudelski Group
NAI
North Atlantic Industries
NAKAMICH
Nakamichi Corporation
NatInst
National Instruments
NatSemi
National Semiconductor Corp.
NCITS
InterNational Committee for Information Technology Standards (INCITS)
NCL
NCL America
NCR
NCR Corporation
Neartek
Neartek, Inc.
NEC
NEC
NETAPP
NetApp, Inc. (was Network Appliance)
NetBSD
The NetBSD Foundation
Netcom
Netcom Storage
NETENGIN
NetEngine, Inc.
NEWISYS
Newisys Data Storage
Newtech
Newtech Co., Ltd.
NEXSAN
Nexsan Technologies, Ltd.
NFINIDAT
Infinidat Ltd.
Table F.1 — T10 vendor identification list (part 10 of 16)
ID
Organization


NHR
NH Research, Inc.
Nike
Nike, Inc.
Nimble
Nimble Storage
NISCA
NISCA Inc.
NISHAN
Nishan Systems Inc.
NKK
NKK Corp.
NRC
Nakamichi Research Corporation
NSD
Nippon Systems Development Co.,Ltd.
NSM
NSM Jukebox GmbH
nStor
nStor Technologies, Inc.
NT
Northern Telecom
NUCONNEX
NuConnex
NUSPEED
NuSpeed, Inc.
NVIDIA
NVIDIA Corporation
NVMe
NVM Express Working Group
OAI
Optical Access International
OCE
Oce Graphics
OHDEN
Ohden Co., Ltd.
OKI
OKI Electric Industry Co.,Ltd (Japan)
Olidata
Olidata S.p.A.
OMI
Optical Media International
OMNIFI
Rockford Corporation - Omnifi Media
OMNIS
OMNIS Company (FRANCE)
Ophidian
Ophidian Designs
opslag
Tyrone Systems
Optelec
Optelec BV
Optiarc
Sony Optiarc Inc.
OPTIMEM
Cipher/Optimem
OPTOTECH
Optotech
ORACLE
Oracle Corporation
ORANGE
Orange Micro, Inc.
ORCA
Orca Technology
OSI
Optical Storage International
OSNEXUS
OS NEXUS, Inc.
OTL
OTL Engineering
OVERLAND
Overland Storage Inc.
pacdigit
Pacific Digital Corp
Packard
Parkard Bell
Panasas
Panasas, Inc.
PARALAN
Paralan Corporation
PASCOsci
Pasco Scientific
PATHLGHT
Pathlight Technology, Inc.
PerStor
Perstor
PERTEC
Pertec Peripherals Corporation
PFTI
Performance Technology Inc.
PFU
PFU Limited
PHILIPS
Philips Electronics
Table F.1 — T10 vendor identification list (part 11 of 16)
ID
Organization


PICO
Packard Instrument Company
PIK
TECHNILIENT & MCS
Pillar
Pillar Data Systems
PIONEER
Pioneer Electronic Corp.
Pirus
Pirus Networks
PIVOT3
Pivot3, Inc.
PLASMON
Plasmon Data
Pliant
Pliant Technology, Inc.
PMCSIERA
PMC-Sierra
PNNMed
PNN Medical SA
POKEN
Poken SA
POLYTRON
PT. HARTONO ISTANA TEKNOLOGI
PRAIRIE
PrairieTek
PREPRESS
PrePRESS Solutions
PRESOFT
PreSoft Architects
PRESTON
Preston Scientific
PRIAM
Priam
PRIMAGFX
Primagraphics Ltd
PRIMOS
Primos
PROCOM
Procom Technology
PROLIFIC
Prolific Technology Inc.
PROMISE
PROMISE TECHNOLOGY, Inc
PROSTOR
ProStor Systems, Inc.
PROSUM
PROSUM
PROWARE
Proware Technology Corp.
PTI
Peripheral Technology Inc.
PTICO
Pacific Technology International
PURE
PURE Storage
QIC
Quarter-Inch Cartridge Drive Standards, Inc.
QLogic
QLogic Corporation
QNAP
QNAP Systems
Qsan
QSAN Technology, Inc.
QUALSTAR
Qualstar
QUANTEL
Quantel Ltd.
QUANTUM
Quantum Corp.
QUIX
Quix Computerware AG
R-BYTE
R-Byte, Inc.
RACALREC
Racal Recorders
RADITEC
Radikal Technologies Deutschland GmbH
RADSTONE
Radstone Technology
RASSYS
Rasilient Systems Inc.
RASVIA
Rasvia Systems, Inc.
rave-mp
Go Video
Readboy
Readboy Ltd Co.
Realm
Realm Systems
realtek
Realtek Semiconductor Corp.
RELDATA
RELDATA Inc
Table F.1 — T10 vendor identification list (part 12 of 16)
ID
Organization


RENAGmbH
RENA GmbH
Revivio
Revivio, Inc.
RGI
Raster Graphics, Inc.
RHAPSODY
Rhapsody Networks, Inc.
RHS
Racal-Heim Systems GmbH
RICOH
Ricoh
RODIME
Rodime
Royaltek
RoyalTek company Ltd.
RPS
RPS
RTI
Reference Technology
S-D
Sauer-Danfoss
S-flex
Storageflex Inc
S-SYSTEM
S-SYSTEM
S1
storONE
SAMSUNG
Samsung Electronics Co., Ltd.
SAN
Storage Area Networks, Ltd.
Sandial
Sandial Systems, Inc.
SanDisk
SanDisk Corporation
SANKYO
Sankyo Seiki
SANRAD
SANRAD Inc.
SANYO
SANYO Electric Co., Ltd.
SC.Net
StorageConnections.Net
SCALE
Scale Computing, Inc.
SCIENTEK
SCIENTEK CORP
SCInc.
Storage Concepts, Inc.
SCREEN
Dainippon Screen Mfg. Co., Ltd.
SDI
Storage Dimensions, Inc.
SDS
Solid Data Systems
SEAC
SeaChange International, Inc.
SEAGATE
Seagate
SEAGRAND
SEAGRAND In Japan
Seanodes
Seanodes
Sec. Key
SecureKey Technologies Inc.
SEQUOIA
Sequoia Advanced Technologies, Inc.
Shinko
Shinko Electric Co., Ltd.
SIEMENS
Siemens
SigmaTel
SigmaTel, Inc.
SII
Seiko Instruments Inc.
SIMPLE
SimpleTech, Inc. (Obs - now STEC, Inc.)
SIVMSD
IMAGO SOFTWARE SL
SLCNSTOR
SiliconStor, Inc.
SLI
Sierra Logic, Inc.
SmrtStor
Smart Storage Systems
SMS
Scientific Micro Systems/OMTI
SMSC
SMSC Storage, Inc.
SMX
Smartronix, Inc.
SNYSIDE
Sunnyside Computing Inc.
Table F.1 — T10 vendor identification list (part 13 of 16)
ID
Organization


SoftLock
Softlock Digital Security Provider
SolidFir
SolidFire, Inc.
SONIC
Sonic Solutions
SoniqCas
SoniqCast
SONY
Sony Corporation Japan
SOUL
Soul Storage Technology (Wuxi) Co., Ltd
SPD
Storage Products Distribution, Inc.
SPECIAL
Special Computing Co.
SPECTRA
Spectra Logic, a Division of Western Automation Labs, Inc.
SPERRY
Sperry (now Unisys Corp.)
Spintso
Spintso International AB
STARBORD
Starboard Storage Systems, Inc.
STARWIND
StarWind Software, Inc.
STEC
STEC, Inc.
Sterling
Sterling Diagnostic Imaging, Inc.
STK
Storage Technology Corporation
STNWOOD
Stonewood Group
STONEFLY
StoneFly Networks, Inc.
STOR
StorageNetworks, Inc.
STORAPP
StorageApps, Inc. (now HP)
STORCOMP
Storage Computer Corporation
STORM
Storm Technology, Inc.
StorMagc
StorMagic
Stratus
Stratus Technologies
StrmLgc
StreamLogic Corp.
SUMITOMO
Sumitomo Electric Industries, Ltd.
SUN
Sun Microsystems, Inc.
SUNCORP
SunCorporation
suntx
Suntx System Co., Ltd
Swinxs
Swinxs BV
SYMANTEC
Symantec Corporation
SYMBIOS
Symbios Logic Inc.
SYMWAVE
Symwave, Inc.
SYNCSORT
Syncsort Incorporated
SYNERWAY
Synerway
SYNOLOGY
Synology, Inc.
SyQuest
SyQuest Technology, Inc.
SYSGEN
Sysgen
T-MITTON
Transmitton England
T-MOBILE
T-Mobile USA, Inc.
T11
INCITS Technical Committee T11
TALARIS
Talaris Systems, Inc.
TALLGRAS
Tallgrass Technologies
TANDBERG
Tandberg Data A/S
TANDEM
Tandem (now HP)
TANDON
Tandon
TCL
TCL Shenzhen ASIC MIcro-electronics Ltd
Table F.1 — T10 vendor identification list (part 14 of 16)
ID
Organization


TDK
TDK Corporation
TEAC
TEAC Japan
TECOLOTE
Tecolote Designs
TEGRA
Tegra Varityper
Tek
Tektronix
TELLERT
Tellert Elektronik GmbH
TENTIME
Laura Technologies, Inc.
TFDATACO
TimeForge
TGEGROUP
TGE Group Co.,LTD.
Thecus
Thecus Technology Corp.
TI-DSG
Texas Instruments
TiGi
TiGi Corporation
TILDESGN
Tildesign bv
Tite
Tite Technology Limited
TKS Inc.
TimeKeeping Systems, Inc.
TLMKS
Telemakus LLC
TMS
Texas Memory Systems, Inc.
TMS100
TechnoVas
TOLISGRP
The TOLIS Group
TOSHIBA
Toshiba Japan
TRIOFLEX
Trioflex Oy
TRIPACE
Tripace
TRLogger
TrueLogger Ltd.
TROIKA
Troika Networks, Inc.
TRULY
TRULY Electronics MFG. LTD.
TRUSTED
Trusted Data Corporation
TSSTcorp
Toshiba Samsung Storage Technology Corporation
TZM
TZ Medical
UD-DVR
Bigstone Project.
UDIGITAL
United Digital Limited
UIT
United Infomation Technology
ULTRA
UltraStor Corporation
UNISTOR
Unistor Networks, Inc.
UNISYS
Unisys
USCORE
Underscore, Inc.
USDC
US Design Corp.
VASCO
Vasco Data Security
VDS
Victor Data Systems Co., Ltd.
Verari
Verari Systems, Inc.
VERBATIM
Verbatim Corporation
Vercet
Vercet LLC
VERITAS
VERITAS Software Corporation
VEXCEL
VEXCEL IMAGING GmbH
VicomSys
Vicom Systems, Inc.
VIDEXINC
Videx, Inc.
VIOLIN
Violin Memory, Inc.
VIRIDENT
Virident Systems, Inc.
Table F.1 — T10 vendor identification list (part 15 of 16)
ID
Organization


VITESSE
Vitesse Semiconductor Corporation
VIXEL
Vixel Corporation (now part of Emulex)
VLS
Van Lent Systems BV
VMAX
VMAX Technologies Corp.
VMware
VMware Inc.
Vobis
Vobis Microcomputer AG
VOLTAIRE
Voltaire Ltd.
VRC
Vermont Research Corp.
VRugged
Vanguard Rugged Storage
Waitec
Waitec NV
WangDAT
WangDAT
WANGTEK
Wangtek
Wasabi
Wasabi Systems
WAVECOM
Wavecom
WD
Western Digital Corporation
WDC
Western Digital Corporation
WDIGTL
Western Digital
WEARNES
Wearnes Technology Corporation
WeeraRes
Weera Research Pte Ltd
Wildflwr
Wildflower Technologies, Inc.
WSC0001
Wisecom, Inc.
X3
InterNational Committee for Information Technology Standards (INCITS)
XEBEC
Xebec Corporation
XENSRC
XenSource, Inc.
Xerox
Xerox Corporation
XIOtech
XIOtech Corporation
XIRANET
Xiranet Communications GmbH
XIV
XIV (now IBM)
XtremIO
XtremIO
XYRATEX
Xyratex
YINHE
NUDT Computer Co.
YIXUN
Yixun Electronic Co.,Ltd.
YOTTA
YottaYotta, Inc.
Zarva
Zarva Digital Technology Co., Ltd.
ZETTA
Zetta Systems, Inc.
Table F.1 — T10 vendor identification list (part 16 of 16)
ID
Organization
