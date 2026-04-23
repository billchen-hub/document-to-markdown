# 7.3.12 Power Condition Transitions log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Non-Medium
Error Count log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The NON-MEDIUM ERROR COUNT field indicates the number of recoverable error events other than read, read
reverse, verify, or write failures.
7.3.12 Power Condition Transitions log page
7.3.12.1 Overview
Using the format shown in table 398, the Power Condition Transitions log page (page code 1Ah) provides a
count of the occurrences of power condition transition events using the parameter codes listed in table 397.
Table 397 — Power Conditions Transitions log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h
Accumulated Transitions to active
Never
7.3.12.2
Mandatory
0002h
Accumulated Transitions to idle_a
At least one b
0003h
Accumulated Transitions to idle_b
0004h
Accumulated Transitions to idle_c
0008h
Accumulated Transitions to standby_z
0009h
Accumulated Transitions to standby_y
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
b If the Power Conditions Transitions log page is supported, at least one of these parameter codes shall
be supported.


The Power Conditions Transitions log page has the format shown in table 398.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 398 for the Power Conditions
Transitions log page.
The contents of each power condition transitions log parameter depends on the value in its PARAMETER CODE
field (see table 397).
7.3.12.2 Accumulated Transitions log parameter
The Accumulated Transitions log parameter has the format shown in table 399.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 399 for the Accumu-
lated Transitions log parameter.
Table 398 — Power Condition Transitions log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (1Ah)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Power condition transitions log parameters
Power condition transitions log parameter (see
table 397) [first]
•••
•••
Power condition transitions log parameter (see
table 397) [last]
•••
n
Table 399 — Accumulated Transitions log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 397)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (04h)
(MSB)
ACCUMULATED TRANSITIONS TO

•••
(LSB)
