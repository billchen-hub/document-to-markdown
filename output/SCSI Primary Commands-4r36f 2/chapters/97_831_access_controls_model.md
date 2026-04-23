# 8.3.1 Access controls model

8.3 ACCESS CONTROLS well known logical unit
8.3.1 Access controls model
8.3.1.1 Access controls commands
The ACCESS CONTROLS well known logical unit shall only process the commands listed in table 664. If a
command is received by the ACCESS CONTROLS well know logical unit that is not listed in table 664, then
the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
8.3.1.2 Access controls overview
Access controls are a SCSI target device feature that application clients may use to restrict logical unit access
to specified initiator ports or groups of initiator ports.
Access controls shall not allow restrictions to be placed on access to well known logical units. Access controls
shall not cause new well known logical units to be defined.
Access controls are handled in the SCSI target device by an access controls coordinator located at the
ACCESS CONTROLS well known logical unit. The access controls coordinator also may be accessible via
LUN 0. The access controls coordinator associates a specific LUN to a specific logical unit depending on
which initiator port accesses the SCSI target device and whether the initiator port has access rights to the
logical unit.
Access rights to a logical unit affects whether the logical unit number appears in the parameter data returned
by a REPORT LUNS command and how the logical unit responds to INQUIRY commands.
The access controls coordinator maintains the ACL as described in 8.3.1.3 to supply information about:
a)
which initiator ports are allowed access to which logical units; and
b)
which LUN value is used by a specific initiator port when accessing a specific logical unit.
The format of the ACL is vendor specific.
To support third party commands (e.g., EXTENDED COPY), the access controls coordinator may provide
proxy tokens (see 8.3.1.6.2) to allow an application client to pass its access capabilities to the application
client for another initiator port.
An application client manages the access controls state of the SCSI target device using the ACCESS
CONTROL IN command (see 8.3.2) and the ACCESS CONTROL OUT command (see 8.3.3).
Table 664 — Commands for the ACCESS CONTROLS well known logical unit
Command
Operation
code
Type
Reference
ACCESS CONTROL IN
86h
M
8.3.2
ACCESS CONTROL OUT
87h
M
8.3.3
INQUIRY
12h
M
6.6
REQUEST SENSE
03h
M
6.39
TEST UNIT READY
00h
M
6.47
Key: M = Command implementation is mandatory.


A SCSI target device has access controls disabled when it is manufactured and after successful completion of
the ACCESS CONTROL OUT command with DISABLE ACCESS CONTROLS service action (see 8.3.3.3). If
access controls are disabled, the ACL contains no entries and the management identifier key (see 8.3.1.8) is
zero.
The first successful ACCESS CONTROL OUT command with MANAGE ACL service action (see 8.3.3.2)
shall enable access controls. If access controls are enabled, all logical units, except LUN 0 and all well known
logical units, shall be inaccessible to all initiator ports unless the ACL (see 8.3.1.3) allows access.
The ACL allows an initiator port access to a logical unit if the ACL contains an ACE (see 8.3.1.3) with an
access identifier (see 8.3.1.3.2) associated with the initiator port and that ACE contains a LUACD (see
8.3.1.3.3) that references the logical unit.
If the ACL allows access to a logical unit, the REPORT LUNS command parameter data bytes representing
that logical unit shall contain the LUN value found in the LUACD that references that logical unit and the appli-
cation client for the initiator port shall use the same LUN value when sending commands to the logical unit.
An initiator port also may be allowed access to a logical unit through the use of a proxy token (see 8.3.1.6.2).
Once access controls are enabled, they shall remain enabled until:
a)
successful completion of an ACCESS CONTROL OUT command with DISABLE ACCESS
CONTROLS service action; or
b)
vendor specific physical intervention.
Successful downloading of microcode (see 6.49) may result in access controls being disabled.
Once access controls are enabled, power cycles, hard resets, logical unit resets, and I_T nexus losses shall
not disable them.
8.3.1.3 The access control list (ACL)
8.3.1.3.1 ACL overview
The specific access controls for a SCSI target device are instantiated by the access controls coordinator using
data in an ACL. The ACL contains zero or more ACEs and zero or more proxy tokens (see 8.3.1.6.2.1).
Each ACE contains the following:
a)
one access identifier (see 8.3.1.3.2) that identifies the initiator port(s) to which the ACE applies; and
b)
a list of LUACDs (see 8.3.1.3.3) that identify the logical units to which the identified initiator port(s)
have access rights and the LUNs used to access those logical units via those initiator port(s). Each
LUACD contains the following:
A)
a vendor specific logical unit reference; and
B)
a LUN value.


