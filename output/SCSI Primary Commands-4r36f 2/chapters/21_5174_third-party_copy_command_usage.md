# 5.17.4 Third-party copy command usage

Copy manager support for third-party copy commands is optional, but support for some third-party copy
commands and features may require support for other third-party copy commands as shown in table 108.
If a copy manager supports a third-party copy command in which the IMMED bit, if any, is allowed to be set to
one, then the copy manager shall support the COPY OPERATION ABORT command (see 6.3).
5.17.4 Third-party copy command usage
5.17.4.1 Prior to sending a third-party copy command
Before the copy manager is instructed to move transfer, the application client requesting the data transfers
shall take any necessary actions required to prepare the copy sources and copy destinations for the
third-party copy command (see 5.17.3). Such preparatory actions include but are not limited to:
a)
loading tapes;
b)
sending media changer commands;
c)
sending MODE SELECT commands, including MODE SELECT commands that:
A)
disable reporting of recovered errors by a block CSCD by setting the PER bit to zero in the Error
Recovery mode page (see SBC-3); and/or
B)
disable reporting of thin provisioning threshold events by a block CSCD by setting the TPERE bit to
zero in the Error Recovery mode page;
d)
sending reservation commands; and/or
Table 108 — Mandatory copy manager command support requirements
Supported command
Optional command
features supported
Copy manager support for the following
commands is mandatory
Held
data a
R_TOKEN
bit b
COPY OPERATION ABORT
n/a
n/a
RECEIVE COPY STATUS(LID4)
EXTENDED COPY(LID1)
n/a
n/a
RECEIVE OPERATING PARAMETERS
RECEIVE FAILURE DETAILS(LID1)
RECEIVE COPY STATUS(LID1)
EXTENDED COPY(LID1)
yes
n/a
RECEIVE COPY STATUS(LID1)
RECEIVE COPY DATA(LID1)
EXTENDED COPY(LID4)
n/a
n/a
RECEIVE COPY STATUS(LID4)
EXTENDED COPY(LID4)
yes
n/a
RECEIVE COPY DATA(LID4)
EXTENDED COPY(LID1) or
EXTENDED COPY(LID4)
n/a
yes
RECEIVE ROD TOKEN INFORMATION
POPULATE TOKEN
n/a
n/a
WRITE USING TOKEN
n/a
n/a
RECEIVE COPY STATUS(LID4)
RECEIVE ROD TOKEN INFORMATION
a Held data (see 5.17.4.5) refers to support for the ability to hold some or all of the data processed
by a copy operation for later transfer to the application client (e.g., support for the stream discard
+ application client segment descriptor (see 6.4.6.8)).
b R_TOKEN bit refers to support for the ability to create ROD tokens that are later returned to the
application client (i.e., support for the R_TOKEN bit being set to one in the ROD CSCD descriptor
(see 6.4.5.9)).


e)
sending tape positioning commands.
After all preparatory actions have been completed, the third-party copy command (e.g., the EXTENDED
COPY(LID4) command) should be sent to the copy manager to originate the copy operation (see 5.17.4.3).
5.17.4.2 List identifiers for third-party copy commands
A third-party copy command (see 5.17.3) may:
a)
take a long time to complete;
b)
have substantial command-specific data to return upon the completion of processing (e.g., held data
(see 5.17.4.4)); and
c)
be processed as a background operation in response to an IMMED bit being set to one (see 5.17.4.3).
List identifiers allow an application client to specify the copy operation (see 5.17.4.3) for which a monitoring or
management function is to be performed, as follows:
1)
the application client specifies the list identifier by which a third-party copy operation is to be identified
in the command or parameter list that originates the copy operation; and
2)
the application client specifies the same list identifier in any command that monitors or manages the
copy operation:
A)
starting from the time the copy operation is originated; and
B)
continuing until:
a)
all data associated with the copy operation has been delivered to the application client; or
b)
the application client specifies that the associated data is to be discarded.
List identifiers are specified in a LIST IDENTIFIER field whose location depends on the third-party command
being processed.
Unless otherwise specified, the LIST IDENTIFIER field contains a value that uniquely identifies a copy operation
among all those being processed that were received on a specific I_T nexus. If the copy manager detects a
duplicate list identifier value, then the originating third-party copy command (see table 107 in 5.17.3) shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to OPERATION IN PROGRESS.
The following LIST IDENTIFIER field formats are defined by this standard:
a)
an eight-bit LIST IDENTIFIER field (e.g., the RECEIVE COPY STATUS(LID1) command (see 6.24)); and
b)
a 32-bit LIST IDENTIFIER field (e.g., the RECEIVE COPY DATA(LID4) command (see 6.20)).
If a copy manager supports any third-party copy commands (see 5.17.3) that contain a 32-bit LIST IDENTIFIER
field, then the copy manager shall treat all list identifiers as 32-bit quantities, regardless of the field size used
to specify the list identifier (e.g., a list identifier of 000000FDh shall specify the same copy operation whether it
is present as FDh in an 8 bit field or as 000000FDh in a 32-bit field).
The results of specifying a list identifier from a third-party copy command that originates a copy operation (see
table 107 in 5.17.3) using 32-bit list identifier values in a third-party copy command that retrieves copy
operation data using an 8-bit list identifier are unpredictable.
5.17.4.3 Third-party copy commands and operations
Third-party copy commands that originate copy operations (see table 107 in 5.17.3) may support the IMMED bit
to allow the application client to specify that the processing of a copy operation continue after the processing
of the originating command has been completed.


