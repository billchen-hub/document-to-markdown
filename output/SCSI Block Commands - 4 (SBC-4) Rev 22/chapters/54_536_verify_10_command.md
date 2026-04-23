# 5.36 VERIFY (10) command

Table 122 defines the UNMAP block descriptor.
The UNMAP LOGICAL BLOCK ADDRESS field specifies the first LBA that is requested to be unmapped
(see 4.7.3.4.2) for this UNMAP block descriptor.
The NUMBER OF LOGICAL BLOCKS field specifies the number of LBAs that are requested to be unmapped
beginning with the LBA specified by the UNMAP LOGICAL BLOCK ADDRESS field.
If the NUMBER OF LOGICAL BLOCKS is set to zero, then no LBAs shall be unmapped for this UNMAP block
descriptor. This condition shall not be considered an error.
If the specified LBA and the specified number of logical blocks exceeds the capacity of the medium (see 4.5),
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS OUT OF RANGE.
If the total number of logical blocks specified in the UNMAP block descriptor data exceeds the value indicated
in the MAXIMUM UNMAP LBA COUNT field (see 6.6.4) or if the number of UNMAP block descriptors exceeds the
value of the MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT field (see 6.6.4), then the device server shall terminate
the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
5.36 VERIFY (10) command
The VERIFY (10) command (see table 124) requests that the device server:
1)
perform verify operations from the specified LBAs; and
2)
if specified, perform a compare operation on:
A) the logical block data transferred from the Data-Out Buffer; and
B) the logical block data from the verify operations.
The device server may process the LBAs in any order but shall perform this sequence in the specified order
for a given LBA.
Table 122 — UNMAP block descriptor
Bit
Byte
(MSB)
UNMAP LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
Reserved
•••


The application client uses the BYTCHK field in the CDB to specify the contents of the Data-Out Buffer as
shown in table 123.
NOTE 14 - Migration from the VERIFY (10) command to the VERIFY 16) command is recommended for all
implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 124 for the
VERIFY (10) command.
See the READ (10) command (see 5.16) for the definition of the DPO bit. See the PRE-FETCH (10) command
(see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field. See the PRE-FETCH (10) command
(see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
If the byte check (BYTCHK) field is set to 00b, then:
a)
no Data-Out Buffer transfer shall occur;
b)
for any mapped LBA specified by the command,  the device server shall check the protection
information from the verify operation based on the VRPROTECT field as shown in table 125; and
c)
for any unmapped LBA specified by the command, the verify operation shall complete as if there is no
verification error.
Table 123 — Data-Out Buffer contents for the VERIFY (10) command
BYTCHK field
Data-Out Buffer contents
00b
Not used
01b
Logical block data for the number of logical blocks specified in the VERIFICATION LENGTH
field
10b a
Not defined
11b
Logical block data for a single logical block
a A BYTCHK field set to 10b is reserved.
Table 124 — VERIFY (10) command
Bit
Byte
OPERATION CODE (2Fh)
VRPROTECT
DPO
Reserved
 BYTCHK
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Restricted
for
MMC-6
Reserved
GROUP NUMBER
(MSB)
VERIFICATION LENGTH
(LSB)
CONTROL


