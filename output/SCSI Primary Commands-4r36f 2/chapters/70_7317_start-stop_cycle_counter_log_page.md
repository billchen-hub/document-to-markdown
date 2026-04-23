# 7.3.17 Start-Stop Cycle Counter log page

7.3.17 Start-Stop Cycle Counter log page
7.3.17.1 Overview
Using the format shown in table 415, the Start-Stop Cycle Counter log page (page code 0Eh) provides infor-
mation about manufacturing dates and cycle counts since date of manufacture using the parameter codes
listed in table 414.
The Start-Stop Cycle Counter log page has the format shown in table 415.
Table 414 — Start-Stop Cycle Counter log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h
Date of Manufacture
Never
7.3.17.2
At least one b
0002h
Accounting Date
Always
7.3.17.3
0003h
Specified Cycle Count Over Device
Lifetime
Never
7.3.17.4
0004h
Accumulated Start-Stop Cycles
Never
7.3.17.5
0005h
Specified Load-Unload Count Over
Device Lifetime
Never
7.3.17.6
0006h
Accumulated Load-Unload Cycles
Never
7.3.17.7
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
b If the Start-Stop Cycle Counter log page is supported, at least one of the parameter codes listed in this
table shall be supported.
Table 415 — Start-Stop Cycle Counter log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (0Eh)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Start stop cycle log parameters
Start stop cycle log parameter (see table 414)
[first]
•••
•••
Start stop cycle log parameter (see table 414)
[last]
•••
n


The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 415 for the Start-Stop Cycle
Counter log page.
7.3.17.2 Date of Manufacture log parameter
The Date of Manufacture log parameter has the format shown in table 416.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 416 for the Date of
Manufacture log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a ASCII format list log parameter (see 7.3.2.2.2.4) for the Date of Manufacture
log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 416 for the Date of
Manufacture log parameter.
The YEAR OF MANUFACTURE field indicates the year in which the SCSI target device was manufactured and
contains four numeric ASCII characters (e.g., 30h for zero and 39h for nine).
The WEEK OF MANUFACTURE field indicates the week of the year in which the SCSI target device was manufac-
tured and contains two numeric ASCII characters.
Table 416 — Date of Manufacture log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – ASCII format list log parameter (see 7.3.2.2.2.4)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (06h)
(MSB)
YEAR OF MANUFACTURE

•••
(LSB)
(MSB)
WEEK OF MANUFACTURE
(LSB)


7.3.17.3 Accounting Date log parameter
The Accounting Date log parameter has the format shown in table 417.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 417 for the Accounting
Date log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a ASCII format list log parameter (see 7.3.2.2.2.4) for the Accounting Date log
parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 417 for the
Accounting Date log parameter.
The ACCOUNTING DATE YEAR field indicates the year in which the SCSI target device was placed in service and
contains four numeric ASCII characters (e.g., 30h for zero and 39h for nine).
The ACCOUNTING DATE WEEK field indicates the week of the year in which the SCSI target device was placed in
service and contains two numeric ASCII characters.
A LOG SELECT command may be used to change the value of the ACCOUNTING DATE YEAR field and
ACCOUNTING DATE WEEK field. If the Accounting Date log parameter is not yet set, then the value placed:
a)
in the ACCOUNTING DATE YEAR field shall be four ASCII space characters (i.e., 20h); and
b)
in the ACCOUNTING DATE WEEK field shall be two ASCII space characters (i.e., 20h).
The ACCOUNTING DATE YEAR field and ACCOUNTING DATE WEEK field shall not be checked for validity by the
device server.
Table 417 — Accounting Date log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0002h)
(LSB)
Parameter control byte – ASCII format list log parameter (see 7.3.2.2.2.4)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (06h)
(MSB)
ACCOUNTING DATE YEAR

•••
(LSB)
(MSB)
ACCOUNTING DATE WEEK
(LSB)


