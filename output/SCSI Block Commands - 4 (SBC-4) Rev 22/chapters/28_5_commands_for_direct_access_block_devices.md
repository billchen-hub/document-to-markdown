# 5 Commands for direct access block devices

5 Commands for direct access block devices
5.1 Commands for direct access block devices overview
The commands for direct access block devices are listed in table 34.
Table 34 — Commands for direct access block devices (part 1 of 5)
Command
Operation
code a
Type
LBACT
Reference
ATA PASS-THROUGH (12)
A1h
O
n/a
SAT-4
ATA PASS-THROUGH (16)
85h
O
n/a
SAT-4
BACKGROUND CONTROL
9Eh/15h
O
n/a
5.2
CHANGE ALIASES
A4h/0Bh
O
n/a
SPC-6
CLOSE ZONE
94h/01h
X
n/a
ZBC-2
COMPARE AND WRITE
89h
O
R, W
5.3
COPY OPERATION ABORT
83h/1Ch
O
n/a
SPC-6
EXTENDED COPY
83h/01h
O
n/a
SPC-6
FINISH ZONE
94h/02h
X
n/a
ZBC-2
FORMAT UNIT
04h
M
Z
5.4
FORMAT WITH PRESET
38h
O
Z
5.5
GET LBA STATUS (16)
9Eh/12h
O
n/a
5.6
GET LBA STATUS (32)
7Fh/0012h
O
n/a
5.7
GET PHYSICAL ELEMENT STATUS
9Eh/17h
O
n/a
5.8
GET STREAM STATUS
9Eh/16h
O
n/a
5.9
INQUIRY
12h
M
n/a
SPC-6
LOG SELECT
4Ch
O
n/a
SPC-6
LOG SENSE
4Dh
O
n/a
SPC-6
MAINTENANCE IN
A3h/00h to 04h
A3h/06h to 09h
X
n/a
SPC-6
SCC-2
MAINTENANCE OUT
A4h/00h to 05h
A4h/07h to 09h
X
n/a
SPC-6
SCC-2
MODE SELECT (6)
15h
O
n/a
SPC-6
MODE SELECT (10)
55h
O
n/a
SPC-6
MODE SENSE (6)
1Ah
O
n/a
SPC-6
Key:
O
= optional
M
= mandatory
X
= implementation requirements are defined in
the reference
R
= read command
U
= unmap command
V
= verify command
W
= write command
Z
= other command
LBACT= logical block access command type
(see 4.2.2)
a If a command is defined by a combination of operation code and service action, then the operation
code value is shown preceding a slash and the service action value is shown after the slash.


MODE SENSE (10)
5Ah
O
n/a
SPC-6
OPEN ZONE
94h/03h
X
n/a
ZBC-2
ORWRITE (16)
8Bh
O
R, W
5.10
ORWRITE (32)
7Fh/000Eh
O
R, W
5.11
PERSISTENT RESERVE IN
5Eh
O
n/a
SPC-6
PERSISTENT RESERVE OUT
5Fh
O
n/a
SPC-6
POPULATE TOKEN
83h/10h
O
n/a
5.12
PRE-FETCH (10)
34h
O
R
5.13
PRE-FETCH (16)
90h
O
R
5.14
PREVENT ALLOW MEDIUM REMOVAL
1Eh
O
n/a
5.15
READ (10)
28h
M
R
5.16
READ (12)
A8h
O
R
5.17
READ (16)
88h
M
R
5.18
READ (32)
7Fh/0009h
O
R
5.19
READ ATTRIBUTE
8Ch
O
n/a
SPC-6
READ BUFFER (10)
3Ch
O
n/a
SPC-6
READ BUFFER (16)
9Bh
O
n/a
SPC-6
READ CAPACITY (10)
25h
M
n/a
5.20
READ CAPACITY (16)
9Eh/10h
M
n/a
5.21
READ DEFECT DATA (10)
37h
O
n/a
5.22
READ DEFECT DATA (12)
B7h
O
n/a
5.23
REASSIGN BLOCKS
07h
O
Z
5.24
READ MEDIA SERIAL NUMBER
ABh/01h
O
n/a
SPC-6
RECEIVE COPY DATA
84h/06h
O
n/a
SPC-6
RECEIVE COPY STATUS
84h/05h
O
n/a
SPC-6
RECEIVE DIAGNOSTIC RESULTS
1Ch
X
n/a
SPC-6
6.3
RECEIVE ROD TOKEN INFORMATION
84h/07h
X
n/a
SPC-6
4.28
5.25
REDUNDANCY GROUP IN
BAh
X
n/a
SCC-2
REDUNDANCY GROUP OUT
BBh
X
n/a
SCC-2
Table 34 — Commands for direct access block devices (part 2 of 5)
Command
Operation
code a
Type
LBACT
Reference
Key:
O
= optional
M
= mandatory
X
= implementation requirements are defined in
the reference
R
= read command
U
= unmap command
V
= verify command
W
= write command
Z
= other command
LBACT= logical block access command type
(see 4.2.2)
a If a command is defined by a combination of operation code and service action, then the operation
code value is shown preceding a slash and the service action value is shown after the slash.


