# 5.12 POPULATE TOKEN command

5.12 POPULATE TOKEN command
5.12.1 POPULATE TOKEN command overview
The POPULATE TOKEN command (see table 71) requests that the copy manager (see SPC-6) create a point
in time ROD token that represents the specified logical blocks (see 4.28).
Each logical block represented by the point in time ROD token includes logical block data.
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 71 for the POPULATE TOKEN command.
The LIST IDENTIFIER field is defined in SPC-6. The list identifier shall be processed as if the LIST ID USAGE field
in the parameter data for an EXTENDED COPY(LID4) command (see SPC-6) is set to 00b.
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter list that is available to be
transferred from the Data-Out Buffer. If the parameter list length is greater than zero and less than 00000010h
(i.e., 16), then the copy manager shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to PARAMETER LIST LENGTH
ERROR. A PARAMETER LIST LENGTH field set to zero specifies that no data shall be transferred. This shall not
be considered an error.
See the PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
The CONTROL byte is defined in SAM-6.
Table 71 — POPULATE TOKEN command
Bit
Byte
OPERATION CODE (83h)
Reserved
SERVICE ACTION (10h)
Reserved
•••
(MSB)
LIST IDENTIFIER
•••
(LSB)
(MSB)
PARAMETER LIST LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.12.2 POPULATE TOKEN parameter list
The parameter list for the POPULATE TOKEN command is shown in table 72.
The POPULATE TOKEN DATA LENGTH field specifies the length in bytes of the data that is available to be
transferred from the Data-Out Buffer. The populate token data length does not include the number of bytes in
the POPULATE TOKEN DATA LENGTH field. If the POPULATE TOKEN DATA LENGTH field is less than 001Eh (i.e., 30),
then the copy manager shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
A ROD type valid (RTV) bit set to zero specifies that the copy manager may create a ROD token with any point
in time copy ROD type and shall ignore the contents of the ROD TYPE field. An RTV bit set to one specifies that
the copy manager shall use the contents of the ROD TYPE field to create the point in time copy ROD.
The immediate (IMMED) bit specifies when the copy manager shall return status for the POPULATE TOKEN
command. If the IMMED bit is set to zero, then the copy manager shall process the POPULATE TOKEN
command until all specified operations are complete or an error is detected. If the IMMED bit is set to one, then
the copy manager:
1)
shall validate the CDB (i.e., detect and report all errors in the CDB);
2)
shall transfer all the parameter data to the copy manager;
Table 72 — POPULATE TOKEN parameter list
Bit
Byte
(MSB)
POPULATE TOKEN DATA LENGTH (n - 1)
(LSB)
Reserved
RTV
IMMED
Reserved
(MSB)
INACTIVITY TIMEOUT
•••
(LSB)
(MSB)
ROD TYPE
•••
(LSB)
Reserved
(MSB)
BLOCK DEVICE RANGE DESCRIPTOR LENGTH (n - 15)
(LSB)
Block device range descriptor list
Block device range descriptor [first] (see 5.12.3)
•••
•••
n - 15
Block device range descriptor [last] (see 5.12.3) (if any)
•••
n


3)
may validate the parameter data;
4)
shall complete the POPULATE TOKEN command with GOOD status; and
5)
shall complete performing of all specified operations as a background operation (see SPC-6).
If the INACTIVITY TIMEOUT field is not set to zero, then the INACTIVITY TIMEOUT field specifies the number of
seconds to use for the ROD token inactivity timeout (see SPC-6). If the INACTIVITY TIMEOUT field is set to a
value larger than the value in the MAXIMUM INACTIVITY TIMEOUT field (see 6.6.9.3), then the copy manager shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the INACTIVITY TIMEOUT field is set to zero, then the DEFAULT INACTIVITY TIMEOUT field (see 6.6.9.3) specifies
the number of seconds to use for the ROD token inactivity timeout (see SPC-6).
If the RTV bit is set to one, then the ROD TYPE field specifies the ROD type (see SPC-6) for creating the point in
time copy ROD token. The copy manager shall terminate the command with CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
PARAMETER LIST, if:
a)
the copy manager does not support the specified ROD type for use with the POPULATE TOKEN
command; or
b)
the ROD TYPE field specifies a ROD type (see SPC-6) that is not a point in time copy ROD.
The BLOCK DEVICE RANGE DESCRIPTOR LENGTH field specifies the length in bytes of the block device range
descriptor list. The block device range descriptor list length should be a multiple of 16. If the block device
range descriptor list length is not a multiple of 16, then the last block device range descriptor is incomplete
and shall be ignored. If the block device range descriptor list length is less than 0010h (i.e.,16), then the copy
manager shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If any block device range descriptors in the block device range descriptor list are truncated as a result of the
parameter list length in the CDB, then those block device range descriptors shall be ignored.
If the number of complete block device range descriptors is larger than the maximum range descriptors value
in the block device ROD token limits descriptor (see 6.6.9.3), then the copy manager shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to TOO MANY SEGMENT DESCRIPTORS.
If the same LBA is included in more than one block device range descriptor, then the copy manager shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the number of bytes of user data represented by the sum of the contents of the NUMBER OF LOGICAL BLOCKS
fields in all of the complete block device range descriptors is larger than:
a)
the MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type specific features descriptor in the
ROD token features third-party copy descriptor in the Third-party Copy VPD page (see SPC-6) and
that field is set to a non-zero value; or
b)
the MAXIMUM TOKEN TRANSFER SIZE field (see 6.6.9.3) and that field is set to a non-zero value,
then the copy manager shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.


