# 7.6.2 Alias entry protocol specific designations

7.6 Protocol specific parameters
7.6.1 Protocol specific parameters introduction
Some commands use protocol specific information in their CDBs or parameter lists. This subclause describes
those protocol specific parameters.
Protocol specific parameters may include a PROTOCOL IDENTIFIER field (see table 477) as a reference for the
SCSI transport protocol to which the protocol specific parameter applies.
7.6.2 Alias entry protocol specific designations
7.6.2.1 Introduction to alias entry protocol specific designations
The alias entries (see 6.2.2) in the parameter data for the CHANGE ALIASES command (see 6.2) and
REPORT ALIASES command (see 6.30) include FORMAT CODE, DESIGNATION LENGTH and DESIGNATION fields
whose contents and meaning are based on the SCSI transport protocol specified in a PROTOCOL IDENTIFIER
field (see 7.6.1). This subclause defines the SCSI transport protocol specific format codes, designation
lengths, and designations.
Table 477 — PROTOCOL IDENTIFIER values
Protocol
Identifier
Description
Protocol
Standard
0h
Fibre Channel Protocol for SCSI
FCP-4
1h
SCSI Parallel Interface
SPI-5
2h
Serial Storage Architecture SCSI-3 Protocol
SSA-S3P
3h
Serial Bus Protocol for IEEE 1394
SBP-3
4h
SCSI RDMA Protocol
SRP
5h
Internet SCSI (iSCSI)
iSCSI
6h
SAS Serial SCSI Protocol
SPL-2
7h
Automation/Drive Interface Transport Protocol
ADT-2
8h
AT Attachment Interface
ACS-2
9h
USB Attached SCSI
UAS-2
Ah
SCSI over PCI Express architecture
SOP
Bh to Eh
Reserved
Fh
No specific protocol


7.6.2.2 Fibre Channel specific alias entry designations
7.6.2.2.1 Introduction to Fibre Channel specific alias entry designations
If an alias entry PROTOCOL IDENTIFIER field is set to the Fibre Channel protocol identifier (0h, see table 477), the
FORMAT CODE, DESIGNATION LENGTH and DESIGNATION fields shall be as defined in table 478.
7.6.2.2.2 Fibre Channel world wide port name alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify a Fibre Channel world wide port name desig-
nation, the alias entry DESIGNATION field shall have the format shown in table 479.
The FIBRE CHANNEL WORLD WIDE PORT NAME field shall contain the port world wide name defined by the port
login (PLOGI) extended link service (see FC-FS-3).
A Fibre Channel world wide port name designation is valid (see 6.2.3) if the device server has access to a
SCSI domain formed by a Fibre Channel fabric and the fabric contains a port with the specified port world
wide name.
Table 478 — Fibre Channel alias entry format codes
Format
Code
Description
Designation
Length
(bytes)
Reference
00h
World Wide Port Name
7.6.2.2.2
01h
World Wide Port Name
with N_Port checking
7.6.2.2.3
02h to FFh
Reserved
Table 479 — Fibre Channel world wide port name alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
FIBRE CHANNEL WORLD WIDE PORT NAME
•••


7.6.2.2.3 Fibre Channel world wide port name with N_Port checking alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify a Fibre Channel world wide port name with N_Port
checking designation, the alias entry DESIGNATION field shall have the format shown in table 480.
The FIBRE CHANNEL WORLD WIDE PORT NAME field shall contain the port world wide name defined by the port
login (PLOGI) extended link service (see FC-FS-3).
The N_PORT field shall contain the FC-FS-3 port D_ID to be used to transport frames including PLOGI and
FCP-4 related frames.
A Fibre Channel world wide port name with N_Port checking designation is valid (see 6.2.3) if all of the
following conditions are true:
a)
the device server has access to a SCSI domain formed by a Fibre Channel fabric;
b)
the fabric contains a port with the specified port World Wide Name; and
c)
the value in the N_PORT field is the N_Port identifier of a Fibre Channel port whose port world wide
name matches that in the FIBRE CHANNEL WORLD WIDE PORT NAME field.
7.6.2.3 RDMA specific alias entry designations
7.6.2.3.1 Introduction to RDMA specific alias entry designations
If an alias entry PROTOCOL IDENTIFIER field is set to the SCSI RDMA protocol identifier (4h, see table 477), the
FORMAT CODE, DESIGNATION LENGTH and DESIGNATION fields shall be as defined in table 481.
Table 480 — Fibre Channel world wide port name with N_Port checking alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
FIBRE CHANNEL WORLD WIDE PORT NAME
•••
Reserved
(MSB)
N_PORT
(LSB)
Table 481 — RDMA alias entry format codes
Format
Code
Description
Designation
Length
(bytes)
Reference
00h
Target Port Identifier
7.6.2.3.2
01h
InfiniBand™ Global Identifier with
Target Port Identifier checking
7.6.2.3.3
02h to FFh
Reserved


