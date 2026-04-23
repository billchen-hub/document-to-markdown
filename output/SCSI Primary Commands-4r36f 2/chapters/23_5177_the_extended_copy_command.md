# 5.17.7 The EXTENDED COPY command

5.17.7 The EXTENDED COPY command
5.17.7.1 EXTENDED COPY parameter list
The EXTENDED COPY(LID4) command (see 6.4) and EXTENDED COPY(LID1) command (see 6.5) use a
parameter list with several elements to define a flexible interface to third-party copy functions (see figure 18).
EXTENDED COPY parameter list elements that are not used are not included in the parameter list (e.g., the
length of the inline data element is zero if no inline data is referenced).
5.17.7.2 EXTENDED COPY command processing
To process an EXTENDED COPY command, the copy manager:
1)
shall determine the global processing conditions for the command (e.g., the value of the IMMED bit
(see 6.4.2));
2)
shall determine the first parameter list byte for each parameter list element shown in figure 18 (see
5.17.7.1) based on fields in the header;
3)
may validate the contents of one or more CSCD descriptors (see 5.17.7.1) and terminate the
EXTENDED COPY command if errors are detected;
4)
may validate the contents of one or more segment descriptors and terminate the EXTENDED COPY
command if errors are detected;
5)
depending on the value of the IMMED bit, if any, (see 5.17.4.3):
A)
shall return status for the EXTENDED COPY(LID4) command if the IMMED bit is set to one; or
B)
shall not return status for the EXTENDED COPY(LID4) command if the IMMED bit is set to zero;
Figure 18 — EXTENDED COPY parameter list structure diagram
Header
CSCD
descriptors
Segment
descriptors
Inline
data
General information and sizes of
other parameter list elements
Information used to locate and
verify the copy source and copy
destination logical units
Instructions for each copy
function to be performed
Data used by CSCD descriptors
or Segment descriptors,
often large sized fields
Parameter List
Element Descriptions
Allowed References
Parameter List
Elements
Segment descriptors reference
CSCD descriptors to specify
the copy source and copy
destination logical unit
Segment descriptors reference
the inline data to transfer spec-
ified data (e.g., tape labels) to
the copy destination (see
6.4.6.6)
CSCD descriptors reference
the inline data for structures
(e.g., ROD tokens (see
5.17.6)) that do not fit in a
CSCD descriptor
Note: If a small amount of data needs to be transferred from the parameter list to the copy destination,
then the embedded data to stream device operation segment descriptor (see 6.4.6.7) may be more
efficient than referencing the inline data.


and
6)
shall process the segment descriptors in the order in which they appear in the parameter list as
described in this subclause.
The copy functions performed by an EXTENDED COPY command are specified by the segment descriptors.
All other elements of the EXTENDED COPY parameter list (see 5.17.7.1) are present to support the segment
descriptors in their specification of the copy functions to be performed.
If a CSCD descriptor is referenced by a segment descriptor (see 5.17.7.1), the information in that CDCD
descriptor should be validated at the time the referencing segment descriptor is processed. The SCSI devices
participating in a SCSI domain may change between the time that processing of an EXTENDED COPY
command begins and the time that processing of a specific segment descriptor begins.
The copy manager shall perform the copy functions specified by the segment descriptors (see 5.17.7.1). The
specific commands issued by the copy manager to the copy sources and copy destinations while processing
the segment descriptors is vendor specific. Upon completion of the copy operation (see 5.17.4.3) originated
by an EXTENDED COPY command with GOOD status, all copy sources and copy destinations that are
stream devices (see SSC-4) shall be positioned at deterministic locations such that they may be repositioned
to the same location by the application client with appropriate commands.
During processing a segment descriptor, the copy manager may be required to:
a)
manage the movement of data from a copy source to a copy destination as follows:
A)
read source data by issuing data input commands to the copy source;
B)
process data, an activity that generally designates data as destination data intended for transfer
to the copy destination; and
C) write some or all of the destination data to the copy destination;
b)
manage the movement of a specified portion of the embedded data or inline data to a copy desti-
nation as follows:
A)
designate the specified portion of the embedded data or inline data as destination data intended
for transfer to the copy destination; and
B)
write some or all of the destination data to the copy destination;
or
c)
perform functions that are specific to the peripheral device type (e.g., writing filemarks) to a copy
destination.
The number of blocks to read and write, the number of bytes to process, and the nature of processing are
determined by the:
a)
segment descriptor type code;
b)
parameters of the segment descriptor; and
c)
amount of residual source or destination data retained from the previous segment, if any.
Except as otherwise specified by particular segment descriptor type codes, the processing of a segment
descriptor is performed as follows:
a)
just enough whole-block reads shall be performed to supply, together with residual source data from
the previous segment or segments, the number of bytes to be processed;
b)
processing consists of removing bytes from the source data and designating them as destination
data, without change; and
c)
as many whole-block writes as possible shall be performed with the destination data, including any
residual destination data from the previous segment or segments.


