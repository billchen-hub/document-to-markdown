# 7.8.12 Protocol Specific Logical Unit Information VPD page

The POWER CONSUMPTION UNITS field (see table 631) indicates the units used for the POWER CONSUMPTION
VALUE field.
The POWER CONSUMPTION VALUE field indicates the maximum power consumption associated with the identifier
in the POWER CONSUMPTION IDENTIFIER field using the units specified by the POWER CONSUMPTION UNITS field.
7.8.12 Protocol Specific Logical Unit Information VPD page
The Protocol Specific Logical Unit Information VPD page (see table 632) contains protocol specific param-
eters associated with a SCSI port that may be different for each logical unit in the SCSI target device.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 632 for the Protocol Specific Logical
Unit Information VPD page.
Table 631 — POWER CONSUMPTION UNITS field
Code
Units
000b
Gigawatts
001b
Megawatts
010b
Kilowatts
011b
Watts
100b
Milliwatts
101b
Microwatts
all others
Reserved
Table 632 — Protocol Specific Logical Unit Information VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (90h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Logical unit information descriptor list
Logical unit information descriptor [first]
(see table 633)

•••
•
•
•
Logical unit information descriptor [last]
(see table 633)
•••
n


The logical unit information descriptor list contains descriptors for SCSI ports known to the device server that
is processing the INQUIRY command. The logical unit information descriptors (see table 633) may be
returned in any order.
The RELATIVE PORT IDENTIFIER field indicates the relative port identifier of the SCSI port to which the logical unit
information descriptor applies and is defined in the SCSI Ports VPD page (see 7.8.14).
The PROTOCOL IDENTIFIER field indicates the SCSI transport protocol to which the logical unit information
descriptor applies as described in 7.6.1.
The PROTOCOL SPECIFIC DATA LENGTH field indicates the length in bytes of the per logical unit SCSI transport
protocol specific data.
The per logical unit SCSI transport protocol specific data is defined by the SCSI transport protocol standard
that corresponds to the SCSI target port.
Table 633 — Logical unit information descriptor
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
Per logical unit SCSI transport protocol specific
data
n
