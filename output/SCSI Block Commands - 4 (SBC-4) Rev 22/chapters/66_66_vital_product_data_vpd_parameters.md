# 6.6 Vital product data (VPD) parameters

6.6 Vital product data (VPD) parameters
6.6.1 VPD parameters overview
See table 257 for references to the VPD pages used with direct access block devices.
6.6.2 Block Device Characteristics VPD page
Table 257 — VPD page codes for direct access block devices
VPD page name
Page code  a
Reference
Support
ASCII Information
01h to 7Fh
SPC-6
See SPC-6
ATA Information
89h
SAT-4
See SAT-4
Block Device Characteristics
B1h
6.6.2
Optional
Block Device Characteristics Extension
B5h
6.6.3
Optional
Block Limits
B0h
6.6.4
Optional
Block Limits Extension
B7h
6.6.5
Optional
CFA Profile Information
8Ch
SPC-6
See SPC-6
Device Constituents
8Bh
SPC-6
See SPC-6
Device Identification
83h
SPC-6
See SPC-6
Extended INQUIRY Data
86h
SPC-6
See SPC-6
Format Presets
B8h
6.6.6
Optional
Logical Block Provisioning
B2h
6.6.7
Optional
Management Network Addresses
85h
SPC-6
See SPC-6
Mode Page Policy
87h
SPC-6
See SPC-6
Power Condition
8Ah
SPC-6
See SPC-6
Power Consumption
8Dh
SPC-6
See SPC-6
Protocol Specific Logical Unit Information
90h
SPC-6
See SPC-6
Protocol Specific Port Information
91h
SPC-6
See SPC-6
Referrals
B3h
6.6.8
Optional
SCSI Feature Sets
92h
SPC-6
See SPC-6
SCSI Ports
88h
SPC-6
See SPC-6
Software Interface Identification
84h
SPC-6
See SPC-6
Supported VPD Pages
00h
SPC-6
See SPC-6
Third-party Copy
8Fh
SPC-6 and 6.6.9
Optional
Supported Block Lengths and Protection
Types
B4h
6.6.10
Optional
Unit Serial Number
80h
SPC-6
See SPC-6
Zoned Block Device Characteristics
B6h
ZBC-2
See ZBC-2
Reserved for this standard
B8h to BFh
a All page codes for direct access block devices not shown in this table are reserved.


The Block Device Characteristics VPD page (see table 258) contains parameters indicating characteristics of
the logical unit.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in SPC-6.
The PAGE CODE field and PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 258 for the Block Device Characteristics VPD page.
The MEDIUM ROTATION RATE field is shown in table 259.
Table 258 — Block Device Characteristics VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B1h)
(MSB)
PAGE LENGTH (003Ch)
(LSB)
(MSB)
MEDIUM ROTATION RATE
(LSB)
PRODUCT TYPE
WABEREQ
WACEREQ
NOMINAL FORM FACTOR
Reserved
ZONED
RBWZ
BOCS
FUAB
VBULS
Reserved
•••
(MSB)
DEPOPULATION TIME
•••
(LSB)
Reserved
•••
Table 259 — MEDIUM ROTATION RATE field
Code
Description
0000h
Medium rotation rate is not reported
0001h
Non-rotating medium (e.g., solid state)
0002h to 0400h
Reserved
0401h to FFFEh
Nominal medium rotation rate in revolutions per minute (e.g., 7 200 rpm =
1C20h,10 000 rpm = 2710h, and 15 000 rpm = 3A98h)
FFFFh
Reserved


The PRODUCT TYPE field (see table 260) defines the product type of the storage device.
The write after block erase required (WABEREQ) field indicates the device server behavior (see table 261), if a
write operation has not been performed to a mapped LBA since a sanitize block erase operation was
performed and no other error occurs during the processing of a read command specifying that LBA.
Table 260 — PRODUCT TYPE field
Code
Description
00h
Not indicated
01h
CFast™ (see CFast) a d
02h
CompactFlash (see CF)
03h
Memory Stick™ (see MS) b d
04h
MultiMediaCard (see e•MMC)
05h
Secure Digital Card (see SD Card)
06h
XQD™ (see XQD) c d
07h
Universal Flash Storage (see UFS)
08h to EFh
Reserved
F0h to FFh
Vendor specific
a CFast is the trademark of a product supplied by the
CompactFlash Association.
b Memory Stick is the trademark of a product supplied by the
One Stop Site for Formats.
c XQD is the trademark of a product supplied by the
CompactFlash Association.
d This information is given for the convenience of users of this
standard and does not constitute an endorsement of the
product named. Equivalent products may be used if they
lead to the same results.
Table 261 — WABEREQ field
Code
Description
00b
Not specified.
01b
The device server completes the read command specifying that LBA with GOOD status and any
data transferred to the Data-In Buffer is indeterminate.
10b
The device server terminates the read command specifying that LBA with CHECK CONDITION
status with sense key set to MEDIUM ERROR and the additional sense code set to an appropriate
value other than WRITE AFTER SANITIZE REQUIRED (e.g., ID CRC OR ECC ERROR).
11b
The device server terminates the read command specifying that LBA with CHECK CONDITION
status with sense key set to MEDIUM ERROR and the additional sense code set to WRITE
AFTER SANITIZE REQUIRED.