Any residual source data from the previous segment or segments shall be processed before any data read
from the copy source during processing of the current segment descriptor. Any residual destination data from
the previous segment or segments shall be written before any data processed during processing of the
current segment descriptor.
Segment descriptor processing requirements that are specific to one or more segment descriptor type codes
are described in table 115 and the referenced subclauses.
Table 115 — Segment descriptor type specific copy manager processing requirements (part 1 of 2)
Segment descriptor type code
Reference
Description
00h (i.e., blockstream) or
0Bh (i.e., blockstream+application
client)
6.4.6.2
The number of bytes processed is determined by
the BLOCK DEVICE NUMBER OF BLOCKS field for the
copy source (see applicable type code definition
subclauses for details). a
02h (i.e., blockblock) or 0Dh (i.e.,
blockblock+application client)
with DC=0
6.4.6.4
02h (i.e., blockblock) or 0Dh (i.e.,
blockblock+application client)
with DC=1
6.4.6.4
The number of blocks or byte range specified shall
be output to the copy destination. If residual desti-
nation data is sufficient to perform the output, then
no data shall be processed. Otherwise, just as
much data as needed shall be processed (which
may involve reading data from the copy source)
so that the destination data (which includes any
residual destination data from the previous
segment) is sufficient. a
01h (i.e., streamblock) or
0Ch (i.e., streamblock+application
client)
6.4.6.3
09h (i.e., streamblock<o>)
6.4.6.11
03h (i.e., streamstream) or
0Eh (i.e., streamstream+application
client)
6.4.6.5
The number of bytes specified in the segment
descriptor shall be processed. a
04h (i.e., inlinestream)
6.4.6.6
The specified number of bytes of inline or
embedded data shall be appended to the desti-
nation data, and no source data shall be processed.
05h (i.e., embeddedstream)
6.4.6.7
06h (i.e., streamdiscard)
6.4.6.8
The specified number of bytes shall be removed
from the source data and discarded.
07h (i.e., verify CSCD operation)
6.4.6.9
No data shall be processed and no reads or writes
shall be performed on CSCDs. Residual source or
destination data, if any, shall be retained or
discarded as if the CAT bit were set to one.
10h (i.e., filemarktape)
6.4.6.13
11h (i.e., spacetape)
6.4.6.14
12h (i.e., locatetape)
6.4.6.15
14h (i.e., register persistent reserva-
tion key)
6.4.6.17
15h (i.e., Third party persistent reser-
vations source I_T nexus)
6.4.6.18
a For segment descriptor type codes 0Bh, 0Ch, 0Dh and 0Eh, a copy of the processed data shall also be
held for retrieval by the application client (see 5.17.4.5).


