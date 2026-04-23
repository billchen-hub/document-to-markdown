# 8.3.2 ACCESS CONTROL IN command

8.3.2 ACCESS CONTROL IN command
8.3.2.1 ACCESS CONTROL IN introduction
The service actions of the ACCESS CONTROL IN command (see table 671) are used to obtain information
about the access controls that are active within the access controls coordinator and to perform other access
control functions (see 8.3.1). If the ACCESS CONTROL IN command is implemented, the ACCESS
CONTROL OUT command also shall be implemented. The ACCESS CONTROL IN command shall not be
affected by access controls.
The ACCESS CONTROL IN command may be addressed to any logical unit whose standard INQUIRY data
(see 6.6.2) has the ACC bit set to one (e.g., LUN 0), in which case it shall be processed in the same manner as
if the command had been addressed to the ACCESS CONTROLS well known logical unit. If an ACCESS
CONTROL IN command is received by a device server whose standard INQUIRY data has the ACC bit set to
zero, the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
Table 671 — ACCESS CONTROL IN service actions
Service
action code
Service action name
Type
Reference
00h
REPORT ACL
M
8.3.2.2
01h
REPORT LU DESCRIPTORS
M
8.3.2.3
02h
REPORT ACCESS CONTROLS LOG
M
8.3.2.4
03h
REPORT OVERRIDE LOCKOUT TIMER
M
8.3.2.5
04h
REQUEST PROXY TOKEN
O
8.3.2.6
05h to 17h
Reserved
18h to 1Fh
Vendor specific
Key: M = Service action implementation is mandatory if ACCESS CONTROL IN is
implemented.
O = Service action implementation is optional.


8.3.2.2 REPORT ACL service action
8.3.2.2.1 REPORT ACL introduction
The ACCESS CONTROL IN command with REPORT ACL service action (see table 672) is used to query the
ACL (see 8.3.1.3) maintained by the access controls coordinator. If the ACCESS CONTROL IN command is
implemented, the REPORT ACL service action shall be implemented.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 672 for the ACCESS
CONTROL IN command with REPORT ACL service action.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 672 for the ACCESS
CONTROL IN command with REPORT ACL service action.
If access controls are disabled, the device server shall ignore the MANAGEMENT IDENTIFIER KEY field and shall
complete the command with GOOD status returning the eight byte parameter list header defined in 8.3.2.2.2
subject to the allocation length limitation described in 4.2.5.6.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then
parameter data shall not be returned and the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED -
INVALID MGMT ID KEY. This event shall be recorded in the invalid keys portion of the access controls log
(see 8.3.1.10).
The ALLOCATION LENGTH field is defined in 4.2.5.6. The ALLOCATION LENGTH field value should be at least eight.
The CONTROL byte is defined in SAM-5.
Table 672 — ACCESS CONTROL IN command with REPORT ACL service action
Bit
Byte
OPERATION CODE (86h)
Reserved
SERVICE ACTION (00h)
(MSB)
MANAGEMENT IDENTIFIER KEY

•••
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


8.3.2.2.2 REPORT ACL parameter data format
8.3.2.2.2.1 REPORT ACL parameter data introduction
The format of the parameter data returned in response to an ACCESS CONTROL IN command with REPORT
ACL service actions is shown in table 673.
The ACL DATA LENGTH field shall contain a count of the number of bytes in the remaining parameter data. If
access controls are disabled, the ACL DATA LENGTH field shall be set to four. The contents of the ACL DATA
LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The DLGENERATION field shall contain the current DLgeneration value (see 8.3.1.4.4).
The ACL data pages contain a description of the ACL (see 8.3.1.3) maintained by the access controls coordi-
nator. Each ACL data page describes one ACE in the ACL or one proxy token (see 8.3.1.6.2). Every ACE and
every proxy token managed by the access controls coordinator shall have an ACL data page in the parameter
data. The content and format of an ACL data page is indicated by a page code. Table 674 lists the ACL data
page codes.
Table 673 — ACCESS CONTROL IN with REPORT ACL parameter data format
Bit
Byte
Parameter list header
(MSB)
ACL DATA LENGTH (n-3)
•••
(LSB)
(MSB)
DLGENERATION
•••
(LSB)
ACL data pages
ACL data page 0
•••
•••
ACL data page x
•••
n
Table 674 — ACL data page codes
Page Code
ACL Data Page Name
Reference
00h
Granted
8.3.2.2.2.2
01h
Granted All
8.3.2.2.2.3
02h
Proxy Tokens
8.3.2.2.2.4
03h to EFh
Reserved
F0h to FFh
Vendor specific


