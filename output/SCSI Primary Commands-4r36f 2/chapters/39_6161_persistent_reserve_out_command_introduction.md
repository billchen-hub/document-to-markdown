# 6.16.1 PERSISTENT RESERVE OUT command introduction

If the R_HOLDER bit is set to one (i.e., if the I_T nexus described by this full status descriptor is a reservation
holder), the SCOPE field and the TYPE field are as defined in the READ RESERVATION service action
parameter data (see 6.15.3). If the R_HOLDER bit is set to zero, the contents of the SCOPE field and the TYPE
field are not defined by this standard.
If the ALL_TG_PT bit set to zero, the RELATIVE TARGET PORT IDENTIFIER field is set to the relative port identifier of
the target port that is part of the I_T nexus described by this full status descriptor. If the ALL_TG_PT bit is set to
one, the contents of the RELATIVE TARGET PORT IDENTIFIER field are not defined by this standard.
The ADDITIONAL DESCRIPTOR LENGTH field indicates the number of bytes that follow in the descriptor (i.e., the
size of the TransportID).
The TransportID specifies a TransportID (see 7.6.4) identifying the initiator port that is part of the I_T nexus or
I_T nexuses described by this full status descriptor.
6.16 PERSISTENT RESERVE OUT command
6.16.1 PERSISTENT RESERVE OUT command introduction
The PERSISTENT RESERVE OUT command (see table 212) is used to request service actions that reserve
a logical unit for the exclusive or shared use of a particular I_T nexus. The command uses other service
actions to manage and remove such persistent reservations.
I_T nexuses performing PERSISTENT RESERVE OUT service actions are identified by a registered reser-
vation key provided by the application client. An application client may use the PERSISTENT RESERVE IN
command to obtain the reservation key, if any, for the I_T nexus holding a persistent reservation and may use
the PERSISTENT RESERVE OUT command to preempt that persistent reservation.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 212 for the PERSISTENT
RESERVE OUT command.
The SERVICE ACTION field is defined in 4.2.5.2 and 6.16.2.
Table 212 — PERSISTENT RESERVE OUT command
Bit
Byte
OPERATION CODE (5Fh)
Reserved
SERVICE ACTION
SCOPE
TYPE
Reserved
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
CONTROL


If a PERSISTENT RESERVE OUT command is attempted, but there are insufficient device server resources
to complete the operation, the command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INSUFFICIENT REGISTRATION
RESOURCES.
The PERSISTENT RESERVE OUT command contains fields that specify a persistent reservation service
action, the intended scope of the persistent reservation, and the restrictions caused by the persistent reser-
vation. The SCOPE field and TYPE field are defined in 6.15.3.3 and 6.15.3.4. If a SCOPE field specifies a scope
that is not implemented, the command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
Fields contained in the PERSISTENT RESERVE OUT parameter list specify the information required to
perform a particular persistent reservation service action.
The PARAMETER LIST LENGTH field specifies the number of bytes of parameter data for the PERSISTENT
RESERVE OUT command.
The parameter list shall be 24 bytes in length and the PARAMETER LIST LENGTH field shall contain 24 (18h), if
the following conditions are true:
a)
the SPEC_I_PT bit (see 6.16.3) is set to zero; and
b)
the service action is not REGISTER AND MOVE.
If the SPEC_I_PT bit is set to zero, the service action is not REGISTER AND MOVE, and the parameter list
length is not 24, then the command shall be terminated with CHECK CONDITION status, with the sense key
set to ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
If the parameter list length is larger than the device server is able to process, the command should be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to PARAMETER LIST LENGTH ERROR.
The CONTROL byte is defined in SAM-5.


6.16.2 PERSISTENT RESERVE OUT service actions
As part of processing the PERSISTENT RESERVE OUT service actions, the device server shall increment
the PRgeneration value as defined in 6.15.2.
The PERSISTENT RESERVE OUT command service actions are defined in table 213.
Table 213 — PERSISTENT RESERVE OUT service action codes
Code
Name
Description
PRGENERATION
field
incremented
(see 6.15.2)
Parameter
list format
00h
REGISTER
Register a reservation key with the device
server (see 5.13.7) or unregister a reser-
vation key (see 5.13.11.2.3).
Yes
Basic
(see 6.16.3)
01h
RESERVE
Creates a persistent reservation having a
specified SCOPE and TYPE (see 5.13.9).
The SCOPE and TYPE of a persistent reser-
vation are defined in 6.15.3.3 and
6.15.3.4.
No
Basic
(see 6.16.3)
02h
RELEASE
Releases the selected persistent reser-
vation (see 5.13.11.2.2).
No
Basic
(see 6.16.3)
03h
CLEAR
Clears all reservation keys (i.e., registra-
tions) and all persistent reservations (see
5.13.11.2.7).
Yes
Basic
(see 6.16.3)
04h
PREEMPT
Preempts persistent reservations and/or
removes registrations (see 5.13.11.2.4).
Yes
Basic
(see 6.16.3)
05h
PREEMPT
AND ABORT
Preempts persistent reservations and/or
removes registrations and aborts all
commands for all preempted I_T nexuses
(see 5.13.11.2.4 and 5.13.11.2.6).
Yes
Basic
(see 6.16.3)
06h
REGISTER
AND IGNORE
EXISTING KEY
Register a reservation key with the device
server (see 5.13.7) or unregister a reser-
vation key (see 5.13.11.2.3).
Yes
Basic
(see 6.16.3)
07h
REGISTER
AND MOVE
Register a reservation key for another I_T
nexus with the device server and move a
persistent reservation to that I_T nexus
(see 5.13.8)
Yes
Register and
move
(see 6.16.4)
08h
REPLACE
LOST
RESERVATION
Replace lost persistent reservation infor-
mation (see 5.13.11.3).
Yes
Basic
(see 6.16.3)
09h to
1Fh
Reserved
