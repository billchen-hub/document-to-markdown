# 8.3.3 ACCESS CONTROL OUT command

If the access controls coordinator does not have enough resources to create and manage a new proxy token,
the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INSUFFICIENT ACCESS CONTROL RESOURCES.
The ALLOCATION LENGTH field is defined in 4.2.5.6. The ALLOCATION LENGTH field value should be at least eight.
The CONTROL byte is defined in SAM-5.
The format of the parameter data returned by the ACCESS CONTROL IN command with REQUEST PROXY
TOKEN service action is shown in table 695.
8.3.3 ACCESS CONTROL OUT command
8.3.3.1 ACCESS CONTROL OUT introduction
The service actions of the ACCESS CONTROL OUT command (see table 696) are used to request service
actions by the access controls coordinator to limit or grant access to the logical units by initiator ports. If the
ACCESS CONTROL OUT command is implemented, the ACCESS CONTROL IN command also shall be
implemented. The ACCESS CONTROL OUT command shall not be affected by access controls.
Table 695 — ACCESS CONTROL IN with REQUEST PROXY TOKEN parameter data
Bit
Byte
PROXY TOKEN
•••
Table 696 — ACCESS CONTROL OUT service actions
Service
action code
Service action name
Type
Reference
00h
MANAGE ACL
M
8.3.3.2
01h
DISABLE ACCESS CONTROLS
M
8.3.3.3
02h
ACCESS ID ENROLL
M
8.3.3.4
03h
CANCEL ENROLLMENT
M
8.3.3.5
04h
CLEAR ACCESS CONTROLS LOG
M
8.3.3.6
05h
MANAGE OVERRIDE LOCKOUT TIMER
M
8.3.3.7
06h
OVERRIDE MGMT ID KEY
M
8.3.3.8
07h
REVOKE PROXY TOKEN
O
8.3.3.9
08h
REVOKE ALL PROXY TOKENS
O
8.3.3.10
09h
ASSIGN PROXY LUN
O
8.3.3.11
0Ah
RELEASE PROXY LUN
O
8.3.3.12
0Bh to 17h
Reserved
18h to 1Fh
Vendor specific
Key: M = Service action implementation is mandatory if ACCESS CONTROL OUT is
implemented.
O = Service action implementation is optional.


The ACCESS CONTROL OUT command may be addressed to any logical unit whose standard INQUIRY
data (see 6.6.2) has the ACC bit set to one (e.g., LUN 0), in which case it shall be processed in the same
manner as if the command had been addressed to the ACCESS CONTROLS well known logical unit. If an
ACCESS CONTROL OUT command is received by a device server whose standard INQUIRY data has the
ACC bit set to zero, the command shall be terminated with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
If an ACCESS CONTROL OUT command is received while an IKEv2-SCSI CCS is in progress (see 5.14.4),
the command shall be terminated with CHECK CONDITION status, with the sense key NOT READY, and the
additional sense code set to LOGICAL UNIT NOT READY, SA CREATION IN PROGRESS. The sense key
specific additional sense data may be set as described in 5.14.5.
The CDB format used by all ACCESS CONTROL OUT service actions is shown in table 697.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 697 for the ACCESS
CONTROL OUT command.
The SERVICE ACTION field is defined in 4.2.5.2 and table 696.
The PARAMETER LIST LENGTH field indicates the amount of data being sent to the access controls coordinator in
the Data-Out Buffer. The format of the parameter list is specific to each service action.
The CONTROL byte is defined in SAM-5.
8.3.3.2 MANAGE ACL service action
8.3.3.2.1 MANAGE ACL introduction
The ACCESS CONTROL OUT command with MANAGE ACL service action is used to authorize access or
revoke access to a logical unit or logical units by initiator ports. The ACCESS CONTROL OUT command with
MANAGE ACL service action adds, changes or removes an entry or multiple entries in the access controls
coordinator’s ACL (see 8.3.1.3). If the ACCESS CONTROL OUT command is implemented, the MANAGE
ACL service action shall be implemented.
The format of the CDB for the ACCESS CONTROL OUT command with MANAGE ACL service action is
shown in table 697 (see 8.3.3.1).
Table 697 — ACCESS CONTROL OUT command format
Bit
Byte
OPERATION CODE (87h)
Reserved
SERVICE ACTION (see table 696)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


If the PARAMETER LIST LENGTH field in the CDB is set to zero, the access controls coordinator shall take no
action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is less than 20 or results in truncation of any ACE page (see
table 699), then the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
If the access controls coordinator is unable to complete the ACCESS CONTROL OUT command with
MANAGE ACL service action because it has insufficient resources, then the access controls coordinator shall
take no action and not change any of its state and the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INSUFFICIENT ACCESS CONTROL RESOURCES.
The format of the parameter data for the ACCESS CONTROL OUT command with MANAGE ACL service
action is shown in table 698.
Table 698 — ACCESS CONTROL OUT with MANAGE ACL parameter data format
Bit
Byte
Parameter list header
Reserved
•••
(MSB)
MANAGEMENT IDENTIFIER KEY
•••
(LSB)
(MSB)
NEW MANAGEMENT IDENTIFIER KEY
•••
(LSB)
Reserved
FLUSH
Reserved
Reserved
Reserved
(MSB)
DLGENERATION
•••
(LSB)
ACE pages
ACE page 0
•••
•••
ACE page x
•••
n