If:
a)
the BYTCHK field is set to 01b or 11b;
b)
the VBULS bit is set to zero in the Block Device Characteristics VPD page (see 6.6.2); and
c)
any LBA specified by the command is unmapped (i.e., deallocated or anchored),
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to MISCOMPARE and the additional sense code set to MISCOMPARE VERIFY OF UNMAPPED LBA.
If:
a)
the BYTCHK field is set to 01b or 11b; and
b)
either:
A) the VBULS bit is set to one in the Block Device Characteristics VPD page; or
B) all LBAs specified by the command are mapped,
then:
a)
if the BYTCHK field is set to 01b, then the Data-Out Buffer transfer shall include the number of logical
blocks specified by the VERIFICATION LENGTH field;
b)
if the BYTCHK field is set to 11b, then:
A) the Data-Out Buffer transfer shall include one logical block; and
B) the device server shall:
1)
duplicate the single logical block, as described in the WRITE SAME command (see 5.52), the
number of times required to satisfy the VERIFICATION LENGTH field; and
2)
place the duplicated data in the Data-Out Buffer;
c)
the device server shall check the protection information transferred from the Data-Out Buffer based
on the VRPROTECT field as shown in table 127;
d)
for any mapped LBA specified by the command, the device server shall perform the verify operation
and check the protection information from the verify operation based on the VRPROTECT field as shown
in table 126;
and
e)
the device server shall perform:
A) a compare operation of:
a)
user data from the verify operations; and
b)
user data from the Data-Out Buffer;
and
B) a compare operation based on the VRPROTECT field as shown in table 128 of:
a)
protection information from the verify operations; and
b)
protection information from the Data-Out Buffer.
The order of the user data and protection information checks and compare operations is vendor specific.
If a compare operation indicates a miscompare, then the device server shall terminate the command with
CHECK CONDITION status with the sense key set to MISCOMPARE and the additional sense code set to the
appropriate value for the condition.
The VERIFICATION LENGTH field specifies the number of contiguous logical blocks that shall be verified, starting
with the logical block referenced by the LBA specified by the LOGICAL BLOCK ADDRESS field. A VERIFICATION
LENGTH field set to zero specifies that no logical blocks shall be transferred or verified. This condition shall not
be considered an error. If the specified LBA and the specified verification length exceed the capacity of the
medium (see 4.5), then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS
OUT OF RANGE. The VERIFICATION LENGTH field is constrained by the MAXIMUM TRANSFER LENGTH field
(see 6.6.4).
If the BYTCHK field is set to 01b, then the VERIFICATION LENGTH field also specifies the number of logical blocks
that the device server shall transfer from the Data-Out Buffer.
The CONTROL byte is defined in SAM-6.


If the BYTCHK field is set to 00b, then table 125 defines the checks that the device server shall perform on the
protection information from the verify operations based on the VRPROTECT field. All footnotes for table 125 are
at the end of the table.
Table 125 — VRPROTECT field with the BYTCHK field set to 00b – checking protection information from
the verify operations (part 1 of 3)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Extended
INQUIRY Data
VPD page bit
value f
If check fails d e, additional sense code
000b
Yes i
LOGICAL
BLOCK GUARD
GRD_CHK = 1
LOGICAL BLOCK GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL
BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL
BLOCK
REFERENCE
TAG
REF_CHK = 1 h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No
No protection information on the medium to check.
001b
101b b
Yes
LOGICAL
BLOCK GUARD
GRD_CHK = 1
LOGICAL BLOCK GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL
BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL
BLOCK
REFERENCE
TAG
REF_CHK = 1 h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No
Error condition a
010b b
Yes
LOGICAL
BLOCK GUARD
No check performed
LOGICAL
BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL
BLOCK
REFERENCE
TAG
REF_CHK = 1 h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No
Error condition a


011b b
Yes
LOGICAL
BLOCK GUARD
No check performed
LOGICAL
BLOCK
APPLICATION
TAG
No check performed
LOGICAL
BLOCK
REFERENCE
TAG
No check performed
No
Error condition a
100b b
Yes
LOGICAL
BLOCK GUARD
GRD_CHK = 1
LOGICAL BLOCK GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL
BLOCK
APPLICATION
TAG
No check performed
LOGICAL
BLOCK
REFERENCE
TAG
No check performed
No
Error condition a
110b to
111b
Reserved
Table 125 — VRPROTECT field with the BYTCHK field set to 00b – checking protection information from
the verify operations (part 2 of 3)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Extended
INQUIRY Data
VPD page bit
value f
If check fails d e, additional sense code


