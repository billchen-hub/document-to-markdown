# 6.18.9 Error history mode (1Ch)

An echo buffer overwritten supported (EBOS) bit set to one indicates either:
a)
the device server returns the ECHO BUFFER OVERWRITTEN additional sense code if the data
being read from the echo buffer is not the data previously written by the same I_T nexus, or
b)
the device server ensures echo buffer data returned to each I_T nexus is the same as that previously
written by that I_T nexus.
An EBOS bit set to zero specifies that the echo buffer may be overwritten by any intervening command
received on any I_T nexus.
A READ BUFFER command with the mode set to echo buffer descriptor may be used to determine the echo
buffer capacity and supported features before a WRITE BUFFER command with the mode set to write data to
echo buffer (see 6.49.9) is sent.
6.18.8 Enable expander communications protocol and Echo buffer (1Ah)
Receipt of a READ BUFFER command with this mode (1Ah) causes a communicative expander (see SPI-5)
to enter the expanded communications protocol mode. Device servers in SCSI target devices that receive a
READ BUFFER command with this mode shall process it as if it were a READ BUFFER command with mode
0Ah (see 6.18.6).
6.18.9 Error history mode (1Ch)
6.18.9.1 Error history overview
This mode is used to manage and retrieve error history (see 5.5).
If the device server is unable to process a READ BUFFER command with the MODE field set to 1Ch because of
a vendor specific condition, then the device server shall terminate the READ BUFFER command with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
COMMAND SEQUENCE ERROR.


The BUFFER ID field (see table 231) specifies the action that the device server shall perform, and the parameter
data, if any, that the device server shall return.
The command shall be terminated with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to OPERATION IN PROGRESS if the device server receives a
READ BUFFER command:
a)
with the MODE field set to 1Ch;
b)
with the BUFFER ID field set to a value that table 231 shows as constrained by error history I_T nexus;
c)
if an error history I_T nexus exists and the command is received from an I_T nexus that is different
than that I_T nexus; and
d)
an error history snapshot exists.
The BUFFER OFFSET field specifies the byte offset from the start of the buffer specified by the BUFFER ID field
from which the device server shall return data. The application client should conform to the offset boundary
requirements indicated in the READ BUFFER descriptor (see 6.18.5). If the buffer offset is not one of those
shown in table 231 or the device server is unable to accept the specified buffer offset, then the device server
shall terminate the READ BUFFER command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.18.9.2 Error history directory
Whenever allowed by established error history I_T nexus constraints (see 6.18.9.1), if any, all error history
device server actions return an error history directory (see table 233). Some error history device server
Table 231 — Error history BUFFER ID field
Code
Description
Buffer
offset
Error history
I_T nexus
constrained
Reference
00h
Return error history directory
0000h
Yes
6.18.9.2
01h
Return error history directory and create
new error history snapshot
0000h
Yes
6.18.9.2
02h
Return error history directory and
establish new error history I_T nexus
0000h
No
6.18.9.2
03h
Return error history directory, establish
new error history I_T nexus, and create
new error history snapshot
0000h
No
6.18.9.2
04h to 0Fh
Reserved
Yes
10h to EFh
Return error history
0000h to
FFFFh
Yes
6.18.9.3
F0h to FDh
Reserved
Yes
FEh
Clear error history I_T nexus
Ignored
Yes
6.18.9.4
FFh
Clear error history I_T nexus and release
error history snapshot
Ignored
Yes
6.18.9.5