08h (i.e., block<o>stream)
6.4.6.10
The required blocks shall be read from the copy
source, the designated byte range shall be
extracted as source data, and the designated
number of bytes (starting with residual source data,
if any) shall be processed.
0Ah (i.e., block<o>block<o>)
6.4.6.12
The source byte range specified shall be read into
source data, the number of bytes specified shall be
moved from source data to destination data, and
the specified destination byte range shall be written
using destination data.
0Fh (i.e., streamdiscard+application
client)
6.4.6.8
The specified number of bytes shall be removed
from the source data and held for retrieval by the
application client.
13h (i.e., <i>tape<i>tape)
6.4.6.16
The data movement, if any, shall not involve
processing as described in this subclause. Residual
source or destination data, if any, shall not be used
and shall be retained or discarded as if the CAT bit
were set to one.
16h (i.e., <i>block<i>block)
6.4.6.19
BEh (i.e., RODblock ranges(n))
6.4.6.20
BFh (i.e., RODblock range(1))
6.4.6.21
Table 115 — Segment descriptor type specific copy manager processing requirements (part 2 of 2)
Segment descriptor type code
Reference
Description
a For segment descriptor type codes 0Bh, 0Ch, 0Dh and 0Eh, a copy of the processed data shall also be
held for retrieval by the application client (see 5.17.4.5).


Reads and writes shall be performed using whole-block transfer lengths determined by the block size, transfer
length, or both. Therefore some source data may remain unprocessed and some destination data may not
have been transferred at the end of a segment. If so, the residue shall be handled according to the CAT bit in
the segment descriptor and the PAD bits of the source and destination target descriptors, as defined in table
116.
Table 116 — PAD and CAT bit definitions
PAD bit in
CAT
bit
Copy manager action
Source
CSCD
descriptor
Destination
CSCD
descriptor
0 or 1
0 or 1
Any residual source data shall be retained as source data for a subse-
quent segment descriptor. Any residual destination data shall be
retained as destination data for a subsequent segment descriptor. It
shall not be an error if either the source CSCD ID or destination CSCD
ID index in the subsequent segment descriptor does not match the
corresponding CSCD ID index with which residual data was originally
associated. If the CAT bit is set to one in the last segment descriptor in
the parameter data (see 5.17.7.1), any residual data shall be discarded
and this shall not be considered an error.
Any residual source data shall be discarded. Any residual destination
data shall be padded with zeroes to make a whole block transfer. a
Any residual source data shall be processed as if the CAT bit is set to
one (i.e., discarded on the last segment and retained otherwise). Any
residual destination data shall be padded with zeroes to make a whole
block transfer. a
Any residual source or destination data shall be discarded.
If there is residual source or destination data, the copy operation (see
5.17.4.3) originated by the EXTENDED COPY command shall be termi-
nated with CHECK CONDITION status, with the sense key set to COPY
ABORTED, and the additional sense code set to UNEXPECTED
INEXACT SEGMENT.
a If the CAT bit is set to zero in the segment descriptor and the PAD bit is set to one in the destination
CSCD descriptor, then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY
command shall be terminated with CHECK CONDITION status, with the sense key set to COPY
ABORTED, and the additional sense code set to UNEXPECTED INEXACT SEGMENT if any of the
following conditions are met:
a)
if any residual destination data is present after writing the designated byte range for a segment
descriptor of type 09h (i.e., streamblock <o>) or 0Ah (i.e., block<o>block<o>); or
b)
if any residual destination data is present after the designated number of blocks have been written
for a segment descriptor of type 02h (i.e., blockblock) with DC set to one, 0Dh (i.e., block-
block+application client) with DC set to one, 01h (i.e., streamblock) or 0Ch (i.e.,
streamblock+application client).


