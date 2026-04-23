# 6.4.6 Segment descriptors

6.4.6 Segment descriptors
6.4.6.1 Segment descriptors introduction
The descriptor type code (see table 130) values assigned to segment descriptors are shown in table 146.
Table 146 — EXTENDED COPY segment descriptor type codes (part 1 of 2)
Descriptor
type
code a
Reference
Description b
Shorthand b
00h
6.4.6.2
Copy from block device to stream device
blockstream
01h
6.4.6.3
Copy from stream device to block device
streamblock
02h
6.4.6.4
Copy from block device to block device
blockblock
03h
6.4.6.5
Copy from stream device to stream device
streamstream
04h
6.4.6.6
Copy inline data to stream device
inlinestream
05h
6.4.6.7
Copy embedded data to stream device
embeddedstream
06h
6.4.6.8
Read from stream device and discard
streamdiscard
07h
6.4.6.9
Verify CSCD
08h
6.4.6.10
Copy block device with offset to stream device
block<o>stream
09h
6.4.6.11
Copy stream device to block device with offset
streamblock<o>
0Ah
6.4.6.12
Copy block device with offset to block device with
offset
block<o>block<o>
0Bh
6.4.6.2
Copy from block device to stream device and hold a
copy of processed data for the application client c
blockstream
+application client
0Ch
6.4.6.3
Copy from stream device to block device and hold a
copy of processed data for the application client c
streamblock
+application client
0Dh
6.4.6.4
Copy from block device to block device and hold a
copy of processed data for the application client c
blockblock
+application client
0Eh
6.4.6.5
Copy from stream device to stream device and
hold a copy of processed data for the application
client c
streamstream
+application client
0Fh
6.4.6.8
Read from stream device and hold a copy of
processed data for the application client c
streamdiscard
+application client
a A copy manager may not support all segment descriptor types, however, the copy manager shall list all
supported segment descriptor types in the Third-party Copy VPD page Supported Descriptors
descriptor (see 7.8.17.6), and in the response to the RECEIVE COPY OPERATING PARAMETERS
command (see 6.22).
b Block devices are those with peripheral device type codes 0h (i.e, direct access block), 5h (i.e.,
CD/DVD), and Eh (i.e., simplified direct-access). Stream devices are those devices with peripheral
device type codes 1h (i.e., sequential-access) and 3h (i.e., processor). Sequential-access stream
(indicated by the term tape in the shorthand column) devices are those with peripheral device type code
1h. See 6.6.2 for peripheral device type code definitions.
c The application client uses the RECEIVE COPY DATA(LID4) command (see 6.20) or RECEIVE COPY
DATA(LID1) command (see 6.21) to retrieve data held for it by the copy manager (see 5.17.4.5).


10h
6.4.6.13
Write filemarks to sequential-access device
filemarktape
11h
6.4.6.14
Space records or filemarks on sequential-access
device
spacetape
12h
6.4.6.15
Locate on sequential-access device
locatetape
13h
6.4.6.16
Tape device image copy
<i>tape<i>tape
14h
6.4.6.17
Register persistent reservation key
15h
6.4.6.18
Third party persistent reservations source I_T
nexus
16h
6.4.6.19
Block device image copy
<i>block<i>block
17h to
BDh
Reserved
BEh
6.4.6.20
Populate ROD from one or more block ranges
RODblock ranges(n)
BFh
6.4.6.21
Populate ROD from one block range
RODblock range(1)
Table 146 — EXTENDED COPY segment descriptor type codes (part 2 of 2)
Descriptor
type
code a
Reference
Description b
Shorthand b
a A copy manager may not support all segment descriptor types, however, the copy manager shall list all
supported segment descriptor types in the Third-party Copy VPD page Supported Descriptors
descriptor (see 7.8.17.6), and in the response to the RECEIVE COPY OPERATING PARAMETERS
command (see 6.22).
b Block devices are those with peripheral device type codes 0h (i.e, direct access block), 5h (i.e.,
CD/DVD), and Eh (i.e., simplified direct-access). Stream devices are those devices with peripheral
device type codes 1h (i.e., sequential-access) and 3h (i.e., processor). Sequential-access stream
(indicated by the term tape in the shorthand column) devices are those with peripheral device type code
1h. See 6.6.2 for peripheral device type code definitions.
c The application client uses the RECEIVE COPY DATA(LID4) command (see 6.20) or RECEIVE COPY
DATA(LID1) command (see 6.21) to retrieve data held for it by the copy manager (see 5.17.4.5).


