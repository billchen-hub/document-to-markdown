# 7.8.17 Third-party Copy VPD page

7.8.17 Third-party Copy VPD page
7.8.17.1 Third-party Copy VPD page overview
The Third-party Copy VPD page (see table 643) provides a means to retrieve descriptors that indicate the
capabilities supported by the copy manager (see 5.17.2).
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 643 for the Third-party Copy VPD
page.
The third-party copy descriptors shall be returned in ascending order based on third-party copy descriptor type
values (see 7.8.17.2).
Table 643 — Third-party Copy VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (8Fh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Third-party copy descriptors
Third-party copy descriptor [first]

•••
•••
Third-party copy descriptor [last]
•••
n


7.8.17.2 Third-party copy descriptor format
Each third-party copy descriptor shall have the format shown in table 644. The third-party copy descriptors are
described in 7.8.17.3.
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field indicates the number of bytes of third-party copy parameters
that follow. All third-party copy descriptor lengths are a multiple of four.
The contents of the third-party copy parameters are indicated by the contents of the THIRD-PARTY COPY
DESCRIPTOR TYPE field (see 7.8.17.3).
Table 644 — Third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
Third-party copy parameters
•••

n


7.8.17.3 Third-party copy descriptor type codes
Third-party copy descriptor type codes (see table 645) indicate which third-party copy descriptor is being
returned.

Table 645 — Third-party copy descriptor type codes
Third-party copy descriptor name
Code
Reference
Support
requirements a
Block Device ROD Limits
0000h
SBC-3
Optional b
Supported Commands
0001h
7.8.17.4
Mandatory
Parameter Data
0004h
7.8.17.5
Optional c
Supported Descriptors
0008h
7.8.17.6
Optional c
Supported CSCD IDs
000Ch
7.8.17.7
Optional c
ROD Token Features
0106h
7.8.17.8
Optional d
Supported ROD Token and ROD Types
0108h
7.8.17.9
Optional d
General Copy Operations
8001h
7.8.17.10
Mandatory
Stream Copy Operations
9101h
7.8.17.11
Optional e
Held Data
C001h
7.8.17.12
Optional f
Restricted (see applicable command standard)
E000h to EFFFh
Reserved
All other codes
a Applicable only if the Third-party Copy VPD page is supported.
b Mandatory as defined by the applicable command standard.
c Mandatory if the EXTENDED COPY(LID4) command (see 6.4) or EXTENDED COPY(LID1) command
(see 6.5) is supported.
d Mandatory if the EXTENDED COPY command ROD CSCD descriptor (see 6.4.5.9) is supported or as
defined by the applicable command standard.
e Mandatory if any EXTENDED COPY command stream segment descriptor (see 6.4.6.1) is supported.
f
Mandatory if the RECEIVE COPY DATA(LID4) command (see 6.20) or the RECEIVE COPY
DATA(LID1) command (see 6.21) is supported.


7.8.17.4 Supported Commands third-party copy descriptor
7.8.17.4.1 Supported Commands third-party copy descriptor overview
The Supported Commands third-party copy descriptor (see table 646) indicates which combinations of
operation code and service action the copy manager supports (see 5.17.3). The information provided by the
Supported Commands third-party copy descriptor is equivalent to information returned by the REPORT
SUPPORTED OPERATION CODES command (see 6.35).
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 646
for the Supported Service Actions third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2.
The SUPPORTED SERVICE ACTIONS LIST LENGTH field indicates the length, in bytes, of the list of service actions
descriptors that follow.
Each command support descriptor (see 7.8.17.4.2) lists the service actions that the copy manager supports
for a specific operation code. The Supported Commands third-party copy descriptor shall contain command
support descriptors for at least the following operation codes in ascending order by operation code value:
1)
83h (e.g., the EXTENDED COPY(LID4) command (see 6.4)); and
2)
84h (e.g., the RECEIVE COPY STATUS(LID4) command (see 6.24)).
The DESCRIPTOR PAD field shall contain zero to three bytes set to zero such that the total length of the
Supported Commands third-party copy descriptor is a multiple of four.
Table 646 — Supported Commands third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0001h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
COMMANDS SUPPORTED LIST LENGTH (m-4)
Commands supported list
Command support descriptor (see table 647)
[first]

•••
•••
Command support descriptor (see table 647)
[last]
•••
m
m+1
DESCRIPTOR PAD (if needed)
•••
n


