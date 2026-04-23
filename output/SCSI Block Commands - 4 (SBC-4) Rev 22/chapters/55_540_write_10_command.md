# 5.40 WRITE (10) command

If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is enabled (see table 125, table 126, table 127, and table 128 in 5.36), then the LOGICAL
BLOCK APPLICATION TAG MASK field contains a value that is a bit mask for enabling the checking of the LOGICAL
BLOCK APPLICATION TAG field in every instance of the protection information for each logical block accessed by
the command. A LOGICAL BLOCK APPLICATION TAG MASK bit set to one enables the checking of the
corresponding bit of the EXPECTED LOGICAL BLOCK APPLICATION TAG field with the corresponding bit of the
LOGICAL BLOCK APPLICATION TAG field in every instance of the protection information. A LOGICAL BLOCK
APPLICATION TAG MASK field bit set to zero disables the checking of the corresponding bit of the EXPECTED
LOGICAL BLOCK APPLICATION TAG field with the corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in
every instance of protection information.
The LOGICAL BLOCK APPLICATION TAG MASK field and the EXPECTED LOGICAL BLOCK APPLICATION TAG field shall
be ignored if:
a)
the ATO bit is set to zero; or
b)
the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is disabled (see table 125, table 126, table 127, and table 128 in 5.36).
5.40 WRITE (10) command
5.40.1 WRITE (10) command overview
The WRITE (10) command (see table 132) requests that the device server:
a)
transfer the specified logical block data from the Data-Out Buffer; and
b)
perform write operations to the specified LBAs using the transferred logical blocks.
NOTE 16 - Migration from the WRITE (10) command to the WRITE (16) command is recommended for all
implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 132 for the
WRITE (10) command.
Table 132 — WRITE (10) command
Bit
Byte
OPERATION CODE (2Ah)
WRPROTECT
DPO
FUA
Reserved
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
GROUP NUMBER
(MSB)
TRANSFER LENGTH
(LSB)
CONTROL


The device server shall check the protection information, if any, transferred from the Data-Out Buffer based on
the WRPROTECT field as described in table 133. All footnotes for table 133 are at the end of the table.
Table 133 — WRPROTECT field (part 1 of 2)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information k
Device
server
check
If check fails d i, additional sense code
000b
Yes f g h
No protection information received from application client to check
No
No protection information received from application client to check
001b b
Yes e
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
Dependent
on RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
Shall (except
for type 3) j
LOGICAL BLOCK REFERENCE TAG CHECK
FAILED
No a
No protection information available to check
010b b
Yes e
LOGICAL BLOCK
GUARD
Shall not
No check performed
LOGICAL BLOCK
APPLICATION TAG
Dependent
on RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May j
LOGICAL BLOCK REFERENCE TAG CHECK
FAILED
No a
No protection information available to check
011b b
Yes e
LOGICAL BLOCK
GUARD
Shall not
No check performed
LOGICAL BLOCK
APPLICATION TAG
Shall not
No check performed
LOGICAL BLOCK
REFERENCE TAG
Shall not
No check performed
No a
No protection information available to check
100b b
Yes e
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
Shall not
No check performed
LOGICAL BLOCK
REFERENCE TAG
Shall not
No check performed
No a
No protection information available to check