8.3.2.2.2.2 Granted ACL data page format
The Granted ACL data page (see table 675) describes an ACE that allows access to a specific set of logical
units via a list of LUACDs (see 8.3.1.3.3).
The PAGE LENGTH field indicates the number of additional bytes required for this ACL data page. The contents
of the PAGE LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The ACCESS IDENTIFIER TYPE field (see 8.3.1.13) indicates the format and usage of the access identifier.
The ACCESS IDENTIFIER LENGTH field indicates the number of bytes following taken up by the ACCESS IDENTIFIER
field. The access identifier length shall be at least 24 and shall be a multiple of four.
The ACCESS IDENTIFIER field contains the identifier that the access controls coordinator uses to select the
initiator port(s) that are allowed access to the logical units named by the LUACD descriptors in this ACL data
page. The format of the ACCESS IDENTIFIER field is defined in table 669 (see 8.3.1.13). One Granted or Granted
All (see 8.3.2.2.2.3) ACL data page shall be returned for a specific pair of values in the ACCESS IDENTIFIER
TYPE and ACCESS IDENTIFIER fields.
Table 675 — Granted ACL data page format
Bit
Byte
PAGE CODE (00h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
Reserved
ACCESS IDENTIFIER TYPE
(MSB)
ACCESS IDENTIFIER LENGTH (m-7)
(LSB)
ACCESS IDENTIFIER
•••
m
LUACD Descriptors
m+1
LUACD descriptor 0
•••
m+20
•••
n-19
LUACD descriptor x
•••
n


Each LUACD descriptor (see table 676) describes the access allowed to one logical unit based on the access
identifier. There shall be one LUACD descriptor for each logical unit to which the access identifier allows
access.
The ACCESS MODE field (see table 677) indicates the type of access allowed to the logical unit referenced by
the DEFAULT LUN field and addressable at the specified LUN value.
The LUN VALUE field indicates the LUN value an accessing application client uses to access the logical unit via
the initiator port to which the LUACD descriptor applies.
The DEFAULT LUN field identifies the logical unit to which access is allowed using the default LUN value
described in 8.3.1.4.3. The value in the DEFAULT LUN field shall be consistent with the DLGENERATION field
value returned in the parameter list header (see 8.3.2.2.2).
The LUN VALUE and DEFAULT LUN fields may contain the same value.
Table 676 — Granted ACL data page LUACD descriptor format
Bit
Byte
ACCESS MODE
Reserved
LUN VALUE
•••
DEFAULT LUN
•••
Table 677 — ACCESS MODE field
Code
Description
00h
Normal access
01h to EFh
Reserved
F0h to FFh
Vendor specific


8.3.2.2.2.3 Granted All ACL data page format
The Granted All ACL data page (see table 678) describes an ACE that allows access to all the SCSI target
device’s logical units with the default LUN values being used as the accessing LUN values. Initiator ports that
have access via the access identifier in a Granted All ACL data page are allowed to access the SCSI target
device as if access controls were disabled.
The PAGE LENGTH, ACCESS IDENTIFIER TYPE, and ACCESS IDENTIFIER LENGTH, are described in 8.3.2.2.2.2.
The ACCESS IDENTIFIER field contains the identifier that the access controls coordinator uses to select the
initiator port(s) that are allowed access to all the SCSI target device’s logical units with the default LUN values
being used as the accessing LUN values. The format of the access identifier field is defined in table 669 (see
8.3.1.13). One Granted (see 8.3.2.2.2.2) or Granted All ACL data page shall be returned for a specific pair of
values in the ACCESS IDENTIFIER TYPE and ACCESS IDENTIFIER fields.
Table 678 — Granted All ACL data page format
Bit
Byte
PAGE CODE (01h)
Reserved
(MSB)
PAGE LENGTH (m-3)
(LSB)
Reserved
ACCESS IDENTIFIER TYPE
(MSB)
ACCESS IDENTIFIER LENGTH (m-7)
(LSB)
ACCESS IDENTIFIER
•••
m


8.3.2.2.2.4 Proxy Tokens ACL data page format
The Proxy Tokens ACL data page (see table 679) describes the proxy tokens (see 8.3.1.6.2) maintained by
the access controls coordinator.
The PAGE LENGTH field indicates the number of bytes that follow in this ACL data page. The contents of the
PAGE LENGTH field are not altered based on the allocation length (see 4.2.5.6).
If there are no active proxy tokens, the access controls coordinator may either not include the Proxy Tokens
ACL data page in the parameter data or may include one such ACL data page containing no proxy token
descriptors.
No more than one Proxy Tokens ACL data page shall be included in the parameter data.
Table 679 — Proxy Tokens ACL data page format
Bit
Byte
PAGE CODE (02h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
Proxy token descriptors
Proxy token descriptor 0
•••
•••
n-19
Proxy token descriptor x
•••
n


Each proxy token descriptor (see table 680) describes the access allowed to one logical unit based on one
proxy token. There shall be one proxy token descriptor for each active proxy token maintained by the access
controls coordinator.
The PROXY TOKEN field indicates the proxy token to which this proxy token descriptor applies.
The DEFAULT LUN field identifies the logical unit to which this proxy token allows access using the default LUN
value described in 8.3.1.4.3. The value in the DEFAULT LUN field shall be consistent with the DLGENERATION
field value returned in the parameter list header (see 8.3.2.2.2).
The same default LUN value may appear in multiple proxy token descriptors, if multiple proxy tokens are valid
for the same logical unit.
8.3.2.3 REPORT LU DESCRIPTORS service action
8.3.2.3.1 REPORT LU DESCRIPTORS introduction
The ACCESS CONTROL IN command with REPORT LU DESCRIPTORS service action (see table 681)
reports the inventory of logical units for which access controls may be established. If the ACCESS CONTROL
IN command is implemented, the REPORT LU DESCRIPTORS service action shall be implemented.
Table 680 — Proxy token descriptor format
Bit
Byte
Reserved
•••
PROXY TOKEN
•••
DEFAULT LUN
•••
Table 681 — ACCESS CONTROL IN command with REPORT LU DESCRIPTORS service action
Bit
Byte
OPERATION CODE (86h)
Reserved
SERVICE ACTION (01h)
(MSB)
MANAGEMENT IDENTIFIER KEY

•••
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 681 for the ACCESS
CONTROL IN command with REPORT LU DESCRIPTORS service action.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 681 for the ACCESS
CONTROL IN command with REPORT LU DESCRIPTORS service action.
If access controls are disabled, the device server shall ignore the MANAGEMENT IDENTIFIER KEY field and shall
complete the command with GOOD status returning the 20 byte parameter list header as defined in 8.3.2.3.2
subject to the ALLOCATION LENGTH limitation described in 4.2.5.6.
NOTE 77 - While access controls are disabled, the logical unit inventory may be obtained using commands
such as REPORT LUNS (see 6.33). To facilitate access controls management, the ACCESS CONTROL IN
command with REPORT LU DESCRIPTORS service action returns more information than the REPORT
LUNS command. While access controls are disabled additional commands such as INQUIRY (see 6.6) are
required to obtain all the information provided by the ACCESS CONTROL IN command with REPORT LU
DESCRIPTORS service action.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then
parameter data shall not be returned and the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED -
INVALID MGMT ID KEY. This event shall be recorded in the invalid keys portion of the access controls log
(see 8.3.1.10).
The ALLOCATION LENGTH field is defined in 4.2.5.6. The ALLOCATION LENGTH field value should be at least 20.
The CONTROL byte is defined in SAM-5.


8.3.2.3.2 REPORT LU DESCRIPTORS parameter data format
The format of the parameter data returned in response to an ACCESS CONTROL IN command with REPORT
LU DESCRIPTORS service actions is shown in table 682.
The LU INVENTORY LENGTH field shall contain a count of the number of bytes in the remaining parameter data.
If access controls are disabled, the LU INVENTORY LENGTH field shall be set to 16. The contents of the LU
INVENTORY LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The NUMBER OF LOGICAL UNITS field shall contain a count of the number of logical units managed by the access
controls coordinator. The value in NUMBER OF LOGICAL UNITS field shall be the same as the number of Logical
Unit descriptors that follow in the parameter data.
Table 682 — ACCESS CONTROL IN with REPORT LU DESCRIPTORS parameter data format
Bit
Byte
Parameter list header
(MSB)
LU INVENTORY LENGTH (n-3)
•••
(LSB)
(MSB)
NUMBER OF LOGICAL UNITS
•••
(LSB)
SUPPORTED LUN MASK FORMAT
•••
(MSB)
DLGENERATION
•••
(LSB)
Logical Unit descriptor list
Logical Unit descriptor 0
•••
•••
Logical Unit descriptor x
•••
n


The SUPPORTED LUN MASK FORMAT field (see table 683) contains a summary of the LUN values (see 8.3.1.3.3)
that the access controls coordinator supports. LUN values are exchanged between application clients and the
access controls coordinator by several service actions (e.g., the ACCESS CONTROL IN command with
REPORT ACL service action described in 8.3.2.2 and the ACCESS CONTROL OUT command with
MANAGE ACL service action described in 8.3.3.2). The format of the SUPPORTED LUN MASK FORMAT field
follows the eight byte LUN structure defined for dependent logical units by SAM-5.
The LUN MASK at each level indicates the approximate range of the logical unit number values the access
controls coordinator supports. A bit set to zero in a LUN MASK field indicates that the access controls coordi-
nator prohibits setting that bit to one in a LUN value. A bit set to one in a LUN MASK field indicates that the
access controls coordinator may allow setting that bit to one in a LUN value.
(E.g., if the access controls coordinator only supports level one LUN values with LUN values ranging from 0 to
255, then the SUPPORTED LUN MASK FORMAT field shall contain 00FF 0000 0000 0000h. If only LUN values
ranging from 0 to 200 were supported, the SUPPORTED LUN MASK FORMAT field still would contain 00FF 0000
0000 0000h.)
The value in the SUPPORT LUN MASK FORMAT field only summarizes the supported LUN values and is not a
complete description. The value in the SUPPORT LUN MASK FORMAT field should be used as a guideline for
specifying LUN values in service actions (e.g., ACCESS CONTROL OUT command with MANAGE ACL
service action). LUN values that appear valid based on the contents of the SUPPORT LUN MASK FORMAT field
may still be rejected.
The DLGENERATION field shall contain the current DLgeneration value (see 8.3.1.4.4).
Table 683 — SUPPORTED LUN MASK FORMAT field format
Bit
Byte
(MSB)
FIRST LEVEL LUN MASK
(LSB)
(MSB)
SECOND LEVEL LUN MASK
(LSB)
(MSB)
THIRD LEVEL LUN MASK
(LSB)
(MSB)
FOURTH LEVEL LUN MASK
(LSB)


Each Logical Unit descriptor (see table 684) contains information about one logical unit managed by the
access controls coordinator. There shall be one Logical Unit descriptor for every logical unit managed by the
access controls coordinator.
The PERIPHERAL DEVICE TYPE field is as defined in 6.6.2.
The DESCRIPTOR LENGTH field indicates the total number of bytes remaining in the descriptor. If the PERIPHERAL
DEVICE TYPE field contains 0h, 4h, or 7h, the DESCRIPTOR LENGTH field shall contain 92 if the descriptor includes
the DEVICE TYPE SPECIFIC DATA field and 80 if it does not. If the PERIPHERAL DEVICE TYPE field contains any
value other than 0h, 4h, or 7h, the DESCRIPTOR LENGTH field shall contain 76. The contents of the DESCRIPTOR
LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The DEFAULT LUN field contains the default LUN value (see 8.3.1.4.3) for the logical unit described by this
logical unit descriptor. The value in the DEFAULT LUN field shall be consistent with the DLGENERATION field
value returned in the parameter list header (see 8.3.2.3.2). The value in the DEFAULT LUN field shall not identify
a well known logical unit.
The EVPD DESIGNATION DESCRIPTOR LENGTH field indicates the number of non pad bytes in the EVPD DESIG-
NATION DESCRIPTOR field.
The DEVICE IDENTIFIER LENGTH field indicates the number of non pad bytes in the DEVICE IDENTIFIER field.
Table 684 — Logical Unit descriptor format
Bit
Byte
Reserved
PERIPHERAL DEVICE TYPE
Reserved
(MSB)
DESCRIPTOR LENGTH (n-3)
(LSB)
DEFAULT LUN
•••
Reserved
EVPD DESIGNATION DESCRIPTOR LENGTH
Reserved
DEVICE IDENTIFIER LENGTH
EVPD DESIGNATION DESCRIPTOR
•••
(MSB)
DEVICE IDENTIFIER
•••
(LSB)
DEVICE TYPE SPECIFIC DATA
•••
n


The EVPD DESIGNATION DESCRIPTOR field shall be derived from one of the Device Identification VPD page (see
7.8.6) designation descriptors having 00b in the ASSOCIATION field as follows:
a)
if the designation descriptor has a length less than 32 bytes, then the EVPD DESIGNATION DESCRIPTOR
field shall be set to the zero-padded (see 4.3.2) designation descriptor value. The EVPD DESIGNATION
DESCRIPTOR LENGTH field shall be set to the length of the designation descriptor not including pad
bytes; or
b)
if the designation descriptor has a length greater than or equal to 32 bytes, then the EVPD DESIGNATION
DESCRIPTOR field shall be set to the first 32 bytes of the designation descriptor. The EVPD DESIGNATION
DESCRIPTOR LENGTH field shall be set to 32.
If there are several designation descriptors having 00b in the ASSOCIATION field, the choice of which descriptor
to copy to the EVPD DESIGNATION DESCRIPTOR field is vendor specific, however, all ACCESS CONTROL IN
commands with REPORT LU DESCRIPTORS service action shall return the same EVPD DESIGNATION
DESCRIPTOR field contents for a specific logical unit.
If a device identifier has been set for the logical unit using the SET IDENTIFYING INFORMATION command
(see 6.43), the DEVICE IDENTIFIER field shall contain that device identifier subject to the following consider-
ations:
a)
if the device identifier has length less than 32 bytes, then the DEVICE IDENTIFIER field shall be set to the
zero-padded (see 4.3.2) device identifier value. The DEVICE IDENTIFIER LENGTH field shall be set to the
length of the device identifier not including pad bytes; or
b)
if the device identifier has length greater than or equal to 32 bytes, then the DEVICE IDENTIFIER field
shall be set to the first 32 bytes of the identifier. The DEVICE IDENTIFIER LENGTH field shall be set to 32.
If no device identifier has been established by a SET IDENTIFYING INFORMATION command, then the
DEVICE IDENTIFIER LENGTH field shall be set to zero and the DEVICE IDENTIFIER field shall be set to zero.
If the PERIPHERAL DEVICE TYPE field contains any value other than 0h, 4h, or 7h, the DEVICE TYPE SPECIFIC DATA
field shall not be present in the Logical Unit descriptor.
The Logical Unit descriptor shall include the DEVICE TYPE SPECIFIC DATA field if:
a)
the PERIPHERAL DEVICE TYPE field contains 0h, 4h, or 7h;
b)
the logical unit supports the READ CAPACITY(16) command (see SBC-3); and
c)
the logical unit standard INQUIRY data (see 6.6.2) has the RMB bit set to zero.
If the Logical Unit descriptor includes the DEVICE TYPE SPECIFIC DATA field, then the size of the DEVICE TYPE
SPECIFIC DATA field shall be 12 bytes and the field shall contain data equivalent to the first 12 bytes of
parameter data returned by a successful READ CAPACITY(16) command.


