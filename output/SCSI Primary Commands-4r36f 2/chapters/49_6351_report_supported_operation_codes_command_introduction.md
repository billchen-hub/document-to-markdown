# 6.35.1 REPORT SUPPORTED OPERATION CODES command introduction

The RELATIVE TARGET PORT IDENTIFIER field indicates the relative port identifier of the target port that is part of
the I_T_L nexus to which the current priority applies.
The ADDITIONAL DESCRIPTOR LENGTH field indicates the number of bytes that follow in the descriptor (i.e., the
size of the TransportID).
The TransportID specifies a TransportID (see 7.6.4) identifying the initiator port that is part of the I_T_L nexus
to which the current priority applies.
6.35 REPORT SUPPORTED OPERATION CODES command
6.35.1 REPORT SUPPORTED OPERATION CODES command introduction
The REPORT SUPPORTED OPERATION CODES command (see table 291) requests information on
commands the addressed logical unit supports. This command uses the MAINTENANCE IN CDB format (see
4.2.2.3.3). An application client may request a list of all operation codes and service actions supported by the
logical unit or the command support data for a specific command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 291 for the REPORT
SUPPORTED OPERATION CODES command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 291 for the REPORT
SUPPORTED OPERATION CODES command.
A return command timeouts descriptor (RCTD) bit set to one specifies that the command timeouts descriptor
(see 6.35.4) shall be included in each command descriptor (see 6.35.2) that is returned or in the
one_command parameter data (see 6.35.3) that is returned. A RCTD bit set to zero specifies that the command
timeouts descriptor shall not be returned.
Table 291 — REPORT SUPPORTED OPERATION CODES command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (0Ch)
RCTD
Reserved
REPORTING OPTIONS
REQUESTED OPERATION CODE
(MSB)
REQUESTED SERVICE ACTION
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The REPORTING OPTIONS field (see table 292) specifies the information to be returned in the parameter data.
The REQUESTED OPERATION CODE field specifies the operation code of the command to be returned in the
one_command parameter data format (see 6.35.3).
The REQUESTED SERVICE ACTION field specifies the service action of the command to be returned in the
one_command parameter data format.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
Table 292 — REPORT SUPPORTED OPERATION CODES REPORTING OPTIONS field
Code
Description
Parameter data
reference
000b
A list of all operation codes and service actions a supported by the logical
unit shall be returned in the all_commands parameter data format. The
REQUESTED OPERATION CODE CDB field and REQUESTED SERVICE ACTION
CDB field shall be ignored.
6.35.2
001b
The command support data for the operation code specified in the
REQUESTED OPERATION CODE field shall be returned in the one_command
parameter data format. The REQUESTED SERVICE ACTION CDB field shall be
ignored. If the REQUESTED OPERATION CODE field specifies an operation
code that has service actions a, then the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.35.3
010b
The command support data for the operation code and service action a
specified in the REQUESTED OPERATION CODE CDB field and REQUESTED
SERVICE ACTION CDB field shall be returned in the one_command
parameter data format. If the REQUESTED OPERATION CODE CDB field
specifies an operation code that does not have service actions a, then the
command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN CDB.
6.35.3
011b to
111b
Reserved
a The device server should also process the following fields in the following commands as specifying
service actions (i.e., the specified field should be processed as a SERVICE ACTION field):
a)
the MODE field in the READ BUFFER command (see 6.18); and
b)
the MODE field in the WRITE BUFFER command (see 6.49).


6.35.2 All_commands parameter data format
The REPORT SUPPORTED OPERATION CODES all_commands parameter data format (see table 293)
begins with a four-byte header that contains the length in bytes of the parameter data followed by a list of
supported commands. Each command descriptor contains information about a single supported command
CDB (i.e., one operation code and service action combination, or one non-service-action operation code). The
list of command descriptors shall contain all commands supported by the logical unit.
The COMMAND DATA LENGTH field indicates the length in bytes of the command descriptor list. The contents of
the COMMAND DATA LENGTH field are not altered based on the allocation length (see 4.2.5.6).
Each command descriptor (see table 294) contains information about a single supported command CDB.
The OPERATION CODE field indicates the operation code of a command supported by the logical unit.
Table 293 — All_commands parameter data
Bit
Byte
(MSB)
COMMAND DATA LENGTH (n-3)

•••
 (LSB)
Command descriptors
Command descriptor 0 (see table 294)
•••
•••
Command descriptor x (see table 294)
•••
n
Table 294 — Command descriptor format
Bit
Byte
OPERATION CODE
Reserved
(MSB)
SERVICE ACTION
(LSB)
Reserved
Reserved
CTDP
SERVACTV
(MSB)
CDB LENGTH
(LSB)
Command timeouts descriptor, if any (see 6.35.4)

•••