Segment descriptors (see table 147) begin with an eight byte header.
The DESCRIPTOR TYPE CODE field is described in 6.4.4. Support for each segment descriptor format is optional.
If a copy manager receives an unsupported descriptor type code in a segment descriptor, the copy operation
(see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to UNSUPPORTED SEGMENT
DESCRIPTOR TYPE CODE.
The destination count (DC) bit is only applicable to segment descriptors with descriptor type code values of
02h and 0Dh (see 6.4.6.4). The DC bit shall be ignored for all other segment descriptors.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is set to the length in bytes of the fields that follow the DESCRIPTOR LENGTH field
in the segment descriptor.
Table 147 — Segment descriptor header
Bit
Byte
DESCRIPTOR TYPE CODE (00h to 3Fh)
Reserved
DC
CAT
(MSB)
DESCRIPTOR LENGTH (n-3)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Segment descriptor parameters
•••
n


The SOURCE CSCD DESCRIPTOR ID field (see table 148) specifies the copy source.
The DESTINATION CSCD DESCRIPTOR ID field (see table 148) specifies the copy destination.
Some segment descriptor formats do not require a SOURCE CSCD DESCRIPTOR ID field or a DESTINATION CSCD
DESCRIPTOR ID field, in which case the field is reserved.
If the CSCD specified by a SOURCE CSCD DESCRIPTOR ID field or a DESTINATION CSCD DESCRIPTOR ID field is not
accessible to the copy manager, then the copy operation (see 5.17.4.3) originated by the command shall be
terminated with CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional
sense code set to UNREACHABLE COPY TARGET.
Table 148 — CSCD descriptor ID values
Code
Description
0000h a
The copy source or copy destination is specified by the contents of the CSCD
descriptor whose location in the EXTENDED COPY command parameter list
(see 5.17.7.1) is computed as follows:
16 + (code  32)
where code is 0000h to 07FFh as shown in this table
0001h to 07FFh b
C000h
The copy source or copy destination is a null logical unit b whose peripheral
device type is 00h (i.e., block)
C001h
The copy source or copy destination is a null logical unit b whose peripheral
device type is 01h (i.e., stream)
F800h c
The copy source or copy destination is the logical unit specified by the ROD
token specified in the ROD CSCD descriptor (see 6.4.5.9) that has this value in
its ROD PRODUCER CSCD DESCRIPTOR ID field.
FFFFh
The copy source or copy destination is the logical unit that contains the copy
manager (see SAM-5) that is processing the EXTENDED COPY command
(i.e., the logical unit to which the EXTENDED COPY command was sent)
all others
Reserved
a Use of these CSCD descriptor IDs for commands other than the EXTENDED COPY command
may cause the copy operation (see 5.17.4.3) originated by the command to be terminated with
CHECK CONDITION status (see 6.4.2).
b A null logical unit is a logical unit that has a specified peripheral device type to which the copy
manager is not allowed to send any SCSI commands. If the processing required by a segment
descriptor necessitates sending a SCSI command to a source device or destination device
specified to be a null logical unit, then the copy operation (see 5.17.4.3) originated by the
EXTENDED COPY command shall be terminated as if an unreachable CSCD had been
encountered (see 5.17.7.4). Null logical units are useful for processing the residual data from
previous segment descriptors without affecting any media (e.g., a segment descriptor of type 06h
stream device to discard with the SOURCE CSCD DESCRIPTOR ID field set to C002h, the BYTE COUNT
field set to zero, the CAT bit set to zero, and the PAD bit set to one may be used to discard all
residual data).
c If this code appears in any field other than the ROD PRODUCER CSCD DESCRIPTOR ID field in the ROD
CSCD descriptor, then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY
command shall be terminated as if an unreachable CSCD had been encountered (see 5.17.7.4).


6.4.6.2 Block device to stream device functions
The segment descriptor format shown in table 149 is used by the copy functions that move data from a block
device to a stream device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1.
For descriptor type code 00h (i.e., blockstream) or descriptor type code 0Bh (i.e., blockstream+appli-
cation client), the copy manager shall copy the data from the copy source block device specified by the
SOURCE CSCD DESCRIPTOR ID field to the copy destination stream device specified by the DESTINATION CSCD
DESCRIPTOR ID field using the logical blocks starting at the location specified by the BLOCK DEVICE LOGICAL
BLOCK ADDRESS field. As many blocks shall be read as necessary to process (see 5.17.7.2) a number of bytes
equal to the contents of the DISK BLOCK LENGTH field in the CSCD descriptor for the source device times the
contents of the BLOCK DEVICE NUMBER OF BLOCKS field. The data shall be written to the stream device starting
at the current position of the media.
For descriptor type code 0Bh (i.e., blockstream+application client), the copy manager also shall hold a copy
of the processed data for delivery to the application client upon completion of the copy operation (see
5.17.4.3) originated by the EXTENDED COPY command as described in 5.17.4.5.
The CAT bit is described in 5.17.7.2.
Table 149 — Block device to stream device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (00h or 0Bh)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0014h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
Reserved
Reserved
(MSB)
BLOCK DEVICE NUMBER OF BLOCKS
(LSB)
(MSB)
BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)


The descriptor length field is described in 6.4.6.1, and shall be set as shown in table 149 for descriptor type
code 00h (i.e., blockstream) and descriptor type code 0Bh (i.e., blockstream+application client).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be written by each write command
sent to the copy destination stream device. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy destination sequential-access device type.
The BLOCK DEVICE NUMBER OF BLOCKS field specifies the length, in copy source logical blocks, of data to be
processed (see 5.17.7.2) in the segment. A value of zero shall not be considered an error. No data shall be
processed, but any residual destination data retained from a previous segment shall be written if possible to
the destination in whole-block transfers. A value of zero shall not modify the handling of residual data.
The BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting logical block address on the copy source
block device for this segment.
6.4.6.3 Stream device to block device functions
The segment descriptor format shown in table 150 is used by the copy functions that move data from a stream
device to a block device.
Table 150 — Stream device to block device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (01h or 0Ch)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0014h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
Reserved
Reserved
(MSB)
BLOCK DEVICE NUMBER OF BLOCKS
(LSB)
(MSB)
BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)


The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1.
For descriptor type code 01h (i.e., streamblock) or descriptor type code 0Ch (i.e., streamblock+appli-
cation client), the copy manager shall copy the data from the copy source stream device specified by the
SOURCE CSCD DESCRIPTOR ID field to the copy destination block device specified by the DESTINATION CSCD
DESCRIPTOR ID field using the stream data starting at the current position of the stream device. The data shall
be written to logical blocks starting at the location specified by the BLOCK DEVICE LOGICAL BLOCK ADDRESS field
and continuing for the number of blocks specified in the BLOCK DEVICE NUMBER OF BLOCKS field.
For descriptor type code 0Ch (i.e., streamblock+application client), the copy manager also shall hold a copy
of the processed data for delivery to the application client upon completion of the copy operation (see
5.17.4.3) originated by the EXTENDED COPY command as described in 5.17.4.5.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 150 for descriptor type
code 01h (i.e., streamblock) and descriptor type code 0Ch (i.e., streamblock+application client).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be read from the copy source
stream device by each read command. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy source sequential-access device type.
The BLOCK DEVICE NUMBER OF BLOCKS field specifies the number blocks to be written by the segment. A value
of zero specifies that no blocks shall be written in this segment. This shall not be considered an error.
The BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting logical block address on the copy desti-
nation block device for this segment.