8.3.2.4 REPORT ACCESS CONTROLS LOG service action
8.3.2.4.1 REPORT ACCESS CONTROLS LOG introduction
The ACCESS CONTROL IN command with REPORT ACCESS CONTROLS LOG service action (see table
685) is used to obtain the access controls log (see 8.3.1.10). If the ACCESS CONTROL IN command is imple-
mented, the REPORT ACCESS CONTROLS LOG service action shall be implemented.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 685 for the ACCESS
CONTROL IN command with REPORT ACCESS CONTROLS LOG service action.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 685 for the ACCESS
CONTROL IN command with REPORT ACCESS CONTROLS LOG service action.
If access controls are disabled, the device server shall ignore the MANAGEMENT IDENTIFIER KEY field and shall
complete the command with GOOD status returning the eight byte parameter list header as defined in
8.3.2.4.2.1 subject to the ALLOCATION LENGTH limitation described in 4.2.5.6.
Since the Key Overrides portion of the log is maintained while access controls are disabled (see 8.3.3.3), it
may be retrieved by enabling access controls and issuing an ACCESS CONTROL IN command with
REPORT ACCESS CONTROLS LOG service action.
If access controls are enabled and table 686 specifies that the management identifier key is not required then
the device server shall ignore the contents of the MANAGEMENT IDENTIFIER KEY field.
If access controls are enabled, table 686 specifies that the management key identifier is required, and the
contents of the MANAGEMENT IDENTIFIER KEY field do not match the current management identifier key (see
8.3.1.8) maintained by the access controls coordinator, then the parameter data shall not be returned and the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to ACCESS DENIED - INVALID MGMT ID KEY. This event shall
be recorded in the invalid keys portion of the access controls log (see 8.3.1.10).
Table 685 — ACCESS CONTROL IN command REPORT ACCESS CONTROLS LOG service action
Bit
Byte
OPERATION CODE (86h)
Reserved
SERVICE ACTION (02h)
(MSB)
MANAGEMENT IDENTIFIER KEY

