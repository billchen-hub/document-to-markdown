# 6.4.5 CSCD descriptors

6.4.5 CSCD descriptors
6.4.5.1 CSCD descriptors introduction
The descriptor type code (see table 130) values for CSCD descriptors are shown in table 131.
Table 131 — EXTENDED COPY CSCD descriptor type codes
Descriptor
type a
Name
Size
(bytes)
Reference
E0h
Fibre Channel N_Port_Name CSCD descriptor
7.6.3.2
E1h
Fibre Channel N_Port_ID CSCD descriptor
7.6.3.3
E2h
Fibre Channel N_Port_ID With N_Port_Name
Checking CSCD descriptor
7.6.3.4
E3h
Parallel Interface T_L CSCD descriptor
7.6.3.5
E4h
Identification Descriptor CSCD descriptor
6.4.5.6
E5h
IPv4 CSCD descriptor
7.6.3.8
E6h
Alias CSCD descriptor
6.4.5.7
E7h
RDMA CSCD descriptor
7.6.3.7
E8h
IEEE 1394 EUI-64 CSCD descriptor
7.6.3.6
E9h
SAS Serial SCSI Protocol CSCD descriptor
7.6.3.10
EAh
IPv6 CSCD descriptor
7.6.3.9
EBh
IP Copy Service CSCD descriptor
6.4.5.8
ECh to FDh
Reserved for CSCD descriptors
FEh
ROD CSCD descriptor b
6.4.5.9
a A copy manager may not support all CSCD descriptor types, however, the copy manager
shall list all supported CSCD descriptor types in the Third-party Copy VPD page Supported
Descriptors descriptor (see 7.8.17.6), and in the response to the RECEIVE COPY
OPERATING PARAMETERS command (see 6.22).
b A copy manager that implements the ROD CSCD descriptor shall implement:
a)
the following third-party copy descriptors in the Third-party Copy VPD page:
A)
the ROD Features third-party copy descriptor (see 7.8.17.8); and
B)
the Supported ROD Types third-party copy descriptor (see 7.8.17.9);
and
b)
at least one of the following segment descriptors:
A)
the Populate a ROD from one or more block device ranges (see 6.4.6.20); or
B)
the Populate a ROD from one block device range (see 6.4.6.21).


All CSCD descriptors (see table 132) are a multiple 32 bytes in length and begin with a four-byte header
containing the DESCRIPTOR TYPE CODE field that specifies the format of the descriptor. If a copy manager
receives an unsupported descriptor type code in a CSCD descriptor, then the copy operation (see 5.17.4.3)
originated by the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to UNSUPPORTED TARGET DESCRIPTOR TYPE
CODE.
The DESCRIPTOR TYPE CODE field is described in 6.4.4.
The LU ID TYPE field (see table 133) specifies the interpretation of the LU IDENTIFIER field in CSCD descriptors
that contain a LU IDENTIFIER field.
Support for LU ID type codes other than 00b is optional. If a copy manager receives an unsupported value in
the LU ID TYPE field, then the copy operation (see 5.17.4.3) originated by the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST.
If the LU ID TYPE field specifies that the LU IDENTIFIER field contains a logical unit number, then the LU IDENTIFIER
field specifies the logical unit within the SCSI device specified by other fields in the CSCD descriptor that shall
be the copy source or copy destination.
If the LU ID TYPE field specifies that the LU IDENTIFIER field contains a proxy token (see 8.3.1.6.2), then the copy
manager shall use the LU IDENTIFIER field contents to obtain proxy access rights to the logical unit associated
with the proxy token. The logical unit number that represents the proxy access rights shall be the copy source
or copy destination.
Table 132 — CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E0h to FEh)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
CSCD descriptor parameters
•••
Device type specific parameters
•••
Zero or more CSCD descriptor extensions
(see 6.4.5.2)
•••
n
Table 133 — LU ID TYPE field
Code
LU IDENTIFIER field contents
Reference
00b
Logical Unit Number
SAM-5
01b
Proxy Token
8.3.1.6.2
10b to 11b
Reserved