101b b
Yes e
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
Dependent
on RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May j
LOGICAL BLOCK REFERENCE TAG CHECK
FAILED
No a
No protection information available to check
110b to
111b
Reserved
a If a logical unit supports protection information (see 4.21) and has not been formatted with protection information,
then the device server shall terminate the command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the requested
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense
code set to INVALID FIELD IN CDB.
c See 5.40.2
d If the device server terminates the command with CHECK CONDITION status, then the device server shall set the
sense key to ABORTED COMMAND.
e The device server shall preserve the contents of protection information (e.g., write it to the medium or store it in
non-volatile memory).
f
The device server shall write a generated CRC (see 4.21.4.2) into each LOGICAL BLOCK GUARD field.
g If the RWWP bit in the Control mode page (see SPC-6) is set to one, then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense
code set to INVALID FIELD IN CDB. If the RWWP bit is set to zero and:
a)
type 1 protection is enabled, then the device server shall write the least significant four bytes of each LBA into
the LOGICAL BLOCK REFERENCE TAG field of each of the written logical blocks; or
b)
type 2 protection or type 3 protection is enabled, then the device server shall write a value of FFFF_FFFFh into
the LOGICAL BLOCK REFERENCE TAG field of each of the written logical blocks.
h If the ATO bit is set to one in the Control mode page (see SPC-6), then the device server shall write FFFFh into each
LOGICAL BLOCK APPLICATION TAG field. If the ATO bit is set to zero, then the device server may write any value into
each LOGICAL BLOCK APPLICATION TAG field.
i
If multiple errors occur while the device server is processing the command, then the selection by the device server
of which error to report is not defined by this standard.
j
If type 1 protection is enabled, then the device server shall check the logical block reference tag by comparing it to
the lower four bytes of the LBA associated with the logical block. If type 2 protection is enabled and the device
server has knowledge of the contents of the LOGICAL BLOCK REFERENCE TAG field, then the device server shall check
each logical block reference tag. If type 2 protection is enabled, then this knowledge may be acquired through the
EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG field in a WRITE (32) command, a WRITE ATOMIC (32)
command, a WRITE SAME (32) command, WRITE SCATTERED (32) command, or a WRITE STREAM (32)
command. If type 3 protection is enabled, the ATO bit is set to one in the Control mode page (see SPC-6), and the
device server has knowledge of the contents of the LOGICAL BLOCK REFERENCE TAG field, then the device server
may check each logical block reference tag. If type 3 protection is enabled, then the method for acquiring this
knowledge is not defined by this standard.
k If the NO_PI_CHK bit is set to one in the Extended INQUIRY Data VPD page (see SPC-6) and the device server
detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.21.2.3) or type 2 protection
(see 4.21.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh,
and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection information interval.
Table 133 — WRPROTECT field (part 2 of 2)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information k
Device
server
check
If check fails d i, additional sense code


See the READ (10) command (see 5.16) for the definition of the DPO bit.
A force unit access (FUA) bit set to one specifies that the device server shall write the logical blocks to:
a)
the non-volatile cache, if any; or
b)
the medium.
An FUA bit set to zero specifies that the device server shall write the logical blocks to:
a)
volatile cache, if any;
b)
non-volatile cache, if any; or
c)
the medium.
See the PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field.
See the PRE-FETCH (10) command and 4.22 for the definition of the GROUP NUMBER field.
The TRANSFER LENGTH field specifies the number of contiguous logical blocks of data that shall be transferred
from the Data-Out Buffer and written, starting with the logical block referenced by the LBA specified by the
LOGICAL BLOCK ADDRESS field. A TRANSFER LENGTH field set to zero specifies that no logical blocks shall be
transferred or written. This condition shall not be considered an error. Any other value specifies the number of
logical blocks that shall be transferred and written. If the specified LBA and the specified transfer length
exceed the capacity of the medium (see 4.5), then the device server shall terminate the command with
CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to LOGICAL BLOCK ADDRESS OUT OF RANGE. The TRANSFER LENGTH field is constrained by the MAXIMUM
TRANSFER LENGTH field (see 6.6.4).
The CONTROL byte is defined in SAM-6.
5.40.2 RWWP interaction
If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field and the ATO bit
is set to one in the Control mode page (see SPC-6), then the device server:
a)
may check each logical block application tag if the RWWP bit is set to zero in the Control mode page
(see SPC-6); and
b)
shall check each logical block application tag if the RWWP bit is set to one in the Control mode page.
If the ATO bit in the Control mode page (see SPC-6) is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK field
in the CDB, if a WRITE (32) command (see 5.43), a WRITE ATOMIC (32) command (see 5.49), a
WRITE SAME (32) command (see 5.54), or a WRITE STREAM (32) command (see 5.58) is received
by the device server;
b)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK field
in each LBA range descriptor, if a WRITE SCATTERED (32) command (see 5.56), is received by the
device server;
c)
the Application Tag mode page (see 6.5.3), if a command other than WRITE (32), WRITE ATOMIC
(32), WRITE SAME (32), WRITE SCATTERED (32), or WRITE STREAM (32) is received by the
device server and the ATMPE bit in the Control mode page (see SPC-6) is set to one; or
d)
a method not defined by this standard, if a command other than WRITE (32), WRITE ATOMIC (32),
WRITE SAME (32), WRITE SCATTERED (32), or WRITE STREAM (32) is received by the device
server, and the ATMPE bit is set to zero.