Table 117 defines the PAD bit handling for segment descriptors that have either no copy source or no copy
destination.
5.17.7.3 EXTENDED COPY command errors detected before segment descriptor processing starts
Errors may occur during processing of an EXTENDED COPY command before GOOD status is returned
because the IMMED bit is set to one or the first segment descriptor is processed. These errors include CRC or
parity errors while transferring the EXTENDED COPY command, invalid parameters in the CDB or parameter
data, invalid segment descriptors, and inability of the copy manager to continue operating. In the event of such
an exception condition, the copy manager shall:
a)
terminate the EXTENDED COPY command with CHECK CONDITION status;
b)
set the sense key to a value that describes the exception condition (i.e., not COPY ABORTED); and
c)
indicate that the INFORMATION field does not contain valid data by:
A)
setting the VALID bit to zero in the fixed format sense data (see 4.5.3); or
B)
not returning the Information descriptor in the descriptor format sense data (see 4.5.2).
5.17.7.4 EXTENDED COPY command errors detected during processing of segment descriptors
Errors may occur after the copy manager has begun processing segment descriptors or GOOD status has
been returned because the IMMED bit was set to one. These errors include invalid parameters in segment
descriptors, invalid segment descriptors, unavailable CSCDs referenced by CSCD descriptors, inability of the
copy manager to continue operating, and errors reported by a CSCD. If the copy manager receives CHECK
CONDITION status from a CSCD, then it shall recover the sense data associated with the exception condition
and clear any ACA condition associated with the CHECK CONDITION status.
If it is not possible to complete processing of a segment because the copy manager is unable to establish
communications with a CSCD, because the CSCD does not respond to INQUIRY, or because the data
returned in response to INQUIRY indicates an unsupported logical unit, then the copy operation (see 5.17.4.3)
originated by the EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the
sense key set to COPY ABORTED, and the additional sense code set to COPY TARGET DEVICE NOT
REACHABLE.
If it is not possible to complete processing of a segment because the data returned in response to an
INQUIRY command indicates a device type that does not match the type in the CSCD descriptor, then the
copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with
CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INCORRECT COPY TARGET DEVICE TYPE.
If the copy manager has issued a command other than INQUIRY to a CSCD while processing an EXTENDED
COPY command and the CSCD either fails to respond with status or responds with status other than BUSY,
TASK SET FULL, ACA ACTIVE, or RESERVATION CONFLICT, then the condition shall be considered a
CSCD command failure. In response to a CSCD command failure the copy operation (see 5.17.4.3) originated
Table 117 — PAD bit processing if there is no copy source or copy destination
Segment descriptor type code
Reference
Description
04h (i.e., inlinestream)
6.4.6.6
Processing shall be as if the PAD is set to
zero for the source CSCD descriptor.
05h (i.e., embeddedstream)
6.4.6.7
06h (i.e., streamdiscard)
0Fh (i.e., streamdiscard+application client)
6.4.6.8
Processing shall be as if the PAD is set to
zero for the destination CSCD descriptor.


