# 4.11 Sanitize operations

Any time the READ CAPACITY (10) parameter data (see 5.20.2) or the READ CAPACITY (16) parameter
data (see 5.21.2) changes (e.g., when a FORMAT UNIT command or a MODE SELECT command causes a
change to the logical block length or protection information, or when a vendor specific mechanism causes a
change), then the device server shall establish a unit attention condition for the SCSI initiator port (see
SAM-6) associated with each I_T nexus, except the I_T nexus on which the command causing the change
was received with the additional sense code set to CAPACITY DATA HAS CHANGED.
NOTE 3 - Logical units compliant with SBC were not required to establish a unit attention condition with the
additional sense code set to CAPACITY DATA HAS CHANGED.
4.11 Sanitize operations
4.11.1 Sanitize operations overview
A sanitize operation causes the device server to:
a)
affect the information on the logical unit’s medium such that recovery of logical block data from the
medium is not possible;
b)
affect the information in the cache by a method that is not defined by this standard such that
previously existing data in cache is unable to be accessed; and
c)
prevent future access by an application client to cache or medium where the device server is unable
to alter the information.
One of the following sanitize operations may be requested on the logical unit’s medium:
a)
a sanitize overwrite operation that causes the device server to alter information by writing a data
pattern to the medium one or more times;
b)
a sanitize block erase operation that causes the device server to alter information by setting the
physical blocks to a vendor specific value; or
c)
a sanitize cryptographic erase operation that causes the device server to change encryption keys to
prevent correct decryption of previously stored information, which may cause protection information, if
any, to be indeterminate.
For zoned block devices:
a)
the ZNR bit (see 5.30) requests specific processing for each write pointer zone (see ZBC-2) upon
successful completion of a sanitize operation (see 4.11.4); and
b)
ZBC-2 describes additional requirements to the way in which sanitize operations are performed and
completed (i.e., extensions to the descriptions in 4.11.3).
An application client may request that a sanitize operation be performed in the restricted completion mode or
the unrestricted completion mode (see 4.11.4) using the AUSE bit (see 5.30).
In the unrestricted completion mode, a SANITIZE command with the EXIT FAILURE MODE service action
exits a failed sanitize operation.
In the restricted completion mode, the only method to exit a failed sanitize operation is  for a SANITIZE
command to request another sanitize operation and for that operation to complete without error. If a sanitize
operation in the restricted completion mode completes with an error, and a subsequent SANITIZE command
requests the unrestricted completion mode (i.e., the AUSE bit set to one), then the device server shall
terminate that SANITIZE command as described in 5.30.1.
All sanitize operations shall be performed on:
a)
the medium that is being used to store logical block data;
b)
the medium that is not being used to store logical block data (e.g., areas previously used to store
logical block data, areas available for allocation, and physical blocks that have become inaccessible);
and
c)
all cache.


An application client requests that the device server perform a sanitize operation using the SANITIZE
command. While the medium is write protected (see 4.12) the device server shall terminate a SANITIZE
command with CHECK CONDITION status with the sense key set to DATA PROTECT and the appropriate
additional sense code for the condition.
4.11.2 Commands allowed during sanitize
Those of the following commands that the device server supports while not performing a sanitize operation
are allowed during sanitize:
a)
INQUIRY commands;
b)
LOG SENSE commands that specify the Temperature log page (see SPC-6);
c)
MODE SENSE commands (see SPC-6) that specify:
A) the Informational Exceptions Control mode page;
B) the Caching mode page;
C) the Control mode page;
D) the Protocol Specific Port mode page; or
E) the Protocol Specific Logical Unit mode page;
d)
READ CAPACITY (10) commands (see 5.20);
e)
READ CAPACITY (16) commands (see 5.21);
f)
REPORT LUNS commands (see SPC-6);
g)
REPORT SUPPORTED OPERATION CODES commands (see SPC-6);
h)
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS commands (see SPC-6);
i)
REPORT ZONES commands (see ZBC-2) with:
A) the ZONE START LBA field set to zero;
B) the REPORTING OPTIONS field set to 3Fh;
C) the PARTIAL bit set to one; and
D) the ALLOCATION LENGTH field set to a value less than or equal to 64;
and
j)
REQUEST SENSE commands.
4.11.3 Performing a sanitize operation
Before performing a sanitize operation, the device server shall:
a)
terminate all commands in all task sets except commands allowed during sanitize (see 4.11.2) with
CHECK CONDITION status with the sense key set to NOT READY, the additional sense code set to
LOGICAL UNIT NOT READY, SANITIZE IN PROGRESS, and the PROGRESS INDICATION field in the
sense data set to indicate that the sanitize operation is beginning;
b)
stop all enabled power condition timers (see SPC-6);
c)
stop all timers for enabled background scan operations (see 4.23);
d)
stop all timers or counters enabled for device specific background functions (see SPC-6);
e)
discard partially downloaded microcode, if any; and
f)
close open streams (see 4.32), if any.
While performing a sanitize operation, the device server shall:
a)
process commands allowed during sanitize (see 4.11.2) and terminate all other commands with
CHECK CONDITION status with the sense key set to NOT READY, the additional sense code set to
LOGICAL UNIT NOT READY, SANITIZE IN PROGRESS, and the PROGRESS INDICATION field in the
sense data set to indicate the progress of the sanitize operation;
b)
provide pollable sense data (see SPC-6) with the sense key set to NOT READY, the additional sense
code set to LOGICAL UNIT NOT READY, SANITIZE IN PROGRESS, and the PROGRESS INDICATION
field set to indicate the progress of the sanitize operation;
c)
suspend the sanitize operation while processing the following conditions (see SAM-6):
A) a power on;
B) a hard reset;
C) a logical unit reset; or