a If the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field, then the
device server shall check each logical block application tag. If the ATO bit in the Control mode page (see
SPC-6) is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK
field in the CDB, if the command is a VERIFY (32) command (see 5.39);
b)
the Application Tag mode page (see 6.5.3), if the command is not a VERIFY (32) command and the
ATMPE bit in the Control mode page (see SPC-6) is set to one; or
c)
a method not defined by this standard, if the command is not a VERIFY (32) command and the
ATMPE bit is set to zero.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
f
See the Extended INQUIRY Data VPD page (see SPC-6) for the definitions of the GRD_CHK bit, the
APP_CHK bit, and the REF_CHK bit.
g If the device server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.21.2.3) or type 2
protection (see 4.21.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection
information interval.
h If type 1 protection is enabled, then the device server shall check each logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 2 protection or
type 3 protection is enabled, and the device server has knowledge of the contents of the LOGICAL BLOCK
REFERENCE TAG field, then the device server shall check the logical block reference tag. If type 2
protection is enabled, then this knowledge may be acquired through the EXPECTED INITIAL LOGICAL
BLOCK REFERENCE TAG field in a VERIFY (32) command (see 5.39). If type 3 protection is enabled, then
the method for acquiring this knowledge is not defined by this standard.
i
If the DPICZ bit in the Control mode page (see SPC-6) is set to one, then protection information shall not
be checked.
Table 125 — VRPROTECT field with the BYTCHK field set to 00b – checking protection information from
the verify operations (part 3 of 3)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Extended
INQUIRY Data
VPD page bit
value f
If check fails d e, additional sense code


If the BYTCHK field is set to 01b or 11b, then table 126 defines the checks that the device server shall perform
on the protection information from the verify operations based on the VRPROTECT field. All footnotes for
table 126 are at the end of the table.
Table 126 — VRPROTECT field with the BYTCHK field set to 01b or 11b – checking protection information
from the verify operations (part 1 of 2)
 Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Extended
INQUIRY Data
VPD page bit
value f
If check fails d e, additional sense code
000b
Yes i
LOGICAL BLOCK
GUARD
GRD_CHK = 1
LOGICAL BLOCK GUARD CHECK
FAILED
GRD_CHK = 0
No check performed
LOGICAL BLOCK
APPLICATION TAG
APP_CHK = 1 c g
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL BLOCK
REFERENCE TAG
REF_CHK = 1 h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No
No protection information available to check
001b
010b
011b
100b
101b b
Yes
LOGICAL BLOCK
GUARD
No check performed
LOGICAL BLOCK
APPLICATION TAG
No check performed
LOGICAL BLOCK
REFERENCE TAG
No check performed
No
Error condition a
110b
to
111b
Reserved


a If the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field, then the
device server shall check each logical block application tag. If the ATO bit in the Control mode page (see
SPC-6) is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK
field in the CDB, if the command is a VERIFY (32) command (see 5.39);
b)
the Application Tag mode page (see 6.5.3), if the command is not a VERIFY (32) command and the
ATMPE bit in the Control mode page (see SPC-6) is set to one; or
c)
a method not defined by this standard, if the command is not a VERIFY (32) command and the
ATMPE bit is set to zero.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
f
See the Extended INQUIRY Data VPD page (see SPC-6) for the definitions of the GRD_CHK bit, the
APP_CHK bit, and the REF_CHK bit.
g If the device server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.21.2.3) or type 2
protection (see 4.21.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection
information interval.
h If type 1 protection is enabled, then the device server shall check each logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 2 protection or
type 3 protection is enabled, and the device server has knowledge of the contents of the LOGICAL BLOCK
REFERENCE TAG field, then the device server shall check the logical block reference tag. If type 2
protection is enabled, then this knowledge may be acquired through the EXPECTED INITIAL LOGICAL BLOCK
REFERENCE TAG field in a VERIFY (32) command (see 5.39). If type 3 protection is enabled, then the
method for acquiring this knowledge is not defined by this standard.
i
If the DPICZ bit in the Control mode page (see SPC-6) is set to one, then protection information shall not
be checked.
Table 126 — VRPROTECT field with the BYTCHK field set to 01b or 11b – checking protection information
from the verify operations (part 2 of 2)
 Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Extended
INQUIRY Data
VPD page bit
value f
If check fails d e, additional sense code


If the BYTCHK field is set to 01b or 11b, then table 127 defines the checks that the device server shall perform
on the protection information transferred from the Data-Out Buffer based on the VRPROTECT field. All footnotes
for table 127 are at the end of the table.
Table 127 — VRPROTECT field with the BYTCHK field set to 01b or 11b – checking protection information
from the Data-Out Buffer (part 1 of 2)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Device server
check
If check fails d e, additional sense code
000b
Yes
No protection information in the Data-Out Buffer to check
No
No protection information in the Data-Out Buffer to check
001b b
Yes
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
May c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
Shall (except
for type 3) f
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
No
Error condition a
010b b
Yes
LOGICAL BLOCK
GUARD
Shall not
No check performed
LOGICAL BLOCK
APPLICATION TAG
May c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May f
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
No
Error condition a
011b b
Yes
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
No
Error condition a
100b b
Yes
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
No
Error condition a


101b b
Yes
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
May c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May f
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
No
Error condition a
110b to
111b
Reserved
a If the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field and the
ATO bit is set to one in the Control mode page (see SPC-6), then the device server may check each
logical block application tag. If the ATO bit is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK
field in the CDB, if the command is a VERIFY (32) command;
b)
the Application Tag mode page (see 6.5.3), if the command is not a VERIFY (32) command and the
ATMPE bit in the Control mode page (see SPC-6) is set to one; or
c)
a method not defined by this standard, if the command is not a VERIFY (32) command and the
ATMPE bit is set to zero.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
f
If type 1 protection is enabled, then the device server shall check the logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 2 protection is
enabled and the device server has knowledge of the contents of the LOGICAL BLOCK REFERENCE TAG
field, then the device server shall check each logical block reference tag. If type 2 protection is enabled,
then this knowledge may be acquired through the EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG field
in a VERIFY (32) command (see 5.39). If type 3 protection is enabled, the ATO bit is set to one in the
Control mode page (see SPC-6), and the device server has knowledge of the contents of the LOGICAL
BLOCK REFERENCE TAG field, then the device server may check each logical block reference tag. If type 3
protection is enabled, then the method for acquiring this knowledge is not defined by this standard.
g If the NO_PI_CHK bit is set to one in the Extended INQUIRY Data VPD page (see SPC-6) and the device
server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.21.2.3) or type 2
protection (see 4.21.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection
information interval.
Table 127 — VRPROTECT field with the BYTCHK field set to 01b or 11b – checking protection information
from the Data-Out Buffer (part 2 of 2)
Code
Logical unit
formatted
with
protection
information
Field in
protection
information g
Device server
check
If check fails d e, additional sense code


If the BYTCHK field is set to 01b or 11b, then table 128 defines the processing by the device server of the
protection information during the compare operation based on the VRPROTECT field. All footnotes for table 128
are at the end of the table.
Table 128 — VRPROTECT field with the BYTCHK field set to 01b or 11b – compare operation requirements
(part 1 of 4)
Code
Logical unit
formatted
with
protection
information
Field in protection
information j
Compare
operation
If compare fails c d, additional sense
code
000b
Yes
No protection information in the Data-Out Buffer to compare. Only user data is
compared within each logical block.
No
No protection information from the verify operations or in the Data-Out Buffer to
compare. Only user data is compared within each logical block.
001b b
Yes
LOGICAL BLOCK GUARD
Shall
LOGICAL BLOCK GUARD CHECK
FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 1) e
Shall i
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 0) f
Shall not
No compare performed
LOGICAL BLOCK
REFERENCE TAG
(not type 3)
Shall g
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 1)
Shall h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 0)
Shall not
No compare performed
No
Error condition a