•••
(LSB)
Reserved
LOG PORTION
Reserved
(MSB)
ALLOCATION LENGTH
(LSB)
Reserved
CONTROL


The LOG PORTION field (see table 686) specifies the access controls log portion being requested.
The ALLOCATION LENGTH field is defined in 4.2.5.6. The ALLOCATION LENGTH field value should be at least eight.
The CONTROL byte is defined in SAM-5.
8.3.2.4.2 REPORT ACCESS CONTROLS LOG parameter data format
8.3.2.4.2.1 REPORT ACCESS CONTROLS LOG parameter data introduction
The format of the parameter data returned in response to an ACCESS CONTROL IN command with REPORT
ACCESS CONTROLS LOG service actions is shown in table 687.
The LOG LIST LENGTH field shall contain a count of the number of bytes in the remaining parameter data. If
access controls are disabled, the LOG LIST LENGTH field shall be set to four. The contents of the LOG LIST
LENGTH field are not altered based on the allocation length (see 4.2.5.6).
Table 686 — CDB LOG PORTION field
Code
Description
Management Identifier
Key Required
00b
Key Overrides portion
No
01b
Invalid Keys portion
Yes
10b
ACL LUN Conflicts portion
Yes
11b
Reserved
Table 687 — ACCESS CONTROL IN with REPORT ACCESS CONTROLS LOG parameter data format
Bit
Byte
Parameter list header
(MSB)
LOG LIST LENGTH (n-3)
•••
(LSB)
Reserved
Reserved
LOG PORTION
(MSB)
COUNTER
(LSB)
Access Controls Log portion pages
Access Controls Log portion page 0
•••
•••
Access Controls Log portion page x
•••
n


