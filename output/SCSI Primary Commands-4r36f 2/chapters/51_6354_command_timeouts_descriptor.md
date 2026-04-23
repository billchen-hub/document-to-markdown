# 6.35.4 Command timeouts descriptor

6.35.4 Command timeouts descriptor
6.35.4.1 Overview
The command timeouts descriptor (see table 297) returns timeout information for commands supported by the
logical unit based on the time from the start of processing for the command to its reported completion.
Values returned in the command timeouts descriptor do not include times that are outside the control of the
device server (e.g., prior commands with the IMMED bit set to one in the CDB, concurrent commands from the
same or different I_T nexuses, manual unloads, power on self tests, prior aborted commands, commands that
force cache synchronization, delays in the service delivery subsystem).
For commands that cause a change in power condition (see 5.12), values returned in the command timeouts
descriptor do not include the power condition transition time (e.g., the time to spinup rotating media).
Values returned in the command timeouts descriptor should not be used to compare products.
The DESCRIPTOR LENGTH field indicates the number of bytes that follow in the command timeouts descriptor.
The contents of the DESCRIPTOR LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The COMMAND SPECIFIC field contains timeout information (see table 298) that is specific to one or more
commands. If no command specific timeout information is defined by this or the applicable command standard
the COMMAND SPECIFIC field is reserved.
A non-zero value in the NOMINAL COMMAND PROCESSING TIMEOUT field indicates the minimum amount of time in
seconds the application client should wait prior to querying for the progress of the command identified by the
parameter data that contains this command timeouts descriptor. A value of zero in the NOMINAL COMMAND
PROCESSING TIMEOUT field indicates that no timeout is indicated.
Table 297 — Command timeouts descriptor format
Bit
Byte
(MSB)
DESCRIPTOR LENGTH (000Ah)
(LSB)
Reserved
COMMAND SPECIFIC
(MSB)
NOMINAL COMMAND PROCESSING TIMEOUT

•••
(LSB)
(MSB)
RECOMMENDED COMMAND TIMEOUT

•••
(LSB)
Table 298 — Command timeouts descriptor COMMAND SPECIFIC field usage in this standard
Command
Reference
WRITE BUFFER
6.35.4.2


NOTE 41 - The value contained in the NOMINAL COMMAND PROCESSING TIMEOUT field may include time
required for typical device error recovery procedures expected to occur on a regular basis.
A non-zero value in the RECOMMENDED COMMAND TIMEOUT field specifies the recommended time in seconds
the application client should wait prior to timing out the command identified by the parameter data that
contains this command timeouts descriptor. A value of zero in the RECOMMENDED COMMAND TIMEOUT field
indicates that no time is indicated.
The device server should set the recommended command timeout to a value greater than or equal to the
nominal command processing timeout.
6.35.4.2 WRITE BUFFER command timeouts descriptor COMMAND SPECIFIC field usage
For the WRITE BUFFER command (see 6.49), the COMMAND SPECIFIC field usage is reserved for all modes
except the following:
a)
download microcode mode (04h);
b)
download microcode and save mode (05h);
c)
download microcode with offsets mode (06h);
d)
download microcode with offsets and save mode (07h);
e)
download microcode with offsets, select activation events, save, and defer activate mode (0Dh) only if
the microcode is activated by an event other than the activate deferred microcode mode;
f)
download microcode with offsets, save, and defer activate mode (0Eh) only if the microcode is
activated by an event other than an activate deferred microcode mode; and
g)
activate deferred microcode mode (0Fh).
If the command timeouts descriptor describes one of the WRITE BUFFER modes listed in this subclause,
then the COMMAND SPECIFIC field indicates the maximum time, in one second increments, that access to the
SCSI device is limited or not possible through any SCSI ports associated with a logical unit that processes a
WRITE BUFFER command that specifies one of the named modes. A value of zero in the COMMAND SPECIFIC
field indicates that no maximum time is indicated.


6.36 REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command
The REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command (see table 299) requests infor-
mation on task management functions (see SAM-5) the addressed logical unit supports. This command uses
the MAINTENANCE IN CDB format (see 4.2.2.3.3).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 299 for the REPORT
SUPPORTED TASK MANAGEMENT FUNCTIONS command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 299 for the REPORT
SUPPORTED TASK MANAGEMENT FUNCTIONS command.
A return extended parameter data (REPD) bit set to one specifies that the task management timeout infor-
mation shall be included in the parameter data that is returned. A REPD bit set to zero specifies that the task
management timeout information shall not be returned.
The ALLOCATION LENGTH field specifies the number of bytes that have been allocated for the returned
parameter data. The allocation length should be at least four. If the allocation length is less than four, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-5.
The format of the parameter data returned by the REPORT SUPPORTED TASK MANAGEMENT
FUNCTIONS command depends on the value of the REPD bit as follows:
a)
if the REPD bit is set to zero, the REPORT SUPPORTED TASK MANAGEMENT FUNCTION
parameter data returned is shown in table 300; and
b)
if the REPD bit is set to one, the REPORT SUPPORTED TASK MANAGEMENT FUNCTION
parameter data returned is shown in table 301.
Table 299 — REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (0Dh)
REPD
Reserved
Reserved
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB)
Reserved
CONTROL


The REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS basic parameter data format is shown in
table 300.
The REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS extended parameter data format is shown
in table 301.
An ABORT TASK supported (ATS) bit set to one indicates the ABORT TASK task management function (see
SAM-5) is supported by the logical unit. An ATS bit set to zero indicates the ABORT TASK task management
function is not supported.
An ABORT TASK SET supported (ATSS) bit set to one indicates the ABORT TASK SET task management
function (see SAM-5) is supported by the logical unit. An ATSS bit set to zero indicates the ABORT TASK SET
task management function is not supported.
A CLEAR ACA supported (CACAS) bit set to one indicates the CLEAR ACA task management function (see
SAM-5) is supported by the logical unit. A CACAS bit set to zero indicates the CLEAR ACA task management
function is not supported.
Table 300 — REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS basic parameter data
Bit
Byte
ATS
ATSS
CACAS
CTSS
LURS
QTS
Obsolete
Obsolete
Reserved
QAES
QTSS
ITNRS
Reserved
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS ADDITIONAL DATA LENGTH (00h)
Table 301 — REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS extended parameter data
Bit
Byte
ATS
ATSS
CACAS
CTSS
LURS
QTS
Obsolete
Obsolete
Reserved
QAES
QTSS
ITNRS
Reserved
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS ADDITIONAL DATA LENGTH (0Ch)
Reserved
TMFTMOV
Reserved
ATTS
ATSTS
CACATS
CTSTS
LURTS
QTTS
Reserved
Reserved
Reserved
QAETS
QTSTS
ITNRTS
(MSB)
TASK MANAGEMENT FUNCTIONS LONG TIMEOUT

•••
(LSB)
(MSB)
TASK MANAGEMENT FUNCTIONS SHORT TIMEOUT

•••
(LSB)