If a third-party copy command supports an IMMED bit and that IMMED bit is set to one, the copy manager:
1)
shall return CHECK CONDTION status if any errors are detected in the CDB;
2)
shall transfer all of the parameter list, if any, to the copy manager;
3)
may validate the parameter list and return CHECK CONDITION status if errors are detected;
4)
shall complete the command with GOOD status; and
5)
shall complete processing of all specified copy operations as a background operation (see SAM-5).
A third-party copy command definition may place additional restrictions on the use of the IMMED bit.
If the IMMED bit is not supported by a command, then the copy manager shall process that command as if the
IMMED bit were set to zero.
If the IMMED bit, if any, is set to:
a)
zero, then the copy manager shall not complete processing of the third-party copy command until the
copy manager has completed processing of the copy operation originated by the command (i.e., the
copy manager processes the copy operation in the foreground); or
b)
one, then the copy manager may complete processing of the third-party copy command that origi-
nated the copy operation before completing the copy operation (i.e., the copy manager processes the
copy operation in the background). Copy operations that are processed in the background shall not
generate deferred errors (see SAM-5) for the errors encountered, if any, during this processing.
Instead, the error information (e.g., status, sense key, additional sense code) shall be made available
to the application client through use of one of the commands described in 5.17.4.4.
5.17.4.4 Monitoring progress of and retrieving results from third-party copy commands
The RECEIVE COPY STATUS(LID4) command (see 6.24) returns information about the current processing
status of the copy operation (see 5.17.4.3) specified by the list identifier (see 5.17.4.2). The parameter data for
the following commands contain the parameter data for the RECEIVE COPY STATUS(LID4) command as a
header (i.e., the shared third-party copy status header):
a)
RECEIVE COPY DATA(LID4) (see 6.24); and
b)
RECEIVE ROD TOKEN INFORMATION (see 6.26).
In the parameter data for all the commands with the shared third-party copy status header, the contents of the
COPY OPERATION STATUS field (see table 249 in 6.24) indicate the current processing status of the specified
copy operation. Unless otherwise specified, the contents of the COPY OPERATION STATUS field are not affected
by whether the copy operation is being or was performed in the foreground or background.
Although the information provided is not as complete, the following commands allow the monitoring of
progress and retrieval of results for certain copy operations in a way that is compatible with SPC-3 but do not
return the shared third-party copy status header:
a)
RECEIVE COPY STATUS(LID1) (see 6.25);
b)
RECEIVE COPY DATA(LID1) (see 6.21); and
c)
RECEIVE COPY FAILURE DETAILS(LID1) (see 6.23).
5.17.4.5 Held data
A copy operation may hold some or all of the data it processes for retrieval by the application client (e.g., the
processing defined for the EXTENDED COPY command streamstream +application client segment
descriptor (see 6.4.6.5)). Held data is retrieved using the RECEIVE COPY DATA(LID4) command (see 6.20)
or the RECEIVE COPY DATA(LID1) command (see 6.21).


