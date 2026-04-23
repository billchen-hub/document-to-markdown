# 7.3.14 Read Error Counters log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Generic protocol
specific port log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The PROTOCOL IDENTIFIER field contains one of the values shown in table 477 (see 7.6.1) to identify the SCSI
transport protocol standard that defines the SCSI transport protocol specific data in this log parameter.
The SCSI transport protocol specific data is defined by the corresponding SCSI transport protocol standard.
7.3.14 Read Error Counters log page
7.3.14.1 Overview
Using the format shown in table 404, the Read Error Counters log page (page code 03h) contains log param-
eters that report bounded data counters for detected events (e.g., total bytes processed) identified by the
parameter codes listed in table 403.
Table 403 — Read Error Counters log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Errors corrected without substantial
delay c
Reset Only
7.3.14.2
At least one b
0001h
Errors corrected with possible delays c
0002h
Total (e.g., rewrites or rereads) c
0003h
Total errors corrected c
0004h
Total times correction algorithm
processed c
0005h
Total bytes processed c
0006h
Total uncorrected errors c
8000h to
FFFFh
Vendor specific
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
b If the Read Error Counters log page is supported, at least one of the parameter codes listed in this table
shall be supported.
c The exact definition of this error counter is not part of this standard. This counter should not be used to
compare products because the products may define errors differently.


The Read Error Counters log page has the format shown in table 404.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 404 for the Read Error Counters
log page.
Each Read Error Counter log parameter contains the information described in 7.3.14.2.
7.3.14.2 Read Error Counter log parameter
The Read Error Counter log parameter has the format shown in table 405.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 403 for the Read Error
Counter log parameter.
Table 404 — Read Error Counters log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (03h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Read Error Counter log parameters
Read Error Counter log parameter (see 7.3.14.2)
[first]
•••
•••
Read Error Counter log parameter (see 7.3.14.2)
[last]
•••
n
Table 405 — Read Error Counter log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 403)
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
READ ERROR COUNTER
•••
n
(LSB)