The copy manager should obtain a LUN value for addressing this logical unit by sending an ACCESS
CONTROL OUT command with ASSIGN PROXY LUN service action (see 8.3.3.11) to the access controls
coordinator of the SCSI target device that is specified by other fields in the CSCD descriptor. The copy
manager shall use a LUN assigned on the basis of a proxy token only for those commands that are necessary
for the processing of the EXTENDED COPY command whose parameter data contains the proxy token. After
the copy manager has completed EXTENDED COPY commands involving a proxy token, the copy manager
should release the LUN value using an ACCESS CONTROL OUT command with RELEASE PROXY LUN
service action (see 8.3.3.12).
EXTENDED COPY access to proxy logical units is to be accomplished only if the LU ID TYPE field is set to 01b.
If the copy manager receives a CSCD descriptor containing LU ID type 00b and a logical unit number
matching a LUN value that the copy manager has obtained using an ACCESS CONTROL OUT command
with ASSIGN PROXY LUN service action, then the copy operation (see 5.17.4.3) originated by the
EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the sense key set to
COPY ABORTED, and the additional sense code set to COPY TARGET DEVICE NOT REACHABLE.
The PERIPHERAL DEVICE TYPE field is described in 6.6.2. The value in the PERIPHERAL DEVICE TYPE field (see
table 132) specifies the format of the device type specific parameters. The device type specific parameters
convey information specific to the type of device specified by the CSCD descriptor.
Table 134 lists the peripheral device type code values having formats defined for the device type specific
parameters in a CSCD descriptor. Peripheral device types with code values not listed in table 134 are
reserved in all PERIPHERAL DEVICE TYPE fields in the EXTENDED COPY parameter list.
The RELATIVE INITIATOR PORT IDENTIFIER field specifies the relative port identifier of the initiator port within the
SCSI device that the copy manager shall use to access the logical unit described by the CSCD descriptor, if
such access requires use of an initiator port (i.e., if the logical unit is in the same SCSI device as the copy
manager, the RELATIVE INITIATOR PORT IDENTIFIER field is ignored). A RELATIVE INITIATOR PORT IDENTIFIER field
set to zero specifies that the copy manager may use any initiator port or ports within the SCSI device.
The copy manager may, as part of processing a segment descriptor, verify the information in a CSCD
descriptor’s device specific fields. However, while verifying the information, the copy manager shall not issue
any commands that change the position of read/write media on the CSCD without returning the media to its
original position. Any errors encountered while verifying the information shall be processed as described in
5.17.7.4.
CSCD descriptor extensions increase the length of a CSCD descriptor as described in 6.4.5.2.
Table 134 — Device type specific parameters in CSCD descriptors
Peripheral
Device Type
Reference
Description
Shorthand
00h, 04h, 05h, 07h, and 0Eh
6.4.5.3
Block devices
Block
01h
6.4.5.4
Sequential-access devices
Stream or Tape
03h
6.4.5.5
Processor devices a
Stream
a This standard defines the use of the processor device type (i.e., 03h) only for the
interactions between copy managers.


