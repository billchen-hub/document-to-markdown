# 4.35 Scattered writes

4.34 Transfer limits
Devices servers may have limits on the amount of logical block data that is able to be transferred in a single
command. The Block Limits VPD page and the Block Limits Extension VPD page report those transfer limits.
Table 33 describes the fields that specify transfer size and the VPD page field that limits the transfer size.
4.35 Scattered writes
4.35.1 Scattered writes overview
Scattered writes are requested by WRITE SCATTERED commands (see 5.55 and 5.56).
A WRITE SCATTERED command describes the ranges of LBAs using a set of LBA range descriptors in the
Data-Out buffer to describe the logical block address for the first LBA to be written and the number of logical
Table 33 — Transfer limits for commands
Command
Field that specifies
the transfer size
VPD page field that
indicates maximum
limits
Additional sense code if
the value in the
specified field exceeds
the maximum limit
Commands limited by fields in the Block Limits VPD page
COMPARE AND WRITE
CDB NUMBER OF
LOGICAL BLOCKS field
MAXIMUM COMPARE AND
WRITE LENGTH field
INVALID FIELD IN CDB
ORWRITE
CDB TRANSFER
LENGTH field
MAXIMUM TRANSFER
LENGTH field
PRE-FETCH
CDB PREFETCH
LENGTH field
MAXIMUM PREFETCH
LENGTH field
READ
CDB TRANSFER
LENGTH field
MAXIMUM TRANSFER
LENGTH field
VERIFY
CDB VERIFICATION
LENGTH field
WRITE
CDB TRANSFER
LENGTH field
WRITE AND VERIFY
POPULATE TOKEN
NUMBER OF LOGICAL
BLOCKS field in any
Block device range
descriptor
(see 5.12.3)
MAXIMUM TRANSFER
LENGTH field
INVALID FIELD IN
PARAMETER LIST
WRITE USING TOKEN
Commands limited by fields in the Block Limits Extension VPD page
WRITE SCATTERED
CDB BUFFER
TRANSFER LENGTH
FIELD
MAXIMUM SCATTERED
TRANSFER LENGTH field
INVALID FIELD IN CDB
CDB NUMBER OF LBA
RANGE DESCRIPTORS
field
MAXIMUM SCATTERED LBA
RANGE DESCRIPTOR
COUNT field
INVALID FIELD IN CDB
LBA range
descriptor TRANSFER
LENGTH field
MAXIMUM SCATTERED LBA
RANGE TRANSFER
LENGTH field
INVALID FIELD IN
PARAMETER LIST


blocks to be written (see figure 15). A WRITE SCATTERED command provides the logical block data to be
written for each LBA range in the same Data-Out buffer as the LBA range descriptors. The logical block data
for each associated LBA range descriptor is provided in the same order as the LBA range descriptors and
follows the LBA range descriptors and optional padding (see figure 15). The LOGICAL BLOCK DATA OFFSET field
in the CDB specifies the start of the logical block data in the Data-Out Buffer.
Figure 15 — LBA range descriptors
Scattered writes request one or more write operations to write data to specified LBA ranges. Each LBA range,
specified by an LBA range descriptor identifies a set of contiguous LBAs associated with logical block data
from the Data-Out Buffer (see figure 2).
To process the WRITE SCATTERED command the device server shall:
1)
validate one or more LBA range descriptors as specified in 5.55; and
2)
perform write operations for the validated descriptors as specified in 4.35.2.
The device server may:
a)
validate one or more LBA range descriptors before performing write operations; and
b)
perform write operations in any order.
4.35.2 Performing write operations for scattered writes
The logical block data in the Data-Out Buffer that is associated with the LBA range descriptors (see 4.35.1) is
in the same order as the LBA range descriptors. The offset into the Data-Out Buffer for the logical block data
associated with an LBA range descriptor is calculated by multiplying the sum of the NUMBER OF LOGICAL
BLOCKS fields from each preceding LBA range descriptor by the length of a logical block (i.e., the length of the
user data and protection information, if any, in one logical block) and adding the result to the offset of the
logical block data from the CDB.
LBA range x
Logical blocks on
the medium
Data-Out Buffer
Logical block address
Number of logical blocks
LBA range
descriptor x
LBA range
descriptors
Write Data
...
Pad (optional)


Figure 16 shows example write operations for a WRITE SCATTERED command.
Figure 16 — Example write operations for WRITE SCATTERED commands
4.35.3 Scattered writes that encounter errors
If the device server encounters an error while performing write operations, then the device server:
a)
may terminate processing of all LBA range descriptors; or
b)
may continue processing range descriptors.
The device server shall terminate a WRITE SCATTERED command that encounters an error as specified in
4.18. If an unrecovered error is reported, then the INFORMATION field in the sense data should be set to a
number indicating the lowest numbered LBA range descriptor for which the associated LBA range was not
successfully written. LBA range descriptors shall be numbered starting with the number one indicating the first
LBA range descriptor in the parameter data and incremented by one for each subsequent LBA range
descriptor. An INFORMATION field set to zero indicates that the lowest numbered LBA range descriptor for
which the associated LBA range was not successfully written is not reported.
Write data 0
Write data n-2
Write data 1
Write data n-1
Write data 2
Write data 0
(i.e., write data
for LBA range
descriptor 0)
Write data n-1
Write data 2
Write data n
Write data 1
Logical blocks on
the medium
LBA 0
LBA z
(capacity)
LBA
range 0
LBA
range n-2
LBA
range 1
LBA
range n-1
LBA
range 2
Data-Out Buffer
LBA range
descriptor n-2
LBA range
descriptor n-1
Device server
LBA range
descriptor 0
...
LBA range
descriptor 2
LBA range
descriptor 1
LBA range
descriptor n
Write data n-2
...
Write data n
LBA
range n
Pad (optional)
Header
