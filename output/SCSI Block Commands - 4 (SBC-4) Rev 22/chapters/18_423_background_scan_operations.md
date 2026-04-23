# 4.23 Background scan operations

offset
the offset in bytes of the IO advice hints group descriptor from the beginning
of the IO Advice Hints Grouping mode page
If the GROUP_SUP bit in the Extended INQUIRY Data VPD page is set to one, then for all commands that
contain a GROUP NUMBER field, the GROUP NUMBER field specifies:
a)
the IO advice hints group number that the device server shall use to associate IO advice hints with all
operations associated with that command; and
b)
the cache ID (see 4.15.2) that the device server shall use for all operations associated with that
command.
In the IO advice hints group descriptor for the specified group number in the IO Advice Hints Grouping mode
page, if the IO ADVICE HINTS MODE field (see table 244) is set to:
a)
00b, then the device server shall use the IO advice hints in the IO advice hints group descriptor
specified by the IO advice hints group number to associate IO advice hints (see 4.30); and
b)
01b, then the device server may associate vendor specific IO advice hints,
with each operation associated with the command.
If the CS_ENABLE bit is set to one in the IO advice hints group descriptor in the IO Advice Hints Grouping mode
page, then the device server should use the cache segments associated with the specified cache ID.
If the IC_ENABLE bit is set to one in the IO advice hints group descriptor in the IO Advice Hints Grouping mode
page, then the device server shall perform the information collection function as described in 4.22.1.
Device servers that support the IO Advice Hints Grouping mode page shall support group 0 to group 63.
4.23 Background scan operations
4.23.1 Background scan overview
A background scan operation is either a background pre-scan operation (see 4.23.2) or a background
medium scan operation (see 4.23.3).
During a background scan operation, the device server performs read medium operations for the purpose of:
a)
identifying logical blocks that are difficult to read (i.e., recoverable) or unreadable (i.e.,
unrecoverable);
b)
logging problems encountered during the background scan operation; and
c)
when allowed, taking a vendor specific action to repair recoverable logical blocks or perform
automatic read reallocation of recoverable logical blocks.
During a background scan operation, if a read medium operation encounters a recovered error (i.e., a logical
block is readable but requires extra actions (e.g., retries or application of a correction algorithm) to be read),
then the device server may resolve the problem using vendor specific means. The value of the ARRE bit
(see 6.5.10) determines whether or not the device server performs automatic read reassignment.
During a background scan operation, if a read medium operation encounters an unrecovered error (i.e., a
logical block is unreadable), then the device server may mark the logical block unrecoverable. The value of
the AWRE bit (see 6.5.10) determines whether or not the device server performs automatic write reassignment.
If  the AWRE bit is set to one, then the device server performs automatic write reassignment at the start of the
next write medium operation accessing that logical block.
During a background scan operation, the device server:
a)
may scan the logical blocks in any order (e.g., based on physical block layout);
b)
should not retain any data from logical blocks in cache memory after the logical blocks are read;
c)
shall ignore pseudo unrecovered errors with correction disabled (see 4.18.2); and
d)
shall process pseudo unrecovered errors with correction enabled.