actions also discard the existing error history snapshot and create a new error history snapshot (see table
232).
The error history directory is defined in table 233.
The T10 VENDOR IDENTIFICATION field contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying the
manufacturer of the logical unit. The T10 vendor identification shall be one assigned by INCITS. A list of
assigned T10 vendor identifications is in Annex F and on the T10 web site (http://www.t10.org).
Table 232 —  Summary of error history directory device server actions
BUFFER ID
field
Establish new
error history
I_T nexus
Error history snapshot
Preserved
(if exists)
Created
00h
No a
Yes
No b
01h
No a
No
Yes
02h
Yes
Yes
No b
03h
Yes
No
Yes
a If no error history I_T nexus is established, a new one is established.
b If no error history snapshot exists, a new one is created.
Table 233 — Error history directory
Bit
Byte
(MSB)
T10 VENDOR IDENTIFICATION

•••
(LSB)
VERSION
Reserved
EHS_RETRIEVED
EHS_SOURCE
CLR_SUP
Reserved

•••
(MSB)
DIRECTORY LENGTH (n-31)
(LSB)
Error history directory list
Error history directory entry [first]
(see table 236)

•••
•••
n-7
Error history directory entry [last]
(see table 236)
•••
n


NOTE 37 - The T10 VENDOR IDENTIFICATION field may contain a different value than the VENDOR IDENTIFICATION
field in the standard INQUIRY data (see 6.6.2) (e.g., this field may indicate a disk drive component vendor
while the standard INQUIRY data indicates the original equipment manufacturer).
The VERSION field indicates the version and format of the vendor specific error history. The VERSION field is
assigned by the vendor indicated in the T10 VENDOR IDENTIFICATION field.
The error history retrieved (EHS_RETRIEVED) field (see table 234) indicates whether a clear error history device
server action has been requested for the error history snapshot. EHS_RETRIEVED field shall be set to 00b or
10b when the error history snapshot is created.
The error history source (EHS_SOURCE) field (see table 235) indicates the source of the error history snapshot.
A clear support (CLR_SUP) bit set to one indicates that the CLR bit is supported in the WRITE BUFFER
command download error history mode (see 6.49.15). A CLR_SUP bit set to zero indicates that the CLR bit is
not supported.
The DIRECTORY LENGTH field indicates the number of bytes that follow in the error history directory list. This
value shall not be altered even if the allocation length is not sufficient to transfer the entire error history
directory list.
Table 234 — EHS_RETRIEVED field
Code
Description
00b
No information
01b
The error history I_T nexus has requested buffer ID FEh (i.e., clear
error history I_T nexus) or buffer ID FFh (i.e., clear error history I_T
nexus and release snapshot) for the current error history snapshot.
10b
An error history I_T nexus has not requested buffer ID FEh (i.e., clear
error history I_T nexus) or buffer ID FFh (i.e., clear error history I_T
nexus and release snapshot) for the current error history snapshot.
11b
Reserved
Table 235 — EHS_SOURCE field
Code
Description
00b
The error history snapshot was created by the device server and was not created due to
processing a READ BUFFER command.
01b
Error history snapshot was created due to processing of the current READ BUFFER command
10b
Error history snapshot was created due to processing of a previous READ BUFFER command
11b
Reserved


The error history directory list contains an error history directory entry (see table 236) for each supported
buffer ID in the range of 00h to EFh. The first entry shall be for buffer ID 00h and the entries shall be in order
of ascending buffer IDs. The supported buffer IDs are not required to be contiguous. There shall not be any
entries for buffer IDs greater than or equal to F0h.
The SUPPORTED BUFFER ID field indicates the error history buffer ID associated with this entry.
The MAXIMUM AVAILABLE LENGTH field indicates the maximum number of data bytes contained in the buffer
indicated by the SUPPORTED BUFFER ID field. The actual number of bytes available for transfer may be smaller.
6.18.9.3 Error history data buffer
Unless an error is encountered, the device server shall return parameter data that contains error history in a
vendor specific format from the error history snapshot from the specified buffer at the specified buffer offset.
If the device server receives a READ BUFFER command with the MODE field set to 1Ch from the established
error history I_T nexus and the BUFFER ID field is set to a value that the error history directory (see 6.18.9.2)
shows as not supported, then the command shall be terminated with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If the value in the BUFFER OFFSET field is not supported, the command shall be terminated with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
INVALID FIELD IN CDB.
The amount of error history in the specified buffer shall be less than or equal to the number of bytes indicated
by the MAXIMUM AVAILABLE LENGTH field in the error history directory (see 6.18.9.2).
6.18.9.4 Clear error history I_T nexus
If the BUFFER ID field is set to FEh, the device server shall:
a)
clear the error history I_T nexus, if any; and
b)
not transfer any data.
6.18.9.5 Clear error history I_T nexus and release snapshot
If the BUFFER ID field is set to FFh, the device server shall:
a)
clear the error history I_T nexus, if any,
b)
release the error history snapshot, if any; and
Table 236 — Error history directory entry
Bit
Byte
SUPPORTED BUFFER ID
Reserved

•••
(MSB)
MAXIMUM AVAILABLE LENGTH

•••
(LSB)


c)
not transfer any data.
6.19 READ MEDIA SERIAL NUMBER command
The READ MEDIA SERIAL NUMBER command (see table 237) reports the media serial number reported by
the device and the currently mounted media. This command uses the SERVICE ACTION IN(12) CDB format
(see 4.2.2.3.5).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 237 for the READ MEDIA
SERIAL NUMBER command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 237 for the READ MEDIA
SERIAL NUMBER command.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
The READ MEDIA SERIAL NUMBER parameter data format is shown in table 238.
Table 237 — READ MEDIA SERIAL NUMBER command
Bit
Byte
OPERATION CODE (ABh)
Reserved
SERVICE ACTION (01h)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
Table 238 — READ MEDIA SERIAL NUMBER parameter data format
Bit
Byte
(MSB)
MEDIA SERIAL NUMBER LENGTH (4n-4)
•••
(LSB)
MEDIA SERIAL NUMBER
•••
4n-1


The MEDIA SERIAL NUMBER LENGTH field shall contain the number of bytes in the MEDIA SERIAL NUMBER field.
The media serial number length shall be a multiple of four. The contents of the MEDIA SERIAL NUMBER LENGTH
field are not altered based on the allocation length (see 4.2.5.6).
The MEDIA SERIAL NUMBER field shall contain the vendor specific serial number of the media currently installed.
If the number of bytes in the vendor specific serial number is not a multiple of four, then up to three bytes
containing zero shall be appended to the highest numbered bytes of the MEDIA SERIAL NUMBER field.
If the media serial number is not available (e.g., the currently installed media has no valid media serial
number), zero shall be returned in the MEDIA SERIAL NUMBER LENGTH field.
If the media serial number is not accessible because there is no media present, the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to NOT READY, and the additional sense code
set to MEDIUM NOT PRESENT.
6.20 RECEIVE COPY DATA(LID4) command
The RECEIVE COPY DATA(LID4) command (see table 239) is a third-party copy command (see 5.17.3) that
returns the held data (see 5.17.4.5), if any, for the copy operation (see 5.17.4.3) specified by the LIST
IDENTIFIER field (see 5.17.4.2) in the CDB. If no copy operation known to the copy manager has a matching list
identifier, then the RECEIVE COPY DATA(LID4) command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
CDB.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 239 for the RECEIVE COPY
DATA(LID4) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 239 for the RECEIVE COPY
DATA(LID4) command.
Table 239 — RECEIVE COPY DATA(LID4) command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (06h)
(MSB)
LIST IDENTIFIER

•••
(LSB)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The LIST IDENTIFIER field is defined in 5.17.4.2 and 6.4.3.2, and specifies the copy operation (see 5.17.4.3)
about which information is to be transferred. The receive command shall return information from the copy
operation that was received on the same I_T nexus with a list identifier that matches the list identifier specified
in the RECEIVE COPY RESULTS CDB.
The ALLOCATION LENGTH field is defined in 4.2.5.6. The actual length of the parameter data is available in the
AVAILABLE DATA field in the parameter data.
The CONTROL byte is defined in SAM-5.


