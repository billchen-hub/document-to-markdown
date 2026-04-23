# 5.10 ORWRITE (16) command

5.9.2.2 Stream status descriptor
The stream status descriptor (see table 65) contains stream status information for one open stream.
The STREAM IDENTIFIER field contains the stream identifier of an open stream.
5.9.2.3 Stream status descriptor relationships
The STREAM IDENTIFIER field in the first stream status descriptor returned in the GET STREAM STATUS
parameter data shall contain:
a)
the value specified in the STARTING STREAM IDENTIFIER field of the CDB if that stream is open; or
b)
the value of the next greater stream identifier of an open stream.
If the value specified in the STARTING STREAM IDENTIFIER field of the CDB is greater than the highest stream
identifier of an open stream, then the device server shall not return any stream status descriptors.
For subsequent stream status descriptors, the contents of the STREAM IDENTIFIER field shall contain the value
of the next greater stream identifier of an open stream.
5.10 ORWRITE (16) command
The ORWRITE (16) command (see table 66) requests that the device server perform an ORWRITE command
operation (see 4.27.4).
Table 65 — Stream status descriptor format
Bit
Byte
Reserved
(MSB)
STREAM IDENTIFIER
(LSB)
Reserved
•••


This command uses the variable length CDB format (see clause A.1).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 66 for the
ORWRITE (16) command.
See the READ (10) command (see 5.16) for the definition of the FUA bit specifying behavior for read
operations. See the WRITE (10) command (see 5.40) for the definition of the FUA bit specifying behavior for
write operations. See the READ (10) command (see 5.16) for the definition of the DPO bit. See the
PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field. See the
PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
The TRANSFER LENGTH field specifies the number of contiguous logical blocks of data that are read, transferred
from the Data-Out Buffer, and ORed into a bitmap buffer, starting with the logical block referenced by the LBA
specified by the LOGICAL BLOCK ADDRESS field. If the specified LBA and the specified transfer length exceed
the capacity of the medium (see 4.5), then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
LOGICAL BLOCK ADDRESS OUT OF RANGE. The TRANSFER LENGTH field is constrained by the MAXIMUM
TRANSFER LENGTH field (see 6.6.4).
The CONTROL byte is defined in SAM-6.
The device server shall:
a)
check protection information from the read operations based on the ORPROTECT field as described in
table 67; and
b)
check protection information transferred from the Data-Out Buffer based on the ORPROTECT field as
described in table 68.
The order of the user data and protection information checks and comparisons is vendor specific.
Table 66 — ORWRITE (16) command
Bit
Byte
OPERATION CODE (8Bh)
ORPROTECT
DPO
FUA
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


The device server shall check the protection information from the read operations based on the ORPROTECT
field as described in table 67. All footnotes for table 67 are at the end of the table.
Table 67 — ORPROTECT field - checking protection information from the read operations (part 1 of 3)
Code
Logical unit
formatted with
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
Yes i j
LOGICAL
BLOCK GUARD
GRD_CHK = 1
LOGICAL BLOCK GUARD CHECK
FAILED
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
LOGICAL BLOCK GUARD CHECK
FAILED
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
LOGICAL BLOCK GUARD CHECK
FAILED
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
Table 67 — ORPROTECT field - checking protection information from the read operations (part 2 of 3)
Code
Logical unit
formatted with
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