A CLEAR TASK SET supported (CTSS) bit set to one indicates the CLEAR TASK SET task management
function (see SAM-5) is supported by the logical unit. A CTSS bit set to zero indicates the CLEAR TASK SET
task management function is not supported.
A LOGICAL UNIT RESET supported (LURS) bit set to one indicates the LOGICAL UNIT RESET task
management function (see SAM-5) is supported by the logical unit. An LURS bit set to zero indicates the
LOGICAL UNIT RESET task management function is not supported.
A QUERY TASK supported (QTS) bit set to one indicates the QUERY TASK task management function (see
SAM-5) is supported by the logical unit. A QTS bit set to zero indicates the QUERY TASK task management
function is not supported.
A QUERY ASYNCHRONOUS EVENT supported (QAES) bit set to one indicates the QUERY
ASYNCHRONOUS EVENT task management function (see SAM-5) is supported by the logical unit. A QAES
bit set to zero indicates the QUERY ASYNCHRONOUS EVENT task management function is not supported.
A QUERY TASK SET supported (QTSS) bit set to one indicates the QUERY TASK SET task management
function (see SAM-5) is supported by the logical unit. A QTSS bit set to zero indicates the QUERY TASK SET
task management function is not supported.
An I_T NEXUS RESET supported (ITNRS) bit set to one indicates the I_T NEXUS RESET task management
function (see SAM-5) is supported by the logical unit. An ITNRS bit set to zero indicates the I_T NEXUS
RESET task management function is not supported.
The REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS ADDITIONAL DATA LENGTH field indicates the number of
bytes that follow in the parameter data. The contents of the REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS
ADDITIONAL DATA LENGTH field are not altered based on the allocation length (see 4.2.5.6).
A task management function timeouts valid (TMFTMOV) bit set to one indicates the contents of the TASK
MANAGEMENT FUNCTIONS SHORT TIMEOUT field and TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field are valid.
A TMFTMOV bit set to zero indicates the contents of the TASK MANAGEMENT FUNCTIONS SHORT TIMEOUT field and
TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field are not valid and should be ignored.
An ABORT TASK timeout selector (ATTS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the ABORT TASK task management function. An ATTS bit set to
zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the ABORT
TASK task management function.
An ABORT TASK SET timeout selector (ATSTS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the ABORT TASK SET task management function. An ATSTS bit set
to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the ABORT
TASK SET task management function.
A CLEAR ACA timeout selector (CACATS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the CLEAR ACA task management function. A CACATS bit set to
zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the CLEAR
ACA task management function.
A CLEAR TASK SET timeout selector (CTSTS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the CLEAR TASK SET task management function. A CTSTS bit set
to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the CLEAR
TASK SET task management function.


A LOGICAL UNIT RESET timeout selector (LURTS) bit set to one indicates that the value in the TASK
MANAGEMENT FUNCTIONS SHORT TIMEOUT field applies to the LOGICAL UNIT RESET task management
function. A LURTS bit set to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT
field applies to the LOGICAL UNIT RESET task management function.
A QUERY TASK timeout selector (QTTS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the QUERY TASK task management function. A QTTS bit set to zero
indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the QUERY TASK
task management function.
A QUERY ASYNCHRONOUS EVENT timeout selector (QAETS) bit set to one indicates that the value in the
TASK MANAGEMENT FUNCTIONS SHORT TIMEOUT field applies to the QUERY ASYNCHRONOUS EVENT task
management function. A QAETS bit set to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS
LONG TIMEOUT field applies to the QUERY ASYNCHRONOUS EVENT task management function.
A QUERY TASK SET timeout selector (QTSTS) bit set to one indicates that the value in the TASK MANAGEMENT
FUNCTIONS SHORT TIMEOUT field applies to the QUERY TASK SET task management function. A QTSTS bit set
to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field applies to the QUERY
TASK SET task management function.
An I_T NEXUS RESET timeout selector (ITNRTS) bit set to one indicates that the value in the TASK
MANAGEMENT FUNCTIONS SHORT TIMEOUT field applies to the I_T NEXUS RESET task management function.
An ITNRTS bit set to zero indicates that the value in the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field
applies to the I_T NEXUS RESET task management function.
If the TMFTMOV bit is set to one and the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field is not set to zero,
then the contents of the TASK MANAGEMENT FUNCTIONS LONG TIMEOUT field indicate the recommended time in
100 millisecond increments that the application client should wait prior to timing out a task management
function for which the applicable selector bit is set to zero. If the TMFTMOV bit is set to zero or the TASK
MANAGEMENT FUNCTIONS LONG TIMEOUT field is set to zero, then the recommended timeout is unspecified for
any task management function for which the applicable selector bit is set to zero.
If the TMFTMOV bit is set to one and the TASK MANAGEMENT FUNCTIONS SHORT TIMEOUT field is not set to zero,
then the contents of the TASK MANAGEMENT FUNCTIONS SHORT TIMEOUT field indicate the recommended time in
100 millisecond increments that the application client should wait prior to timing out a task management
function for which the applicable selector bit is set to one. If the TMFTMOV bit is set to zero or the TASK
MANAGEMENT FUNCTIONS SHORT TIMEOUT field is set to zero, then the recommended timeout is unspecified for
any task management function for which the applicable selector bit is set to one.


6.37 REPORT TARGET PORT GROUPS command
The REPORT TARGET PORT GROUPS command (see table 302) requests that the device server send
target port group information to the application client. This command uses the MAINTENANCE IN CDB format
(see 4.2.2.3.3). This command shall be supported by logical units that report in the standard INQUIRY data
(see 6.6.2) that they support asymmetric logical unit access (i.e., return a non-zero value in the TPGS field).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 302 for the REPORT
TARGET PORT GROUPS command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 302 for the REPORT
TARGET PORT GROUPS command.
The PARAMETER DATA FORMAT field (see table 303) specifies the requested format for the parameter data
returned by the REPORT TARGET PORT GROUPS command. The device server may ignore the PARAMETER
DATA FORMAT field. If the device server ignores the PARAMETER DATA FORMAT field, the device server shall
return the parameter data format defined in table 304.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
Returning REPORT TARGET PORT GROUPS parameter data may require the enabling of a nonvolatile
memory. If the nonvolatile memory is not ready, the command shall be terminated with CHECK CONDITION
status, rather than wait for the nonvolatile memory to become ready. The sense key shall be set to NOT
READY and the additional sense code shall be set as described in table 334 (see 6.47).
Table 302 — REPORT TARGET PORT GROUPS command
Bit
Byte
OPERATION CODE (A3h)
PARAMETER DATA FORMAT
SERVICE ACTION (0Ah)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
Table 303 — PARAMETER DATA FORMAT field
Code
Description
Reference
000b
Length only header parameter data format
table 304
001b
Extended header parameter data format
table 305
010b to 111b
Reserved


The length only header format for the parameter data returned by the REPORT TARGET PORT GROUPS
command is shown in table 304.
The RETURN DATA LENGTH field indicates the length in bytes of the list of target port groups. The contents of the
RETURN DATA LENGTH field are not altered based on the allocation length (see 4.2.5.6).
There shall be one target port group descriptor (see table 306) for each target port group.
Table 304 — Length only header parameter data format
Bit
Byte
(MSB)
RETURN DATA LENGTH (n-3)
•••
(LSB)
Target port group descriptor list
Target port group descriptor [first] (see table 306)
•••
•••
Target port group descriptor [last] (see table 306)
•••
n


The extended header format for the parameter data returned by the REPORT TARGET PORT GROUPS
command is shown in table 305.
The RETURN DATA LENGTH field indicates the length in bytes of the list of target port groups. The contents of the
RETURN DATA LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The FORMAT TYPE field indicates the returned parameter data format and shall be set to 001b to indicate the
extended header parameter data format.
The IMPLICIT TRANSITION TIME field indicates the minimum amount of time in seconds the application client
should wait prior to timing out an implicit state transition (see 5.16.2.2). A value of zero indicates that the
implicit transition time is not specified.
Table 305 — Extended header parameter data format
Bit
Byte
(MSB)
RETURN DATA LENGTH (n-3)
•••
(LSB)
Reserved
FORMAT TYPE (001b)
Reserved
IMPLICIT TRANSITION TIME
Reserved
Target port group descriptor list
Target port group descriptor [first] (see table 306)
•••
•••
Target port group descriptor [last] (see table 306)
•••
n


There shall be one target port group descriptor (see table 306) for each target port group.
A preferred target port (PREF) bit set to one indicates that the primary target port group is a preferred primary
target port group for accessing the addressed logical unit (see 5.16.2.6). A PREF bit set to zero indicates the
primary target port group is not a preferred primary target port group.
The ASYMMETRIC ACCESS STATE field (see table 307) contains the target port group’s current target port
asymmetric access state.
If any of the T_SUP bit, O_SUP bit, LBD_SUP bit, U_SUP bit, S_SUP bit, AN_SUP bit, or AO_SUP bit are set to one,
then the T_SUP bit, O_SUP bit, LBD_SUP bit, U_SUP bit, S_SUP bit, AN_SUP bit, and AO_SUP bit are as defined in
this standard. If the T_SUP bit, O_SUP bit, U_SUP bit, S_SUP bit, AN_SUP bit, and AO_SUP bit are all set to zero,
then which target port asymmetric access states are supported is vendor specific.
Table 306 — Target port group descriptor format
Bit
Byte
PREF
0b
0b
0b
ASYMMETRIC ACCESS STATE
T_SUP
O_SUP
Reserved
LBD_SUP
U_SUP
S_SUP
AN_SUP
AO_SUP
(MSB)
TARGET PORT GROUP
(LSB)
Reserved
STATUS CODE
Vendor specific
TARGET PORT COUNT
Target port descriptor list
Target port descriptor [first] (see table 309)
•••
•••
n-3
Target port descriptor [last] (see table 309)
•••
n
Table 307 — ASYMMETRIC ACCESS STATE field
Code
State
Type (see 5.16.2.1)
Reference
0h
Active/optimized
Primary
5.16.2.4.2
1h
Active/non-optimized
Primary
5.16.2.4.3
2h
Standby
Primary
5.16.2.4.4
3h
Unavailable
Primary
5.16.2.4.5
4h
Logical block dependent
Primary
5.16.2.4.7
5h to Dh
Reserved
Eh
Offline
Secondary
5.16.2.4.6
Fh
Transitioning between states
Primary
5.16.2.5


A transitioning supported (T_SUP) bit set to one indicates that the device server supports returning the
ASYMMETRIC ACCESS STATE field set to Fh (i.e., transitioning between states). A T_SUP bit set to zero indicates
that the device server does not return an ASYMMETRIC ACCESS STATE field set to Fh.
An offline supported (O_SUP) bit set to one indicates that the offline secondary target port asymmetric access
state is supported. A O_SUP bit set to zero indicates that the offline secondary target port asymmetric access
state is not supported.
A logical block dependent (LBD_SUP) bit set to one indicates that the logical block dependent primary target
port asymmetric access state is supported. An LBD_SUP bit set to zero indicates that the logical block
dependent primary target port asymmetric access state is not supported.
An unavailable supported (U_SUP) bit set to one indicates that the unavailable primary target port asymmetric
access state is supported. A U_SUP bit set to zero indicates that the unavailable primary target port
asymmetric access state is not supported.
A standby supported (S_SUP) bit set to one indicates that the standby primary target port asymmetric access
state is supported. An S_SUP bit set to zero indicates that the standby primary target port asymmetric access
state is not supported.
An active/non-optimized supported (AN_SUP) bit set to one indicates that the active/non-optimized primary
target port asymmetric access state is supported. An AN_SUP bit set to zero indicates that the
active/non-optimized primary target port asymmetric access state is not supported.
An active/optimized supported (AO_SUP) bit set to one indicates that the active/optimized primary target port
asymmetric access state is supported. An AO_SUP bit set to zero indicates that the active/optimized primary
target port asymmetric access state is not supported.
The TARGET PORT GROUP field contains an identification of the target port group described by this target port
group descriptor. Target port group information is also returned in the Device Identification VPD page (see
7.8.6).
The STATUS CODE field (see table 308) indicates why a target port group may be in a specific target port
asymmetric access state. It provides a mechanism to indicate error conditions.
Table 308 — STATUS CODE field
Code
Description
00h
No status available.
01h
The target port asymmetric access state altered by SET
TARGET PORT GROUPS command.
02h
The target port asymmetric access state altered by implicit
asymmetrical logical unit access behavior.
03h to FFh
Reserved


The TARGET PORT COUNT field indicates the number of target ports that are in that target port group and the
number of target port descriptors in the target port group descriptor. Every target port group shall contain at
least one target port. The target port group descriptor shall include one target port descriptor for each target
port in the target port group.
The RELATIVE TARGET PORT IDENTIFIER field indicates a relative port identifier of a target port in the target port
group.
6.38 REPORT TIMESTAMP command
The REPORT TIMESTAMP command (see table 310) requests that the device server return the value of the
logical unit’s timestamp. This command uses the MAINTENANCE IN CDB format (see 4.2.2.3.3).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 310 for the REPORT
TIMESTAMP command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 310 for the REPORT
TIMESTAMP command.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
Table 309 — Target port descriptor format
Bit
Byte
Reserved
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
Table 310 — REPORT TIMESTAMP command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (0Fh)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The format for the parameter data returned by the REPORT TIMESTAMP command is shown in table 311.
The TIMESTAMP PARAMETER DATA LENGTH field indicates the number of bytes of parameter data that follow. The
contents of the TIMESTAMP PARAMETER DATA LENGTH field are not altered based on the allocation length (see
4.2.5.6).
The TIMESTAMP ORIGIN field indicates the origin of the timestamp (see 5.2).
The TIMESTAMP field contains the current value of the timestamp (see 5.2).
6.39 REQUEST SENSE command
The REQUEST SENSE command (see table 312) requests that the device server transfer parameter data
containing sense data (see 4.5) to the application client.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 312 for the REQUEST
SENSE command.
Table 311 — REPORT TIMESTAMP parameter data format
Bit
Byte
(MSB)
TIMESTAMP PARAMETER DATA LENGTH (000Ah)
(LSB)
Reserved
TIMESTAMP ORIGIN
Reserved
(MSB)
TIMESTAMP
•••
(LSB)
Reserved
Reserved
Table 312 — REQUEST SENSE command
Bit
Byte
OPERATION CODE (03h)
Reserved
DESC
Reserved
ALLOCATION LENGTH
CONTROL


The descriptor format (DESC) bit (see table 313) specifies which sense data format the device server shall
return in the parameter data.
The ALLOCATION LENGTH field is defined in 4.2.5.6. Application clients should request 252 bytes of sense data
to ensure they retrieve all the sense data. If fewer than 252 bytes are requested, sense data may be lost since
the REQUEST SENSE command with any allocation length clears the sense data.
The CONTROL byte is defined in SAM-5.
Sense data shall be available and cleared under the conditions defined in SAM-5.
Upon completion of the REQUEST SENSE command, the logical unit shall return to the same power condition
(see 5.12) that was active before the REQUEST SENSE command was received. A REQUEST SENSE
command shall not reset any power condition timers.
The device server shall return CHECK CONDITION status for a REQUEST SENSE command only to report
exception conditions specific to the REQUEST SENSE command itself. Examples of conditions that cause a
REQUEST SENSE command to return CHECK CONDITION status are:
a)
an invalid field value is detected in the CDB;
b)
the device server does not support the REQUEST SENSE command (see 4.2.1);
c)
the initiator port that sent the REQUEST SENSE command is pending enrollment for access controls
(see 8.3.1.7) and no other sense data is available to return;
d)
an unrecovered error is detected by a SCSI target port; or
e)
a malfunction prevents return of the sense data.
If a REQUEST SENSE command is terminated with CHECK CONDITION status, then:
a)
any parameter data that is transferred is invalid (i.e., the parameter data does not contain sense data);
and
b)
if the REQUEST SENSE command was received on an I_T nexus with a pending unit attention
condition (i.e., before the device server reports CHECK CONDITION status), then the device server
shall not clear the pending unit attention condition (see SAM-5).
The REQUEST SENSE command shall be capable of being processed to completion with GOOD status in
any power condition (see 5.12). However, some implementations may require a level of power consumption
that is higher than associated with the current power condition in any other circumstance. Details of how much
power processing a REQUEST SENSE command requires is outside the scope of this standard.
Table 313 — DESC bit
Code
Descriptor format sense
data supported?
Description
0b
yes or no
The device server shall return fixed format sense data (see
4.5.3) in the parameter data.
1b
yes
The device server shall return descriptor format sense data
(see 4.5.2) in the parameter data.
no
The device server shall return no parameter data and terminate
the REQUEST SENSE command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
Note: Device servers that are compliant with SPC-3 are capable of ignoring a DESC bit that is set to one.