Table 240 shows the format of the parameter data returned by the copy manager in response to the RECEIVE
COPY DATA(LID4) command.
After the completion of a copy operation (see 5.17.4.3), the copy manager shall preserve all held data as
described in 5.17.4.5. The application client should issue a RECEIVE COPY DATA(LID4) command as soon
as possible following completion of the copy operation to ensure that the data is not discarded by the copy
manager.
Table 240 — Parameter data for the RECEIVE COPY DATA(LID4) command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)

•••
(LSB)
Reserved
RESPONSE TO SERVICE ACTION
HDD
COPY OPERATION STATUS
(MSB)
OPERATION COUNTER
(LSB)
(MSB)
ESTIMATED STATUS UPDATE DELAY

•••
(LSB)
EXTENDED COPY COMPLETION STATUS
LENGTH OF THE SENSE DATA FIELD (X-31)
SENSE DATA LENGTH
TRANSFER COUNT UNITS
(MSB)
TRANSFER COUNT

•••
(LSB)
(MSB)
SEGMENTS PROCESSED
(LSB)
Reserved

•••
SENSE DATA
•••
x
x+1
(MSB)
HELD DATA LENGTH (n-(x+4))

•••
x+4
(LSB)
x+5
HELD DATA
•••
n


The copy manager shall not discard the data returned by a RECEIVE COPY DATA(LID4) command in
response to an ABORT TASK task management function (see SAM-5) or a COPY OPERATION ABORT
command (see 6.3).
The AVAILABLE DATA field, RESPONSE TO SERVICE ACTION field, COPY OPERATION STATUS field, OPERATION
COUNTER field, ESTIMATED STATUS UPDATE DELAY field, EXTENDED COPY COMPLETION STATUS field, LENGTH OF
THE SENSE DATA FIELD field, SENSE DATA LENGTH field, TRANSFER COUNT UNITS field, TRANSFER COUNT field,
SEGMENTS PROCESSED field, and SENSE DATA field are defined in 6.24.
The held data discarded (HDD) bit indicates whether held data has been discarded as described in 5.17.4.5.
If the COPY OPERATION STATUS field is set to a value that table 249 (see 6.24) describes as meaning the
operation completed without errors, then the HELD DATA LENGTH field indicates the number of bytes that follow
in the HELD DATA field. If the COPY OPERATION STATUS field is not set to a value that table 249 describes as
meaning the operation completed without errors, then the HELD DATA LENGTH field shall be set to zero.
The HELD DATA field contains the held data (see 5.17.4.5) for the copy operation (see 5.17.4.3) specified by the
list identifier in the CDB (see 5.17.4.2). Unless the copy manager’s held data limit (see 5.17.4.5) is exceeded,
the first byte held (i.e., the oldest byte held) in response to the copy operation (e.g., the first segment
descriptor in the EXTENDED COPY parameter list prescribing the holding of data) is returned in the first byte
in the HELD DATA field. The last byte held (i.e., the newest byte held) in response to the copy operation (e.g.,
the last segment descriptor in the EXTENDED COPY parameter list prescribing the holding of data) is
returned in the last byte in the HELD DATA field.


6.21 RECEIVE COPY DATA(LID1) command
The RECEIVE COPY DATA(LID1) command (see table 241) is an SPC-3 compatible third-party copy
command (see 5.17.3) that returns the held data (see 5.17.4.5), if any, for the copy operation (see 5.17.4.3)
specified by the LIST IDENTIFIER field (see 5.17.4.2) in the CDB. The RECEIVE COPY DATA(LID1) command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB if:
a)
no copy operation known to the copy manager has a list identifier that matches the LIST IDENTIFIER
field in the CDB; or
b)
if the LIST IDENTIFIER field in the CDB specifies a copy operation that still is being processed by the
copy manager.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 241 for the RECEIVE COPY
DATA(LID1) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 241 for the RECEIVE COPY
DATA(LID1) command.
The LIST IDENTIFIER field and ALLOCATION LENGTH field are defined in 6.20.
The CONTROL byte is defined in SAM-5.
Table 241 — RECEIVE COPY DATA(LID1) command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (01h)
LIST IDENTIFIER
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


Table 242 shows the format of the parameter data returned by the copy manager in response to the RECEIVE
COPY DATA(LID1) command.
After the completion of a copy operation (see 5.17.4.3), the copy manager shall preserve all held data as
described in 5.17.4.5.
The AVAILABLE DATA field shall contain the number of bytes of held data that follow. The contents of the
AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
The HELD DATA field is defined in 6.20.
6.22 RECEIVE COPY OPERATING PARAMETERS command
The RECEIVE COPY OPERATING PARAMETERS command (see table 243) is an SPC-3 compatible
third-party copy command (see 5.17.3) that returns the operating parameters for the EXTENDED COPY
command. The Third-party Copy VPD page (see 7.8.17) provides the same information as the RECEIVE
COPY OPERATING PARAMETERS command and additional copy manager support information.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 243 for the RECEIVE COPY
OPERATING PARAMETERS command.
Table 242 — Parameter data for the RECEIVE COPY DATA(LID1) command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)
•••
(LSB)
HELD DATA
•••
n
Table 243 — RECEIVE COPY OPERATING PARAMETERS command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (03h)
Reserved

•••

(MSB)
ALLOCATION LENGTH

•••

(LSB)
Reserved
CONTROL