by the EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the sense key
set to COPY ABORTED, and the additional sense code set to THIRD PARTY DEVICE FAILURE.
If a CSCD completes a command from the copy manager with a status of BUSY, TASK SET FULL, ACA
ACTIVE, or RESERVATION CONFLICT, the copy manager shall either retry the command or terminate the
EXTENDED COPY command as a CSCD command failure.
NOTES
The copy manager is assumed to employ a vendor specific retry policy that minimizes time consuming
repetition of retries.
RESERVATION CONFLICT status is listed only to give the copy manager leeway in multi-port cases.
The copy manager may have multiple initiator ports that are capable of reaching a CSCD, and a
persistent reservation may restrict access to a single I_T nexus. The copy manager may need to try
access from multiple initiator ports to find the correct I_T nexus.
If a CSCD responds to an input or output request with a GOOD status but less data than expected is trans-
ferred, then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be termi-
nated with CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional sense
code set to COPY TARGET DEVICE DATA UNDERRUN. If an overrun is detected, then the copy operation
originated by the EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the
sense key set to COPY ABORTED, and the additional sense code set to COPY TARGET DEVICE DATA
OVERRUN.
After an exception condition is detected during segment descriptor processing:
a)
the copy manager shall terminate the copy operation (see 5.17.4.3) originated by the EXTENDED
COPY command with CHECK CONDITION status, with the sense key set to COPY ABORTED;
b)
the copy manager shall indicate the segment that was being processed at the time of the exception by
writing the segment number to the third and fourth bytes of the COMMAND-SPECIFIC INFORMATION field.
The segment number is based on the relative position of the segment descriptor in the parameter list
(see 5.17.7.1) (i.e., the first segment descriptor in the parameter list is assigned descriptor number
zero, the second is assigned one, etc.);
c)
if any data has been written to the copy destination for the segment being processed at the time the
error occurred, the residual for the segment shall be placed in the INFORMATION field, and the VALID bit
shall be set to one. The residual count shall be reported in:
A)
bytes if the destination CSCD descriptor contains:
a)
03h (i.e., processor device) in the PERIPHERAL DEVICE TYPE field; or
b)
01h (i.e., sequential-access device) in the PERIPHERAL DEVICE TYPE field and the FIXED bit is
set to zero in the device type specific parameters;
and
B)
copy destination blocks for all other cases.
The residual count shall be computed by subtracting the number of bytes or blocks successfully
written during the processing of the current segment from the number of bytes or blocks which would
have been written if all commands had completed with GOOD status and all READ commands had
returned the full data length requested. While computing the residual count, the copy manager shall
include only the results of commands successfully completed by a copy destination (i.e., commands
completed by a copy destination with GOOD status or with CHECK CONDITION status and the EOM
bit set to one in the sense data). If the copy manager has used out of order transfers, then the residual
count shall be based only on the contiguous successfully completed transfers starting at relative byte
zero of the segment (i.e., any successfully completed transfers farther from relative byte zero than the
first incomplete or unsuccessful transfer shall not contribute to the computation of the residual count).
If no data has been written to the copy destination for the segment being processed at the time the
error occurred, then the copy manager shall indicate that the INFORMATION field does not contain valid
data by:


A)
setting the VALID bit to zero in the fixed format sense data (see 4.5.3); or
B)
not returning the information descriptor in the descriptor format sense data (see 4.5.2).
Segment descriptors that do not specify a transfer count shall not have a valid residual count;
d)
if the exception condition is reported by the copy source, then:
A)
if fixed format sense data (see 4.5.3) is being returned, then the first byte of the
COMMAND-SPECIFIC INFORMATION field shall be set to the starting byte number, relative to the first
byte of sense data, of an area that contains the status byte and sense data delivered to the copy
manager by the copy. The status byte and sense data shall not be modified by the copy manager.
A zero value indicates that no status byte and sense data is being returned for the copy source; or
B)
if descriptor format sense data (see 4.5.2) is being returned, then the status byte and sense data
delivered to the copy manager by the copy source shall be returned in a forwarded additional
sense data descriptor (see 4.5.2.7) with the SOURCE field set to 1h. The status byte shall not be
modified by the copy manager. The sense data may be truncated by the copy manager but shall
not be modified in any other way. If the sense data is truncated, then the FSDT bit in the forwarded
additional sense data descriptor shall be set to one;
e)
if the exception condition is reported by the copy destination, then:
A)
if fixed format sense data (see 4.5.3) is being returned, then the second byte of the
COMMAND-SPECIFIC INFORMATION field shall be set to the starting byte number, relative to the first
byte of sense data, of an area that contains the status byte and sense data delivered to the copy
manager by the copy destination. The status byte and sense data shall not be modified by the
copy manager. A zero value indicates that no status byte and sense data is being returned for the
copy destination; or
B)
if descriptor format sense data (see 4.5.2) is being returned, then the status byte and sense data
delivered to the copy manager by the copy destination shall be returned in a forwarded additional
sense data descriptor with the SOURCE field set to 2h. The status byte shall not be modified by the
copy manager. The sense data may be truncated by the copy manager but shall not be modified
in any other way. If the sense data is truncated, then the FSDT bit in the forwarded additional
sense data descriptor shall be set to one;
f)
if segment processing is terminated because a CSCD is unreachable or as the result of a failure in a
command sent to a CSCD, then the SENSE-KEY SPECIFIC field shall be set as described in 4.5.2.4.5,
with the FIELD POINTER field indicating the first byte of the CSCD descriptor that specifies the CSCD;
g)
if, during the processing of a segment descriptor, the copy manager detects an error in the segment
descriptor, then the SENSE-KEY SPECIFIC field shall be set as described in 4.5.2.4.5, with the FIELD
POINTER field indicating the byte in error. The FIELD POINTER field may be used to indicate an offset into
either the parameter data or the segment descriptor. The SD bit is used to differentiate between these
two cases. The SD bit shall be set to zero to indicate the FIELD POINTER field is set to an offset from the
start of the parameter data. The SD bit shall be set to one to indicate the FIELD POINTER field is set to an
offset from the start of the segment descriptor; and
h)
if the LIST ID USAGE field is set to 00b or 10b in the parameter data (see 5.17.7.1), the copy manager
shall preserve information for:
A)
the RECEIVE COPY FAILURE DETAILS(LID1) command (see 6.23), if supported. The preserved
information, if any, shall be discarded as described in 6.23; and
B)
the:
a)
RECEIVE COPY STATUS(LID4) command (see 6.24), if supported;
b)
RECEIVE COPY DATA(LID4) command (see 6.20), if supported; and
c)
RECEIVE ROD TOKEN INFORMATION command (see 6.26), if supported.
The preserved information, if any, shall be discarded as described in 6.24.
5.17.7.5 EXTENDED COPY considerations for RODs and ROD tokens
5.17.7.5.1 EXTENDED COPY command CSCD ROD identifiers
All ROD CSCD descriptors (see 6.4.5.9) create an identifier for the ROD that they describe. The identifier is
the CSCD descriptor ID (see table 146 in 6.4.6.1) for the ROD CSCD descriptor.


