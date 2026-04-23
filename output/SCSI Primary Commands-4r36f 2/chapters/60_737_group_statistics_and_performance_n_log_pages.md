# 7.3.7 Group Statistics and Performance (n) log pages

The NUMBER OF READ FUA COMMANDS field indicates the number of read commands (see table 375 in 7.3.6.1)
with the FUA bit (see SBC-3) set to one received by the logical unit.
The NUMBER OF WRITE FUA COMMANDS field indicates the number of write commands (see table 375 in 7.3.6.1)
with the FUA bit (see SBC-3) set to one received by the logical unit.
The NUMBER OF READ FUA_NV COMMANDS field indicates the number of read commands (see table 375 in
7.3.6.1) with the FUA_NV bit (see SBC-3) set to one received by the logical unit.
The NUMBER OF WRITE FUA_NV COMMANDS field indicates the number of write commands (see table 375 in
7.3.6.1) with the FUA_NV bit (see SBC-3) set to one received by the logical unit.
The READ FUA COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals (see
7.3.5.7) spent by the logical unit processing read commands (see table 375 in 7.3.6.1) with the FUA bit (see
SBC-3) set to one.
The WRITE FUA COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals (see
7.3.5.7) spent by the logical unit processing write commands (see table 375 in 7.3.6.1) with the FUA bit (see
SBC-3) set to one.
The READ FUA_NV COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals
(see 7.3.5.7) spent by the logical unit processing read commands (see table 375 in 7.3.6.1) with the FUA_NV
bit (see SBC-3) set to one.
The WRITE FUA_NV COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals
(see 7.3.5.7) spent by the logical unit processing write commands (see table 375 in 7.3.6.1) with the FUA_NV
bit (see SBC-3) set to one.
7.3.7 Group Statistics and Performance (n) log pages
7.3.7.1 Overview
Using the format shown in table 381, Group Statistics and Performance (n) log pages (page code 19h,
subpage codes 01h  to 1Fh) collect statistics and performance information for the group number specified in a
read CDB or a write CDB based on the parameter codes listed in table 380.
The Group Statistics and Performance (n) log pages provide the following statistics and performance results
associated to the addressed logical unit and the GROUP NUMBER field:
a)
Statistics and Performance log parameters:
A)
number of read commands;
Table 380 — Group Statistics and Performance log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h
Group n Statistics and Performance
Reset Only
7.3.7.2
Mandatory
0004h
Group n Force Unit Access Statistics
and Performance
Reset Only
7.3.7.3
Optional
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


B)
number of write commands;
C) number of read logical blocks transmitted by a target port;
D) number of write logical blocks received by a target port;
E)
read command processing time;
F)
write command processing time;
and
b)
Force Unit Access Statistics and Performance log parameters:
A)
number of read commands with the FUA bit (see SBC-3) set to one;
B)
number of write commands with the FUA bit set to one;
C) number of read commands with the FUA_NV bit (see SBC-3) set to one;
D) number of write commands with the FUA_NV bit set to one;
E)
read command with the FUA bit set to one processing intervals;
F)
write command with the FUA bit set to one processing intervals;
G) read command with the FUA_NV bit set to one processing intervals; and
H) write command with the FUA_NV bit set to one processing intervals.
In the Group Statistics and Performance (n) log pages, read commands and write commands are those shown
in table 375 (see 7.3.6.1).
The Group Statistics and Performance (n) log pages provide logging of statistics and performance of read and
write operations based on group numbers. There are 31 Group Statistics and Performance (n) log pages one
for each group number. The statistics and performance information associated with each group number is
collected in the corresponding Group Statistics and Performance (n) log page (e.g., operations associated
with group number 16 are logged in the Group Statistics and Performance (16) log page).
Each Group Statistics and Performance (n) log page has the format shown in table 381.
Table 381 — Group Statistics and Performance (n) log page
Bit
Byte
DS
SPF (1b)
PAGE CODE (19h)
SUBPAGE CODE (01h to 1Fh) (see table 382) a
(MSB)
PAGE LENGTH (n-3)
(LSB)
Group statistics and performance log parameters

General statistics and performance log parame-
ter
(see table 380) [first]

•••
•••
General statistics and performance log parame-
ter
(see table 380) [last]

•••
n
a The log parameter associated with the specific group number as specified by the value of n is collected
in the corresponding log parameter (e.g., the count of read commands with the GROUP NUMBER field set
to 9 is logged in the GROUP N NUMBER OF READ COMMANDS field in the Group n Statistics and
Performance log parameter of the Group Statistics and Performance (9) log page).


The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 381 for the Group Statistics and
Performance (n) log pages.
The SUBPAGE CODE field (see table 382) associates the Group Statistics and Performance (n) log page being
transferred with the contents of the GROUP NUMBER field in a read command CDB or write command CDB (see
table 375 in 7.3.6.1 and SBC-3).
Table 382 — Group Statistics and Performance (n) subpage codes (part 1 of 2)
Subpage code
Log page name a
Group number b
01h
Group Statistics and Performance (1)
00001b
02h
Group Statistics and Performance (2)
00010b
03h
Group Statistics and Performance (3)
00011b
04h
Group Statistics and Performance (4)
00100b
05h
Group Statistics and Performance (5)
00101b
06h
Group Statistics and Performance (6)
00110b
07h
Group Statistics and Performance (7)
00111b
08h
Group Statistics and Performance (8)
01000b
09h
Group Statistics and Performance (9)
01001b
0Ah
Group Statistics and Performance (10)
01010b
0Bh
Group Statistics and Performance (11)
01011b
0Ch
Group Statistics and Performance (12)
01100b
0Dh
Group Statistics and Performance (13)
01101b
0Eh
Group Statistics and Performance (14)
01110b
0Fh
Group Statistics and Performance (15)
01111b
10h
Group Statistics and Performance (16)
10000b
11h
Group Statistics and Performance (17)
10001b
12h
Group Statistics and Performance (18)
10010b
13h
Group Statistics and Performance (19)
10011b
14h
Group Statistics and Performance (20)
10100b
15h
Group Statistics and Performance (21)
10101b
a The statistics and performance information associated with a group number is
collected in the corresponding Group Statistics and Performance (n) log page
(e.g., operations associated with group number 10000b are logged in the
Group Statistics and Performance (16) log page).
b The GROUP NUMBER field is from the read command CDB or the write
command CDB (see table 375 in 7.3.6.1 and SBC-3).