4.23.2 Background pre-scan operations
4.23.2.1 Enabling background pre-scan operations
A background pre-scan operation is enabled after:
1)
the EN_PS bit (see 6.5.4) is set to zero:
2)
the EN_PS bit is set to one; and
3)
the SCSI device is power cycled if;
A) the S_L_FULL bit (see 6.5.4)is:
a)
set to zero; or
b)
set to one and the Background Scan log parameters (see 6.4.2) are not all used;
and
B) the saved value of the EN_PS bit is set to one.
After a background pre-scan operation is enabled, the device server shall:
a)
initialize the Background Pre-scan Time Limit timer to the time specified in the BACKGROUND PRE-SCAN
TIME LIMIT field  (see 6.5.4) and start the timer;
b)
initialize the Background Medium Scan Interval timer to the time specified in the BACKGROUND MEDIUM
SCAN INTERVAL TIME field  (see 6.5.4) and start the timer; and
c)
begin the background pre-scan operation (i.e., begin scanning the medium).
4.23.2.2 Suspending and resuming background pre-scan operations
A background pre-scan operation shall be suspended when any of the following occurs:
a)
a command or task management function is processed that requires the background pre-scan
operation to be suspended;
b)
a SCSI event (e.g., a hard reset) (see SAM-6) is processed that requires the background pre-scan
operation to be suspended;
c)
a power condition timer expires (see the Power Condition mode page in SPC-6), and the
PM_BG_PRECEDENCE field in the Power Condition mode page is set to 10b; or
d)
the S_L_FULL bit (see 6.5.4) is set to one, and the Background Scan log parameters (see 6.4.2) are all
used.
If a command is received that requires a background pre-scan operation to be suspended, then the following
should occur within the time specified in the MAXIMUM TIME TO SUSPEND BACKGROUND SCAN field (see 6.5.4):
a)
the logical unit suspends the background medium scan operation; and
b)
the device server begins processing the command.
If a background pre-scan operation is suspended, then the device server shall not stop:
a)
the Background Pre-scan Time Limit timer;
b)
the Background Medium Scan Interval timer; and
c)
any process that results in an event that causes a background function to occur (e.g., not stop any
timers or counters associated with background functions).
While a background pre-scan operation is suspended and not halted (see 4.23.3.2), the device server shall
convert each write operation accessing a logical block that has not been scanned during the background
pre-scan operation into a write medium operation followed by a verify medium operation in order to verify that
the logical block data just written was read back without error. If a write medium operation accesses a logical
block that has already been scanned during the background pre-scan operation, then the device server shall
not perform the additional verify medium operation.
A background pre-scan operation shall be resumed from where the operation was suspended when:
a)
there are no commands in any task set to be processed;
b)
there are no task management functions to be processed;
c)
there are no SCSI events to be processed;


d)
no ACA condition exists;
e)
the PM_BG_PRECEDENCE field in the Power Condition mode page is set to 10b (see SPC-6), but no
power condition timer defined in the Power Condition mode page has expired;
f)
the S_L_FULL bit is set to zero (see 6.5.4), or the Background Medium Scan log parameters
(see 6.4.2)are not all used;
g)
the logical unit has been idle for the time specified in the MINIMUM IDLE TIME BEFORE BACKGROUND SCAN
field  (see 6.5.4); and
h)
the background pre-scan operation has not been halted (see 4.23.3.2).
4.23.2.3 Halting background pre-scan operations
The device server shall halt a background pre-scan operation if any of the following occurs:
a)
the background pre-scan operation completes scanning all logical blocks on the medium;
b)
an application client sets the EN_PS bit to zero in the Background Control mode page (see 6.5.4);
c)
the Background Pre-scan Time Limit timer expires;
d)
the device server detects a fatal error;
e)
the device server detects a vendor specific pattern of errors;
f)
the device server detects a medium formatted without a PLIST (see 4.13); or
g)
the device server detects temperature out of range.
After a background pre-scan operation has been halted, the device server shall not enable a background
operation until the conditions in 4.23.2.1 are met.
4.23.3 Background medium scan
4.23.3.1 Enabling background medium scan operations
Background medium scan operations are enabled if:
a)
a background pre-scan operation (see 4.23.2) is not in progress;
b)
the S_L_FULL bit (see 6.5.4) is:
A) set to zero; or
B) set to one and the Background Scan log parameters (see 6.4.2) are not all used;
and
c)
the EN_BMS bit (see 6.5.4)is set to one.
If background medium scan operations are enabled, then the device server shall begin a background medium
scan operation (i.e., begin scanning the medium) when:
a)
the Background Medium Scan Interval timer has expired; and
b)
the logical unit has been idle for the time specified in the MINIMUM IDLE TIME BEFORE BACKGROUND SCAN
field (see 6.5.4).
After power on, if background pre-scan operations are not enabled (see 4.23.2.1), then the device server shall
set the Background Medium Scan Interval timer to zero (i.e., expired).
Whenever a background medium scan operation begins, the device server shall set the Background Medium
Scan Interval timer to the time specified in the BACKGROUND MEDIUM SCAN INTERVAL TIME field  (see 6.5.4) and
start the timer.
4.23.3.2 Suspending and resuming background medium scan operations
The logical unit shall suspend a background medium scan operation if any of the following occurs:
a)
a command or task management function is processed that requires the background medium scan
operation to be suspended;
b)
a SCSI event (e.g., a hard reset) (see SAM-6) is processed that requires the background medium
scan operation to be suspended;