The write after cryptographic erase required (WACEREQ) field indicates the device server behavior
(see table 262), if a write operation has not been performed to a mapped LBA since a sanitize cryptographic
erase operation was performed and no other error occurs during the processing of a read command
specifying that LBA.
The NOMINAL FORM FACTOR field indicates the nominal form factor of the device containing the logical unit and
is shown in table 263.
The ZONED field indicates the type of zoned block capabilities implemented by the device server as shown in
table 264.
A reassign blocks write zero (RBWZ) bit set to one indicates that during the processing of a REASSIGN
BLOCKS command that does not recover logical block data, the device server writes zeros as described in
Table 262 — WACEREQ field
Code
Description
00b
Not specified.
01b
The device server completes the read command specifying that LBA with GOOD status and any
data transferred to the Data-In Buffer is indeterminate.
10b
The device server terminates the read command specifying that LBA with CHECK CONDITION
status with sense key set to MEDIUM ERROR and the additional sense code set to an appropriate
value other than WRITE AFTER SANITIZE REQUIRED (e.g., ID CRC OR ECC ERROR).
11b
The device server terminates the read command specifying that LBA with CHECK CONDITION
status with sense key set to MEDIUM ERROR and the additional sense code set to WRITE
AFTER SANITIZE REQUIRED.
Table 263 — NOMINAL FORM FACTOR field
Code
Description
0h
Nominal form factor is not reported
1h
5.25 inch
2h
3.5 inch
3h
2.5 inch
4h
1.8 inch
5h
Less than 1.8 inch
All others
Reserved
Table 264 — ZONED field
Code
Description
00b
Not reported
01b
Device server implements the host aware zoned block device
capabilities defined in ZBC-2
10b
Device server implements device managed zoned block device
capabilities
11b
Reserved


5.24. A RBWZ bit set to zero indicates that during the processing of a REASSIGN BLOCKS command that
does not recover the logical block data, the device server writes vendor specific data as described in 5.24.
A background operation control supported (BOCS) bit set to one indicates that background operation control is
supported as described in 4.31. A BOCS bit set to zero indicates that background operation control is not
supported.
A force unit access behavior (FUAB) bit set to one indicates that the device server interprets the
SYNCHRONIZE CACHE command and the FUA bit in read commands and write commands in compliance
with this standard. An FUAB bit set to zero indicates that the device server interprets the SYNCHRONIZE
CACHE command and the FUA bit in read commands and write commands in compliance with SBC-2.
A verify byte check unmapped LBA supported (VBULS) bit set to one indicates that the device server supports
unmapped LBAs while processing VERIFY commands (see 5.36, 5.37, 5.38, and 5.39) and WRITE AND
VERIFY commands (see 5.44, 5.45, 5.46, and 5.47) with the BYTCHK field set to 01b. A VBULS bit set to zero
indicates that the device server does not support unmapped LBAs while processing VERIFY commands and
WRITE AND VERIFY commands with the BYTCHK field set to 01b. The device server should set the VBULS bit
to one.
The DEPOPULATION TIME field indicates the maximum time in seconds for the device server to perform the
operations associated with a REMOVE ELEMENT AND TRUNCATE command.
6.6.3 Block Device Characteristics Extension VPD page
The Block Device Characteristics Extension VPD page (see table 265) contains parameters indicating
characteristics of the logical unit.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in SPC-6.
Table 265 — Block Device Characteristics Extension VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B5h)
(MSB)
PAGE LENGTH (007Ch)
(LSB)
Reserved
UTILIZATION TYPE
UTILIZATION UNITS
UTILIZATION INTERVAL
(MSB)
UTILIZATION B
•••
(LSB)
(MSB)
UTILIZATION A
•••
(LSB)
Reserved
•••


The PAGE CODE field and PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 265 for the Block Device Characteristics Extension VPD page.
The UTILIZATION TYPE field (see table 266) indicates the designed utilization characteristics for the direct
access block device based on the contents of the UTILIZATION A field and the UTILIZATION B field evaluated
using the units indicated by the UTILIZATION UNITS field over the time interval indicated by the UTILIZATION
INTERVAL field.
The UTILIZATION UNITS field (see table 267) indicates the units of measure for the values, if any, in the
UTILIZATION A field and the UTILIZATION B field.
The UTILIZATION INTERVAL field (see table 268) indicates a nominal calendar time reference interval over which
the values, if any, in the UTILIZATION A field and the UTILIZATION B field may be applied.
The UTILIZATION B field and the UTILIZATION A field indicate the designed utilization characteristics for the direct
access block device as:
a)
defined by the UTILIZATION TYPE field;
b)
expressed in the units defined by the UTILIZATION UNITS field; and
c)
over the time interval defined by the UTILIZATION INTERVAL field.
Table 266 — UTILIZATION TYPE field
Code
Description
01h
Combined writes and reads: the UTILIZATION A field contains designed number of host
requested bytes transferred by write operations and host requested bytes transferred by
read operations. The UTILIZATION B field is reserved.
02h
Writes only: the UTILIZATION A field contains designed number of host requested bytes
transferred by write operations. The UTILIZATION B field is reserved.
03h
Separate writes and reads: the UTILIZATION A field contains designed number of host
requested bytes transferred by write operations. The UTILIZATION B field contains
designed number of host requested bytes transferred by read operations.
all others
Reserved
Table 267 — UTILIZATION UNITS field
Code
Description
02h
megabytes
03h
gigabytes
04h
terabytes
05h
petabytes
06h
exabytes
all others
Reserved
Table 268 — UTILIZATION INTERVAL field
Code
Description
0Ah
per day
0Eh
per year
all others
Reserved


6.6.4 Block Limits VPD page
The Block Limits VPD page (see table 269) provides the application client with the means to obtain certain
operating parameters of the logical unit.
Table 269 — Block Limits VPD page (part 1 of 2)
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B0h)
(MSB)
PAGE LENGTH (003Ch)
(LSB)
Reserved
WSNZ
MAXIMUM COMPARE AND WRITE LENGTH
(MSB)
OPTIMAL TRANSFER LENGTH GRANULARITY
(LSB)
(MSB)
MAXIMUM TRANSFER LENGTH
•••
(LSB)
(MSB)
OPTIMAL TRANSFER LENGTH
•••
(LSB)
(MSB)
MAXIMUM PREFETCH LENGTH
•••
(LSB)
(MSB)
MAXIMUM UNMAP LBA COUNT
•••
(LSB)
(MSB)
MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT
•••
(LSB)
(MSB)
OPTIMAL UNMAP GRANULARITY
•••
(LSB)
UGAVALID
(MSB)
UNMAP GRANULARITY ALIGNMENT
•••
(LSB)
(MSB)
MAXIMUM WRITE SAME LENGTH
•••
(LSB)
(MSB)
MAXIMUM ATOMIC TRANSFER LENGTH
•••
(LSB)