If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then the
access controls coordinator’s state shall not be altered, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
ACCESS DENIED - INVALID MGMT ID KEY. This event shall be recorded in the invalid keys portion of the
access controls log (see 8.3.1.10).
If the contents of the MANAGEMENT IDENTIFIER KEY field match the current management identifier key
maintained by the access controls coordinator, the access controls coordinator shall set its management
identifier key to the value specified in the NEW MANAGEMENT IDENTIFIER KEY field and if access controls are
disabled it shall enable them.
The FLUSH bit set to one instructs the access controls coordinator to place every initiator port in the enrolled
state into the pending-enrolled state (see 8.3.1.5.1.4).
The DLGENERATION field specifies the DLgeneration value (see 8.3.1.4.4) associated with the default LUN
values in the Grant/Revoke ACE pages in the parameter data.
The ACE pages that may follow the parameter list header provide additional changes to the ACL. Each ACE
page describes one ACE in the ACL that is to be added, modified, or removed. The content and format of an
ACE page is indicated by a page code (see table 699).
The following requirements apply to the processing of changes to the access control state:
a)
no change to the access control state shall occur if the ACCESS CONTROL OUT command with
MANAGE ACL service action completes with a status other than GOOD status; and
b)
if the ACCESS CONTROL OUT command with MANAGE ACL service action completes with GOOD
status, the following shall have been performed as a single indivisible event:
1)
changes resulting from the contents of fields in the parameter list header shall be processed; and
2)
changes resulting from the contents of ACE pages shall be processed;
a)
multiple ACE pages shall be processed sequentially;
b)
if an ACE page contains conflicting instructions in LUACD descriptors, the instructions in the
last LUACD descriptor within the ACE page shall take precedence; and
c)
if an ACE containing an AccessID type access identifier (see 8.3.1.3.2) is replaced and the
ACE page that caused the change has the NOCNCL bit (see 8.3.3.2.2) set to zero, then any
initiator port in the enrolled state or pending-enrolled state under the AccessID in that ACE
shall be placed in the not-enrolled state (see 8.3.1.5.1.2).
An ACE page contains conflicting instructions if either of the following is true:
a)
two LUACD descriptors are present with the same LUN value and different default LUN values; or
b)
two LUACD descriptors are present with different LUN values and the same default LUN value.
Table 699 — ACE page codes
Page Code
ACE Page Name
Reference
00h
Grant/Revoke
8.3.3.2.2
01h
Grant All
8.3.3.2.3
02h
Revoke Proxy Token
8.3.3.2.4
03h
Revoke All Proxy Tokens
8.3.3.2.5
04h to EFh
Reserved
F0h to FFh
Vendor specific


8.3.3.2.2 The Grant/Revoke ACE page
The Grant/Revoke ACE page (see table 700) is used to add, modify, or remove an ACE from the ACL (see
8.3.1.3).
The PAGE LENGTH field specifies the number of additional bytes present in this ACE page.
A no changes to current logical unit access (NOCNCL) bit set to one specifies that the application client is telling
the access controls coordinator that this ACE page makes no changes to the existing logical unit access
conditions in the ACL. A NOCNCL bit set to zero specifies that the ACE page may or may not change existing
logical unit access conditions. If the ACCESS IDENTIFIER TYPE specifies a TransportID (see 8.3.2.2.2.2), the
NOCNCL bit shall be ignored.
The ACCESS IDENTIFIER TYPE and ACCESS IDENTIFIER LENGTH fields are described in 8.3.2.2.2.2.
The ACCESS IDENTIFIER field contains the identifier that the access controls coordinator uses to select the ACE
that is to be added, modified, or removed. The format of the ACCESS IDENTIFIER field is defined in table 669
(see 8.3.1.13).
Table 700 — Grant/Revoke ACE page format
Bit
Byte
PAGE CODE (00h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
NOCNCL
Reserved
ACCESS IDENTIFIER TYPE
(MSB)
ACCESS IDENTIFIER LENGTH (m-7)
(LSB)
ACCESS IDENTIFIER
•••
m
LUACD descriptors
m+1
LUACD descriptor 0
•••
m+20
•••
n-19
LUACD descriptor x
•••
n


Any of the following conditions in the parameter header or any Grant/Revoke ACE page or Grant All ACE
page shall cause the access coordinator to not change its state and shall cause the command to be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST:
a)
the value in the DLGENERATION field in the parameter list header (see 8.3.3.2.1) does not match the
current value of the DLgeneration counter (see 8.3.1.4.4) maintained by the access controls coordi-
nator;
b)
an ACCESS IDENTIFIER TYPE field specifies an unsupported value;
c)
an ACCESS IDENTIFIER TYPE field contains 01h (see 8.3.1.3.2) with an ACCESS IDENTIFIER field that
contains an invalid TransportID (see 8.3.1.3.2) as defined for the applicable protocol standard;
d)
two ACE pages that have the same values in the ACCESS IDENTIFIER TYPE and ACCESS IDENTIFIER
fields; or
e)
changes in the ACL that result in an ACL LUN conflict (see 8.3.1.5.2).
NOTE 80 - The application client is responsible for obtaining the current association of default LUN values to
logical units and the DLgeneration value for that association prior to issuing this service action. The ACCESS
CONTROL IN command with REPORT LU DESCRIPTORS service action (see 8.3.2.3) returns the
necessary information.
Each LUACD descriptor (see table 701) describes the access to be allowed to one logical unit based on the
access identifier in the ACE page. An ACE page may contain zero or more LUACD descriptors.
The ACCESS MODE field is described in 8.3.2.2.2.2.
The LUN VALUE field specifies the LUN value an accessing application client uses to access the logical unit via
the initiator port to which the LUACD descriptor applies.
The DEFAULT LUN field specifies the logical unit to which the value in the LUN VALUE allows access. The
DEFAULT LUN field shall contain a default LUN value (see 8.3.1.4.3). The value in the DEFAULT LUN field shall be
consistent with the DLGENERATION field value specified in the parameter list header (see 8.3.3.2.1). If the
DEFAULT LUN field references a well known logical unit, the access controls coordinator’s state shall not be
modified and the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
Table 701 — ACE page LUACD descriptor format
Bit
Byte
ACCESS MODE
Reserved
LUN VALUE
•••
DEFAULT LUN
•••