6.4.5.2 The CSCD descriptor extension
A CSCD descriptor (see 6.4.5.1) is extended by appending one or more CSCD descriptor extensions (see
table 135) to it. A CSCD descriptor extension is 32 bytes in length and begins with a one-byte header
containing the descriptor type code value that identifies the descriptor as a CSCD descriptor extension (i.e.,
FFh).
The EXTENSION DESCRIPTOR TYPE CODE field is a descriptor type code value (see 6.4.4), and shall be set to the
value shown in table 135 for each CSCD descriptor extension.
The CSCD descriptor specific information contains data that extends the CSCD descriptor or CSCD descriptor
extension located adjacent to and preceding this CSCD descriptor extension.
If a SOURCE CSCD DESCRIPTOR ID field or a DESTINATION CSCD DESCRIPTOR ID field in a segment descriptor (see
6.4.6.1) references a CSCD descriptor extension (i.e, a descriptor with the descriptor type code set to FFh),
then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated
with CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code
set to INVALID FIELD IN PARAMETER LIST.
6.4.5.3 Device type specific CSCD descriptor parameters for block device types
The format for the device type specific CSCD descriptor parameters for block device types (i.e., device type
code values 00h, 04h, 05h, 07h, and 0Eh) is shown in table 136.
The PAD bit is used in conjunction with the CAT bit (see 6.4.6.1) in the segment descriptor to determine what
action should be taken if a segment of the copy does not fit exactly into an integer number of destination
blocks (see 5.17.7.2).
The DISK BLOCK LENGTH field is set to the number of bytes in a disk block, excluding any protection information
(see SBC-2), for the logical unit being addressed.
If the DISK BLOCK LENGTH field is set to zero and the PERIPHERAL DEVICE TYPE field (see 6.4.5.1) is set to 00h,
then the copy manager shall determine the block size of the CSCD logical unit (e.g., by sending a READ
Table 135 — CSCD descriptor extension format
Bit
Byte
EXTENSION DESCRIPTOR TYPE CODE (FFh)
CSCD descriptor specific information
•••
Table 136 — Device type specific CSCD descriptor parameters for block device types
Bit
Byte
Reserved
PAD
Reserved
(MSB)
DISK BLOCK LENGTH
(LSB)


CAPACITY command (see SBC-3)), and use the result wherever the use of the DISK BLOCK LENGTH field is
required by this standard.
The copy manager may read ahead from copy sources of the block device type (i.e., the copy manager may
perform reads from a copy source block device at any time and in any order during processing of an
EXTENDED COPY command), provided that the relative order of writes and reads on the same blocks within
the same CSCD descriptor does not differ from their order in the segment descriptor list (see 5.17.7.1).
6.4.5.4 Device type specific CSCD descriptor parameters for sequential-access device types
The format for the device type specific CSCD descriptor parameters for the sequential-access device type
(i.e., device type code value 01h) operating in the implicit address mode (see SSC-4) is shown in table 137.
The contents of the FIXED bit and STREAM BLOCK LENGTH field are combined with the STREAM DEVICE TRANSFER
LENGTH FIELD in the segment descriptor to determine the length of the stream read or write as defined in table
138.
The PAD bit is used in conjunction with the CAT bit (see 5.17.7.2) in the segment descriptor to determine what
action should be taken if a segment of the copy does not fit exactly into an integer number of destination
blocks (see 5.17.7.2).
All read commands issued to sequential-access type devices shall have the SILI bit set to zero.
Table 137 — Device type specific CSCD descriptor parameters for sequential-access device types
Bit
Byte
Reserved
PAD
Reserved
FIXED
(MSB)
STREAM BLOCK LENGTH
(LSB)
Table 138 — Stream device transfer lengths
FIXED
bit
STREAM BLOCK
LENGTH field
Description
000000h
Use variable length reads or writes. The number of bytes for each read or write
is specified by the STREAM DEVICE TRANSFER LENGTH field in the segment
descriptor.
000001h to
FFFFFFh
The command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
000000h
The command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST
000001h to
FFFFFFh
Use fixed record length reads or writes. The number of bytes for each read or
write shall be the product of the STREAM BLOCK LENGTH field and the STREAM
DEVICE TRANSFER LENGTH field in the segment descriptor.


The copy manager shall not read ahead from copy sources of the stream device type (i.e., the reads required
by a segment descriptor for which the copy source is a stream device shall not be started until all writes for
previous segment descriptors have completed).
6.4.5.5 Device type specific CSCD descriptor parameters for processor device types
The format for the device type specific CSCD descriptor parameters for the processor device type (i.e., device
type code value 03h) is shown in table 139.
The PAD bit is used in conjunction with the CAT bit (see 5.17.7.2) in the segment descriptor to determine what
action should be taken if a segment of the copy does not fit exactly into an integer number of EXTENDED
COPY(LID4) commands (see 6.4), EXTENDED COPY(LID1) commands (see 6.5), RECEIVE COPY
DATA(LID1) commands (see 6.21), or RECEIVE COPY DATA(LID4) commands (see 6.20).
If the processor device is a copy source, the number of bytes to be transferred by an EXTENDED COPY
command shall be specified by STREAM DEVICE TRANSFER LENGTH field in the segment descriptor. If the
processor device is a copy destination, the number of bytes to be transferred by an EXTENDED COPY
command and subsequent RECEIVE COPY DATA command shall be specified by STREAM DEVICE TRANSFER
LENGTH field in the segment descriptor.
Table 139 — Device type specific CSCD descriptor parameters for processor device types
Bit
Byte
Reserved
PAD
Reserved
Reserved
•••


