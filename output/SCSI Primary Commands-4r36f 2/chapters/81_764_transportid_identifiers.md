# 7.6.4 TransportID identifiers

The PORT NUMBER field shall contain the TCP port number. The TCP port number shall conform to the require-
ments defined by iSCSI (see RFC 3720).
The INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number. The Internet protocol number
shall conform to the requirements defined by iSCSI (see RFC 3720).
NOTE 59 - The internet protocol number for TCP is 0006h.
7.6.3.10 SAS Serial SCSI Protocol CSCD descriptor format
The CSCD descriptor format shown in table 497 is used by an EXTENDED COPY command to specify a SAS
CSCD using its SAS address.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 497 for the SAS Serial SCSI Protocol CSCD
descriptor.
The SAS ADDRESS field specifies the SAS address (see SPL-2).
7.6.4 TransportID identifiers
7.6.4.1 Overview of TransportID identifiers
An application client may use a TransportID to specify an initiator port other than the initiator port that is trans-
porting the command and parameter data (e.g., as an Access identifiers (see 8.3.1.3.2) in ACL ACEs, as the
Table 497 — SAS Serial SCSI Protocol CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E9h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
SAS ADDRESS
•••
Reserved
•••
Device type specific parameters
•••


initiator port in the I_T nexus to which PERSISTENT RESERVE OUT command with REGISTER AND MOVE
service action (see 5.13.8) is moving a persistent reservation).
TransportIDs (see table 498) shall be at least 24 bytes long and shall be a multiple of four bytes in length.
The FORMAT CODE field specifies the format of the TransportID. All format codes not defined in this standard
are reserved.
The PROTOCOL IDENTIFIER field (see table 477 in 7.6.1) specifies the SCSI transport protocol to which the
TransportID applies.
The format of the SCSI transport protocol specific data depends on the value in the PROTOCOL IDENTIFIER field.
The SCSI transport protocol specific data in a TransportID shall only include initiator port identifiers, initiator
port names, or SCSI device names (see SAM-5) that persist across hard resets and I_T nexus losses. Trans-
portID formats specific to SCSI transport protocols are listed in table 499.
Table 498 — TransportID format
Bit
Byte
FORMAT CODE
Reserved
PROTOCOL IDENTIFIER
SCSI transport protocol specific data
•••
n
Table 499 — TransportID formats for specific SCSI transport protocols
SCSI transport Protocol
Protocol
Standard
Reference
Fibre Channel Protocol (FCP)
FCP-4
7.6.4.2
SCSI Parallel Interface (SPI)
SPI-5
7.6.4.3
Serial Bus Protocol (SBP) (i.e., IEEE 1394)
SBP-3
7.6.4.4
Remote Direct Memory Access (RDMA) (e.g., InfiniBand™)
SRP
7.6.4.5
Internet SCSI (iSCSI)
iSCSI
7.6.4.6
Serial Attached SCSI (SAS) Serial SCSI Protocol (SSP)
SPL
7.6.4.7
SCSI over PCI Express architecture (SOP)
SOP
7.6.4.8


7.6.4.2 TransportID for initiator ports using SCSI over Fibre Channel
A Fibre Channel TransportID (see table 500) specifies an FCP-4 initiator port based on the N_Port_Name
belonging to that initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 500 for the Fibre Channel TransportID format.
The N_PORT_NAME field shall contain the N_Port_Name defined by the N_Port login (PLOGI) extended link
service (see FC-FS-3).
Table 500 — Fibre Channel TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (0h)
Reserved
•••
N_PORT_NAME
•••
Reserved
•••


7.6.4.3 TransportID for initiator ports using a parallel SCSI bus
A parallel SCSI bus TransportID (see table 501) specifies a SPI-5 initiator port based on the SCSI address of
an initiator port and the relative port identifier of the target port through which the application client accesses
the SCSI target device.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 501 for the Parallel SCSI bus TransportID format.
The SCSI ADDRESS field specifies the SCSI address (see SPI-5) of the initiator port.
The RELATIVE TARGET PORT IDENTIFIER field specifies the relative port identifier of the target port for which the
initiator port SCSI address applies. If the RELATIVE TARGET PORT IDENTIFIER does not reference a target port in
the SCSI target device, the TransportID is invalid.
Table 501 — Parallel SCSI bus TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (1h)
Reserved
(MSB)
SCSI ADDRESS
(LSB)
Obsolete
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
Reserved
•••


7.6.4.4 TransportID for initiator ports using SCSI over IEEE 1394
An IEEE 1394 TransportID (see table 502) specifies an SBP-3 initiator port based on the EUI-64 initiator port
name belonging to that initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 502 for the IEEE 1394 TransportID format.
The EUI-64 NAME field shall contain the EUI-64 IEEE 1394 node unique identifier (see SBP-3) for an initiator
port.
7.6.4.5 TransportID for initiator ports using SCSI over an RDMA interface
A RDMA TransportID (see table 503) specifies an SRP initiator port based on the world wide unique initiator
port name belonging to that initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 503 for the RDMA TransportID format.
The INITIATOR PORT IDENTIFIER field shall contain an SRP initiator port identifier (see SRP).
Table 502 — IEEE 1394 TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (3h)
Reserved
•••
EUI-64 NAME
•••
Reserved
•••
Table 503 — RDMA TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (4h)
Reserved
•••
INITIATOR PORT IDENTIFIER
•••