A ROD identifier identifies a ROD that is one of the following:
a)
specified by segment descriptors that populate the ROD (see 5.17.7.5.2) in the EXTENDED COPY
parameter list (see 5.17.7.1); or
b)
the conversion of a ROD token into an identifier using the following entries in the EXTENDED COPY
parameter list:
A)
copying the ROD token to the inline data (see 5.17.7.1) in the EXTENDED COPY parameter list;
and
B)
referencing the copied ROD token in a ROD CSCD descriptor in which the ROD TYPE field is set to
zero.
If the R_TOKEN bit is set to one in a ROD CSCD descriptor (see 6.4.5.9) in which the ROD TYPE field is not set
to zero, then the identified ROD is used to create a ROD token that is made available for transfer to the appli-
cation client using the RECEIVE ROD TOKEN INFORMATION command (see 6.26) and used as described in
5.17.6.6.
After the copy manager finishes processing the copy operation (see 5.17.4.3) originated by an EXTENDED
COPY command, all the ROD identifiers created by that command shall become invalid.
If a ROD identifier becomes invalid (see 5.17.6.2.2, 5.17.6.2.3, and 5.17.6.7) before processing has been
completed for the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command in which it is
defined, any attempt to use the ROD as a copy source or copy destination shall cause the copy operation
originated by the command to be terminated as if an unreachable CSCD device had been encountered (see
5.17.7.4).
5.17.7.5.2 Populating an EXTENDED COPY command ROD
If the ROD TYPE field (see 6.4.5.9) is not set to zero in the ROD CSCD descriptor, the following segment
descriptors are used to populate a ROD as described 5.17.6.3:
a)
populate a ROD from one or more block device ranges (see 6.4.6.20); and
b)
populate a ROD from one block device range (see 6.4.6.21).
If one of the segment descriptors listed in this subclause specifies the CSCD descriptor ID (see table 146 in
6.4.6.1) of the ROD CSCD descriptor as the copy destination and no errors are detected, then the specified
ROD is populated with the information associated with the ROD type (see 5.17.6.2) based on the contents of
the segment descriptor.
If the CSCD descriptor ID of a ROD CSCD descriptor in which the ROD TYPE field (see 6.4.5.9) is set to zero is
specified as the copy destination in one of the segment descriptors listed in this subclause, then the copy
operation (see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST. The sense key specific data, if any, shall identify the CSCD descriptor ID in the segment
descriptor as the field that in error.
Bytes shall be added to the ROD in the order that the segment descriptors are present in the EXTENDED
COPY parameter data (see 5.17.7.1). If a single segment descriptor specifies multiple ROD byte sources, the
bytes shall be added to the ROD in the order that the bytes are present in that segment descriptor.
The process of populating the ROD ends when:
a)
the CSCD descriptor ID for the ROD CSCD descriptor is specified as a copy source or copy desti-
nation in a segment descriptor that is not one of those listed in this subclause; or
b)
processing of the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command ends.