Figure 19 shows the logical structure of an ACL.
8.3.1.3.2 Access identifiers
Initiator ports are identified in an ACE using one of the following types of access identifiers:
a)
AccessID - based on initiator port enrollment;
b)
TransportID - based on protocol specific identification of initiator ports; or
c)
vendor specific access identifiers.
An initiator port is allowed access to the logical units in an ACE containing an AccessID type access identifier
when that initiator port is enrolled as described in 8.3.1.5. An initiator port that has not previously enrolled
uses the ACCESS CONTROL OUT command with ACCESS ID ENROLL service action to enroll including the
AccessID in parameter data as defined in 8.3.3.4.
An initiator port is associated with an AccessID type access identifier if that initiator port is in the enrolled state
or pending-enrolled state with respect to that AccessID (see 8.3.1.5). At any instant in time, an initiator port
may be associated with at most one AccessID. All initiator ports enrolled using a specific AccessID share the
same ACE and access to all the logical units its LUACDs describe.
TransportID access identifiers are SCSI transport protocol specific as described in 7.6.4.
An initiator port is allowed access to the logical units in an ACE containing a TransportID type access identifier
if the identification for the initiator port matches that found in the TransportID in a way that is consistent with
the TransportID definition (see 7.6.4). There is no need to process any command to obtain logical unit access
based on a Transport ID because the needed information is provided by the SCSI transport protocol layer.
The formats of access identifiers are defined in 8.3.1.13.
Figure 19 — ACL Structure
ACE
ACE
ACE
ACE
Proxy
Token
ACL
Access
Identifier
LUACD
LUACD
LUACD
LUACD
LUACD
ACE
Logical Unit
Reference
LUACD
LUN
Proxy
Token
Proxy
Token


8.3.1.3.3 Logical unit access control descriptors
Each LUACD in an ACE identifies one logical unit to which the initiator ports associated with the access
identifier are allowed access and specifies the LUN value used when accessing the logical unit via those
initiator ports. The format of a LUACD is vendor specific.
The identification of a logical unit in a LUACD is vendor specific. The logical unit identified by a LUACD shall
not be a well known logical unit. A logical unit shall be referenced in no more than one LUACD per ACE.
The LUN value shall conform to the requirements defined in SAM-5. A specific LUN value shall appear in no
more than one LUACD per ACE.
8.3.1.4 Managing the ACL
8.3.1.4.1 ACL management overview
The contents of the ACL are managed by an application client using the ACCESS CONTROL OUT command
with MANAGE ACL and DISABLE ACCESS CONTROLS service actions. The ACCESS CONTROL OUT
command with MANAGE ACL service action (see 8.3.3.2) is used to add, remove, or modify ACEs thus
adding, revoking, or changing the allowed access of initiator ports to logical units. The ACCESS CONTROL
OUT command with DISABLE ACCESS CONTROLS service action (see 8.3.3.3) disables access controls
and discards the ACL.
8.3.1.4.2 Authorizing ACL management
To reduce the possibility of applications other than authorized ACL managers changing the ACL, successful
completion of specific access controls service actions (e.g., ACCESS CONTROL OUT command with
MANAGE ACL or DISABLE ACCESS CONTROLS service action) requires delivery of the correct
management identifier key value (see 8.3.1.8) in the ACCESS CONTROL OUT parameter data. The service
actions that require the correct management identifier key are shown in table 665 and table 666.
Table 665 — ACCESS CONTROL OUT management identifier key requirements
ACCESS CONTROL OUT command
service action
Management Identifier
Key Required
Reference
ACCESS ID ENROLL
No
8.3.3.4
ASSIGN PROXY LUN
No
8.3.3.11
CANCEL ENROLLMENT
No
8.3.3.5
CLEAR ACCESS CONTROLS LOG
Yes
8.3.3.6
DISABLE ACCESS CONTROLS
Yes
8.3.3.3
MANAGE ACL
Yes
8.3.3.2
MANAGE OVERRIDE LOCKOUT TIMER
Yes/No
8.3.3.7
OVERRIDE MGMT ID KEY
No
8.3.3.8
RELEASE PROXY LUN
No
8.3.3.12
REVOKE ALL PROXY TOKENS
No
8.3.3.10
REVOKE PROXY TOKEN
No
8.3.3.9


8.3.1.4.3 Identifying logical units during ACL management
The access controls coordinator shall identify every logical unit of a SCSI target device with a unique default
LUN value. The default LUN values used by the access controls coordinator shall be the LUN values that
would be reported by the REPORTS LUNS command if access controls were disabled.
An application client discovers the default LUN values using the ACCESS CONTROL IN command with
REPORT LU DESCRIPTORS (see 8.3.2.3) or REPORT ACL (see 8.3.2.2) service action and then supplies
those default LUN values to the access controls coordinator using the ACCESS CONTROL OUT command
with MANAGE ACL service action.
The association between default LUN values and logical units is managed by the access controls coordinator
and may change due to circumstances that are beyond the scope of this standard. To track such changes, the
access controls coordinator maintains the DLgeneration counter as described in 8.3.1.4.4.
8.3.1.4.4 Tracking changes in logical unit identification
The access controls coordinator shall implement a Default LUNs Generation (DLgeneration) counter to track
changes in the association between default LUN values and logical units. The DLgeneration counter is a
wrapping counter.
When access controls are disabled the DLgeneration counter shall be set to zero. When access controls are
first enabled (see 8.3.1.2) the DLgeneration counter shall be set to one. While access controls are enabled,
the access controls coordinator shall increment the DLgeneration counter by one every time the association
between default LUN values and logical units changes (e.g., following the creation of a new logical unit,
deletion of an existing logical unit, or removal and recreation of an existing logical unit).
The access controls coordinator shall include the current DLgeneration value in the parameter data returned
by an ACCESS CONTROL IN command with REPORT LU DESCRIPTORS (see 8.3.2.3) or REPORT ACL
(see 8.3.2.2) service action. The application client shall supply the DLgeneration value for the default LUN
values it is using in the parameter data for an ACCESS CONTROL OUT command with MANAGE ACL
service action (see 8.3.3.2).
Before processing the ACL change information in the parameter list provided by an ACCESS CONTROL OUT
command with MANAGE ACL service action, the access controls coordinator shall verify that the DLgener-
ation value in the parameter data matches the current value of the DLgeneration counter. If the DLgeneration
value verification finds a mismatch, the command shall be terminated with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
Table 666 — ACCESS CONTROL IN management identifier key requirements
ACCESS CONTROL IN command
service action
Management Identifier
Key Required
Reference
REPORT ACCESS CONTROLS LOG
Yes
8.3.2.4
REPORT ACL
Yes
8.3.2.2
REPORT LU DESCRIPTORS
Yes
8.3.2.3
REPORT OVERRIDE LOCKOUT TIMER
Yes
8.3.2.5
REQUEST PROXY TOKEN
No
8.3.2.6