6.4.6.4 Block device to block device functions
The segment descriptor format shown in table 151 is used by the copy functions that move data from a block
device to a block device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1.
For descriptor type code 02h (i.e., blockblock) or descriptor type code 0Dh (i.e., blockblock+application
client), the copy manager shall copy the data from the copy source block device specified by the SOURCE CSCD
DESCRIPTOR ID field to the copy destination block device specified by the DESTINATION CSCD DESCRIPTOR ID field
using the logical blocks starting at the location specified by the SOURCE BLOCK DEVICE LOGICAL BLOCK ADDRESS
field. The data shall be written to logical blocks starting at the location specified by the DESTINATION BLOCK
DEVICE LOGICAL BLOCK ADDRESS field.
If the destination count (DC) bit is set to zero, then:
a)
as many blocks shall be read as necessary to process (see 5.17.7.2) a number of bytes equal to the
contents of the DISK BLOCK LENGTH field in the CSCD descriptor for the copy source device times the
contents of the BLOCK DEVICE NUMBER OF BLOCKS field; and
b)
as many writes as possible shall be performed using any residual destination data from the previous
segment and the data processed in this segment.
Table 151 — Block device to block device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (02h or 0Dh)
Reserved
DC
CAT
(MSB)
DESCRIPTOR LENGTH (0018h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
Reserved
(MSB)
BLOCK DEVICE NUMBER OF BLOCKS
(LSB)
(MSB)
SOURCE BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
DESTINATION BLOCK DEVICE LOGICAL BLOCK
ADDRESS
•••
(LSB)


If the DC bit is set to one, then:
a)
the number of blocks specified by the BLOCK DEVICE NUMBER OF BLOCKS field shall be written to the
copy destination block device;
b)
as many bytes shall be processed (see 5.17.7.2) as necessary for these writes to be performed; and
c)
as many blocks shall be read as necessary to supply the data to be processed.
For descriptor type code 0Dh (i.e., blockblock+application client), the copy manager also shall hold a copy
of the processed data for delivery to the application client upon completion of the copy operation (see
5.17.4.3) originated by the EXTENDED COPY command as described in 5.17.4.5.
The CAT bit is described in 5.17.7.2.
The DC bit specifies whether the BLOCK DEVICE NUMBER OF BLOCKS field refers to the copy source or copy desti-
nation. A DC bit set to zero specifies that the BLOCK DEVICE NUMBER OF BLOCKS field refers to the copy source.
A DC bit set to one specifies that the BLOCK DEVICE NUMBER OF BLOCKS field refers to the copy destination.
The DESCRIPTOR LENGTH field shall is described in 6.4.6.16.3.7.1, and shall be set as shown in table 151 for
descriptor type code 02h (i.e., blockblock) and descriptor type code 0Dh (i.e., blockblock+application
client).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
If the DC bit is set to zero, the BLOCK DEVICE NUMBER OF BLOCKS field specifies the number of blocks to be
processed. If the DC bit is set to one, the BLOCK DEVICE NUMBER OF BLOCKS field specifies the number of blocks
to be written to the copy destination.
If the DC bit is set to zero, a BLOCK DEVICE NUMBER OF BLOCKS field set to zero specifies that:
a)
no source blocks shall be read and no source data shall be processed;
b)
any residual destination data from a previous segment shall be written if possible to the destination in
whole-block transfers; and
c)
any residual data shall be processed as described in 5.17.7.2.
If the DC bit set to one, a BLOCK DEVICE NUMBER OF BLOCKS field set to zero specifies that:
a)
no destination blocks shall be written; and
b)
the only processing to be performed is that any residual source data or destination data from the
previous segment shall be processed as residual data as described in 5.17.7.2.
The SOURCE BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the copy source logical block address from
which the reading of data shall start.
The DESTINATION BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the copy destination logical block
address to which the writing of data shall begin.


6.4.6.5 Stream device to stream device functions
The segment descriptor format shown in table 152 is used by the copy functions that move data from a stream
device to a stream device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1.
For descriptor type code 03h (i.e., streamstream) or descriptor type code 0Eh (i.e., streamstream+appli-
cation client), the copy manager shall copy the data from the copy source stream device specified by the
SOURCE CSCD DESCRIPTOR ID field to the destination copy stream device specified by the DESTINATION CSCD
DESCRIPTOR ID field. Data shall be read from the copy source stream device starting at the current position of
the copy source stream device. Data shall be written to the copy destination stream device starting at the
current position of the copy destination stream device. The BYTE COUNT field defines the number of bytes to be
processed (see 5.17.7.2) by the copy manager. The copy manager shall perform reads as necessary to
supply the source data, and as many writes as possible using the destination data.
For descriptor type code 0Eh (i.e., streamstream+application client), the copy manager also shall hold a
copy of the processed data for delivery to the application client upon completion of the copy operation (see
5.17.4.3) originated by the EXTENDED COPY command as described in 5.17.4.5.
The CAT bit is described in 5.17.7.2.
Table 152 — Stream device to stream device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (03h or 0Eh)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0010h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
SOURCE STREAM DEVICE TRANSFER LENGTH
(LSB)
Reserved
(MSB)
DESTINATION STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
BYTE COUNT
•••
(LSB)


The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 152 for descriptor type
code 03h (i.e., streamstream) and descriptor type code 0Eh (i.e., streamstream+application client).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The SOURCE STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be read from the copy
source stream device by each read command. See 6.4.5.4 for a description of how data in the SOURCE STREAM
DEVICE TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field
in the device type specific CSCD descriptor parameters for the copy source sequential-access device type.
The DESTINATION STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be written to the copy
destination stream device by each write command. See 6.4.5.4 for a description of how data in the DESTI-
NATION STREAM DEVICE TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM
BLOCK LENGTH field in the device type specific CSCD descriptor parameters for the copy destination
sequential-access device type.
The BYTE COUNT field specifies the number of bytes that shall be processed (see 5.17.7.2) for this segment
descriptor. A value of zero shall not be considered an error, and specifies that no source data shall be read
and no source data shall be processed. However, a value of zero specifies that any residual destination data
from a previous segment shall be written if possible to the copy destination in whole-block transfers, and any
residual data shall be processed as described in 5.17.7.2.


6.4.6.6 Inline data to stream device function
The segment descriptor format shown in table 153 instructs the copy manager to write inline data from the
EXTENDED COPY parameter list to a stream device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 153 for
the inline data to stream device segment descriptor.
Descriptor type code 04h (i.e., inlinestream) instructs the copy manager to write inline data from the
EXTENDED COPY parameter list (see 5.17.7.1) to a copy destination stream device. The inline data shall be
read from the optional inline data at the end of the EXTENDED COPY parameter list. The data shall be written
to the copy destination stream device specified by the DESTINATION CSCD DESCRIPTOR ID field starting at the
current position of the stream device. Any residual destination data from a previous segment descriptor shall
be written before the data of the current segment descriptor. Any residual source data from a previous
segment descriptor shall not be processed (see 5.17.7.2), and shall be processed as residual source data.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 153 for descriptor type
code 04h (i.e., inlinestream).
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
Table 153 — Inline data to stream device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (04h)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0010h)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
INLINE DATA OFFSET
•••
(LSB)
(MSB)
INLINE DATA NUMBER OF BYTES
•••
(LSB)


The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be written to the copy destination
stream device by each write command. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy destination sequential-access device type.
The value in the INLINE DATA OFFSET field is added to the location of the first byte of inline data in the
EXTENDED COPY parameter list (see 5.17.7.1) to locate the first byte of inline data to be written to the copy
destination stream device. The INLINE DATA OFFSET value shall be a multiple of 4.
The INLINE DATA NUMBER OF BYTES field specifies the number of bytes of inline data that are to be transferred to
the copy destination stream device. A value of zero shall not be considered an error.
If the sum of the INLINE DATA OFFSET and the INLINE DATA NUMBER OF BYTES values exceeds the value in the
INLINE DATA LENGTH field (see 6.4.3.6), the copy manager shall terminate the copy operation (see 5.17.4.3)
originated by the EXTENDED COPY command with CHECK CONDITION status, with the sense key set to
COPY ABORTED, and the additional sense code set to INLINE DATA LENGTH EXCEEDED.
6.4.6.7 Embedded data to stream device function
The segment descriptor format shown in table 154 instructs the copy manager to write embedded data from
the segment descriptor to a stream device.
Table 154 — Embedded data to stream device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (05h)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (n-3)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
EMBEDDED DATA NUMBER OF BYTES
(LSB)
Reserved
EMBEDDED DATA
•••
n