c)
a power condition timer expires (see the Power Condition mode page in SPC-6), and the
PM_BG_PRECEDENCE field in the Power Condition mode page is set to 10b;
d)
the S_L_FULL bit (see 6.5.4) is set to one, and the Background Scan log parameters (see 6.4.2) are all
used; or
e)
an application client sets the EN_BMS bit to zero (see 6.5.4).
If a command is received that requires a background medium scan operation to be suspended, then the
following should occur within the time specified in the MAXIMUM TIME TO SUSPEND BACKGROUND SCAN field
(see 6.5.4):
a)
the logical unit suspends the background medium scan operation; and
b)
and the device server begins processing the command.
If a background pre-scan operation is suspended, then the device server shall not stop:
a)
the Background Medium Scan Interval timer; and
b)
any process that results in an event that causes a background function to occur (e.g., not stop any
timers or counters associated with background functions).
The logical unit shall resume a suspended background medium scan operation from where the operation was
suspended when:
a)
there are no commands in any task set to be processed;
b)
there are no task management functions to be processed;
c)
there are no SCSI events to be processed;
d)
the PM_BG_PRECEDENCE field in the Power Condition mode page is set to 10b (see SPC-6), but no
power condition timer defined in the Power Condition mode page has expired;
e)
the S_L_FULL bit (see 6.5.4)is set to zero , or the Background Medium Scan log parameters in the
Background Scan Results log page are not all used;
f)
the EN_BMS (see 6.5.4)is set to one; and
g)
the logical unit has been idle for the time specified in the MINIMUM IDLE TIME BEFORE BACKGROUND SCAN
field (see 6.5.4).
4.23.3.3 Halting background medium scan operations
The device server shall halt background medium scan operations if any of the following occurs:
a)
the background medium scan operation completes scanning all logical blocks on the medium;
b)
the device server detects a fatal error;
c)
the device server detects a vendor specific pattern of errors;
d)
the device server detects a medium formatted without a PLIST (see 4.13); or
e)
the device server detects temperature out of range.
After background medium scan operations have been halted, the device server shall  not enable a
background medium scan operation until the conditions in 4.23.3.1 are met.
4.23.4 Interpreting the logged background scan results
An application client may:
a)
poll the Background Scan Results log page (see 6.4.2) to get information about background pre-scan
and background medium scan activity; or
b)
use the EBACKERR bit and the MRIE field (see 6.5.8) to select a method of indicating that a medium
error was detected.
If the EBACKERR bit is set to one and a medium error was detected, then the device server shall return the
following additional sense codes using the method defined by the value in the MRIE field:
a)
WARNING - BACKGROUND PRE-SCAN DETECTED MEDIUM ERROR, if the failure occurs during
a background pre-scan operation; or
b)
WARNING - BACKGROUND MEDIUM SCAN DETECTED MEDIUM ERROR, if the failure occurs
during a background medium scan operation.


The Background Scan Status log parameter (see 6.4.2.2) in the Background Scan Results log page
(see 6.4.2) indicates:
a)
whether or not a background scan operation is active or halted;
b)
the number of background scan operations that have been performed on the medium; and
c)
the progress of a background scan operation, if active.
This information may be used by an application client to monitor the background scan operations and should
be used by an application client after notification via an informational exception (see 6.5.8).
The Background Scan Results log parameters (see 6.4.2.3), if any, in the Background Scan Results log page
describe the LBA and the reassignment status of each logical block that generated recovered errors or
unrecovered errors during the background scan’s read medium operations.
After an application client analyzes the Background Scan Results log parameters and has completed actions,
if any, to repair any of the indicated LBAs, the application client may delete all Background Scan Results log
parameters by issuing a LOG SELECT command (e.g., with the PCR bit set to one in the CDB or with the PC
field set to 11b and the PARAMETER LIST LENGTH field set to zero in the CDB) (see SPC-6).
A background medium scan operation may continue to run during log page accesses. To ensure that the
values in the Background Scan Results log page do not change during a sequence of accesses, the
application client:
1)
sets the EN_BMS bit to zero in the Background Control mode page in order to suspend the background
medium scan operation;
2)
reads the Background Scan Results log page with a LOG SENSE command;
3)
processes the Background Scan Results log page;
4)
deletes the Background Scan Results log page entries with the LOG SELECT command (e.g., with
the PCR bit set to one in the CDB); and
5)
sets the EN_BMS bit to one in the Background Control mode page in order to re-enable the background
scan operation.
4.24 Deferred microcode activation
After receiving a FORMAT UNIT command (see 5.4) or a START STOP UNIT command (see 5.31), a device
server shall, prior to processing the command, activate any deferred microcode that has been downloaded as
a result of a WRITE BUFFER command with the MODE field set to 0Eh (see SPC-6).
