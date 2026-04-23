# 7.3.4 Buffer Over-Run/Under-Run log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the General Usage Appli-
cation Client log parameter.
The contents of the GENERAL USAGE PARAMETER BYTES field represent data sent to the device server in a
previous LOG SELECT command. If a previous LOG SELECT command has not occurred, the contents of
the GENERAL USAGE PARAMETER BYTES field are vendor specific.
7.3.4 Buffer Over-Run/Under-Run log page
7.3.4.1 Overview
Using the format shown in table 362, the Buffer Over-Run/Under-Run log page (page code 01h) defines
bounded data counters that record the number of buffer over-runs or under-runs detected by the device
server. The parameter codes for the Buffer Over-Run/Under-Run log page are listed in table 361.
Table 361 — Buffer Over-Run/Under-Run log page parameter codes (part 1 of 2)
Parameter
code a
Incremented once per:
Resettable or
Changeable b
Reference
Support
requirements
Over- or
Under-run
Experienced
by (or during)
Problem
detected
0000h
Under-run
Undefined
Undefined
Reset Only
7.3.4.2
At least one c
0001h
Over-run
0020h
Under-run
A command
0021h
Over-run
0040h
Under-run
An I_T nexus
0041h
Over-run
0080h
Under-run
A unit of time d
0081h
Over-run
0002h
Under-run
Undefined
Service
delivery
subsystem
busy
Reset Only
7.3.4.2
At least one c
0003h
Over-run
0022h
Under-run
A command
0023h
Over-run
0042h
Under-run
An I_T nexus
0043h
Over-run
0082h
Under-run
A unit of time d
0083h
Over-run
a See SPC-2 for a description of how these parameter codes are derived.
b The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
c If the Buffer Over-Run/Under-Run log page is supported, at least one of the parameter codes listed in
this table shall be supported.
d The size of the unit of time is vendor specific.


A buffer over-run or under-run may occur if a SCSI initiator device does not transmit data to or from the logical
unit’s buffer fast enough to keep up with reading or writing the media. A buffer over-run condition may occur
during a read operation if a buffer full condition prevents continued transfer of data from the media to the
buffer. A buffer under-run condition may occur during a write operation if a buffer empty condition prevents
continued transfer of data to the media from the buffer. Most devices incur a delay at this point while the media
is repositioned.
0004h
Under-run
Undefined
Transfer
rate too
slow
Reset Only
7.3.4.2
At least one c
0005h
Over-run
0024h
Under-run
A command
0025h
Over-run
0044h
Under-run
An I_T nexus
0045h
Over-run
0084h
Under-run
A unit of time d
0085h
Over-run
all others
Reserved
Table 361 — Buffer Over-Run/Under-Run log page parameter codes (part 2 of 2)
Parameter
code a
Incremented once per:
Resettable or
Changeable b
Reference
Support
requirements
Over- or
Under-run
Experienced
by (or during)
Problem
detected
a See SPC-2 for a description of how these parameter codes are derived.
b The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
c If the Buffer Over-Run/Under-Run log page is supported, at least one of the parameter codes listed in
this table shall be supported.
d The size of the unit of time is vendor specific.


The Buffer Over-Run/Under-Run log page has the format shown in table 362.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 362 for the Buffer
Over-Run/Under-Run log page.
Each Buffer Over-run/Under-run log parameter contains the information described in 7.3.4.2.
7.3.4.2 Buffer Over-run/Under-run log parameter
The Buffer Over-run/Under-run log parameter has the format shown in table 363.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 361 for the Buffer
Over-run/Under-run log parameter log parameter.
Table 362 — Buffer Over-Run/Under-Run log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (01h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Buffer over-run/under-run log parameters
Buffer Over-run/Under-run log parameter
(see 7.3.4.2) [first]
•••
•••
Buffer Over-run/Under-run log parameter
(see 7.3.4.2) [last]
•••
n
Table 363 — Buffer Over-run/Under-run log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 361)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
(MSB)
OVER-RUN/UNDER-RUN COUNTER
•••
n
(LSB)