The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 154 for
the embedded data to stream device segment descriptor.
Descriptor type code 05h (i.e., embeddedstream) instructs the copy manager to write embedded data from
the segment descriptor to a copy destination stream device. The embedded data shall be read from the
segment descriptor. The data shall be written to the copy destination stream device specified by the DESTI-
NATION CSCD DESCRIPTOR ID field starting at the current position of the copy destination stream device. Any
residual destination data from a previous segment descriptor shall be written before the data of the current
segment descriptor. Any residual source data from a previous segment descriptor shall not be processed (see
5.17.7.2), and shall be processed as residual source data.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1. The value in the DESCRIPTOR LENGTH field shall be a
multiple of 4.
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be written to the copy destination
stream device by each write command. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy destination sequential-access device type.
The EMBEDDED DATA NUMBER OF BYTES field specifies the number of bytes of embedded data that are to be
transferred to the copy destination stream device. A value of zero shall not be considered an error. If the value
in the EMBEDDED DATA NUMBER OF BYTES field is greater than the value in the DESCRIPTOR LENGTH field minus
12, then the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST.
The EMBEDDED DATA field is a zero-padded (see 4.3.2) field whose length is a multiple of 4 that specifies the
embedded data to be copied to the copy destination stream device.


6.4.6.8 Stream device to discard functions
The segment descriptor format shown in table 155 instructs the copy manager to read data from a stream
device and not transfer it to any copy destination.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1.
For descriptor type code 06h (i.e., streamdiscard) or descriptor type code 0Fh (i.e., streamdiscard+appli-
cation client), the copy manager shall read data as necessary from the copy source stream device specified
by the SOURCE CSCD DESCRIPTOR ID field starting at the current position of the copy source stream device. The
number of bytes specified by the NUMBER OF BYTES field shall be removed from the source data, starting with
any residual source data from the previous segment.
For descriptor type code 06h (i.e., streamdiscard) the removed data shall be discarded and not written to
any copy destination.
For descriptor type code 0Fh (i.e., streamdiscard+application client) the removed data shall be held for
delivery to the application client upon completion of the copy operation (see 5.17.4.3) originated by the
EXTENDED COPY command as described in 5.17.4.5.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, shall be set as shown in table 155 for descriptor type
code 0Fh (i.e., streamdiscard+application client) and descriptor type code 0Fh (i.e., streamdiscard+appli-
cation client).
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
Table 155 — Stream device to discard segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (06h or 0Fh)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
Reserved
Reserved
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
NUMBER OF BYTES
•••
(LSB)


The SOURCE STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be read from the copy
source stream device on each read command. See 6.4.5.4 for a description of how data in the SOURCE
STREAM DEVICE TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK
LENGTH field in the device type specific CSCD descriptor parameters for the copy source sequential-access
device type.
The NUMBER OF BYTES field specifies the number of bytes to be removed from the source data.
6.4.6.9 Verify CSCD function
The segment descriptor format shown in table 156 instructs the copy manager to verify the accessibility of a
CSCD.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 156 for
the verify CSCD segment descriptor.
Descriptor type code 07h instructs the copy manager to verify the accessibility of the CSCD specified by the
SOURCE CSCD DESCRIPTOR ID field.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 156 for the verify
CSCD segment descriptor.
The SOURCE CSCD DESCRIPTOR ID field is described in 6.4.6.1.
Support for a value of one in the test unit ready (TUR) bit is optional. If setting the TUR bit to one is supported
and the TUR bit is set to one, then a TEST UNIT READY command (see 6.47) shall be used to determine the
readiness of the CSCD. If setting the TUR to one is not supported and the TUR bit is set to one, then the copy
operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with CHECK
CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST. The SENSE-KEY SPECIFIC field shall be set as described in 5.17.7.4. If
the TUR bit is set to zero, then the accessibility should be verified without disturbing established unit attention
conditions or ACA conditions (e.g., using the INQUIRY command (see 6.6)).
Table 156 — Verify CSCD segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (07h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0008h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
Reserved
Reserved
TUR
Reserved
•••


If the SOURCE CSCD DESCRIPTOR ID field specifies a ROD CSCD descriptor (see 6.4.5.9), the copy manager
shall ignore the TUR bit and shall process the Verify CSCD segment descriptor based on the contents of ROD
TYPE field as follows:
a)
if the ROD TYPE field is set to zero, the copy manager shall verify the accessibility as follows:
A)
if the ROD token was created by the copy manager that is processing the Verify CSCD segment
descriptor, then the ROD token shall be validated as described in 5.17.6.5.2;
B)
if the ROD token was created by a copy manager in the same SCSI target device as the copy
manager that is processing the Verify CSCD segment descriptor, then the creating copy manager
shall be requested to validate the ROD token as described in 5.17.6.5.2; and
C) if the ROD token was created by a copy manager in SCSI target device other than the SCSI
target device that contains the copy manager that is processing the Verify CSCD segment
descriptor, then the validation of the ROD token depends on the contents of the REMOTE TOKENS
field in the ROD Features third-party copy descriptor (see 7.8.17.8) as follows:
a)
if REMOTE TOKENS field is set to 0h, then the copy operation (see 5.17.4.3) originated by the
command shall be terminated with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID TOKEN OPERATION,
REMOTE TOKEN USAGE NOT SUPPORTED; or
b)
if REMOTE TOKENS field is not set to 0h, then the processing copy manager shall request the
copy manager that created the ROD token to validate it;
or
b)
if the ROD TYPE field is not set to zero, the processing copy manager shall ignore the Verify CSCD
segment descriptor. This shall not be considered an error.


6.4.6.10 Block device with offset to stream device function
The segment descriptor format shown in table 157 is used to instruct the copy manager to move data from a
block device with a byte offset to a stream device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 157 for
the block device with offset to stream device segment descriptor.
Descriptor type code 08h (i.e., block<o>stream) instructs the copy manager to copy the data from the copy
source block device specified by the SOURCE CSCD DESCRIPTOR ID field to the copy destination stream device
specified by the DESTINATION CSCD DESCRIPTOR ID field using data starting at the location specified by the
BLOCK DEVICE BYTE OFFSET field in the logical block specified by the BLOCK DEVICE LOGICAL BLOCK ADDRESS
field and continuing for the number of bytes specified in the NUMBER OF BYTES field. The data shall be written to
the copy destination stream device starting at the current position of the media.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 157 for the block
device with offset to stream device segment descriptor.
Table 157 — Block device with offset to stream device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (08h)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0018h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
NUMBER OF BYTES
•••
(LSB)
(MSB)
BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
Reserved
(MSB)
BLOCK DEVICE BYTE OFFSET
(LSB)


The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be written by each write command
send to the copy destination stream device. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy destination sequential-access device type.
The NUMBER OF BYTES field specifies the number bytes to be read. A value of zero specifies that no bytes shall
be transferred in this segment. This shall not be considered an error.
The BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting logical block address on the copy source
block device for this segment.
The BLOCK DEVICE BYTE OFFSET field specifies the offset into the first copy source block at which to begin
reading bytes.