If the specified access mode is not supported or if the DEFAULT LUN field contains value that is not valid or the
LUN VALUE field contains a value that the access controls coordinator does not support as a valid LUN, then
the access controls coordinator’s state shall not be modified and the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, the additional sense code set to
ACCESS DENIED - INVALID LU IDENTIFIER, and the SENSE-KEY SPECIFIC field shall be set as described for
the ILLEGAL REQUEST sense key in 4.5.2.4.2. If the error is an unsupported value in the LUN VALUE field,
then the access controls coordinator should determine a suggested LUN value that is unlikely to produce an
error while also minimizing the absolute value of the difference of the erroneous default LUN value and the
suggested LUN value. If a suggested LUN value is determined, the first four bytes of the suggested LUN value
shall be placed in the INFORMATION field and the last four bytes shall be placed in the COMMAND-SPECIFIC
INFORMATION field of the sense data (see 4.5).
Based on the access identifier and the presence or absence of LUACD descriptors, the access controls
coordinator shall add, modify, or remove an ACE in the ACL as shown in table 702.
If the ACCESS IDENTIFIER TYPE indicates type AccessID, the enrollment state (see 8.3.1.5.1) of any initiator port
that is enrolled under the specified AccessID, shall be affected as follows:
a)
if the ACE containing the AccessID is removed, the initiator port shall be placed in the not-enrolled
state; or
b)
if the ACE containing the AccessID is modified by a Grant/Revoke ACE page or a Grant All ACE
page, then;
A)
if the NOCNCL bit is set to zero in that ACE page, the initiator port shall be placed in the
not-enrolled state; or
B)
if the NOCNCL bit is set to one in that ACE page, the enrollment state of the initiator port may be left
unchanged or the initiator port may be placed in the not-enrolled state (see 8.3.1.5.1.2) based on
vendor specific considerations.
Table 702 — Access Coordinator Grant/Revoke ACE page actions
ACL already contains an ACE with the access
identifier matching the one in the ACE page?
Yes
No
ACE page
includes
LUCAD
descriptors?
Yes
Modify the existing ACE in
the ACL.
Add a new ACE to the
ACL.
No
Remove the existing ACE
from the ACL.
Take no action; this shall
not be considered an
error.


8.3.3.2.3 The Grant All ACE page
The Grant All ACE page (see table 703) is used to add or modify an ACE in the ACL (see 8.3.1.3). An ACE
added or modified using the Grant All ACE page allows initiator ports with the specified access identifier to
access the SCSI target device as if access controls were disabled.
The PAGE LENGTH, NOCNCL, ACCESS IDENTIFIER TYPE, ACCESS IDENTIFIER LENGTH, and ACCESS IDENTIFIER fields
are defined in 8.3.3.2.2.
The Grant All ACE page shall be processed as if it is a Grant/Revoke ACE page (see 8.3.3.2.2) with one
LUACD descriptor for every logical unit managed by the access controls coordinator with the fields in each
LUACD containing:
a)
an access mode of 00h (see 8.3.2.2.2.2);
b)
a LUN VALUE field whose contents match the contents of the DEFAULT LUN field; and
c)
a DEFAULT LUN field whose contents reference the logical unit appropriate to the DLgeneration value
(see 8.3.1.4.4).
Table 703 — Grant All ACE page format
Bit
Byte
PAGE CODE (01h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
NOCNCL
Reserved
ACCESS IDENTIFIER TYPE
(MSB)
ACCESS IDENTIFIER LENGTH (m-7)
(LSB)
ACCESS IDENTIFIER
•••
n


8.3.3.2.4 The Revoke Proxy Token ACE page
The Revoke Proxy Token ACE page (see table 704) is used to revoke one or more proxy tokens (see
8.3.1.6.2).
The PAGE LENGTH field specifies the number of additional bytes present in this ACE page. If the page length is
less than eight or not a multiple of eight, the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense be set to PARAMETER LIST
LENGTH ERROR.
The PROXY TOKEN field(s) specify the proxy tokens to be revoked. The access controls coordinator shall
revoke each proxy token listed in a PROXY TOKEN field. If the contents of a PROXY TOKEN field do not identify a
valid proxy token the field shall be ignored and this shall not be considered an error.
Multiple Revoke Proxy Token ACE pages may be included in the parameter data.
8.3.3.2.5 The Revoke All Proxy Tokens ACE page
The Revoke All Proxy Tokens ACE page (see table 705) is used to revoke all currently valid proxy tokens (see
8.3.1.6.2).
Multiple Revoke All Proxy Tokens ACE pages may be included in the parameter data.
Table 704 — Revoke Proxy Token ACE page format
Bit
Byte
PAGE CODE (02h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
PROXY TOKEN 0
•••
•••
n-7
PROXY TOKEN x
•••
n
Table 705 — Revoke All Proxy Tokens ACE page format
Bit
Byte
PAGE CODE (03h)
Reserved
(MSB)
PAGE LENGTH (0000h)
(LSB)


8.3.3.3 DISABLE ACCESS CONTROLS service action
The ACCESS CONTROL OUT command with DISABLE ACCESS CONTROLS service action is used to
place the access controls coordinator in the access controls disabled state. If the ACCESS CONTROL OUT
command is implemented, the DISABLE ACCESS CONTROLS service action shall be implemented.
The format of the CDB for the ACCESS CONTROL OUT command with DISABLE ACCESS CONTROLS
service action is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is neither zero nor 12, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is 12, the parameter list shall have the format shown in table
706.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then the
access controls coordinator’s states shall not be altered, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
ACCESS DENIED - INVALID MGMT ID KEY. This event shall be recorded in the invalid keys portion of the
access controls log (see 8.3.1.10).
In response to an ACCESS CONTROL OUT command with DISABLE ACCESS CONTROLS service action
with correct management identifier key value the access controls coordinator shall:
a)
disable access controls;
b)
clear the ACL (see 8.3.1.3);
c)
place all initiator ports into the not-enrolled state (see 8.3.1.5.1);
d)
set the management identifier key to zero (see 8.3.1.8);
e)
set the override lockout timer to zero (see 8.3.1.8.2.2);
f)
set the initial override lockout timer value to zero (see 8.3.1.8.2.2);
g)
clear the access controls log, including resetting the events counters to zero, with the exception of the
key overrides portion of the access controls log (see 8.3.1.10);
h)
allow all initiator port’s access to all logical units at their default LUN value;
i)
optionally, set the DLgeneration counter to zero (see 8.3.1.4.4); and
Table 706 — ACCESS CONTROL OUT with DISABLE ACCESS CONTROLS parameter data format
Bit
Byte
Reserved
•••
(MSB)
MANAGEMENT IDENTIFIER KEY
•••
(LSB)