The LOG PORTION field (see table 688) indicates the access controls log portion being returned, the contents of
the COUNTER field, and the type of access controls log portion pages being returned.
The COUNTER field contains the events counter value (see 8.3.1.10) for the access controls log portion
indicated by the LOG PORTION field (see table 688).
The format of the access controls log portion pages is indicated by the value in the LOG PORTION field (see
table 688). All the access controls log portion pages returned in a single parameter list shall have the same
format. If the access controls coordinator does not support access controls log portion pages in the portion of
the access controls log indicated by the LOG PORTION field, then the parameter data shall only contain the
parameter list header.
8.3.2.4.2.2 Key Overrides access controls log portion page format
The Key Overrides access controls log portion page (see table 689) contains details of logged attempts to
override the management identifier key (see 8.3.1.10) using the ACCESS CONTROL OUT command with
OVERRIDE MGMT ID KEY service action (see 8.3.3.8) whether those attempts were successful or not.
The TRANSPORTID ADDITIONAL LENGTH field indicates the additional length of the TransportID beyond the
minimum length of 24 bytes. The TransportID additional length shall be a multiple of four.
Table 688 — Parameter data LOG PORTION field
Code
Access Controls Log
Portion Being Returned
COUNTER Field Contents
Access Controls Log
Page Format Reference
00b
Key Overrides portion
Key Override events counter
8.3.2.4.2.2
01b
Invalid Keys portion
Invalid Key events counter
8.3.2.4.2.3
11b
ACL LUN Conflicts portion
ACL LUN Conflict events counter
8.3.2.4.2.4
11b
Reserved
Table 689 — Key Overrides access controls log portion page format
Bit
Byte
(MSB)
TRANSPORTID ADDITIONAL LENGTH (m-32)
(LSB)
Reserved
Reserved
SUCCESS
(MSB)
TIME STAMP
•••
(LSB)
TransportID
•••
m-1
m
(MSB)
INITIAL OVERRIDE LOCKOUT TIMER
m+1
(LSB)
m+2
(MSB)
OVERRIDE LOCKOUT TIMER
m+3
(LSB)


