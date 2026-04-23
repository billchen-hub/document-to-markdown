# 4.29 Atomic writes

The logical block length associated with the block device zero ROD token is that of the direct access block
device to which the data is being written (e.g., if a block device zero ROD token is used to write to a logical
unit that has 642-byte logical blocks, then the logical block length of the block device zero ROD token is 642
bytes).
The ROD TOKEN TYPE field is defined in SPC-6 and shall be set to the value shown in table 31 for the block
device zero ROD token.
The ROD TOKEN LENGTH field is defined in SPC-6 and shall be set to the value shown in table 31 for the block
device zero ROD token.
A CRC VALID bit set to one indicates that the token represents user data in which the protection information, if
any, has the LOGICAL BLOCK GUARD field in the protection information set to 0000h. A CRC VALID bit set to zero
indicates that the token represents user data in which the protection information, if any, has the LOGICAL BLOCK
GUARD field in the protection information set to FFFFh.
4.28.5 ROD token device type specific data
The device type specific data for ROD tokens (see SPC-6) created by a copy manager for a direct access
block devices (see 6.7):
a)
provides information about the logical unit at the time that the ROD token was created; and
b)
is a subset of the parameter data returned by the READ CAPACITY (16) command (see 5.21) for the
logical unit that contains the copy manager that created the ROD token.
If the READ CAPACITY (16) parameter data changes so that the copy manager that created the ROD token is
no longer able to access the data represented by the ROD token, then that copy manager shall invalidate the
ROD token.
4.29 Atomic writes
4.29.1 Atomic writes overview
An atomic write command performs one or more atomic write operations. The following write commands are
atomic write commands:
a)
WRITE ATOMIC (16) (see 5.48); and
b)
WRITE ATOMIC (32) (see 5.49).
To perform an atomic write operation, the device server:
a)
ensures that any subsequent read operation returns either all of the write data or none of the write
data for the atomic write operation as described in 4.29.2;
b)
performs operations as described in 4.29.3; and
c)
processes ACA conditions as described in 4.29.4.
The MAXIMUM ATOMIC TRANSFER LENGTH field (see 6.6.4) indicates the maximum transfer length for atomic
write commands that specify an atomic boundary set to zero. If an atomic write command specifies an atomic
boundary set to zero and a transfer length greater than the maximum atomic transfer length, then the device
server shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB, and the field pointer pointing to the
TRANSFER LENGTH field in the CDB.
The MAXIMUM ATOMIC TRANSFER LENGTH WITH ATOMIC BOUNDARY field  (see 6.6.4) indicates the maximum
transfer length for atomic write commands that specify an atomic boundary set to a non-zero value. If an
atomic write command specifies a non-zero atomic boundary and the transfer length is greater than the
maximum atomic transfer length with atomic boundary, then the device server shall terminate the command
with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST, the additional sense code set
to INVALID FIELD IN CDB, and the field pointer pointing to the TRANSFER LENGTH field in the CDB.


