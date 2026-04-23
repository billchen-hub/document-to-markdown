# 6.16.3 Basic PERSISTENT RESERVE OUT parameter list

6.16.3 Basic PERSISTENT RESERVE OUT parameter list
The parameter list format shown in table 214 shall be used by the PERSISTENT RESERVE OUT command
with any service action except the REGISTER AND MOVE service action. All fields shall be sent, even if the
field is not required for the specified service action and scope values.
The obsolete fields in bytes 16 to 19, byte 22 and byte 23 were defined in a previous standard.
The RESERVATION KEY field contains an 8-byte value provided by the application client to the device server to
identify the I_T nexus that is the source of the PERSISTENT RESERVE OUT command. The device server
shall verify that the contents of the RESERVATION KEY field in a PERSISTENT RESERVE OUT command
parameter data matches the registered reservation key for the I_T nexus from which the command was
received, except for:
a)
the REGISTER AND IGNORE EXISTING KEY service action where the RESERVATION KEY field shall
be ignored;
b)
the REGISTER service action for an unregistered I_T nexus where the RESERVATION KEY field shall
contain zero; and
c)
the REPLACE LOST RESERVATION service action where the RESERVATION KEY field shall contain
zero.
Except as noted above, if a PERSISTENT RESERVE OUT command specifies a RESERVATION KEY field other
than the reservation key registered for the I_T nexus, then the device server shall complete the command with
RESERVATION CONFLICT status. Except as noted above, the reservation key of the I_T nexus shall be
verified to be correct regardless of the SERVICE ACTION and SCOPE field values.
Table 214 — PERSISTENT RESERVE OUT parameter list
Bit
Byte
(MSB)
RESERVATION KEY
•••
(LSB)
(MSB)
SERVICE ACTION RESERVATION KEY
•••
(LSB)
Obsolete
•••
Reserved
SPEC_I_PT
ALL_TG_PT
Reserved
APTPL
Reserved
Obsolete
Additional parameter data
•••
n


The SERVICE ACTION RESERVATION KEY field contains information needed for the following service actions:
a)
REGISTER;
b)
REGISTER AND IGNORE EXISTING KEY;
c)
PREEMPT;
d)
PREEMPT AND ABORT; and
e)
REPLACE LOST RESERVATION.
The SERVICE ACTION RESERVATION KEY field is ignored for the following service actions:
a)
RESERVE;
b)
RELEASE; and
c)
CLEAR.
For the REGISTER service action and REGISTER AND IGNORE EXISTING KEY service action, the SERVICE
ACTION RESERVATION KEY field contains:
a)
the new reservation key to be registered in place of the registered reservation key; or
b)
zero to unregister the registered reservation key.
For the PREEMPT service action and PREEMPT AND ABORT service action, the SERVICE ACTION RESER-
VATION KEY field contains the reservation key of:
a)
the registrations to be removed; and
b)
if the SERVICE ACTION RESERVATION KEY field identifies a persistent reservation holder (see 5.13.10),
persistent reservations that are to be preempted.
For the REPLACE LOST RESERVATION service action, the SERVICE ACTION RESERVATION KEY field contains
the new reservation key to be registered
If the Specify Initiator Ports (SPEC_I_PT) bit is set to zero, the device server shall apply the registration only to
the I_T nexus that sent the PERSISTENT RESERVE OUT command. If the SPEC_I_PT bit is set to one for any
service action except the REGISTER service action, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST. If the SPEC_I_PT bit is set to one for the REGISTER service action,
then the additional parameter data (see table 215) shall include a list of transport IDs and the device server