7.8.17.4.2 Command support descriptor format
Each command support descriptor (see table 647) indicates an operation code that the copy manager
supports and the services actions for that operation code that are supported.
The SUPPORTED OPERATION CODE field indicates the operation code for which a list of supported service
actions is being returned.
The SUPPORTED SERVICE ACTIONS LIST LENGTH field indicates the number of supported service action values
that follow.
The list of supported service actions contains one byte for each service action of the operation code indicated
by the SUPPORTED OPERATION CODE field that the copy manager supports, with a unique supported service
action in each byte. The service actions shall appear in the list in ascending numerical order.
Table 647 — Command support descriptor format
Bit
Byte
SUPPORTED OPERATION CODE
SUPPORTED SERVICE ACTIONS LIST LENGTH (m-1)
List of supported service actions
•••
m


7.8.17.5 Parameter Data third-party copy descriptor
The Parameter Data third-party copy descriptor (see table 648) indicates the limits that the copy manager
places on the contents of the EXTENDED COPY command parameter data.
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 648
for the Parameter Data third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2 and shall be set as shown in table
648 for the Parameter Data third-party copy descriptor.
The MAXIMUM CSCD DESCRIPTOR COUNT field indicates the maximum number of CSCD descriptors that the
copy manager allows in an EXTENDED COPY parameter list (see 5.17.7.1).
The MAXIMUM SEGMENT COUNT field indicates the maximum number of segment descriptors that the copy
manager allows in an EXTENDED COPY parameter list (see 5.17.7.1).
The MAXIMUM DESCRIPTOR LIST LENGTH field indicates the maximum length, in bytes, of the CSCD descriptor
list and segment descriptor list that the copy manager allows in an EXTENDED COPY command parameter
list (see 5.17.7.1).
Table 648 — Parameter Data third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0004h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (001Ch)
(LSB)
Reserved

•••

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
MAXIMUM INLINE DATA LENGTH

•••
(LSB)
Reserved

•••


The MAXIMUM INLINE DATA LENGTH field indicates the length, in bytes, of the largest amount of inline data (see
6.4.3.6) that the copy manager supports in an EXTENDED COPY parameter list (see 5.17.7.1). The MAXIMUM
INLINE DATA LENGTH field shall be set to zero if the copy manager does not support descriptor type code 04h
(see 6.4.6.6).
7.8.17.6 Supported Descriptors third-party copy descriptor
The Supported Descriptors third-party copy descriptor (see table 649) indicates which CSCD descriptors (see
6.4.5.1) and segment descriptors (see 6.4.6.1) the copy manager supports.
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 649
for the Supported Descriptors third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2.
The SUPPORTED DESCRIPTOR LIST LENGTH field indicates the length, in bytes, of the list of supported descriptor
type codes that follows.
The list of supported descriptor type codes contains one byte for each CSCD descriptor and segment
descriptor DESCRIPTOR TYPE CODE value (see 6.4.4) supported by the copy manager, with a unique supported
DESCRIPTOR TYPE CODE value in each byte. The descriptor type code values shall appear in the list in
ascending numerical order.
The DESCRIPTOR PAD field shall contain zero to three bytes set to zero such that the total length of the
Supported Descriptors third-party copy descriptor is a multiple of four.
Table 649 — Supported Descriptors third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0008h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
SUPPORTED DESCRIPTOR LIST LENGTH (m-4)
List of supported descriptor type codes
•••
m
m+1
DESCRIPTOR PAD (if needed)
•••
n