A SUCCESS bit set to one indicates that the specific ACCESS CONTROL OUT command with OVERRIDE
MGMT ID KEY service action event recorded in the access controls log successfully overrode the
management identifier key. A SUCCESS bit set to zero indicates that the command did not succeed.
The TIME STAMP field shall contain zero or an indication of the time at which the ACCESS CONTROL OUT
command with OVERRIDE MGMT ID KEY service action was processed as described in 8.3.1.10.
The TransportID indicates the TransportID of the initiator port from which the command was received.
The INITIAL OVERRIDE LOCKOUT TIMER field shall contain the access controls coordinator’s initial override
lockout timer value (see 8.3.1.8.2.2) at the time when the key override event was logged.
The OVERRIDE LOCKOUT TIMER field shall contain the access controls coordinator’s override lockout timer value
(see 8.3.1.8.2.2) at the time when the key override event was logged.
8.3.2.4.2.3 Invalid Keys access controls log portion page format
The Invalid Keys access controls log portion page (see table 690) contains details of logged receipts of
ACCESS CONTROL IN or ACCESS CONTROL OUT commands specifying an incorrect management
identifier key (see 8.3.1.10).
The TRANSPORTID ADDITIONAL LENGTH field indicates the additional length of the TransportID beyond the
minimum length of 24 bytes. The TransportID additional length shall be a multiple of four.
The OPERATION CODE and SERVICE ACTION fields shall be set to the respective values from the CDB of the
access controls command that specified the invalid management identifier key.
The TIME STAMP field shall contain zero or an indication of the time at which the ACCESS CONTROL IN or
ACCESS CONTROL OUT command was processed as described in 8.3.1.10.
The TransportID indicates the TransportID of the initiator port from which the command was received.
Table 690 — Invalid Keys access controls log portion page format
Bit
Byte
(MSB)
TRANSPORTID ADDITIONAL LENGTH (m-32)
(LSB)
OPERATION CODE
Reserved
SERVICE ACTION
(MSB)
TIME STAMP
•••
(LSB)
TransportID
•••
m-1
m
(MSB)
INVALID MANAGEMENT IDENTIFIER KEY
•••
m+7
(LSB)