5.41 WRITE (12) command
The WRITE (12) command (see table 134) requests that the device server perform the actions defined for the
WRITE (10) command (see 5.40).
NOTE 17 - Migration from the WRITE (12) command to the WRITE (16) command is recommended for all
implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 134 for the
WRITE (12) command.
See the WRITE (10) command (see 5.40) for the definitions of the other fields in this command.
Table 134 — WRITE (12) command
Bit
Byte
OPERATION CODE (AAh)
WRPROTECT
DPO
FUA
Reserved
Obsolete
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
Restricted
for
MMC-6
Reserved
GROUP NUMBER
CONTROL


5.42 WRITE (16) command
The WRITE (16) command (see table 135) requests that the device server perform the actions defined for the
WRITE (10) command (see 5.40).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 135 for the
WRITE (16) command.
See the READ (16) command (see 5.18) for the definitions of the DLD2 bit, the DLD1 bit, and the DLD0 bit.
See the WRITE (10) command (see 5.40) for the definitions of the other fields in this command.
Table 135 — WRITE (16) command
Bit
Byte
OPERATION CODE (8Ah)
WRPROTECT
DPO
FUA
Reserved
Obsolete
DLD2
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
DLD1
DLD0
GROUP NUMBER
CONTROL


5.43 WRITE (32) command
The WRITE (32) command (see table 136) requests that the device server perform the actions defined for the
WRITE (10) command (see 5.40).
The device server shall process a WRITE (32) command only if type 2 protection is enabled (see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 136 for the WRITE (32) command.
See the WRITE (10) command (see 5.40) for the definitions of the CONTROL byte, the GROUP NUMBER field, the
WRPROTECT field, the DPO bit, the FUA bit, the LOGICAL BLOCK ADDRESS field, and the TRANSFER LENGTH field.
See the READ (16) command (see 5.18) for the definitions of the DLD2 bit, DLD1 bit, and DLD0 bit.
If checking of the LOGICAL BLOCK REFERENCE TAG field is enabled (see table 133), then the EXPECTED INITIAL
LOGICAL BLOCK REFERENCE TAG field contains the value of the LOGICAL BLOCK REFERENCE TAG field expected in
Table 136 — WRITE (32) command
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
SERVICE ACTION (000Bh)
(LSB)
WRPROTECT
DPO
FUA
Reserved
Obsolete
Reserved
Reserved
DLD2
DLD1
DLD0
(MSB)
LOGICAL BLOCK ADDRESS
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
(MSB)
TRANSFER LENGTH
•••
(LSB)


the protection information of the first logical block accessed by the command instead of a value based on the
LBA (see 4.21.3).
If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is enabled (see table 133), then the LOGICAL BLOCK APPLICATION TAG MASK field contains
a value that is a bit mask for enabling the checking of the LOGICAL BLOCK APPLICATION TAG field in every
instance of protection information for each logical block accessed by the command. A LOGICAL BLOCK
APPLICATION TAG MASK bit set to one enables the checking of the corresponding bit of the EXPECTED LOGICAL
BLOCK APPLICATION TAG field with the corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every
instance of protection information. A LOGICAL BLOCK APPLICATION TAG MASK field bit set to zero disables the
checking of the corresponding bit of the EXPECTED LOGICAL BLOCK APPLICATION TAG field with the
corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every instance of protection information.
If the ATO bit is set to:
a)
zero; or
b)
one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK APPLICATION TAG field
is disabled (see table 133),
then the LOGICAL BLOCK APPLICATION TAG MASK field and the EXPECTED LOGICAL BLOCK APPLICATION TAG field
shall be ignored
5.44 WRITE AND VERIFY (10) command
The WRITE AND VERIFY (10) command (see table 137) requests that the device server:
1)
transfer the specified the logical block data for the command from the Data-Out Buffer;
2)
perform write medium operations to the specified LBAs;
3)
perform verify operations from the specified LBAs; and
4)
if specified, perform a compare operation on:
A) the logical block data transferred from the Data-Out Buffer; and
B) the logical block data from the verify operations.
The device server may process the LBAs in any order but shall perform this sequence in the specified order
for a given LBA.
NOTE 18 - Migration from the WRITE AND VERIFY (10) command to the WRITE AND VERIFY (16)
command is recommended for all implementations.
Table 137 — WRITE AND VERIFY (10) command
Bit
Byte
OPERATION CODE (2Eh)
WRPROTECT
DPO
Reserved
BYTCHK
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
GROUP NUMBER
(MSB)
TRANSFER LENGTH
(LSB)
CONTROL


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 137 for the
WRITE AND VERIFY (10) command.
See the PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field. See the
PRE-FETCH (10) command and 4.22 for the definition of the GROUP NUMBER field. See the WRITE (10)
command (see 5.40) for the definitions of the CONTROL byte, the TRANSFER LENGTH field and the WRPROTECT
field. See the READ (10) command (see 5.16) for the definition of the DPO bit.
See the VERIFY (10) command (see 5.36) for definition of the byte check (BYTCHK) field when set to 00b, 01b,
and 10b. For a WRITE AND VERIFY (10) command, a BYTCHK field set to 11b is reserved.
5.45 WRITE AND VERIFY (12) command
The WRITE AND VERIFY (12) command (see table 138) requests that the device server perform the actions
defined for the WRITE AND VERIFY (10) command (see 5.44).
NOTE 19 - Migration from the WRITE AND VERIFY (12) command to the WRITE AND VERIFY (16)
command is recommended for all implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 138 for the
WRITE AND VERIFY (12) command.
See the WRITE AND VERIFY (10) command (see 5.44) for the definitions of the other fields in this command.
Table 138 — WRITE AND VERIFY (12) command
Bit
Byte
OPERATION CODE (AEh)
WRPROTECT
DPO
Reserved
BYTCHK
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.46 WRITE AND VERIFY (16) command
The WRITE AND VERIFY (16) command (see table 139) requests that the device server perform the actions
defined for the WRITE AND VERIFY (10) command (see 5.44).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 139 for the
WRITE AND VERIFY (16) command.
See the WRITE AND VERIFY (10) command (see 5.44) for the definitions of the other fields in this command.
Table 139 — WRITE AND VERIFY (16) command
Bit
Byte
OPERATION CODE (8Eh)
WRPROTECT
DPO
Reserved
BYTCHK
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.47 WRITE AND VERIFY (32) command
The WRITE AND VERIFY (32) command (see table 140) requests that the device server perform the actions
defined for the WRITE AND VERIFY (10) command (see 5.44).
The device server shall process a WRITE AND VERIFY (32) command only if type 2 protection is enabled
(see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 140 for the WRITE AND VERIFY (32) command.
See the WRITE AND VERIFY (10) command (see 5.44) for the definitions of the CONTROL byte, the GROUP
NUMBER field, the WRPROTECT field, the DPO bit, the BYTCHK field, the LOGICAL BLOCK ADDRESS field, and the
TRANSFER LENGTH field.
If checking of the LOGICAL BLOCK REFERENCE TAG field is enabled (see table 133), then the EXPECTED INITIAL
LOGICAL BLOCK REFERENCE TAG field contains the value of the LOGICAL BLOCK REFERENCE TAG field expected in
Table 140 — WRITE AND VERIFY (32) command
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
SERVICE ACTION (000Ch)
(LSB)
WRPROTECT
DPO
Reserved
BYTCHK
Reserved
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
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
(MSB)
TRANSFER LENGTH
•••
(LSB)


the protection information of the first logical block accessed by the command instead of a value based on the
LBA (see 4.21.3).
If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is enabled (see table 133 in 5.40), then the LOGICAL BLOCK APPLICATION TAG MASK field
contains a value that is a bit mask for enabling the checking of the LOGICAL BLOCK APPLICATION TAG field in
every instance of protection information for each logical block accessed by the command. A LOGICAL BLOCK
APPLICATION TAG MASK bit set to one enables the checking of the corresponding bit of the EXPECTED LOGICAL
BLOCK APPLICATION TAG field with the corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every
instance of protection information. A LOGICAL BLOCK APPLICATION TAG MASK field bit set to zero disables the
checking of the corresponding bit of the EXPECTED LOGICAL BLOCK APPLICATION TAG field with the
corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every instance of protection information.
If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is disabled (see table 133), or if the ATO bit is set to zero, then the LOGICAL BLOCK
APPLICATION TAG MASK field and the EXPECTED LOGICAL BLOCK APPLICATION TAG field shall be ignored.
5.48 WRITE ATOMIC (16) command
The WRITE ATOMIC (16) command (see table 141) requests that the device server:
a)
transfer logical block data from the Data-Out Buffer; and
b)
perform one or more atomic write operations (see 4.29) of the LBAs specified by this command.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 141 for the WRITE
ATOMIC (16) command.
The ATOMIC BOUNDARY field specifies whether multiple atomic write operations may be performed. If the
ATOMIC BOUNDARY field is set to zero, then a single atomic write operation of the length specified in the
TRANSFER LENGTH field shall be performed. If the ATOMIC BOUNDARY field is set to a non-zero value then
multiple atomic write operations may be performed as described in 4.29.
See the WRITE (10) command (see 5.40) for the definitions of the other fields in this command.
Table 141 — WRITE ATOMIC (16) command
Bit
Byte
OPERATION CODE (9Ch)
WRPROTECT
DPO
FUA
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
ATOMIC BOUNDARY
(MSB)
TRANSFER LENGTH
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.49 WRITE ATOMIC (32) command
The WRITE ATOMIC (32) command (see table 142) requests that the device server perform the actions
defined for the WRITE ATOMIC (16) command (see 5.48).
The device server shall process a WRITE ATOMIC (32) command only if type 2 protection is enabled
(see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 142 for the WRITE ATOMIC (32) command.
See the WRITE ATOMIC (16) command (see 5.48) for the definition of the ATOMIC BOUNDARY field.
See the WRITE (32) command (see 5.43) for the definitions of the other fields in this command.
Table 142 — WRITE ATOMIC (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
(MSB)
ATOMIC BOUNDARY
(LSB)
Reserved
GROUP NUMBER
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (000Fh)
(LSB)
WRPROTECT
DPO
FUA
Reserved
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
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
(MSB)
TRANSFER LENGTH
•••
(LSB)


5.50 WRITE LONG (10) command
The WRITE LONG (10) command (see table 143) requests that the device server mark a logical block as
containing a pseudo unrecovered error. If a cache contains the specified logical block, then the device server
shall invalidate that logical block in the cache.
NOTE 20 - Migration from the WRITE LONG (10) command to the WRITE LONG (16) command is
recommended for all implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 143 for the
WRITE LONG (10) command.
The write uncorrectable error (WR_UNCOR) bit is shown in table 144.
If the WRITE LONG command is supported, then the WU_SUP bit in the Extended INQUIRY Data VPD page
(see SPC-6) shall be set to one to indicate that the logical unit supports setting the WR_UNCOR bit to one.
The LOGICAL BLOCK ADDRESS field specifies an LBA. If the specified LBA exceeds the capacity of the medium
(see 4.5), then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS
OUT OF RANGE.
The CONTROL byte is defined in SAM-6.
Table 143 — WRITE LONG (10) command
Bit
Byte
OPERATION CODE (3Fh)
Obsolete
WR_UNCOR
Obsolete
Reserved
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
Obsolete
CONTROL
Table 144 — WR_UNCOR bit
WR_UNCOR
Description
Obsolete
Mark the specified logical block as containing a pseudo unrecovered error with
correction disabled (see 4.18.2).
No data is transferred.
