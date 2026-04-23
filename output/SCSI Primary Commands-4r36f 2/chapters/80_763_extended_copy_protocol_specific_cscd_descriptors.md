# 7.6.3 EXTENDED COPY protocol specific CSCD descriptors

7.6.3 EXTENDED COPY protocol specific CSCD descriptors
7.6.3.1 Introduction to EXTENDED COPY protocol specific CSCD descriptors
The protocol-specific CSCD descriptors (see 6.4.5.1) in the parameter list (see 5.17.7.1) of the EXTENDED
COPY(LID4) command (see 6.4) and the EXTENDED COPY(LID1) command (see 6.5) are described in
7.6.3.
7.6.3.2 Fibre Channel N_Port_Name CSCD descriptor format
The CSCD descriptor format shown in table 489 is used by an EXTENDED COPY command to specify an
FCP CSCD using its Fibre Channel N_Port_Name.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 489 for the Fibre Channel N_Port_Name CSCD
descriptor.
The N_PORT_NAME field shall contain the N_Port_Name defined by the port login (PLOGI) extended link
service (see FC-LS-2).
NOTE 54 - The Fibre Channel N_Port_Name CSCD descriptor format requests that the copy manager
translate the N_Port_Name to an N_Port_ID (see FC-FS-3, FC-LS-2, and 7.6.3.3).
Table 489 — Fibre Channel N_Port_Name CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E0h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
N_PORT_NAME
•••
Reserved
•••
Device type specific parameters
•••


