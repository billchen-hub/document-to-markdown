# 7.8.5 Device Constituents VPD page

7.8.5 Device Constituents VPD page
7.8.5.1 Device Constituents VPD page overview
The Device Constituents VPD page (see table 581) provides identifying information for the constituents (e.g.,
logical units in other SCSI devices, microcode, storage medium, or vendor specific information technology
components) of the logical unit described in the standard INQUIRY data (see 6.6.2).
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 581 for the Device Constituents VPD
page.
Table 581 — Device Constituents VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (8Bh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Constituent descriptor list
Constituent descriptor (see table 582) [first]
•••
•••
Constituent descriptor (see table 582) [last]
•••
n


Each constituent descriptor (see table 582) contains identifying information for one constituent of the logical
unit described in the standard INQUIRY data (see 6.6.2).
The CONSTITUENT TYPE field (see table 583) indicates the constituent descriptor type.
Table 582 — Constituent descriptor
Bit
Byte
(MSB)
CONSTITUENT TYPE
(LSB)
CONSTITUENT DEVICE TYPE
Reserved
(MSB)
T10 VENDOR IDENTIFICATION
•••
(LSB)
(MSB)
PRODUCT IDENTIFICATION
•••
(LSB)
(MSB)
PRODUCT REVISION LEVEL
•••
(LSB)
Reserved
(MSB)
CONSTITUENT DESCRIPTOR LENGTH (n-35)
(LSB)
Constituent type specific descriptor list
Constituent type specific descriptor [first]
•••
•••
Constituent type specific descriptor [last]
•••
n
Table 583 — CONSTITUENT TYPE field
Code
Description
Reference
0000h
Reserved
0001h
Virtual tape library
7.8.5.2
0002h
Virtual tape drive
7.8.5.3
0003h
Direct access block device
0004h to FFFFh
Reserved


The CONSTITUENT DEVICE TYPE field (see table 584) indicates the constituent descriptor type.
The T10 VENDOR IDENTIFICATION field, PRODUCT IDENTIFICATION field, and the PRODUCT REVISION LEVEL field are
identifying information for one constituent of the logical unit described in the standard INQUIRY data, and are
as defined in 6.6.2.
The CONSTITUENT DESCRIPTOR LENGTH field indicates the length of the constituent type specific descriptor list.
Each constituent type specific descriptor contains information that is specific to the constituent type. The
format of each constituent type specific descriptor is defined by the constituent type (see table 583).
7.8.5.2 Virtual tape library constituent type specific descriptor
If the CONSTITUENT TYPE field (see 7.8.5.1) is set to 0001h (i.e., virtual tape library), then the format for each
constituent type specific descriptor (see 7.8.5.1) is defined in table 585.
The VIRTUAL TAPE LIBRARY SPECIFIC TYPE field (see table 586) indicates the type of virtual tape library specific
data in this descriptor.
The ADDITIONAL LENGTH field indicates the number of bytes that follow in this descriptor.
The contents of the virtual tape library specific data depend on the value in the VIRTUAL TAPE LIBRARY SPECIFIC
TYPE field.
Table 584 — CONSTITUENT DEVICE TYPE field
Code
Description
Reference
00h to 1Fh
One of the values defined for the PERIPHERAL DEVICE TYPE field
in the standard INQUIRY data
6.6.2
20h to FEh
Reserved
FFh
Unknown
Table 585 — Virtual tape library constituent type specific descriptor format
Bit
Byte
VIRTUAL TAPE LIBRARY SPECIFIC TYPE
Reserved
ADDITIONAL LENGTH (n-3)
Virtual tape library specific data
•••
n
Table 586 — VIRTUAL TAPE LIBRARY SPECIFIC TYPE field
Code
Description
00h to FEh
Reserved
FFh
Vendor specific


7.8.5.3 Virtual tape drive constituent type specific descriptor
If the CONSTITUENT TYPE field (see 7.8.5.1) is set to 0002h (i.e., virtual tape drive), then the format for each
constituent type specific descriptor (see 7.8.5.1) is defined in table 587.
The VIRTUAL TAPE DRIVE SPECIFIC TYPE field (see table 588) indicates the type of virtual tape drive specific data
in this descriptor.
The ADDITIONAL LENGTH field indicates the number of bytes that follow in this descriptor.
The contents of the virtual tape drive specific data depend on the value in the VIRTUAL TAPE DRIVE SPECIFIC
TYPE field.
7.8.5.4 Direct access block device constituent type specific descriptor
If the CONSTITUENT TYPE field (see 7.8.5.1) is set to 0003h (i.e., direct access block device), then the format for
each constituent type specific descriptor (see 7.8.5.1) is defined in table 589.
Table 587 — Virtual tape drive constituent type specific descriptor format
Bit
Byte
VIRTUAL TAPE DRIVE SPECIFIC TYPE
Reserved
ADDITIONAL LENGTH (n-3)
Virtual tape drive specific data
•••
n
Table 588 — VIRTUAL TAPE DRIVE SPECIFIC TYPE field
Code
Description
00h to FEh
Reserved
FFh
Vendor specific
Table 589 — Direct access block device constituent type specific descriptor format
Bit
Byte
DIRECT ACCESS BLOCK DEVICE SPECIFIC TYPE
Reserved
ADDITIONAL LENGTH (n-3)
Direct access block device specific data
•••
n
