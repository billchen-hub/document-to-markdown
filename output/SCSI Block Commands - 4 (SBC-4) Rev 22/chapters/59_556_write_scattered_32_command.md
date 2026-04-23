# 5.56 WRITE SCATTERED (32) command

5.56 WRITE SCATTERED (32) command
5.56.1 WRITE SCATTERED (32) command overview
The WRITE SCATTERED (32) command (see table 153) requests that the device server perform the actions
defined for the WRITE SCATTERED (16) command (see 5.55).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 153 for the WRITE SCATTERED (32) command.
See the WRITE SCATTERED (16) command (see 5.55) for the definitions of the other fields in this command.
Table 153 — WRITE SCATTERED (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
•••
Reserved
GROUP NUMBER
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (0011h)
(LSB)
WRPROTECT
DPO
FUA
Reserved
Reserved
(MSB)
LOGICAL BLOCK DATA OFFSET
(LSB)
Reserved
(MSB)
NUMBER OF LBA RANGE DESCRIPTORS
(LSB)
Reserved
•••
(MSB)
BUFFER TRANSFER LENGTH
•••
(LSB)


5.56.2 WRITE SCATTERED (32) command Data-Out Buffer contents
Table 154 defines the Data-Out Buffer contents for the WRITE SCATTERED (32) command
The LBA range descriptor list specifies one or more LBA range descriptors (see table 155). The LBA range
descriptors may be in any order. The device server may process the LBA range descriptors in any order. The
application client should not specify overlapping LBA ranges. If overlapping LBA ranges are specified, then
the logical block data in the overlapping LBAs may be any of the logical block data specified for those LBAs.
The device server shall not consider an LBA range with the NUMBER OF LOGICAL BLOCKS field set to
0000_0000h as overlapping with any other LBA range.
The PAD field shall contain zero or more bytes set to zero such that the total length of the LBA range descriptor
list and the PAD field is a multiple of the length of a logical block (i.e., the length of the user data and protection
information, if any, in one logical block). Device servers shall ignore the PAD field.
Table 154 — Data-Out Buffer contents for the WRITE SCATTERED (32) command
Bit
Byte
WRITE SCATTERED (32) parameter list header
Reserved
•••
LBA range descriptor list
LBA range descriptor [first] (see table 155)
•••
•••
k-31
LBA range descriptor [last] (see table 155)
•••
k
k+1
PAD (if any)
•••
m
Scattered write logical block data
m+1
Logical block data for first LBA range
•••
•••
Logical block data for last LBA range
•••
k


Table 155 defines the LBA range descriptor.
See the WRITE SCATTERED (16) command (see 5.55) for the definitions of the LOGICAL BLOCK ADDRESS field
and the NUMBER OF LOGICAL BLOCKS field.
See the WRITE (32) command (see 5.43) for the definitions of the EXPECTED INITIAL LOGICAL BLOCK REFERENCE
TAG field, the EXPECTED LOGICAL BLOCK APPLICATION TAG field, and the LOGICAL BLOCK APPLICATION TAG MASK
field.
Table 155 — LBA range descriptor
 Bit
Byte
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
(MSB)
EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG
•••
(LSB)
(MSB)
EXPECTED LOGICAL BLOCK APPLICATION TAG
(LSB)
(MSB)
LOGICAL BLOCK APPLICATION TAG MASK
(LSB)
Reserved
•••