6.4.5.6 Identification Descriptor CSCD descriptor format
The CSCD descriptor format shown in table 140 instructs the copy manager to locate a SCSI target device
and logical unit that returns a Device Identification VPD page (see 7.8.6) containing an Identification
descriptor having the field specified values in the CODE SET field, ASSOCIATION field, DESIGNATOR TYPE field,
IDENTIFIER LENGTH field, and DESIGNATOR field. The copy manager may use any SCSI transport protocol (see
SAM-5), target port identifier (see SAM-5) and logical unit number (see SAM-5) values that result in matching
VPD field values to address the logical unit. If multiple combinations of SCSI transport protocols, target port
identifiers, and logical unit numbers access matching VPD field values, the copy manager may use any
combination to address the logical unit and shall try other combinations in the event that one combination
becomes non-operational during the processing of an EXTENDED COPY command.
The DESCRIPTOR TYPE CODE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT IDENTIFIER field, and
the device type specific parameters are described in 6.4.5.1. The DESCRIPTOR TYPE CODE field shall be set as
shown in table 140 for the Identification Descriptor CSCD descriptor.
The LU ID TYPE field shall be ignored in the Identification Descriptor CSCD descriptor.
The CODE SET field contains a code set enumeration (see 4.3.3) that indicates the format of the DESIGNATOR
field.
The contents of the ASSOCIATION field, DESIGNATOR TYPE field, and DESIGNATOR LENGTH field are described in
7.8.6.1. The designator length shall be 20 or less.
The DESIGNATOR field is a fixed-length zero-padded (see 4.3.2) field that has the DESIGNATOR field format
defined in 7.8.6.
Some combinations of code set, association, designator type, designator length and designator do not
uniquely identify a logical unit to serve as a CSCD. The behavior of the copy manager if such combinations
are specified is unpredictable.
Table 140 — Identification Descriptor CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E4h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
Reserved
CODE SET
Reserved
ASSOCIATION
DESIGNATOR TYPE
Reserved
DESIGNATOR LENGTH
DESIGNATOR
•••
Device type specific parameters
•••


6.4.5.7 Alias CSCD descriptor format
The CSCD descriptor format shown in table 141 instructs the copy manager to locate a SCSI target port and
logical unit using the alias list designation associated with the specified alias value. The alias list is maintained
using the CHANGE ALIASES command (see 6.2).
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The DESCRIPTOR TYPE CODE
field shall be set as shown in table 141 for the Alias CSCD descriptor.
The ALIAS VALUE field specifies an alias value in the alias list as managed by the CHANGE ALIASES
command (see 6.2) and maintained by the device server.
When the copy manager first processes an Alias CSCD descriptor, it shall check the value of the ALIAS VALUE
field for a corresponding entry in the alias list. If the value is not in the alias list or the copy manager is unable
to validate the designation (see 6.2.3) associated with the alias value, the copy operation (see 5.17.4.3) origi-
nated by the command shall be terminated because the CSCD is unreachable (see 5.17.7.4). An application
client generating EXTENDED COPY commands that include Alias CSCD descriptors in the parameter list is
responsible for providing a valid entry in the alias list using the CHANGE ALIASES command (see 6.2) prior to
sending the EXTENDED COPY command.
Table 141 — Alias CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E6h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
ALIAS VALUE
•••
Reserved
•••
Device type specific parameters
•••