The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in SPC-6.
The PAGE CODE field and PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 269 for the Block Limits VPD page.
A write same non-zero (WSNZ) bit set to one indicates that the device server does not support a value of zero
in the NUMBER OF LOGICAL BLOCKS field in the WRITE SAME command CDBs (see 5.52, 5.53, and 5.54). A
WSNZ bit set to zero indicates that the device server may or may not support a value of zero in the NUMBER OF
LOGICAL BLOCKS field of the WRITE SAME commands.
A MAXIMUM COMPARE AND WRITE LENGTH field set to a non-zero value indicates the maximum value that the
device server accepts in the NUMBER OF LOGICAL BLOCKS field in the COMPARE AND WRITE command
(see 5.3). A MAXIMUM COMPARE AND WRITE LENGTH field set to 00h indicates that the device server does not
support the COMPARE AND WRITE command. If the MAXIMUM TRANSFER LENGTH field is not set to zero, then
the device server shall set the MAXIMUM COMPARE AND WRITE LENGTH field to a value less than or equal to the
value in the MAXIMUM TRANSFER LENGTH field.
An OPTIMAL TRANSFER LENGTH GRANULARITY field set to a non-zero value indicates the optimal transfer length
granularity size in logical blocks for a single command shown in the command column of table 33. If a device
server receives one of these commands with a transfer size that is not equal to a multiple of this value, then
the device server may incur delays in processing the command. An OPTIMAL TRANSFER LENGTH GRANULARITY
field set to 0000h indicates that the device server does not report optimal transfer length granularity.
A MAXIMUM TRANSFER LENGTH field set to a non-zero value indicates the maximum transfer length in logical
blocks that the device server accepts for a single command shown in table 33. If a device server receives one
of these commands with a transfer size greater than this value, then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to the value shown in table 33. A MAXIMUM TRANSFER LENGTH field set to 0000_0000h indicates
that the device server does not report a limit on the transfer length.
An OPTIMAL TRANSFER LENGTH field set to a non-zero value indicates the optimal transfer size in logical blocks
for a single command shown in table 33. If a device server receives one of these commands with a transfer
size greater than this value, then the device server may incur delays in processing the command. An OPTIMAL
TRANSFER LENGTH field set to 0000_0000h indicates that the device server does not report an optimal transfer
size.
The MAXIMUM PREFETCH LENGTH field indicates the maximum prefetch length in logical blocks that the device
server accepts for a single PRE-FETCH command. If the MAXIMUM TRANSFER LENGTH field is not set to zero,
then the device server should set the MAXIMUM PREFETCH LENGTH field to a value less than or equal to the
value in the MAXIMUM TRANSFER LENGTH field.
(MSB)
ATOMIC ALIGNMENT
•••
(LSB)
(MSB)
ATOMIC TRANSFER LENGTH GRANULARITY
•••
(LSB)
(MSB)
MAXIMUM ATOMIC TRANSFER LENGTH WITH ATOMIC BOUNDARY
•••
(LSB)
(MSB)
MAXIMUM ATOMIC BOUNDARY SIZE
•••
(LSB)
Table 269 — Block Limits VPD page (part 2 of 2)
Bit
Byte


A MAXIMUM UNMAP LBA COUNT field set to a non-zero value indicates the maximum number of LBAs that may
be unmapped by an UNMAP command (see 5.35). If the number of LBAs that may be unmapped by an
UNMAP command is constrained only by the amount of data that may be contained in the UNMAP parameter
list (see 5.35.2), then the device server shall set the MAXIMUM UNMAP LBA COUNT field to FFFF_FFFFh. If the
device server implements the UNMAP command, then the value in this field shall be greater than or equal to
one. A MAXIMUM UNMAP LBA COUNT field set to 0000_0000h indicates that the device server does not
implement the UNMAP command.
A MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT field set to a non-zero value indicates the maximum number of
UNMAP block descriptors (see 5.35.2) that shall be contained in the parameter data transferred to the device
server for an UNMAP command (see 5.35). If there is no limit on the number of UNMAP block descriptors
contained in the parameter data, then the device server shall set the MAXIMUM UNMAP BLOCK DESCRIPTOR
COUNT field to FFFF_FFFFh. If the device server implements the UNMAP command, then the value in the
MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT field shall be greater than or equal to one. A MAXIMUM UNMAP BLOCK
DESCRIPTOR COUNT field set to 0000_0000h indicates that the device server does not implement the UNMAP
command.
An OPTIMAL UNMAP GRANULARITY field set to a non-zero value indicates the optimal granularity in logical blocks
for unmap requests (e.g., an UNMAP command or a WRITE SAME (16) command with the UNMAP bit set to
one). An unmap request with a number of logical blocks that is not a multiple of this value may result in unmap
operations on fewer LBAs than requested. An OPTIMAL UNMAP GRANULARITY field set to 0000_0000h indicates
that the device server does not report an optimal unmap granularity.
An unmap granularity alignment valid (UGAVALID) bit set to one indicates that the UNMAP GRANULARITY
ALIGNMENT field is valid. A UGAVALID bit set to zero indicates that the UNMAP GRANULARITY ALIGNMENT field is not
valid.
The UNMAP GRANULARITY ALIGNMENT field indicates the LBA of the first logical block to which the OPTIMAL
UNMAP GRANULARITY field applies. The unmap granularity alignment is used to calculate an optimal unmap
request starting LBA as follows:
optimal unmap request starting LBA = (n × optimal unmap granularity) + unmap granularity alignment
where:
n
is zero or any positive integer value;
optimal unmap granularity
is the value in the OPTIMAL UNMAP GRANULARITY field; and
unmap granularity alignment
is the value in the UNMAP GRANULARITY ALIGNMENT field.
An unmap request with a starting LBA that is not optimal may result in unmap operations on fewer LBAs than
requested.
A MAXIMUM WRITE SAME LENGTH field set to a non-zero value indicates the maximum number of contiguous
logical blocks that the device server allows to be unmapped or written in a single WRITE SAME command. A
MAXIMUM WRITE SAME LENGTH field set to 0000_0000h indicates that the device server does not report a limit
on the number of logical blocks that it allows to be unmapped or written in a single WRITE SAME command.
If the ATOMIC BOUNDARY field in the the WRITE ATOMIC (16) command (see 5.48) or WRITE ATOMIC (32)
command (see 5.49) is set to 0000h, then a MAXIMUM ATOMIC TRANSFER LENGTH field set to a non-zero value
indicates the maximum atomic transfer length in logical blocks that the device server supports for a single
atomic write command (see 4.29). A MAXIMUM ATOMIC TRANSFER LENGTH field set to 0000_0000h indicates that
the device server does not indicate a maximum atomic transfer length. The maximum atomic transfer length
indicated by the MAXIMUM ATOMIC TRANSFER LENGTH field shall be less than or equal to the maximum transfer
length indicated by the MAXIMUM TRANSFER LENGTH field. The maximum atomic transfer length indicated by the
MAXIMUM ATOMIC TRANSFER LENGTH field shall be a multiple of the value in the ATOMIC TRANSFER LENGTH
GRANULARITY field. If the ATOMIC BOUNDARY field is set to a non-zero value, then the MAXIMUM ATOMIC TRANSFER
LENGTH field is ignored.
The ATOMIC ALIGNMENT field indicates the required alignment of the starting LBA in an atomic write command.
If the ATOMIC ALIGNMENT field is set to 0000_0000h, then there is no alignment requirement for atomic write
commands.


