# 7.3.5 Cache Memory Statistics log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Buffer
Over-run/Under-run log parameter log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The OVER-RUN/UNDER-RUN COUNTER field contains the value for the counter described by the contents of the
PARAMETER CODE field.
Each counter contains the total number of times buffer over-run or under-run conditions have occurred since
the last time the counter was reset. The counter shall be incremented for each occurrence of a buffer
under-run or over-run condition and may be incremented more than once for multiple occurrences during the
processing of a single command.
7.3.5 Cache Memory Statistics log page
7.3.5.1 Overview
Using the format shown in table 366, the Cache Memory Statistics log page (page code 19h, subpage code
20h) contains statistics and performance results identified by the parameter codes listed in table 364.
The Cache Memory Statistics log page provides the following statistics and performance results associated
with the addressed logical unit:
a)
Cache Memory Statistics log parameters:
A)
number of read cache memory hits;
B)
number of reads to cache memory;
C) number of write cache memory hits; and
D) number of writes from cache memory;
b)
Hard Reset log parameter:
A)
time from last hard reset (see SAM-5);
and
c)
Time Interval log parameter:
A)
time interval.
Table 364 — Cache Memory Statistics log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h
Read Cache Memory Hits
Reset Only
7.3.5.2
At least one b
0002h
Reads To Cache Memory
Reset Only
7.3.5.3
0003h
Write Cache Memory Hits
Reset Only
7.3.5.4
0004h
Writes From Cache Memory
Reset Only
7.3.5.5
0005h
Time From Last Hard Reset
Never
7.3.5.6
0006h
Time Interval
Never
7.3.5.7
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
b If the Cache Memory Statistics log page is supported, at least one of the parameter codes listed in this
table shall be supported.


In the Cache Memory Statistics log page, read commands and write commands are those shown in table 365.
The Cache Memory Statistics log page has the format shown in table 366.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 366 for the Cache Memory
Statistics log page.
The contents of each cache memory statistics log parameter depends on the value in its PARAMETER CODE
field (see table 364).
Table 365 — Cache Memory Statistics log page commands
Read commands a
Write commands a
READ(10)
READ(12)
READ(16)
READ(32)
PRE-FETCH(10)
PRE-FETCH(16)
SYNCHRONIZE CACHE(10)
SYCNHRONIZE CACHE(16)
WRITE(10)
WRITE(12)
WRITE(16)
WRITE(32)
WRITE AND VERIFY(10)
WRITE AND VERIFY(12)
WRITE AND VERIFY(16)
WRITE AND VERIFY(32)
a See SBC-3.
Table 366 — Cache Memory Statistics log page
Bit
Byte
DS
SPF (1b)
PAGE CODE (19h)
SUBPAGE CODE (20h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Cache memory statistics log parameters

Cache memory statistics log parameter
(see table 364) [first]
•••
•••

Cache memory statistics log parameter
(see table 364) [last]
•••
n


7.3.5.2 Read Cache Memory Hits log parameter
The Read Cache Memory Hits log parameter has the format shown in table 367.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 367 for the Read
Cache Memory Hits log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Read Cache
Memory Hits log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 367 for the Read
Cache Memory Hits log parameter.
The NUMBER OF READ CACHE MEMORY HITS field indicates the number of read commands (see table 365 in
7.3.5.1) received on an I_T nexus that resulted in:
a)
user data being read from cache memory; and
b)
no user data read from the medium before the read command being processed is completed.
The NUMBER OF READ CACHE MEMORY HITS field shall not be modified as a result of any read command that
contains an FUA bit (see SBC-3) set to one or an FUA_NV bit (see SBC-3) set to one.
The contents of the NUMBER OF READ CACHE MEMORY HITS field shall be set to zero as part of processing a hard
reset condition (see SAM-5).
Table 367 — Read Cache Memory Hits log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
NUMBER OF READ CACHE MEMORY HITS

•••
(LSB)


7.3.5.3 Reads To Cache Memory Hits log parameter
The Reads To Cache Memory log parameter has the format shown in table 368.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 368 for the Reads To
Cache Memory log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Reads To Cache
Memory log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 368 for the Reads
To Cache Memory log parameter.
The NUMBER OF READS TO CACHE MEMORY field indicates the number of read commands (see table 365 in
7.3.5.1) initiated to move user data from the medium to cache memory.
The NUMBER OF READS TO CACHE MEMORY field shall not be modified as a result of any read command that
contains an FUA bit (see SBC-3) set to one or an FUA_NV bit (see SBC-3) set to one.
The contents of the NUMBER OF READS TO CACHE MEMORY field shall be set to zero as part of processing a hard
reset condition (see SAM-5).
Table 368 — Reads To Cache Memory log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0002h)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
NUMBER OF READS TO CACHE MEMORY