7.3.17.4 Specified Cycle Count Over Device Lifetime log parameter
The Specified Cycle Count Over Device Lifetime log parameter has the format shown in table 418.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 418 for the Specified
Cycle Count Over Device Lifetime log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Specified Cycle Count
Over Device Lifetime log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 418 for the
Specified Cycle Count Over Device Lifetime log parameter.
The contents of the SPECIFIED CYCLE COUNT OVER DEVICE LIFETIME field indicate the number of stop-start cycles
that may be performed over the lifetime of the SCSI target device without degrading the SCSI target device's
operation or reliability outside the limits specified by the manufacturer of the SCSI target device.
7.3.17.5 Accumulated Start-Stop Cycles log parameter
The Accumulated Start-Stop Cycles log parameter has the format shown in table 419.
Table 418 — Specified Cycle Count Over Device Lifetime log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0003h)
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
SPECIFIED CYCLE COUNT OVER DEVICE LIFETIME

•••
(LSB)
Table 419 — Accumulated Start-Stop Cycles log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0004h)
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
ACCUMULATED START-STOP CYCLES

•••
(LSB)


The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 419 for the Accumu-
lated Start-Stop Cycles log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Accumulated Start-Stop
Cycles log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 419 for the
Accumulated Start-Stop Cycles log parameter.
The contents of the ACCUMULATED START-STOP CYCLES field indicate the number of stop-start cycles the SCSI
target device has detected since its date of manufacture. This saturating counter is incremented by one for
each complete cycle. The time in the cycle at which the counter is incremented is vendor specific.
For rotating magnetic storage devices (see SBC-3), a single start-stop cycle is defined as an operational cycle
that:
a)
begins with the disk spindle at rest;
b)
continues while the disk accelerates to its normal operational rotational rate;
c)
continues during the entire period the disk is rotating;
d)
continues as the disk decelerates toward a resting state; and
e)
ends when the disk is no longer rotating.
For devices without a spindle or with multiple spindles, the definition of a single start-stop cycle is vendor
specific.
The device server shall not compare the contents of the ACCUMULATED START-STOP CYCLES field to contents of
the SPECIFIED CYCLE COUNT OVER DEVICE LIFETIME field (see 7.3.17.4).
7.3.17.6 Specified Load-Unload Count Over Device Lifetime log parameter
The Specified Load-Unload Count Over Device Lifetime log parameter has the format shown in table 420.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 420 for the Specified
Load-Unload Count Over Device Lifetime log parameter.
Table 420 — Specified Load-Unload Count Over Device Lifetime log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0005h)
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
SPECIFIED LOAD-UNLOAD COUNT OVER DEVICE
LIFETIME

•••
(LSB)


The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Specified Load-Unload
Count Over Device Lifetime log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 420 for the
Specified Load-Unload Count Over Device Lifetime log parameter.
The contents of the SPECIFIED LOAD-UNLOAD COUNT OVER DEVICE LIFETIME field indicate the number of
load-unload cycles that may be performed over the lifetime of the SCSI target device without degrading the
SCSI target device's operation or reliability outside the limits specified by the manufacturer of the SCSI target
device.
7.3.17.7 Accumulated Load-Unload Cycles log parameter
The Accumulated Load-Unload Cycles log parameter has the format shown in table 421.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 421 for the Accumu-
lated Load-Unload Cycles log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Accumulated
Load-Unload Cycles log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 421 for the
Accumulated Load-Unload Cycles log parameter.
The contents of the ACCUMULATED LOAD-UNLOAD CYCLES field indicate the number of load-unload cycles the
SCSI target device has detected since its date of manufacture. This saturating counter is incremented by one
for each complete cycle. The time in the cycle at which the counter is incremented is vendor specific.
For rotating magnetic storage devices (see SBC-3), a single load-unload cycle is defined as an operational
cycle that:
a)
begins with the heads unloaded from the medium;
b)
continues while the heads are loaded onto the spinning medium; and
c)
ends when the heads are unloaded from the medium.
Table 421 — Accumulated Load-Unload Cycles log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0006h)
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
ACCUMULATED LOAD-UNLOAD CYCLES