The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 243 for the RECEIVE COPY
OPERATING PARAMETERS command.
The CONTROL byte is defined in SAM-5.
Table 244 shows the format of the parameter data returned by the RECEIVE COPY OPERATING PARAM-
ETERS command. If the Third-party Copy VPD page (see 7.8.17) is supported, the values in the RECEIVE
COPY OPERATING PARAMETERS parameter data fields shall be the same as the values in the equivalent
fields in the Third-party Copy VPD page.
Table 244 — Parameter data for the RECEIVE COPY OPERATING PARAMETERS command (part 1 of 2)
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)
•••
(LSB)
Reserved
SNLID
Reserved
(MSB)
MAXIMUM CSCD DESCRIPTOR COUNT
(LSB)
(MSB)
MAXIMUM SEGMENT DESCRIPTOR COUNT
(LSB)
(MSB)
MAXIMUM DESCRIPTOR LIST LENGTH
•••
(LSB)
(MSB)
MAXIMUM SEGMENT LENGTH
•••
(LSB)
(MSB)
MAXIMUM INLINE DATA LENGTH
•••
(LSB)
(MSB)
HELD DATA LIMIT
•••
(LSB)
(MSB)
MAXIMUM STREAM DEVICE TRANSFER SIZE
•••
(LSB)
Reserved


The AVAILABLE DATA field shall contain the number of bytes following the AVAILABLE DATA field in the parameter
data. The contents of the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
A supports no list identifier (SNLID) bit set to one indicates the copy manager supports an EXTENDED COPY
command parameter list in which the LIST ID USAGE field is set to 11b and the LIST IDENTIFIER field is set to zero
as described in 6.4.3.2. A SNLID bit set to zero indicates the copy manager does not support an EXTENDED
COPY command parameter list (see 5.17.7.1) in which the LIST ID USAGE field is set to 11b.
The MAXIMUM CSCD DESCRIPTOR COUNT field indicates the maximum number of CSCD descriptors that the
copy manager allows in an EXTENDED COPY command parameter list (see 5.17.7.1).
The MAXIMUM SEGMENT COUNT field indicates the maximum number of segment descriptors that the copy
manager allows in an EXTENDED COPY command parameter list (see 5.17.7.1).
The MAXIMUM DESCRIPTOR LIST LENGTH field indicates the maximum length, in bytes, of the CSCD descriptor
list and segment descriptor list that the copy manager allows in an EXTENDED COPY command parameter
list (see 5.17.7.1).
The MAXIMUM SEGMENT LENGTH field indicates the length, in bytes, of the largest amount of data that the copy
manager supports writing via a single segment. Bytes introduced as a result of the PAD bit being set to one
(see 5.17.7.2) are not counted towards this limit. A value of zero indicates that the copy manager places no
limits on the amount of data written by a single segment.
The MAXIMUM INLINE DATA LENGTH field indicates the length, in bytes, of the largest amount of inline data (see
6.4.3.6) that the copy manager supports in an EXTENDED COPY parameter list (see 5.17.7.1). The MAXIMUM
INLINE DATA LENGTH field shall be set to zero if the copy manager does not support descriptor type code 04h
(see 6.4.6.6).
The HELD DATA LIMIT field indicates the length, in bytes, of the minimum amount of data the copy manager
shall hold for return to the application client as described in 5.17.4.5.
(MSB)
TOTAL CONCURRENT COPIES
(LSB)
MAXIMUM CONCURRENT COPIES
DATA SEGMENT GRANULARITY (log 2)
INLINE DATA GRANULARITY (log 2)
HELD DATA GRANULARITY (log 2)
Reserved
IMPLEMENTED DESCRIPTOR LIST LENGTH (n-43)
List of implemented descriptor type codes
(ordered)
•••
n
Table 244 — Parameter data for the RECEIVE COPY OPERATING PARAMETERS command (part 2 of 2)
Bit
Byte


If the SNLID bit is set to one, the TOTAL CONCURRENT COPIES field indicates the maximum number of
EXTENDED COPY commands with the LIST ID USAGE field set to 00b, 10b, or 11b that are supported for
concurrent processing by the copy manager. If the SNLID bit is set to zero, then the TOTAL CONCURRENT COPIES
field shall be set to zero.
The MAXIMUM CONCURRENT COPIES field indicates the maximum number of EXTENDED COPY commands with
the LIST ID USAGE field set to 00b or 10b that are supported for concurrent processing by the copy manager. If
the SNLID bit is set to one, then the contents of the TOTAL CONCURRENT COPIES field shall be greater than or
equal to the contents of the MAXIMUM CONCURRENT COPIES field.
Each EXTENDED COPY command with the LIST ID USAGE field set to 00b or 10b reduces the number of
EXTENDED COPY commands with the LIST ID USAGE field set to 11b that may be processed concurrently.
However, the converse may not be true (e.g. when the number of outstanding EXTENDED COPY commands
with the LIST ID USAGE field set to 11b exceeds the difference between the total concurrent copies and
maximum concurrent copies).
The DATA SEGMENT GRANULARITY field indicates the length of the smallest data block that the copy manager
permits in a non-inline segment descriptor (i.e., segment descriptors with type codes other than 04h). The
amount of data transferred by a single segment descriptor shall be a multiple of the granularity. The DATA
SEGMENT GRANULARITY value is expressed as a power of two. Bytes introduced as a result of the PAD bit being
set to one (see 5.17.7.2) are not counted towards the data length granularity.
The INLINE DATA GRANULARITY field indicates the length of the of the smallest block of inline data that the copy
manager permits being written by a segment descriptor containing the 04h descriptor type code (see 6.4.6.6).
The amount of inline data written by a single segment descriptor shall be a multiple of the granularity. The
INLINE DATA GRANULARITY value is expressed as a power of two. Bytes introduced as a result of the PAD bit
being set to one (see 5.17.7.2) are not counted towards the length granularity.
If the copy manager encounters a data or inline segment descriptor that violates either the data segment
granularity or the inline data granularity, the copy operation (see 5.17.4.3) originated by the EXTENDED
COPY command shall be terminated with CHECK CONDITION status, with the sense key set to COPY
ABORTED, and the additional sense code set to COPY SEGMENT GRANULARITY VIOLATION.
The HELD DATA GRANULARITY field indicates the length of the smallest block of held data (see 5.17.4.5) that the
copy manager shall transfer to the application client in response to a RECEIVE COPY DATA(LID4) command
(see 6.20) or a RECEIVE COPY DATA(LID1) command (see 6.21). The amount of data held by the copy
manager in response to any one function (e.g., one segment descriptor (see 6.4.6)) in a copy operation (see
5.17.4.3) shall be a multiple of this granularity. The HELD DATA GRANULARITY value is expressed as a power of
two.
The MAXIMUM STREAM DEVICE TRANSFER SIZE field indicates the maximum transfer size, in bytes, supported for
stream devices.
The IMPLEMENTED DESCRIPTOR LIST LENGTH field indicates the length, in bytes, of the list of implemented
descriptor type codes.
The list of implemented descriptor type codes contains one byte for each segment or CSCD DESCRIPTOR TYPE
CODE value (see 6.4.5) supported by the copy manager, with a unique supported DESCRIPTOR TYPE CODE value
in each byte. The DESCRIPTOR TYPE CODE values shall appear in the list in ascending numerical order.


