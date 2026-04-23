# 6.6.3 SCSI Parallel Interface specific INQUIRY data

6.6.3 SCSI Parallel Interface specific INQUIRY data
As shown in table 174, portions of bytes 6 and 7 and all of byte 56 of the standard INQUIRY data shall be
used only by SCSI target devices that implement the SCSI Parallel Interface. For details on how the
SPI-specific fields relate to the SCSI Parallel Interface see SPI-n (where n is 2 or greater). Table 180 shows
the SPI-specific standard INQUIRY fields.
A wide SCSI address 16 (ADDR16) bit set to one indicates that the SCSI target device supports 16-bit wide
SCSI addresses. An ADDR16 bit set to zero indicates that the SCSI target device does not support 16-bit wide
SCSI addresses.
A wide bus 16 (WBUS16) bit set to one indicates that the SCSI target device supports 16-bit wide data
transfers. A WBUS16 bit set to zero indicates that the SCSI target device does not support 16-bit wide data
transfers.
A synchronous transfer (SYNC) bit set to one indicates that the SCSI target device supports synchronous data
transfer. A SYNC bit set to zero indicates the SCSI target device does not support synchronous data transfer.
UAS T10/2095-D revision 02
1743h
UAS T10/2095-D revision 04
1747h
UAS ANSI INCITS 471-2010
1748h
UAS-2 (no version claimed)
1780h
Universal Serial Bus Specification, Revision 1.1
1728h
Universal Serial Bus Specification, Revision 2.0
1729h
USB Mass Storage Class Bulk-Only Transport, Revision 1.0
1730h
Version Descriptor Not Supported or No Standard Identified
0000h
Reserved
all others
Table 180 — SPI-specific standard INQUIRY bits
Bit
Byte
n/a a
ADDR16
n/a a
WBUS16
SYNC
n/a a
Obsolete
n/a a
•••
Reserved
CLOCKING
QAS
IUS
a The meanings of these bits and fields are not specific to SPI-5. See table 174 for their definitions.
Table 179 — Version descriptor values (part 12 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


Table 181 defines the relationships between the ADDR16 bit and the WBUS16 bit.
The CLOCKING field shall not apply to asynchronous transfers and is defined in table 182.
A quick arbitration and selection supported (QAS) bit set to one indicates that the target port supports quick
arbitration and selection (see SPI-5). A QAS bit set to zero indicates that the target port does not support quick
arbitration and selection.
An information units supported (IUS) bit set to one indicates that the SCSI target device supports information
unit transfers (see SPI-5). A IUS bit set to zero indicates that the SCSI target device does not support infor-
mation unit transfers.
Table 181 — Maximum logical device configuration table
ADDR16
WBUS16
Description
8-bit wide data path on a single cable with
8 SCSI IDs supported
16-bit wide data path on a single cable
with 8 SCSI IDs supported
16-bit wide data path on a single cable
with 16 SCSI IDs supported
Table 182 — CLOCKING field
Code
Description
00b
Indicates the target port supports only ST (see SPI-5)
01b
Indicates the target port supports only DT (see SPI-5)
10b
Reserved
11b
Indicates the target port supports ST and DT