shall also apply the registration to the I_T nexus for each initiator port specified by a TransportID. If a regis-
tration fails for any initiator port (e.g., if the logical unit does not have enough resources available to hold the
registration information), no registrations shall be made, and the command shall be terminated with CHECK
CONDITION status.
The TRANSPORTID PARAMETER DATA LENGTH field specifies the number of bytes of TransportIDs that follow.
The command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST:
a)
if the value in the PARAMETER LIST LENGTH field in the CDB does not include all of the additional
parameter list bytes specified by the TRANSPORTID PARAMETER DATA LENGTH field; or
b)
if the value in the TRANSPORTID PARAMETER DATA LENGTH field results in the truncation of a Trans-
portID.
The format of a TransportID is defined in 7.6.4.
The All Target Ports (ALL_TG_PT) bit is valid only for the REGISTER service action and the REGISTER AND
IGNORE EXISTING KEY service action, and shall be ignored for all other service actions. Support for the
ALL_TG_PT bit is optional. If the device server receives a REGISTER service action or a REGISTER AND
IGNORE EXISTING KEY service action with the ALL_TG_PT bit set to one, it shall create the specified regis-
tration on all target ports in the SCSI target device known to the device server (i.e., as if the same registration
request had been received individually through each target port). If the device server receives a REGISTER
service action or a REGISTER AND IGNORE EXISTING KEY service action with the ALL_TG_PT bit set to
zero, it shall apply the registration only to the target port through which the PERSISTENT RESERVE OUT
command was received. If a device server that does not support an ALL_TG_PT bit set to one receives that
value in a REGISTER service action or a REGISTER AND IGNORE EXISTING KEY service action, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
Table 215 — PERSISTENT RESERVE OUT specify initiator ports additional parameter data
Bit
Byte
TRANSPORTID PARAMETER DATA LENGTH (n-27)
•••
TransportIDs list
TransportID [first]
•••
•••
TransportID [last]
•••
n


The Activate Persist Through Power Loss (APTPL) bit is:
a)
valid only for the REGISTER service action, the REGISTER AND IGNORE EXISTING KEY service
action, and the REPLACE LOST RESERVATION service action; and
b)
shall be ignored for all other service actions.
Support for an APTPL bit equal to one is optional. If a device server that does not support an APTPL bit set to
one receives that value in a REGISTER service action, a REGISTER AND IGNORE EXISTING KEY service
action, or a REPLACE LOST RESERVATION service action, then the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
If the last valid APTPL bit value received by the device server is zero, the loss of power in the SCSI target
device shall release the persistent reservation for the logical unit and remove all registered reservation keys
(see 5.13.7). If the last valid APTPL bit value received by the device server is one, the logical unit shall retain
any persistent reservation(s) that may be present and all reservation keys (i.e., registrations) for all I_T
nexuses even if power is lost and later returned (see 5.13.5).
Table 216 summarizes which fields are set by the application client and interpreted by the device server for
each service action and scope value.
Table 216 — PERSISTENT RESERVE OUT service actions and valid parameters (part 1 of 2)
Service action
Allowed SCOPE
Parameters (part 1 of 2)
TYPE
RESERVATION
KEY
SERVICE ACTION
RESERVATION
KEY
APTPL
REGISTER
ignored
ignored
valid
valid
valid
REGISTER
AND IGNORE
EXISTING KEY
ignored
ignored
ignored
valid
valid
RESERVE
LU_SCOPE
valid
valid
ignored
ignored
RELEASE
LU_SCOPE
valid
valid
ignored
ignored
CLEAR
ignored
ignored
valid
ignored
ignored
PREEMPT
LU_SCOPE
valid
valid
valid
ignored
PREEMPT AND
ABORT
LU_SCOPE
valid
valid
valid
ignored
REGISTER
AND MOVE
LU_SCOPE
valid
valid
valid
not
applicable a
REPLACE
LOST
RESERVATION
LU_SCOPE
valid
valid
valid
valid
a The parameter list format for the REGISTER AND MOVE service action is described in 6.16.4.


Table 216 — PERSISTENT RESERVE OUT service actions and valid parameters (part 2 of 2)
Service action
Allowed
SCOPE
Parameters (part 2 of 2)
ALL_TG_PT
SPEC_I_PT
REGISTER
ignored
valid
valid
REGISTER
AND IGNORE
EXISTING KEY
ignored
valid
invalid
RESERVE
LU_SCOPE
ignored
invalid
RELEASE
LU_SCOPE
ignored
invalid
CLEAR
ignored
ignored
invalid
PREEMPT
LU_SCOPE
ignored
invalid
PREEMPT AND
ABORT
LU_SCOPE
ignored
invalid
REGISTER
AND MOVE
LU_SCOPE
not
applicable a
invalid
REPLACE
LOST
RESERVATION
LU_SCOPE
invalid
invalid
a The parameter list format for the REGISTER AND MOVE
service action is described in 6.16.4.