Except as described elsewhere in this subclause, the device server shall process a REQUEST SENSE
command as follows:
1)
return applicable sense data in the parameter data as follows:
1)
if the logical unit that reports a peripheral qualifier of 011b or 001b in its standard INQUIRY data
(see 6.6.2), then return parameter data containing sense data with the sense key set to ILLEGAL
REQUEST and the additional sense code shall be set to LOGICAL UNIT NOT SUPPORTED;
2)
if the logical unit that reports a peripheral qualifier of 000b in its standard INQUIRY data because
it has a peripheral device connected but is not ready for access, then return parameter data
containing sense data appropriate to the condition that is making the logical unit not operational;
3)
if the REQUEST SENSE command was received on an I_T nexus with a pending unit attention
condition, then return parameter data containing sense data for the unit attention and clear the
unit attention condition as described in SAM-5;
4)
if a recovered error occurs during the processing of the REQUEST SENSE command, then return
parameter data containing sense data with the sense key set to RECOVERED ERROR;
5)
if deferred error sense data (see 4.5.5) is available, then return parameter data containing sense
data for the deferred error;
6)
return pollable sense data (see 5.11.2), if any; or
7)
return parameter data containing sense data with the sense key set to NO SENSE and the
additional sense code set to NO ADDITIONAL SENSE INFORMATION;
and
2)
complete the REQUEST SENSE command with GOOD status.
Device servers shall return at least 18 bytes of parameter data in response to a REQUEST SENSE command
if the allocation length is 18 or greater and the DESC bit is set to zero. Application clients may determine how
much sense data has been returned by examining the ALLOCATION LENGTH field in the CDB and the ADDITIONAL
SENSE LENGTH field in the sense data. Device servers shall not adjust the additional sense length to reflect
truncation if the allocation length is less than the sense data available.


6.40 SECURITY PROTOCOL IN command
The SECURITY PROTOCOL IN command (see table 314) is used to retrieve security protocol information
(see 7.7.1) or the results of one or more SECURITY PROTOCOL OUT commands (see 6.41).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 314 for the SECURITY
PROTOCOL IN command.
Table 314 — SECURITY PROTOCOL IN command
Bit
Byte
OPERATION CODE (A2h)
SECURITY PROTOCOL
SECURITY PROTOCOL SPECIFIC
INC_512
Reserved
Reserved
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The SECURITY PROTOCOL field (see table 315) specifies which security protocol is being used.
Editors Note 1 - ROW: SECURITY PROTOCOL field code values 22h to 2Fh are tentatively reserved
for SSC-x uses.
The contents of the SECURITY PROTOCOL SPECIFIC field depend on the protocol specified by the SECURITY
PROTOCOL field (see table 315).
A 512 increment (INC_512) bit set to one specifies that the ALLOCATION LENGTH field (see 4.2.5.6) expresses the
maximum number of bytes available to receive data in increments of 512 bytes (e.g., a value of one means
512 bytes, two means 1 024 bytes, etc.). Pad bytes may or may not be appended to meet this length. Pad
bytes shall have a value of 00h. An INC_512 bit set to zero specifies that the ALLOCATION LENGTH field
expresses the number of bytes to be transferred.
Indications of data overrun or underrun and the mechanism, if any, for processing retries depend on the
protocol specified by the SECURITY PROTOCOL field (see table 315).
The CONTROL byte is defined in SAM-5.
Any association between a previous SECURITY PROTOCOL OUT command and the data transferred by a
SECURITY PROTOCOL IN command depends on the protocol specified by the SECURITY PROTOCOL field (see
table 315). If the device server has no data to transfer (e.g., the results for any previous SECURITY
PROTOCOL OUT commands are not yet available), the device server may transfer data indicating it has no
other data to transfer.
Table 315 — SECURITY PROTOCOL field in SECURITY PROTOCOL IN command
Code
Description
Reference
00h
Security protocol information
7.7.1
01h to 06h
Defined by the TCG
3.1.182
07h
CbCS
7.7.4
08h to 1Fh
Reserved
20h
Tape Data Encryption
SSC-3
21h
Data Encryption Configuration
ADC-3
22h to 3Fh
Reserved
40h
SA Creation Capabilities
7.7.2
41h
IKEv2-SCSI
7.7.3
42h to EBh
Reserved
ECh
JEDEC Universal Flash Storage
UFS
EDh
SDcard TrustedFlash Security
Systems Specification 1.1.3
3.1.151
EEh
Authentication in Host Attachments
of Transient Storage Devices
IEEE 1667
EFh
ATA Device Server Password
SAT-3
F0h to FFh
Vendor Specific


