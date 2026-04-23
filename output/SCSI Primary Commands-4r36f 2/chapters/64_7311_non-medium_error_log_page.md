# 7.3.11 Non-Medium Error log page

7.3.10.2 Error Event log parameters
Each Error Event log parameter has the format shown in table 393.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 391 for the Error Event
log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a ASCII format list log parameter (see 7.3.2.2.2.4) for the Error Event log
parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The ERROR EVENT DATA field contains ASCII data (see 4.3.1) that may describe the error event. The contents
of the ERROR EVENT DATA field are not defined by this standard.
7.3.11 Non-Medium Error log page
7.3.11.1 Overview
Using the format shown in table 395, the Non-Medium Error log page (page code 06h) provides for counting
the occurrences of recoverable error events other than read (see 7.3.14), read reverse (see 7.3.15), verify
(see 7.3.22), or write (see 7.3.23) failures. No discrimination among the various types of events is provided.
Vendor specific discrimination may be provided through the vendor specific parameter codes. The parameter
codes for the Non-Medium Error log page are listed in table 394.
Table 393 — Error Event log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 391)
(LSB)
Parameter control byte – ASCII format list log parameter (see 7.3.2.2.2.4)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
ERROR EVENT DATA
•••
n
Table 394 — Non-Medium Error log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Non-Medium Error Count
Reset Only
7.3.11.2
Mandatory
8000h to FFFFh
Vendor specific error counts
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


The Non-Medium Error log page has the format shown in table 395.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 395 for the Non-Medium Error log
page.
The contents of each non-medium error log parameter depends on the value in its PARAMETER CODE field (see
table 394).
7.3.11.2 Non-Medium Error Count log parameter
The Non-Medium Error Count log parameter has the format shown in table 396.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 396 for the
Non-Medium Error Count log parameter.
Table 395 — Non-Medium Error log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (06h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Non-medium error log parameters
Non-medium error log parameter (see table 394)
[first]
•••
•••
Non-medium error log parameter (see table 394)
[last]
•••
n
Table 396 — Non-Medium Error Count log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
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
NON-MEDIUM ERROR COUNT
•••
n
(LSB)