6.23 RECEIVE COPY FAILURE DETAILS(LID1) command
The RECEIVE COPY FAILURE DETAILS(LID1) command (see table 245) is an SPC-3 compatible third-party
copy command (see 5.17.3) that returns details of the segment processing failure, if any, that caused termi-
nation of the EXTENDED COPY(LID1) command specified by the LIST IDENTIFIER field in the CDB. The
RECEIVE COPY FAILURE DETAILS(LID1) command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB if:
a)
no EXTENDED COPY(LID1) command known to the copy manager has a list identifier that matches
the LIST IDENTIFIER field in the CDB; or
b)
if the LIST IDENTIFIER field in the CDB specifies an EXTENDED COPY(LID1) command that still is
being processed by the copy manager.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 245 for the RECEIVE COPY
FAILURE DETAILS(LID1) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 245 for the RECEIVE COPY
FAILURE DETAILS(LID1) command.
The LIST IDENTIFIER field and ALLOCATION LENGTH field are defined in 6.20.
The CONTROL byte is defined in SAM-5.
Table 245 — RECEIVE COPY FAILURE DETAILS(LID1) command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (04h)
LIST IDENTIFIER
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


Table 246 shows the format of the parameter data returned by the RECEIVE COPY FAILURE DETAILS(LID1)
command.
If processing of an EXTENDED COPY(LID1) command is aborted and processing of a segment descriptor is
incomplete, then the copy manager shall preserve details about the progress in processing of that descriptor.
These details enable the application client to obtain information it needs to determine the state in which
CSCDs (e.g., stream devices) have been left by incomplete processing.
The application client should issue a RECEIVE COPY FAILURE DETAILS(LID1) command as soon as
possible after the failure of the EXTENDED COPY(LID1) command to ensure that the information is not
discarded by the copy manager. The copy manager shall discard the failed segment details:
a)
after all failed segment details held for a specific EXTENDED COPY(LID1) command have been
successfully transferred to the application client;
b)
if a RECEIVE COPY FAILURE DETAILS(LID1) command has been received on the same I_T nexus
with a matching list identifier, with the ALLOCATION LENGTH field set to zero;
c)
if another EXTENDED COPY(LID1) command is received on the same I_T nexus using the same list
identifier;
d)
if the copy manager detects a logical unit reset condition or I_T nexus loss condition (see SAM-5); or
e)
if the copy manager requires the resources used to preserve the data.
The AVAILABLE DATA field shall contain the number of bytes of failed segment details that follow. If no failed
segment details data is available for the specified list identifier then the AVAILABLE DATA field shall be set to
zero and no data beyond the AVAILABLE DATA field shall be transferred. The contents of the AVAILABLE DATA
field are not altered based on the allocation length (see 4.2.5.6).
The COPY COMMAND STATUS field contains the SCSI status value that was returned for the EXTENDED
COPY(LID1) command specified by the LIST IDENTIFIER field in the CDB.
The SENSE DATA LENGTH field indicates how many bytes of sense data are present in the SENSE DATA field.
Table 246 — Parameter data for the RECEIVE COPY FAILURE DETAILS(LID1) command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)
•••
(LSB)
Reserved
•••
EXTENDED COPY COMMAND STATUS
Reserved
(MSB)
SENSE DATA LENGTH (n-59)
(LSB)
SENSE DATA
•••
n


The SENSE DATA field contains a copy of the sense data that the copy manager prepared as part of terminating
the EXTENDED COPY(LID1) command indicated by the list identifier with CHECK CONDITION status.
6.24 RECEIVE COPY STATUS(LID4) command
The RECEIVE COPY STATUS(LID4) command (see table 247) is a third-party copy command (see 5.17.3)
that returns the held data (see 5.17.4.5), if any, for the copy operation (see 5.17.4.3) specified by the LIST
IDENTIFIER field (see 5.17.4.2) in the CDB. If no copy operation known to the copy manager has a matching list
identifier, then the RECEIVE COPY STATUS(LID4) command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
CDB.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 247 for the RECEIVE COPY
STATUS(LID4) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 247 for the RECEIVE COPY
STATUS(LID4) command.
The LIST IDENTIFIER field and ALLOCATION LENGTH field are defined in 6.20.
The CONTROL byte is defined in SAM-5.
Table 247 — RECEIVE COPY STATUS(LID4) command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (05h)
(MSB)
LIST IDENTIFIER

