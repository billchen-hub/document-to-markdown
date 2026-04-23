# 7.3.13 Protocol Specific Port log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Accumulated Transi-
tions log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 399 for the
Accumulated Transitions log parameter.
The ACCUMULATED TRANSITIONS TO field contains a saturating counter that is incremented by one at a time
defined by the contents of the parameter code field as described in table 400. The time in the transition at
which the count is incremented is vendor specific.
All values in the ACCUMULATED TRANSITIONS TO field are accumulated from the time the SCSI target device is
manufactured.
7.3.13 Protocol Specific Port log page
7.3.13.1 Overview
Using the format shown in table 401, the Protocol Specific Port log page (page code 18h) provides SCSI
transport protocol specific parameters that are associated with the SCSI target ports in the SCSI target device.
This log page may be implemented in any logical unit, including the TARGET LOG PAGES well-known logical
unit (see 8.4).
Protocol Specific Port log pages do not identify the information being logged using the PARAMETER CODE field
in each log parameter. Instead, the SUBPAGE CODE field in the log page header (see table 401) serves as the
indicator of what logged information is present. The PARAMETER CODE field identifies the SCSI Target Port to
which the logged information applies.
Table 400 — Accumulated Transitions parameter codes and saturating counters
Parameter code
Saturating counter incremented while the device server transitions
from any other power condition to this power condition
0001h
active power condition (see 5.12.4)
0002h
idle_a power condition (see 5.12.5)
0003h
idle_b power condition (see 5.12.5)
0004h
idle_c power condition (see 5.12.5)
0008h
standby_z power condition (see 5.12.6)
0009h
standby_y power condition (see 5.12.6)


The Protocol Specific Port log page has the format shown in table 401.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 401 for the Protocol Specific Port
log page.
The contents of each protocol specific port log parameter is defined by the corresponding SCSI transport
protocol standard.
7.3.13.2 Generic protocol specific port log parameter
The generic format of a protocol specific port log parameter is shown in table 402.
For the Generic protocol specific port log parameter, the PARAMETER CODE field is described in 7.3.2.2.1, and
contains the relative target port identifier of the target port for which the parameter data applies.
Table 401 — Protocol Specific Port log page
Bit
Byte
DS
SPF
PAGE CODE (18h)
SUBPAGE CODE (00h to FEh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Protocol specific port log parameters
Protocol specific port log parameter [first]
•••
•••
Protocol specific port log parameter [last]
•••
n
Table 402 — Generic protocol specific port log parameter
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
PARAMETER LENGTH (n-3)
Reserved
PROTOCOL IDENTIFIER
SCSI transport protocol specific
•••
n