7.6.2.3.2 RDMA target port identifier alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify a SCSI RDMA target port identifier designation,
the alias entry DESIGNATION field shall have the format shown in table 482.
The TARGET PORT IDENTIFIER field shall contain an SRP target port identifier.
A SCSI RDMA target port identifier designation is valid (see 6.2.3) if the device server has access to an SRP
SCSI domain containing the specified SRP target port identifier.
7.6.2.3.3 InfiniBand global identifier with target port identifier checking alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify an InfiniBand global identifier with target port
identifier checking designation, the alias entry designation field shall have the format shown in table 483.
The INFINIBAND GLOBAL IDENTIFIER field specifies an InfiniBand global identifier (GID) of an InfiniBand port
connected to an SRP target port.
The TARGET PORT IDENTIFIER field shall specify an SRP target port identifier.
An InfiniBand global identifier with target port identifier checking designation is valid (see 6.2.3) if all of the
following conditions are true:
a)
the device server has access to an SRP SCSI domain layered on InfiniBand;
Table 482 — RDMA target port identifier alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
TARGET PORT IDENTIFIER
•••
Table 483 — InfiniBand global identifier with target port identifier checking alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
INFINIBAND GLOBAL IDENTIFIER
•••
TARGET PORT IDENTIFIER
•••


b)
the device server has access to an SRP target port based on the InfiniBand global identifier specified
in the INFINIBAND GLOBAL IDENTIFIER field; and
c)
the value in the TARGET PORT IDENTIFIER field is the SRP target port identifier for the SRP target port
that is accessible via the InfiniBand global identifier contained in the INFINIBAND GLOBAL IDENTIFIER
field.
7.6.2.4 Internet SCSI specific alias entry designations
7.6.2.4.1 Introduction to Internet SCSI specific alias entry designations
If an alias entry PROTOCOL IDENTIFIER field is set to the iSCSI protocol identifier (5h, see table 477), the FORMAT
CODE, DESIGNATION LENGTH and DESIGNATION fields shall be as defined in table 484.
NOTE 53 - A designation that contains no IP addressing information or contains IP addressing information
that does not address the named SCSI target device may require a device server to have access to a name
server or to other discovery protocols to resolve the given iSCSI Name to an IP address through which the
device server may establish iSCSI Login. Access to such a service is protocol specific and vendor specific.
7.6.2.4.2 iSCSI name alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify iSCSI name designation, the alias entry DESIG-
NATION field shall have the format shown in table 485.
The null-terminated, null-padded (see 4.3.2) ISCSI NAME field shall contain the iSCSI name of an iSCSI node
(see RFC 3720). The number of bytes in the ISCSI NAME field shall be a multiple of four.
An iSCSI name designation is valid if the device server has access to a SCSI domain containing an Internet
protocol network and that network contains an iSCSI node with the specified iSCSI name.
Table 484 — iSCSI alias entry format codes
Format
Code
Description
Designation
Length
(bytes,
maximum)
Reference
00h
iSCSI Name
7.6.2.4.2
01h
iSCSI Name with binary IPv4 address
7.6.2.4.3
02h
iSCSI Name with IPName
7.6.2.4.4
03h
iSCSI Name with binary IPv6 address
7.6.2.4.5
04h to FFh
Reserved
Table 485 — iSCSI name alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
(MSB)
ISCSI NAME
•••
4m-1
(LSB)