8.3.1.5 Enrolling AccessIDs
8.3.1.5.1 Enrollment states
8.3.1.5.1.1 Summary of enrollment states
Application clients enroll an initiator port AccessID with the access controls coordinator to be allowed to
access logical units listed in the ACE having the same AccessID type access identifier. The ACCESS
CONTROL OUT command with ACCESS ID ENROLL service action (see 8.3.3.4) is used to enroll an
AccessID. An initiator port shall be in one of three states with respect to such an enrollment:
a)
Not-enrolled: the state for an initiator port before the first ACCESS CONTROL OUT command with
ACCESS ID ENROLL service action is sent to the access controls coordinator. Also the state for an
initiator port following successful completion of an ACCESS CONTROL OUT command with CANCEL
ENROLLMENT service action (see 8.3.3.5);
b)
Enrolled: the state for an initiator port following successful completion of an ACCESS CONTROL
OUT command with ACCESS ID ENROLL service action; or
c)
Pending-enrolled: the state for an enrolled initiator port following:
A)
events described in 8.3.1.12; or
B)
successful completion of an ACCESS CONTROL OUT command with MANAGE ACL service
action from any initiator port with the FLUSH bit set to one (see 8.3.3.2).
8.3.1.5.1.2 Not-enrolled state
The access controls coordinator shall place an initiator port in the not-enrolled state when it first detects the
receipt of a SCSI command or task management function from that initiator port. The initiator port shall remain
in the not-enrolled state until successful completion of an ACCESS CONTROL OUT command with ACCESS
ID ENROLL service action (see 8.3.3.5).
While in the not-enrolled state, an initiator port shall only have access to logical units on the basis of a Trans-
portID (see 8.3.1.3.2) or on the basis of proxy tokens (see 8.3.1.6.2.1).
The access controls coordinator changes an initiator port from the enrolled state or pending-enrolled state to
the not-enrolled state in response to the following events:
a)
successful completion of the ACCESS CONTROL OUT command with CANCEL ENROLLMENT
service action (see 8.3.3.5) shall change the state to not-enrolled; or
b)
successful completion of an ACCESS CONTROL OUT command with MANAGE ACL service action
(see 8.3.3.2) that replaces the ACL entry for the enrolled AccessID as follows:
A)
if the NOCNCL bit (see 8.3.3.2.2) is set to zero in the ACCESS CONTROL OUT command with
MANAGE ACL service action parameter data, the state shall change to not-enrolled; or
B)
if the NOCNCL bit is set to one, the state may change to not-enrolled based on vendor specific
criteria.
An application client for an enrolled initiator port may discover that the initiator port has transitioned to the
not-enrolled state as a result of actions taken by a third party (e.g., an ACCESS CONTROL OUT command
with MANAGE ACL service action performed by another initiator port or a logical unit reset).
Placing an enrolled initiator in the not-enrolled state indicates that the ACE defining that initiator port’s logical
unit access has changed (e.g., previous relationships between logical units and LUN values may no longer
apply).