If one of the segment descriptors listed in this subclause specifies the CSCD descriptor ID of the ROD CSCD
descriptor as the copy destination after the process of populating the ROD has ended, then the copy operation
(see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with CHECK CONDITION
status, with the sense key set to COPY ABORTED, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
If the R_TOKEN bit is set to one in the ROD CSCD descriptor (see 6.4.5.9), then the copy manager shall create
a ROD token (see 5.17.6) for the populated ROD and prepare the ROD token for retrieval using the RECEIVE
ROD TOKEN INFORMATION command (see 6.26).
The copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with
CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST if:
a)
the value in PERIPHERAL DEVICE TYPE field of a copy source specified in a segment descriptor does not
match the value in the PERIPHERAL DEVICE TYPE field in ROD CSCD descriptor (see 6.4.5.9); or
b)
characteristics (e.g., block size, protection information characteristics (see SBC-3)) associated with
the data specified by a segment descriptor are incompatible with the characteristics associated with
the data specified by a previous segment descriptor, if any.
5.17.7.6 EXTENDED COPY command use of RODs when the peripheral device type is 00h
(i.e., block device)
The copy manager shall cause a ROD whose peripheral device type is 00h to function as a block device that:
a)
exists only while the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command is
being processed;
b)
may be used by any segment descriptor (see 6.4.6.1) that operates on a block device as a:
A)
copy source; or
B)
copy destination, if allowed by the ROD type (see 5.17.6.2);
c)
has the following block device characteristics:
A)
a contiguous range of logical blocks;
B)
LBAs numbered from zero to the number of logical blocks represented by the ROD (see
5.17.7.5.2) minus one;
C) data that matches the data that is in the ROD; and
D) characteristics that match those of the logical blocks that are represented by the ROD, including
at least the following:
a)
a DISK BLOCK LENGTH field in the device type specific CSCD descriptor parameters (see
6.4.5.3) that is set to the block size of each block represented by the ROD; and
b)
protection information that matches the protection information of the logical blocks that are
represented by the ROD;
and
d)
may have logical block provisioning information equivalent to the logical block provisioning infor-
mation of the logical blocks that are represented by the ROD (see 5.17.6).


