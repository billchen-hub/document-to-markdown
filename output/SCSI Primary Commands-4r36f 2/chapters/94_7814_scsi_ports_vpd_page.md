# 7.8.14 SCSI Ports VPD page

7.8.14 SCSI Ports VPD page
The SCSI Ports VPD page (see table 636) provides a means to retrieve designation descriptors for all the
SCSI ports in a SCSI target device.
The SCSI Ports VPD page only reports information on SCSI ports known to the device server processing the
INQUIRY command. The REPORT LUNS well-known logical unit (see 8.2) may be used to return information
on all SCSI ports in the SCSI device (i.e., all target ports and all initiator ports).
If the device server detects that a SCSI port is added or removed from the SCSI device and the SCSI port
designation descriptor list changes, it shall establish a unit attention condition (see SAM-5) for the initiator port
associated with every I_T nexus, with the additional sense code set to INQUIRY DATA HAS CHANGED.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 636 for the SCSI Ports VPD page.
Table 636 — SCSI Ports VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (88h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Designation descriptor list
SCSI port designation descriptor [first]
(see table 637)
•••
•••
SCSI port designation descriptor [last]
(see table 637)
•••
n


Each SCSI port designation descriptor (see table 637) identifies a SCSI port. The SCSI port designation
descriptors may be returned in any order.
The RELATIVE PORT IDENTIFIER field (see table 638) contains the relative port identifier of the SCSI port to which
the SCSI port designation descriptor applies.
Table 637 — SCSI port designation descriptor
Bit
Byte
Reserved
(MSB)
RELATIVE PORT IDENTIFIER
(LSB)
Reserved
(MSB)
INITIATOR PORT TRANSPORTID LENGTH (k-7)
(LSB)
INITIATOR PORT TRANSPORTID, if any
•••
k
k+1
Reserved
k+2
k+3
(MSB)
TARGET PORT DESCRIPTORS LENGTH (n-(k+4))
k+4
(LSB)
Target port descriptor list
k+5
Target port descriptor [first] (see table 639)
•••
•••
Target port descriptor [last] (see table 639)
•••
n
Table 638 — RELATIVE PORT IDENTIFIER field
Code
Description
0h
Reserved
1h
Relative port 1, historically known as port A
2h
Relative port 2, historically known as port B
3h to FFFFh
Relative port 3 through 65 535


The INITIATOR PORT TRANSPORTID LENGTH field indicates the length of the INITIATOR PORT TRANSPORTID field. An
INITIATOR PORT TRANSPORTID LENGTH field set to zero indicates no INITIATOR PORT TRANSPORTID field is present
(i.e., the SCSI port is not an initiator port).
If the INITIATOR PORT TRANSPORTID LENGTH field is set to a non-zero value, the INITIATOR PORT TRANSPORTID
field indicates a TransportID identifying the initiator port as defined in 7.6.4.
The TARGET PORT DESCRIPTORS LENGTH field indicates the length of the target port descriptors, if any. A TARGET
PORT DESCRIPTORS LENGTH field set to zero indicates no target port descriptors are present (i.e., the SCSI port
is not a target port).
Each target port descriptor (see table 639) contains an identifier for the target port. The target port descriptors
may be returned in any order.
The PROTOCOL IDENTIFIER field indicates the SCSI transport protocol to which the designation descriptor
applies as described in 7.6.1.
The CODE SET field, PIV field, ASSOCIATION field, DESIGNATOR TYPE field, DESIGNATOR LENGTH field, and DESIG-
NATOR field are as defined in the Device Identification VPD page designation descriptor (see 7.8.6.1), with the
following additional requirements:
a)
the PIV bit shall be set to one (i.e., the PROTOCOL IDENTIFIER field always contains a SCSI transport
protocol identifier); and
b)
the ASSOCIATION field shall be set to 01b (i.e., the descriptor always identifies a target port).
Table 639 — Target port descriptor
Bit
Byte
PROTOCOL IDENTIFIER
CODE SET
PIV (1b)
Reserved
ASSOCIATION (01b)
DESIGNATOR TYPE
Reserved
DESIGNATOR LENGTH (n-3)
DESIGNATOR
•••
n


7.8.15 Software Interface Identification VPD page
The Software Interface Identification VPD page (see table 640) provides identification of software interfaces
applicable to the logical unit. Logical units may have more than one associated software interface identifier.
NOTE 75 - Application clients may use the software IDs to differentiate peripheral device functions in cases
where the command set (e.g., processor devices) is too generic to distinguish different software interfaces
implemented.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 640 for the Software Interface Identi-
fication VPD page.
Each software interface identifier (see table 641) is a six-byte, fixed-length field that contains information
identifying a software interface implemented by the logical unit. The contents of software interface identifier
are in EUI-48 format.
The IEEE COMPANY_ID field contains a 24 bit OUI assigned by the IEEE.
Table 640 — Software Interface Identification VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (84h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Software interface identifier list
Software interface identifier [first]
•••
•••
n-9
Software interface identifier [last]
•••
n
Table 641 — Software interface identifier format
Bit
Byte
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC EXTENSION IDENTIFIER
(LSB)


The VENDOR SPECIFIC EXTENSION IDENTIFIER a 24 bit numeric value that is uniquely assigned by the organi-
zation associated with the OUI as required by the IEEE definition of EUI-48. The combination of OUI and
vendor specific extension identifier shall uniquely identify the document or documents that specify the
supported software interface.
7.8.16 Supported VPD Pages VPD page
The Supported VDP Pages VPD page contains a list of the VPD page codes supported by the logical unit (see
table 642). If a device server supports any VPD pages, it also shall support this VPD page.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 642 for the Supported VDP Pages
VPD page.
The supported VPD page list shall contain a list of all VPD page codes (see 7.8) implemented by the logical
unit in ascending order beginning with page code 00h.
Table 642 — Supported VPD Pages VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported VPD page list
•••
n