7.8.17.7 Supported CSCD IDs third-party copy descriptor
The Supported CSCD IDs third-party copy descriptor (see table 650) indicates which CSCD IDs (see table
131 in 6.4.5.1) other than 0000h  to 07FFh the copy manager supports.
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 650
for the Supported CSCD IDs third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2.
The SUPPORTED CSCD IDS LIST LENGTH field indicates the length, in bytes, of the list of supported CSCD IDs
that follows.
Each SUPPORTED CSCD ID field indicates one unique CSCD ID (see table 131 in 6.4.5.1) with a value greater
than 07FFh that is supported by the copy manger. The CSCD IDs shall appear in the list in ascending
numerical order.
In addition to the CSCD IDs listed in the Supported CSCD IDs third-party copy descriptor, the copy manager
shall support each CSCD ID between zero and one less than the value in the MAXIMUM CSCD DESCRIPTOR
COUNT field in the Parameter Data third-party copy descriptor (see 7.8.17.5).
If the TOKEN_IN bit is set to one in any ROD token descriptor in the Supported ROD Types third-party copy
descriptor (see 7.8.17.9), then F800h shall be included in the CSCD IDs list. F800h shall not be included in
the CSCD IDs list if the:
a)
Supported ROD Types third-party copy descriptor is not included in the Third-party Copy VPD page;
or
Table 650 — Supported CSCD IDs third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (000Ch)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
(MSB)
SUPPORTED CSCD IDS LIST LENGTH (m-5)
(LSB)
Supported CSCD ID list
(MSB)
SUPPORTED CSCD ID [first]
(LSB)
•••
m-1
(MSB)
SUPPORTED CSCD ID [last]
m
(LSB)
m+1
DESCRIPTOR PAD (if needed)
•••

n


b)
TOKEN_IN bit is set to zero in all the ROD token descriptors in the Supported ROD Types third-party
copy descriptor.
The DESCRIPTOR PAD field shall contain zero to three bytes set to zero such that the total length of the
Supported CSCD IDs Descriptors third-party copy descriptor is a multiple of four.


7.8.17.8 ROD Token Features third-party copy descriptor
7.8.17.8.1 ROD Token Features third-party copy descriptor overview
The ROD Token Features third-party copy descriptor (see table 651) indicates the limits that the copy
manager places on processing of ROD tokens by copy operations (see 5.17.4.3).
Table 651 — ROD Token Features third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0106h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
Reserved
REMOTE TOKENS

Reserved

•••

(MSB)
MINIMUM TOKEN LIFETIME

•••
(LSB)
(MSB)
MAXIMUM TOKEN LIFETIME

•••

(LSB)
(MSB)
MAXIMUM TOKEN INACTIVITY TIMEOUT

•••
(LSB)

Reserved

•••

(MSB)
ROD DEVICE TYPE SPECIFIC FEATURES
DESCRIPTORS LENGTH (m-47)
(LSB)
ROD device type specific features descriptors

ROD device type specific features descriptor
[first]

•••

•••

ROD device type specific features descriptor
[last]
•••

m

m+1

DESCRIPTOR PAD (if needed)
•••

n


The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 651
for the ROD Token Features third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2.
The REMOTE TOKENS field (see table 652) indicates the level of support the copy manager provides for ROD
tokens (see 5.17.6) that are not created by the copy manager that is processing the copy operation (see
5.17.4.3).
The MINIMUM TOKEN LIFETIME field indicates the smallest lifetime, in seconds, that the copy manager supports
for a ROD token. If a ROD token lifetime is requested (e.g., if the REQUESTED ROD TOKEN LIFETIME field in a
ROD CSCD descriptor (see 6.4.5.9) specifies a value) that is less than the value in the MINIMUM TOKEN
LIFETIME field, then the ROD token’s lifetime may be set to the value in the MINIMUM TOKEN LIFETIME field.
The MAXIMUM TOKEN LIFETIME field indicates the largest lifetime, in seconds, that the copy manager supports
for a ROD token. If a ROD token lifetime is requested (e.g., if the REQUESTED ROD TOKEN LIFETIME field in a
ROD CSCD descriptor (see 6.4.5.9) specifies a value) that is greater than the value in the MAXIMUM TOKEN
LIFETIME field, then the copy operation (see 5.17.4.3) is terminated (see 6.4.5.9).
The MAXIMUM TOKEN INACTIVITY TIMEOUT field indicates the largest inactivity timeout value, in seconds, that the
copy manager supports for a ROD token. If a ROD token inactivity timeout is requested (e.g., if the REQUESTED
ROD TOKEN INACTIVITY TIMEOUT field in a ROD CSCD descriptor (see 6.4.5.9) specifies a value) that is greater
than the value in the MAXIMUM TOKEN INACTIVITY TIMEOUT field, then the copy operation (see 5.17.4.3) is termi-
nated (see 6.4.5.9). The MAXIMUM TOKEN INACTIVITY TIMEOUT field is also used by the POPULATE TOKEN
command (see SBC-3).
The ROD DEVICE TYPE SPECIFIC FEATURES DESCRIPTORS LENGTH field indicates the length, in bytes, of the ROD
device type specific features descriptors that follow.
Table 652 — REMOTE TOKENS field
Code
Description
0h
The copy manager supports the use of ROD tokens created by itself or any other copy
manager in the same SCSI target device as copy sources and copy destinations, but
does not support creation of ROD tokens that represent any bytes other than those
accessible to its logical unit (e.g., a ROD CSCD descriptor (see 6.4.5.9) in which the
ROD TYPE field is set to zero and the ROD PRODUCER CSCD DESCRIPTOR ID field specifies
a copy manager producer of the ROD that is not copy manager that is processing the
EXTENDED COPY command)
4h
The copy manager supports the use of ROD tokens created by itself or any other copy
manager in any SCSI target device as copy sources and copy destinations, but does
not support creation of ROD tokens that represent any bytes other than those accessi-
ble to its logical unit
6h
The copy manager supports the use of ROD tokens created by itself or any other copy
manager in any SCSI target device as copy sources and copy destinations, and the
creation of ROD tokens that represent any bytes other than those accessible to its log-
ical unit
all others
Reserved