j)
establish a unit attention condition for the initiator port associated with every I_T nexus in each logical
unit in the SCSI target device, with the additional sense code set to REPORTED LUNS DATA HAS
CHANGED.
8.3.3.4 ACCESS ID ENROLL service action
The ACCESS ID ENROLL service action of the ACCESS CONTROL OUT command is used by an application
client to enroll an AccessID for an initiator port with the access controls coordinator. If the ACCESS
CONTROL OUT command is implemented, the ACCESS ID ENROLL service action shall be implemented.
The format of the CDB for the ACCESS CONTROL OUT command with ACCESS ID ENROLL service action
is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is neither zero nor 24, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is 24, the parameter list shall have the format shown in table
707.
The ACCESSID field is described in 8.3.1.3.2.
If the initiator port is in the enrolled state or pending-enrolled state (see 8.3.1.5.1) under a specific AccessID
and the ACCESSID field contains a different AccessID, then the access controls coordinator shall place the
initiator port in the pending-enrolled state, the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED -
ENROLLMENT CONFLICT.
If the initiator port is in the enrolled state or pending-enrolled state under a specific AccessID and the
ACCESSID field contains a matching AccessID, the access controls coordinator shall place the initiator port in
the enrolled state and make no other changes.
If the initiator port is in the not-enrolled state and the ACCESSID field contents do not match the AccessID in
any ACE in the ACL (see 8.3.1.3), then the initiator port shall remain in the not-enrolled state and the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to ACCESS DENIED - NO ACCESS RIGHTS.
Table 707 — ACCESS CONTROL OUT with ACCESS ID ENROLL parameter data format
Bit
Byte
ACCESSID
•••
Reserved
•••


If the initiator port is in the not-enrolled state and the ACCESSID field contents matches the AccessID in an
ACE in the ACL, the actions taken depend on whether enrolling the initiator port would create an ACL LUN
conflict (see 8.3.1.5.2). If there is no ACL LUN conflict, the initiator port shall be placed in the enrolled state
(see 8.3.1.5.1.3). If there is an ACL LUN conflict, then the initiator port shall remain in the not-enrolled state
and the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to ACCESS DENIED - ACL LUN CONFLICT. This event shall
be recorded in the ACL LUN conflicts portion of the access controls log (see 8.3.1.10).
An application client that receives the ACCESS DENIED - ACL LUN CONFLICT additional sense code should
remove any proxy access rights it has acquired using the ACCESS CONTROL OUT command with
RELEASE PROXY LUN service action and retry the enrollment request. If the ACL LUN conflict resulted from
proxy access, the retried enrollment succeeds. Otherwise, the mechanisms for resolving ACL LUN conflicts
are outside the scope of this standard.
8.3.3.5 CANCEL ENROLLMENT service action
The ACCESS CONTROL OUT command with CANCEL ENROLLMENT service action is used to remove an
initiator port’s enrollment with the access controls coordinator (see 8.3.1.5). Successful completion of this
command changes the state of the initiator port to the not-enrolled state. If the ACCESS CONTROL OUT
command is implemented, the CANCEL ENROLLMENT service action shall be implemented.
The ACCESS CONTROL OUT command with CANCEL ENROLLMENT service action should be used by an
application client prior to any period where use of its accessible logical units may be suspended for a lengthy
period of time (e.g., when a host is preparing to shutdown). This allows the access controls coordinator to free
any resources allocated to manage the enrollment for the initiator port.
The format of the CDB for the ACCESS CONTROL OUT command with CANCEL ENROLLMENT service
action is shown in table 697 (see 8.3.3.1).
If access controls are disabled, the access controls coordinator shall take no action and the command shall be
completed with GOOD status.
There is no parameter data for the ACCESS CONTROL OUT command with CANCEL ENROLLMENT
service action. If the PARAMETER LIST LENGTH field in the CDB is not set to zero, the initiator port’s enrollment
shall not be changed and the command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
If the PARAMETER LIST LENGTH field in the CDB is set to zero, the initiator port shall be placed in the not-enrolled
state (see 8.3.1.5.1.2) Any subsequent commands addressed to the logical units no longer accessible are
handled according to the requirements stated in 8.3.1.7.
8.3.3.6 CLEAR ACCESS CONTROLS LOG service action
The ACCESS CONTROL OUT command with CLEAR ACCESS CONTROLS LOG service action is used to
instruct the access controls coordinator to reset a specific access control events counter to zero and to clear a
portion of the access controls log (see 8.3.1.10). If the ACCESS CONTROL OUT command is implemented,
the CLEAR ACCESS CONTROLS LOG service action shall be implemented.
The format of the CDB for the ACCESS CONTROL OUT command with CLEAR ACCESS CONTROLS LOG
service action is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.


