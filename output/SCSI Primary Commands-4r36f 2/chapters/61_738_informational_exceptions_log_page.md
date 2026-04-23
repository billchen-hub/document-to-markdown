# 7.3.8 Informational Exceptions log page

The GROUP N NUMBER OF READ FUA COMMANDS field indicates the number of read commands (see table 375 in
7.3.6.1) with the FUA bit (see SBC-3) set to one received by the logical unit.
The GROUP N NUMBER OF WRITE FUA COMMANDS field indicates the number of write commands (see table 375 in
7.3.6.1) with the FUA bit (see SBC-3) set to one received by the logical unit.
The GROUP N NUMBER OF READ FUA_NV COMMANDS field indicates the number of read commands (see table
375 in 7.3.6.1) with the FUA_NV bit (see SBC-3) set to one received by the logical unit.
The GROUP N NUMBER OF WRITE FUA_NV COMMANDS field indicates the number of write commands (see table
375 in 7.3.6.1) with the FUA_NV bit (see SBC-3) set to one received by the logical unit.
The GROUP N READ FUA COMMAND PROCESSING INTERVALS field indicates the cumulative number of time
intervals spent by the logical unit processing read commands (see table 375 in 7.3.6.1) with the FUA bit (see
SBC-3) set to one. Time intervals are defined in the Time Interval log parameter (see 7.3.5.7) as returned in
the General Statistics and Performance log page (see 7.3.6).
The GROUP N WRITE FUA COMMAND PROCESSING INTERVALS field indicates the cumulative number of time
intervals spent by the logical unit processing write commands (see table 375 in 7.3.6.1) with the FUA bit (see
SBC-3) set to one. Time intervals are defined in the Time Interval log parameter (see 7.3.5.7) as returned in
the General Statistics and Performance log page (see 7.3.6).
The GROUP N READ FUA_NV COMMAND PROCESSING INTERVALS field indicates the cumulative number of time
intervals spent by the logical unit processing read commands (see table 375 in 7.3.6.1) with the FUA_NV bit
(see SBC-3) set to one. Time intervals are defined in the Time Interval log parameter (see 7.3.5.7) as returned
in the General Statistics and Performance log page (see 7.3.6).
The GROUP N WRITE FUA_NV COMMAND PROCESSING INTERVALS field indicates the cumulative number of time
intervals spent by the logical unit processing write commands (see table 375 in 7.3.6.1) with the FUA_NV bit
(see SBC-3) set to one. Time intervals are defined in the Time Interval log parameter (see 7.3.5.7) as returned
in the General Statistics and Performance log page (see 7.3.6).
7.3.8 Informational Exceptions log page
7.3.8.1 Overview
Using the format shown in table 386, the Informational Exceptions log page (page code 2Fh) reports details
about informational exceptions identified by the parameter codes listed in table 385.
Table 385 — Informational Exceptions log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Informational Exceptions General
Reset Only
7.3.8.2
Mandatory
0001h to FFFFh
Vendor specific
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


The Informational Exceptions log page has the format shown in table 386.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 386 for the Informational Excep-
tions log page.
The contents of each informational exceptions log parameter depends on the value in its PARAMETER CODE
field (see table 385).
7.3.8.2 Informational Exceptions General log parameter
The Informational Exceptions General log parameter has the format shown in table 387.
Table 386 — Informational Exceptions log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (2Fh)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Informational exceptions log parameters

Informational exceptions log parameter
(see table 385) [first]

•••
•••
Informational exceptions log parameter
(see table 385) [last]

•••
n
Table 387 — Informational Exceptions General log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
INFORMATIONAL EXCEPTION ADDITIONAL SENSE CODE
INFORMATIONAL EXCEPTION ADDITIONAL SENSE CODE QUALIFIER
MOST RECENT TEMPERATURE READING
Vendor specific
•••
n
