# 6.16.4 Parameter list for the PERSISTENT RESERVE OUT command with REGISTER AND MOVE service action

6.16.4 Parameter list for the PERSISTENT RESERVE OUT command with REGISTER AND MOVE
service action
The parameter list format shown in table 217 shall be used by the PERSISTENT RESERVE OUT command
with REGISTER AND MOVE service action.
The RESERVATION KEY field contains an 8-byte value provided by the application client to the device server to
identify the I_T nexus that is the source of the PERSISTENT RESERVE OUT command. The device server
shall verify that the contents of the RESERVATION KEY field in a PERSISTENT RESERVE OUT command
parameter data matches the registered reservation key for the I_T nexus from which the command was
received. If a PERSISTENT RESERVE OUT command specifies a RESERVATION KEY field other than the
reservation key registered for the I_T nexus, the device server shall complete the command with RESER-
VATION CONFLICT status.
The SERVICE ACTION RESERVATION KEY field contains the reservation key to be registered to the specified I_T
nexus.
The Activate Persist Through Power Loss (APTPL) bit set to one is optional. If a device server that does not
support an APTPL bit set to one receives that value, it shall return CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the last valid APTPL bit value received by the device server is zero, the loss of power in the SCSI target
device shall release the persistent reservation for the logical unit and remove all registered reservation keys
(see 5.6.5). If the last valid APTPL bit value received by the device server is one, the logical unit shall retain any
persistent reservation(s) that may be present and all reservation keys (i.e., registrations) for all I_T nexuses
even if power is lost and later returned (see 5.13.5).
Table 217 — PERSISTENT RESERVE OUT with REGISTER AND MOVE service action parameter list
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
Reserved
Reserved
UNREG
APTPL
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
(MSB)
TRANSPORTID LENGTH (n-23)
•••
(LSB)
TransportID
•••
n


The unregister (UNREG) bit set to zero specifies that the device server shall not unregister the I_T nexus on
which the PERSISTENT RESERVE OUT command REGISTER AND MOVE service action was received. An
UNREG bit set to one specifies that the device server shall unregister the I_T nexus on which the PERSISTENT
RESERVE OUT command REGISTER AND MOVE service action was received.
The RELATIVE TARGET PORT IDENTIFIER field specifies the relative port identifier of the target port in the I_T
nexus to which the persistent reservation is to be moved.
The TRANSPORTID LENGTH field specifies the number of bytes of the TransportID that follow, shall be a
minimum of 24 bytes, and shall be a multiple of 4.
The TransportID specifies the initiator port in the I_T nexus to which the persistent reservation is to be moved.
The format of the TransportID is defined in 7.6.4.
The command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST:
a)
if the value in the PARAMETER LIST LENGTH field in the CDB does not include all of the parameter list
bytes specified by the TRANSPORTID LENGTH field; or
b)
if the value in the TRANSPORTID LENGTH field results in the truncation of a TransportID.