If the value in the PARAMETER LIST LENGTH field is neither zero nor 12, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is 12, the parameter list shall have the format shown in table
708.
The LOG PORTION field (see table 709) specifies the access controls log portion to be cleared.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then the
access controls coordinator’s states shall not be altered, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
ACCESS DENIED - INVALID MGMT ID KEY. This event shall be recorded in the invalid keys portion of the
access controls log (see 8.3.1.10).
In response to an ACCESS CONTROL OUT command with CLEAR ACCESS CONTROLS LOG service
action with correct management identifier key value the access controls coordinator shall perform the
following to clear the portion of the access controls log identified by the LOG PORTION field (see table 709) in
the parameter data:
a)
set the events counter for the specified log portion to zero; and
b)
if the specified log portion contains log records, remove the log records from the specified log portion.
8.3.3.7 MANAGE OVERRIDE LOCKOUT TIMER service action
The ACCESS CONTROL OUT command with MANAGE OVERRIDE LOCKOUT TIMER service action is
used to manage the override lockout timer (see 8.3.1.8.2.2). If the ACCESS CONTROL OUT command is
implemented, the MANAGE OVERRIDE LOCKOUT TIMER service action shall be implemented.
Table 708 — ACCESS CONTROL OUT with CLEAR ACCESS CONTROLS LOG parameter data format
Bit
Byte
Reserved
Reserved
LOG PORTION
(MSB)
MANAGEMENT IDENTIFIER KEY
•••
(LSB)
Table 709 — CLEAR ACCESS CONTROLS LOG LOG PORTION field
Code
Description
00b
Reserved
01b
Invalid Keys portion
10b
ACL LUN Conflicts portion
11b
Reserved


If access controls are disabled, the access controls coordinator shall take no action and the command shall be
completed with GOOD status.
The format of the CDB for the ACCESS CONTROL OUT command with MANAGE OVERRIDE LOCKOUT
TIMER service action is shown in table 697 (see 8.3.3.1).
If the PARAMETER LIST LENGTH field in the CDB is set to zero, the access controls coordinator shall reset the
override lockout timer to the current initial override lockout timer value maintained by the access controls
coordinator.
If the value in the PARAMETER LIST LENGTH field is neither zero nor 12, the device server shall respond with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is 12, the parameter list shall have the format shown in table
710.
The NEW INITIAL OVERRIDE LOCKOUT TIMER field specifies the value that access controls coordinator shall
maintain for initial override lockout timer if the specified management identifier key is correct.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then the
access controls coordinator shall not change the initial override lockout timer value but shall set the override
lockout timer to the unaltered current initial override lockout timer value. The command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to ACCESS DENIED - INVALID MGMT ID KEY. This event shall be recorded in the invalid keys
portion of the access controls log (see 8.3.1.10).
In response to an ACCESS CONTROL OUT command with MANAGE OVERRIDE LOCKOUT TIMER service
action with correct management identifier key value the access controls coordinator shall:
a)
replace the currently saved initial override lockout timer with the value in the NEW INITIAL OVERRIDE
LOCKOUT TIMER field; and
b)
set the override lockout timer to the new initial value.
Table 710 — ACCESS CONTROL OUT command MANAGE OVERRIDE LOCKOUT TIMER service
action parameter data format
Bit
Byte
Reserved
(MSB)
NEW INITIAL OVERRIDE LOCKOUT TIMER
(LSB)
(MSB)
MANAGEMENT IDENTIFIER KEY
•••
(LSB)


8.3.3.8 OVERRIDE MGMT ID KEY service action
The ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action is used to override
the current management identifier key (see 8.3.1.4.2) maintained by the access controls coordinator. The
ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action should be used in a
failure situation where the application client no longer has access to its copy of the current management
identifier key.
Successful use of the ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action is
constrained by the override lockout timer (see 8.3.1.8.2.2).
If the ACCESS CONTROL OUT command is implemented, the OVERRIDE MGMT ID KEY service action
shall be implemented.
The format of the CDB for the ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service
action is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.
If access controls are enabled, the access controls coordinator shall log every ACCESS CONTROL OUT
command with OVERRIDE MGMT ID KEY service action processed whether successful or not in the access
controls log as defined in 8.3.1.10.
If the value in the PARAMETER LIST LENGTH field is neither zero nor 12, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is 12, the parameter data shall have the format shown in table
711.
The NEW MANAGEMENT IDENTIFIER KEY field specifies a new management identifier key.
If the override lockout timer managed by the access controls coordinator is not zero, the access controls
coordinator’s states shall not be altered, the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
If the override lockout timer managed by the access controls coordinator is zero, then the access controls
coordinator shall replace the current management identifier key with the value in the to the NEW MANAGEMENT
IDENTIFIER KEY field.
Table 711 — ACCESS CONTROL OUT with OVERRIDE MGMT ID KEY parameter data format
Bit
Byte
Reserved
•••
(MSB)
NEW MANAGEMENT IDENTIFIER KEY
•••
(LSB)