If the ATOMIC ALIGNMENT field is non-zero, then the starting LBA of an atomic write request shall meet the
following:
atomic request starting LBA = n × atomic alignment
where:
The ATOMIC TRANSFER LENGTH GRANULARITY field indicates the minimum transfer length for an atomic write
command. Atomic write operations are required to have a transfer length that is a multiple of the atomic
transfer length granularity. An ATOMIC TRANSFER LENGTH GRANULARITY field set to 0000_0000h indicates that
there is no atomic transfer length granularity requirement.
If the ATOMIC BOUNDARY field in the WRITE ATOMIC (16) command (see 5.48) or WRITE ATOMIC (32)
command (see 5.49) is set to a non-zero value, then a MAXIMUM ATOMIC TRANSFER LENGTH WITH ATOMIC
BOUNDARY field set to a non-zero value indicates the maximum transfer length in logical blocks that the device
server supports for a single atomic write command (see 4.29). A MAXIMUM ATOMIC TRANSFER LENGTH WITH
ATOMIC BOUNDARY field set to 0000_0000h indicates that the device server does not indicate a maximum
atomic transfer length with atomic boundary. The maximum atomic transfer length with atomic boundary
indicated by the MAXIMUM ATOMIC TRANSFER LENGTH WITH ATOMIC BOUNDARY field shall be less than or equal to
the maximum transfer length indicated by the MAXIMUM TRANSFER LENGTH field. The maximum atomic transfer
length with atomic boundary indicated by the MAXIMUM ATOMIC TRANSFER LENGTH WITH BOUNDARY field shall be
a multiple of the value in the ATOMIC TRANSFER LENGTH GRANULARITY field. If the ATOMIC BOUNDARY field is set
to 0000h, then the MAXIMUM ATOMIC TRANSFER LENGTH WITH ATOMIC BOUNDARY field is ignored.
A MAXIMUM ATOMIC BOUNDARY SIZE field set to a non-zero value indicates that the device server supports
atomic write commands performing more than one atomic write operation. The maximum atomic boundary
size indicates the maximum number of logical blocks on which the device server is able to perform atomicwrite
operations (see 4.29.1). A MAXIMUM ATOMIC BOUNDARY SIZE field set to 0000h indicates that the device server
does not support atomic write commands performing more than one atomic write operation. The MAXIMUM
ATOMIC BOUNDARY SIZE field shall be a multiple of the value in the ATOMIC TRANSFER LENGTH GRANULARITY field.
6.6.5 Block Limits Extension VPD page
The Block Limits Extension VPD page (see table 270) provides the application client with the means to obtain
certain operating parameters of the logical unit.
n
is zero or any positive integer value; and
atomic alignment
is the value in the ATOMIC ALIGNMENT field.
Table 270 — Block Limits Extension VPD page (part 1 of 2)
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B7h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Reserved
(MSB)
MAXIMUM NUMBER OF STREAMS
(LSB)
(MSB)
OPTIMAL STREAM WRITE SIZE
(LSB)


The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in SPC-6.
The PAGE CODE field is defined in SPC-6 and shall be set to the values shown in table 270 for the Block Limits
Extension VPD page.
The MAXIMUM NUMBER OF STREAMS field indicates the maximum number of streams that the device server
supports and the maximum value for the stream identifier. A MAXIMUM NUMBER OF STREAMS field set to 0000h
indicates that the device server does not support stream control.
The OPTIMAL STREAM WRITE SIZE field indicates the alignment and size of the optimal stream write as a number
of logical blocks. The optimal stream write size is the same for all streams in the device server.
The STREAM GRANULARITY SIZE field indicates the stream granularity size in number of optimal stream write
size blocks as described in 4.32.
A MAXIMUM SCATTERED LBA RANGE TRANSFER LENGTH field set to a non-zero value indicates the maximum value
that the device server supports in the NUMBER OF LOGICAL BLOCKS field for a single LBA range descriptor in a
WRITE SCATTERED command (see 5.55 and 5.56). A MAXIMUM SCATTERED LBA RANGE TRANSFER LENGTH
field set to 0000_0000h indicates that the device server does not report a limit.
A MAXIMUM SCATTERED LBA RANGE DESCRIPTOR COUNT field set to a non-zero value indicates the maximum
number of LBA range descriptors that the device server supports for a single WRITE SCATTERED command
(see 5.55 and 5.56). A MAXIMUM SCATTERED LBA RANGE DESCRIPTOR COUNT field set to 0000h indicates that the
device server does not report a limit.
A MAXIMUM SCATTERED TRANSFER LENGTH field set to a non-zero value indicates the maximum transfer length
in logical blocks that the device server accepts for a single WRITE SCATTERED command (see 5.55 and
5.56). A MAXIMUM SCATTERED TRANSFER LENGTH field set to 0000_0000h indicates that the device server does
not report a limit.
(MSB)
STREAM GRANULARITY SIZE
•••
(LSB)
Reserved
(MSB)
MAXIMUM SCATTERED LBA RANGE TRANSFER LENGTH
•••
(LSB)
Reserved
(MSB)
MAXIMUM SCATTERED LBA RANGE DESCRIPTOR COUNT
(LSB)
(MSB)
MAXIMUM SCATTERED TRANSFER LENGTH
•••
(LSB)
Reserved
•••
n
Table 270 — Block Limits Extension VPD page (part 2 of 2)
Bit
Byte


