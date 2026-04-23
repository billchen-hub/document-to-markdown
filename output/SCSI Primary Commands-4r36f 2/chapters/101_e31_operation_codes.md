# E.3.1 Operation codes

E.3 Operation codes
E.3.1 Operation codes
Table E.2 is a numerical order listing of the command operation codes.
Table E.2 — Operation codes (part 1 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description
00h
MMMMMMMMMMMMMM
TEST UNIT READY
01h
M
REWIND
01h
Z
V
Z Z Z Z
REZERO UNIT
02h
V V V V V V
V
03h
MMMMMMMMMMOMMM
REQUEST SENSE
04h
M
OO
FORMAT UNIT
04h
O
FORMAT MEDIUM
04h
O
FORMAT
05h
VMV V V V
V
READ BLOCK LIMITS
06h
V V V V V V
V
07h
O V V
O
O V
REASSIGN BLOCKS
07h
O
INITIALIZE ELEMENT STATUS
08h
Z MV
O
O V
READ(6)
08h
O
RECEIVE
08h
GET MESSAGE(6)
09h
V V V V V V
V
0Ah
Z O
O
O V
WRITE(6)
0Ah
M
SEND(6)
0Ah
SEND MESSAGE(6)
0Ah
M
PRINT
0Bh
Z
Z O Z V
SEEK(6)
0Bh
O
SET CAPACITY
0Bh
O
SLEW AND PRINT
0Ch
V V V V V V
V
0Dh
V V V V V V
V
0Eh
V V V V V V
V
0Fh
V O V V V V
V
READ REVERSE(6)
10h
VM
V V V
WRITE FILEMARKS(6)
10h
O
SYNCHRONIZE BUFFER
11h
VMV V V V
SPACE(6)
12h
MMMMMMMMMMMMMM
INQUIRY
13h
V
V V V V
13h
O
VERIFY(6)
14h
V OO V V V
RECOVER BUFFERED DATA
15h
OMO
O
OOOO
OO
MODE SELECT(6)


16h
Z Z M Z O
OOO Z
O
RESERVE(6)
16h
Z
RESERVE ELEMENT(6)
17h
Z Z M Z O
OOO Z
O
RELEASE(6)
17h
Z
RELEASE ELEMENT(6)
18h
Z Z Z Z O Z O
Z
COPY
19h
VMV V V V
ERASE(6)
1Ah
OMO
O
OOOO
OO
MODE SENSE(6)
1Bh
O
OOO
O
MO
O
START STOP UNIT
1Bh
O
M
LOAD UNLOAD
1Bh
SCAN
1Bh
O
STOP PRINT
1Bh
O
OPEN/CLOSE IMPORT/EXPORT ELEMENT
1Ch
OOOOO
OOOM
OOO
RECEIVE DIAGNOSTIC RESULTS
1Dh
MMMMM
MMOM
MMM
SEND DIAGNOSTIC
1Eh
OO
OOOO
O
O
PREVENT ALLOW MEDIUM REMOVAL
1Fh
20h
V
V V V
V
21h
V
V V V
V
22h
V
V V V
V
23h
V
V
V
V
23h
O
READ FORMAT CAPACITIES
24h
V
V V
SET WINDOW
25h
M
M
M
M
READ CAPACITY(10)
25h
O
READ CAPACITY
25h
M
READ CARD CAPACITY
25h
GET WINDOW
26h
V
V V
27h
V
V V
28h
M
MOM
MM
READ(10)
28h
GET MESSAGE(10)
29h
V
V V O
READ GENERATION
2Ah
O
MOM
MO
WRITE(10)
2Ah
SEND(10)
2Ah
SEND MESSAGE(10)
2Bh
Z
OOO
O
SEEK(10)
2Bh
M
LOCATE(10)
2Bh
O
POSITION TO ELEMENT
2Ch
V
OO
ERASE(10)
2Dh
O
READ UPDATED BLOCK
2Dh
V
2Eh
O
OOO
MO
WRITE AND VERIFY(10)
2Fh
O
OOO
VERIFY(10)
Table E.2 — Operation codes (part 2 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description


30h
Z
Z Z Z
SEARCH DATA HIGH(10)
31h
Z
Z Z Z
SEARCH DATA EQUAL(10)
31h
OBJECT POSITION
32h
Z
Z Z Z
SEARCH DATA LOW(10)
33h
Z
O Z O
SET LIMITS(10)
34h
O
O
O
O
PRE-FETCH(10)
34h
M
READ POSITION
34h
GET DATA BUFFER STATUS
35h
O
OOO
MO
SYNCHRONIZE CACHE(10)
36h
Z
O
O
O
LOCK UNLOCK CACHE(10)
37h
O
O
READ DEFECT DATA(10)
37h
O
INITIALIZE ELEMENT STATUS WITH RANGE
38h
O
O
O
MEDIUM SCAN
39h
Z Z Z Z O Z O
Z
COMPARE
3Ah
Z Z Z Z O Z O
Z
COPY AND VERIFY
3Bh
OOOOOOOOOOMOOO
WRITE BUFFER
3Ch
OOOOOOOOOO
OOO
READ BUFFER
3Dh
O
UPDATE BLOCK
3Eh
O
O
O
READ LONG(10)
3Fh
O
O
O
WRITE LONG(10)
40h
Z Z Z Z O Z O Z
CHANGE DEFINITION
41h
O
WRITE SAME(10)
42h
O
UNMAP
42h
O
READ SUB-CHANNEL
43h
O
READ TOC/PMA/ATIP
44h
M
M
REPORT DENSITY SUPPORT
44h
READ HEADER
45h
O
PLAY AUDIO(10)
46h
M
GET CONFIGURATION
47h
O
PLAY AUDIO MSF
48h
O
O
SANITIZE
49h
4Ah
M
GET EVENT STATUS NOTIFICATION
4Bh
O
PAUSE/RESUME
4Ch
OOOOO
OOOO
OOO
LOG SELECT
4Dh
OOOOO
OOOO
OMO
LOG SENSE
4Eh
O
STOP PLAY/SCAN
4Fh
50h
Z
XDWRITE(10)
51h
O
XPWRITE(10)
51h
O
READ DISC INFORMATION
52h
Z
XDREAD(10)
Table E.2 — Operation codes (part 3 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description


52h
O
READ TRACK INFORMATION
53h
O
XDWRITEREAD(10)
53h
O
RESERVE TRACK
54h
O
SEND OPC INFORMATION
55h
OOO
OMOOOOMOMO
MODE SELECT(10)
56h
Z Z M Z O
OOO Z
RESERVE(10)
56h
Z
RESERVE ELEMENT(10)
57h
Z Z M Z O
OOO Z
RELEASE(10)
57h
Z
RELEASE ELEMENT(10)
58h
O
REPAIR TRACK
59h
5Ah
OOO
OMOOOOMOMO
MODE SENSE(10)
5Bh
O
CLOSE TRACK/SESSION
5Ch
O
READ BUFFER CAPACITY
5Dh
O
SEND CUE SHEET
5Eh
OMOOO
OOOO
M
PERSISTENT RESERVE IN
5Fh
OMOOO
OOOO
M
PERSISTENT RESERVE OUT
7Eh
OO
O
OOOO
O
extended CDB
7Fh
O
M
variable length CDB (more than 16 bytes)
80h
Z
XDWRITE EXTENDED(16)
80h
M
WRITE FILEMARKS(16)
81h
Z
REBUILD(16)
81h
O
READ REVERSE(16)
82h
Z
REGENERATE(16)
82h
O
ALLOW OVERWRITE
83h
OOOOO
O
OO
Third-party Copy OUT
84h
OOOOO
O
OO
Third-party Copy IN
85h
O
O
ATA PASS-THROUGH(16)
86h
OO
OO
OOOOOOO
ACCESS CONTROL IN
87h
OO
OO
OOOOOOO
ACCESS CONTROL OUT
88h
MO
O
O
O
READ(16)
89h
O
COMPARE AND WRITE
8Ah
OO
O
O
O
WRITE(16)
8Bh
O
ORWRITE
8Ch
OO
O
OO
O
M
READ ATTRIBUTE
8Dh
OO
O
OO
O
O
WRITE ATTRIBUTE
8Eh
O
O
O
O
WRITE AND VERIFY(16)
8Fh
OO
O
O
O
VERIFY(16)
90h
O
O
O
O
PRE-FETCH(16)
91h
O
O
O
O
SYNCHRONIZE CACHE(16)
91h
O
SPACE(16)
92h
Z
O
O
LOCK UNLOCK CACHE(16)
Table E.2 — Operation codes (part 4 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description


92h
M
LOCATE(16)
93h
O
WRITE SAME(16)
93h
M
ERASE(16)
94h
[usage proposed by SCSI Socket Services project]
95h
[usage proposed by SCSI Socket Services project]
96h
[usage proposed by SCSI Socket Services project]
97h
[usage proposed by SCSI Socket Services project]
98h
99h
9Ah
9Bh
9Ch
9Dh
SERVICE ACTION BIDIRECTIONAL
9Eh
SERVICE ACTION IN(16)
9Fh
M
SERVICE ACTION OUT(16)
A0h
MMOOO
OMMM
OMO
REPORT LUNS
A1h
O
BLANK
A1h
O
O
ATA PASS-THROUGH(12)
A2h
OO
O
O
SECURITY PROTOCOL IN
A3h
OOO
O
OOMOOOM
MAINTENANCE IN
A3h
O
SEND KEY
A4h
OOO
O
OOOOOOO
MAINTENANCE OUT
A4h
O
REPORT KEY
A5h
Z
O
OM
MOVE MEDIUM
A5h
O
PLAY AUDIO(12)
A6h
O
EXCHANGE MEDIUM
A6h
O
LOAD/UNLOAD C/DVD
A7h
Z Z
O
O
MOVE MEDIUM ATTACHED
A7h
O
SET READ AHEAD
A8h
O
OOO
READ(12)
A8h
GET MESSAGE(12)
A9h
O
SERVICE ACTION OUT(12)
AAh
O
OOO
WRITE(12)
AAh
SEND MESSAGE(12)
ABh
O
O
SERVICE ACTION IN(12)
ACh
O
ERASE(12)
ACh
O
GET PERFORMANCE
ADh
O
READ DVD STRUCTURE
AEh
O
O
O
WRITE AND VERIFY(12)
AFh
O
O
O
VERIFY(12)
B0h
Z Z Z
SEARCH DATA HIGH(12)
B1h
Z Z Z
SEARCH DATA EQUAL(12)
Table E.2 — Operation codes (part 5 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description


B2h
Z Z Z
SEARCH DATA LOW(12)
B3h
Z
O Z O
SET LIMITS(12)
B4h
Z Z
O Z O
READ ELEMENT STATUS ATTACHED
B5h
OO
O
O
SECURITY PROTOCOL OUT
B5h
O
REQUEST VOLUME ELEMENT ADDRESS
B6h
O
SEND VOLUME TAG
B6h
O
SET STREAMING
B7h
O
O
READ DEFECT DATA(12)
B8h
Z
O Z OM
READ ELEMENT STATUS
B9h
O
READ CD MSF
BAh
O
O
OOMO
REDUNDANCY GROUP (IN)
BAh
O
SCAN
BBh
O
O
OOOO
REDUNDANCY GROUP (OUT)
BBh
O
SET CD SPEED
BCh
O
O
OOMO
SPARE (IN)
BDh
O
O
OOOO
SPARE (OUT)
BDh
O
MECHANISM STATUS
BEh
O
O
OOMO
VOLUME SET (IN)
BEh
O
READ CD
BFh
O
O
OOOO
VOLUME SET (OUT)
BFh
O
SEND DVD STRUCTURE
Table E.2 — Operation codes (part 6 of 6)
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description


E.3.2 Additional operation codes for devices with the ENCSERV bit set to one
Table E.3 is a numerical order listing of the additional command operation codes used by devices that have
the ENCSERV bit set to one in their standard INQUIRY data. The operation codes listed in table E.3 are in
addition to the operation codes listed in E.3.1 for the device type indicated by the standard INQUIRY data
having the ENCSERV bit set to one.
Table E.3 — Additional operation codes for devices with the ENCSERV bit set to one
D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
M = Mandatory
.
L – Printer Device (SSC)
O = Optional
.
P – Processor Device (SPC-2)
V = Vendor specific
.
. W – Write Once Block Device (SBC)
Z = Obsolete
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
.
.
.
.
. F – Object-based Storage Device (OSD-2)
OP
D T L PWROMA E B K V F
Description
1C
MMMMMMMMMMMMMM
RECEIVE DIAGNOSTIC RESULTS
1D
MMMMMMMMMMMMMM
SEND DIAGNOSTIC


E.3.3 MAINTENANCE IN and MAINTENANCE OUT service actions
The assignment of service action codes for the MAINTENANCE IN and MAINTENANCE OUT operation
codes by this standard is shown in table E.4. The MAINTENANCE IN and MAINTENANCE OUT service
actions that may be assigned by other command standards are noted as restricted but their specific usage is
not described.
Table E.4 — MAINTENANCE IN and MAINTENANCE OUT service actions
Service
Action
Description
MAINTENANCE IN [operation code A3h]
00h to 04h
Restricted (see SCC-2)
05h
REPORT IDENTIFYING INFORMATION
06h to 09h
Restricted (see SCC-2)
0Ah
REPORT TARGET PORT GROUPS
0Bh
REPORT ALIASES
0Ch
REPORT SUPPORTED OPERATION CODES
0Dh
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS
0Eh
REPORT PRIORITY
0Fh
REPORT TIMESTAMP
10h
MANAGEMENT PROTOCOL IN
11h to 1Dh
Reserved
1Eh
Restricted (see ADC-3)
1Fh
Vendor specific
MAINTENANCE OUT [operation code A4h]
00h to 05h
Restricted (see SCC-2)
06h
SET IDENTIFYING INFORMATION
07h to 09h
Restricted (see SCC-2)
0Ah
SET TARGET PORT GROUPS
0Bh
CHANGE ALIASES
0Ch
REMOVE I_T NEXUS
0Dh
Reserved
0Eh
SET PRIORITY
0Fh
SET TIMESTAMP
10h
MANAGEMENT PROTOCOL OUT
11h to 1Dh
Reserved
1Eh
Restricted (see ADC-3, and SMC-3)
1Fh
Vendor specific


E.3.4 SERVICE ACTION IN and SERVICE ACTION OUT service actions
The assignment of service action codes for the SERVICE ACTION IN(12) and SERVICE ACTION OUT(12)
operation codes by this standard is shown in table E.5. The SERVICE ACTION IN(12) and SERVICE ACTION
OUT(12) service actions that may be assigned by other command standards are noted as restricted but their
specific usage is not described.
The assignment of service action codes for the SERVICE ACTION IN(16) and SERVICE ACTION OUT(16)
operation codes by this standard is shown in table E.6. The SERVICE ACTION IN(16) and SERVICE ACTION
OUT(16) service actions that may be assigned by other command standards are noted as restricted but their
specific usage is not described.
Table E.5 — SERVICE ACTION IN(12) and SERVICE ACTION OUT(12) service actions
Service
Action
Description
SERVICE ACTION IN(12) [operation code ABh]
00h
Reserved
01h
READ MEDIA SERIAL NUMBER
02h to 1Fh
Reserved
SERVICE ACTION OUT(12) [operation code A9h]
00h to 1Eh
Reserved
1Fh
Restricted (see applicable command standard)
Table E.6 — SERVICE ACTION IN(16) and SERVICE ACTION OUT(16) service actions
Service
Action
Description
SERVICE ACTION IN(16) [operation code 9Eh]
00h to 0Fh
Reserved
10h to 1Fh
Restricted (see applicable command standard)
SERVICE ACTION OUT(16) [operation code 9Fh]
00h to 0Fh
Reserved
10h to 1Fh
Restricted (see applicable command standard)


E.3.5 SERVICE ACTION BIDIRECTIONAL service actions
The assignment of service action codes for the SERVICE ACTION BIDIRECTIONAL operation codes by this
standard is shown in table E.7. The SERVICE ACTION BIDIRECTIONAL service actions that may be
assigned by other command standards are noted as restricted but their specific usage is not described.
Table E.7 — SERVICE ACTION BIDIRECTIONAL service actions
Service
Action
Description
SERVICE ACTION BIDIRECTIONAL [operation code 9Dh]
00h to 0Fh
Reserved
10h to 1Fh
Restricted (see applicable command standard)