6.4.5.8 IP Copy Service CSCD descriptor
The CSCD descriptor format shown in table 142 instructs the copy manager to communicate with the copy
service specified in the IP ADDRESS field to locate the CSCD that returns a Device Identification VPD page (see
7.8.6) containing an Identification descriptor having the specified CODE SET field, ASSOCIATION field, DESIG-
NATOR TYPE field, DESIGNATOR LENGTH field, and DESIGNATOR field values.
The protocol used by the copy manager to communicate with the copy service is vendor specific.
The DESCRIPTOR TYPE CODE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT IDENTIFIER field, and
the device type specific parameters are described in 6.4.5.1. The DESCRIPTOR TYPE CODE field shall be set as
shown in table 142 for the IP Copy Service CSCD descriptor.
The LU ID TYPE field shall be ignored in the IP Copy Service CSCD descriptor.
Table 142 — IP Copy Service CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (EBh)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
Reserved
IPTYPE
Reserved
•••
(MSB)
COPY SERVICE IP ADDRESS
•••
(LSB)
Device type specific parameters
EXTENSION DESCRIPTOR TYPE CODE (FFh)
Reserved
(MSB)
COPY SERVICE PORT NUMBER
(LSB)
(MSB)
COPY SERVICE INTERNET PROTOCOL NUMBER
(LSB)
Reserved
CODE SET
Reserved
ASSOCIATION
DESIGNATOR TYPE
Reserved
DESIGNATOR LENGTH
DESIGNATOR
•••


If the IPTYPE bit is set to zero, the COPY SERVICE IP ADDRESS field shall contain a zero-padded IPv4 address
(see RFC 791). If the IPTYPE bit is set to one, the COPY SERVICE IP ADDRESS field shall contain a unicast IPv6
address (see RFC 4291).
The COPY SERVICE IP ADDRESS field is set to the IP address of the copy service in the format specified by the
IPTYPE bit.
The EXTENSION DESCRIPTOR TYPE CODE field is described in 6.4.5.2. If the EXTENSION DESCRIPTOR TYPE CODE
field does not contain the value shown in table 142, then the copy manager shall terminate the EXTENDED
COPY command with CHECK CONDITION status, with the sense key set to COPY ABORTED, and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
The COPY SERVICE PORT NUMBER field shall contain the TCP port number.
The COPY SERVICE INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number.
The contents of the COPY SERVICE IP ADDRESS field, the COPY SERVICE PORT NUMBER field, and the COPY
SERVICE INTERNET PROTOCOL NUMBER field may be obtained using the network service descriptor with the
SERVICE TYPE field set to 06h (i.e., copy service) in Management Network Addresses VPD page (see 7.8.8)
returned by the logical unit that returns a Device Identification VPD page (see 7.8.6) containing an Identifi-
cation descriptor having the specified CODE SET field, ASSOCIATION field, DESIGNATOR TYPE field, DESIGNATOR
LENGTH field, and DESIGNATOR field values.
The CODE SET field contains a code set enumeration (see 4.3.3) that indicates the format of the DESIGNATOR
field.
The contents of the ASSOCIATION field, DESIGNATOR TYPE field, and DESIGNATOR LENGTH field are described in
7.8.6.1. The designator length shall be 20 or less.
The DESIGNATOR field is a fixed-length zero-padded (see 4.3.2) field that has the DESIGNATOR field format
defined in 7.8.6.
Some combinations of code set, association, designator type, designator length and designator do not
uniquely identify a logical unit to serve as a CSCD. The behavior of the copy manager if such combinations
are specified is unpredictable.


6.4.5.9 ROD CSCD descriptor
The CSCD descriptor format shown in table 143 instructs the copy manager to use the specified ROD as a
copy source or copy destination. If the ROD represents no data when the copy manager begins processing
the EXTENDED COPY command (e.g., the ROD TYPE field is not set to zero), then the copy manager shall
allow the ROD to be populated as defined in 5.17.7.5.2. If a segment descriptor attempts to use an unpopu-
lated ROD as a copy source or copy destination, the copy operation (see 5.17.4.3) originated by the
command shall be terminated as if an unreachable CSCD had been encountered (see 5.17.7.4).
The DESCRIPTOR TYPE CODE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT IDENTIFIER field, and
the device type specific parameters are described in 6.4.5.5. The DESCRIPTOR TYPE CODE field shall be set as
shown in table 143 for the ROD CSCD descriptor.
Table 143 — ROD CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (FEh)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
(MSB)
ROD PRODUCER CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
ROD TYPE

•••
(LSB)
(MSB)
REQUESTED ROD TOKEN LIFETIME