6.6.6 Format Presets VPD page
6.6.6.1 Format Presets VPD page overview
The Format Presets VPD page (see table 271) provides a means to retrieve the descriptions for the presets
that are specified by the PRESET IDENTIFIER field in the FORMAT WITH PRESET command (see 5.5).
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in SPC-6.
The PAGE CODE field is defined in SPC-6 and shall be set as shown in table 271 for the Format Presets VPD
page.
Table 271 — Format Presets VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B8h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Format preset descriptors list
Format preset descriptor [first] (see table 272)
•••
•••
n-63
Format preset descriptor [last] (see table 272)
•••
n


Each format preset descriptor (see table 272) contains information about one preset used by the FORMAT
WITH PRESET command.
Table 272 — Format preset descriptor
Bit
Byte
(MSB)
PRESET IDENTIFIER
•••
(LSB)
SCHEMA TYPE
Reserved
Reserved
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT
(MSB)
LOGICAL BLOCK LENGTH
•••
(LSB)
Reserved
•••
(MSB)
DESIGNED LAST LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
•••
FMPTINFO
Reserved
PROTECTION FIELD USAGE
Reserved
PROTECTION INTERVAL EXPONENT
(MSB)
Schema type specific information
•••
(LSB)


If the contents of the PRESET IDENTIFIER field (see table 273) is equal to the content of the PRESET IDENTIFIER
field in a FORMAT WITH PRESET command (see 5.5), then this format preset descriptor is selected for use in
the processing of that FORMAT WITH PRESET command.
Table 273 — PRESET IDENTIFIER field
 Code
Description
SCHEMA TYPE
field
(see table 274)
0000_0000h
Default non-zoned with 512-bytes of user
data in each logical block a
01h
0000_0001h
Default host aware zoned block device
model (see ZBC-2) with 512-bytes of user
data in each logical block a
02h
0000_0002h
Default host managed zoned block device
model (see ZBC-2) with 512-bytes of user
data in each logical block a
03h
0000_0003h to
0000_00FFh
Reserved
0000_0100h
Default non-zoned with 4 096-bytes of
user data in each logical block b
01h
0000_0101h
Default host aware zoned block device
model (see ZBC-2) with 4 096-bytes of
user data in each logical block b
02h
0000_0102h
Default host managed zoned block device
model (see ZBC-2) with 4 096-bytes of
user data in each logical block b
03h
0000_0103h to
0000_FFFFh
Reserved
all others
Vendor specific
a In this format preset descriptor, the LOGICAL BLOCK LENGTH field shall be set to
0000_0200h and the LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field shall
be set to 0h or 3h.
b In this format preset descriptor, the LOGICAL BLOCK LENGTH field shall be set to
0000_1000h and the LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field shall
be set to 0h.


The SCHEMA TYPE field (see table 274) indicates the overall format described by this format preset descriptor.
The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field indicates the value of x where the number of logical
blocks in one physical block is 2x for this format preset descriptor.
The LOGICAL BLOCK LENGTH field indicates the number of bytes of user data in a logical block for this format
preset descriptor.
The DESIGNED LAST LOGICAL BLOCK ADDRESS field indicates the value that this format preset descriptor is
designed to return in the RETURNED LOGICAL BLOCK ADDRESS field of a subsequent READ CAPACITY (16)
command (see 5.21). The value actually returned in the RETURNED LOGICAL BLOCK ADDRESS field of a
subsequent READ CAPACITY (16) command is affected by the value of the FMTMAXLBA bit (see 5.5) and the
condition of the media being formatted.
The FMTPINFO field, PROTECTION FIELD USAGE field, and PROTECTION INTERVAL EXPONENT field are defined in
5.4.
The contents of the schema type specific information depends on the schema type (see table 274).
Table 274 — SCHEMA TYPE field
 Code
Description
Schema type
specific
information
(see table 272)
01h
This format preset descriptor does not
define any zones (i.e., none of the
requirements in ZBC-2 apply).
Reserved
02h
This format preset descriptor defines the
zones in the host aware zoned block
device model (see ZBC-2).
See 6.6.6.2
03h
This format preset descriptor defines the
zones in the host managed zoned block
device model (see ZBC-2).
See 6.6.6.3
all others
Reserved