6.4.6.11 Stream device to block device with offset function
The segment descriptor format shown in table 158 is used to instruct the copy manager to move data from a
stream device to a block device with a byte offset.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 158 for
the stream device with offset to block device segment descriptor.
Descriptor type code 09h (i.e., streamblock<o>) instructs the copy manager to copy the data from the copy
source stream device specified by the SOURCE CSCD DESCRIPTOR ID field to the copy destination block device
specified by the DESTINATION CSCD DESCRIPTOR ID field using the stream data starting at the current position of
the copy source stream device. The data shall be written starting at the location specified by the BLOCK DEVICE
BYTE OFFSET field in the logical block specified by the BLOCK DEVICE LOGICAL BLOCK ADDRESS field and
continuing for the number of bytes specified in the NUMBER OF BYTES field.
Table 158 — Stream device with offset to block device segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (09h)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (0018h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
(MSB)
STREAM DEVICE TRANSFER LENGTH
(LSB)
(MSB)
NUMBER OF BYTES
•••
(LSB)
(MSB)
BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
Reserved
(MSB)
BLOCK DEVICE BYTE OFFSET
(LSB)


The content of the starting logical block on the copy destination block device before the starting offset shall be
preserved. The content on the ending logical block on the copy destination block device beyond the end of the
transfer shall be preserved. The copy manager may implement this function by reading the starting and
ending logical blocks, modifying a portion of the blocks as required, and writing the full blocks to the copy
destination block device.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 158 for the stream
device with offset to block device segment descriptor.
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The STREAM DEVICE TRANSFER LENGTH field specifies the amount of data to be read from the copy source
stream device by each read command. See 6.4.5.4 for a description of how data in the STREAM DEVICE
TRANSFER LENGTH field in the segment descriptor interacts with data in the STREAM BLOCK LENGTH field in the
device type specific CSCD descriptor parameters for the copy source sequential-access device type.
The NUMBER OF BYTES field specifies the number bytes to be read. A value of zero specifies that no bytes shall
be transferred in this segment. This shall not be considered an error.
The BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting logical block address on the copy desti-
nation block device for this segment.
The BLOCK DEVICE BYTE OFFSET field specifies the offset into the first destination block at which to begin writing
data to the copy destination block device.


6.4.6.12 Block device with offset to block device with offset function
The segment descriptor format shown in table 159 instructs the copy manager to move data from a block
device with a byte offset to a block device with a byte offset.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 159 for
the block device with offset to block device with offset segment descriptor.
Descriptor type code 0Ah (i.e., block<o>block<o>) instructs the copy manager to copy the data from the
copy source block device specified by the SOURCE CSCD DESCRIPTOR ID field to the copy destination block
device specified by the DESTINATION CSCD DESCRIPTOR ID field using data starting at the location specified by
the source BLOCK DEVICE BYTE OFFSET field in the logical block specified by the SOURCE BLOCK DEVICE LOGICAL
BLOCK ADDRESS field and continuing for the number of bytes specified in the NUMBER OF BYTES field. The data
shall be written to the copy destination block device starting at the location specified by the DESTINATION BLOCK
DEVICE BYTE OFFSET field in the logical block specified by the DESTINATION BLOCK DEVICE LOGICAL BLOCK
ADDRESS field.
The content of the starting logical block on the copy destination block device before the starting offset shall be
preserved. The content on the ending logical block on the copy destination block device beyond the end of the
transfer shall be preserved. The copy manager may implement this operation by reading the starting and
Table 159 — Block device with offset to block device with offset segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (0Ah)
Reserved
CAT
(MSB)
DESCRIPTOR LENGTH (001Ch)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
NUMBER OF BYTES
•••
(LSB)
(MSB)
SOURCE BLOCK DEVICE LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
DESTINATION BLOCK DEVICE LOGICAL BLOCK
ADDRESS
•••
(LSB)
(MSB)
SOURCE BLOCK DEVICE BYTE OFFSET
(LSB)
(MSB)
DESTINATION BLOCK DEVICE BYTE OFFSET
(LSB)


ending logical blocks, modifying a portion of the blocks as required, and writing the full blocks to the block on
the copy destination block device.
The CAT bit is described in 5.17.7.2.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 159 for the block
device with offset to block device with offset segment descriptor.
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The NUMBER OF BYTES field specifies the number bytes to be read. A value of zero specifies that no bytes shall
be transferred in this segment. This shall not be considered an error.
The SOURCE BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting address on the copy source
block device for this segment.
The DESTINATION BLOCK DEVICE LOGICAL BLOCK ADDRESS field specifies the starting logical block address on the
copy destination block device for this segment.
The SOURCE BLOCK DEVICE BYTE OFFSET field specifies the offset into the first copy source block at which to
begin reading bytes.
The DESTINATION BLOCK DEVICE BYTE OFFSET field specifies the offset into the first copy destination block at
which to begin writing data to the copy destination block device.
6.4.6.13 Write filemarks function
The segment descriptor format shown in table 160 instructs the copy manager to write filemarks on the desti-
nation tape device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 160 for
the write filemarks segment descriptor.
Table 160 — Write filemarks segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (10h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0008h)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
Obsolete
W_IMMED
(MSB)
FILEMARK COUNT
(LSB)


Descriptor type code 10h (i.e., filemarktape) instructs the copy manager to write filemarks to the copy desti-
nation tape device specified by the DESTINATION CSCD DESCRIPTOR ID field starting at the current position of the
copy destination tape device. If the PERIPHERAL DEVICE TYPE field in the CSCD descriptor specified by the
DESTINATION CSCD DESCRIPTOR ID field does not contain 01h, the copy manager shall terminate the copy
operation (see 5.17.4.3) originated by the command with CHECK CONDITION status, with the sense key set
to COPY ABORTED, and the additional sense code set to INVALID OPERATION FOR COPY SOURCE OR
DESTINATION.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 160 for the write
filemarks segment descriptor.
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
If the write immediate (W_IMMED) bit in the segment descriptor is set to one, then the copy manager shall issue
a WRITE FILEMARKS command to the copy destination tape device with the immediate bit is set to one. If the
W_IMMED bit is set to zero, then the copy manager shall issue a WRITE FILEMARKS command to the copy
destination tape device with the immediate bit is set to zero.
The FILEMARK COUNT field contents in the WRITE FILEMARKS command sent to the copy destination tape
device shall be set to the value in the FILEMARK COUNT field in the segment descriptor.
6.4.6.14 Space function
The segment descriptor format shown in table 161 instructs the copy manager to send a SPACE command
(see SSC-4) to the destination tape device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 161 for
the space segment descriptor.
Table 161 — Space segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (11h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0008h)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved
CODE
(MSB)
COUNT
(LSB)


Descriptor type code 11h (i.e., spacetape) instructs the copy manager to send a SPACE command to the
copy destination tape device specified by the DESTINATION CSCD DESCRIPTOR ID field. If the PERIPHERAL DEVICE
TYPE field in the CSCD descriptor specified by the DESTINATION CSCD DESCRIPTOR ID field does not contain 01h,
the copy manager shall terminate the copy operation (see 5.17.4.3) originated by the command with CHECK
CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INVALID OPERATION FOR COPY SOURCE OR DESTINATION.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 161 for the space
segment descriptor.
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
The CODE field and COUNT field contents in the SPACE command sent to the copy destination tape device
shall be set to the values in the CODE field and COUNT field in the segment descriptor. All other fields in the
SPACE command sent to the copy destination tape device that affect the positioning of the tape shall be set to
zero.
6.4.6.15 Locate function
The segment descriptor format shown in table 162 instructs the copy manager to send a LOCATE command
(see SSC-4) to the destination tape device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 162 for
the locate segment descriptor.
Descriptor type code 12h (i.e., locatetape) instructs the copy manager to send a LOCATE command to the
copy destination tape device specified by the DESTINATION CSCD DESCRIPTOR ID field. If the PERIPHERAL DEVICE
TYPE field in the CSCD descriptor specified by the DESTINATION CSCD DESCRIPTOR ID field does not contain 01h,
the copy manager shall terminate the copy operation (see 5.17.4.3) originated by the command with CHECK
CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INVALID OPERATION FOR COPY SOURCE OR DESTINATION.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 162 for the locate
segment descriptor.
Table 162 — Locate segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (12h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0008h)
(LSB)
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
LOGICAL OBJECT IDENTIFIER
•••
(LSB)


The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
The LOGICAL OBJECT IDENTIFIER field contents in the LOCATE command sent to the copy destination tape
device shall be set to the value in the LOGICAL OBJECT IDENTIFIER field in the segment descriptor. All other fields
in the LOCATE command sent to the copy destination tape device that affect the positioning of the tape shall
be set to zero.
NOTE 28 - The restrictions described in this subclause for the LOCATE command limit the function to locating
logical block identifiers in the current tape partition.
6.4.6.16 Tape device image copy function
The segment descriptor format shown in table 163 instructs the copy manager to perform an image copy from
the copy source tape device to the copy destination tape device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1 and shall be set as shown in table 163 for
the tape device image copy segment descriptor.
Descriptor type code 13h (i.e., <i>tape<i>tape) instructs the copy manager to create a compatible image of
the copy source specified by the SOURCE CSCD DESCRIPTOR ID field on the copy destination specified by the
DESTINATION CSCD DESCRIPTOR ID field beginning at the current positions of the copy source and the copy
destination. If the PERIPHERAL DEVICE TYPE field in the CSCD descriptor specified by the SOURCE CSCD
DESCRIPTOR ID field or the DESTINATION CSCD DESCRIPTOR ID field does not contain 01h, the copy manager shall
terminate the copy operation (see 5.17.4.3) originated by the command with CHECK CONDITION status, with
the sense key set to COPY ABORTED, and the additional sense code set to INVALID OPERATION FOR
COPY SOURCE OR DESTINATION.
The DESCRIPTOR LENGTH field is described in 6.4.6.1 and shall be set as shown in table 163 for descriptor type
code 13h (i.e., <i>tape<i>tape).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
A COUNT field set to zero specifies that the tape image copy function shall not terminate due to any number of
consecutive filemarks. Other error or exception conditions (e.g., early-warning, end-of-partition on the copy
Table 163 — Tape device image copy segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (13h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0008h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
COUNT
•••
(LSB)


destination) may cause the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command to
terminate prior to completion. If this occurs, the residue shall not be calculated and the INFORMATION field in
the sense data shall be set to zero.
A COUNT field not set to zero specifies that the tape image copy function shall be terminated if the specified
number of consecutive filemarks are copied.
The tape image copy operation terminates when:
a)
the copy source encounters an end-of-partition as defined by the copy source;
b)
the copy source encounters an end-of-data as defined by the copy source (i.e., BLANK CHECK
sense key); or
c)
the copy manager has copied the number of consecutive filemarks specified in the COUNT field from
the copy source to the copy destination.
6.4.6.17 Register persistent reservation key function
The segment descriptor format shown in table 164 instructs the copy manager to register an I_T nexus using
the reservation key (see 5.13.7) specified by the RESERVATION KEY field with the logical unit specified by the
DESTINATION CSCD DESCRIPTOR ID field.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 164 for
the register persistent reservation key segment descriptor.
Table 164 — Register persistent reservation key segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (14h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0018h)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
RESERVATION KEY
•••
(LSB)
(MSB)
SERVICE ACTION RESERVATION KEY
•••
(LSB)
Reserved
•••


