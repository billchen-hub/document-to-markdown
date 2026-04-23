# 6.35.3 One_command parameter data format

The SERVICE ACTION field indicates a supported service action of the supported operation code indicated by
the OPERATION CODE field. If the operation code indicated in the OPERATION CODE field does not have any
service actions, the SERVICE ACTION field shall be set to 00h.
A command timeouts descriptor present (CTDP) bit set to one indicates that the command timeouts descriptor
(see 6.35.4) is included in this command descriptor. A CTDP bit set to zero indicates that the command
timeouts descriptor is not included in this command descriptor.
A service action valid (SERVACTV) bit set to zero indicates the operation code indicated by the OPERATION CODE
field does not have service actions and the SERVICE ACTION field contents are reserved. A SERVACTV bit set to
one indicates the operation code indicated by the OPERATION CODE field has service actions and the contents
of the SERVICE ACTION field are valid.
The CDB LENGTH field indicates the length of the command CDB in bytes for the operation code indicated in the
OPERATION CODE field, and if the SERVACTV bit is set to the service action indicated by the SERVICE ACTION field.
If the RCTD bit is set to one in the REPORT SUPPORTED OPERATION CODES CDB (see 6.35.1), the
command timeouts descriptor (see table 297 in 6.35.4) shall be included. If the RCTD bit is set to zero, the
command timeouts descriptor shall not be included.
6.35.3 One_command parameter data format
The REPORT SUPPORTED OPERATION CODES one_command parameter data format (see table 295)
contains information about the CDB and a usage map for bits in the CDB for the command specified by the
REPORTING OPTIONS, REQUESTED OPERATION CODE, and REQUESTED SERVICE ACTION fields in the REPORT
SUPPORTED OPERATION CODES CDB.
A command timeouts descriptor present (CTDP) bit set to one indicates that the command timeouts descriptor
(see 6.35.4) is included in the parameter data. A CTDP bit set to zero indicates that the command timeouts
descriptor is not included in the parameter data.
Table 295 — One_command parameter data
Bit
Byte
Reserved
CTDP
Reserved
SUPPORT
(MSB)
CDB SIZE (n-3)
(LSB)
CDB USAGE DATA
•••
n
n+1
Command timeouts descriptor, if any (see 6.35.4)
•••
n+12


The SUPPORT field is defined in table 296.
The CDB SIZE field indicates the size of the CDB USAGE DATA field in the parameter data, and the number of
bytes in the CDB for command being queried (i.e., the command specified by the REPORTING OPTIONS,
REQUESTED OPERATION CODE, and REQUESTED SERVICE ACTION fields in the REPORT SUPPORTED
OPERATION CODES CDB).
The CDB USAGE DATA field contains information about the CDB for the command being queried. The first byte
of the CDB USAGE DATA field shall contain the operation code for the command being queried. If the command
being queried contains a service action, then that service action code shall be placed in the CDB USAGE DATA
field in the same location as the SERVICE ACTION field of the command CDB. All other bytes of the CDB USAGE
DATA field shall contain a usage map for bits in the CDB for the command being queried.
The bits in the usage map shall have a one-for-one correspondence to the CDB for the command being
queried. If the device server evaluates a bit in the CDB for the command being queried, the usage map shall
contain a one in the corresponding bit position. If any bit representing part of a field is returned as one, all bits
for the field shall be returned as one. If the device server ignores or treats as reserved a bit in the CDB for the
command being queried, the usage map shall contain a zero in the corresponding bit position. The usage map
bits for a given CDB field all shall have the same value.
For example, the CDB usage bit map for the REPORT SUPPORTED OPERATION CODES command is: A3h,
0Ch, 87h, FFh, FFh, FFh, FFh, FFh, FFh, FFh, 00h, 07h. This example assumes that the logical unit only
supports the low-order three bits of the CDB CONTROL byte. The first byte contains the operation code, and the
second byte contains three reserved bits and the service action. The remaining bytes contain the usage map.
If the RCTD bit is set to one in the REPORT SUPPORTED OPERATION CODES CDB (see 6.35.1), the
command timeouts descriptor (see table 297 in 6.35.4) shall be included. If the RCTD bit is set to zero, the
command timeouts descriptor shall not be included.
Table 296 — SUPPORT values
Support
Description
000b
Data about the requested SCSI command is not currently available. All data after
byte 1 is not valid. A subsequent request for command support data may be suc-
cessful.
001b
The device server does not support the requested command. All data after byte 1 is
undefined.
010b
Reserved
011b
The device server supports the requested command in conformance with a SCSI
standard. The parameter data format conforms to the definition in table 295.
100b
Reserved
101b
The device server supports the requested command in a vendor specific manner.
The parameter data format conforms to the definition in table 295.
110b to 111b
Reserved