D) a power loss expected;
d)
not suspend the sanitize operation while processing an I_T nexus loss;
e)
resume performing the sanitize operation after processing:
A) a logical unit reset; or
B) a power loss expected condition in which no power loss occurs within constraints defined by the
applicable SCSI transport protocol standard (e.g., power loss timeout in SPL-5);
f)
process task management functions without affecting the processing of the sanitize operation (e.g.,
an ABORT TASK task management function aborts the SANITIZE command and has no effect on
performing the sanitize operation);
g)
not alter mode data, INQUIRY data, or READ CAPACITY (16) parameter data (e.g., the number of
logical blocks, logical block length, or protection information settings for the logical unit); and
h)
identify inaccessible physical blocks and in a vendor specific manner prevent future access to these
blocks following a successful sanitize operation.
4.11.4 Completing a sanitize operation
If a sanitize operation completes without error, and logical block provisioning management (see 4.7.3) is
supported, then:
a)
the initial condition for every LBA should be anchored (see 4.7.3.2) or deallocated (see 4.7.3.3); and
b)
read operations and write operations should complete without error.
If a sanitize operation completes without error and logical block provisioning management is not supported,
then:
a)
read commands are processed as described in 5.30.2.2, 5.30.2.3, 5.30.2.4, and 5.30.2.5; and
b)
write operations should complete without error.
If a sanitize operation completes without error on a zoned block device, then the ZNR bit (see 5.30) requests
specific processing for each write pointer zone (see ZBC-2).
If the sanitize operation completes with an error in restricted completion mode, then the device server shall:
a)
terminate the SANITIZE command being performed, if any (e.g., the IMMED bit was set to zero in the
CDB, and the failure occurs before status is returned for the command), with CHECK CONDITION
status with the sense key set to MEDIUM ERROR and the additional sense code set to SANITIZE
COMMAND FAILED; and
b)
until completion of a successful sanitize operation has occurred, terminate all commands, except
SANITIZE commands allowed in the restricted completion mode and commands allowed during
sanitize (see 4.11.2) with CHECK CONDITION status with the sense key set to MEDIUM ERROR and
the additional sense code set to SANITIZE COMMAND FAILED.
If a sanitize operation completes with an error in unrestricted completion mode, then the device server shall:
a)
terminate the SANITIZE command being performed, if any (e.g., the IMMED bit was set to zero in the
CDB, and the failure occurs before status is returned for the command), with CHECK CONDITION
status with the sense key set to MEDIUM ERROR and the additional sense code set to SANITIZE
COMMAND FAILED; and
b)
until completion of a successful sanitize operation has occurred, terminate all commands, except
SANITIZE commands and commands allowed during sanitize (see 4.11.2) with CHECK CONDITION
status with the sense key set to MEDIUM ERROR and the additional sense code set to SANITIZE
COMMAND FAILED.
A sanitize operation that completed with error and was cleared with a SANITIZE command with the service
action of EXIT FAILURE MODE may have not performed a complete sanitize operation (e.g., this action may
enable the recovery of logical block data from the cache and medium for those logical blocks that were not
sanitized).
After the sanitize operation completes the device server shall:
1)
initialize all enabled timers and counters; and
2)
start all enabled timers and counters for power conditions and background functions.