7.6.4.6 TransportID for initiator ports using SCSI over iSCSI
An iSCSI TransportID specifies an iSCSI initiator port using one of the TransportID formats listed in table 504.
iSCSI TransportIDs with a format code of 00b may be rejected. iSCSI TransportIDs with a format code of 01b
should not be rejected.
A iSCSI TransportID with the format code set to 00b (see table 505) specifies an iSCSI initiator port based on
the world wide unique SCSI device name of the iSCSI initiator device containing the initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 505 for the iSCSI initiator device TransportID format.
The ADDITIONAL LENGTH field specifies the number of bytes that follow in the TransportID. The additional length
shall be at least 20 and shall be a multiple of four.
The null-terminated, null-padded (see 4.3.2) ISCSI NAME field shall contain the iSCSI name of an iSCSI initiator
node (see RFC 3720). The first ISCSI NAME field byte containing an ASCII null character terminates the ISCSI
NAME field without regard for the specified length of the iSCSI TransportID or the contents of the ADDITIONAL
LENGTH field.
NOTE 60 - The maximum length of the iSCSI TransportID is 228 bytes because the iSCSI name length does
not exceed 223 bytes.
If a iSCSI TransportID with the format code set to 00b appears in a PERSISTENT RESERVE OUT parameter
list (see 6.16.3), all initiator ports known to the device server with an iSCSI node name matching the one in the
TransportID shall be registered.
If a iSCSI TransportID with the format code set to 00b appears in an ACE access identifier (see 8.3.1.3.2), the
logical units listed in the ACE shall be accessible to any initiator port with an iSCSI node name matching the
value in the TransportID. The access controls coordinator shall reject any command that attempts to define
Table 504 —  iSCSI TransportID formats
Format code
Description
Reference
00b
Initiator port is identified using the world wide unique SCSI device name of
the iSCSI initiator device containing the initiator port.
table 505
01b
Initiator port is identified using the world wide unique initiator port identifier.
table 506
10b to 11b
Reserved
Table 505 — iSCSI initiator device TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (5h)
Reserved
(MSB)
ADDITIONAL LENGTH (m-3)
(LSB)
(MSB)
ISCSI NAME
•••
m
(LSB)


more than one ACEs with an iSCSI TransportID access identifier containing the same iSCSI name. The
command shall be terminated with CHECK CONDITION status, with the sense key ILLEGAL REQUEST, and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
A iSCSI TransportID with the format code set to 01b (see table 506) specifies an iSCSI initiator port based on
its world wide unique initiator port identifier.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 506 for the iSCSI initiator port TransportID format.
The ADDITIONAL LENGTH field specifies the number of bytes that follow in the TransportID encompassing the
ISCSI NAME, SEPARATOR, and ISCSI INITIATOR SESSION ID fields. The additional length shall be at least 20 and
shall be a multiple of four.
The ISCSI NAME field shall contain the iSCSI name of an iSCSI initiator node (see RFC 3720). The ISCSI NAME
field shall not be null-terminated (see 4.3.2) and shall not be padded.
The SEPARATOR field shall contain the five ASCII characters ',i,0x'.
NOTE 61 - The notation used to define the SEPARATOR field is described in 3.5.3.
The null-terminated, null-padded ISCSI INITIATOR SESSION ID field shall contain the iSCSI initiator session
identifier (see RFC 3720) in the form of ASCII characters that are the hexadecimal digits converted from the
binary iSCSI initiator session identifier value. The first ISCSI INITIATOR SESSION ID field byte containing an ASCII
null character terminates the ISCSI INITIATOR SESSION ID field without regard for the specified length of the
iSCSI TransportID or the contents of the ADDITIONAL LENGTH field.
Table 506 — iSCSI initiator port TransportID format
Bit
Byte
FORMAT CODE (01b)
Reserved
PROTOCOL IDENTIFIER (5h)
Reserved
(MSB)
ADDITIONAL LENGTH (m-3)
(LSB)
(MSB)
ISCSI NAME
•••
n-1
(LSB)
n
(MSB)
SEPARATOR (2C 692C 3078h)
•••
n+4
(LSB)
n+5
(MSB)
ISCSI INITIATOR SESSION ID
•••
m
(LSB)


7.6.4.7 TransportID for initiator ports using SCSI over SAS Serial SCSI Protocol
A SAS Serial SCSI Protocol (SSP) TransportID (see table 507) specifies a SAS initiator port that is communi-
cating via SSP using the SAS address belonging to that initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 507 for the SAS Serial SCSI Protocol TransportID format.
The SAS ADDRESS field specifies the SAS address of the initiator port.
7.6.4.8 TransportID for initiator ports using SCSI over PCI Express architecture
A SCSI over PCI Express architecture (SOP) TransportID (see table 508) specifies a SOP initiator port.
The FORMAT CODE field and PROTOCOL IDENTIFIER field are defined in 7.6.4.1, and shall be set as shown in
table 508 for the SOP TransportID format.
The ROUTING ID field shall contain a PCI Express routing ID (see SOP).
Table 507 — SAS Serial SCSI Protocol TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (6h)
Reserved
•••
SAS ADDRESS
•••
Reserved
•••
Table 508 — SOP TransportID format
Bit
Byte
FORMAT CODE (00b)
Reserved
PROTOCOL IDENTIFIER (Ah)
Reserved
ROUTING ID
Reserved
•••