•••
(LSB)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


Table 248 shows the format of the parameter data returned by the copy manager in response to the RECEIVE
COPY STATUS(LID4) command.
The data returned by a RECEIVE COPY STATUS(LID4) command shall be available at any time the copy
operation (see 5.17.4.3) is in progress (i.e., whenever the COPY OPERATION STATUS field is set to 10h, 11h, or
12h).
After the completion of a copy operation (see 5.17.4.3) (i.e., whenever the COPY OPERATION STATUS field is set
to 01h, 02h, 03h, or 60h), the copy manager shall preserve all data returned by a RECEIVE COPY
STATUS(LID4) command for a vendor specific period of time. The copy manager shall discard the RECEIVE
COPY STATUS(LID4) command parameter data in which the COPY OPERATION STATUS field is set to 01h, 02h,
03h, or 60h if:
a)
another third-party copy command that originates a copy operation (see table 107 in 5.17.3) is
received on the same I_T nexus and the list identifier matches the list identifier associated with the
data preserved for the RECEIVE COPY STATUS(LID4) command;
Table 248 — Parameter data for the RECEIVE COPY STATUS(LID4) command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)

•••
(LSB)
Reserved
RESPONSE TO SERVICE ACTION
Reserved
COPY OPERATION STATUS
(MSB)
OPERATION COUNTER
(LSB)
(MSB)
ESTIMATED STATUS UPDATE DELAY

•••
(LSB)
EXTENDED COPY COMPLETION STATUS
LENGTH OF THE SENSE DATA FIELD (X-31)
SENSE DATA LENGTH
TRANSFER COUNT UNITS
(MSB)
TRANSFER COUNT

•••
(LSB)
(MSB)
SEGMENTS PROCESSED
(LSB)
Reserved

•••
SENSE DATA
•••
x


b)
the copy manager detects a logical unit reset condition or I_T nexus loss condition (see SAM-5); or
c)
the copy manager requires the resources used to preserve the data.
The copy manager may discard the sense data in the RECEIVE COPY STATUS(LID4) command parameter
data in which the COPY OPERATION STATUS field is set to 01h, 02h, 03h, or 60h after that data has been
returned by a RECEIVE COPY STATUS(LID4) command received on the same I_T nexus with a matching list
identifier.
The copy manager shall not discard the data returned by a RECEIVE COPY STATUS(LID4) command in
response to an ABORT TASK task management function (see SAM-5) or a COPY OPERATION ABORT
command (see 6.3).
The AVAILABLE DATA field shall contain the number of bytes that follow in the parameter data. The contents of
the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
The RESPONSE TO SERVICE ACTION field indicates the value in the SERVICE ACTION field of the third-party copy
command (see 5.17.3) specified by the LIST IDENTIFIER field in the CDB.
The COPY OPERATION STATUS field indicates the status of the copy operation (see 5.17.4.3) specified by the
LIST IDENTIFIER field in the CDB as defined in table 249.
The OPERATION COUNTER field contains a wrapping counter of the number of SCSI commands, or equivalent,
that the copy manager has sent to a copy source or copy destination as part of processing the copy operation
(see 5.17.4.3) specified by the LIST IDENTIFIER field in the CDB, and for which the copy manager has received
one of the following completion status values:
a)
GOOD;
Table 249 — COPY OPERATION STATUS field
Code
Meaning
Operation
completed
without errors
01h
Operation completed without errors
Yes
02h
Operation completed with errors
No
03h a
Operation completed without errors but with partial ROD token
usage (see SBC-3)
Yes
04h
Operation completed without errors but with residual data b
Yes
10h
Operation in progress, foreground or background unknown c
No
11h
Operation in progress in foreground (see 5.17.4.3)
No
12h
Operation in progress in background (see 5.17.4.3)
No
60h
Operation terminated (e.g., by the preemption of a persistent
reservation (see 5.9.11.5))
No
all others
Reserved
a If the third-party copy command that originated the copy operation is an EXTENDED COPY
command, the COPY OPERATION STATUS field shall never be set to 03h.
b The copy manager has determined that the application client should verify that all requested
data transfers have been performed.
c Codes 11h and 12h should be used instead of this code whenever possible.


b)
CONDITION MET; or
c)
CHECK CONDITION with the sense key set to RECOVERED ERROR.
The ESTIMATED STATUS UPDATE DELAY field indicates the number of milliseconds that the copy manager recom-
mends that the application client wait before sending another RECEIVE COPY STATUS(LID4) command on
the same I_T nexus with the same list identifier. If a RECEIVE COPY STATUS(LID4) command is received
sooner than the indicated time, the copy manager may return the same parameter data. If the COPY
OPERATION STATUS field is set to 01h, 02h, 03h, 04h, or 60h, then the ESTIMATED STATUS UPDATE DELAY field
shall be set to FFFF FFFEh. If the ESTIMATED STATUS UPDATE DELAY field is set to FFFF FFFFh, then the copy
manager is unable to recommend a delay interval.
If the EXTENDED COPY COMPLETION STATUS field indicates the status code (see SAM-5), if any, established for
the completed copy operation (see 5.17.4.3) specified by the LIST IDENTIFIER field depending on the contents
of the COPY OPERATION STATUS field as shown in table 250. If the IMMED bit, if any, (see 5.17.4.3) is set to one
in the third-party copy command that originated the copy operation, then the contents of the EXTENDED COPY
COMPLETION STATUS field may be different than the status returned by the originating third-party copy
command.
The LENGTH OF THE SENSE DATA FIELD field indicates the number of bytes in the SENSE DATA field. The LENGTH
OF THE SENSE DATA FIELD field shall be set to zero or a multiple of four.
If the COPY OPERATION STATUS field is set to 10h, 11h, 12h, or 60h, then the SENSE DATA LENGTH field shall be
set to zero. If the COPY OPERATION STATUS field is set to 01h, 02h, 03h, or 04h, then the SENSE DATA LENGTH
field indicates the number of bytes in the SENSE DATA field that contain sense data. The value in the SENSE
DATA LENGTH field shall be less than or equal to the value in the LENGTH OF THE SENSE DATA FIELD field (e.g.,
the SENSE DATA field may contain pad bytes that are counted in the LENGTH OF THE SENSE DATA FIELD field but
not in the SENSE DATA LENGTH field).
Table 250 — EXTENDED COPY COMPLETION STATUS field contents based on COPY OPERATION STATUS field
COPY OPERATION
STATUS field contents
EXTENDED COPY COMPLETION STATUS field contents
10h, 11h, or 12h
The EXTENDED COPY COMPLETION STATUS field is reserved.
01h, 02h, 03h, or 04h
The EXTENDED COPY COMPLETION STATUS field indicates the status code estab-
lished for the completed copy operation specified by the LIST IDENTIFIER field.
60h
The EXTENDED COPY COMPLETION STATUS field shall be set to TASK ABORTED
(see SAM-5).