7.6.2.4.3 iSCSI name with binary IPv4 address alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify iSCSI name with binary IPv4 address designation,
the alias entry DESIGNATION field shall have the format shown in table 486.
The null-terminated, null-padded (see 4.3.2) ISCSI NAME field shall contain the iSCSI name of an iSCSI node
(see RFC 3720). The number of bytes in the ISCSI NAME field shall be a multiple of four.
The IPV4 ADDRESS field shall contain an IPv4 address (see RFC 791).
The PORT NUMBER field shall contain a TCP port number. The TCP port number shall conform to the require-
ments defined by iSCSI (see RFC 3720).
The INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number. The Internet protocol number
shall conform to the requirements defined by iSCSI (see RFC 3720).
An iSCSI name designation is valid if the device server has access to a SCSI domain containing an Internet
protocol network and that network contains an iSCSI node with the specified iSCSI name.
The IPv4 address, port number, and Internet protocol number provided in the designation may be used by a
device server for addressing to discover and establish communication with the named iSCSI node. Alterna-
tively, the device server may use other protocol specific or vendor specific methods to discover and establish
communication with the named iSCSI node.
Table 486 — iSCSI name with binary IPv4 address alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
(MSB)
ISCSI NAME
•••
4m-1
(LSB)
4m
(MSB)
IPV4 ADDRESS
•••
4m+3
(LSB)
4m+4
Reserved
4m+5
4m+6
(MSB)
PORT NUMBER
4m+7
(LSB)
4m+8
Reserved
4m+9
4m+10
(MSB)
INTERNET PROTOCOL NUMBER
4m+11
(LSB)


7.6.2.4.4 iSCSI name with IPname alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify iSCSI name with IPname designation, the alias
entry DESIGNATION field shall have the format shown in table 487.
The null-terminated (see 4.3.2) ISCSI NAME field shall contain the iSCSI name of an iSCSI node (see RFC
3720).
The null-terminated (see 4.3.2) IPNAME field shall contain a Internet protocol domain name.
The PAD field shall contain zero to three bytes set to zero such that the total length of the ISCSI NAME, IPNAME,
and PAD fields is a multiple of four. Device servers shall ignore the PAD field.
The PORT NUMBER field shall contain a TCP port number. The TCP port number shall conform to the require-
ments defined by iSCSI (see RFC 3720).
The INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number. The Internet protocol number
shall conform to the requirements defined by iSCSI (see RFC 3720).
An iSCSI name designation is valid if the device server has access to a SCSI domain containing an Internet
protocol network and that network contains an iSCSI node with the specified iSCSI name.
The Internet protocol domain name, port number, and Internet protocol number provided in the designation
may be used by a device server for addressing to discover and establish communication with the named
Table 487 — iSCSI name with IPname alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
(MSB)
ISCSI NAME
•••
k
(LSB)
k+1
(MSB)
IPNAME
•••
n
(LSB)
n+1
PAD (if needed)
4m-1
4m
Reserved
4m+1
4m+2
(MSB)
PORT NUMBER
4m+3
(LSB)
4m+4
Reserved
4m+5
4m+6
(MSB)
INTERNET PROTOCOL NUMBER
4m+7
(LSB)


iSCSI node. Alternatively, the device server may use other protocol specific or vendor specific methods to
discover and establish communication with the named iSCSI node.
7.6.2.4.5 iSCSI name with binary IPv6 address alias entry designation
If the PROTOCOL IDENTIFIER and FORMAT CODE fields specify iSCSI name with binary IPv6 address designation,
the alias entry DESIGNATION field shall have the format shown in table 488.
The null-terminated, null-padded (see 4.3.2) ISCSI NAME field shall contain the iSCSI name of an iSCSI node
(see RFC 3720).
The IPV6 ADDRESS field shall contain an IPv6 address (see RFC 4291).
The PORT NUMBER field shall contain a TCP port number. The TCP port number shall conform to the require-
ments defined by iSCSI (see RFC 3720).
The INTERNET PROTOCOL NUMBER field shall contain an Internet protocol number. The Internet protocol number
shall conform to the requirements defined by iSCSI (see RFC 3720).
An iSCSI name designation is valid if the device server has access to a SCSI domain containing an Internet
protocol network and that network contains an iSCSI node with the specified iSCSI name.
The IPv6 address, port number and Internet protocol number provided in the designation may be used by a
device server for addressing to discover and establish communication with the named iSCSI node. Alterna-
tively, the device server may use other protocol specific or vendor specific methods to discover and establish
communication with the named iSCSI node.
Table 488 — iSCSI name with binary IPv6 address alias entry designation
Bit
Byte
See table 121 in 6.2.2
•••
(MSB)
ISCSI NAME
•••
n
(LSB)
4m
(MSB)
IPV6 ADDRESS
•••
4m+15
(LSB)
4m+16
Reserved
4m+17
4m+18
(MSB)
PORT NUMBER
4m+19
(LSB)
4m+20
Reserved
4m+21
4m+22
(MSB)
INTERNET PROTOCOL NUMBER
4m+23
(LSB)
