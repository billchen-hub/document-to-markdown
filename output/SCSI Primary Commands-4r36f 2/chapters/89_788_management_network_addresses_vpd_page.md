# 7.8.8 Management Network Addresses VPD page

set to zero indicates that the device server does not support a WRITE BUFFER command with the MODE field
set to 0Dh and the PO_ACT bit set to one.
A hard reset activation supported (HRA_SUP) bit set to one indicates that the device server supports a WRITE
BUFFER command with the MODE field set to 0Dh (see 6.49.10) and the HR_ACT bit set to one. A HRA_SUP bit
set to zero indicates that the device server does not support a WRITE BUFFER command with the MODE field
set to 0Dh and the HR_ACT bit set to one.
A vendor specific activation supported (VSA_SUP) bit set to one indicates that the device server supports a
WRITE BUFFER command with the MODE field set to 0Dh (see 6.49.10) and the VSE_ACT bit set to one. A
VSA_SUP bit set to zero indicates that the device server does not support a WRITE BUFFER command with
the MODE field set to 0Dh and the VSE_ACT bit set to one.
The MAXIMUM SUPPORTED SENSE DATA LENGTH field indicates the maximum length in bytes of sense data (see
4.5) that the device server is capable of returning in the same I_T_L_Q nexus transaction as the status. A
MAXIMUM SUPPORTED SENSE DATA LENGTH field set to zero indicates that the device server does not report a
maximum length. This value shall be less than or equal to 252.
7.8.8 Management Network Addresses VPD page
The Management Network Addresses VPD page (see table 622) provides a list of network addresses of
management services associated with a SCSI target device, target port, or logical unit.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 622 for the Management Network
Address VPD page.
Table 622 — Management Network Addresses VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (85h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Network services descriptor list
Network services descriptor [first]
•••
•••
Network services descriptor [last]
•••
n


Each network service descriptor (see table 623) contains information about one management service.
The ASSOCIATION field (see table 593 in 7.8.6.1) indicates the entity (i.e., SCSI target device, target port, or
logical unit) with which the service is associated.
The SERVICE TYPE field (see table 624) allows differentiation of multiple services with the same protocol
running at different port numbers or paths.
NOTE 74 - A SCSI target device may provide separate HTTP services for configuration and diagnostics. One
of these services may use the standard HTTP port 80 and the other service may use a different port (e.g.,
8080).
The NETWORK ADDRESS LENGTH field indicates the length in bytes of the NETWORK ADDRESS field. The network
address length shall be a multiple of four.
The null-terminated, null-padded NETWORK ADDRESS field contains the URL form of a URI as defined in RFC
3986.
Table 623 — Network service descriptor format
Bit
Byte
Reserved
ASSOCIATION
SERVICE TYPE
Reserved
(MSB)
NETWORK ADDRESS LENGTH (n-3)
(LSB)
NETWORK ADDRESS
•••
n
Table 624 — SERVICE TYPE field
Code
Description
00h
Unspecified
01h
Storage Configuration Service
02h
Diagnostics
03h
Status
04h
Logging
05h
Code Download
06h
Copy Service
07h
Administrative Configuration Service
08h to 1Fh
Reserved