6.6.6.2 Host aware zones schema type specific information
If the SCHEMA TYPE field is set to 02h, then the schema type specific information is shown in table 275.
The LOW LBA CONVENTIONAL ZONES PERCENTAGE field indicates the approximate percentage of the zones
formatted as conventional zones (see ZBC-2) starting with LBA 0.
The HIGH LBA CONVENTIONAL ZONES PERCENTAGE field indicates the approximate percentage of the zones
formatted as conventional zones ending with the largest valued LBA formatted.
The units for the conventional zones percentages are tenths of a percent (e.g., 0 indicates 0%, 1 indicates
0.1%, 10 indicates 1.0%, 255 indicates 25.5%).
The actual number of zones formatted as conventional zones depends on several factors (e.g., the number of
logical blocks in a zone). Zones that are not formatted as conventional zones are formatted as sequential
write preferred write pointer zones (see ZBC-2).
The LOGICAL BLOCKS PER ZONE field indicates the number of logical blocks in each zone. A LOGICAL BLOCKS
PER ZONE field set to zero indicates that the number of logical blocks in a zone is not reported.
Table 275 — Host aware zones schema type specific information
Bit
Byte
LOW LBA CONVENTIONAL ZONES PERCENTAGE
HIGH LBA CONVENTIONAL ZONES PERCENTAGE
Reserved
•••
(MSB)
LOGICAL BLOCKS PER ZONE
•••
(LSB)
Reserved
•••


6.6.6.3 Host managed zones schema type specific information
If the SCHEMA TYPE field is set to 03h, then the schema type specific information is shown in table 276.
The LOW LBA CONVENTIONAL ZONES PERCENTAGE field indicates the approximate percentage of the zones
formatted as conventional zones (see ZBC-2) starting with LBA 0.
The HIGH LBA CONVENTIONAL ZONES PERCENTAGE field indicates the approximate percentage of the zones
formatted as conventional zones ending with the largest valued LBA formatted.
The units for the conventional zones percentages are tenths of a percent (e.g., 0 indicates 0%, 1 indicates
0.1%, 10 indicates 1.0%, 255 indicates 25.5%).
The actual number of zones formatted as conventional zones depends on several factors (e.g., the number of
logical blocks in a zone). Zones that are not formatted as conventional zones are formatted as sequential
write required write pointer zones (see ZBC-2).
The LOGICAL BLOCKS PER ZONE field indicates the number of logical blocks in each zone. A LOGICAL BLOCKS
PER ZONE field set to zero indicates that the number of logical blocks in a zone is not reported.
Table 276 — Host managed zones schema type specific information
Bit
Byte
LOW LBA CONVENTIONAL ZONES PERCENTAGE
HIGH LBA CONVENTIONAL ZONES PERCENTAGE
Reserved
•••
(MSB)
LOGICAL BLOCKS PER ZONE
•••
(LSB)
Reserved
•••


6.6.7 Logical Block Provisioning VPD page
The Logical Block Provisioning VPD page (see table 277) provides the application client with logical block
provisioning related operating parameters of the logical unit.
The PERIPHERAL QUALIFIER field is defined in SPC-6.
The PAGE CODE field and PERIPHERAL DEVICE TYPE field are defined in SPC-6 and shall be set to the value
shown in table 277 for the Logical Block Provisioning VPD page.
The PAGE LENGTH field is defined in SPC-6. If the DP bit is set to zero, then the PAGE LENGTH field shall be set
to 0004h. If the DP bit is set to one, then the PAGE LENGTH field shall be set to n-3 as shown in table 277.
If the Logical Block Provisioning log page (see 6.4.5.1) is supported, then the logical unit shall support:
a)
logical block provisioning threshold sets; or
b)
logical block provisioning percentages.
The THRESHOLD EXPONENT field indicates the threshold set size as described in 4.7.3.7.2. A THRESHOLD
EXPONENT field set to zero indicates that the logical unit does not support logical block provisioning threshold
sets.
If logical block provisioning threshold sets  are supported, then the threshold exponent shall be a non-zero
value selected such that:
(capacity ÷ 2(threshold exponent)) < 2(32)
where:
capacity
is 1 + the LBA of the last logical block as returned in the READ
CAPACITY (16) parameter data (see 5.21.2) (i.e., the number of logical
blocks on the direct access block device);
threshold exponent
is the contents of the THRESHOLD EXPONENT field; and
2(32)
is the constant value 1_0000_0000h (i.e., 4 294 967 296).
A THRESHOLD PERCENTAGE field set to zero indicates that the logical unit does not support logical block
provisioning percentages. If logical block provisioning percentages are supported, then the threshold
percentage shall be set to a non-zero value selected from the values in table 278. The units for the threshold
Table 277 — Logical Block Provisioning VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE (00000b)
PAGE CODE (B2h)
(MSB)
PAGE LENGTH (0004h or (n - 3))
(LSB)
THRESHOLD EXPONENT
LBPU
LBPWS
LBPWS10
LBPRZ
ANC_SUP
DP
MINIMUM PERCENTAGE
PROVISIONING TYPE
THRESHOLD PERCENTAGE
PROVISIONING GROUP DESCRIPTOR (if any)
•••
n


percentage is tenths of a percent. This percentage represents the range over which logical block provisioning
threshold percentages operates as described in 4.7.3.7.3.
A MINIMUM PERCENTAGE field set to zero indicates that the logical unit does not report a minimum percentage
of resources required by the device. A MINIMUM PERCENTAGE field set to a non-zero value indicates the
minimum percentage of resources required by the device server as described in table 279. This value
indicates the point where a device server may begin device initiated advanced background operations.
A logical block provisioning UNMAP command (LBPU) bit set to one indicates that the device server supports
the UNMAP command (see 5.35). An LBPU bit set to zero indicates that the device server does not support the
UNMAP command.
A logical block provisioning WRITE SAME (16) command (LBPWS) bit set to one indicates that the device
server supports the use of the WRITE SAME (16) command (see 5.53) to unmap LBAs. An LBPWS bit set to
zero indicates that the device server does not support the use of the WRITE SAME (16) command to unmap
LBAs.
A logical block provisioning WRITE SAME (10) command (LBPWS10) bit set to one indicates that the device
server supports the use of the WRITE SAME (10) command (see 5.52) to unmap LBAs. An LBPWS10 bit set to
zero indicates that the device server does not support the use of the WRITE SAME (10) command to unmap
LBAs.
The logical block provisioning read zeros (LBPRZ) field is described in table 280. See table 10 for the definition
of the logical block data returned by a read operation from an unmapped LBA for the different values of the
LBPRZ field.
An anchor supported (ANC_SUP) bit set to one indicates that the device server supports anchored LBAs
(see 4.7.1). An ANC_SUP bit set to zero indicates that the device server does not support anchored LBAs.
Table 278 — THRESHOLD PERCENTAGE field
Code
Description
The logical unit does not support logical block provisioning percentages
1 to 255
(i.e., 01h to FFh)
0.1% to 25.5% of the total allocation resources
Table 279 — MINIMUM PERCENTAGE field
Code
Description
The logical unit does not report a minimum percentage of resources required
1 to 30
(i.e., 01h to 1Eh)
1% to 30% of the total allocation resources
All others
Reserved
Table 280 — LBPRZ field
Code
Description
000b
The logical block data represented by unmapped LBAs (see 4.7.4.4) is vendor
specific
xx1b
The logical block data represented by unmapped LBAs is set to zeros
010b
The logical block data represented by unmapped LBAs is set to the
provisioning initialization pattern
all others
Reserved


