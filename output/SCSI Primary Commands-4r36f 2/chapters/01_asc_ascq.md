# ASC & ASCQ

The additional sense codes (i.e., the ADDITIONAL SENSE CODE field and ADDITIONAL SENSE CODE QUALIFIER field
values in sense data) are defined in table 54.
Bh
ABORTED COMMAND: Indicates that the device server aborted the command. The appli-
cation client may be able to recover by trying the command again.
Ch
Reserved
Dh
VOLUME OVERFLOW: Indicates that a buffered SCSI device has reached the end-of-partition
and data may remain in the buffer that has not been written to the medium. One or more
RECOVER BUFFERED DATA command(s) may be issued to read the unwritten data from the
buffer. (See SSC-3.)
Eh
MISCOMPARE: Indicates that the source data did not match the data read from the medium.
Fh
COMPLETED: Indicates there is command completed sense data (see SAM-5) to be reported.
This may occur for a successful command.
Table 54 — ASC and ASCQ assignments (part 1 of 18)
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
ASC ASCQ
DT LPWROMAEBKVF
Description
20h
0Bh
DT
PWROMAEBK
ACCESS DENIED - ACL LUN CONFLICT
20h
08h
DT
PWROMAEBK
ACCESS DENIED - ENROLLMENT CONFLICT
20h
01h
DT
PWROMAEBK
ACCESS DENIED - INITIATOR PENDING-ENROLLED
20h
09h
DT
PWROMAEBK
ACCESS DENIED - INVALID LU IDENTIFIER
20h
03h
DT
PWROMAEBK
ACCESS DENIED - INVALID MGMT ID KEY
20h
0Ah
DT
PWROMAEBK
ACCESS DENIED - INVALID PROXY TOKEN
20h
02h
DT
PWROMAEBK
ACCESS DENIED - NO ACCESS RIGHTS
4Bh
03h
DT
PWROMAEBK
ACK/NAK TIMEOUT
67h
02h
A
ADD LOGICAL UNIT FAILED
13h
00h
D
W
O
BK
ADDRESS MARK NOT FOUND FOR DATA FIELD
12h
00h
D
W
O
BK
ADDRESS MARK NOT FOUND FOR ID FIELD
67h
08h
A
ASSIGN FAILURE OCCURRED
27h
03h
T
R
ASSOCIATED WRITE PROTECT
2Ah
06h
DT LPWROMAEBKVF
ASYMMETRIC ACCESS STATE CHANGED
47h
04h
DT LPWROMAEBKVF
ASYNCHRONOUS INFORMATION PROTECTION ERROR DETECTED
44h
71h
DT
B
ATA DEVICE FAILED SET FEATURES
67h
0Bh
DT
B
ATA DEVICE FEATURE NOT ENABLED
00h
1Dh
DT
B
ATA PASS THROUGH INFORMATION AVAILABLE
A numeric ordered listing of the ASC and ASCQ assignments is provided in E.2.
Table 53 — Sense key descriptions (part 2 of 2)
Sense
Key
Description