The INVALID MANAGEMENT IDENTIFIER KEY field shall be set to the value of the invalid management identifier key
detected by the access controls coordinator.
NOTE 78 - The management identifier key is typically in the CDB for ACCESS CONTROL IN commands and
in the parameter data for ACCESS CONTROL OUT commands.
8.3.2.4.2.4 ACL LUN Conflicts access controls log portion page format
The ACL LUN Conflicts access controls log portion page (see table 691) contains details of logged ACL LUN
conflicts (see 8.3.1.10) encountered by the access controls coordinator if a previously not-enrolled initiator
port sends an ACCESS CONTROL OUT command with ACCESS ID ENROLL service action (see 8.3.3.4).
The TRANSPORTID ADDITIONAL LENGTH field indicates the additional length of the TransportID beyond the
minimum length of 24 bytes. The TransportID additional length shall be a multiple of four.
The TIME STAMP field shall contain zero or an indication of the time at which the ACCESS CONTROL OUT
command with ACCESS ID ENROLL service action was processed as described in 8.3.1.10.
The TransportID indicates the TransportID of the initiator port from which the command was received that
resulted in the ACL LUN conflict.
The ACCESSID field shall be set to the AccessID that the initiator port attempted to enroll. This shall corre-
spond to an access identifier in ACL entry at the time the ACL LUN conflict event occurred.
Table 691 — ACL LUN Conflicts access controls log portion page format
Bit
Byte
(MSB)
TRANSPORTID ADDITIONAL LENGTH (m-32)
(LSB)
Reserved
(MSB)
TIME STAMP
•••
(LSB)
TransportID
•••
m-1
m
(MSB)
ACCESSID
•••
m+23
(LSB)