8.3.3.9 REVOKE PROXY TOKEN service action
 An application client for an initiator port uses the ACCESS CONTROL OUT command with REVOKE PROXY
TOKEN service action to cancel all proxy access rights to a logical unit that have been granted under the
specified proxy token (see 8.3.1.6.2). If this service action is not supported, the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN CDB.
The format of the CDB for the ACCESS CONTROL OUT command with REVOKE PROXY TOKEN service
action is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is neither zero nor eight, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is eight, the parameter data shall have the format shown in
table 712.
If the PROXY TOKEN field does not contain a valid proxy token previously obtained via the initiator port, no
action is taken by the access controls coordinator. This shall not be considered an error.
If the proxy token is valid, the access controls coordinator shall take the following actions:
a)
invalidate the proxy token; and
b)
deny access to the associated logical unit by any initiator port whose rights were granted under that
proxy token via an ACCESS CONTROL OUT command with ASSIGN PROXY LUN service action
(see 8.3.3.11) according to the requirements stated in 8.3.1.7.
8.3.3.10 REVOKE ALL PROXY TOKENS service action
An application client for an initiator port uses the ACCESS CONTROL OUT command with REVOKE ALL
PROXY TOKENS service action to cancel all proxy access rights to a specified logical unit that it obtained with
zero or more proxy tokens (see 8.3.1.6.2). If this service action is not supported, the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
The format of the CDB for the ACCESS CONTROL OUT command with REVOKE ALL PROXY TOKENS
service action is shown in table 697 (see 8.3.3.1).
If access controls are disabled or if the PARAMETER LIST LENGTH field in the CDB is set to zero, the access
controls coordinator shall take no action and the command shall be completed with GOOD status.
Table 712 — ACCESS CONTROL OUT with REVOKE PROXY TOKEN parameter data format
Bit
Byte
PROXY TOKEN
•••


If the value in the PARAMETER LIST LENGTH field is neither zero nor eight, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is eight, the parameter data shall have the format shown in
table 713.
If the LUN in the LUN VALUE field is not associated to a logical unit to which the requesting initiator port has
non-proxy access rights based on the contents of an ACE (see 8.3.1.3) or if the LUN value is based on a
proxy token (see 8.3.1.6.2), then no further action is taken by the access controls coordinator. This shall not
be considered an error.
If the LUN value is associated to a logical unit to which the requesting initiator port has non-proxy access
rights, the access controls coordinator shall take the following additional actions:
a)
invalidate all proxy tokens for the initiator port for the logical unit specified by the LUN VALUE field;
b)
deny access to that logical unit by any initiator port whose rights were granted under any of the invali-
dated proxy tokens via an ACCESS CONTROL OUT command with ASSIGN PROXY LUN service
action (see 8.3.3.11) according to the requirements stated in 8.3.1.7.
8.3.3.11 ASSIGN PROXY LUN service action
The ACCESS CONTROL OUT command with ASSIGN PROXY LUN service action is used to request access
to a logical unit under the rights of a proxy token (see 8.3.1.6.2) and to assign that logical unit a particular LUN
value for addressing by the requesting initiator port. If this service action is not supported, the command shall
be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
The format of the CDB for the ACCESS CONTROL OUT command with ASSIGN PROXY LUN service action
is shown in table 697 (see 8.3.3.1).
If the PARAMETER LIST LENGTH field in the CDB is set to zero, the access controls coordinator shall take no
action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is neither zero nor 16, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
Table 713 — ACCESS CONTROL OUT with REVOKE ALL PROXY TOKENS parameter data format
Bit
Byte
LUN VALUE
•••


If the value in the PARAMETER LIST LENGTH field is 16, the parameter data shall have the format shown in table
714.
The PROXY TOKEN field contains a proxy token. If the contents of the PROXY TOKEN field are not valid, then the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to ACCESS DENIED - INVALID PROXY TOKEN.
NOTE 81 - If access controls are disabled, there are no valid proxy tokens and the device server always
responds with the specified error information. This differs from the behavior of many other ACCESS
CONTROL OUT service actions where the response is GOOD status while access controls are disabled. The
difference in behavior is intended to inform the application client that its request for the new LUN assignment
failed.
The LUN VALUE field specifies the LUN value the application client intends to use while accessing the logical
unit described by the proxy token.
If the proxy token is valid but the access controls coordinator is unable to assign the requested LUN value to
the associated logical unit (e.g., because the LUN value already is associated with a logical unit for the
initiator port, or because the LUN value is not a supported logical unit address), then access rights shall not be
granted, the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED - INVALID LU IDENTIFIER, and
the SENSE-KEY SPECIFIC field shall be set as described for the ILLEGAL REQUEST sense key in 4.5.2.4.2. The
access controls coordinator should determine a suggested LUN value that is unlikely to produce an error while
also minimizing the absolute value of the difference of the erroneous default LUN value and the suggested
LUN value. If a suggested LUN value is determined, the first four bytes of the suggested LUN value shall be
placed in the INFORMATION field and the last four bytes shall be placed in the COMMAND-SPECIFIC INFORMATION
field of the sense data (see 4.5).
If the proxy token is valid but the access controls coordinator has insufficient resources to manage proxy
logical unit access, the command shall be terminated with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INSUFFICIENT ACCESS CONTROL
RESOURCES.
If the proxy token is valid and the access controls coordinator has sufficient resources, the initiator port shall
be allowed proxy access to the referenced logical unit at the specified LUN value.
Table 714 — ACCESS CONTROL OUT with ASSIGN PROXY LUN parameter data format
Bit
Byte
PROXY TOKEN
•••
LUN VALUE
•••