If an application client detects this loss of enrollment on an initiator port, it may take recovery actions.
However, such actions may be disruptive for the SCSI initiator device and may not be required. Use of the
not-enrolled state is avoidable if the application client that sends the ACCESS CONTROL OUT command with
MANAGE ACL service action determines that its requested changes to the ACL do not alter the existing
relationships between logical units and LUN values in any existing ACEs with AccessID type access identifiers
and sets the NOCNCL bit to one, recommending that initiator ports be left in their current enrollment state.
The access controls coordinator selects from the following options for responding to a NOCNCL bit set to one in
a vendor specific manner:
a)
honor the recommendation, causing the minimum effects on SCSI initiator devices and requiring no
extra actions on the part of the access controls coordinator;
b)
ignore the recommendation and always place initiator ports in the non-enrolled state, causing the
maximum disruption for SCSI initiator devices, but requiring no extra resources on the part of the
access controls coordinator; or
c)
ignore the recommendation and examine the current and new ACEs to determine if an initiator port
should be placed in the non-enrolled state.
If the application client that sends the ACCESS CONTROL OUT command with MANAGE ACL service action
is unable to determine whether the ACE logical unit relationships are altered as a result of processing the
command, then it should set the NOCNCL bit to zero and it should coordinate the ACL change with the appli-
cation clients for affected initiator ports to ensure proper data integrity. Such coordination is beyond the scope
of this standard.
8.3.1.5.1.3 Enrolled state
The access controls coordinator shall place an initiator port in the enrolled state (i.e., enroll the initiator port)
following successful completion of the ACCESS CONTROL OUT command with ACCESS ID ENROLL
service action (see 8.3.3.4). The ACCESS CONTROL OUT command with ACCESS ID ENROLL service
action is successful only if:
a)
the initiator port was in the not-enrolled state and the AccessID in the ACCESS CONTROL OUT
command with ACCESS ID ENROLL service action parameter data matches the access identifier in
an ACE. This results in the initiator port being enrolled and allowed access to the logical units
specified in the LUACDs in the ACE (see 8.3.1.3); or
b)
the initiator port was in the enrolled state or pending-enrolled state and the AccessID in the ACCESS
CONTROL OUT command with ACCESS ID ENROLL service action parameter data matches the
current enrolled AccessID for the initiator port.
If the initiator port was in the enrolled state or pending-enrolled state and the AccessID in the ACCESS
CONTROL OUT command with ACCESS ID ENROLL service action parameter data does not match the
current enrolled AccessID for the initiator port, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
ACCESS DENIED - ENROLLMENT CONFLICT. If the initiator port was in the enrolled state, it shall be transi-
tioned to the pending-enrolled state.
Transitions from the enrolled state to the not-enrolled state are described in 8.3.1.5.1.2. Transitions from the
enrolled state to the pending-enrolled state are described in 8.3.1.5.1.4.
NOTE 76 - This standard does not preclude implicit enrollments through mechanisms in a service delivery
subsystem. Such mechanisms should perform implicit enrollments after identification by TransportID and
should fail in the case where there are ACL conflicts as described in 8.3.1.5.2.


8.3.1.5.1.4 Pending-enrolled state
The access controls coordinator shall place an initiator port in the pending-enrolled state if that initiator port
currently is in the enrolled state, and in response to the following:
a)
a logical unit reset;
b)
an I_T nexus loss associated with that initiator port; or
c)
successful completion of an ACCESS CONTROL OUT command with MANAGE ACL service action
where the FLUSH bit is set to one in the parameter data.
While in the pending-enrolled state, the initiator port’s access to logical units is limited as described in 8.3.1.7.
8.3.1.5.2 ACL LUN conflict resolution
ACL LUN conflicts may occur if:
a)
an application client for an initiator port in the not-enrolled state attempts to enroll an AccessID using
the ACCESS CONTROL OUT command with ACCESS ID ENROLL service action (see 8.3.3.4); or
b)
an ACCESS CONTROL OUT command with MANAGE ACL service action (see 8.3.3.2) attempts to
change the ACL with the result that it conflicts with existing enrollments (see 8.3.1.5) or proxy LUN
assignments (see 8.3.1.6.2.2).
Three types of ACL LUN conflicts may occur:
a)
the TransportID ACE (see 8.3.1.3) and the AccessID ACE for the initiator port each contain a LUACD
with the same LUN value but with different logical unit references;
b)
the TransportID ACE and the AccessID ACE for the initiator port each contain a LUACD with the
different LUN values but with the same logical unit references; or
c)
the enrolling initiator port has proxy access rights to a logical unit addressed with a LUN value that
equals a LUN value in a LUACD in the AccessID ACE for the initiator port.
If an ACL LUN conflict occurs during the processing of an ACCESS CONTROL OUT command with MANAGE
ACL service action, the command shall be terminated with CHECK CONDITION status (see 8.3.3.2.2).
If an ACL LUN conflict occurs during the processing of an ACCESS CONTROL OUT command with ACCESS
ID ENROLL service action, the following actions shall be taken as part of the handling of the enrollment
function:
a)
the ACCESS CONTROL OUT command with ACCESS ID ENROLL service action shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, the additional
sense code set to ACCESS DENIED - ACL LUN CONFLICT;
b)
the initiator port shall remain in the not-enrolled state; and
c)
if the ACL LUN conflict is not the result of proxy access rights, the access controls coordinator shall
record the event in the access controls log as described in 8.3.1.10.
8.3.1.6 Granting and revoking access rights
8.3.1.6.1 Non-proxy access rights
The ACCESS CONTROL OUT command with MANAGE ACL service action (see 8.3.3.2) adds or replaces
ACEs in the ACL (see 8.3.1.3). One ACE describes the logical unit access allowed by one access identifier
(see 8.3.1.3.2) and the LUN values to be used in addressing the accessible logical units. The access identifier
specifies the initiator port(s) permitted access to the logical units described by the ACE.


