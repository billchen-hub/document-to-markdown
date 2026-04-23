# 7.3.10 Last n Error Events log page

7.3.9.2 Deferred Error or Asynchronous Event log parameters
Each Deferred Error or Asynchronous Event log parameter has the format shown in table 390.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 388 for the Deferred
Error or Asynchronous Event log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Deferred Error or
Asynchronous Event log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The SENSE DATA field contains the sense data (see 4.5) for a deferred error or asynchronous event that has
occurred.
7.3.10 Last n Error Events log page
7.3.10.1 Overview
Using the format shown in table 392, the Last n Error Events log page (page code 07h) provides one or more
Error Event log parameters (see 7.3.10.2). The number of these Error Event log parameters supported (i.e., n)
is vendor specific. The parameter codes for the Last n Error Events log page are listed in table 391.
Table 390 — Deferred Error or Asynchronous Event log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 388)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
SENSE DATA (see 4.5)
•••
n
Table 391 — Last n Error Events log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Error Event
Reset Only
7.3.10.2
Mandatory
0001h to FFFFh
Optional
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


The Last n Error Events log page has the format shown in table 392.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 392 for the Last n Error Events log
page.
The contents of each error event log parameter is described are 7.3.10.2. The device server shall assign
parameter codes to log parameters as follows:
a)
if the vendor specific number of supported error event log parameters has not been exceeded, then
the parameter code in each log parameter shall indicate the relative time at which the error event
occurred. A higher parameter code indicates that the error event occurred later in time; or
b)
if the vendor specific number of supported error event log parameters has been exceeded, then:
A)
the log parameter with the oldest data shall be overwritten with the newest data (i.e., after the
highest supported parameter code is used, reporting wraps so that the next error event is
reported in the log parameter with parameter code zero); and
B)
if the RLEC bit is set to one in the Control mode page (see 7.5.8) and a LOG SELECT command
that transfers the Last n Error Events log page completes without error, except for the parameter
code being at its maximum value, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to RECOVERED ERROR, and the additional sense
code set to LOG LIST CODES EXHAUSTED.
Table 392 — Last n Error Events log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (07h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Error event log parameters
Error event log parameter (see 7.3.10.2) [first]
•••
•••
Error event log parameter (see 7.3.10.2) [last]
•••
n