The format of the data transferred depends on the protocol specified by the SECURITY PROTOCOL field (see
table 315).
The device server shall retain data resulting from a SECURITY PROTOCOL OUT command, if any, until one
of the following events is processed:
a)
transfer of the data via a SECURITY PROTOCOL IN command from the same I_T_L nexus as
defined by the protocol specified by the SECURITY PROTOCOL field (see table 315);
b)
logical unit reset (see SAM-5); or
c)
I_T nexus loss (see SAM-5) associated with the I_T nexus that sent the SECURITY PROTOCOL
OUT command.
If the data is lost due to one of these events the application client may send a new SECURITY PROTOCOL
OUT command to retry the operation.
6.41 SECURITY PROTOCOL OUT command
The SECURITY PROTOCOL OUT command (see table 316) is used to send data to the logical unit. The data
sent specifies one or more operations to be performed by the logical unit. The format and function of the
operations depends on the contents of the SECURITY PROTOCOL field (see table 317). Depending on the
protocol specified by the SECURITY PROTOCOL field, the application client may use the SECURITY PROTOCOL
IN command (see 6.40) to retrieve data derived from these operations.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 316 for the SECURITY
PROTOCOL OUT command.
Table 316 — SECURITY PROTOCOL OUT command
Bit
Byte
OPERATION CODE (B5h)
SECURITY PROTOCOL
SECURITY PROTOCOL SPECIFIC
INC_512
Reserved
Reserved
(MSB)
TRANSFER LENGTH

•••
(LSB)
Reserved
CONTROL


The SECURITY PROTOCOL field (see table 317) specifies which security protocol is being used.
Editors Note 2 - ROW: SECURITY PROTOCOL field code values 22h to 2Fh are tentatively reserved
for SSC-x uses.
The contents of the SECURITY PROTOCOL SPECIFIC field depend on the protocol specified by the SECURITY
PROTOCOL field (see table 317).
A 512 increment (INC_512) bit set to one specifies that the TRANSFER LENGTH field (see 4.2.5.4) expresses the
number of bytes to be transferred in increments of 512 bytes (e.g., a value of one means 512 bytes, two
means 1 024 bytes, etc.). Pad bytes shall be appended as needed to meet this requirement. Pad bytes shall
have a value of 00h. A INC_512 bit set to zero specifies that the TRANSFER LENGTH field indicates the number of
bytes to be transferred.
The CONTROL byte is defined in SAM-5.
Any association between a SECURITY PROTOCOL OUT command and a subsequent SECURITY
PROTOCOL IN command depends on the protocol specified by the SECURITY PROTOCOL field (see table 317).
Each protocol shall define whether:
a)
the device server shall complete the command with GOOD status as soon as it determines the data
has been correctly received. An indication that the data has been processed is obtained by sending a
SECURITY PROTOCOL IN command and receiving the results in the associated data transfer; or
b)
the device server shall complete the command with GOOD status only after the data has been
successfully processed and an associated SECURITY PROTOCOL IN command is not required.
Table 317 — SECURITY PROTOCOL field in SECURITY PROTOCOL OUT command
Code
Description
Reference
00h
Reserved
01h to 06h
Defined by the TCG
3.1.182
07h
CbCS
7.7.4
08h to 1Fh
Reserved
20h
Tape Data Encryption
SSC-3
21h
Data Encryption Configuration
ADC-3
22h to 40h
Reserved
41h
IKEv2-SCSI
7.7.3
42h to EBh
Reserved
ECh
JEDEC Universal Flash Storage
UFS
EDh
SDcard TrustedFlash Security
Systems Specification 1.1.3
3.1.151
EEh
Authentication in Host Attachments
of Transient Storage Devices
IEEE 1667
EFh
ATA Device Server Password
SAT-3
F0h to FFh
Vendor Specific


The format of the data transferred depends on the protocol specified by the SECURITY PROTOCOL field (see
table 317).
6.42 SEND DIAGNOSTIC command
The SEND DIAGNOSTIC command (see table 318) requests that the device server perform diagnostic opera-
tions on the SCSI target device, on the logical unit, or on both. Logical units that support this command shall
implement, at a minimum, the default self-test feature (i.e., the SELFTEST bit equal to one and a parameter list
length of zero).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 318 for the SEND
DIAGNOSTIC command.
Table 318 — SEND DIAGNOSTIC command
Bit
Byte
OPERATION CODE (1Dh)
SELF-TEST CODE
PF
Reserved
SELFTEST
DEVOFFL
UNITOFFL
Reserved
(MSB)
PARAMETER LIST LENGTH
(LSB)
CONTROL


The SELF-TEST CODE field defined in table 319 and further described in table 320.
The page format (PF) bit (see table 320) specifies the format of any parameter list sent by the application client
for a SEND DIAGNOSTIC command and may specify the format of the parameter data, if any, returned by the
device server in response to a subsequent RECEIVE DIAGNOSTIC RESULTS command (see 6.28). The
implementation of the PF bit is optional.
NOTE 42 - Logical units compliant with SPC-2 may transfer more than one diagnostic page in the SEND
DIAGNOSTIC command’s parameter list and by doing so may request that more than one diagnostic page be
transmitted in the RECEIVE DIAGNOSTIC RESULTS command’s parameter data.
The self-test (SELFTEST) bit (see table 320) specifies whether the device server shall perform the default
self-test (see 5.15.2).
A SCSI target device offline (DEVOFFL) bit set to one specifies that the device server may perform a default
self-test (see 5.15.2) that affects any logical unit in the SCSI target device (e.g., by alteration of reservations,
log parameters, or sense data). A DEVOFFL bit set to zero specifies that, after the device server has
completed a default self-test specified in the SEND DIAGNOSTIC command, no logical unit shall exhibit any
effects resulting from the device server’s processing the SEND DIAGNOSTIC command that are detectable
by any application client. If the SELFTEST bit is set to zero, the device server shall ignore the DEVOFFL bit.
A unit offline (UNITOFFL) bit set to one specifies that the device server may perform a default self-test (see
5.15.2) that affects the user accessible medium on the logical unit (e.g., write operations to the user acces-
Table 319 — SELF-TEST CODE field
Code
Name
Description
000b
This value is used if an operation not described in this table is being
requested (see table 320).
001b
Background
short self-test
The device server shall start its short self-test (see 5.15.3) in the background
mode (see 5.15.4.3).
010b
Background
extended self-test
The device server shall start its extended self-test (see 5.15.3) in the back-
ground mode (see 5.15.4.3).
011b
Reserved
100b
Abort background
self-test
If the SCSI target device is performing a self-test in the background mode
(see 5.15.4.3), then the device server shall abort the self-test. If the target
device is performing a self-test in the foreground mode, then the device
server shall process the command as described in 5.15.4.2.a If the target
device is not performing a self-test, then the device server shall terminate
the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD
IN CDB.
101b
Foreground
short self-test
The device server shall start its short self-test (see 5.15.3) in the foreground
mode (see 5.15.4.2).
110b
Foreground
extended self-test
The device server shall start its extended self-test (see 5.15.3) in the fore-
ground mode (see 5.15.4.2).
111b
Reserved
a Device servers compliant with SPC-3 may terminate the command with CHECK CONDITION status
with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB.


sible medium or repositioning of the medium on sequential access devices). A UNITOFFL bit set to zero
specifies that, after the device server has completed a default self-test specified in the SEND DIAGNOSTIC
command, the user accessible medium shall exhibit no effects resulting from the device server’s processing
the SEND DIAGNOSTIC command that are detectable by any application client. If the SELFTEST bit is set to
zero, the device server shall ignore the UNITOFFL bit.
The PARAMETER LIST LENGTH field (see table 320) specifies the length in bytes of the parameter list that shall
be transferred from the application client Data-Out Buffer to the device server. A parameter list length of zero
specifies that no data shall be transferred. This condition shall not be considered an error.
The CONTROL byte is defined in SAM-5.


Table 320 defines:
a)
the meaning of the combinations of values for the SELF-TEST CODE field, the PF bit, the SELFTEST bit,
and the PARAMETER LIST LENGTH field; and
b)
under which conditions the DEVOFFL bit and the UNITOFFL bit, if implemented, may be used and
under which conditions these bits are ignored.
Table 320 — The meanings of the SELF-TEST CODE field, the PF bit, the SELFTEST bit, and the
PARAMETER LIST LENGTH field (part 1 of 4)
SELF-
TEST
CODE
field
PF
bit
SELF
TEST
bit
PARA-
METER LIST
LENGTH
field
Description a, b
000b
0000h
The device server shall complete the command with GOOD status.
000b
0000h
The device server shall receive the amount of vendor specific
parameter list specified by the PARAMETER LIST LENGTH field.
If the parameter list is valid and requests that the device server
perform a diagnostic operation c, then:
a)
if the operation succeeds, the device server shall complete the
command with GOOD status;
b)
if the operation fails, then the device server shall terminate the
command with CHECK CONDITION status with the sense key
set to HARDWARE ERROR and the additional sense code set
to the appropriate value to describe the failure; and
c)
if parameter data is required to be returned by the device server
for the operation, then a subsequent RECEIVE DIAGNOSTIC
RESULTS command (see 6.28) determines the device server’s
response.
If the parameter list is valid and does not request the device server to
perform a diagnostic operation, then the device server processes the
vendor specific data. A subsequent RECEIVE DIAGNOSTIC
RESULTS command may be required for an application client to
determine the device server’s response.
If the parameter list is not valid, then the device server shall terminate
the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN PARAMETER LIST.
a Each description assumes that all other bits and fields in the CDB that are not defined for a particular
case are valid. If, in any case, some other bit or field in the CDB is not valid, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN CDB.
b The device server shall ignore the DEVOFFL bit and the UNITOFFL bit in all cases where their use is not
included in the description.
c Before beginning any self-test, the device server shall:
a)
stop all running power condition timers;
b)
not stop any process that causes a background function to occur (e.g., not stop any timers or
counters associated with background functions); and
c)
after completing the command, the device server shall reinitialize and restart all enabled power
condition timers.