5.12.3 Block device range descriptor
The block device range descriptor is shown in table 73.
The LOGICAL BLOCK ADDRESS field specifies the first LBA on which the copy manager shall operate for this
block device range descriptor.
The NUMBER OF LOGICAL BLOCKS field specifies the number of logical blocks on which the copy manager shall
operate for this block device range descriptor beginning with the LBA specified by the LOGICAL BLOCK ADDRESS
field.
Processing of block device range descriptors with a number of logical blocks that is not a multiple of the
OPTIMAL BLOCK ROD LENGTH GRANULARITY field in the block ROD device type specific features descriptor in the
ROD token features third-party copy descriptor in the Third-party Copy VPD page (see SPC-6) may incur
delays in processing. If the OPTIMAL BLOCK ROD LENGTH GRANULARITY field in the block ROD device type
specific features descriptor in the ROD token features third-party copy descriptor in the Third-party Copy VPD
page is not reported, then the optimal transfer length granularity in the Block Limits VPD page (see 6.6.4) may
indicate the granularity.
For a POPULATE TOKEN command, processing of block device range descriptors where the number of bytes
of user data contained in the number of logical blocks exceeds the OPTIMAL BYTES TO TOKEN PER SEGMENT field
in the block ROD device type specific features descriptor in the ROD token features third-party copy
descriptor in the Third-party Copy VPD page may incur delays in processing.
For a WRITE USING TOKEN command (see 5.59), processing of block device range descriptors where the
number of bytes of user data contained in the number of logical blocks exceeds the OPTIMAL BYTES FROM
TOKEN PER SEGMENT field in the block ROD device type specific features descriptor in the ROD token features
third-party copy descriptor in the Third-party Copy VPD page may incur delays in processing.
If the number of bytes of user data contained in the number of logical blocks is greater than:
1)
the value in the MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type specific features
descriptor in the ROD token features third-party copy descriptor in the Third-party Copy VPD page,
and the MAXIMUM BYTES IN BLOCK ROD field is set to a non-zero value; or
2)
the value in the MAXIMUM TRANSFER LENGTH field (see 6.6.4), the MAXIMUM TRANSFER LENGTH field is
set to a non-zero value, and the MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type
specific features descriptor is not reported,
then the copy manager shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the NUMBER OF LOGICAL BLOCKS field is set to zero, then the copy manager shall perform no operation for this
block device range descriptor. This condition shall not be considered an error.
Table 73 — Block device range descriptor
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


If the specified LBA and the specified number of logical blocks exceed the capacity of the medium (see 4.5),
then the copy manager shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS OUT OF RANGE.
5.13 PRE-FETCH (10) command
The PRE-FETCH (10) command (see table 74) requests that the device server:
a)
for any mapped LBAs specified by the command that are not already contained in cache,  perform
read medium operations and write cache operations (see 4.15); and
b)
for any unmapped LBAs specified by the command, update the volatile cache and/or non-volatile
cache to prevent retrieval of stale data.
No data shall be transferred to the Data-In Buffer.
NOTE 7 - Migration from the PRE-FETCH (10) command to the PRE-FETCH (16) command is
recommended for all implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 74 for the
PRE-FETCH (10) command.
An immediate (IMMED) bit set to zero specifies that status shall be returned after the operation is complete. An
IMMED bit set to one specifies that the device server shall:
a)
validate the CDB;
b)
if the cache has:
A) sufficient capacity to accept all of the specified logical blocks, then complete the command with
CONDITION MET status; or
B) insufficient capacity to accept all of the specified logical blocks, then complete the command with
GOOD status;
and
c)
if one or more of the specified logical blocks are not successfully transferred to the cache for reasons
other than lack of cache capacity, then report a deferred error (see SPC-6).
The LOGICAL BLOCK ADDRESS field specifies the LBA of the first logical block (see 4.5) accessed by this
command.
Table 74 — PRE-FETCH (10) command
Bit
Byte
OPERATION CODE (34h)
Reserved
IMMED
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
GROUP NUMBER
(MSB)
PREFETCH LENGTH
(LSB)
CONTROL