6 Commands for all device types
6.1 Summary of commands for all device types
The operation codes for commands that apply to all device types are listed in table 118.
Table 118 — Commands for all device types (part 1 of 2)
Command
Operation
code
Type
Reference
ACCESS CONTROL IN
86h
O
8.3.2
ACCESS CONTROL OUT
87h
O
8.3.3
CHANGE ALIASES
A4h/0Bh a
O
6.2
COPY OPERATION ABORT
83h/1Ch a
O
6.3
EXTENDED COPY(LID4)
83h/01h a
O
6.4
EXTENDED COPY(LID1)
83h/00h a
O
6.5
INQUIRY
12h
M
6.6
LOG SELECT
4Ch
O
6.7
LOG SENSE
4Dh
O
6.8
MANAGEMENT PROTOCOL IN
A3h/10h a
O
6.9
MANAGEMENT PROTOCOL OUT
A4h/10h a
O
6.10
MODE SELECT(6)
15h
C
6.11
MODE SELECT(10)
55h
C
6.12
MODE SENSE(6)
1Ah
C
6.13
MODE SENSE(10)
5Ah
C
6.14
PERSISTENT RESERVE IN
5Eh
C
6.15
PERSISTENT RESERVE OUT
5Fh
C
6.16
READ ATTRIBUTE
8Ch
O
6.17
READ BUFFER
3Ch
O
6.18
READ MEDIA SERIAL NUMBER
ABh/01h a
C
6.19
RECEIVE COPY DATA(LID4)
84h/06h a
O
6.20
RECEIVE COPY DATA(LID1)
84h/01h a
O
6.21
RECEIVE COPY OPERATING PARAMETERS
84h/03h a
O
6.22
RECEIVE COPY FAILURE DETAILS(LID1)
84h/04h a
O
6.23
RECEIVE COPY STATUS(LID4)
84h/05h a
O
6.24
RECEIVE COPY STATUS(LID1)
84h/00h a
O
6.25
RECEIVE ROD TOKEN INFORMATION
84h/07h a
O
6.26
RECEIVE CREDENTIAL
7Fh/1800h a
O
6.27
RECEIVE DIAGNOSTIC RESULTS
1Ch
O
6.28
A numeric ordered listing of operation codes is provided in E.3.
Type Key: C = Command implementation is defined in the applicable command standard.
M = Command implementation is mandatory.
O = Command implementation is optional.
Z = Command implementation is defined in a previous standard.
a This command is defined by a combination of operation code and service action. The operation code
value is shown preceding the slash and the service action value is shown after the slash.
b The following operation codes are obsolete: 16h, 17h, 18h, 39h, 3Ah, 40h, 56h, and 57h.


REMOVE I_T NEXUS
A4h/0Ch a
O
6.29
REPORT ALIASES
A3h/0Bh a
O
6.30
REPORT ALL ROD TOKENS
84h/08h a
O
6.31
REPORT IDENTIFYING INFORMATION
A3h/05h a
O
6.32
REPORT LUNS
A0h
M
6.33
REPORT PRIORITY
A3h/0Eh a
O
6.34
REPORT SUPPORTED OPERATION CODES
A3h/0Ch a
O
6.35
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS
A3h/0Dh a
O
6.36
REPORT TARGET PORT GROUPS
A3h/0Ah a
O
6.37
REPORT TIMESTAMP
A3h/0Fh a
O
6.38
REQUEST SENSE
03h
C
6.39
SECURITY PROTOCOL IN
A2h
O
6.40
SECURITY PROTOCOL OUT
B5h
O
6.41
SEND DIAGNOSTIC
1Dh
C
6.42
SET IDENTIFYING INFORMATION
A4h/06h a
O
6.43
SET PRIORITY
A4h/0Eh a
O
6.44
SET TARGET PORT GROUPS
A4h/0Ah a
O
6.45
SET TIMESTAMP
A4h/0Fh a
O
6.46
TEST UNIT READY
00h
M
6.47
WRITE ATTRIBUTE
8Dh
O
6.48
WRITE BUFFER
3Bh
C
6.49
Obsolete b
Table 118 — Commands for all device types (part 2 of 2)
Command
Operation
code
Type
Reference
A numeric ordered listing of operation codes is provided in E.3.
Type Key: C = Command implementation is defined in the applicable command standard.
M = Command implementation is mandatory.
O = Command implementation is optional.
Z = Command implementation is defined in a previous standard.
a This command is defined by a combination of operation code and service action. The operation code
value is shown preceding the slash and the service action value is shown after the slash.
b The following operation codes are obsolete: 16h, 17h, 18h, 39h, 3Ah, 40h, 56h, and 57h.