REMOVE ELEMENT AND TRUNCATE
9Eh/18h
O
Z
5.26
REMOVE I_T NEXUS
A4h/0Ch
O
n/a
SPC-6
REPORT ALIASES
A3h/0Bh
O
n/a
SPC-6
REPORT ALL ROD TOKENS
84h/08h
O
n/a
SPC-6
REPORT IDENTIFYING INFORMATION
A3h/05h
O
n/a
SPC-6
REPORT LUNS
A0h
M
n/a
SPC-6
REPORT PRIORITY
A3h/0Eh
O
n/a
SPC-6
REPORT PROVISIONING INITIALIZATION
PATTERN
A3h/1Dh
O
n/a
5.27
REPORT REALMS
95h/06h
X
n/a
ZBC-2
REPORT REFERRALS
9Eh/13h
O
n/a
5.28
REPORT SUPPORTED OPERATION CODES
A3h/0Ch
O
n/a
SPC-6
REPORT SUPPORTED TASK MANAGEMENT
FUNCTIONS
A3h/0Dh
O
n/a
SPC-6
REPORT TARGET PORT GROUPS
A3h/0Ah
O
n/a
SPC-6
REPORT TIMESTAMP
A3h/0Fh
O
n/a
SPC-6
REPORT ZONE DOMAINS
95h/07h
X
n/a
ZBC-2
REPORT ZONES
95h/00h
X
n/a
ZBC-2
REQUEST SENSE
03h
M
n/a
SPC-6
RESET WRITE POINTER
94h/04h
X
n/a
ZBC
RESTORE ELEMENTS AND REBUILD
9Eh/19h
O
Z
5.29
SANITIZE
48h
O
Z
5.30
SECURITY PROTOCOL IN
A2h
O
n/a
SPC-6
SECURITY PROTOCOL OUT
B5h
O
n/a
SPC-6
SEND DIAGNOSTIC
1Dh
O
n/a
SPC-6
SEQUENTIALIZE ZONE
94h/10h
X
n/a
ZBC-2
SET IDENTIFYING INFORMATION
A4h/06h
O
n/a
SPC-6
SET PRIORITY
A4h/0Eh
O
n/a
SPC-6
SET TARGET PORT GROUPS
A4h/0Ah
O
n/a
SPC-6
SET TIMESTAMP
A4h/0Fh
O
n/a
SPC-6
SPARE IN
BCh
X
n/a
SCC-2
SPARE OUT
BDh
X
n/a
SCC-2
Table 34 — Commands for direct access block devices (part 3 of 5)
Command
Operation
code a
Type
LBACT
Reference
Key:
O
= optional
M
= mandatory
X
= implementation requirements are defined in
the reference
R
= read command
U
= unmap command
V
= verify command
W
= write command
Z
= other command
LBACT= logical block access command type
(see 4.2.2)
a If a command is defined by a combination of operation code and service action, then the operation
code value is shown preceding a slash and the service action value is shown after the slash.


