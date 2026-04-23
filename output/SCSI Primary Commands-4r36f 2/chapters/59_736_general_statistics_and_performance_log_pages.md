# 7.3.6 General Statistics and Performance log pages

The EXPONENT field contains the negative power of 10 exponent to multiply with the INTEGER field (e.g., a value
of 9 represents 10-9)
When multiplied by the exponent, the INTEGER field contains the value that represents one time interval (e.g., a
value of 5 in the INTEGER field and a value of 9 in the EXPONENT field represents a time interval of 510-9
seconds or 5 nanoseconds).
7.3.6  General Statistics and Performance log pages
7.3.6.1 Overview
Using the format shown in table 376, the General Statistics and Performance log page (page code 19h,
subpage code 00h) collects statistics and performance information for all read CDBs and write CDBs based
on the parameter codes listed in table 374.
The General Statistics and Performance log page provides the following statistics and performance results
associated to the addressed logical unit:
a)
Statistics and Performance log parameters:
A)
number of read commands;
B)
number of write commands;
C) number of read logical blocks transmitted by a target port;
D) number of write logical blocks received by a target port;
E)
read command processing time;
F)
write command processing time;
G) sum of the command weights of the read commands plus write commands;
H) sum of the weighted command time of the read commands plus write commands;
b)
Idle Time log parameter:
A)
idle time;
c)
Time Interval log parameter:
A)
time interval;
and
d)
Force Unit Access Statistics and Performance log parameters:
A)
number of read commands with the FUA bit (see SBC-3) set to one;
B)
number of write commands with the FUA bit set to one;
C) number of read commands with the FUA_NV bit (see SBC-3) set to one;
D) number of write commands with the FUA_NV bit set to one; and
Table 374 — General Statistics and Performance log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h
General Access Statistics and
Performance
Reset Only
7.3.6.2
Mandatory
0002h
Idle Time
Reset Only
7.3.6.3
Mandatory
0003h
Time Interval
Never
7.3.5.7
Mandatory
0004h
Force Unit Access Statistics and
Performance
Reset Only
7.3.6.4
Optional
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