The TRANSFER COUNT UNITS field indicates the units for the TRANSFER COUNT field as shown in table 251.
The TRANSFER COUNT field indicates the amount of data written to a copy destination for the copy operation
(see 5.17.4.3) specified by the LIST IDENTIFIER field in the CDB prior to receiving the RECEIVE COPY
STATUS(LID4) command. If data has been written to the copy destination in an order other than what the
command specified (e.g., if concurrent processing of multiple segment descriptors has resulted in some data
being written out of order), then the TRANSFER COUNT field shall indicate only those bytes that have been
written in strict order conformance with what the command specified.
The SEGMENTS PROCESSED field indicates the number of segments the copy manager has processed for the
copy operation (see 5.17.4.3) specified by the LIST IDENTIFIER field in the CDB including the segment currently
being processed. The SEGMENTS PROCESSED field shall be set to zero if:
a)
the copy manager has not yet begun processing segment descriptors; or
b)
the RESPONSE TO SERVICE ACTION field indicates a third-party copy command that does not support
segment descriptors.
Table 251 — COPY STATUS TRANSFER COUNT UNITS field
Code
Meaning a
Multiplier to convert
TRANSFER COUNT field to bytes
00h
Bytes
01h
Kibibytes
210 or 1024
02h
Mebibytes
03h
Gibibytes
04h
Tebibytes
05h
Pebibytes
06h
Exbibytes
F1h
n/a
block size of copy destination
all others
Reserved
a See 3.5.2.


6.25 RECEIVE COPY STATUS(LID1) command
The RECEIVE COPY STATUS(LID1) command (see table 252) is an SPC-3 compatible third-party copy
command (see 5.17.3) that returns the status information for the copy operation (see 5.17.4.3) specified by
the LIST IDENTIFIER field (see 5.17.4.2) in the CDB. If no copy operation known to the copy manager has a
matching list identifier, then the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 252 for the RECEIVE COPY
STATUS(LID1) command.
The service action field is defined in 4.2.5.2 and shall be set as shown in table 252 for the RECEIVE COPY
STATUS(LID1) command.
The LIST IDENTIFIER field and ALLOCATION LENGTH field are defined in 6.20.
The CONTROL byte is defined in SAM-5.
Table 252 — RECEIVE COPY STATUS(LID1) command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (00h)
LIST IDENTIFIER
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


Table 253 shows the format of the parameter data returned by the copy manager in response to the RECEIVE
COPY STATUS(LID1) command.
After the completion of a copy operation (see 5.17.4.3), the copy manager shall preserve all data returned by
the RECEIVE COPY STATUS(LID1) command for a vendor specific period of time. The copy manager shall
discard the RECEIVE COPY STATUS(LID1) command parameter data if:
a)
a RECEIVE COPY STATUS(LID1) command is received on the same I_T nexus with a matching list
identifier;
b)
another third-party copy command that originates a copy operation (see table 107 in 5.17.3) is
received on the same I_T nexus and the list identifier matches the list identifier associated with the
data preserved for the RECEIVE COPY STATUS(LID1) command;
c)
the copy manager detects a logical unit reset condition or I_T nexus loss condition (see SAM-5); or
d)
the copy manager requires the resources used to preserve the data.
The AVAILABLE DATA field shall contain the number of bytes that follow in the parameter data, and shall be set
as shown in table 253 for the RECEIVE COPY STATUS(LID1) command. The contents of the AVAILABLE DATA
field are not altered based on the allocation length (see 4.2.5.6).
The held data discarded (HDD) bit indicates whether held data has been discarded as described in 5.17.4.5.
The COPY COMMAND STATUS field is set to the current status of the third-party copy command (see 5.17.3)
specified by the LIST IDENTIFIER field in the CDB as defined in table 254.
The SEGMENTS PROCESSED field, TRANSFER COUNT UNITS field, and TRANSFER COUNT field are defined in 6.24.
Table 253 — Parameter data for the RECEIVE COPY STATUS(LID1) command
Bit
Byte
(MSB)
AVAILABLE DATA (00000008h)
•••
(LSB)
HDD
COPY COMMAND STATUS
(MSB)
SEGMENTS PROCESSED
(LSB)
TRANSFER COUNT UNITS
(MSB)
TRANSFER COUNT
•••
(LSB)
Table 254 — COPY COMMAND STATUS field
Code
Meaning
00h
Operation in progress
01h
Operation completed without errors
02h
Operation completed with errors
03h to 7Fh
Reserved