•••
(LSB)
(MSB)
REQUESTED ROD TOKEN INACTIVITY TIMEOUT

•••
(LSB)
Reserved

Reserved
R_TOKEN
Reserved
DEL_TKN
ROD TOKEN OFFSET

•••

Device type specific parameters
•••


The LU ID TYPE field shall be ignored in the ROD CSCD descriptor.
If the ROD TYPE field is set to zero, then:
a)
the PERIPHERAL DEVICE TYPE field shall be ignored; and
b)
the peripheral device type of the ROD CSCD descriptor shall be the peripheral device type specified
by the ROD token that is specified by the ROD TOKEN OFFSET field.
The ROD PRODUCER CSCD DESCRIPTOR ID field specifies the CSCD device (see table 148 in 6.4.6.1) that
contains the logical unit that contains the copy manager that:
a)
created the ROD token that is specified by the ROD TOKEN OFFSET field, if the ROD TYPE field is set to
zero; or
b)
creates the ROD token that is created during processing of the EXTENDED COPY command, if the
ROD TYPE field is not set to zero.
The ROD TYPE field (see table 110 in 5.17.6.2.1) specifies the type of ROD begin populated or referenced by a
ROD token.
For all ROD types (see 5.17.6.2), access to the bytes within a ROD is established by specifying:
a)
the identifier of a ROD CSCD descriptor that describes the ROD for the duration of the copy operation
(see 5.17.4.3) originated by an EXTENDED COPY command; or
b)
that a ROD token be created that allows the copy manager that creates the ROD token creator to
identify and access the bytes represented by the ROD across multiple third-party copy commands.
Methods are available to create a ROD token from a ROD identifier and create a ROD identifier from a ROD
token (see 5.17.7.5.1).


Fields in the ROD CSCD descriptor and fields in the ROD Features third-party copy descriptor (see 7.8.17.8)
in the Third-party Copy VPD page that affect the processing of the ROD PRODUCER CSCD DESCRIPTOR ID field
are shown in table 144.
Table 144 — Inputs that affect the processing of the ROD PRODUCER CSCD DESCRIPTOR ID field
ROD
PRODUCER
CSCD
DESCRIPTOR
ID field
R_TOKEN
bit
ROD TYPE
field
REMOTE
TOKENS
field a
Description
n/a
zero
n/a
the command shall be terminated b
FFFFh
n/a
n/a
process the command
not zero
n/a
process the command
F800h
0 or 1
not zero
n/a
the command shall be terminated b
zero
local c
n/a
process the command
zero
remote c
0h
remote ROD tokens not supported d
4h
process the command
Others e
not zero
0h
remote ROD tokens not supported d
4h
the command shall be terminated b
zero
0h
remote ROD tokens not supported d
4h
process the command
not zero
0h
remote ROD tokens not supported d
4h
remote ROD token creation not supported f
6h
process the command
a Refers to the REMOTE TOKENS field is in the ROD Features third-party copy descriptor (see 7.8.17.8).
b The copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
c Processing depends on the copy manager that created the ROD token specified by the ROD TOKEN
OFFSET field as follows:
a)
local: a ROD token created by a copy manager that is contained within the same SCSI target device
that is processing the copy operation originated by the EXTENDED COPY command; or
b)
remote: a ROD token created by a copy manager that is not contained within the same SCSI target
device that is processing the copy operation originated by the EXTENDED COPY command.
d The copy operation originated by the EXTENDED COPY command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID TOKEN OPERATION, REMOTE ROD TOKEN USAGE NOT SUPPORTED.
e Any other CSCD descriptor ID (i.e., not FFFFh and not F800h) that specifies a logical unit not contained
within the same SCSI target device as the processing copy manager.
f
The copy operation originated by the EXTENDED COPY command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID TOKEN OPERATION, REMOTE ROD TOKEN CREATION NOT SUPPORTED.