Each ROD device type specific features descriptor provides support information for internal RODs and ROD
tokens associated with a specific device type. The ROD device type specific features descriptors shall be
included in the ROD Token Features third-party copy descriptor in the following order:
1)
zero or one block ROD device type specific feature descriptors (see 7.8.17.8.2);
2)
zero or one stream ROD device type specific feature descriptors (see 7.8.17.8.3); and
3)
zero or one copy manager ROD device type specific features descriptors (see 7.8.17.8.4).
ROD device type specific features descriptors:
a)
shall be included for each device type for which internal RODs or ROD tokens may be generated by
the copy manager; and
b)
shall not be included for any device type for which the copy manager does not generate internal
RODs or ROD tokens.
7.8.17.8.2 Block ROD device type specific features descriptor
The block ROD device type specific features descriptor (see table 653) provides support information for ROD
tokens associated with block type devices.
Table 653 — Block ROD device type specific features descriptor format
Bit
Byte
DESCRIPTOR FORMAT (000b)
PERIPHERAL DEVICE TYPE (00h)
Reserved
(MSB)
DESCRIPTOR LENGTH (002Ch)
(LSB)
Reserved
(MSB)
OPTIMAL BLOCK ROD LENGTH GRANULARITY
(LSB)
(MSB)
MAXIMUM BYTES IN BLOCK ROD

•••

(LSB)
(MSB)
OPTIMAL BYTES IN BLOCK ROD TRANSFER

•••

(LSB)
(MSB)
OPTIMAL BYTES TO TOKEN PER SEGMENT

•••

(LSB)
(MSB)
OPTIMAL BYTES FROM TOKEN PER SEGMENT

•••

(LSB)
Reserved

•••