With the exception of proxy access rights (see 8.3.1.6.2), access rights are granted by:
a)
adding a new ACE to the ACL; or
b)
replacing an existing ACE with an ACE that includes additional LUACDs.
With the exception of proxy access rights, access rights are revoked by:
a)
removing an ACE from the ACL; or
b)
replacing an existing ACE with an ACE that removes one or more LUACDs.
If an ACE is added or replaced the requirements stated in 8.3.1.5.1.2 and 8.3.1.11 apply.
8.3.1.6.2 Proxy access
8.3.1.6.2.1 Proxy tokens
An application client with access rights to a logical unit via an initiator port on the basis of an ACE in the ACL
(see 8.3.1.6.1) may temporarily share that access with third parties using the proxy access mechanism. The
application client uses the ACCESS CONTROL IN command with REQUEST PROXY TOKEN service action
(see 8.3.2.6) to request that the access control coordinator generate a proxy token for the logical unit
specified by the LUN value in the CDB.
The access controls coordinator generates the proxy token in a vendor specific manner. For a specific SCSI
target device, all active proxy token values should be unique. Proxy token values should be reused as infre-
quently as possible to prevent proxy tokens that have been used and released from being given unintended
meaning.
Power cycles, hard resets, logical unit resets, and I_T nexus losses shall not affect the validity and proxy
access rights of proxy tokens (see 8.3.1.12). A proxy token shall remain valid and retain the same proxy
access rights until one of the following occurs:
a)
an application client with access rights to a logical unit via an initiator port based on an ACE in the
ACL revokes the proxy token using:
A)
the ACCESS CONTROL OUT command with REVOKE PROXY TOKEN service action (see
8.3.3.9); or
B)
the ACCESS CONTROL OUT command with REVOKE ALL PROXY TOKENS service action
(see 8.3.3.10);
or
b)
an application client issues the ACCESS CONTROL OUT command with MANAGE ACL service
action (see 8.3.3.2) with parameter data containing the Revoke Proxy Token ACE page (see
8.3.3.2.4) or Revoke All Proxy Tokens ACE page (see 8.3.3.2.5).
8.3.1.6.2.2 Proxy LUNs
To extend proxy access rights to a third party, an application client forwards a proxy token (see 8.3.1.6.2.2) to
the third party (e.g., in a target descriptor in the parameter data of the EXTENDED COPY command).
The third party sends the access controls coordinator an ACCESS CONTROL OUT command with ASSIGN
PROXY LUN service action (see 8.3.3.11) specifying the proxy token to request creation of a proxy access
right to the referenced logical unit. The access controls coordinator determines the referenced logical unit
from the proxy token value. The third party is unaware of the exact logical unit to which it is requesting access.


The parameter data for the ACCESS CONTROL OUT command with ASSIGN PROXY LUN service action
includes the LUN value that the third party intends to use when accessing the referenced logical unit. The
resulting LUN value is called a proxy LUN. If the ACCESS CONTROL OUT command with ASSIGN PROXY
LUN service action is successful, the proxy LUN becomes the third party’s mechanism for accessing the
logical unit by proxy.
Once assigned, a proxy LUN shall remain valid until one of the following occurs:
a)
the third party releases the proxy LUN value using the ACCESS CONTROL OUT command with
RELEASE PROXY LUN service action (see 8.3.3.12);
b)
the proxy token is made invalid as described in 8.3.1.6.2.1; or
c)
a logical unit reset or I_T nexus loss of the I_T nexus used to assign the proxy LUN (see 8.3.1.12).
The third party may reissue the ACCESS CONTROL OUT command with ASSIGN PROXY LUN service
action in an attempt to re-establish its proxy access rights. If the cause of the proxy token becoming invalid
was temporary, the reissued command should succeed. The access controls coordinator shall process the
request as described in 8.3.1.6.2.1 without reference to any previous assignment of the proxy LUN value.
8.3.1.7 Verifying access rights
While access controls are enabled (see 8.3.1.2), access rights for an initiator port shall be validated as
described in this subclause.
Relationships between access controls and commands in a task set are described in 8.3.1.11.1.
All commands shall be processed as if access controls were not present if the ACL (see 8.3.1.3) allows the
initiator port access to the addressed logical unit as a result of one of the following conditions:
a)
the ACL contains an ACE containing a TransportID type access identifier (see 8.3.1.3.2) for the
initiator port and that ACE includes a LUACD with LUN value matching the addressed LUN;
b)
the initiator port is in the enrolled state (see 8.3.1.5.1.3) under an AccessID, the ACL contains an ACE
containing that AccessID as an access identifier, and that ACE includes a LUACD with LUN value
matching the addressed LUN; or
c)
the addressed LUN matches a proxy LUN value (see 8.3.1.6.2.2) assigned using the ACCESS
CONTROL OUT command with ASSIGN PROXY LUN service action (see 8.3.3.11) and the proxy
token (see 8.3.1.6.2.1) used to assign the proxy LUN value is still valid.
If the initiator port is in the pending-enrolled state (see 8.3.1.5.1.4) under an AccessID, the ACL contains an
ACE containing that AccessID as an access identifier, and that ACE includes a LUACD with LUN value
matching the addressed LUN, then commands shall be processed as follows:
a)
INQUIRY, REPORT LUNS, ACCESS CONTROL OUT and ACCESS CONTROL IN commands shall
be processed as if access controls were not present;
b)
a REQUEST SENSE command (see 6.39) shall be processed as if access controls were not present,
except in cases where parameter data containing pollable sense data (see 5.11.2) would be returned.
In these cases, device server shall terminate the REQUEST SENSE command with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST and the additional sense code set
to ACCESS DENIED - INITIATOR PENDING-ENROLLED; and
c)
any other command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to ACCESS DENIED - INITIATOR
PENDING-ENROLLED.