E)
read command with the FUA bit set to one processing intervals;
F)
write command with the FUA bit set to one processing intervals;
G) read command with the FUA_NV bit set to one processing intervals; and
H) write command with the FUA_NV bit set to one processing intervals.
In the General Statistics and Performance log page and the Group Statistics and Performance (n) log pages
(see 7.3.7), read commands and write commands are those shown in table 375.
The General Statistics and Performance log page has the format shown in table 376.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 376 for the General Statistics and
Performance log page.
The contents of each general statistics and performance log parameter depends on the value in its PARAMETER
CODE field (see table 374).
Table 375 — Statistics and Performance log pages commands
Read commands a
Write commands a
POPULATE TOKEN
READ(10)
READ(12)
READ(16)
READ(32)
WRITE USING TOKEN
UNMAP
WRITE(10)
WRITE(12)
WRITE(16)
WRITE(32)
WRITE AND VERIFY(10)
WRITE AND VERIFY(12)
WRITE AND VERIFY(16)
WRITE AND VERIFY(32)
a See SBC-3.
Table 376 — General Statistics and Performance log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (19h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
General statistics and performance log parameters

General statistics and performance log parame-
ter
(see table 374) [first]

•••
•••
General statistics and performance log parame-
ter
(see table 374) [last]

•••
n


7.3.6.2 General Access Statistics and Performance log parameter
The General Access Statistics and Performance log parameter has the format shown in table 377.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 377 for the General
Access Statistics and Performance log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for an unbounded data counter log parameter (see 7.3.2.2.2.3) for the General
Access Statistics and Performance log parameter.
Table 377 — General Access Statistics and Performance log parameter
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
PARAMETER LENGTH (40h)
(MSB)
NUMBER OF READ COMMANDS

•••
(LSB)
(MSB)
NUMBER OF WRITE COMMANDS

•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS RECEIVED

•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS TRANSMITTED

•••
(LSB)
(MSB)
READ COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
WRITE COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
WEIGHTED NUMBER OF READ COMMANDS
PLUS WRITE COMMANDS

•••
(LSB)
(MSB)
WEIGHTED READ COMMAND PROCESSING
PLUS WRITE COMMAND PROCESSING

•••
(LSB)


The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 377 for the General
Access Statistics and Performance log parameter.
The NUMBER OF READ COMMANDS field indicates the number of read commands (see table 375 in 7.3.6.1)
received by the logical unit.
The NUMBER OF WRITE COMMANDS field indicates the number of write commands (see table 375 in 7.3.6.1)
received by the logical unit.
The NUMBER OF LOGICAL BLOCKS RECEIVED field indicates the number of logical blocks received by any SCSI
target port for the logical unit as a result of write commands (see table 375 in 7.3.6.1).
The NUMBER OF LOGICAL BLOCKS TRANSMITTED field indicates the number of logical blocks transmitted by any
SCSI target port for the logical unit as a result of read commands (see table 375 in 7.3.6.1).
The READ COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals (see
7.3.5.7) spent by the logical unit processing read commands (see table 375 in 7.3.6.1).
The WRITE COMMAND PROCESSING INTERVALS field indicates the cumulative number of time intervals (see
7.3.5.7) spent by the logical unit processing write commands (see table 375 in 7.3.6.1).
If command priority is supported (see SAM-5), then the WEIGHTED NUMBER OF READ COMMANDS PLUS WRITE
COMMANDS field indicates the cumulative command weight of the read commands and write commands (see
table 375 in 7.3.6.1) processed by the logical unit.
Command weight is calculated as follows:
command weight = (360 360  command priority)
where:
command priority is as defined in SAM-5. However, if the computed command priority is zero, then
the command priority shall be set to seven (i.e., a mid-range command priority value).
If command priority is not supported, then the WEIGHTED NUMBER OF READ COMMANDS PLUS WRITE COMMANDS
field shall be set to zero.
If command priority is supported (see SAM-5), then the WEIGHTED READ COMMAND PROCESSING PLUS WRITE
COMMAND PROCESSING field indicates the cumulative weighted command time of the time intervals (see
7.3.5.7) spent processing read commands and write commands (see table 375 in 7.3.6.1) by the logical unit.
Weighted command time is calculated as follows:
weighted command time = (time increments processing the command  time interval)
 (360 360  command priority)
where:
time increments processing a command is the number of time intervals from the time the task
manager places the command into a task set until the device server sends a SCSI transport protocol
service response for the command;
time interval is the value represented in the TIME INTERVAL DESCRIPTOR field of the Time Interval log
parameter (see 7.3.5.7), and


command priority is as defined in SAM-5. However, if the computed command priority is zero, then
the command priority time shall be set to seven (i.e., a mid-range command priority value).
If command priority is not supported, then the WEIGHTED READ COMMAND PROCESSING PLUS WRITE COMMAND
PROCESSING field shall be set to zero.
7.3.6.3 Idle Time log parameter
The Idle Time log parameter has the format shown in table 378.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 378 for the Idle Time
log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for an unbounded data counter log parameter (see 7.3.2.2.2.3) for the Idle Time log
parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 378 for the Idle
Time log parameter.
The IDLE TIME INTERVALS field indicates the cumulative number of idle times spent while there are no
commands in the task set and there are no commands being processed by the logical unit.
Idle time is calculated as follows:
idle time = (time increments not processing commands  time interval)
where:
time increments not processing commands is the number of time intervals while there are no
commands in the task set and the device server has sent a SCSI transport protocol service response
for all commands being processed (i.e., there are no commands to be processed or being processed);
and
time interval is the value represented in the time interval descriptor of the Time Interval log parameter
(see 7.3.5.7).
Table 378 — Idle Time log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0002h)
(LSB)
Parameter control byte – unbounded data counter log parameter (see 7.3.2.2.2.3)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
IDLE TIME INTERVALS

•••
(LSB)


7.3.6.4 Force Unit Access Statistics and Performance log parameter
The Force Unit Access Statistics and Performance log parameter has the format shown in table 379.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 379 for the Force Unit
Access Statistics and Performance log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for an unbounded data counter log parameter (see 7.3.2.2.2.3) for the Force Unit
Access Statistics and Performance log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 379 for the Force
Unit Access Statistics and Performance log parameter.
Table 379 — Force Unit Access Statistics and Performance log parameter
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
NUMBER OF READ FUA COMMANDS

•••
(LSB)
(MSB)
NUMBER OF WRITE FUA COMMANDS

•••
(LSB)
(MSB)
NUMBER OF READ FUA_NV COMMANDS

•••
(LSB)
(MSB)
NUMBER OF WRITE FUA_NV COMMANDS

•••
(LSB)
(MSB)
READ FUA COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
WRITE FUA COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
READ FUA_NV COMMAND PROCESSING INTERVALS

•••
(LSB)
(MSB)
WRITE FUA_NV COMMAND PROCESSING INTERVALS

•••
(LSB)
