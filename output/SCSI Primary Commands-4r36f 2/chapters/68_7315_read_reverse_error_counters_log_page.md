# 7.3.15 Read Reverse Error Counters log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Read Error
Counter log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The READ ERROR COUNTER field contains the value for the counter described by the contents of the PARAMETER
CODE field.
7.3.15 Read Reverse Error Counters log page
7.3.15.1 Overview
Using the format shown in table 407, the Read Reverse Error Counters log page (page code 04h) contains log
parameters that report bounded data counters for detected events (e.g., total bytes processed) identified by
the parameter codes listed in table 406.
Table 406 — Read Reverse Error Counters log page parameter codes
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
7.3.15.2
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
b If the Read Reverse Error Counters log page is supported, at least one of the parameter codes listed in
this table shall be supported.
c The exact definition of this error counter is not part of this standard. This counter should not be used to
compare products because the products may define errors differently.


The Read Reverse Error Counters log page has the format shown in table 407.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 407 for the Read Reverse Error
Counters log page.
Each Read Reverse Error Counter log parameter contains the information described in 7.3.15.2.
7.3.15.2 Read Reverse Error Counter log parameter
The Read Reverse Error Counter log parameter has the format shown in table 408.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 406 for the Read
Reverse Error Counter log parameter.
Table 407 — Read Reverse Error Counters log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (04h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Read reverse error counter log parameters
Read Reverse Error Counter log parameter (see
7.3.15.2) [first]
•••
•••
Read Reverse Error Counter log parameter (see
7.3.15.2) [last]
•••
n
Table 408 — Read Reverse Error Counter log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 406)
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
READ REVERSE ERROR COUNTER
•••
n
(LSB)