The DESCRIPTOR FORMAT field indicates the format of the descriptor and shall be set as shown in table 653 for
the block ROD device type specific features descriptor.
The PERIPHERAL DEVICE TYPE field indicates the device type associated with the descriptor and shall be set as
shown in table 653 for the block ROD device type specific features descriptor.
The DESCRIPTOR LENGTH field indicates the number of bytes that follow in the descriptor and shall be set as
shown in table 653 for the block ROD device type specific features descriptor.
The OPTIMAL BLOCK ROD LENGTH GRANULARITY field indicates the optimal size granularity in blocks for a ROD or
ROD token. RODs or ROD tokens with sizes not equal to a multiple of this value may incur significant delays
in processing. If the OPTIMAL BLOCK ROD LENGTH GRANULARITY field is set to zero, then the copy manager does
not report the optimal ROD or ROD token length granularity for a block device.
The MAXIMUM BYTES IN BLOCK ROD field indicates the largest number of bytes the copy manager supports in an
internal ROD or ROD token for a block device. If a third-party copy command (see 5.17.3) attempts to
populate an internal ROD or ROD token with more than the indicated number of bytes, the copy operation
(see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST. If the MAXIMUM BYTES IN BLOCK ROD field is set to zero, then the copy manager does not report a largest
number of bytes the copy manager supports in an internal ROD or ROD token for a block device.
The OPTIMAL BYTES IN BLOCK ROD TRANSFER field indicates the optimal number of bytes the copy manager is
able to transfer in a single third-party copy command (see 5.17.3) or EXTENDED COPY segment descriptor
(see 6.4.6). Significant delays in processing may be incurred if a third-party copy command attempts to
transfer more bytes than indicated by the OPTIMAL BYTES IN BLOCK ROD TRANSFER field to or from a ROD
associated with block device. If the OPTIMAL BYTES IN BLOCK ROD TRANSFER field is set to zero, then the copy
manager does not report the optimal number of bytes the copy manager is able to transfer in a single
third-party copy command for a block device. If the OPTIMAL BYTES IN BLOCK ROD TRANSFER field is set to
FFFF FFFF FFFF FFFFh, then there is no limit on the optimal number of bytes the copy manager is able to
transfer in a single third-party copy command.
The OPTIMAL BYTES TO TOKEN PER SEGMENT field indicates the optimal number of bytes of user data the copy
manager is able to transfer into a ROD associated with a block device in a single segment descriptor (see
6.4.6) or block device range descriptor (see SBC-3). Significant delays in processing may be incurred if a
third-party copy command attempts to transfer more bytes of user data in a single descriptor than indicated by
the OPTIMAL BYTES TO TOKEN PER SEGMENT field to a ROD associated with a block device. If the OPTIMAL BYTES
TO TOKEN PER SEGMENT field is set to zero, then the copy manager does not report the optimal number of bytes
the copy manager is able to transfer in a single descriptor for a block device. If the OPTIMAL BYTES TO TOKEN
PER SEGMENT field is set to FFFF FFFF FFFF FFFFh, then there is no limit on the optimal number of bytes the
copy manager is able to transfer in a single descriptor.
The OPTIMAL BYTES FROM TOKEN PER SEGMENT field indicates the optimal number of bytes of user data the
copy manager is able to transfer from a ROD associated with a block device in a single segment descriptor
(see 6.4.6) or block device range descriptor (see SBC-3). Significant delays in processing may be incurred if a
third-party copy command attempts to transfer more bytes of user data in a single descriptor than indicated by
the OPTIMAL BYTES FROM TOKEN PER SEGMENT field from a ROD associated with a block device. If the OPTIMAL
BYTES FROM TOKEN PER SEGMENT field is set to zero, then the copy manager does not report the optimal
number of bytes the copy manager is able to transfer in a single descriptor for a block device. If the OPTIMAL
BYTES FROM TOKEN PER SEGMENT field is set to FFFF FFFF FFFF FFFFh, then there is no limit on the optimal
number of bytes the copy manager is able to transfer in a single descriptor.


7.8.17.8.3 Stream ROD token device type features descriptor
The stream ROD device type specific features descriptor (see table 654) provides support information for
ROD tokens associated with stream type devices.
The DESCRIPTOR FORMAT field indicates the format of the descriptor and shall be set as shown in table 654 for
the stream ROD device type specific features descriptor.
The PERIPHERAL DEVICE TYPE field indicates the device type associated with the descriptor and shall be set as
shown in table 654 for the stream ROD device type specific features descriptor.
The DESCRIPTOR LENGTH field indicates the number of bytes that follow in the descriptor and shall be set as
shown in table 654 for the stream ROD device type specific features descriptor.
The MAXIMUM BYTES IN STREAM ROD field indicates the largest number of bytes the copy manager supports in
an internal ROD or ROD token for a stream device. If third-party copy command (see 5.17.3) attempts to
populate an internal ROD or ROD token with more than the indicated number of bytes, the copy operation
(see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST. If the MAXIMUM BYTES IN STREAM ROD field is set to zero, then the copy manager does not report a largest
number of bytes the copy manager supports in an internal ROD or ROD token for a stream device.
The OPTIMAL BYTES IN STREAM ROD TRANSFER field indicates the optimal number of bytes the copy manager is
able to transfer in a single third-party copy command (see 5.17.3) or EXTENDED COPY segment descriptor
(see 6.4.6). Significant delays in processing may be incurred if a third-party copy command attempts to
transfer more bytes than indicated by the OPTIMAL BYTES IN STREAM TOKEN TRANSFER field to or from a stream
device. If the OPTIMAL BYTES IN STREAM ROD TRANSFER field is set to zero, then the copy manager does not
report the optimal number of bytes the copy manager is able to transfer in a single third-party copy command
Table 654 — Stream ROD device type specific features descriptor format
Bit
Byte
DESCRIPTOR FORMAT (000b)
PERIPHERAL DEVICE TYPE (01h)
Reserved
(MSB)
DESCRIPTOR LENGTH (002Ch)
(LSB)
Reserved

•••
(MSB)
MAXIMUM BYTES IN STREAM ROD

•••
(LSB)
(MSB)
OPTIMAL BYTES IN STREAM ROD TRANSFER

•••
(LSB)
Reserved

•••


for a stream device. If the OPTIMAL BYTES IN STREAM ROD TRANSFER field is set to FFFF FFFF FFFF FFFFh,
then there is no limit on the optimal number of bytes the copy manager is able to transfer in a single third-party
copy command.
7.8.17.8.4 Copy manager ROD token device type features descriptor
The copy manager ROD device type specific features descriptor (see table 655) provides support information
for ROD tokens associated with copy manager only devices (e.g., devices for which the device server
associated with the copy manager reports a peripheral device type of 03h (i.e., processor) as described in
5.17.2).
The DESCRIPTOR FORMAT field indicates the format of the descriptor and shall be set as shown in table 655 for
the copy manager ROD device type specific features descriptor.
The PERIPHERAL DEVICE TYPE field indicates the device type associated with the descriptor and shall be set as
shown in table 655 for the copy manager ROD device type specific features descriptor.
The DESCRIPTOR LENGTH field indicates the number of bytes that follow in the descriptor and shall be set as
shown in table 655 for the copy manager ROD device type specific features descriptor.
The MAXIMUM BYTES IN PROCESSOR ROD field indicates the largest number of bytes the copy manager supports
in an internal ROD or ROD token for a copy manager only device. If third-party copy command (see 5.17.3)
attempts to populate an internal ROD or ROD token with more than the indicated number of bytes, the copy
operation (see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST. If the MAXIMUM BYTES IN PROCESSOR ROD field is set to zero, then the copy manager does
not report a largest number of bytes the copy manager supports in an internal ROD or ROD token for a copy
manager only device.
Table 655 — Copy manager ROD device type specific features descriptor format
Bit
Byte
DESCRIPTOR FORMAT (000b)
PERIPHERAL DEVICE TYPE (03h)
Reserved
(MSB)
DESCRIPTOR LENGTH (002Ch)
(LSB)
Reserved

•••
(MSB)
MAXIMUM BYTES IN PROCESSOR ROD

•••
(LSB)
(MSB)
OPTIMAL BYTES IN PROCESSOR ROD TRANSFER

•••
(LSB)
Reserved

•••


The OPTIMAL BYTES IN PROCESSOR ROD TRANSFER field indicates the optimal number of bytes the copy
manager is able to transfer in a single third-party copy command (see 5.17.3) or EXTENDED COPY segment
descriptor (see 6.4.6). Significant delays in processing may be incurred if a third-party copy command
attempts to transfer more bytes than indicated by the OPTIMAL BYTES IN PROCESSOR ROD TRANSFER field to or
from a copy manager only device. If the OPTIMAL BYTES IN PROCESSOR ROD TRANSFER field is set to zero, then
the copy manager does not report the optimal number of bytes the copy manager is able to transfer in a single
third-party copy command for a copy manager only device. If the OPTIMAL BYTES IN PROCESSOR ROD TRANSFER
field is set to FFFF FFFF FFFF FFFFh, then there is no limit on the optimal number of bytes the copy
manager is able to transfer in a single third-party copy command.
7.8.17.9 Supported ROD Types third-party copy descriptor
The Supported ROD Types third-party copy descriptor (see table 656) indicates which ROD types (see
5.17.6.2) the copy manager supports and the processing characteristics supported for those types.
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 656
for the Supported ROD Token and ROD Types third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2.
The ROD TYPE DESCRIPTORS LENGTH field indicates the length, in bytes, of the ROD type descriptors that follow.
Table 656 — Supported ROD Types third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (0108h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (n-3)
(LSB)
Reserved
(MSB)
ROD TYPE DESCRIPTORS LENGTH (m-7)
(LSB)
ROD type descriptors
ROD type descriptor (see table 657) [first]

•••
•••
ROD type descriptor (see table 657) [last]
•••
m
m+1
DESCRIPTOR PAD (if needed)
•••
n


Each ROD type descriptor (see 7.8.17.9.1) indicates what support the copy manager provides for a specific
ROD type (see 5.17.6.2).
The ROD type descriptors shall appear in ascending numerical order based on the contents of the ROD TYPE
field (see 7.8.17.9.1).
The DESCRIPTOR PAD field shall contain zero to three bytes set to zero such that the total length of the
Supported ROD Types third-party copy descriptor is a multiple of four.
7.8.17.9.1 ROD type descriptor format
The copy manager’s support for a ROD type (see 5.17.6.2) and the ROD token, if any, associated with that
ROD type is indicated by the ROD type descriptor (see table 657).
The ROD TYPE field indicates the ROD type (see table 110 in 5.17.6.2) for which this ROD type descriptor
indicates copy manager support.
The copy manager shall support a ROD TYPE field set to zero in a ROD CSCD descriptor (see 6.4.5.9), shall
include a ROD type descriptor with the ROD TYPE field set to zero in the Supported ROD Types third-party copy
descriptor (see 7.8.17.9), and shall include CSCD ID F800h in the Supported CSCD IDs third-party copy
descriptor (see 7.8.17.7), if:
a)
the ROD CSCD descriptor is supported; and
b)
any ROD type descriptor contains:
A)
a non-zero value in the ROD TYPE field; and
B)
the TOKEN_IN bit set to one.
An ECPY_INT bit set to one indicates that the copy manager supports use the ROD type indicated by the ROD
TYPE field for internal RODs in the EXTENDED COPY command (see 5.17.7). An ECPY_INT bit set to zero
indicates that the copy manager does not support use the ROD type indicated by the ROD TYPE field for
internal RODs in the EXTENDED COPY command.
A TOKEN_IN bit set to one indicates that the copy manager supports the receipt of ROD tokens (see 5.17.6)
that have the ROD type indicated by the ROD TYPE field by one or more commands that the copy manager
processes. A TOKEN_IN bit set to zero indicates that the copy manager does not support the receipt of ROD
tokens that have the ROD type indicated by the ROD TYPE field.
Table 657 — ROD type descriptor format
Bit
Byte
(MSB)
ROD TYPE