Descriptor type code 14h instructs the copy manager to register an I_T nexus using the reservation key
specified by the RESERVATION KEY field with the logical unit specified by the DESTINATION CSCD DESCRIPTOR ID
field using a PERSISTENT RESERVE OUT command with a REGISTER service action (see 6.16.2).
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 164 for the register
persistent reservation key segment descriptor.
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
The RESERVATION KEY field and SERVICE ACTION RESERVATION KEY field contents in the PERSISTENT
RESERVE OUT command sent to the copy destination shall be copied from the RESERVATION KEY field and
SERVICE ACTION RESERVATION KEY field in the segment descriptor.
The application client sending an EXTENDED COPY command that contains a register persistent reservation
key segment descriptor may need to remove the reservation key held by the copy manager as described in
5.13.11 prior to sending the EXTENDED COPY command.
6.4.6.18 Third party persistent reservations source I_T nexus function
The segment descriptor format shown in table 165 instructs the copy manager to send a PERSISTENT
RESERVATION OUT command with REGISTER AND MOVE service action (see 5.13.8) with the specified
I_T nexus after all other segment descriptors have been processed. If an error is detected any time after
receiving a third party persistent source reservation I_T nexus segment descriptor, the PERSISTENT RESER-
VATION OUT command REGISTER AND MOVE service action shall be processed before the copy operation
(see 5.17.4.3) originated by the EXTENDED COPY command is completed.
This segment descriptor should be placed at or near the beginning of the list of segment descriptors to assure
the copy manager processes the PERSISTENT RESERVATION OUT command with REGISTER AND MOVE
service action in the event of an error that terminates the processing of segment descriptors. If an error is
detected in a segment descriptor and third party persistent reservations source I_T nexus segment descriptor
has not been processed, the copy manager shall not send a PERSISTENT RESERVATION OUT command
with REGISTER AND MOVE service action.
Placing more than one source third party persistent reservations source I_T nexus segment descriptor in the
list of descriptors is not an error. All source third party persistent reservations source I_T nexus segment