110b to
111b
Reserved
a If  the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field, then the
device server shall check the logical block application tag. If the ATO bit in the Control mode page (see
SPC-6) is set to one, then this knowledge is acquired from:
a)
the Application Tag mode page (see 6.5.3), if the ATMPE bit in the Control mode page (see SPC-6)
is set to one; or.
b)
a method not defined by this standard, if the ATMPE bit is set to zero.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
f
See the Extended INQUIRY Data VPD page (see SPC-6) for the definitions of the GRD_CHK bit, the
APP_CHK bit, and the REF_CHK bit.
g If the device server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, and type 1 protection (see 4.21.2.3) is
enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, the LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection
information interval.
h If type 1 protection is enabled, then the device server shall check the logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 3 protection is
enabled, then the device server shall check each logical block reference tag only if the device server
has knowledge of the contents of the LOGICAL BLOCK REFERENCE TAG field. The method for acquiring this
knowledge is not defined by this standard.
i
If the RWWP bit in the Control mode page (see SPC-6) is set to one, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB.
j
If the DPICZ bit in the Control mode page (see SPC-6) is set to one, and the RWWP bit in the Control
mode page is set to zero, then protection information shall not be checked.
Table 67 — ORPROTECT field - checking protection information from the read operations (part 3 of 3)
Code
Logical unit
formatted with
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


The device server shall check the protection information transferred from the Data-Out Buffer based on the
ORPROTECT field as described in table 68. All footnotes for table 68 are at the end of the table.
Table 68 — ORPROTECT field - checking protection information from the Data-Out Buffer (part 1 of 2)
Code
Logical unit
formatted with
protection
information
Field in
protection
information
Device server
check
If check fails d h, additional sense code
000b
Yes e f g
No protection information in the Data-Out buffer to check
No
No protection information in the Data-Out buffer to check
001b b
Yes
LOGICAL BLOCK
GUARD
Shall
LOGICAL BLOCK GUARD CHECK
FAILED
LOGICAL BLOCK
APPLICATION TAG
Dependent on
RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
Shall (except
for type 3) i
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
Dependent on
RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May i
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
LOGICAL BLOCK GUARD CHECK
FAILED
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
LOGICAL BLOCK GUARD CHECK
FAILED
LOGICAL BLOCK
APPLICATION TAG
Dependent on
RWWP c
LOGICAL BLOCK APPLICATION TAG
CHECK FAILED
LOGICAL BLOCK
REFERENCE TAG
May i
LOGICAL BLOCK REFERENCE TAG
CHECK FAILED
No
Error condition a
110b to
111b
Reserved
a If a logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the ATO bit is set to one in the Control mode page (see SPC-6), and the device server has knowledge
of the contents of the LOGICAL BLOCK APPLICATION TAG field, then the device server:
a)
may check each logical block application tag if the RWWP bit is set to zero in the Control mode page
(see SPC-6); and
b)
shall check each logical block application tag if the RWWP bit is set to one in the Control mode page.
If the ATMPE bit in the Control mode page (see SPC-6) is set to one, then this knowledge is acquired
from the Application Tag mode page. If the ATMPE bit is set to zero, then the method for acquiring this
knowledge is not defined by this standard.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e The device server shall write a generated CRC (see 4.21.4.2) into each LOGICAL BLOCK GUARD field.
f
If the RWWP bit in the Control mode page (see SPC-6) is set to one, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN CDB. If the RWWP bit is set to zero, and:
a)
type 1 protection is enabled, then the device server shall write the least significant four bytes of
each LBA into the LOGICAL BLOCK REFERENCE TAG field of each of the written logical blocks; or
b)
type 3 protection is enabled, then the device server shall write a value of FFFF_FFFFh into the
LOGICAL BLOCK REFERENCE TAG field of each of the written logical blocks.
g If the ATO bit is set to one in the Control mode page (see SPC-6), then the device server shall write
FFFFh into each LOGICAL BLOCK APPLICATION TAG field. If the ATO bit is set to zero, then the device server
may write any value into each LOGICAL BLOCK APPLICATION TAG field.
h If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
i
If type 1 protection is enabled, then the device server shall check the logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 3 protection is
enabled, then the device server may check each logical block reference tag if the ATO bit is set to one in
the Control mode page (see SPC-6), and the device server has knowledge of the contents of the
LOGICAL BLOCK REFERENCE TAG. The method for acquiring this knowledge is not defined by this
standard.
Table 68 — ORPROTECT field - checking protection information from the Data-Out Buffer (part 2 of 2)
Code
Logical unit
formatted with
protection
information
Field in
protection
information
Device server
check
If check fails d h, additional sense code