The MAXIMUM ATOMIC BOUNDARY SIZE field (see 6.6.4) indicates the maximum atomic boundary for atomic write
commands. If an atomic write command specifies a non-zero atomic boundary that is greater than the
maximum atomic boundary size, then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST, the additional sense code set to INVALID
FIELD IN CDB, and the field pointer pointing to the ATOMIC BOUNDARY field in the CDB.
If the starting LBA of an atomic write command does not meet the requirements of the ATOMIC ALIGNMENT field
(see 6.6.4), then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If the ATOMIC TRANSFER LENGTH GRANULARITY field (see 6.6.4) contains a non-zero value and:
a)
the TRANSFER LENGTH field in an atomic write command is not a multiple of the atomic transfer length
granularity; or
b)
the ATOMIC BOUNDARY field in an atomic write command contains a non-zero value that is not a
multiple of the atomic transfer length granularity,
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If an atomic write command specifies a non-zero atomic boundary that is less than or equal to the maximum
atomic boundary size and a transfer length that is less than or equal to the maximum atomic transfer length
with atomic boundary, then the device server shall perform one or more atomic write operations each of which
is a size that is a multiple of the size specified in the ATOMIC BOUNDARY field.
If multiple atomic write operations are performed as a result of a non-zero atomic boundary, then:
a)
the atomic write operations may be performed in any order; and
b)
if the device server is unable to complete all atomic write operations, then the device server shall
terminate the command with the sense key set to ABORTED COMMAND and the additional sense
code set to INCOMPLETE MULTIPLE ATOMIC WRITE OPERATIONS.
If the device server supports atomic write commands, then the device server shall process commands as
described in SAM-6 with the additional restrictions described in 4.29.
4.29.2 Atomic write operations that do not complete
If the device server is not able to successfully complete an atomic write operation (e.g., the command is
terminated or aborted), then the device server shall ensure that none of the LBAs specified by the atomic write
operation have been altered by any logical block data from the atomic write operation (i.e., the specified LBAs
return logical block data as if the atomic write operation had not occurred).
If a power loss causes loss of logical block data from an atomic write operation in a volatile write cache that
has not yet been stored on the medium, then the device server shall ensure that none of the LBAs specified
by the atomic write operation have been altered by any logical block data from the atomic write operation (i.e.,
the specified LBAs return logical block data as if the atomic write operation had not occurred and writes from
the cache to the medium preserve the specified atomicity).
EXAMPLE - If the device server processes an atomic write command that specifies a non-zero atomic boundary using five
atomic write operations in such a way that:
1)
two atomic write operations are performed successfully;
2)
an atomic write operation encounters an error; and
3)
the remaining two atomic write operations are not performed,
then subsequent read commands of the LBAs written by the two successful atomic write operations return
new logical block data and subsequent read commands of the LBAs specified by the other three atomic
write operations return old logical block data.


4.29.3 Performing operations with respect to atomic write operations
4.29.3.1 Performing operations before and after an atomic write operation
Before an atomic write operation completes, the device server shall not use any logical block data from the
atomic write operation for any other operations (e.g., read operations return old logical block data until the
atomic write operation completes).
After an atomic write operation completes, the device server shall use all of the logical block data from the
atomic write operation as the basis for subsequent operations (e.g., read operations return logical block data
from the atomic write operation).
4.29.3.2 Performing operations during an atomic write operation
Table 32 defines the device server requirements for starting to perform an atomic write operation that has an
overlapping LBA with an operation that the device server is already performing.
If the device server is performing an atomic write operation and is requested to perform an operation that has
an LBA that overlaps with that atomic write operation, then the device server shall complete that atomic write
operation before performing the requested operation.
EXAMPLE 1 - While the device server is performing an atomic write operation that accesses LBAs 0 to 15, it may perform
a second atomic write operation accessing LBAs 16 to 31 and shall not perform a third atomic write operation accessing
LBAs 7 to 15. After the first atomic write operation completes, the device server may perform the third atomic write
operation.
EXAMPLE 2 -While the device server is performing an atomic write operation that accesses LBAs 0 to 15, if a second write
operation accessing LBAs 7 to 31 is available for performing, then the device server may perform the write operation’s
accesses to LBAs 16 to 31 and shall not perform the write operation’s accesses to LBAs 7 to 15. After the atomic write
operation completes, the device server may perform the write operation’s accesses to LBAs 7 to 15.
Performing an atomic write operation does not prevent the device server from performing, at any time, other
operations that only contain non-overlapping LBAs.
Table 32 — Performing atomic write operations with overlapping LBAs during current operations
Operation A that is currently being
processed by the device server is a
Device server is requested to perform an atomic
write operation B that accesses an LBA that is
being accessed by operation A
read or verify
The device server shall perform one of the following:
a)
should complete operation A before starting
operation B; or
b)
may terminate operation A with CHECK
CONDITION status with a sense key of
ABORTED COMMAND and an additional
sense code set to OVERLAPPING ATOMIC
COMMAND IN PROGRESS before starting
operation B.
write or unmap
format or sanitize
The device server shall terminate operation B as
specified in 4.11.2 and 4.33.2
Uninterruptible sequence of operations
The device server shall wait for operation A to complete
before it starts performing operation B.
atomic write