An application client should respond to the ACCESS DENIED - INITIATOR PENDING-ENROLLED additional
sense code by sending an ACCESS CONTROL OUT command with ACCESS ID ENROLL service action. If
the command succeeds, the application client may retry the terminated command.
If an INQUIRY command is addressed to a LUN for which there is no matching LUN value in any LUACD in
any ACE allowing the initiator port logical unit access rights, the standard INQUIRY data (see 6.6.2)
PERIPHERAL DEVICE TYPE field shall be set to 1Fh and PERIPHERAL QUALIFIER field shall be set to 011b (i.e., the
device server is not capable of supporting a device at this logical unit).
The parameter data returned in response to a REPORT LUNS command addressed to LUN 0 or to the
REPORT LUNS well known logical unit shall return only the list of LUN values that are associated to acces-
sible logical units according to the following criteria:
a)
if the initiator port is in the enrolled state or pending-enrolled state, the REPORT LUNS parameter
data shall include any LUN values found in LUACDs in the ACE containing the AccessID enrolled by
the initiator port;
b)
if the initiator port, in any enrollment state has a TransportID found in the access identifier of an ACE,
then the REPORT LUNS parameter data shall include any LUN values found in LUACDs in that ACE;
and
c)
if the initiator port, in any enrollment state has access to any proxy LUNs (see 8.3.1.6.2.2), then those
LUN values shall be included in the REPORT LUNS parameter data.
The parameter data returned in response to a REPORT LUNS command that describes well known logical
units shall not be affected by access controls.
If the initiator port is in the not-enrolled state and is not allowed access to any logical unit as result of its Trans-
portID or as a result of a proxy LUN assignment, then the REPORT LUNS parameter data shall include only
LUN 0 and well known logical units, as defined in 6.33.
Except while access controls are disabled, all cases not described previously in this subclause shall result in
termination of the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST,
and the additional sense code set to LOGICAL UNIT NOT SUPPORTED.
8.3.1.8 The management identifier key
8.3.1.8.1 Management identifier key usage
The management identifier key identifies the application that is responsible for managing access controls for a
SCSI target device. This identification occurs when the application client specifies a new management
identifier key value in each ACCESS CONTROL OUT command with the MANAGE ACL service action (see
8.3.3.2), and when the last specified management identifier key value appears in ACCESS CONTROL IN and
ACCESS CONTROL OUT service actions as required in 8.3.1.4.2.
To allow for failure scenarios where the management identifier key value has been lost, an override procedure
involving a timer is described in 8.3.1.8.2.
Use of the management identifier key has the following features:
a)
management of access controls is associated with those application clients that provide the correct
management identifier key without regard for the initiator port from which the command was received;
and
b)
only an application client that has knowledge of the management identifier key may change the ACL,
allowing the management of access controls to be limited to specific applications and application
clients.


8.3.1.8.2 Overriding the management identifier key
8.3.1.8.2.1 The OVERRIDE MGMT ID KEY service action
If the management identifier key needs to be replaced and the current management identifier key is not
available, then the ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action (see
8.3.3.8) may be used to force the management identifier key to a known value.
The ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action should be used only
for failure recovery. If failure recovery is not required, the ACCESS CONTROL OUT command with MANAGE
ACL service action should be used.
To protect the management identifier key from unauthorized overrides, the access controls coordinator shall
restrict use of the ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action based
on the value of the override lockout timer (see 8.3.1.8.2.2).
While the override lockout timer is not zero, an ACCESS CONTROL OUT command with OVERRIDE MGMT
ID KEY service action shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
While the override lockout timer is zero, an ACCESS CONTROL OUT command with OVERRIDE MGMT ID
KEY service action shall be processed as described in 8.3.3.8.
The access controls coordinator shall log the receipt of each ACCESS CONTROL OUT command with
OVERRIDE MGMT ID KEY service action and its success or failure as described in 8.3.1.10.
8.3.1.8.2.2 The override lockout timer
The access controls coordinator shall maintain the override lockout timer capable of counting up to 65 535
seconds. While the override lockout timer is not zero it shall be decreased by one nominally once per second
but no more frequently than once every 800 milliseconds until the value reaches zero. While the override
lockout timer is zero, it shall not be changed except as the result of commands sent by an application client.
The ACCESS CONTROL OUT command with MANAGE OVERRIDE LOCKOUT TIMER service action
manages the state of the override lockout timer (see 8.3.3.7), performing one of the following functions:
a)
if the incorrect management identifier key is supplied or if no parameter data is sent, the access
controls coordinator shall reset the override lockout timer to the last received initial override lockout
timer value; or
b)
if the correct management identifier key is supplied, then the access controls coordinator shall do the
following:
1)
save the initial override lockout timer value supplied in the parameter data; and
2)
reset the override lockout timer to the new initial value.
Setting the initial override lockout timer value to zero disables the override lockout timer and allows the
ACCESS CONTROL OUT command with OVERRIDE MGMT KEY service action to succeed at any time.
Any application that knows the management identifier key may establish an initial override lockout timer value
of sufficient duration (i.e., up to about 18 hours). Maintaining a non-zero override lockout timer value may be
accomplished without knowing the management identifier key or transporting the management identifier key
on a service delivery subsystem. Attempts to establish a zero initial override lockout timer value that are not
accompanied by the correct management identifier key result in decreasing the probability that a subsequent
ACCESS CONTROL OUT command with OVERRIDE MGMT ID KEY service action is able to succeed by
resetting the override lockout timer.