8.3.2.5 REPORT OVERRIDE LOCKOUT TIMER service action
The ACCESS CONTROL IN command with REPORT OVERRIDE LOCKOUT TIMER service action (see
table 692) is used query the value of the override lockout timer (see 8.3.1.8.2.2). If the ACCESS CONTROL
IN command is implemented, the REPORT OVERRIDE LOCKOUT TIMER service action shall be imple-
mented.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 692 for the ACCESS
CONTROL IN command with REPORT OVERRIDE LOCKOUT TIMER service action.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 692 for the ACCESS
CONTROL IN command with REPORT OVERRIDE LOCKOUT TIMER service action.
If access controls are disabled, eight bytes of zeros shall be returned subject to the allocation length limita-
tions described in 4.2.5.6 and GOOD status shall be returned.
If access controls are enabled and the contents of the MANAGEMENT IDENTIFIER KEY field do not match the
current management identifier key (see 8.3.1.8) maintained by the access controls coordinator, then
parameter data shall not be returned, the command shall be terminated with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED - INVALID
MGMT ID KEY. This event shall be recorded in the invalid keys portion of the access controls log (see
8.3.1.10).
The ALLOCATION LENGTH field is defined in 4.2.5.6. The ALLOCATION LENGTH field value should be at least eight.
The CONTROL byte is defined in SAM-5.
Table 692 — ACCESS CONTROL IN command REPORT OVERRIDE LOCKOUT TIMER service action
Bit
Byte
OPERATION CODE (86h)
Reserved
SERVICE ACTION (03h)
(MSB)
MANAGEMENT IDENTIFIER KEY

•••
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


If access controls are enabled, the parameter data returned by the ACCESS CONTROL IN command with
REPORT OVERRIDE LOCKOUT TIMER service action shall have the format shown in table 693.
The CURRENT OVERRIDE LOCKOUT TIMER field shall be set to the current value of the override lockout timer (see
8.3.1.8.2.2).
The INITIAL OVERRIDE LOCKOUT TIMER field shall be set to the initial override lockout timer value (see
8.3.1.8.2.2) established by the last successful ACCESS CONTROL OUT command with MANAGE
OVERRIDE LOCKOUT TIMER service action (see 8.3.3.7).
The KEY OVERRIDES COUNTER field shall be set to the value of the Key Override events counter in the access
controls log (see 8.3.1.10).
8.3.2.6 REQUEST PROXY TOKEN service action
The ACCESS CONTROL IN command with REQUEST PROXY TOKEN service action (see table 694) is used
to obtain a proxy token (see 8.3.1.6.2) for a logical unit to which that initiator port has non-proxy access rights.
The returned proxy token may be used to pass temporary access to the logical unit to a third party that may
use other proxy related service actions of the ACCESS CONTROL IN and ACCESS CONTROL OUT
Table 693 — ACCESS CONTROL IN with REPORT OVERRIDE LOCKOUT TIMER parameter data
Bit
Byte
Reserved
(MSB)
CURRENT OVERRIDE LOCKOUT TIMER
(LSB)
(MSB)
INITIAL OVERRIDE LOCKOUT TIMER
(LSB)
(MSB)
KEY OVERRIDES COUNTER
(LSB)


commands to gain access to the logical unit. If the ACCESS CONTROL IN command with REQUEST PROXY
TOKEN service action is not supported, the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 694 for the ACCESS
CONTROL IN command with REQUEST PROXY TOKEN service action.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 694 for the ACCESS
CONTROL IN command with REQUEST PROXY TOKEN service action.
If access controls are disabled, the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
NOTE 79 - If access controls are disabled, all logical units are accessible and all initiator ports share the
same LUN values for addressing. A proxy token is not needed because sharing LUN values is sufficient.
The LUN VALUE field shall contain the LUN value the application client uses to access the logical unit via the
initiator port over which the proxy token is requested.
If the LUN value corresponds to a logical unit that is accessible to the requesting initiator port either through a
TransportID or through the AccessID under which the initiator port is currently in the enrolled state (see
8.3.1.5.1), and the access controls coordinator has sufficient resources to create and manage a new proxy
token, then the parameter data shown in table 695 shall be returned.
If the LUN value does not correspond to an accessible logical unit or corresponds to a logical unit accessible
only through a proxy token, then the parameter data shall not be returned and the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to ACCESS DENIED - INVALID LU IDENTIFIER.
If the LUN value corresponds to a logical unit accessible only through an enrolled AccessID and the initiator
port is in the pending-enrolled state, then the parameter data shall not be returned and the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to ACCESS DENIED - INITIATOR PENDING-ENROLLED.
Table 694 — ACCESS CONTROL IN command with REQUEST PROXY TOKEN service action
Bit
Byte
OPERATION CODE (86h)
Reserved
SERVICE ACTION (04h)
(MSB)
LUN VALUE

•••
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