The contents of each group statistics and performance log parameter depends on the value in its PARAMETER
CODE field (see table 380).
16h
Group Statistics and Performance (22)
10110b
17h
Group Statistics and Performance (23)
10111b
18h
Group Statistics and Performance (24)
11000b
19h
Group Statistics and Performance (25)
11001b
1Ah
Group Statistics and Performance (26)
11010b
1Bh
Group Statistics and Performance (27)
11011b
1Ch
Group Statistics and Performance (28)
11100b
1Dh
Group Statistics and Performance (29)
11101b
1Eh
Group Statistics and Performance (30)
11110b
1Fh
Group Statistics and Performance (31)
11111b
Table 382 — Group Statistics and Performance (n) subpage codes (part 2 of 2)
Subpage code
Log page name a
Group number b
a The statistics and performance information associated with a group number is
collected in the corresponding Group Statistics and Performance (n) log page
(e.g., operations associated with group number 10000b are logged in the
Group Statistics and Performance (16) log page).
b The GROUP NUMBER field is from the read command CDB or the write
command CDB (see table 375 in 7.3.6.1 and SBC-3).


7.3.7.2 Group n Statistics and Performance log parameter
The Group n Statistics and Performance log parameter has the format shown in table 383.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 383 for the Group n
Statistics and Performance log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for an unbounded data counter log parameter (see 7.3.2.2.2.3) for the Group n
Statistics and Performance log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 383 for the Group
n Statistics and Performance log parameter.
The GROUP N NUMBER OF READ COMMANDS field indicates the number of read commands (see table 375 in
7.3.6.1) received by the logical unit.
The GROUP N NUMBER OF WRITE COMMANDS field indicates the number of write commands (see table 375 in
7.3.6.1) received by the logical unit.
Table 383 — Group n Statistics and Performance log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – unbounded data counter log parameter (see 7.3.2.2.2.3)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (30h)
(MSB)
GROUP N NUMBER OF READ COMMANDS

•••
(LSB)
(MSB)
GROUP N NUMBER OF WRITE COMMANDS

•••
(LSB)
(MSB)
GROUP N NUMBER OF LOGICAL BLOCKS RECEIVED

•••
(LSB)
(MSB)
GROUP N NUMBER OF LOGICAL BLOCKS TRANSMIT-
TED

•••
(LSB)
(MSB)
GROUP N READ COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
GROUP N WRITE COMMAND PROCESSING INTERVALS

•••
(LSB)


The GROUP N NUMBER OF LOGICAL BLOCKS RECEIVED field indicates the number of logical blocks received by
any SCSI target port for the logical unit as a result of write commands (see table 375 in 7.3.6.1).
The GROUP N NUMBER OF LOGICAL BLOCKS TRANSMITTED field indicates the number of logical blocks transmitted
by any SCSI target port for the logical unit as a result of read commands (see table 375 in 7.3.6.1).
The GROUP N READ COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals
spent by the logical unit processing read commands (see table 375 in 7.3.6.1). Time intervals are defined in
the Time Interval log parameter (see 7.3.5.7) as returned in the General Statistics and Performance log page
(see 7.3.6).
The GROUP N WRITE COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals
spent by the logical unit processing write commands (see table 375 in 7.3.6.1). Time intervals are defined in
the Time Interval log parameter (see 7.3.5.7) as returned in the General Statistics and Performance log page
(see 7.3.6).


7.3.7.3 Group n Force Unit Access Statistics and Performance log parameter
The Group n Force Unit Access Statistics and Performance log parameter has the format shown in table 384.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 384 for the Group n
Force Unit Access Statistics and Performance log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for an unbounded data counter log parameter (see 7.3.2.2.2.3) for the Group n
Force Unit Access Statistics and Performance log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 384 for the Group
n Force Unit Access Statistics and Performance log parameter.
Table 384 — Group n Force Unit Access Statistics and Performance log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0004h)
(LSB)
Parameter control byte – unbounded data counter log parameter (see 7.3.2.2.2.3)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (40h)
(MSB)
GROUP N NUMBER OF READ FUA COMMANDS

•••
(LSB)
(MSB)
GROUP N NUMBER OF WRITE FUA COMMANDS

•••
(LSB)
(MSB)
GROUP N NUMBER OF READ FUA_NV COMMANDS

•••
(LSB)
(MSB)
GROUP N NUMBER OF WRITE FUA_NV COMMANDS

•••
(LSB)
(MSB)
GROUP N READ FUA COMMAND PROCESSING
INTERVALS

•••
(LSB)
(MSB)
GROUP N WRITE FUA COMMAND PROCESSING
INTERVALS

•••
(LSB)
(MSB)
GROUP N READ FUA_NV COMMAND PROCESSING
INTERVALS

•••
(LSB)
(MSB)
GROUP N WRITE FUA_NV COMMAND PROCESSING
INTERVALS

•••
(LSB)