8.3.3.12 RELEASE PROXY LUN service action
The ACCESS CONTROL OUT command with RELEASE PROXY LUN service action is used to release proxy
access to a logical unit created with a proxy token (see 8.3.1.6.2) and the ACCESS CONTROL OUT
command with ASSIGN PROXY LUN service action (see 8.3.3.11). If this service action is not supported, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The ACCESS CONTROL OUT command with RELEASE PROXY LUN service action should be used if an
application client no longer requires the logical unit access rights granted to an initiator port under a proxy
token (e.g., when a copy manager has completed a specific third party copy operation under a proxy token).
This allows the access controls coordinator to free any resources allocated to manage the proxy access.
The format of the CDB for the ACCESS CONTROL OUT command with RELEASE PROXY LUN service
action is shown in table 697 (see 8.3.3.1).
If the PARAMETER LIST LENGTH field in the CDB is set to zero, the access controls coordinator shall take no
action and the command shall be completed with GOOD status.
If the value in the PARAMETER LIST LENGTH field is neither zero nor eight, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to PARAMETER LIST LENGTH ERROR.
If the value in the PARAMETER LIST LENGTH field is eight, the parameter data shall have the format shown in
table 715.
The LUN VALUE field specifies a LUN value that was associated with a logical unit based on a proxy token
using an ACCESS CONTROL OUT command with ASSIGN PROXY LUN service action. If the LUN value
was not assigned to a logical unit by an ACCESS CONTROL OUT command with ASSIGN PROXY LUN
service action, the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
NOTE 82 - If access controls are disabled, there are no valid proxy tokens and therefore no LUN value could
be assigned to a logical unit by an ACCESS CONTROL OUT command with ASSIGN PROXY LUN service
action so the device server always responds with the specified error information. This differs from the
behavior of many other ACCESS CONTROL OUT service actions where the response is GOOD status while
access controls are disabled. The difference in behavior is intended to inform the application client that the
LUN value remains as a valid address for the logical unit.
If the LUN value was assigned to a logical unit by an ACCESS CONTROL OUT command with ASSIGN
PROXY LUN service action, the access controls coordinator shall not allow access to the logical unit at the
specified LUN value.
Table 715 — ACCESS CONTROL OUT with RELEASE PROXY LUN parameter data format
Bit
Byte
LUN VALUE
•••


8.4 TARGET LOG PAGES well known logical unit
The TARGET LOG PAGES well known logical unit shall only process the commands listed in table 716. If a
command is received by the TARGET LOG PAGES well know logical unit that is not listed in table 716, then
the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
The TARGET LOG PAGES well known logical unit shall support the Protocol Specific Port log page (see
7.3.13) and may support other log pages with parameters that apply to the SCSI target device.
8.5 SECURITY PROTOCOL well known logical unit
The SECURITY PROTOCOL well known logical unit shall only process the commands listed in table 717. If a
command is received by the SECURITY PROTOCOL well known logical unit that is not listed in table 717,
then the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
Table 716 — Commands for the TARGET LOG PAGES well known logical unit
Command
Operation
code
Type
Reference
INQUIRY
12h
M
6.6
LOG SELECT
4Ch
M
6.7
LOG SENSE
4Dh
M
6.8
REQUEST SENSE
03h
M
6.39
TEST UNIT READY
00h
M
6.43
Key: M = Command implementation is mandatory.
Table 717 — Commands for the SECURITY PROTOCOL well known logical unit
Command
Operation
code
Type
Reference
INQUIRY
12h
M
6.6
REQUEST SENSE
03h
M
6.39
SECURITY PROTOCOL IN
A2h
M
6.40
SECURITY PROTOCOL OUT
B5h
M
6.41
TEST UNIT READY
00h
M
6.47
Key: M = Command implementation is mandatory.


8.6 MANAGEMENT PROTOCOL well known logical unit
The MANAGEMENT PROTOCOL well known logical unit shall only process the commands listed in table 718.
If a command is received by the MANAGEMENT PROTOCOL well known logical unit that is not listed in table
718, then the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
Table 718 — Commands for the MANAGEMENT PROTOCOL well known logical unit
Command
Operation
code
Type
Reference
INQUIRY
12h
M
6.6
MANAGEMENT PROTOCOL IN
A3h/10h a
M
6.9
MANAGEMENT PROTOCOL OUT
A4h/10h a
M
6.10
REQUEST SENSE
03h
M
6.39
TEST UNIT READY
00h
M
6.47
Key: M = Command implementation is mandatory.
a This command is defined by a combination of operation code and service action. The
operation code value is shown preceding the slash and the service action value is shown
after the slash.


9 Security manager command set
A security manager shall only process the commands listed in table 719. If a command is received by the
security manager that is not listed in table 719, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID COMMAND OPERATION CODE.
Table 719 — Commands for a security manager
Command
Operation
code
Type
Reference
INQUIRY
12h
M
6.6
RECEIVE CREDENTIAL
7Fh/1800 a
M
6.27
REPORT LUNS
A0h
M
6.33
REQUEST SENSE
03h
M
6.39
SECURITY PROTOCOL IN
A2h
M
6.40
SECURITY PROTOCOL OUT
B5h
M
6.41
TEST UNIT READY
00h
M
6.47
Type Key:M = Command implementation is mandatory.
a This command is defined by a combination of operation code and service action. The operation code
value is shown preceding the slash and the service action value is shown after the slash.


