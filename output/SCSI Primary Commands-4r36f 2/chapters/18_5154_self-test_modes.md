# 5.15.4 Self-test modes

5.15.4 Self-test modes
5.15.4.1 Self-test modes overview
A foreground mode (see 5.15.4.2) and a background mode (see 5.15.4.3) are defined for the short self-test
and the extended self-test. An application client specifies the self-test mode by the value in the SELF-TEST
CODE field in the SEND DIAGNOSTIC command (see 6.42).
5.15.4.2 Foreground mode
If an application client specifies a self-test to be performed in the foreground mode, the device server shall
return status for the command after the self-test has been completed.
While a SCSI target device is performing a self-test in the foreground mode, the device server shall terminate
all commands received while the self-test is in progress, except INQUIRY, REPORT LUNS, and REQUEST
SENSE, with CHECK CONDITION status, with the sense key set to NOT READY, and the additional sense
code set to LOGICAL UNIT NOT READY, SELF-TEST IN PROGRESS. If the device server receives an
INQUIRY command, a REPORT LUNS command, or a REQUEST SENSE command while performing a
self-test in the foreground mode, then the device server shall process the command.
If a SCSI target device is performing a self-test in the foreground mode and an error occurs during the test,
then:
a)
the SCSI target device shall abort the self-test; and
b)
the device server shall update the Self-Test Results log page (see 7.3.16):
A)
if the device server is able to update the Self-Test Results log page, then the device server shall
terminate the SEND DIAGNOSTIC command with CHECK CONDITION status, with the sense
key set to HARDWARE ERROR, and the additional sense code set to LOGICAL UNIT FAILED
SELF-TEST. The application client may obtain additional information about the failure by reading
the Self-Test Results log page; or
B)
if the device server is unable to update the Self-Test Results log page, then the device server
shall terminate the SEND DIAGNOSTIC command with CHECK CONDITION status, with the
sense key set to HARDWARE ERROR, and the additional sense code set to LOGICAL UNIT
UNABLE TO UPDATE SELF-TEST LOG.
An application client may cause a SCSI target device to abort a self-test that is being performed in the
foreground mode by using a task management function (see SAM-5) (e.g., an ABORT TASK task
management function, a CLEAR TASK SET task management function) or a transport specific reset (e.g., a
hard reset event) (see SAM-5). In addition, a self-test being performed in the foreground mode shall be termi-
nated by an I_T nexus loss event or a power loss expected event (see SAM-5). If a SCSI target device aborts
a self-test that is being performed in the foreground mode based on the SCSI target device receiving a task
management function or a transport specific event, then the device server shall update the Self-Test Results
log page (see 7.3.16).
5.15.4.3 Background mode
If a device server receives a SEND DIAGNOSTIC command specifying a self-test to be performed in the
background mode, then:
a)
the device server shall terminate the command if the CDB is invalid; or
b)
the device server shall:
1)
complete the command with GOOD status;
2)
initialize the next self-test results log parameter in the Self-Test Results log page (see 7.3.16) by
setting:


a)
the SELF-TEST CODE field to the self-test code from the SEND DIAGNOSTIC command; and
b)
the SELF-TEST RESULTS field to Fh;
and
3)
begin the self-test.
An application client may request that a device server abort a self-test that is being performed in the
background mode by sending a SEND DIAGNOSTIC command with the SELF-TEST CODE field set to 100b (i.e.,
abort background self-test function). A SCSI target device shall not abort a self-test being performed in the
background mode as the result of an I_T nexus loss event (see SAM-5). A SCSI target device shall abort a
self-test being performed in the background mode as the result of a power loss expected event (see SAM-5).
While the SCSI target device is performing a self-test in the background mode, the device server shall
terminate with CHECK CONDITION status any received SEND DIAGNOSTIC command that meets any of the
following criteria:
a)
the SELFTEST bit is set to one; or
b)
the SELF-TEST CODE field is set to a value other than 000b or 100b.
When terminating a received SEND DIAGNOSTIC command that meets the criteria described in this
subclause, the device server shall set the sense key to NOT READY and the additional sense code to
LOGICAL UNIT NOT READY, SELF-TEST IN PROGRESS.
If the SCSI target device is performing a self-test in the background mode, and the device server receives any
command that requires suspension of the self-test to process, except those listed in table 105, then:
a)
the logical unit shall suspend the self-test;
b)
the device server shall begin processing the command within two seconds after the CDB has been
validated; and
c)
after the command completes, the logical unit shall resume the self-test.
If the device server receives one of the commands listed in table 105, then the device server shall:
a)
abort the self-test;
b)
update the self-test log; and