•••
(LSB)


The Accumulated Load-Unload Cycles log parameter is not applicable to rotating magnetic storage devices
without unloadable heads.
The device server shall not compare the contents of the ACCUMULATED LOAD-UNLOAD CYCLES field to contents
of the SPECIFIED LOAD-UNLOAD COUNT OVER DEVICE LIFETIME field (see 7.3.17.6).
7.3.18 Supported Log Pages log page
For the LOG SENSE command, the Supported Log Pages log page (see table 422) returns the list of log
pages implemented by the logical unit. Logical units that implement the LOG SENSE command shall
implement this log page. This log page is not defined for the LOG SELECT command.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The DS
bit, SPF bit, SUBPAGE CODE field shall be set as shown in table 422 for the Supported Log Pages log page.
The supported page descriptors shall contain a list of all log page codes (see table 423) with a subpage code
of zero implemented by the logical unit in ascending order beginning with page code 00h.
The PAGE CODE field indicates the number of a supported log page.
Table 422 — Supported Log Pages log page
Bit
Byte
DS (0b)
SPF (0b)
PAGE CODE (00h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported pages list
Supported page descriptor (see table 423) [first]
•••
n
Supported page descriptor (see table 423) [last]
Table 423 — Supported page descriptor
Bit
Byte
Reserved
PAGE CODE


7.3.19 Supported Log Pages and Subpages log page
For the LOG SENSE command, the Supported Log Pages and Subpages log page (see table 424) returns the
list of log pages and subpages implemented by the logical unit. If log subpages are supported this page shall
be supported. This log page is not defined for the LOG SELECT command.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The DS
bit, SPF bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 424 for the Supported Log
Pages and Subpages log page.
The supported page/subpage descriptors (see table 425) shall be in ascending order sorted by page code
then subpage code.
The PAGE CODE field indicates the number of a supported log page.
The SUBPAGE CODE field indicates the subpage number of a supported log page.
Table 424 — Supported Log Pages and Subpages log page
Bit
Byte
DS (0b)
SPF (1b)
PAGE CODE (00h)
SUBPAGE CODE (FFh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported page/subpage descriptors
Supported page/subpage descriptor (see table
425) [first]
•••
n-1
Supported page/subpage descriptor (see table
425) [last]
n
Table 425 — Supported page/subpage descriptor
Bit
Byte
Reserved
PAGE CODE
SUBPAGE CODE


7.3.20 Supported Subpages log page
For the LOG SENSE command, the Supported Subpages log page (see table 426) returns the list of all
subpage codes (i.e., 00h to FFh) that are implemented by the logical unit for a specified page code. If log
subpages are supported this page shall be supported. This log page is not defined for the LOG SELECT
command.
The DS bit, SPF bit, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The DS bit, SPF bit,
SUBPAGE CODE field shall be set as shown in table 426 for the Supported Subpages log page.
The PAGE CODE field (see 7.3.2) indicates the log page for which log page and subpage codes are being
returned.
The supported subpage descriptors (see table 427) shall be in ascending order sorted by page code then
subpage code, and shall include a descriptor with subpage code 00h for any implemented log page in which
the SPF bit is set to zero.
The PAGE CODE field indicates the number of a supported log page.
NOTE 45 - The page code is the same in the page header (see table 426) and in each supported subpage
descriptor (see table 427).
The SUBPAGE CODE field indicates the subpage number of a supported log page.
Table 426 — Supported Subpages log page
Bit
Byte
DS (0b)
SPF (1b)
PAGE CODE
SUBPAGE CODE (FFh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported subpage descriptors
Supported subpage descriptor (see table 427)
[first]
•••
n-1
Supported subpage descriptor (see table 427)
[last]
n
Table 427 — Supported subpage descriptor
Bit
Byte
Reserved
PAGE CODE
SUBPAGE CODE