After a logical unit reset, the override lock timer shall be set to the initial override lockout timer value within ten
seconds of the non-volatile memory containing the initial override lockout timer value becoming available.
The ACCESS CONTROL IN command with REPORT OVERRIDE LOCKOUT TIMER may be used to
discover the state of the override lockout timer.
8.3.1.9 Reporting access control information
Specific service actions of the ACCESS CONTROL IN command may be used by an application client to
request a report from the access controls coordinator about its access controls data and state.
The ACCESS CONTROL IN command with REPORT ACL service action (see 8.3.2.2) returns the ACL (see
8.3.1.3). The information reported includes the following:
a)
the list of access identifiers (see 8.3.1.3.2) and the associated LUACDs (see 8.3.1.3.3) currently in
effect; and
b)
the list of proxy tokens (see 8.3.1.6.2.1) currently in effect.
The ACCESS CONTROL IN command with REPORT ACCESS CONTROLS LOG service action (see 8.3.2.4)
returns the contents of the access controls log (see 8.3.1.10).
The ACCESS CONTROL IN command with REPORT OVERRIDE LOCKOUT TIMER service action (see
8.3.2.5) reports on the state of the override lockout timer (see 8.3.1.8.2.2).
8.3.1.10 Access controls log
The access controls log is a record of events maintained by the access controls coordinator.
The access controls log has three portions, each recording a different class of events:
c)
invalid key events: mismatches between the management identifier key (see 8.3.1.8) specified by a
service action and the current value maintained by the access controls coordinator;
d)
key override events: attempts to override the management identifier key (see 8.3.1.8.2.1), whether
the attempt fails or succeeds; and
e)
ACL LUN conflict events: (see 8.3.1.5.2).
Each portion of the log is required to contain a saturating counter of the corresponding events. When a SCSI
target device is manufactured, all event counters shall be set to zero. While access controls are disabled, all
event counters except the Key Override events counter shall be set to zero. Each event counter shall be incre-
mented by one whenever the corresponding event occurs.
Each log portion may contain additional records with more specific information about each event. If the
resources for additional log records are exhausted, the access controls coordinator shall preserve the most
recently added log records in preference to older log records.
Log records contain a TIME STAMP field whose contents are vendor specific. If the access controls coordinator
has no time stamp resources the TIME STAMP field shall be set to zero. If time stamp values are provided, the
same timing clock and time stamp format shall be used for all access controls log entries.
Invalid key events occur whenever an access controls command requires the checking of an application client
supplied management identifier key against the current management identifier key saved by the access
controls coordinator and the two values fail to match. If such an event occurs, the access controls coordinator


shall increment the Invalid Keys events counter by one. If the log has additional resources to record event
details, the access controls coordinator shall add an invalid keys log record (containing the information
defined in 8.3.2.4.2.3) describing the event.
Key override events occur if the access controls coordinator receives the ACCESS CONTROL OUT
command with OVERRIDE MGMT KEY service action (see 8.3.3.8). If such an event occurs, the access
controls coordinator shall increment the Key Overrides events counter by one without regard for whether the
command succeeds or fails. If the log has additional resources to record event details, the access controls
coordinator shall add a key overrides log record (containing the information defined in 8.3.2.4.2.2) describing
the event.
ACL LUN conflict events occur as defined in 8.3.1.5.2. If such an event occurs, the access controls coordi-
nator shall increment the ACL LUN Conflicts events counter by one. If the log has additional resources to
record event details, the access controls coordinator shall add an ACL LUN conflicts log record (containing the
information defined in 8.3.2.4.2.4) describing the event.
Selected portions of the access controls log may be requested by an application client using the ACCESS
CONTROL IN command with REPORT ACCESS CONTROLS LOG service action (see 8.3.2.4). With the
exception of the key overrides portion, selected portions of the log may be cleared and the event counters
reset to zero using the ACCESS CONTROL OUT command with CLEAR ACCESS CONTROLS LOG service
action (see 8.3.3.6).
8.3.1.11 Interactions of access controls and other features
8.3.1.11.1 Task set management and access controls
Upon successful completion of an ACCESS CONTROL OUT command with MANAGE ACL service action
(see 8.3.3.2), the specified ACL (see 8.3.1.3) shall apply to all commands that subsequently enter the enabled
command state. Commands that have modified SCSI target device state information (e.g., media, mode
pages, and log pages) shall not be affected by an ACCESS CONTROL OUT command that subsequently
enters the enabled command state. Commands in the enabled command state that have not modified SCSI
target device state information may or may not be affected by an ACCESS CONTROL OUT command that
subsequently enters the enabled command state. The ACL in effect prior to the time at which the ACCESS
CONTROL OUT command with MANAGE ACL or DISABLE ACCESS CONTROLS service action entered the
enabled command state shall apply to all commands that are not affected by the ACCESS CONTROL OUT
command.
All the operations performed by a command shall complete under the control of a single ACL, either the state
in effect prior to processing of the ACCESS CONTROL OUT command or the state in effect following
processing of the ACCESS CONTROL OUT command. After a command enters the enabled command state
for the first time changing the access control state from disabled to enabled (see 8.3.1.2) shall have no effect
on the command.
Multiple access control commands, both ACCESS CONTROL IN and ACCESS CONTROL OUT, may be in
the task set concurrently. The order of processing of such commands is defined by the task set management
requirements (see SAM-5), but each command shall be processed as a single indivisible command without
any interleaving of actions that may be required by other access control commands.
8.3.1.11.2 Existing reservations and ACL changes
If a logical unit is reserved by one I_T nexus and that logical unit becomes accessible to another I_T nexus as
a result of an access control command, then there shall be no changes in the reservation of that logical unit.