000b
0000h
The device server shall perform its default self-test, and if imple-
mented, use the values in the DEVOFFL bit and the UNITOFFL bit for
processing the self-test
If the self-test succeeds, the device server shall return GOOD status
for the command.
If the self-test fails, then the device server shall terminate the com-
mand with CHECK CONDITION status with the sense key set to
HARDWARE ERROR and the additional sense code set to the
appropriate value to describe the failure.
000b
0000h
The device server shall terminate the command with CHECK CONDI-
TION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
000b
0000h
The device server shall:
a)
complete the command with GOOD status; and
b)
if requested by a subsequent RECEIVE DIAGNOSTIC
RESULTS command, then:
A)
if the PF bit is supported by the device server, then return a
single diagnostic page (see 7.2) as specified by the
command; or
B)
if the PF bit is not supported by the device server, then return
vendor specific parameter data as specified by the
command.
Table 320 — The meanings of the SELF-TEST CODE field, the PF bit, the SELFTEST bit, and the
PARAMETER LIST LENGTH field (part 2 of 4)
SELF-
TEST
CODE
field
PF
bit
SELF
TEST
bit
PARA-
METER LIST
LENGTH
field
Description a, b
a Each description assumes that all other bits and fields in the CDB that are not defined for a particular
case are valid. If, in any case, some other bit or field in the CDB is not valid, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN CDB.
b The device server shall ignore the DEVOFFL bit and the UNITOFFL bit in all cases where their use is not
included in the description.
c Before beginning any self-test, the device server shall:
a)
stop all running power condition timers;
b)
not stop any process that causes a background function to occur (e.g., not stop any timers or
counters associated with background functions); and
c)
after completing the command, the device server shall reinitialize and restart all enabled power
condition timers.


000b
0000h
The device server shall receive the amount of parameter list specified
by the PARAMETER LIST LENGTH field.
If the PF bit is supported by the device server, then:
a)
the parameter list shall be a single diagnostic page; and
b)
if the specified parameter list length results in the truncation of
the diagnostic page (e.g., the parameter list length is less than
the page length indicated by the diagnostic page), then the
device server shall terminate the command with CHECK
CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID
FIELD IN CDB.
If the PF bit is not supported by the device server, then the parameter
list is vendor specific.
If the parameter list is valid and requests that the device server
perform a diagnostic operation c, then:
a)
if the operation succeeds, the device server shall complete the
command with GOOD status;
b)
if the operation fails, then the device server shall terminate the
command with CHECK CONDITION status with the sense key
set to HARDWARE ERROR and the additional sense code set
to the appropriate value to describe the failure; and
c)
if parameter data is required to be returned by the device server
for the operation, then a subsequent RECEIVE DIAGNOSTIC
RESULTS command (see 6.28) determines the device server’s
response.
If the parameter list is valid and does not request the device server to
perform a diagnostic operation, then the device server processes the
data as defined in 7.2. A subsequent RECEIVE DIAGNOSTIC
RESULTS command may be required for an application client to
determine the device server’s response.
If the parameter list is not valid, then the device server shall terminate
the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN PARAMETER LIST.
Table 320 — The meanings of the SELF-TEST CODE field, the PF bit, the SELFTEST bit, and the
PARAMETER LIST LENGTH field (part 3 of 4)
SELF-
TEST
CODE
field
PF
bit
SELF
TEST
bit
PARA-
METER LIST
LENGTH
field
Description a, b
a Each description assumes that all other bits and fields in the CDB that are not defined for a particular
case are valid. If, in any case, some other bit or field in the CDB is not valid, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN CDB.
b The device server shall ignore the DEVOFFL bit and the UNITOFFL bit in all cases where their use is not
included in the description.
c Before beginning any self-test, the device server shall:
a)
stop all running power condition timers;
b)
not stop any process that causes a background function to occur (e.g., not stop any timers or
counters associated with background functions); and
c)
after completing the command, the device server shall reinitialize and restart all enabled power
condition timers.


000b
n/a
The device server shall terminate the command with CHECK CONDI-
TION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
000b
0000h
The device server shall perform the operation defined in table 319. c
000b
0000h
The device server shall terminate the command with CHECK CONDI-
TION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
000b
n/a
000b
0000h
The device server shall perform the operation defined in table 319. c
If the device server supports the PF bit, then, for a subsequent
RECEIVE DIAGNOSTIC RESULTS command, the device server
shall return a single diagnostic page as specified by the command.
If the device server does not support the PF bit, then, the parameter
data for a subsequent RECEIVE DIAGNOSTIC RESULTS command
is vendor specific.
000b
0000h
The device server shall terminate the command with CHECK CONDI-
TION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN CDB.
000b
n/a
Table 320 — The meanings of the SELF-TEST CODE field, the PF bit, the SELFTEST bit, and the
PARAMETER LIST LENGTH field (part 4 of 4)
SELF-
TEST
CODE
field
PF
bit
SELF
TEST
bit
PARA-
METER LIST
LENGTH
field
Description a, b
a Each description assumes that all other bits and fields in the CDB that are not defined for a particular
case are valid. If, in any case, some other bit or field in the CDB is not valid, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN CDB.
b The device server shall ignore the DEVOFFL bit and the UNITOFFL bit in all cases where their use is not
included in the description.
c Before beginning any self-test, the device server shall:
a)
stop all running power condition timers;
b)
not stop any process that causes a background function to occur (e.g., not stop any timers or
counters associated with background functions); and
c)
after completing the command, the device server shall reinitialize and restart all enabled power
condition timers.


6.43 SET IDENTIFYING INFORMATION command
The SET IDENTIFYING INFORMATION command (see table 321) requests that the device server set identi-
fying information (see 5.6) in the logical unit to the value received in the SET IDENTIFYING INFORMATION
parameter list. This command uses the MAINTENANCE OUT CDB format (see 4.2.2.3.4). The SET IDENTI-
FYING INFORMATION command is an extension to the SET PERIPHERAL DEVICE/COMPONENT DEVICE
IDENTIFIER service action of the MAINTENANCE OUT command defined in SCC-2.
Processing a SET IDENTIFYING INFORMATION command may require the enabling of a nonvolatile
memory within the logical unit. If the nonvolatile memory is not ready, the command shall be terminated with
CHECK CONDITION status, and not wait for the nonvolatile memory to become ready. The sense key shall
be set to NOT READY and the additional sense code shall be set as described in table 334 (see 6.47). This
information should allow the application client to determine the action required to cause the device server to
become ready.
On successful completion of a SET IDENTIFYING INFORMATION command that changes identifying infor-
mation saved by the logical unit, the device server shall establish a unit attention condition (see SAM-5) for
the initiator port associated with every I_T nexus except the I_T nexus on which the SET IDENTIFYING
INFORMATION command was received, with the additional sense code set to DEVICE IDENTIFIER
CHANGED.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 321 for the SET IDENTI-
FYING INFORMATION command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 321 for the SET IDENTI-
FYING INFORMATION command.
The PARAMETER LIST LENGTH field specifies the length in bytes of the identifying information that shall be trans-
ferred from the application client to the device server. A parameter list length of zero specifies that no data
shall be transferred, and that subsequent REPORT IDENTIFYING INFORMATION commands shall return the
INFORMATION LENGTH field set to zero for the specified information type.
Table 321 — SET IDENTIFYING INFORMATION command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (06h)
Reserved
Restricted (see SCC-2)
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
INFORMATION TYPE
Reserved
CONTROL


The INFORMATION TYPE field (see table 322) specifies the identifying information type to be set. If the specified
information type is not implemented by the device server, then the command shall be terminated with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-5.
The SET IDENTIFYING INFORMATION parameter list (see table 323) contains the identifying information to
be set by the device server.
The INFORMATION field specifies the identifying information to be set for the specified information type (see
5.6).
Upon successful completion of a SET IDENTIFYING INFORMATION command, the identifying information
that is saved by the logical unit shall persist through logical unit resets, hard resets, power loss, I_T nexus
losses, media format operations, and media replacement.
Table 322 — INFORMATION TYPE field
Code
Description
0000000b
Peripheral device identifying information (see 5.6).
If the PARAMETER LIST LENGTH field is set to greater than the maximum length of the periph-
eral device identifying information (see 5.6) supported by the device server, then the device
server shall terminate the command with CHECK CONDITION status with the sense key
set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
0000010b
Peripheral device text identifying information (see 5.6).
If the PARAMETER LIST LENGTH field is set to a value greater than the maximum length of the
peripheral device text identifying information (see 5.6) supported by the device server, then
the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD
IN CDB.
If the format of the INFORMATION field is incorrect, the device server shall terminate the com-
mand with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
xxxxxx1b
Restricted (see SCC-2)
All other
Reserved
Table 323 — SET IDENTIFYING INFORMATION parameter list
Bit
Byte
INFORMATION
•••
n


6.44 SET PRIORITY command
The SET PRIORITY command (see table 324) requests that a priority be set to the specified value. This
command uses the MAINTENANCE OUT CDB format (see 4.2.2.3.4). The priority set by this command shall
remain in effect until one of the following occurs:
a)
another SET PRIORITY command is received;
b)
hard reset;
c)
logical unit reset; or
d)
power off.
The priority set by this command shall not be affected by an I_T nexus loss.
The priority set by a SET PRIORITY command may be used as a command priority (see SAM-5) for
commands received by the logical unit via an I_T nexus (i.e., an I_T_L nexus).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 324 for the SET PRIORITY
command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 324 for the SET PRIORITY
command.
Table 324 — SET PRIORITY command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (0Eh)
I_T_L NEXUS TO SET
Reserved
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