If a copy manager supports any third-party copy commands (see 5.17.3) or an EXTENDED COPY command
copy function (see 6.4.6) capable of holding data for retrieval by the application client, then the copy manager:
a)
shall support the RECEIVE COPY DATA(LID4), if any third-party copy commands are supported that
originate copy operations (see table 107 in 5.17.3) with 32 bit list identifiers (see 5.17.4.2);
b)
shall support the RECEIVE COPY DATA(LID1), if any third-party copy commands are supported that
originate copy operations with 8 bit list identifiers;
c)
shall support either the Third-party Copy VPD page Held Data descriptor (see 7.8.17.12) or the
RECEIVE COPY OPERATING PARAMETERS command (see 6.22); and
d)
should support the Third-party Copy VPD page Held Data descriptor.
After the completion of a third-party copy command that originates a copy operation (see table 107 in 5.17.3),
the copy manager shall preserve all held data for a vendor specific period of time. The application client
should retrieve the held data (e.g., by sending a third-party copy command that retrieves the results of a previ-
ously originated copy operation (see table 107 in 5.17.3)) as soon as possible after the completion of the copy
operation to ensure that the data is not discarded by the copy manager. The copy manager shall discard the
held data:
a)
after all the held data for a specific copy operation has been successfully transferred to the application
client;
b)
if a RECEIVE COPY DATA(LID4) command (see 6.20) or a RECEIVE COPY DATA(LID1) command
(see 6.21) has been received on the same I_T nexus with a matching list identifier (see 5.17.4.2), with
the ALLOCATION LENGTH field set to zero;
c)
if another third-party copy command that originates a copy operation is received on the same I_T
nexus and the list identifier matches the list identifier associated with the held data;
d)
if the copy manager detects a logical unit reset condition or I_T nexus loss condition (see SAM-5); or
e)
if the copy manager requires the resources used to preserve the data.
The copy manager indicates the minimum amount of held data it supports in the HELD DATA LIMIT field that is
returned in the:
a)
Held Data descriptor (see 7.8.17.12) in the Third-party Copy VPD page (see 7.8.17); or
b)
parameter data for a RECEIVE COPY OPERATING PARAMETERS command (see 6.22).
The HELD DATA LIMIT field indicates the length, in bytes, of the minimum amount of data the copy manager
shall hold for return to the application client. If the processing of a copy operation requires more data to be
held, the copy manager may discard some of the held data in a vendor specific manner that retains the held
bytes from the most recently processed portion of the copy operation. The discarding of held data bytes shall
not be considered an error.
The held data discarded (HDD) bit indicates whether held data has been discarded for the copy operation
specified by a list identifier (see 5.17.4.2). If the HDD bit is set to one, held data has been discarded. If the HDD
bit is set to zero, held data has not been discarded. The HDD bit is returned in the parameter data for the:
a)
RECEIVE COPY DATA(LID4) command (see 6.20); and
b)
RECEIVE COPY STATUS(LID1) command (see 6.25).


5.17.4.6 Aborting third-party copy commands and copy operations
A task manager shall ensure that all commands and data transfers generated by a third-party copy operation
have been terminated and are no longer transferring data before allowing the completion of the task
management function or command (e.g., the PERSISTENT RESERVE OUT command with PREEMPT AND
ABORT service action) if one of the following causes the termination of the third-party copy command:
a)
an ABORT TASK task management function (see SAM-5);
b)
an ABORT TASK SET task management function (see SAM-5);
c)
a CLEAR TASK SET task management function (see SAM-5); or
d)
a PERSISTENT RESERVE OUT command with PREEMPT AND ABORT service action (see
5.13.11.2.6).
5.17.4.7 The COPY OPERATION ABORT command
Aborting a copy operation is not always possible with a task management function (e.g., a copy operation (see
5.17.4.3) that was originated by a third-party copy command with the IMMED bit set to one). The COPY
OPERATION ABORT command (see 6.3) provides an abort capability that is equivalent to an ABORT TASK
task management function for any copy operation that is able to be specified with a list identifier (see 5.17.4.2)
without regard for whether the copy operation is being performed in the foreground or background (see
5.17.4.3).
If the copy operation specified by a COPY OPERATION ABORT command was originated by a third-party
copy command (see table 107 in 5.17.3) with:
a)
the IMMED bit, if any, set to one, then the copy manager shall ensure that all commands and data
transfers generated by that copy operation have been terminated and are no longer transferring data
before completing the COPY OPERATION ABORT command; or
b)
no IMMED bit defined or with the IMMED bit set to zero, then the copy manager shall ensure that all
commands and data transfers generated by that copy operation have been terminated and are no
longer transferring data before terminating the originating third-party copy command with the sense
key set to COPY ABORTED and the additional sense code set to COMMAND CLEARED BY DEVICE
SERVER.
5.17.5 Responses to the conditions that result from SCSI events
The effects on copy operations that are produced by the conditions that result from SCSI events (see SAM-5)
are shown in table 109.
Table 109 — Responses to the conditions that result from SCSI events
Condition that results from a SCSI event
Effects of condition on copy operations
Power on
Hard reset
Logical unit reset
Power loss expected
All foreground and background copy operations shall be
aborted as if a COPY OPERATION ABORT command
(see 6.3) has been received for each copy operation.
I_T nexus loss
None