descriptors known to the copy manager shall be processed after all other segment descriptors have been
processed.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1, and shall be set as shown in table 165 for
the third party persistent reservations source I_T nexus segment descriptor.
Descriptor type code 15h instructs the copy manager to send PERSISTENT RESERVATION OUT command
with REGISTER AND MOVE service action (see 6.16) to the target port specified by the DESTINATION CSCD
DESCRIPTOR ID field.
The DESCRIPTOR LENGTH field is described in 6.4.6.1. The value in the DESCRIPTOR LENGTH field shall be a
multiple of 4.
The DESTINATION CSCD DESCRIPTOR ID field is described in 6.4.6.1.
If the PERIPHERAL DEVICE TYPE field in the CSCD descriptor specified by the DESTINATION CSCD DESCRIPTOR ID
field does not contain 01h, the copy manager shall terminate the copy operation (see 5.17.4.3) originated by
Table 165 — Third party persistent reservations source I_T nexus segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (15h)
Reserved
(MSB)
DESCRIPTOR LENGTH (n-3)
(LSB)
Reserved
Reserved
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
RESERVATION KEY
•••
(LSB)
(MSB)
SERVICE ACTION RESERVATION KEY
•••
(LSB)
Reserved
Reserved
UNREG
APTPL
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
(MSB)
TRANSPORTID LENGTH (n-31)
•••
(LSB)
TransportID
•••
n


the command with CHECK CONDITION status, with the sense key set to COPY ABORTED, and the
additional sense code set to INVALID OPERATION FOR COPY SOURCE OR DESTINATION.
Bytes 8 to n of the third party persistent reservations source I_T nexus segment descriptor shall be sent as the
parameter list (see 6.16.4) for the PERSISTENT RESERVE OUT command with REGISTER AND MOVE
service action.
For a description of the RESERVATION KEY field, SERVICE ACTION RESERVATION KEY field, UNREG bit, APTPL bit,
RELATIVE TARGET PORT IDENTIFIER field, TRANSPORTID LENGTH field, and TransportID, see 6.16.4.
6.4.6.19 Block device image copy function
The segment descriptor format shown in table 166 instructs the copy manager to perform an image copy from
the copy source block device to the copy destination block device.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1 and shall be set as shown in table 166 for
the block device image copy segment descriptor.
Descriptor type code 16h (i.e., <i>block<i>block) instructs the copy manager to copy logical blocks from the
copy source block device specified by the SOURCE CSCD DESCRIPTOR ID field to the copy destination block
device specified by the DESTINATION CSCD DESCRIPTOR ID field while preserving the characteristics (e.g., block
size, protection information) associated with each logical block.
Table 166 — Block device image copy segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (16h)
Reserved
(MSB)
DESCRIPTOR LENGTH (0018h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
STARTING SOURCE LOGICAL BLOCK ADDRESS

•••

(LSB)
(MSB)
STARTING DESTINATION LOGICAL BLOCK ADDRESS

•••

(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS

•••

(LSB)


The copy operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with
CHECK CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INCORRECT COPY TARGET DEVICE TYPE if:
a)
the DISK BLOCK LENGTH field in the device type specific CSCD descriptor parameters (see 6.4.5.3) for
the copy source is not equal to DISK BLOCK LENGTH field in the device type specific CSCD descriptor
parameters for the copy destination; or
b)
the protection information characteristics for the copy source are not the same as the protection infor-
mation characteristics for the copy destination.
While copying logical blocks from the copy source to the copy destination, the copy manager shall preserve
the protection information.
While copying logical blocks from the copy source to the copy destination, the copy manager should preserve
the logical block provisioning information, if any. If the copy manager detects differences between the logical
block provisioning characteristics for the copy source and the logical block provisioning characteristics for the
copy destination that prevent the preservation of logical block provisioning information, then the copy
operation (see 5.17.4.3) originated by the EXTENDED COPY command may be terminated with CHECK
CONDITION status, with the sense key set to COPY ABORTED, and the additional sense code set to
INCORRECT COPY TARGET DEVICE TYPE.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 166 for descriptor type
code 16h (i.e., <i>block<i>block).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The STARTING SOURCE LOGICAL BLOCK ADDRESS field specifies the first logical block to read from the copy
source block device.
The STARTING DESTINATION LOGICAL BLOCK ADDRESS field specifies the first logical block to write on the copy
destination block device.
The NUMBER OF LOGICAL BLOCKS field specifies the number of logical blocks to copy. If the NUMBER OF LOGICAL
BLOCKS field is set to zero, the copy manager shall use FFFF FFFF FFFF FFFFh as the number of logical
blocks to copy.
The copy manager shall copy logical blocks from the copy source to the copy destination beginning at the
specified logical block addresses until:
a)
the specified number of logical blocks are copied;
b)
the maximum logical block address on the copy source is reached; or
c)
the maximum logical block address on the copy destination is reached.
The <i>block<i>block copy function shall be considered a success regardless of which limit on the number
of blocks copied caused the function to end.


6.4.6.20 Populate a ROD from one or more block ranges function
The segment descriptor format shown in table 167 instructs the copy manager to add one or more ranges
from the copy source block device to the end of the ROD that is specified as the copy destination. The copy
operation (see 5.17.4.3) originated by the EXTENDED COPY command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST if the:
a)
PERIPHERAL DEVICE TYPE field in the specified copy source CSCD descriptor is not set to 00h (i.e.,
block device);
b)
PERIPHERAL DEVICE TYPE field in the specified copy destination CSCD descriptor is not set to 00h (i.e.,
block device);
c)
SOURCE CSCD DESCRIPTOR ID field is not set to FFFFh (i.e., the logical unit that contains the copy
manager);
d)
copy destination CSCD descriptor is not a ROD CSCD descriptor (see 6.4.5.9);
e)
ROD TYPE field in the copy destination CSCD descriptor is set to zero; or
f)
same LBA is specified in more than one range descriptor (see 5.17.6.3).
Table 167 — Populate a ROD from one or more block ranges segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (BEh)
Reserved
(MSB)
DESCRIPTOR LENGTH (n-3)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
Reserved

•••

RANGE DESCRIPTOR TYPE
(MSB)
RANGE DESCRIPTORS LENGTH (n-15)
(LSB)
Range descriptors
Range descriptor [first]

•••

•••
Range descriptor [last]
•••

n


The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1 and shall be set as shown in table 167 for
the Populate a ROD from one or more block ranges segment descriptor.
Descriptor type code BEh (i.e., RODblock ranges(n)) instructs the copy manager to add the ranges
specified in the segment descriptor from the copy source specified by the SOURCE CSCD DESCRIPTOR ID field to
the end of the ROD specified by the DESTINATION CSCD DESCRIPTOR ID field.
The DESCRIPTOR LENGTH field is described in 6.4.6.1.
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
The RANGE DESCRIPTOR TYPE field specifies the format of all range descriptors.
The RANGE DESCRIPTORS LENGTH field specifies the number of bytes of range descriptors that follow.
If the RANGE DESCRIPTOR TYPE field is set to 01h, each range descriptor (see table 169) has the format
specified by the RANGE DESCRIPTOR TYPE field.
The LOGICAL BLOCK ADDRESS field specifies the first LBA from the copy source to be added to the copy desti-
nation ROD.
The number of blocks field specifies the number of consecutive LBAs from the copy source to be added to the
copy destination ROD.
Table 168 — RANGE DESCRIPTOR TYPE field
Code
Description
Reference
01h
Four gibi-block range descriptor
table 169
all others
Reserved
Table 169 — Populate a ROD four gibi-block range descriptor format
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