The I_T_L NEXUS TO SET field (see table 325) specifies the I_T_L nexus and the location of the priority value to
be assigned to that I_T_L nexus.
The PARAMETER LIST LENGTH field specifies the length in bytes of the SET PRIORITY parameter list (see table
326) that shall be contained in the Data-Out Buffer. A parameter list length of zero specifies that the Data-Out
Buffer shall be empty. This condition shall not be considered an error.
The CONTROL byte is defined in SAM-5.
Table 325 — I_T_L NEXUS TO SET field
Code
Description
00b
The priority for the I_T_L nexus associated with this command shall be set to the value con-
tained in the PRIORITY TO SET field in the SET PRIORITY parameter list (see table 326). All fields
in the SET PRIORITY parameter list except the PRIORITY TO SET field shall be ignored.
If the parameter list length is zero, the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
PARAMETER LIST LENGTH ERROR.
01b
The priority for the I_T_L nexus specified by the logical unit that is processing this command, the
RELATIVE TARGET PORT IDENTIFIER field, and the TransportID in the SET PRIORITY parameter list
(see table 326) shall be set to the value specified by the PRIORITY TO SET field in the SET PRIOR-
ITY parameter list.
If the parameter list length results in the truncation of the RELATIVE TARGET PORT IDENTIFIER field,
the ADDITIONAL DESCRIPTOR LENGTH field, or the TransportID, then the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to PARAMETER LIST LENGTH ERROR.
On successful completion of a SET PRIORITY command the device server shall establish a unit
attention condition (see SAM-5) for the initiator port associated with the I_T nexus specified by
the TransportID and the RELATIVE TARGET PORT IDENTIFIER field, with the additional sense code
set to PRIORITY CHANGED.
10b
The priority value specified in the INITIAL COMMAND PRIORITY field of the Control Extension mode
page (see 7.5.9) shall be used for all I_T_L nexuses associated with the logical unit that is pro-
cessing this command regardless of any prior priority. The contents of the SET PRIORITY
parameter list shall be ignored.
On successful completion of a SET PRIORITY command the device server shall establish a unit
attention condition (see SAM-5) for the initiator port associated with every other I_T_L nexus,
with the additional sense code set to PRIORITY CHANGED.
11b
Reserved


The format for the parameter data returned by the SET PRIORITY command is shown in table 326.
The PRIORITY TO SET field specifies the priority to be assigned to the I_T_L nexus specified by the I_T_L NEXUS
TO SET field in the CDB. The value in the PRIORITY TO SET field shall be returned in subsequent REPORT
PRIORITY commands (see 6.34) until one of the conditions described in this subclause occurs. A priority to
set value of zero specifies the I_T_L nexus specified by the I_T_L NEXUS TO SET field shall be set to the value
specified in the INITIAL COMMAND PRIORITY field of the Control Extension mode page (see 7.5.9). The contents
of the I_T_L NEXUS TO SET field may specify that the PRIORITY TO SET field shall be ignored.
The RELATIVE TARGET PORT IDENTIFIER field specifies the relative port identifier of the target port that is part of
the I_T_L nexus for which the priority is to be set. The contents of the I_T_L NEXUS TO SET field may specify
that the RELATIVE TARGET PORT IDENTIFIER field shall be ignored.
The ADDITIONAL LENGTH field specifies the number of bytes that follow in the SET PRIORITY parameter list
(i.e., the size of the TransportID).
The TransportID specifies a TransportID (see 7.6.4) identifying the initiator port that is part of the I_T_L nexus
for which the priority is to be set. The contents of the I_T_L NEXUS TO SET field may specify that the TRANS-
PORTID field shall be ignored.
Table 326 — SET PRIORITY parameter list format
Bit
Byte
Reserved
PRIORITY TO SET
Reserved
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
Reserved
Reserved
(MSB)
ADDITIONAL LENGTH (n-7)
(LSB)
TransportID
•••
n


6.45 SET TARGET PORT GROUPS command
The SET TARGET PORT GROUPS command (see table 327) requests that the device server set the primary
target port asymmetric access state of all of the target ports in the specified primary target port groups and/or
the secondary target port asymmetric access state of the specified target ports. This command uses the
MAINTENANCE OUT CDB format (see 4.2.2.3.4). See 5.16 for details regarding the transition between target
port asymmetric access states. This command is mandatory for all logical units that report in the standard
INQUIRY data (see 6.6.2) that they support explicit asymmetric logical units access (i.e., the TPGS field is set
to either 10b or 11b).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 327 for the SET TARGET
PORT GROUPS command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 327 for the SET TARGET
PORT GROUPS command.
The PARAMETER LIST LENGTH field specifies the length in bytes of the target port group management param-
eters that shall be transferred from the application client to the device server. A parameter list length of zero
specifies that no data shall be transferred, and that no change shall be made in the target port asymmetric
access state of any target port groups or target ports. If the parameter list length violates the vendor specific
length requirements, the command shall be terminated with CHECK CONDITION status, with the sense key
set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-5.
The allowable values to which target port asymmetric access states may be set is vendor specific and should
be reported in the REPORT TARGET PORT GROUP parameter data (see 6.37).
Primary target port groups that are not specified in a parameter list may change primary target port
asymmetric access states as a result of the SET TARGET PORT GROUPS command. This shall not be
considered an implicit target port asymmetric access state change.
If the SET TARGET PORT GROUPS attempts to establish an invalid combination of target port asymmetric
access states or attempts to establish an unsupported target port asymmetric access state, then the
Table 327 — SET TARGET PORT GROUPS command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (0Ah)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the SET TARGET PORT GROUPS command has been performed, the completion of the command
depends upon which of the following conditions apply:
a)
if the transition is treated as a single indivisible event (see 5.16.2.5), then the SET TARGET PORT
GROUPS command shall not complete until the transition to the requested state has completed; or
b)
if the transition is not treated as a single indivisible event (i.e., the device server supports other
commands (see 5.16.2.5) when those commands are routed though a target port that is transitioning
between target port asymmetric access states), then the SET TARGET PORT GROUPS command
may complete before the transition into the requested state has completed.
If the SET TARGET PORT GROUPS command is not performed successfully, the completion of the command
depends upon which of the following conditions apply:
a)
if the processing of a SET TARGET PORT GROUPS command requires the enabling of a nonvolatile
memory and the nonvolatile memory is not ready, then the command shall be terminated with CHECK
CONDITION status, rather than wait for the logical unit to become ready. The sense key shall be set
to NOT READY and the additional sense code shall be set as described in table 334 (see 6.47); or
b)
if a failure occurred before the transition was completed, the command shall be terminated with
CHECK CONDITION status, with the sense key set to HARDWARE ERROR, and the additional
sense code set to SET TARGET PORT GROUPS COMMAND FAILED.
If two SET TARGET PORT GROUPS commands are performed concurrently, the target port asymmetric
access state change behavior is vendor specific. A SCSI target device should not process multiple SET
TARGET PORT GROUPS concurrently.
The SET TARGET PORT GROUPS parameter data format is shown in table 328.
Table 328 — SET TARGET PORT GROUPS parameter list format
Bit
Byte
Reserved
•••
Set target port group descriptor list
Set target port group descriptor 0 (see table 329)
•••
•••
n-3
Set target port group descriptor x (see table 329)
•••
n


The format of the set target port group descriptor is defined in table 329.
If the ASYMMETRIC ACCESS STATE field (see table 330) specifies a primary target port asymmetric access state,
then all the target ports in the specified target port group shall transition to the specified state (see 5.16.2.5). If
the ASYMMETRIC ACCESS STATE field specifies a secondary target port asymmetric access state, then the
specified target port shall transition to the specified state.
If the ASYMMETRIC ACCESS STATE field (see table 330) specifies a primary target port asymmetric access state,
then the TARGET PORT GROUP OR TARGET PORT field specifies a primary target port group for which the primary
target port asymmetric access state shall be changed. If the ASYMMETRIC ACCESS STATE field specifies a
secondary target port asymmetric access state, then the TARGET PORT GROUP OR TARGET PORT field specifies
the relative target port identifier of the target port for which the secondary target port asymmetric access state
shall be changed.
Table 329 — Set target port group descriptor parameter list
Bit
Byte
Reserved
ASYMMETRIC ACCESS STATE
Reserved
(MSB)
TARGET PORT GROUP OR TARGET PORT
(LSB)
Table 330 — ASYMMETRIC ACCESS STATE field
Value
State (see 5.16.2.4)
Type (see 5.16.2.1)
0h
Active/optimized
Primary
1h
Active/non-optimized
Primary
2h
Standby
Primary
3h
Unavailable
Primary
4h
Illegal Request a
5h to Dh
Reserved
Eh
Offline
Secondary
Fh
Illegal Request a
a If the ASYMMETRIC ACCESS STATE field in any target port group descriptor
contains Fh, the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.


6.46 SET TIMESTAMP command
The SET TIMESTAMP command (see table 331) requests that the device server initialize the timestamp (see
5.2), if the SCSIP bit is set to one or the TCMOS bit is set to one in the Control Extension mode page (see 7.5.9).
If the SCSIP bit is set to zero, the SET TIMESTAMP command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
CDB. This command uses the MAINTENANCE OUT CDB format (see 4.2.2.3.4).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 331 for the SET
TIMESTAMP command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 331 for the SET TIMESTAMP
command.
The PARAMETER LIST LENGTH field specifies the length in bytes of the SET TIMESTAMP parameters that shall
be transferred from the application client to the device server. A parameter list length of zero specifies that no
data shall be transferred, and that no change shall be made to the timestamp.
The CONTROL byte is defined in SAM-5.
Table 331 — SET TIMESTAMP command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (0Fh)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


The format for the parameter list for the SET TIMESTAMP command is shown in table 332.
The TIMESTAMP field shall contain the initial value of the timestamp in the format defined in 5.2. The timestamp
should be the number of milliseconds that have elapsed since midnight, 1 January 1970 UT. If the high order
byte in the TIMESTAMP field is greater than F0h, the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
On successful completion of a SET TIMESTAMP command the device server shall establish a unit attention
condition for the initiator port associated with every I_T nexus except the I_T nexus on which the SET
TIMESTAMP command was received (see SAM-5), with the additional sense code set to TIMESTAMP
CHANGED.
Table 332 — SET TIMESTAMP parameter list format
Bit
Byte
Reserved
•••
(MSB)
TIMESTAMP
•••
(LSB)
Reserved