If a logical unit is reserved by an I_T nexus and that logical unit becomes inaccessible to that I_T nexus as a
result of an access control command or other access control related event, then there shall be no changes in
the reservation. Existing persistent reservations mechanisms allow for other SCSI initiator devices with
access to that logical unit to clear the reservation.
8.3.1.12 Access controls information persistence and memory usage requirements
If a SCSI target device supports access controls, then the SCSI target device shall contain an access controls
coordinator that shall maintain the following information in nonvolatile memory:
a)
whether access controls are enabled or disabled; and
b)
the access controls data that table 667 and table 668 require to persist across power cycles, hard
resets, and logical unit resets.
If the access control coordinator’s nonvolatile memory is not ready and the access controls coordinator is
unable to determine that access controls are disabled, then the device servers for all logical units shall
terminate all commands except INQUIRY and REQUEST SENSE commands with CHECK CONDITION
status, with the sense key set to NOT READY, and the additional sense code set as described in table 334
(see 6.47). If a device server in any logical unit receives an INQUIRY command or a REQUEST SENSE
command while the access control coordinator’s nonvolatile memory is not ready and the access controls
coordinator is unable to determine that access controls are disabled, then the device server shall process the
command.
Following an I_T nexus loss, a previously enrolled initiator port shall be placed in the pending-enrolled state, if
that initiator port was associated with the lost I_T nexus. Following a logical unit reset, all previously enrolled
initiator ports shall be placed in the pending-enrolled state.
The information shown in table 667 shall be maintained by the access controls coordinator.
Table 667 — Mandatory access controls resources
Information Description
Size
(in bits)
Persistent
Across Power
Cycles, Hard
Resets, and
Logical Unit
Resets
One ACL (see 8.3.1.3) containing at least one ACE contain-
ing one access identifier (see 8.3.1.3.2), and at least one
LUACD (see 8.3.1.3.3)
VS
Yes
The Enrollment State for each initiator port (see 8.3.1.5.1)
VS
Yes
Management Identifier Key (see 8.3.1.8)
Yes
Default LUNs Generation (DLgeneration, see 8.3.1.4.4)
Yes
Override Lockout Timer (see 8.3.1.8.2.2)
No
Initial Override Lockout Timer value (see 8.3.1.8.2.2)
Yes
Access Controls Log Event Counters (see 8.3.1.10) contain-
ing at least the following:
a)
Key Override events counter;
b)
Invalid Key events counter; and
c)
ACL LUN Conflict events counter
Yes
Yes
Yes
Yes


Optionally, the access controls coordinator may maintain the information shown in table 668.
At the time of manufacturer, the ACL shall be empty, all values shown in table 667 shall be zero, additional
access control log structures shall be empty and there shall be no valid proxy tokens.
8.3.1.13 Access identifier formats
8.3.1.13.1 Access identifier type
The ACCESS IDENTIFIER TYPE field (see table 669) indicates the format and usage of the access identifier.
8.3.1.13.2 AccessID access identifiers
AccessID access identifiers shall have the format shown in table 670.
The ACCESSID field contains a value that identifies the AccessID type ACE in which the AccessID access
identifier appears. Within the ACL, no two ACEs shall contain the same AccessID.
Table 668 — Optional access controls resources
Information Description
Size
(in bits)
Persistent Across
Power Cycles,
Hard Resets, and
Logical Unit
Resets
One or more proxy tokens (see 8.3.1.6.2.1)
Yes
One or more proxy LUNs (see 8.3.1.6.2.2)
No
Access controls log event records (see 8.3.1.10) for:
a)
Key Override events;
b)
Invalid Key events; and
c)
ACL LUN Conflict events
(see 8.3.2.4.2.2)
(see 8.3.2.4.2.3)
(see 8.3.2.4.2.4)
Yes
Yes
Yes
Table 669 — ACCESS IDENTIFIER TYPE field
Code
Access Identifier Name
Reference
00h
AccessID
8.3.1.13.2
01h
TransportID
7.6.4
02h to 7Fh
Reserved
80h to FFh
Vendor specific
Table 670 — AccessID access identifier format
Bit
Byte
ACCESSID
•••
Reserved
•••
