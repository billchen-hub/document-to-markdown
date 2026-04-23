# 5.16 READ (10) command

prevention of medium removal function for a SCSI initiator port (e.g., an initiator port is not operating
correctly).
While a prevention of medium removal condition is in effect, the logical unit shall inhibit mechanisms that allow
removal of the medium by an operator.
5.16 READ (10) command
The READ (10) command (see table 78) requests that the device server:
a)
perform read operations from the specified LBAs: and
b)
transfer the requested logical block data to the Data-In Buffer.
The logical block data transferred to the Data-In Buffer shall include protection information based on the value
in the RDPROTECT field (see table 79) and the medium format.
NOTE 8 - Migration from the READ (10) command to the READ (16) command is recommended for all
implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 78 for the
READ (10) command.
Table 78 — READ (10) command
Bit
Byte
OPERATION CODE (28h)
RDPROTECT
DPO
FUA
RARC
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


The device server shall check the protection information from the read operations before returning status for
the command based on the RDPROTECT field as described in table 79. All footnotes for table 79 are at the end
of the table.
Table 79 — RDPROTECT field  (part 1 of 3)
Code
Logical unit
formatted
with
protection
information
Shall device
server
transmit
protection
information?
Field in
protection
information h
Extended
INQUIRY Data
VPD page bit
value g
If check fails d f,
additional sense code
000b
Yes j
No
LOGICAL BLOCK
GUARD
GRD_CHK = 1
LOGICAL BLOCK
GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK
APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL BLOCK
REFERENCE
TAG
REF_CHK = 1 i
LOGICAL BLOCK
REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No
No protection information available to check
001b
101b b
Yes
Yes e
LOGICAL BLOCK
GUARD
GRD_CHK = 1
LOGICAL BLOCK
GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK
APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL BLOCK
REFERENCE
TAG
REF_CHK = 1 i
LOGICAL BLOCK
REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No a
No protection information available to transmit to the Data-In Buffer or for
checking


010b b
Yes
Yes e
LOGICAL BLOCK
GUARD
No check performed
LOGICAL BLOCK
APPLICATION
TAG
APP_CHK = 1 c
LOGICAL BLOCK
APPLICATION TAG
CHECK FAILED
APP_CHK = 0
No check performed
LOGICAL BLOCK
REFERENCE
TAG
REF_CHK = 1 i
LOGICAL BLOCK
REFERENCE TAG
CHECK FAILED
REF_CHK = 0
No check performed
No a
No protection information available to transmit to the Data-In Buffer or for
checking
011b b
Yes
Yes e
LOGICAL BLOCK
GUARD
No check performed
LOGICAL BLOCK
APPLICATION
TAG
No check performed
LOGICAL BLOCK
REFERENCE
TAG
No check performed
No a
No protection information available to transmit to the Data-In Buffer or for
checking
100b b
Yes
Yes e
LOGICAL BLOCK
GUARD
GRD_CHK = 1
LOGICAL BLOCK
GUARD CHECK FAILED
GRD_CHK = 0
No check performed
LOGICAL BLOCK
APPLICATION
TAG
No check performed
LOGICAL BLOCK
REFERENCE
TAG
No check performed
No a
No protection information available to transmit to the Data-In Buffer or for
checking
110b to
111b
Reserved
Table 79 — RDPROTECT field  (part 2 of 3)
Code
Logical unit
formatted
with
protection
information
Shall device
server
transmit
protection
information?
Field in
protection
information h
Extended
INQUIRY Data
VPD page bit
value g
If check fails d f,
additional sense code


A disable page out (DPO) bit set to zero specifies that the retention priority shall be determined by the
RETENTION PRIORITY fields in the Caching mode page (see 6.5.6). A DPO bit set to one specifies that the device
server shall assign the logical blocks accessed by this command the lowest retention priority for being fetched
into or retained by the cache (see 4.15). A DPO bit set to one overrides any retention priority specified in the
Caching mode page. All other aspects of the algorithm implementing the cache replacement strategy are not
defined by this standard.
NOTE 9 - The DPO bit is used to control replacement of logical blocks in the cache when the application client
has information on the future usage of the logical blocks. If the DPO bit is set to one, then the application client
a If the logical unit supports protection information (see 4.21) and has not been formatted with protection
information, then the device server shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB.
b If the logical unit does not support protection information, then the device server should terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
c If the device server has knowledge of the contents of the LOGICAL BLOCK APPLICATION TAG field, then the
device server shall check each logical block application tag. If the ATO bit in the Control mode page
(see SPC-6) is set to one, then this knowledge is acquired from:
a)
the EXPECTED LOGICAL BLOCK APPLICATION TAG field and the LOGICAL BLOCK APPLICATION TAG MASK
field in the CDB, if a READ (32) command (see 5.19) is received by the device server;
b)
the Application Tag mode page (see 6.5.3), if a command other than READ (32) is received by the
device server, and the ATMPE bit in the Control mode page (see SPC-6) is set to one; or
c)
a method not defined by this standard, if a command other than READ (32) is received by the
device server, and the ATMPE bit is set to zero.
d If the device server terminates the command with CHECK CONDITION status, then the device server
shall set the sense key to ABORTED COMMAND.
e The device server shall transmit protection information to the Data-In Buffer.
f
If multiple errors occur while the device server is processing the command, then the selection by the
device server of which error to report is not defined by this standard.
g See the Extended INQUIRY Data VPD page (see SPC-6) for the definitions of the GRD_CHK bit, the
APP_CHK bit, and the REF_CHK bit.
h If the device server detects:
a)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, and type 1 protection (see 4.21.2.3) or type 2
protection (see 4.21.2.4) is enabled; or
b)
a LOGICAL BLOCK APPLICATION TAG field set to FFFFh, the LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server shall not check any protection information in the associated protection
information interval.
i
If type 1 protection is enabled, then the device server shall check the logical block reference tag by
comparing it to the lower four bytes of the LBA associated with the logical block. If type 2 protection or
type 3 protection is enabled, and the device server has knowledge of the contents of the LOGICAL
BLOCK REFERENCE TAG field, then the device server shall check each logical block reference tag. If type
2 protection is enabled, then this knowledge may be acquired through the EXPECTED INITIAL LOGICAL
BLOCK REFERENCE TAG field in a READ (32) command (see 5.19). If type 3 protection is enabled, then
the method for acquiring this knowledge is not defined by this standard.
j
If the DPICZ bit in the Control mode page (see SPC-6) is set to one, then protection information shall not
be checked.
Table 79 — RDPROTECT field  (part 3 of 3)
Code
Logical unit
formatted
with
protection
information
Shall device
server
transmit
protection
information?
Field in
protection
information h
Extended
INQUIRY Data
VPD page bit
value g
If check fails d f,
additional sense code