A GROUP NUMBER field set to a non-zero value specifies the group into which attributes associated with the
command should be collected (see 4.22). A GROUP NUMBER field set to zero specifies that any attributes
associated with the command shall not be collected into any group.
The PREFETCH LENGTH field specifies the number of contiguous logical blocks that shall be pre-fetched (i.e.,
transferred to the cache from the medium), starting with the LBA specified by the LOGICAL BLOCK ADDRESS
field. A PREFETCH LENGTH field set to zero specifies that all logical blocks starting with the LBA specified in the
LOGICAL BLOCK ADDRESS field to the last logical block on the medium shall be pre-fetched. Any other value
specifies the number of logical blocks that shall be pre-fetched. If the specified LBA and the specified prefetch
length exceed the capacity of the medium (see 4.5), then the device server shall terminate the command with
CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to LOGICAL BLOCK ADDRESS OUT OF RANGE.
The CONTROL byte is defined in SAM-6.
If the IMMED bit is set to zero, and the specified logical blocks were transferred to the cache without error, then
the device server shall complete the command with CONDITION MET status.
If the IMMED bit is set to zero and the cache does not have sufficient capacity to accept all of the specified
logical blocks, then the device server shall transfer to the cache as many of the specified logical blocks that fit.
If these logical blocks are transferred without error, then the device server shall complete the command with
GOOD status.
5.14 PRE-FETCH (16) command
The PRE-FETCH (16) command (see table 75) requests that the device server perform the actions defined for
the PRE-FETCH (10) command (see 5.13).
No data shall be transferred to the Data-In Buffer.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 75 for the
PRE-FETCH (16) command.
See the PRE-FETCH (10) command (see 5.13) for the definitions of the other fields in this command.
Table 75 — PRE-FETCH (16) command
Bit
Byte
OPERATION CODE (90h)
Reserved
IMMED
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
PREFETCH LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.15 PREVENT ALLOW MEDIUM REMOVAL command
The PREVENT ALLOW MEDIUM REMOVAL command (see table 76) requests that the logical unit enable or
disable the removal of the medium. If medium removal is prevented on any I_T nexus that has access to the
logical unit, then the logical unit shall not allow medium removal.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 76 for the
PREVENT ALLOW MEDIUM REMOVAL command.
Table 77 defines the PREVENT field.
The CONTROL byte is defined in SAM-6.
The prevention of medium removal shall begin when any application client issues a PREVENT ALLOW
MEDIUM REMOVAL command with the PREVENT field set to 01b (i.e., medium removal prevented). The
prevention of medium removal for the logical unit shall no longer be prevented after:
a)
one of the following occurs for each I_T nexus through which medium removal had been prevented:
A) receipt of a PREVENT ALLOW MEDIUM REMOVAL command with the PREVENT field set to 00b;
or
B) an I_T nexus loss;
b)
a power on;
c)
a hard reset; or
d)
a logical unit reset.
If possible, the device server shall perform a synchronize cache operation before ending the prevention of
medium removal.
If a persistent reservation or registration is being preempted by a PERSISTENT RESERVE OUT command
with PREEMPT AND ABORT service action (see SPC-6) or PERSISTENT RESERVE OUT command with
CLEAR service action (see SPC-6), then the equivalent of a PREVENT ALLOW MEDIUM REMOVAL
command with the PREVENT field set to 00b shall be processed for each I_T nexuses associated with the
persistent reservation or registrations being preempted allowing an application client to override the
Table 76 — PREVENT ALLOW MEDIUM REMOVAL command
Bit
Byte
OPERATION CODE (1Eh)
Reserved
Reserved
Reserved
Reserved
PREVENT
CONTROL
Table 77 — PREVENT field
Value
Description
00b
Medium removal is allowed.
01b
Medium removal shall be prevented.
10b to 11b
Obsolete