•••

(LSB)
ECPY_INT
Reserved
TOKEN_IN
TOKEN_OUT
Reserved
PREFERENCE INDICATION

Reserved
•••


A TOKEN_OUT bit set to one indicates that the copy manager supports the generation and returning of ROD
tokens (see 5.17.6) that have the ROD type indicated by the ROD TYPE field by one or more commands that
the copy manager processes. A TOKEN_OUT bit set to zero indicates that the copy manager does not support
the generation and returning of ROD tokens that have the ROD type indicated by the ROD TYPE field.
If the ROD TYPE field is set to FFFF 0001h (i.e., if the ROD type is the one used by the block device zero ROD
token (see SBC-3)), then the TOKEN_OUT bit shall be set to zero (i.e., the return of block device zero ROD
tokens is prohibited).
The PREFERENCE INDICATOR field indicates the degree of preference the copy manager provides for the
services (e.g., number of RODs supported as active at the one time, number of ROD tokens supported as
active at the one time, maximum ROD lifetimes supported, performance associated with any aspect of ROD
processing) that are associated with the ROD type indicated by the ROD TYPE field. Except for zero, values in
the PREFERENCE INDICATOR field provide this indication as follows:
a)
larger values indicate a higher degree of preference for the ROD related services; and
b)
smaller value indicate a lower degree of preference for the same ROD related services.
A PREFERENCE INDICATOR field set to zero indicates that:
a)
no ROD preference information is provided, if all PREFERENCE INDICATOR fields in all ROD type
descriptors are set to zero; or
b)
no valid comparison is possible between the preference for the ROD type indicated by the ROD TYPE
field and other ROD types supported by the copy manager, if at least one PREFERENCE INDICATOR field
is not set to zero in another ROD type descriptor.
The sum of the values in all PREFERENCE INDICATOR fields in all ROD type descriptors shall be equal to either
zero or FFFFh.
EXAMPLE – An instance where some PREFERENCE INDICATOR field values are zero and other are non-zero concerns the
block device zero ROD token (see SBC-3). Suppose several copy on reference ROD types are supported in addition to
the block device zero ROD token. Each supported ROD type has a ROD type descriptor, including the ROD type used by
the block device zero ROD token. Further suppose that support for the block device zero ROD token requires so few
resources that its preference is infinite for all practical purposes. Setting the PREFERENCE INDICATOR field values are zero in
the ROD type descriptor for the block device zero ROD token allows the copy manager to better reflect the preferences
among the various copy on reference ROD types.