7.6.3.3 Fibre Channel N_Port_ID CSCD descriptor format
The CSCD descriptor format shown in table 490 is used by an EXTENDED COPY command to specify an
FCP CSCD using its Fibre Channel N_Port_ID.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 490 for the Fibre Channel N_Port_ID CSCD
descriptor.
The N_PORT_ID field shall contain the port D_ID (see FC-FS-3) to be used to transport frames including PLOGI
(see (FC-LS-2) and FCP-4 related frames.
NOTE 55 - Use of N_Port_ID addressing restricts this CSCD descriptor format to a single Fibre Channel
fabric.
Table 490 — Fibre Channel N_Port_ID CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E1h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
Reserved
•••
(MSB)
N_PORT_ID
(LSB)
Reserved
•••
Device type specific parameters
•••


7.6.3.4 Fibre Channel N_Port_ID With N_Port_Name Checking CSCD descriptor format
The CSCD descriptor format shown in table 491 is used by an EXTENDED COPY command to specify an
FCP CSCD using its Fibre Channel N_Port_ID and to require the copy manager to verify that the
N_Port_Name of the specified N_Port matches the value in the CSCD descriptor.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 491 for the Fibre Channel N_Port_ID With
N_Port_Name Checking CSCD descriptor.
The N_PORT_NAME field shall contain the N_Port_Name defined by the port login (PLOGI) extended link
service (see FC-FS-3 and FC-LS-2).
The N_PORT_ID field shall contain the port D_ID (see FC-FS-3) to be used to transport frames including PLOGI
(see FC-LS-2) and FCP-4 related frames.
NOTE 56 - Use of N_Port addressing restricts this CSCD descriptor format to a single fabric.
If the copy manager first processes a segment descriptor that references this type of CSCD descriptor, it shall
confirm that the D_ID in the N_PORT_ID field is associated with the N_Port_Name in the N_PORT_NAME field. If
the confirmation fails, the copy operation (see 5.17.4.3) originated by the command shall be terminated
because the CSCD is unreachable (see 5.17.7.4). The copy manager processing this CSCD descriptor shall
Table 491 — Fibre Channel N_Port_ID With N_Port_Name Checking CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E2h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
N_PORT_NAME
•••
Reserved
(MSB)
N_PORT_ID
(LSB)
Reserved
•••
Device type specific parameters
•••


track configuration changes that affect the D_ID value for the duration of the copy operation (see 5.17.4.3). An
application client is responsible for tracking configuration changes between commands.
7.6.3.5  SCSI Parallel T_L CSCD descriptor format
The CSCD descriptor format shown in table 492 is used by an EXTENDED COPY command to specify a SPI
CSCD using one of its target port identifiers (see SAM-5).
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 492 for the SCSI Parallel T_L CSCD descriptor.
The TARGET IDENTIFIER field specifies the SCSI target identifier (see SPI-5).
Table 492 — SCSI Parallel T_L CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E3h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
Vendor specific
TARGET IDENTIFIER
Reserved
•••
Device type specific parameters
•••


7.6.3.6 IEEE 1394 EUI-64 CSCD descriptor format
The CSCD descriptor format shown in table 493 is used by an EXTENDED COPY command to specify an
SBP-3 CSCD using its IEEE 1394 Extended Unique Identifier, 64-bits (EUI-64) and configuration ROM
(Read-Only Memory) directory identifier.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 493 for the IEEE 1394 EUI-64 CSCD descriptor.
The EUI-64 field shall contain the SBP-3 node’s unique identifier (EUI-64) obtained from the configuration
ROM bus information block, as specified by ANSI IEEE 1394a:2000.
NOTE 57 - ANSI IEEE 1394a-2000 separately labels the components of the EUI-64 as NODE_VENDOR_ID,
CHIP_ID_HI and CHIP_ID_LO. Collectively these form the node’s EUI-64.
The DIRECTORY ID field shall contain the CSCD’s directory identifier, as specified by ISO/IEC 13213:1994.
Table 493 — IEEE 1394 EUI-64 CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E8h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
EUI-64
•••
DIRECTORY ID
Reserved
•••
Device type specific parameters
•••


7.6.3.7 RDMA CSCD descriptor format
The CSCD descriptor format shown in table 494 is used by an EXTENDED COPY command to specify an
SRP CSCD using its RDMA SRP target port identifier.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 494 for the RDMA CSCD descriptor.
The TARGET PORT IDENTIFIER field specifies the SRP target port identifier (see SRP).
Table 494 — RDMA CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E7h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
TARGET PORT IDENTIFIER
•••
Device type specific parameters
•••


7.6.3.8  iSCSI IPv4 CSCD descriptor format
The CSCD descriptor format shown in table 495 is used by an EXTENDED COPY command to specify an
iSCSI CSCD using its binary IPv4 (Internet Protocol version 4) address.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 495 for the iSCSI IPv4 CSCD descriptor.
The IPV4 ADDRESS field shall contain an IPv4 address (see RFC 791).
The PORT NUMBER field shall contain the TCP port number. The TCP port number shall conform to the require-
ments defined by iSCSI (see RFC 3720).
The INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number. The Internet protocol number
shall conform to the requirements defined by iSCSI (see RFC 3720).
NOTE 58 - The internet protocol number for TCP is 0006h.
Table 495 — iSCSI IPv4 CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (E5h)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
(MSB)
IPV4 ADDRESS
•••
(LSB)
Reserved
•••
(MSB)
PORT NUMBER
(LSB)
Reserved
(MSB)
INTERNET PROTOCOL NUMBER
(LSB)
Device type specific parameters
•••


7.6.3.9  iSCSI IPv6 CSCD descriptor format
The CSCD descriptor format shown in table 496 is used by an EXTENDED COPY command to specify an
iSCSI CSCD using its binary IPv6 (Internet Protocol version 6) address.
The DESCRIPTOR TYPE CODE field, LU ID TYPE field, PERIPHERAL DEVICE TYPE field, RELATIVE INITIATOR PORT
IDENTIFIER field, LU IDENTIFIER field, and the device type specific parameters are described in 6.4.5.1. The
DESCRIPTOR TYPE CODE field shall be set as shown in table 496 for the iSCSI IPv6 CSCD descriptor.
The IPV6 ADDRESS field shall contain a unicast IPv6 address (see RFC 4291).
The EXTENSION DESCRIPTOR TYPE CODE field is described in 6.4.5.2. If the EXTENSION DESCRIPTOR TYPE CODE
field does not contain the value shown in table 496, then the copy operation (see 5.17.4.3) originated by the
EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the sense key set to
COPY ABORTED, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
Table 496 — iSCSI IPv6 CSCD descriptor format
Bit
Byte
DESCRIPTOR TYPE CODE (EAh)
LU ID TYPE
Obsolete
PERIPHERAL DEVICE TYPE
(MSB)
RELATIVE INITIATOR PORT IDENTIFIER
(LSB)
LU IDENTIFIER
•••
(MSB)
IPV6 ADDRESS
•••
(LSB)
Device type specific parameters
•••
EXTENSION DESCRIPTOR TYPE CODE (FFh)
Reserved
(MSB)
PORT NUMBER
(LSB)
(MSB)
INTERNET PROTOCOL NUMBER
(LSB)
Reserved
•••