010b b
Yes
LOGICAL BLOCK GUARD
Shall not
No compare performed
LOGICAL BLOCK
APPLICATION TAG
(ATO = 1) e
Shall i
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 0) f
Shall not
No compare performed
LOGICAL BLOCK
REFERENCE TAG
(not type 3)
Shall g
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 1)
Shall h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 0)
Shall not
No compare performed
No
Error condition a
011b
100b  b
Yes
LOGICAL BLOCK GUARD
Shall
LOGICAL BLOCK GUARD CHECK
FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 1) e
Shall i
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 0) f
Shall not
No compare performed
LOGICAL BLOCK
REFERENCE TAG
(not type 3)
Shall g
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 1)
Shall h
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
(type 3 and ATO = 0)
Shall not
No compare performed
No
Error condition a
Table 128 — VRPROTECT field with the BYTCHK field set to 01b or 11b – compare operation requirements
(part 2 of 4)
Code
Logical unit
formatted
with
protection
information
Field in protection
information j
Compare
operation
If compare fails c d, additional sense
code


101b b
Yes
LOGICAL BLOCK GUARD
Shall
LOGICAL BLOCK GUARD CHECK
FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 1) e
Shall i
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
APPLICATION TAG
(ATO = 0) f
Shall not
No compare performed
LOGICAL BLOCK
REFERENCE TAG
Shall not
No compare performed
No
Error condition a
110b to
111b
Reserved
Table 128 — VRPROTECT field with the BYTCHK field set to 01b or 11b – compare operation requirements
(part 3 of 4)
Code
Logical unit
formatted
with
protection
information
Field in protection
information j
Compare
operation
If compare fails c d, additional sense
code