A descriptor present (DP) bit set to one indicates a PROVISIONING GROUP DESCRIPTOR field is present. A DP bit
set to zero indicates a PROVISIONING GROUP DESCRIPTOR field is not present.
The PROVISIONING TYPE field is shown in table 281.
The PROVISIONING GROUP DESCRIPTOR field, if any, contains a designation descriptor (see SPC-6) for the LBA
mapping resources used by this logical unit.
If a PROVISIONING GROUP DESCRIPTOR field is present:
a)
the ASSOCIATION field shall be set to 00b (i.e. logical unit); and
b)
the DESIGNATOR TYPE field shall be set to:
A) 1h (i.e., T10 vendor ID based);
B) 3h (i.e., NAA); or
C) Ah (i.e., UUID identifier).
6.6.8 Referrals VPD page
The Referrals VPD page (see table 282) contains parameters indicating characteristics of the user data
segments contained within this logical unit.
The PERIPHERAL QUALIFIER field is defined in SPC-6.
The PAGE CODE field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in SPC-6 and shall be
set to the values shown in table 282 for the Referrals VPD page.
Table 281 — PROVISIONING TYPE field
Code
Description
000b
The device server does not report a provisioning type
or may be fully provisioned.
001b
The logical unit is resource provisioned (see 4.7.3.2).
010b
The logical unit is thin provisioned (see 4.7.3.3).
All others
Reserved
Table 282 — Referrals VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE (00000b)
PAGE CODE (B3h)
(MSB)
PAGE LENGTH (000Ch)
(LSB)
Reserved
•••
(MSB)
USER DATA SEGMENT SIZE
•••
(LSB)
(MSB)
USER DATA SEGMENT MULTIPLIER
•••
(LSB)


A USER DATA SEGMENT SIZE field set to a non-zero value indicates the number of contiguous logical blocks in a
user data segment (see 4.26.2). A USER DATA SEGMENT SIZE field set to zero indicates the user data segment
size information (i.e., the first user data segment LBA to the last user data segment LBA) is as indicated in the
user data segment referral descriptor (see table 18).
The USER DATA SEGMENT MULTIPLIER field is used by an application client to calculate the beginning LBA of
each user data segment as described in 4.26.2.
6.6.9 Third-party Copy VPD page
6.6.9.1 Third-party Copy VPD page overview
The Third-party Copy VPD page (see SPC-6) provides a means to retrieve third-party copy descriptors
including a descriptor that describes operating parameters for the POPULATE TOKEN command (see 5.12)
and the WRITE USING TOKEN command (see 5.59).
6.6.9.2 Block device third-party copy descriptor type codes
Block device third-party copy descriptor type codes (see table 283) indicate which third-party copy descriptor
is being returned.
Table 283 — Block device third-party copy descriptor type codes
 Descriptor
code
Third-party copy descriptor name
Reference
Support
requirements
0000h
Block Device ROD Limits
6.6.9.3
See a
All other codes
See SPC-6
See SPC-6
See SPC-6
a Mandatory if the POPULATE TOKEN command and the WRITE USING TOKEN command are
supported.


6.6.9.3 Block Device ROD  Limits descriptor
The Block Device ROD Limits descriptor (see table 284) is a third-party copy descriptor in the Third-party
Copy VPD page (see SPC-6) that provides the application client with a method to obtain operating parameters
for direct access block device ROD token operations (see 4.28).
The THIRD-PARTY COPY DESCRIPTOR TYPE field and the THIRD-PARTY COPY DESCRIPTOR LENGTH field are defined
in SPC-6 and shall be set to the values shown in table 284 for the Block Device ROD Limits descriptor.
The MAXIMUM RANGE DESCRIPTORS field indicates the maximum number of block device range descriptors that
may be specified in the parameter data of a POPULATE TOKEN command (see 5.12) and the parameter data
of a WRITE USING TOKEN command (see 5.59). If the MAXIMUM RANGE DESCRIPTORS field is set to zero, then
the copy manager does not report a maximum number of block device range descriptors.
The MAXIMUM INACTIVITY TIMEOUT field indicates the maximum value in the INACTIVITY TIMEOUT field of the
parameter data of a POPULATE TOKEN command that is accepted by the copy manager. If the MAXIMUM
INACTIVITY TIMEOUT field is set to zero, then the device server does not report a maximum inactivity timeout
value. If the MAXIMUM INACTIVITY TIMEOUT field is set to FFFF_FFFFh then there is no maximum value that may
be specified in the INACTIVITY TIMEOUT field in the parameter data of the POPULATE TOKEN command.
The DEFAULT INACTIVITY TIMEOUT field indicates the inactivity timeout value that is used if the INACTIVITY
TIMEOUT field in the parameter data of a POPULATE TOKEN command is set to zero. If the DEFAULT INACTIVITY
TIMEOUT field is set to zero, then the copy manager does not report a default inactivity timeout value.
Table 284 — Block Device ROD Limits descriptor
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0000h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (0020h)
(LSB)
Vendor specific
•••
(MSB)
MAXIMUM RANGE DESCRIPTORS
(LSB)
(MSB)
MAXIMUM INACTIVITY TIMEOUT
•••
(LSB)
(MSB)
DEFAULT INACTIVITY TIMEOUT
•••
(LSB)
(MSB)
MAXIMUM TOKEN TRANSFER SIZE
•••
(LSB)
(MSB)
OPTIMAL TRANSFER COUNT
•••
(LSB)