START STOP UNIT
1Bh
O
n/a
5.31
STREAM CONTROL
9Eh/14h
O
n/a
5.32
SYNCHRONIZE CACHE (10)
35h
O
W
5.33
SYNCHRONIZE CACHE (16)
91h
O
W
5.34
TEST UNIT READY
00h
M
n/a
SPC-6
UNMAP
42h
X
U
5.35
4.7
VERIFY (10)
2Fh
O
V, W
5.36
VERIFY (12)
AFh
O
V, W
5.37
VERIFY (16)
8Fh
O
V, W
5.38
VERIFY (32)
7Fh/000Ah
O
V, W
5.39
VOLUME SET IN
BEh
X
n/a
SCC-2
VOLUME SET OUT
BFh
X
n/a
SCC-2
WRITE (10)
2Ah
O
W
5.40
WRITE (12)
AAh
O
W
5.41
WRITE (16)
8Ah
O
W
5.42
WRITE (32)
7Fh/000Bh
O
W
5.43
WRITE AND VERIFY (10)
2Eh
O
V, W
5.44
WRITE AND VERIFY (12)
AEh
O
V, W
5.45
WRITE AND VERIFY (16)
8Eh
O
V, W
5.46
WRITE AND VERIFY (32)
7Fh/000Ch
O
V, W
5.47
WRITE ATOMIC (16)
9Ch
O
W
5.48
WRITE ATOMIC (32)
7Fh/000Fh
O
W
5.49
WRITE ATTRIBUTE
8Dh
O
n/a
SPC-6
WRITE BUFFER
3Bh
O
n/a
SPC-6
WRITE LONG (10)
3Fh
O
Z
5.50
WRITE LONG (16)
9Fh/11h
O
Z
5.51
WRITE SAME (10)
41h
X
U, W
5.52
4.7
WRITE SAME (16)
93h
X
U, W
5.53
4.7
WRITE SAME (32)
7Fh/000Dh
X
U, W
5.54
4.7
Table 34 — Commands for direct access block devices (part 4 of 5)
Command
Operation
code a
Type
LBACT
Reference
Key:
O
= optional
M
= mandatory
X
= implementation requirements are defined in
the reference
R
= read command
U
= unmap command
V
= verify command
W
= write command
Z
= other command
LBACT= logical block access command type
(see 4.2.2)
a If a command is defined by a combination of operation code and service action, then the operation
code value is shown preceding a slash and the service action value is shown after the slash.


5.2 BACKGROUND CONTROL command
5.2.1 BACKGROUND CONTROL command overview
The BACKGROUND CONTROL command (see table 35) is used to request that the device server start or
stop host initiated advanced background operations (see 4.31), if any.
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
WRITE SCATTERED (16)
9Fh/12h
O
W
5.55
WRITE SCATTERED (32)
7Fh/0011h
O
W
5.56
WRITE STREAM (16)
9Ah
O
W
5.57
WRITE STREAM (32)
7Fh/0010h
O
W
5.58
WRITE USING TOKEN
83h/11h
X
Z
5.59
4.28
ZONE ACTIVATE
95h/08h
X
n/a
ZBC-2
ZONE QUERY
95h/09h
X
n/a
ZBC-2
Note 1 - Operation codes that are obsolete are listed in Annex A, Annex B, and SPC-6.
Note 2 - The following operation codes are vendor specific: 02h, 05h, 06h, 09h, 0Ch, 0Dh, 0Eh, 0Fh, 10h,
11h, 13h, 14h, 19h, 20h, 21h, 22h, 23h, 24h, 26h, 27h, 29h, 2Ch, 2Dh, and C0h to FFh.
Note 3 - A complete summary of operation codes is available at http://www.t10.org/lists/2op.htm. The
summary includes information about obsolete commands.
Table 35 — BACKGROUND CONTROL command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (15h)
BO_CTL
Reserved
BO_TIME
Reserved
•••
CONTROL
Table 34 — Commands for direct access block devices (part 5 of 5)
Command
Operation
code a
Type
LBACT
Reference
Key:
O
= optional
M
= mandatory
X
= implementation requirements are defined in
the reference
R
= read command
U
= unmap command
V
= verify command
W
= write command
Z
= other command
LBACT= logical block access command type
(see 4.2.2)
a If a command is defined by a combination of operation code and service action, then the operation
code value is shown preceding a slash and the service action value is shown after the slash.
