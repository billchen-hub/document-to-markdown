# 5.55 WRITE SCATTERED (16) command

APPLICATION TAG MASK bit set to one enables the checking of the corresponding bit of the EXPECTED LOGICAL
BLOCK APPLICATION TAG field with the corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every
instance of protection information. A LOGICAL BLOCK APPLICATION TAG MASK field bit set to zero disables the
checking of the corresponding bit of the EXPECTED LOGICAL BLOCK APPLICATION TAG field with the
corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every instance of protection information.
If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is disabled (see table 133 in 5.40), or if the ATO bit is set to zero, then the LOGICAL BLOCK
APPLICATION TAG MASK field and the EXPECTED LOGICAL BLOCK APPLICATION TAG field shall be ignored.
5.55 WRITE SCATTERED (16) command
5.55.1 WRITE SCATTERED (16) command overview
The WRITE SCATTERED (16) command (see table 150) requests that the device server perform scattered
writes (see 4.35).
This command uses the SERVICE ACTION OUT (16) CDB format (see SPC-6).
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 150 for the WRITE SCATTERED (16) command.
See the WRITE (10) command (see 5.40) for the definition of the WRPROTECT field and the FUA bit. See the
READ (10) command (see 5.16) for the definition of the DPO bit. See the READ (16) command (see 5.18) for
the definition of the DLD2 bit.
The LOGICAL BLOCK DATA OFFSET field specifies the offset of the scattered write logical block data in the
Data-Out Buffer (see table 151) in multiples of the length of a logical block (i.e., the length of the user data and
protection information, if any, in one logical block). The value in the LOGICAL BLOCK DATA OFFSET field is
Table 150 — WRITE SCATTERED (16) command
Bit
Byte
OPERATION CODE (9Fh)
Reserved
SERVICE ACTION (12h)
WRPROTECT
DPO
FUA
Reserved
DLD2
Reserved
(MSB)
LOGICAL BLOCK DATA OFFSET
(LSB)
Reserved
(MSB)
NUMBER OF LBA RANGE DESCRIPTORS
(LSB)
(MSB)
BUFFER TRANSFER LENGTH
•••
(LSB)
DLD1
DLD0
GROUP NUMBER
CONTROL


calculated by dividing (m+1) (see table 151) by the length of a logical block (i.e., the length of the user data
and protection information, if any, in one logical block).
The NUMBER OF LBA RANGE DESCRIPTORS field specifies the number of LBA range descriptors (see table 152)
in the LBA range descriptor list that shall be transferred from the Data-Out Buffer. If the NUMBER OF LBA RANGE
DESCRIPTORS field is greater than the number indicated by the MAXIMUM SCATTERED LBA RANGE DESCRIPTOR
COUNT field in the Block Limits Extension VPD page (see 6.6.5), then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN CDB. A NUMBER OF LBA RANGE DESCRIPTORS field set to 0000h specifies
that no data shall be transferred or written. This condition shall not be considered an error. If the value in the
LOGICAL BLOCK DATA OFFSET field is not large enough to contain the specified number of LBA range
descriptors, then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
The BUFFER TRANSFER LENGTH field specifies the number of logical blocks that shall be transferred from the
Data-Out Buffer. If the BUFFER TRANSFER LENGTH field is greater than the MAXIMUM SCATTERED TRANSFER
LENGTH field in the Block Limits Extension VPD page (see 6.6.5), then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN CDB. A BUFFER TRANSFER LENGTH field set to zero specifies that no
logical blocks shall be transferred. This condition shall not be considered an error.
See the READ (16) command for the definitions of the DLD1 bit and the DLD0 bit.
The CONTROL byte is defined in SAM-6.


5.55.2 WRITE SCATTERED (16) command Data-Out Buffer contents
Table 151 defines the Data-Out Buffer contents for the WRITE SCATTERED (16) command
The LBA range descriptor list specifies one or more LBA range descriptors (see table 152). The LBA range
descriptors may be in any order. The device server may process the LBA range descriptors in any order. The
application client should not specify overlapping LBA ranges. If overlapping LBA ranges are specified, then
the logical block data in the overlapping LBAs may be any of the logical block data specified for those LBAs.
The device server shall not consider an LBA range with the NUMBER OF LOGICAL BLOCKS field set to
0000_0000h as overlapping with any other LBA range.
The PAD field shall contain zero or more bytes set to zero such that the total length of the LBA range descriptor
list and the PAD field is a multiple of the length of a logical block (i.e., the length of the user data and protection
information, if any, in one logical block). Device servers shall ignore the PAD field.
Table 152 defines the LBA range descriptor.
Table 151 — Data-Out Buffer contents for the WRITE SCATTERED (16) command
Bit
Byte
WRITE SCATTERED (16) parameter list header
Reserved
•••
LBA range descriptor list
LBA range descriptor [first] (see table 152)
•••
•••
k-31
LBA range descriptor [last] (see table 152)
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


The LOGICAL BLOCK ADDRESS field specifies the LBA of the first logical block (see 4.5) in this LBA range.
The NUMBER OF LOGICAL BLOCKS field specifies the number of contiguous logical blocks of logical block data
from the scattered write logical block data (see table 151) that are associated with this LBA range descriptor. If
the NUMBER OF LOGICAL BLOCKS field is greater than the MAXIMUM SCATTERED LBA RANGE TRANSFER LENGTH field
(see 6.6.5), then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER
LIST. A NUMBER OF LOGICAL BLOCKS field set to zero specifies that no logical blocks shall be written. This
condition shall not be considered an error. Any other value specifies the number of logical blocks that shall be
written to the medium as specified in 4.35
If the specified LBA and the specified number of logical blocks exceed the capacity of the medium (see 4.5),
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS OUT OF RANGE.
If:
a)
the device server processes an LBA range descriptor and the value in the NUMBER OF LOGICAL BLOCKS
field added to the sum of the values from the NUMBER OF LOGICAL BLOCKS fields in the LBA range
descriptors from this command that have already been processed exceeds the BUFFER TRANSFER
LENGTH field in the CDB minus the LOGICAL BLOCK DATA OFFSET field in the CDB (i.e., the number of
logical blocks requested to be written by all of the processed LBA range descriptors exceeds the
number of logical blocks in the scattered write logical block data (see table 151)); or
b)
the device server processes all of the LBA range descriptors and the sum of the values in the NUMBER
OF LOGICAL BLOCKS fields from all of the LBA range descriptors does not equal the BUFFER TRANSFER
LENGTH field in the CDB minus the LOGICAL BLOCK DATA OFFSET field in the CDB,
then the device server shall terminate the command with CHECK CONDITION status, with the sense key set
to ABORTED COMMAND, the additional sense code set to PARAMETER LIST LENGTH ERROR, and the
field pointer pointing to the BUFFER TRANSFER LENGTH field. The contents of the logical blocks referenced by
any LBA range descriptors already processed may be old data, new data, or any combination thereof.
Table 152 — LBA range descriptor
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
Reserved
•••