c)
begin processing the command within two seconds after the CDB has been validated.
5.15.4.4 Features common to foreground and background self-test modes
An application client may use a REQUEST SENSE command (see 6.39) to poll for progress indication at any
time during a self-test. In response to the REQUEST sense command, the device server returns parameter
data containing sense data with the sense key set to NOT READY, the additional sense code set to LOGICAL
UNIT NOT READY, SELF-TEST IN PROGRESS, and the PROGRESS INDICATION field set to indicate the
progress of the self-test.
An application client may use the EBACKERR bit and the MRIE field in the Informational Exceptions Control
mode page (see applicable command standard) to control the reporting of errors that occur during a
background self-test operation.
An application client may obtain information about the 20 most recent self-tests, including the self-test in
progress, if any, by reading the Self-Test Results log page (see 7.3.16). With the exception of progress
indication, this is the only method for an application client to obtain information about self-tests performed in
the background mode unless an error occurs during the self-test.
Table 106 summarizes:
a)
when a device server returns status after receipt of a self-test command;
b)
how an application client may abort a self-test;
c)
how a device server processes commands that are entered into the task set while a self-test is in
progress; and
Table 105 — Exception commands for background self-tests
Device type
Command
Reference
All device types
SEND DIAGNOSTIC (with SELF-TEST CODE field set to 100b)
WRITE BUFFER (with the mode set to any download microcode option)
6.42
6.49
Direct access
block
FORMAT UNIT
START STOP UNIT
SBC-3
Sequential
access
ERASE
FORMAT MEDIUM
LOAD UNLOAD
LOCATE
READ
READ POSITION
READ REVERSE
REWIND
SPACE
VERIFY
WRITE
WRITE BUFFER
WRITE FILEMARKS
SSC-3
Media changer
EXCHANGE MEDIUM
INITIALIZE ELEMENT STATUS
MOVE MEDIUM
POSITION TO ELEMENT
READ ELEMENT STATUS (if CURDATA=0 and device motion is required)
WRITE BUFFER
SMC-3
Object-based
storage
Any command with operation code 7Fh (i.e., all commands defined by
the OSD standard)
OSD
NOTE Device types not listed in this table do not have commands that are exceptions for background
self-tests, other than those listed above for all device types.


d)
how a self-test failure is reported.
5.16 Target port group asymmetric access states
5.16.1 Target port group access overview
Logical units may be connected to one or more service delivery subsystems via multiple target ports (see
SAM-5). The access to logical units through the multiple target ports may be symmetrical (see 5.16.3) or
asymmetrical (see 5.16.2).
Table 106 — Self-test mode summary
Self-
test
mode
When
status is
returned
How to abort
the self-test
Processing of
commands while a
self-test is in progress
Self-test failure reporting
Fore-
ground
After the
self-test
is com-
plete
A task
management
function or
reset event
that causes a
self-test to be
aborted (see
5.15.4.2)
If the command is
INQUIRY, REPORT LUNS
or REQUEST SENSE,
then process normally,
otherwise, terminate with
CHECK CONDITION sta-
tus, with the sense key set
to NOT READY, and the
additional sense code set
to LOGICAL UNIT NOT
READY, SELF-TEST IN
PROGRESS.
The device server terminates the
SEND DIAGNOSTIC command with
CHECK CONDITION status, with the
sense key set to HARDWARE
ERROR, and the additional sense
code set to LOGICAL UNIT FAILED
SELF-TEST or LOGICAL UNIT
UNABLE TO UPDATE SELF-TEST
LOG (see 5.15.4.2). a
Back-
ground
After the
CDB is
validated
A SEND
DIAG-
NOSTIC
command
with the
SELF-TEST
CODE field set
to 100b
Process the command,
except as described in
5.15.4.3.
An application client:
a)
checks the Self-Test Results
log page (see 7.3.16) after the
PROGRESS INDICATION field
returned in response to a
REQUEST SENSE command
indicates that the self-test is
complete; or
b)
uses the EBACKERR bit and the
MRIE field (see applicable
command standard) to specify
a method of indicating that a
failure occurred. If a failure
occurs, then an additional
sense code of WARNING -
BACKGROUND SELF-TEST
FAILED shall be returned using
the method defined in the MRIE
field.
a The device server shall not report an error until after the Self-Test Results log page is updated.