The MAXIMUM TOKEN TRANSFER SIZE field indicates the maximum size in logical blocks that may be specified by
the sum of the NUMBER OF LOGICAL BLOCKS fields in all block device range descriptors for the following
commands:
a)
POPULATE TOKEN; and
b)
WRITE USING TOKEN.
If the MAXIMUM TOKEN TRANSFER SIZE field is set to zero, then the copy manager does not report a maximum
token transfer size.
If the MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type specific features descriptor in the ROD
token features third-party copy descriptor in the Third-party Copy VPD page (see SPC-6) is reported, then the
MAXIMUM TOKEN TRANSFER SIZE field shall be set to the number of logical blocks that represents the value in the
MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type specific features descriptor in the ROD token
features third-party copy descriptor in the Third-party Copy VPD page.
The OPTIMAL TRANSFER COUNT field indicates the optimal number of logical blocks that the copy manager is
able to transfer. If the sum of the NUMBER OF LOGICAL BLOCKS fields in all block device range descriptors in the
parameter data of a POPULATE TOKEN command or the parameter data of a WRITE USING TOKEN
command exceeds this value then, a delay in processing the request may be incurred. If the field is set to
zero, then the copy manager does not report an optimal transfer count.
If the OPTIMAL BYTES IN BLOCK ROD TRANSFER field in the block ROD device type specific features descriptor in
the ROD token features third-party copy descriptor in the Third-party Copy VPD page is reported, then the
OPTIMAL TRANSFER COUNT field shall be set to the number of logical blocks that represents the value in the
OPTIMAL BYTES IN BLOCK ROD TRANSFER field in the block ROD device type specific features descriptor in the
ROD token features third-party copy descriptor in the Third-party Copy VPD page.
6.6.10 Supported Block Lengths and Protection Types VPD page
The Supported Block Lengths and Protection Types VPD page (see table 285) contains parameters indicating
the specific protection types (see 4.21) supported for each supported logical block length. If the SBLP bit is set
to zero in the Control mode page (See SPC-6), then the device server shall not support this VPD page.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in SPC-6.
The PAGE CODE field is defined in SPC-6 and shall be set to the value shown in table 285 for the Supported
Logical Block Lengths and Protection Types VPD page.
Table 285 — Supported Block Lengths and Protection Types VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (B4h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Logical block length and protection types descriptor list
Logical block length and protection types descriptor [first]
•••
•••
n-7
Logical block length and protection types descriptor [last]
•••
n


The PAGE LENGTH field is defined in SPC-6.
The logical block length and protection types descriptor list shall contain one logical block length and
protection types descriptor for each logical block length that the device server supports.
Each logical block length and protection types descriptor describes the protection types supported for the
logical block length indicated (see table 286).
The LOGICAL BLOCK LENGTH field indicates the logical block length in bytes of user data that is supported by the
device server for which the device server supports the protection types identified in the P_I_I_SUP bit, T3PS bit,
T2PS bit, T1PS bit, T0PS bit, GRD_CHK bit, APP_CHK bit, and REF_CHK bit. If protection information is not
supported, then the T0PS bit shall be set to one.
A protection information interval supported (P_I_I_SUP) bit set to one indicates that the logical unit supports
protection information intervals for the indicated logical block length. A P_I_I_SUP bit set to zero indicates that
the logical unit does not support protection information intervals for the indicated logical block length.
A no protection information checking (NO_PI_CHK) bit set to one indicates that the device server disables
checking of all protection information for the associated protection information interval when performing a
write operation if:
a)
the LOGICAL BLOCK APPLICATION TAG field is set to FFFFh and type 1 protection (see 4.21) is enabled;
b)
the LOGICAL BLOCK APPLICATION TAG field is set to FFFFh and type 2 protection is enabled; or
c)
the LOGICAL BLOCK APPLICATION TAG field is set to FFFFh, the LOGICAL BLOCK REFERENCE TAG field is
set to FFFF FFFFh, and type 3 protection is enabled.
A NO_PI_CHK bit set to zero indicates that the device server checks protection information as specified by the
WRPROTECT field when performing a write operation.
A guard check (GRD_CHK) bit set to zero indicates that the device server does not check the LOGICAL BLOCK
GUARD field in the protection information, if any, for the indicated logical block length. A GRD_CHK bit set to one
indicates that the device server checks the LOGICAL BLOCK GUARD field in the protection information, if any, for
the indicated logical block length.
An application tag check (APP_CHK) bit set to zero indicates that the device server does not check the LOGICAL
BLOCK APPLICATION TAG field in the protection information, if any, for the indicated logical block length. An
APP_CHK bit set to one indicates that the device server checks the LOGICAL BLOCK APPLICATION TAG field in the
protection information, if any, for the indicated logical block length.
A reference tag check (REF_CHK) bit set to zero indicates that the device server does not check the LOGICAL
BLOCK REFERENCE TAG field in the protection information, if any, for the indicated logical block length. A
REF_CHK bit set to one indicates that the device server checks the LOGICAL BLOCK REFERENCE TAG field in the
protection information, if any, for the indicated logical block length.
A type 3 protection supported (T3PS) bit set to one indicates that type 3 protection is supported for the
indicated logical block length. A T3PS bit set to zero indicates that type 3 protection is not supported for the
indicated logical block length.
Table 286 — Logical block length and protection types descriptor format
Bit
Byte
(MSB)
LOGICAL BLOCK LENGTH
•••
(LSB)
Reserved
P_I_I_SUP
Reserved
NO_PI_CHK
GRD_CHK
APP_CHK
REF_CHK
Reserved
T3PS
T2PS
T1PS
T0PS
Reserved
