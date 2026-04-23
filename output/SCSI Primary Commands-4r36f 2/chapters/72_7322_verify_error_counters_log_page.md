# 7.3.22 Verify Error Counters log page

7.3.22 Verify Error Counters log page
7.3.22.1 Overview
Using the format shown in table 433, the Verify Error Counters log page (page code 05h) contains log param-
eters that report bounded data counters for detected events (e.g., total bytes processed) identified by the
parameter codes listed in table 432.
Table 432 — Verify Error Counters log page parameter codes
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
7.3.22.2
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
b If the Verify Error Counters log page is supported, at least one of the parameter codes listed in this table
shall be supported.
c The exact definition of this error counter is not part of this standard. This counter should not be used to
compare products because the products may define errors differently.


The Verify Error Counters log page has the format shown in table 433.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 433 for the Verify Error Counters
log page.
Each Verify Error Counter log parameter contains the information described in 7.3.22.2.
7.3.22.2 Verify Error Counter log parameter
The Verify Error Counter log parameter has the format shown in table 434.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 432 for the Verify Error
Counter log parameter.
Table 433 — Verify Error Counters log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (05h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Verify error counter log parameters
Verify Error Counter log parameter (see 7.3.22.2)
[first]
•••
•••
Verify Error Counter log parameter (see 7.3.22.2)
[last]
•••
n
Table 434 — Verify Error Counter log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 432)
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
VERIFY ERROR COUNTER
•••
n
(LSB)