If the copy manager is unable to perform the activities with the remote copy manager specified by the ROD
PRODUCER CSCD DESCRIPTOR ID field necessary to use or create a remote ROD token, then the copy operation
(see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated as if an unreachable CSCD
device had been encountered (see 5.17.7.4).
If the R_TOKEN bit is set to one, the REQUESTED ROD TOKEN LIFETIME field specifies the number of seconds the
ROD token should remain valid (see 5.17.6.7).
If the REQUESTED ROD TOKEN LIFETIME field specifies a number of seconds that is less than the value in the
MINIMUM TOKEN LIFETIME field in the ROD Features third-party copy descriptor (see 7.8.17.8), then the copy
manager shall use the value in the MINIMUM TOKEN LIFETIME field. If the REQUESTED ROD TOKEN LIFETIME field
specifies a number of seconds that is greater than the value in the MAXIMUM TOKEN LIFETIME field in the ROD
Features third-party copy descriptor, then the copy operation (see 5.17.4.3) originated by the EXTENDED
COPY command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the R_TOKEN bit is set to zero and the REQUESTED ROD TOKEN LIFETIME field is not set to zero, then the copy
operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
If the R_TOKEN bit is set to one, the REQUESTED ROD TOKEN INACTIVITY TIMEOUT field specifies number of
seconds that the copy manager should wait for the next third-party copy command that specifies the ROD
token, if any, before invalidating that ROD token (see 5.17.6.7).
If the REQUESTED ROD TOKEN INACTIVITY TIMEOUT field specifies zero seconds, then the copy manager shall not
invalidate the ROD token due to the lack of its active use. If the REQUESTED ROD TOKEN INACTIVITY TIMEOUT
field specifies a number of seconds that is greater than the value in the MAXIMUM TOKEN INACTIVITY TIMEOUT
field in the ROD Features third-party copy descriptor (see 7.8.17.8), then the copy operation (see 5.17.4.3)
originated by the EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
If the R_TOKEN bit is set to zero and the REQUESTED ROD TOKEN INACTIVITY TIMEOUT field is not set to zero, then
the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
Processing of the R_TOKEN bit depends on the value in the ROD TYPE field as follows:
a)
If the ROD TYPE field is not set to zero, the R_TOKEN bit specifies whether a ROD token is to be
returned for the ROD created during processing of the EXTENDED COPY command as follows:
A)
if the R_TOKEN bit is set to zero, a ROD token shall not be returned; or
B)
if the R_TOKEN bit is set to one and table 144 does not require termination of the EXTENDED
COPY command with an error, then a ROD token shall be made available for retrieval using the
RECEIVE ROD TOKEN INFORMATION command (see 6.26);
or
b)
if the ROD TYPE field is set to zero, the processing of the R_TOKEN bit shall be as shown in table 144.
If the LIST ID USAGE field (see 6.4.3.2) is set to a value other than 00b or 10b and the R_TOKEN bit is set to one,
then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST.


The delete token (DEL_TKN) bit specifies whether the ROD token, if any, specified by the ROD CSCD
descriptor should be deleted (see 5.17.6.7) when processing of the EXTENDED COPY command is complete
as shown in table 145.
If the ROD TYPE field is set to zero, the ROD TOKEN OFFSET field specifies the ROD token (see 5.17.6) to be
accessed via this ROD CSCD descriptor. The ROD token is specified as the number of bytes to be added to
the number of the parameter data byte at offset zero of the inline data (see 5.17.7.1). If the ROD TYPE field is
not set to zero and the ROD TOKEN OFFSET field is not set to zero, then the copy operation (see 5.17.4.3) origi-
nated by the EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
Table 145 — DEL_TKN bit processing
DEL_TKN
bit
ROD TYPE
field
ROD token created by
Description
n/a
n/a
processing of the command shall not cause the
ROD token, if any, to be deleted
zero
processing copy manager or
a copy manager in the same
SCSI target device as the
copy manager that created
the ROD token
the copy manager should delete the ROD token
after processing of the command has been com-
pleted
a copy manager in different
SCSI target device from the
copy manager that created
the ROD token
the copy manager may communicate with the copy
manager that created the ROD token to cause the
ROD token to be deleted after processing of the
command has been completed
not zero
n/a
the copy operation (see 5.17.4.3) originated by the
command shall be terminated with CHECK
CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code
set to INVALID FIELD IN PARAMETER LIST.