a If the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to MISCOMPARE.
d If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
e If the ATO bit is set to one in the Control mode page (see SPC-6), then the device server shall not modify
the logical block application tag.
f
If the ATO bit is set to zero in the Control mode page (see SPC-6), then the device server may modify
any logical block application tag.
g If the BYTCHK field is set to 11b, then the device server shall compare the value from each LOGICAL BLOCK
REFERENCE TAG field received in the single logical block data from the Data-Out Buffer with the
corresponding LOGICAL BLOCK REFERENCE TAG field in the first logical block from the verify operations,
and the device server shall compare the value of the previous LOGICAL BLOCK REFERENCE TAG field plus
one with each of the subsequent LOGICAL BLOCK REFERENCE TAG fields (see 4.22.3).
h If the BYTCHK field is set to 11b, then the device server shall compare the value from each LOGICAL BLOCK
REFERENCE TAG field received in the single logical block data from the Data-Out Buffer with the
corresponding LOGICAL BLOCK REFERENCE TAG field in each logical block from the verify operations
(see 4.21.3).
i
If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field and the
ATO bit is set to one in the Control mode page (see SPC-6), then the device server shall compare each
logical block application tag. If the ATO bit is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK
field in the CDB, if the command is a VERIFY (32) command;
b)
the Application Tag mode page (see 6.5.3), if the command is not a VERIFY (32) command and the
ATMPE bit in the Control mode page (see SPC-6) is set to one; or
c)
a method not defined by this standard, if the command is not a VERIFY (32) command and the
ATMPE bit is set to zero.
j
If the device server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.22.2.3) or type 2
protection (see 4.22.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.22.2.5) is enabled,
then the device server shall not compare any protection information in the associated protection
information interval.
Table 128 — VRPROTECT field with the BYTCHK field set to 01b or 11b – compare operation requirements
(part 4 of 4)
Code
Logical unit
formatted
with
protection
information
Field in protection
information j
Compare
operation
If compare fails c d, additional sense
code


5.37 VERIFY (12) command
The VERIFY (12) command (see table 129) requests that the device server perform the actions defined for
the VERIFY (10) command (see 5.36).
NOTE 15 - Migration from the VERIFY (12) command to the VERIFY (16) command is recommended for all
implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 129 for the
VERIFY (12) command.
See the VERIFY (10) command (see 5.36) for the definitions of the other fields in this command.
Table 129 — VERIFY (12) command
Bit
Byte
OPERATION CODE (AFh)
VRPROTECT
DPO
Reserved
BYTCHK
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
VERIFICATION LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.38 VERIFY (16) command
The VERIFY (16) command (see table 130) requests that the device server perform the actions defined for
the VERIFY (10) command (see 5.36).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 130 for the
VERIFY (16) command.
See the VERIFY (10) command (see 5.36) for the definitions of the other fields in this command.
Table 130 — VERIFY (16) command
Bit
Byte
OPERATION CODE (8Fh)
VRPROTECT
DPO
Reserved
BYTCHK
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
VERIFICATION LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.39 VERIFY (32) command
The VERIFY (32) command (see table 131) requests that the device server perform the actions defined for
the VERIFY (10) command (see 5.36).
The device server shall process a VERIFY (32) command only if type 2 protection is enabled (see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 131 for the VERIFY (32) command.
See the VERIFY (10) command (see 5.36) for the definitions of the CONTROL byte, the GROUP NUMBER field,
the VRPROTECT field, the DPO bit, the BYTCHK field, the LOGICAL BLOCK ADDRESS field, and the VERIFICATION
LENGTH field.
If checking of the LOGICAL BLOCK REFERENCE TAG field is enabled (see table 125, table 126, table 127, and
table 128 in 5.36), then the EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG field contains the value of the
LOGICAL BLOCK REFERENCE TAG field expected in the protection information of the first logical block accessed
by the command instead of a value based on the LBA (see 4.21.3).
Table 131 — VERIFY (32) command
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
SERVICE ACTION (000Ah)
(LSB)
VRPROTECT
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
VERIFICATION LENGTH
•••
(LSB)