•••
(LSB)


7.3.5.4 Write Cache Memory Hits log parameter
The Write Cache Memory Hits log parameter has the format shown in table 369.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 369 for the Write
Cache Memory Hits log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Writes From
Cache Memory log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 369 for the Write
Cache Memory Hits log parameter.
The NUMBER OF WRITES FROM CACHE MEMORY field indicates the number of write commands (see table 365 in
7.3.5.1) received on an I_T nexus that resulted in:
a)
user data being written to cache memory; and
b)
no user data written to the medium before the write command being processed is completed.
The NUMBER OF WRITES FROM CACHE MEMORY field shall not be modified as a result of any read command that
contains an FUA bit (see SBC-3) set to one or an FUA_NV bit (see SBC-3) set to one.
The contents of the NUMBER OF WRITES FROM CACHE MEMORY field shall be set to zero as part of processing a
hard reset condition (see SAM-5).
Table 369 — Write Cache Memory Hits log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0003h)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
NUMBER OF WRITES FROM CACHE MEMORY

•••
(LSB)


7.3.5.5 Writes From Cache Memory Hits log parameter
The Writes From Cache Memory log parameter has the format shown in table 370.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 370 for the Writes From
Cache Memory log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Writes From
Cache Memory log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 370 for the Writes
From Cache Memory log parameter.
The NUMBER OF WRITES FROM CACHE MEMORY field indicates the number of write commands (see table 365 in
7.3.5.1) initiated to move user data from cache memory to the medium.
The NUMBER OF WRITES FROM CACHE MEMORY field shall not be modified as a result of any read command that
contains an FUA bit (see SBC-3) set to one or an FUA_NV bit (see SBC-3) set to one.
The contents of the NUMBER OF WRITES FROM CACHE MEMORY field shall be set to zero as part of processing a
hard reset condition (see SAM-5).
Table 370 — Writes From Cache Memory log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0004h)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
NUMBER OF WRITES FROM CACHE MEMORY

•••
(LSB)


7.3.5.6 Time From Last Hard Reset log parameter
The Time From Last Hard Reset log parameter has the format shown in table 371.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 371 for the Time From
Last Hard Reset log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Time From Last
Hard Reset log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 371 for the Time
From Last Hard Reset log parameter.
The LAST HARD RESET INTERVALS field indicates the number of time intervals that have occurred since a hard
reset was processed by the logical unit.
The time since a hard reset was processed by the logical unit is calculated as follows:
time = (time intervals since last hard reset  time interval)
where:
time intervals since last hard reset is the contents of the LAST HARD RESET INTERVALS field; and
time interval is the value represented in the time interval descriptor of the Time Interval log parameter
(see table 372 in 7.3.5.7).
Table 371 — Time From Last Hard Reset log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0005h)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
LAST HARD RESET INTERVALS

•••
(LSB)


7.3.5.7 Time Interval log parameter
The Time Interval log parameter has the format shown in table 372.
The PARAMETER CODE field is described in 7.3.2.2.1. A PARAMETER CODE field set to:
a)
0003h identifies the log parameter being transferred as the Time Interval log parameter in the General
Statistics and Performance log page (see 7.3.6); or
b)
0006h identifies the log parameter being transferred as the Time Interval log parameter in the Cache
Memory Statistics log page (see 7.3.5).
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the log parameters
described in this subclause.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 372 for the log
parameters described in this subclause.
The time interval descriptor (see table 373) contains the time interval in seconds used in various time interval
fields in the:
a)
Time From Last Hard Reset log parameter (see 7.3.5.6);
b)
General Access Statistics and Performance log parameter (see 7.3.6.2);
c)
Force Unit Access Statistics and Performance log parameter (see 7.3.6.4);
d)
Group n Statistics and Performance log parameter (see 7.3.7.2); and
e)
Group n Force Unit Access Statistics and Performance log parameter (see 7.3.7.3).
Table 372 — Time Interval log parameter
Bit
Byte
(MSB)
PARAMETER CODE
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (08h)
Time interval descriptor (see table 373)

•••
Table 373 — Time interval descriptor
Bit
Byte
(MSB)
EXPONENT

•••
(LSB)
(MSB)
INTEGER

•••
(LSB)