Annex A
(informative)
Terminology mapping
Table A.1 lists changes in terminology between SPC-2 and this standard.
Table A.1 — This standard to SPC-2 terminology mapping
Equivalent term in this standard
SPC-2 term
initiator port identifier
initiator identifier
queue
task set
SCSI initiator port
initiator
SCSI port
port
target port identifier or
initiator port identifier
device identifier
target port identifier or
initiator port identifier
SCSI identifier
SCSI target port
target
target port identifier
target identifier


Annex B
(Informative)
Replacing RESERVE/RELEASE functionality with PERSISTENT RESERVE
IN/OUT equivalents
B.1 Introduction
This annex specifies the PERSISTENT RESERVE OUT command features necessary to replace the
reserve/release management method (see SPC-2) and provides guidance on how to perform a third party
reservation using persistent reservations. The PERSISTENT RESERVE IN command is not used to replace
any feature of the reserve/release management method.
B.2 Replacing the reserve/release method with the PERSISTENT RESERVE OUT
COMMAND
The minimum PERSISTENT RESERVE OUT command (see 6.16) features necessary to replace the
reserve/release management method (see SPC-2) are shown in table B.1.
Table B.1 — PERSISTENT RESERVE OUT command features
PERSISTENT RESERVE OUT command features
Replaces
reserve/release
Service
action
REGISTER
Yes b
RESERVE
Yes
RELEASE
Yes
CLEAR
Yes c
PREEMPT
No
PREEMPT AND ABORT
No
REGISTER AND IGNORE EXISTING KEY
Yes b
REGISTER AND MOVE
Yes d
Scope
LU_SCOPE
Yes
Type
Write Exclusive
No
Exclusive Access
Yes
Write Exclusive – Registrants Only
No
Exclusive Access – Registrants Only
No
Write Exclusive – All Registrants
No
Exclusive Access – All Registrants
No
b An implementation uses either the REGISTER service action or REGISTER
AND IGNORE EXISTING KEY service action.
c Necessary to clear the registration and reservation (e.g, a failed initiator).
d Necessary only for third party reservations.


B.3 Third party reservations
For some uses of the EXTENDED COPY(LID4) command (see 6.4) and EXTENDED COPY(LID1) command
(see 6.5), the application client performs a locking function to maintain data integrity on the source and may
also lock the destination device prior to starting the copy operation. The persistent reservation management
method may be used to perform the locking function. Other methods (e.g., access controls, see 8.3) may also
perform the locking function.
To accomplish a third party persistent reservation the following steps are recommended:
1)
backup application uses the REGISTER service action to register an I_T nexus with a logical unit
(e.g., a tape drive logical unit);
2)
backup application uses the RESERVE service action to establish a persistent reservation with the
Exclusive Access type;
3)
backup application prepares the logical unit for access (e.g., medium is loaded and positioned);
4)
backup application uses the REGISTER AND MOVE service action to register the I_T nexus that the
copy manager is expected to use and to move the persistent reservation to that I_T nexus;
5)
backup application sends the EXTENDED COPY command to the copy manager that includes a third
party persistent reservations source I_T nexus segment descriptor (see 6.4.6.18);
6)
copy manager processes all segment descriptors in the received EXTENDED COPY command
except the third party persistent reservations source I_T nexus segment descriptor; and
7)
copy manager issues a REGISTER AND MOVE service action, using the reservation key and I_T
nexus specified in the third party persistent reservations source I_T nexus segment descriptor
received from the backup application (see step 5), to move the persistent reservation back to the
original I_T nexus.


Annex C
(Informative)
Third-party copy implementation and usage
C.1 Embedded and dedicated copy manager implementations
C.1.1 Overview
Although a copy manager is always contained in a logical unit, the logical unit may:
a)
have a function (e.g., providing access to a block storage device) in addition to the copy manager
function (i.e., the copy manager is embedded (see C.1.2) in another device type); or
b)
be dedicated to providing the copy manager function (i.e., the copy manager is contained in a
dedicated (see C.1.3) logical unit).
In both implementations:
a)
the device server processes commands (e.g., INQUIRY) that are not third-party copy commands (see
5.17.3), and the copy manager processes third-party copy commands; and
b)
the standard INQUIRY data (see 6.6.2) indicates a logical unit that is accessible, and has a defined
device type.
C.1.2 Embedded copy manager implementations
The device type indicated by the standard INQUIRY data (see 6.6.2) for an embedded copy manager is the
device type appropriate to the device in which the copy manager is embedded.
In addition to whatever copy manager commands are supported, the commands associated with the device
type (e.g., reads and writes) are supported and processed by the device server.
The copy manager is able to support and translate the FFFFh CSCS descriptor ID value (i.e., this logical unit)
shown in table 131 (see 6.4.5.1) to the logical unit and device type in which the copy manager is embedded.
C.1.3 Dedicated copy manager implementations
The device type indicated by the standard INQUIRY data (see 6.6.2) for a dedicated copy manager is not
constrained by other uses of the logical unit. Any defined device type may be indicated in standard INQUIRY
data. One device type often used by dedicated copy managers is the processor device type (see SPC-2).
Very few commands beyond the commands those that table 118 shows to be mandatory for all device types
(see 6.1) are supported by the logical unit for a dedicated copy manager.
In most cases, a dedicated copy manager is not able to support and translate the FFFFh CSCS descriptor ID
value (i.e., this logical unit) shown in table 131 (see 6.4.5.1).