7.8.17.10 General Copy Operations third-party copy descriptor
The General Copy Operations third-party copy descriptor (see table 660) indicates the limits that the copy
manager places on processing of copy operations (see 5.17.4.3).
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 658
for the General Copy Operations third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2 and shall be set as shown in table
658 for the General Copy Operations third-party copy descriptor.
The TOTAL CONCURRENT COPIES field indicates the maximum number of third-party copy commands (see
5.17.3) that are supported for concurrent processing by the copy manager.
The MAXIMUM IDENTIFIED CONCURRENT COPIES field indicates the maximum number of third-party copy
commands (see 5.17.3) that are not an EXTENDED COPY command with the LIST ID USAGE field (see 6.4.3.2)
set to 11b that are supported for concurrent processing by the copy manager.
The contents of the TOTAL CONCURRENT COPIES field shall be greater than or equal to the contents of the
MAXIMUM IDENTIFIED CONCURRENT COPIES field.
The MAXIMUM SEGMENT LENGTH field indicates the length, in bytes, of the largest amount of data that the copy
manager supports writing via a single segment. Bytes introduced as a result of the PAD bit being set to one
(see 5.17.7.2) are not counted towards this limit. A value of zero indicates that the copy manager places no
limits on the amount of data written by a single segment.
Table 658 — General Copy Operations third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (8001h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (0020h)
(LSB)
(MSB)
TOTAL CONCURRENT COPIES

•••

(LSB)
(MSB)
MAXIMUM IDENTIFIED CONCURRENT COPIES

•••

(LSB)
(MSB)
MAXIMUM SEGMENT LENGTH

(LSB)
DATA SEGMENT GRANULARITY (log 2)
INLINE DATA GRANULARITY (log 2)
Reserved

•••


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
7.8.17.11 Stream Copy Operations third-party copy descriptor
The Stream Copy Operations third-party copy descriptor (see table 660) indicates the limits that the copy
manager places on processing of copy operations (see 5.17.4.3).
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 659
for the Stream Copy Operations third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2 and shall be set as shown in table
659 for the Stream Copy Operations third-party copy descriptor.
The MAXIMUM STREAM DEVICE TRANSFER SIZE field indicates the maximum transfer size, in bytes, supported for
stream devices.
Table 659 — Stream Copy Operations third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (9101h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
MAXIMUM STREAM DEVICE TRANSFER SIZE

•••
(LSB)
Reserved

•••


7.8.17.12 Held Data third-party copy descriptor
The Held Data third-party copy descriptor (see table 660) indicates the limits that the copy manager places on
held data (see 5.17.4.5).
The THIRD-PARTY COPY DESCRIPTOR TYPE field is described in 7.8.17.3 and shall be set as shown in table 660
for the Held Data third-party copy descriptor.
The THIRD-PARTY COPY DESCRIPTOR LENGTH field is described in 7.8.17.2 and shall be set as shown in table
660 for the Held Data third-party copy descriptor.
The HELD DATA LIMIT field indicates the length, in bytes, of the minimum amount of data the copy manager
shall hold for return to the application client as described in 5.17.4.5.
The HELD DATA GRANULARITY field indicates the length of the smallest block of held data (see 5.17.4.5) that the
copy manager shall transfer to the application client in response to a RECEIVE COPY DATA(LID4) command
(see 6.20) or a RECEIVE COPY DATA(LID1) command (see 6.21). The amount of data held by the copy
manager in response to any one function (e.g., one segment descriptor (see 6.4.6)) in a copy operation (see
5.17.4.3) shall be a multiple of this granularity. The HELD DATA GRANULARITY value is expressed as a power of
two.
Table 660 — Held Data third-party copy descriptor format
Bit
Byte
(MSB)
THIRD-PARTY COPY DESCRIPTOR TYPE (C001h)
(LSB)
(MSB)
THIRD-PARTY COPY DESCRIPTOR LENGTH (001Ch)
(LSB)
(MSB)
HELD DATA LIMIT

•••

(LSB)
HELD DATA GRANULARITY (log 2)
Reserved

•••