6.47 TEST UNIT READY command
The TEST UNIT READY command (see table 333) provides a means to check if the logical unit is ready. This
is not a request for a self-test. If the logical unit is able to accept an appropriate medium-access command
without returning CHECK CONDITION status, this command shall return a GOOD status. If the logical unit is
unable to become operational or is in a state such that an application client action (e.g., START UNIT
command) is required to make the logical unit ready, the command shall be terminated with CHECK
CONDITION status, with the sense key set to NOT READY.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 333 for the TEST UNIT
READY command.
The CONTROL byte is defined in SAM-5.
Table 334 defines the suggested CHECK CONDITION status responses to the TEST UNIT READY
command. Other conditions (e.g., deferred errors, reservations, or target port asymmetric access state
changes) may result in other responses (e.g., GOOD status, CHECK CONDITION status, BUSY status, or
RESERVATION CONFLICT status, each with or without other sense key and additional sense code values).
Table 333 — TEST UNIT READY command
Bit
Byte
OPERATION CODE (00h)
Reserved

•••
CONTROL
Table 334 — Preferred TEST UNIT READY responses
Status
Sense Key
Additional Sense Code
CHECK CONDITION
ILLEGAL REQUEST
LOGICAL UNIT NOT SUPPORTED
CHECK CONDITION
NOT READY
LOGICAL UNIT DOES NOT RESPOND
TO SELECTION
CHECK CONDITION
NOT READY
MEDIUM NOT PRESENT
CHECK CONDITION
NOT READY
LOGICAL UNIT NOT READY,
CAUSE NOT REPORTABLE
CHECK CONDITION
NOT READY
LOGICAL UNIT IS IN PROCESS
OF BECOMING READY
CHECK CONDITION
NOT READY
LOGICAL UNIT NOT READY,
INITIALIZING COMMAND REQUIRED
CHECK CONDITION
NOT READY
LOGICAL UNIT NOT READY,
MANUAL INTERVENTION REQUIRED
CHECK CONDITION
NOT READY
LOGICAL UNIT NOT READY,
FORMAT IN PROGRESS
CHECK CONDITION
NOT READY
LOGICAL UNIT NOT READY,
SANITIZE IN PROGRESS


6.48 WRITE ATTRIBUTE command
The WRITE ATTRIBUTE command (see table 335) allows an application client to write attributes to medium
auxiliary memory. Device servers that implement the WRITE ATTRIBUTE command shall also implement the
READ ATTRIBUTE command (see 6.17). Application clients should issue READ ATTRIBUTE commands
prior to using this command to discover device server support for medium auxiliary memory.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 335 for the WRITE
ATTRIBUTE command.
The write-through cache (WTC) bit set to one specifies the attributes in the parameter list shall be synchronized
with the medium auxiliary memory during the processing of the WRITE ATTRIBUTE command and GOOD
status shall not be returned until the attributes have been synchronized with the medium auxiliary memory.
The WTC bit is set to zero specifies no requirement related to the attributes in the parameter list being synchro-
nized with the medium auxiliary memory during the processing of the WRITE ATTRIBUTE command.
The LOGICAL VOLUME NUMBER field specifies a logical volume (e.g., the medium auxiliary memory storage for
one side of a double sided medium) within the medium auxiliary memory. The number of logical volumes of
the medium auxiliary memory shall equal that of the attached medium. If the medium only has a single logical
volume, then its logical volume number shall be zero.
The PARTITION NUMBER field specifies a partition (see SSC-3) within a logical volume. The number of partitions
of the medium auxiliary memory shall equal that of the attached medium. If the medium only has a single
partition, then its partition number shall be zero.
If the combination of logical volume number and partition number is not valid, the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
Table 335 — WRITE ATTRIBUTE command
Bit
Byte
OPERATION CODE (8Dh)
Reserved
WTC
Restricted (see SMC-3)
LOGICAL VOLUME NUMBER
Reserved
PARTITION NUMBER
Reserved
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter list contained in the Data-Out
Buffer. A parameter list length of zero specifies that no parameter data is present; this shall not be considered
an error. If the parameter list length results in the truncation of an attribute, the WRITE ATTRIBUTE command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to PARAMETER LIST LENGTH ERROR.
The CONTROL byte is defined in SAM-5.
The parameter list shall have the format shown in table 336. Attributes should be sent in ascending numerical
order. If the attributes are not in order, then no attributes shall be changed and the WRITE ATTRIBUTE
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The PARAMETER DATA LENGTH field should contain the number of bytes of attribute data and shall be ignored by
the device server.
The format of the attributes is described in 7.4.1.
If there is not enough space to write the attributes to the medium auxiliary memory, then no attributes shall be
changed and the WRITE ATTRIBUTE command shall be terminated with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to AUXILIARY MEMORY OUT
OF SPACE.
If the medium auxiliary memory is not accessible because there is no medium present, then no attributes shall
be changed and the WRITE ATTRIBUTE command shall be terminated with CHECK CONDITION status, with
the sense key set to NOT READY, and the additional sense code set to MEDIUM NOT PRESENT.
If the medium is present but the medium auxiliary memory is not accessible, then no attributes shall be
changed and the WRITE ATTRIBUTE command shall be terminated with CHECK CONDITION status, with
the sense key set to MEDIUM ERROR, and the additional sense code set to LOGICAL UNIT NOT READY,
AUXILIARY MEMORY NOT ACCESSIBLE.
Table 336 — WRITE ATTRIBUTE parameter list format
Bit
Byte
(MSB)
PARAMETER DATA LENGTH (n-3)

•••
 (LSB)
Attribute(s)
Attribute 0 (see 7.4.1)
•••
•••
Attribute x (see 7.4.1)
•••
n


If the medium auxiliary memory is not operational (e.g., bad checksum), the WRITE ATTRIBUTE command
shall be terminated with CHECK CONDITION status, with the sense key set to MEDIUM ERROR, and the
additional sense code set to AUXILIARY MEMORY WRITE ERROR.
If the WRITE ATTRIBUTE command parameter data contains an attribute with an ATTRIBUTE LENGTH field (see
7.4.1) set to zero, then one of the following actions shall occur:
a)
if the attribute state is unsupported or read only (see 5.7), then no attributes shall be changed and the
WRITE ATTRIBUTE command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST;
b)
if the attribute state is read/write, the attribute shall be changed to the nonexistent state. This attribute
shall not be returned in response to a READ ATTRIBUTE command and not be reported by the READ
ATTRIBUTE command with ATTRIBUTE LIST service action; or
c)
if the attribute state is nonexistent, the attribute in the WRITE ATTRIBUTE command parameter list
shall be ignored; this shall not be considered an error.
No attributes shall be changed, the WRITE ATTRIBUTE command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST if the parameter data contains any of the following:
a)
an attempt to change an attribute in the read only state (see 5.7);
b)
an attribute with incorrect ATTRIBUTE LENGTH field (see 7.4.1) contents; or
c)
an attribute with unsupported ATTRIBUTE VALUE field (see 7.4.1) contents.


6.49 WRITE BUFFER command
6.49.1 WRITE BUFFER command introduction
The WRITE BUFFER command (see table 337) is used in conjunction with the READ BUFFER command for:
a)
testing logical unit buffer memory;
b)
testing the integrity of the service delivery subsystem;
c)
downloading microcode (see 5.4); and
d)
downloading application client error history (see 5.5).
This command shall not alter any medium of the logical unit if the data mode or the combined header and data
mode is specified.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 337 for the WRITE BUFFER
command.
The usage of the MODE SPECIFIC field depends on the value in the MODE field.
Table 337 — WRITE BUFFER command
Bit
Byte
OPERATION CODE (3Bh)
MODE SPECIFIC
MODE
BUFFER ID
(MSB)
BUFFER OFFSET
(LSB)
(MSB)
PARAMETER LIST LENGTH
(LSB)
CONTROL


The function of this command and the meaning of fields within the CDB depend on the contents of the MODE
field. The MODE field is defined in table 338.
The MODE field may be processed as specifying a service action by the REPORT SUPPORTED OPERATION
CODES command (see 6.35).
The CONTROL byte is defined in SAM-5.
6.49.2 Combined header and data mode (00h)
In this mode, data to be transferred is preceded by a four-byte header. The four-byte header consists of all
reserved bytes.
The MODE SPECIFIC field is reserved.
The BUFFER ID and the BUFFER OFFSET fields shall be set to zero.
The PARAMETER LIST LENGTH field specifies the maximum number of bytes that shall be transferred from the
Data-Out Buffer. This number includes four bytes of header, so the data length to be stored in the device
Table 338 — WRITE BUFFER MODE field
Code
Description
Reference
00h
Combined header and data a
6.49.2
01h
Vendor specific a
6.49.3
02h
Data
6.49.4
03h
Reserved
04h
Download microcode and activate
5.4 and 6.49.5
05h
Download microcode, save, and activate
5.4 and 6.49.6
06h
Download microcode with offsets and activate
5.4 and 6.49.7
07h
Download microcode with offsets, save, and activate
5.4 and 6.49.8
08h to 09h
Reserved
0Ah
Write data to echo buffer
6.49.9
0Bh to 0Ch
Reserved
0Dh
Download microcode with offsets, select activation events,
save, and defer activate
5.4 and 6.49.10
0Eh
Download microcode with offsets, save, and defer activate
5.4 and 6.49.11
0Fh
Activate deferred microcode
5.4 and 6.49.12
10h to 19h
Reserved
1Ah
Enable expander communications protocol and Echo buffer
6.49.13
1Bh
Disable expander communications protocol
6.49.14
1Ch
Download application client error history
5.5 and 6.49.15
1Dh to 1Fh
Reserved
a Modes 00h and 01h are not recommended.


