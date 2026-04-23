# 7.8.13 Protocol Specific Port Information VPD page

7.8.13 Protocol Specific Port Information VPD page
The Protocol Specific Port Information VPD page (see table 634) contains protocol specific parameters
associated with a SCSI port that are the same for all logical units in the SCSI target device.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 634 for the Protocol Specific Port
Information VPD page.
Table 634 — Protocol Specific Port Information VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (91h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Port information descriptor list
Port information descriptor [first] (see table 633)

•••
•••
Port information descriptor [last] (see table 633)
•••
n


The port information descriptor list contains descriptors for SCSI ports known to the device server that is
processing the INQUIRY command. The port information descriptors (see table 635) may be returned in any
order.
The RELATIVE PORT IDENTIFIER field indicates the relative port identifier of the SCSI port to which the port infor-
mation descriptor applies and is defined in the SCSI Ports VPD page (see 7.8.14).
The PROTOCOL IDENTIFIER field indicates the SCSI transport protocol to which the port information descriptor
applies as described in 7.6.1.
The PROTOCOL SPECIFIC DATA LENGTH field indicates the length in bytes of the shared SCSI transport protocol
specific data.
The shared SCSI transport protocol specific data is defined by the SCSI transport protocol standard that
corresponds to the SCSI target port.
Table 635 — Port information descriptor
Bit
Byte
(MSB)
RELATIVE PORT IDENTIFIER
(LSB)
Reserved
PROTOCOL IDENTIFIER
Reserved
(MSB)
PROTOCOL SPECIFIC DATA LENGTH (n-7)
(LSB)
Shared SCSI transport protocol specific data
•••
n