6.26 RECEIVE ROD TOKEN INFORMATION command
The RECEIVE ROD TOKEN INFORMATION command (see table 255) is a third-party copy command (see
5.17.3) that returns all the ROD tokens (see 5.17.6.1) created during the copy operation (see 5.17.4.3)
specified by the LIST IDENTIFIER field (see 5.17.4.2) in the CDB. If no copy operation known to the copy
manager has a matching list identifier, then the RECEIVE ROD TOKEN INFORMATION command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 255 for the RECEIVE ROD
TOKEN INFORMATION command.
The service action field is defined in 4.2.5.2 and shall be set as shown in table 255 for the RECEIVE ROD
TOKEN INFORMATION command.
The LIST IDENTIFIER field and ALLOCATION LENGTH field are defined in 6.20.
The CONTROL byte is defined in SAM-5.
After the completion of a copy operation (see 5.17.4.3), the copy manager shall preserve all created ROD
tokens for a vendor specific period of time. The application client should retrieve the ROD tokens using the
RECEIVE ROD TOKEN INFORMATION command as soon as possible after the completion of the copy
operation to ensure that the data is not discarded by the copy manager. The copy manager shall discard the
parameter data for the created ROD tokens:
a)
after all the ROD tokens created by a specific copy operation (see 5.17.4.3) have been transferred
without errors to the application client;
b)
if a RECEIVE ROD TOKEN INFORMATION command has been received on the same I_T nexus with
a matching list identifier (see 5.17.4.2), with the ALLOCATION LENGTH field set to zero;
c)
if another a third-party command that originates a copy operation (see table 107 in 5.17.3) is received
on the same I_T nexus and the list identifier matches the list identifier associated with the ROD
tokens;
Table 255 — RECEIVE ROD TOKEN INFORMATION command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (07h)
(MSB)
LIST IDENTIFIER

•••
(LSB)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


d)
if the copy manager detects a logical unit reset condition or I_T nexus loss condition (see SAM-5); or
e)
if the copy manager requires the resources used to preserve the data.
The copy manager shall not discard the data returned by a RECEIVE ROD TOKEN INFORMATION command
in response to an ABORT TASK task management function (see SAM-5) or a COPY OPERATION ABORT
command (see 6.3).


Table 256 shows the format of the parameter data returned by the copy manager in response to the RECEIVE
ROD TOKEN INFORMATION command.
Table 256 — Parameter data for the RECEIVE ROD TOKEN INFORMATION command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)

•••

(LSB)
Reserved
RESPONSE TO SERVICE ACTION
Reserved
COPY OPERATION STATUS
(MSB)
OPERATION COUNTER
(LSB)
(MSB)
ESTIMATED STATUS UPDATE DELAY

•••
(LSB)
EXTENDED COPY COMPLETION STATUS
LENGTH OF THE SENSE DATA FIELD (X-31)
SENSE DATA LENGTH
TRANSFER COUNT UNITS
(MSB)
TRANSFER COUNT

•••
(LSB)
(MSB)
SEGMENTS PROCESSED
(LSB)
Reserved

•••

SENSE DATA
•••

x
x+1
ROD TOKEN DESCRIPTORS LENGTH (n-(x+4))

•••
x+4
ROD token descriptors
x+5
ROD token descriptor (see table 257) [first]

•••
•••
ROD token descriptor (see table 257) [last]
•••

n


The AVAILABLE DATA field, RESPONSE TO SERVICE ACTION field, COPY OPERATION STATUS field, OPERATION
COUNTER field, OPERATION COUNTER field, ESTIMATED STATUS UPDATE DELAY field, EXTENDED COPY COMPLETION
STATUS field, LENGTH OF THE SENSE DATA FIELD field, SENSE DATA LENGTH field, TRANSFER COUNT UNITS field,
TRANSFER COUNT field, SEGMENTS PROCESSED field, and SENSE DATA field are defined in 6.24.
If the COPY OPERATION STATUS field is set to a value that table 249 (see 6.24) describes as meaning the
operation completed without errors, then the ROD TOKEN DESCRIPTORS LENGTH field indicates the number of
bytes that follow in ROD token descriptors. If the COPY OPERATION STATUS field is not set to a value that table
249 (see 6.24) describes as meaning the operation completed without errors, then the ROD TOKEN
DESCRIPTORS LENGTH field shall be set to zero.
If the COPY OPERATION STATUS field is set to 01h or 03h, then each ROD token descriptor (see table 257) shall
contain one ROD token created by the copy operation whose service action is indicated by the RESPONSE TO
SERVICE ACTION field.
If the RESPONSE TO SERVICE ACTION field is set to 00h or 01h (i.e., if the ROD tokens being returned were
created by an EXTENDED COPY command), then the ID FOR CREATING ROD CSCD DESCRIPTOR field indicates
the CSCD descriptor ID for the ROD CSCD descriptor in which the R_TOKEN bit was set to one resulting in the
creation of the ROD token contained in the ROD TOKEN field (i.e., the value any segment descriptor that caused
the ROD to be populated had in its DESTINATION CSCD DESCRIPTOR ID field). If the RESPONSE TO SERVICE ACTION
field does not contain 00h or 01h (i.e., if the ROD tokens being returned were created by a command other
than the EXTENDED COPY command), then the ID FOR CREATING ROD CSCD DESCRIPTOR field is reserved.
The ROD TOKEN field contains a ROD token (see 5.17.6.4) created by the copy manager.
Table 257 — ROD token descriptor format
Bit
Byte
(MSB)
ID FOR CREATING ROD CSCD DESCRIPTOR
(LSB)
ROD TOKEN
•••
n