server’s buffer is parameter list length minus four. The application client should attempt to ensure that the
parameter list length is not greater than four plus the BUFFER CAPACITY field value (see 6.18.2) that is returned
in the header of the READ BUFFER command combined header and data mode (i.e., 0h). If the parameter list
length exceeds the buffer capacity, the command shall be terminated with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.49.3 Vendor specific mode (01h)
In this mode, the MODE SPECIFIC field is reserved.
The meaning of the BUFFER ID, BUFFER OFFSET, and PARAMETER LIST LENGTH fields are not specified by this
standard.
6.49.4 Data mode (02h)
In this mode, the Data-Out Buffer contains buffer data destined for the logical unit. The BUFFER ID field
identifies a specific buffer within the logical unit. The vendor assigns buffer ID codes to buffers within the
logical unit. Buffer ID zero shall be supported. If more than one buffer is supported, then additional buffer ID
codes shall be assigned contiguously, beginning with one. If an unsupported buffer ID code is selected, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The MODE SPECIFIC field is reserved.
The BUFFER OFFSET field specifies the location in the buffer to which the data is written. The application client
should conform to the offset boundary requirements returned in the READ BUFFER descriptor (see 6.18.5). If
the device server is unable to process the specified buffer offset, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN CDB.
The PARAMETER LIST LENGTH field specifies the maximum number of bytes that shall be transferred from the
Data-Out Buffer to be stored in the specified buffer beginning at the buffer offset. The application client should
attempt to ensure that the parameter list length plus the buffer offset does not exceed the capacity of the
specified buffer. The capacity of the buffer is indicated by the BUFFER CAPACITY field in the READ BUFFER
descriptor (see 6.18.5). If the BUFFER OFFSET and PARAMETER LIST LENGTH fields specify a transfer in excess of
the buffer capacity, the command shall be terminated with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.49.5 Download microcode and activate mode (04h)
In this mode, microcode shall be transferred to the device server and activated (see 5.4).
The MODE SPECIFIC field is reserved.
The BUFFER ID field, BUFFER OFFSET field, and PARAMETER LIST LENGTH field are vendor specific.


6.49.6 Download microcode, save, and activate mode (05h)
In this mode, microcode shall be transferred to the device server, saved to nonvolatile storage, and activated
(see 5.4) based on the setting of the ACTIVATE MICROCODE field in the Extended INQUIRY VPD page (see
7.8.7).
The MODE SPECIFIC field is reserved.
The BUFFER ID field, BUFFER OFFSET field, and PARAMETER LIST LENGTH field are vendor specific.
6.49.7 Download microcode with offsets and activate mode (06h)
In this mode, microcode shall be transferred to the device server using one or more WRITE BUFFER
commands and activated (see 5.4).
The MODE SPECIFIC field is reserved.
The BUFFER ID field specifies a buffer within the logical unit. The vendor assigns buffer ID codes to buffers
within the logical unit. A buffer ID value of zero shall be supported. If more than one buffer is supported, then
additional buffer ID codes shall be assigned contiguously, beginning with one. If an unsupported buffer ID
code is specified, the command shall be terminated with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The BUFFER OFFSET field specifies the location in the buffer to which the microcode is written. The application
client shall send commands that conform to the offset boundary requirements returned in the READ BUFFER
descriptor (see 6.18.5). If the device server is unable to process the specified buffer offset, the command shall
be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
The PARAMETER LIST LENGTH field specifies the maximum number of bytes that shall be present in the
Data-Out Buffer to be stored in the specified buffer beginning at the buffer offset. The application client should
ensure that the parameter list length plus the buffer offset does not exceed the capacity of the specified buffer.
If the BUFFER OFFSET and PARAMETER LIST LENGTH fields specify a transfer in excess of the buffer capacity, then
the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.49.8 Download microcode with offsets, save, and activate mode (07h)
In this mode, microcode shall be transferred to the device server using one or more WRITE BUFFER
commands, saved to nonvolatile storage, and activated (see 5.4) based on the setting of the ACTIVATE
MICROCODE field in the Extended INQUIRY VPD page (see 7.8.7).
The BUFFER ID field, BUFFER OFFSET field, and PARAMETER LIST LENGTH field are defined in the download
microcode with offsets mode (see 6.49.7).
6.49.9 Write data to echo buffer mode (0Ah)
In this mode the device server transfers data from the application client and stores it in an echo buffer. An
echo buffer is assigned in the same manner by the device server as it would for a write operation. Data shall
be sent aligned on four-byte boundaries.


The BUFFER ID and BUFFER OFFSET fields shall be ignored in this mode.
NOTE 43 - It is recommended that the logical unit assign echo buffers on a per I_T nexus basis to limit the
number of exception conditions that may occur when I_T nexuses are present.
Upon successful completion of a WRITE BUFFER command the data shall be preserved in the echo buffer
unless there is an intervening command to any logical unit in which case the data may be changed.
The PARAMETER LIST LENGTH field specifies the maximum number of bytes that shall be transferred from the
Data-Out Buffer to be stored in the echo buffer. The application client should ensure that the parameter list
length does not exceed the capacity of the echo buffer. The capacity of the echo buffer is indicated by the
BUFFER CAPACITY field in the READ BUFFER echo buffer descriptor (see 6.18.7). If the PARAMETER LIST
LENGTH field specifies a transfer in excess of the buffer capacity, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN CDB.
6.49.10 Download microcode with offsets, select activation, save, and defer activate mode (0Dh)
In this mode, microcode shall be transferred to the device server using one or more WRITE BUFFER
commands, saved to nonvolatile storage, and considered deferred (see 5.4). The deferred microcode shall be
activated and no longer considered deferred if a WRITE BUFFER command with the activate deferred
microcode mode (0Fh) is processed (see 6.49.12).
The MODE SPECIFIC field (see table 339) specifies additional events that shall be used to activate the deferred
microcode.
If the power on activate (PO_ACT) bit is set to one, then deferred microcode shall be activated and no longer
considered deferred if a power on occurs. If the PO_ACT bit is set to zero, then deferred microcode shall not be
activated if a power on occurs.
If the hard reset activate (HR_ACT) bit is set to one, then deferred microcode shall be activated and no longer
considered deferred if a hard reset occurs. If the HR_ACT bit is set to zero, then deferred microcode shall not
be activated if a hard reset occurs.
If the vendor specific event activate (VSE_ACT) bit is set to one, then deferred microcode shall be activated and
no longer considered deferred if a vendor specific event occurs. If the VSE_ACT bit is set to zero, then deferred
microcode shall not be activated if a vendor specific event occurs.
The supported activation events shall be reported in the POA_SUP bit, HRA_SUP bit, and VSA_SUP bit in the
Extended INQUIRY VPD page (see 7.8.7). If the MODE SPECIFIC field specifies an activation event that is not
supported (e.g., if the PO_ACT bit is set to one and the POA_SUP bit is set to zero), then the command shall be
terminated with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN CDB.
The BUFFER ID field, BUFFER OFFSET field, and PARAMETER LIST LENGTH field are defined in the download
microcode with offsets mode (see 6.49.7).
Table 339 — MODE SPECIFIC field
Bit
…
PO_ACT
HR_ACT
VSE_ACT
…


6.49.11 Download microcode with offsets, save, and defer activate mode (0Eh)
In this mode, microcode shall be transferred to the device server using one or more WRITE BUFFER
commands, saved to nonvolatile storage, and considered deferred (see 5.4).
The deferred microcode shall be activated and no longer considered deferred if any one of the following
occurs:
a)
a power on;
b)
a hard reset;
c)
a START STOP UNIT command is processed (see SBC-3);
d)
a FORMAT UNIT command is processed (see SBC-3); or
e)
a WRITE BUFFER command with the activate deferred microcode mode (0Fh) is processed (see
6.49.12).
The MODE SPECIFIC field, BUFFER ID field, BUFFER OFFSET field, and PARAMETER LIST LENGTH field are defined in
the download microcode with offsets mode (see 6.49.7).
6.49.12 Activate deferred microcode mode (0Fh)
In this mode, deferred microcode, if any, that has been saved using one of the modes list in this subclause
shall be activated and no longer considered deferred (see 5.4). The modes that save deferred microcode are
the:
a)
download microcode with offsets, select activation events, save, and defer activate mode (0Dh) (see
6.49.10); and
b)
download microcode with offsets, save, and defer activate mode (0Eh) (see 6.49.11).
The MODE SPECIFIC field is reserved.
The the BUFFER ID field, the BUFFER OFFSET field, and PARAMETER LIST LENGTH field shall be ignored in this
mode.
If there is no deferred microcode that has been saved using one of the modes list in this subclause, then the
WRITE BUFFER command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to COMMAND SEQUENCE ERROR.
6.49.13 Enable expander communications protocol and Echo buffer mode (1Ah)
Receipt of a WRITE BUFFER command with this mode causes a communicative expander (see SPI-5) to
enter the expanded communications protocol mode.
The MODE SPECIFIC field is reserved.
Device servers in SCSI target devices that receive a WRITE BUFFER command with this mode shall process
it as if it were a WRITE BUFFER command with the write data to Echo buffer mode (see 6.49.9).
6.49.14 Disable expander communications protocol mode (1Bh)
Receipt of a WRITE BUFFER command with this mode causes a communicative expander (see SPI-5) to exit
the expanded communications protocol mode and return to simple expander operation.