6.4.6.21 Populate a ROD from one block range function
The segment descriptor format shown in table 170 instructs the copy manager to add one range from the copy
source block device to the end of the ROD that is specified as the copy destination. The copy operation (see
5.17.4.3) originated by the EXTENDED COPY command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST if the:
a)
PERIPHERAL DEVICE TYPE field in the specified copy source CSCD descriptor is not set to 00h (i.e.,
block device);
b)
PERIPHERAL DEVICE TYPE field in the specified copy destination CSCD descriptor is not set to 00h (i.e.,
block device);
c)
SOURCE CSCD DESCRIPTOR ID field is not set to FFFFh (i.e., the logical unit that contains the copy
manager);
d)
copy destination CSCD descriptor is not a ROD CSCD descriptor (see 6.4.5.9); or
e)
ROD TYPE field in the copy destination CSCD descriptor is set to zero.
The DESCRIPTOR TYPE CODE field is described in 6.4.4 and 6.4.6.1 and shall be set as shown in table 170 for
the Populate a ROD from one block range segment descriptor.
Descriptor type code BFh (i.e., RODblock range(1)) instructs the copy manager to add the range specified
in the segment descriptor from the copy source specified by the SOURCE CSCD DESCRIPTOR ID field to the end
of the ROD specified by the DESTINATION CSCD DESCRIPTOR ID field.
The DESCRIPTOR LENGTH field is described in 6.4.6.1, and shall be set as shown in table 170 for descriptor type
code BEh (i.e., RODblock range(1)).
The SOURCE CSCD DESCRIPTOR ID field and DESTINATION CSCD DESCRIPTOR ID field are described in 6.4.6.1.
Table 170 — Populate a ROD from one block range segment descriptor
Bit
Byte
DESCRIPTOR TYPE CODE (BFh)
Reserved
(MSB)
DESCRIPTOR LENGTH (0010h)
(LSB)
(MSB)
SOURCE CSCD DESCRIPTOR ID
(LSB)
(MSB)
DESTINATION CSCD DESCRIPTOR ID
(LSB)
(MSB)
LOGICAL BLOCK ADDRESS

•••

(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS

•••

(LSB)


The LOGICAL BLOCK ADDRESS field specifies the first LBA from the copy source to be added to the copy desti-
nation ROD.
The number of blocks field specifies the number of consecutive LBAs from the copy source to be added to the
copy destination ROD.
6.5 EXTENDED COPY(LID1) command
The EXTENDED COPY(LID1) command (see table 171) is a third-party copy command (see 5.17.3) that
provides an SPC-3 compatible means to copy data from one set of copy sources (e.g., a set of source logical
units) to a set of copy destinations (e.g., a set of destination logical units).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 171 for the EXTENDED
COPY(LID1) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 171 for the EXTENDED
COPY(LID1) command.
The PARAMETER LIST LENGTH field is defined in 6.4.1.
The CONTROL byte is defined in SAM-5.
Table 171 — EXTENDED COPY(LID1) command
Bit
Byte
OPERATION CODE (83h)
Reserved
SERVICE ACTION (00h)
Reserved

•••

(MSB)
PARAMETER LIST LENGTH

•••

(LSB)
Reserved
CONTROL


The format of the EXTENDED COPY(LID1) parameter list is shown in table 172.
The LIST IDENTIFIER field is defined in 6.4.3.2.
The STR bit is defined in 6.4.3.1.
The LIST ID USAGE field is defined in 6.4.3.2.
The PRIORITY field is defined in 6.4.3.3.
Table 172 — EXTENDED COPY(LID1) parameter list
Bit
Byte
LIST IDENTIFIER
Reserved
STR
LIST ID USAGE
PRIORITY
(MSB)
CSCD DESCRIPTOR LIST LENGTH (n-15)
(LSB)
Reserved

•••

(MSB)
SEGMENT DESCRIPTOR LIST LENGTH (m-n)
(LSB)
(MSB)
INLINE DATA LENGTH (k-m)
(LSB)
CSCD descriptor list
CSCD descriptor [ID 1] (see 6.4.5)
•••
•••
n-31
CSCD descriptor [ID x] (see 6.4.5)
•••
n
Segment descriptor list
n+1
Segment descriptor [first] (see 6.4.6)
•••
n+1+l
•••
Segment descriptor [first] (see 6.4.6)
•••
m
m+1
Inline data
•••
k


The CSCD DESCRIPTOR LIST LENGTH field is defined in 6.4.3.4.
The SEGMENT DESCRIPTOR LIST LENGTH field is defined in 6.4.3.5.
The INLINE DATA LENGTH field is defined in 6.4.3.6.
The CSCD descriptors are defined in 6.4.3.4 and 6.4.5.
The segment descriptors are defined in 6.4.3.5 and 6.4.6.
The inline data is defined in 6.4.3.6.


6.6 INQUIRY command
6.6.1 INQUIRY command introduction
The INQUIRY command (see table 173) requests that information regarding the logical unit and SCSI target
device be sent to the application client.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 173 for the INQUIRY
command.
An enable vital product data (EVPD) bit set to one specifies that the device server shall return the vital product
data specified by the PAGE CODE field (see 7.8). If the device server does not implement the requested vital
product data page, then the device server shall terminate the command with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
An EVPD bit is set to zero specified that the device server shall return the standard INQUIRY data (see 6.6.2).
If the PAGE CODE field is not set to zero and the EVPD bit is set to zero, then the device server shall terminate
the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
If the EVPD bit is set to one, the PAGE CODE field specifies which page of vital product data information the
device server shall return (see 7.8).
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
In response to an INQUIRY command received by an incorrect logical unit, the SCSI target device shall return
the INQUIRY data with the peripheral qualifier set to the value defined in 6.6.2. The INQUIRY command shall
return CHECK CONDITION status only if the device server is unable to return the requested INQUIRY data.
If an INQUIRY command is received from an initiator port with a pending unit attention condition (i.e., before
the device server reports CHECK CONDITION status), the device server shall perform the INQUIRY
command and shall not clear the unit attention condition (see SAM-5).
The device server should be able to process the INQUIRY command even when an error occurs that prohibits
normal command completion.
Table 173 — INQUIRY command
Bit
Byte
OPERATION CODE (12h)
Reserved
Obsolete
EVPD
PAGE CODE
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL
