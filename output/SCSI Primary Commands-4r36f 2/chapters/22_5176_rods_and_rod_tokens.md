# 5.17.6 RODs and ROD tokens

5.17.6 RODs and ROD tokens
5.17.6.1 RODs and ROD related tokens overview
A ROD provides a way to represent multiple bytes of data that may or may not be addressable as the content
of some media (e.g., one or more ranges of contiguous logical blocks that may be addressed as LBAs
or maintained as a point in time copy (see 5.17.6.2.3) of the contents of the specified LBA ranges). Each ROD
is created and maintained by a copy manager as specified by this standard.
The types of RODs are described in 5.17.6.2. The process of creating and populating a ROD is described in
5.17.6.3.
A ROD token is a token that a copy manager transfers to an application client to represent a specified ROD
outside the copy manager. Application clients may use ROD tokens as follows:
a)
if a valid ROD token is sent to the copy manager that created it, then that copy manager is able to
associate the ROD token with the original ROD and process the data represented by the ROD in
specified ways (e.g., the ways specified by segment descriptors in an EXTENDED COPY command);
b)
if a ROD token is sent to a copy manager other than the copy manager that created it, then the
receiving copy manager may be able to process the data that the ROD token represents by communi-
cating with the copy manager that created the ROD token. The communications between the copy
managers shall conform to the models described in this standard but are not required to use the
commands or data transfer mechanisms described in this standard; and
c)
if a ROD token is transferred from one application client to another by a means outside the scope of
this standard, then the second application client may use the ROD token in any of the ways described
in this subclause.
The format of a ROD token is defined in 5.17.6.4. The interval of time during which the ROD token remains
valid is called the ROD token’s lifetime (see 5.17.6.7).
ROD management tokens (see 5.17.6.4) are used to manage (e.g., delete) ROD tokens.


5.17.6.2 ROD types
5.17.6.2.1 ROD types overview
A copy manager uses the ROD types shown in table 110.
If a third-party copy command requests the creation of a ROD and the copy manager does not have sufficient
resources to create or maintain the ROD, then the copy manager shall terminate the command with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INSUFFICIENT RESOURCES TO CREATE ROD.
A copy manager shall indicate the types of RODs it supports in the Supported ROD Types third-party copy
descriptor (see 7.8.17.9) in the Third-party Copy VPD page.
5.17.6.2.2 Access upon reference type RODs
Access upon reference type RODs are RODs in which the bytes are represented by addressing information
(e.g., their LBAs for block devices). The copy manager that creates the ROD is not required to:
a)
access the bytes until the ROD is used as a copy source or copy destination; or
b)
maintain any specific user data contents in association with the ROD.
Table 110 — ROD types
Type code
ranges
Type code range
applicability
Type codes
defined by
this standard
Description
Reference
0000 0000h
Copy manager
internal ROD
0000 0000h
ROD type specified by
ROD token
command
definition a
0000 0001h to
0000 FFFFh
Reserved
0001 0000h to
FEFF FFFFh
Any device type
0001 0000h
Access upon reference
5.17.6.2.2
0080 0000h
Point in time copy – default
5.17.6.2.3.2
0080 0001h
Point in time copy
– change vulnerable
5.17.6.2.3.3
0080 0002h
Point in time copy
– persistent
5.17.6.2.3.4
0080 FFFFh
Point in time copy – any
5.17.6.2.3.5
all others
in this range
Reserved
FF00 0000h to
FFFF FFEFh
Device type specific
applicable
command
standard
FFFF FFF0h to
FFFF FFFFh
Vendor specific ROD token body and ROD token extension (see 5.17.6.4 and
5.17.6.5)
a Some commands (e.g., an EXTENDED COPY command with the ROD CSCD descriptor (see 6.4.5.9)
in parameter list (see 5.17.7.1)) use this ROD type code when processing a ROD token sent to the copy
manager. Details of such usage are specific to the command.


An access upon reference type ROD shall remain valid as long as the addresses for the bytes remain valid
(e.g., a MODE SELECT command that decreases the number of blocks on a block device in a way that elimi-
nates one of the LBAs in an access upon reference type ROD causes the ROD to become invalid). Invali-
dating a ROD in this way may cause it to become invalid before its specified lifetime (see 5.17.6.7) has
elapsed.
5.17.6.2.3 Point in time copy RODs
5.17.6.2.3.1 Point in time copy RODs overview
Point in time copy RODs are RODs for which the data returned when the ROD is used as a copy source is the
data that was present when the ROD was populated (see 5.17.6.3). The copy manager that creates the ROD
shall maintain the data that populates the ROD for as long as the ROD remains valid (see 5.17.6.7). The
method that the copy manager uses to maintain the data is outside the scope of this standard.
If the copy manager is unable to maintain the data that populates a point in time copy ROD, the copy manager
shall invalidate this type of ROD. Invalidating a ROD in this way may cause it to become invalid before its
specified lifetime (see 5.17.6.7) has elapsed.
If a third-party copy command that originates a copy operation (see table 107 in 5.17.3) specifies a point in
time copy ROD as a copy destination, then the copy operation (see 5.17.4.3) originated by the command shall
be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
5.17.6.2.3.2 Point in time copy – default
A point in time copy – default type ROD is a point in time copy ROD (see 5.17.6.2.3.1) for which the method
that maintains the data that populates the ROD is vendor specific.
5.17.6.2.3.3 Point in time copy – change vulnerable
A point in time copy – change vulnerable type ROD is a point in time copy ROD (see 5.17.6.2.3.1) for which
the copy manager shall create the ROD using the method that consumes the fewest resources without regard
for whether this increases the chance that changes in the data may cause the ROD to become invalid before
its specified lifetime (see 5.17.6.7) has elapsed.
The copy manager may invalidate this type of ROD if the data that populated that ROD when it was created is
modified (e.g., by a write command) or becomes invalid (e.g., a MODE SELECT command decreases the
number of blocks on a block device in a way that eliminates one of the LBAs in the ROD).
5.17.6.2.3.4 Point in time copy – persistent
A point in time copy – persistent type ROD is a point in time copy ROD (see 5.17.6.2.3.1) for which the copy
manager shall maintain the data present when the ROD was populated for the RODs specified lifetime(see
5.17.6.7) regardless of modifications to the data that populated the ROD when it was created.
A point in time copy – persistent type ROD may become invalidated before the specified lifetime for reasons
other than a modification to the data that populated the ROD when it was created (see 5.17.6.7).


5.17.6.2.3.5 Point in time copy – any
A point in time copy – any type ROD is a point in time copy ROD (see 5.17.6.2.3.1) for which the copy
manager shall create the ROD using one of the following ROD types, in order of preference:
1)
point in time copy – persistent (see 5.17.6.2.3.4); or
2)
point in time copy – change vulnerable (see 5.17.6.2.3.3).
If a ROD token (see 5.17.6.4 and 5.17.6.5) is returned for a point in time copy – any type ROD, the value in
the ROD TOKEN field shall indicate the type of ROD the copy manager created (e.g., 0080 0001h for point in
time copy – change vulnerable).
5.17.6.3 Populating a ROD or ROD token
The content of a ROD is established when the ROD is populated. Details of how a ROD is populated are
defined by the command or commands that cause the ROD to become populated.
After a ROD is populated, it may be:
a)
used by later processing steps defined by the command that caused the ROD to be populated (i.e.,
used inside the copy manager that created the ROD); or
b)
used to create a ROD token (see 5.17.6.4) that may be used by application clients and copy
managers in the ways described in 5.17.6.1.
Commands are not required to provide a means to use a ROD inside the copy manager, but any ROD tokens
that a copy manager creates during the processing of a command shall be made available for transfer to the
application client using the RECEIVE ROD TOKEN INFORMATION command (see 6.26).
The format of a ROD token is defined in 5.17.6.4. The interval of time during which the ROD token remains
valid is called the ROD token’s lifetime (see 5.17.6.7).
If a third-party copy command attempts to populate a ROD with the same data more than one time (e.g.,
specifying the same LBA twice), then the copy operation (see 5.17.4.3) originated by the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
EXAMPLE 1 – The EXTENDED COPY(LID4) command (see 6.4) defines a CSCD descriptor that establishes an internal
ROD and segment descriptors that populate that ROD. The populated ROD may be used by other segment descriptors,
and optionally returned as a ROD token using the methods described in this subclause.
EXAMPLE 2 – The POPULATE TOKEN command (see SBC-3) establishes and populates a ROD whose only use is in the
creation of a ROD token that is returned using the methods described in this subclause.


5.17.6.4 ROD token format
The ROD token format is shown in table 111.
Every ROD token shall include the ROD TYPE field and the ROD TOKEN LENGTH field. Except for the ROD TYPE
field and the ROD TOKEN LENGTH field, the definition for any ROD token format may not include the other fields
shown in table 111. At least the fields shown in table 111 shall be included in the ROD token body if:
a)
information about the ROD token is returned by the REPORT ALL ROD TOKENS command (see
6.31); or
b)
any fields are defined in the ROD token extension.
Table 111 — ROD token format
Bit
Byte
ROD token header
(MSB)
ROD TYPE

•••

(LSB)
Reserved
(MSB)
ROD TOKEN LENGTH (n-7)
(LSB)
ROD token body
(MSB)
COPY MANAGER ROD TOKEN IDENTIFIER

•••

(LSB)
CREATOR LOGICAL UNIT DESCRIPTOR

•••

(MSB)
NUMBER OF BYTES REPRESENTED

•••

(LSB)
ROD token type specific data
•••
ROD token extension
Device type specific data
•••
ROD token type and copy manager
specific data
•••
n


EXAMPLE – The block device zero ROD token (see SBC-3) has a value selected from table 110 (see 5.17.6.2.1) in the
ROD TYPE field, and the ROD TOKEN LENGTH field set to 01F8h. All bytes in the ROD token body and ROD token extension
are reserved. This is a valid ROD token format because the block device zero ROD token is not returned by the REPORT
ALL ROD TOKENS command.
Commands that manage ROD tokens (e.g., the REPORT ALL ROD TOKENS command (see 6.31)) use a
ROD management token that consists of the ROD token header and the ROD token body in the ROD token
being managed (i.e., the ROD token extension is omitted in ROD management tokens). The ROD TOKEN
LENGTH field is not modified when the a ROD management token is built from a ROD token (i.e., the ROD
TOKEN LENGTH field does not indicate the length ROD management token).
The ROD TYPE field (see table 110 in 5.17.6.2.1) indicates the use and content of the ROD token that follows
the header.
The ROD TOKEN LENGTH field indicates the number of bytes that follow in the ROD token. The minimum size of
a ROD token shall be 512 bytes (i.e., the minimum value in the ROD TOKEN LENGTH field is 01F8h). Bytes in
unused ROD token fields shall be reserved (e.g., in a ROD token that does not include the ROD token body,
the bytes assigned to the COPY MANAGER ROD TOKEN IDENTIFIER field, CREATOR LOGICAL UNIT DESCRIPTOR field,
and NUMBER OF BYTES REPRESENTED field are reserved).
When present, the COPY MANAGER ROD TOKEN IDENTIFIER field contains a value that differentiates this ROD
token from all other valid ROD tokens created by and known to a specific copy manager. No two ROD tokens
known to a specific copy manager shall have the same value in the COPY MANAGER ROD TOKEN IDENTIFIER
FIELD. After a ROD token becomes invalid, the copy manager should not reuse the copy manager ROD token
identifier value from that ROD token in another ROD token for as long as possible, and shall not reuse that
value until at least 50 000 ROD tokens have been created by that copy manager.
When present, the CREATOR LOGICAL UNIT DESCRIPTOR field contains an Identification Descriptor CSCD
descriptor (see 6.4.5.6) for the logical unit that contains the copy manager that created the ROD token. That
Identification Descriptor CSCD descriptor shall contain a designation descriptor with the DESIGNATOR TYPE
field set to:
a)
2h (i.e., EUI-64-based); or
b)
3h (i.e., NAA).
When present, the NUMBER OF BYTES REPRESENTED field is set to the total number of bytes that the ROD
token represents. If the number of bytes represented by the ROD token is unknown or greater than
FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFEh, then the NUMBER OF BYTES REPRESENTED field shall be set
to FFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFFh. Command standards may define restrictions on the
contents of the NUMBER OF BYTES REPRESENTED field.


5.17.6.5 Generic ROD tokens
5.17.6.5.1 Generic ROD token format
Unless a different format is defined, ROD tokens for the ROD types other than 00h (see table 110 in
5.17.6.2.1) have the format shown in table 112.
Table 112 — Generic ROD token format
Bit
Byte
ROD token header
(MSB)
ROD TYPE

•••

(LSB)
Reserved
(MSB)
ROD TOKEN LENGTH (n-7)
(LSB)
ROD token body
(MSB)
COPY MANAGER ROD TOKEN IDENTIFIER

•••

(LSB)
CREATOR LOGICAL UNIT DESCRIPTOR

•••

(MSB)
NUMBER OF BYTES REPRESENTED

•••

(LSB)
Reserved
•••
ROD token extension
Device type specific data
•••
TARGET DEVICE DESCRIPTOR
•••
t
t+1
EXTENDED ROD TOKEN DATA
•••
n


The ROD TYPE field is described in 5.17.6.2.1 and shall contain one of the values shown in table 113.
The ROD TOKEN LENGTH field is defined in 5.17.6.4, and shall be set to the value shown in table 113 based on
the contents of the ROD TYPE field.
The COPY MANAGER ROD TOKEN IDENTIFIER field, CREATOR LOGICAL UNIT DESCRIPTOR field, and NUMBER OF
BYTES REPRESENTED field are defined in 5.17.6.4.
The device type specific data is specified by the command standard for the peripheral device type indicated by
the CREATOR LOGICAL UNIT DESCRIPTOR field (see 5.17.6.4) (e.g., for peripheral device type 00h, see SBC-3).
The TARGET DEVICE DESCRIPTOR field contains a designation descriptor for the SCSI target device (see 7.8.6)
that contains the logical unit indicated by the descriptor in CREATOR LOGICAL UNIT DESCRIPTOR field. The desig-
nation descriptor shall have the ASSOCIATION field set to 10b (i.e., SCSI target device) and the DESIGNATOR
TYPE field set to:
a)
2h (i.e., EUI-64-based);
b)
3h (i.e., NAA); or
c)
8h (i.e., SCSI name string).
The EXTENDED ROD TOKEN DATA field contains vendor specific data that makes the entire ROD token difficult to
predict or guess. The EXTENDED ROD TOKEN DATA field shall contain at least 256 bits of secure random number
material (see 4.4) generated when the ROD token was created, and may contain information that is used by
the copy manager that created the ROD token to process the ROD token (e.g., an expiration time in a vendor
specific format). The EXTENDED ROD TOKEN DATA field should not contain data that enables an entity outside
the SCSI target device in which the ROD token was created to determine the data (e.g., LBAs or logical
blocks) that the ROD token represents.
Those portions of the EXTENDED ROD TOKEN DATA field that do not contain defined values should be set to
unpredictable random values. The contents of the EXTENDED ROD TOKEN DATA field may be defined to contain:
a)
zero or more values that are based on the ROD represented by the generic ROD token (e.g., pointers,
expiration time); and
b)
zero or more values used by the copy manger to determine whether the generic ROD token is valid
(e.g., cryptographic integrity check values, message authentication codes, digital signatures).
Table 113 — ROD TYPE field in generic ROD
Code
Description
ROD TOKEN
LENGTH field
contents
TARGET DEVICE
DESCRIPTOR
FIELD size
(in bytes)
ROD type
Reference
0001 0000h
Access upon reference
01F8h
5.17.6.2.2
0080 0000h
Point in time copy – default
01F8h
5.17.6.2.3.2
0080 0001h
Point in time copy
– change vulnerable
01F8h
5.17.6.2.3.3
0080 0002h
Point in time copy
– persistent
01F8h
5.17.6.2.3.4
all others
see table 110 in 5.17.6.2.1
NOTE
Subclause 5.17.6.2.3.5 defines the value in the ROD TYPE field if the ROD type
requested is point in time – any.


5.17.6.5.2 Validating generic ROD tokens
5.17.6.5.2.1 Overview of validating generic ROD tokens
A copy manager shall ensure that a generic ROD token (see 5.17.6.5.1) is valid before performing any action
based on the contents of that ROD token. The determination of whether a generic ROD token is valid shall be
performed only by the copy manager that created that ROD token. If the processing copy manager is in the
same SCSI target device as the copy manager that created the ROD token, an exchange of information
between the two copy managers is needed to accomplish the required validation.
If a copy manager is unable to validate the generic ROD token, then no data shall be transferred by the
command that contains the invalid ROD token, and the copy operation (see 5.17.4.3) originated by the
command shall be terminated as described in 5.17.6.5.2.3.
If a command containing a generic ROD token is processed by a copy manager that is not in the same SCSI
target device as the copy manager that created the ROD token, then the actions of the processing copy
manager depend on the contents of the REMOTE TOKENS field in the ROD Features third-party copy descriptor
(see 7.8.17.8) as follows:
a)
if REMOTE TOKENS field is set to 0h, then the processing copy manager may treat the generic ROD
token as invalid without contacting another copy manager (e.g., because the processing copy
manager is unable to identify or contact the copy manager that created the ROD token) and terminate
the command that contains the ROD token as described in 5.17.6.5.2.3; or
b)
if REMOTE TOKENS field is not set to 0h, then the processing copy manager shall:
1)
use the information in the generic ROD token to locate the copy manager that created the ROD
token;
2)
communicate the generic ROD token to the creating copy manager with a request to determine
the validity of the ROD token (e.g., send an EXTENDED COPY command with a verify CSCD
segment descriptor (see 6.4.6.9); and
3)
if the generic ROD token is invalid, then the copy operation (see 5.17.4.3) originated by the
command shall be terminated as described in 5.17.6.5.2.3.
The process of determining the validity of a generic ROD token involves many tests. A generic ROD token:
a)
shall be invalid if the contents the generic ROD token do not match the equivalent information stored
by the copy manager for any ROD token created by the copy manager as described in this subclause;
b)
should be invalid if the generic ROD token’s lifetime has elapsed (see 5.17.6.7); and
c)
may be invalid based on vendor specific tests.
The check for if a generic ROD token matches a generic ROD token created by the copy manager may use:
a)
exact validation that detects all differences (e.g., by comparing the generic ROD token to copies of
valid generic ROD tokens saved by the copy manager when those generic ROD tokens were created)
to which the additional requirements stated in 5.17.6.5.2.2 do not apply; or
b)
inexact validation that does not detect all differences (e.g., by comparing a hash of the generic ROD
token to hashes of valid generic ROD tokens) and implementation of the additional requirements
described in 5.17.6.5.2.2.
If a copy manager determines that a generic ROD token is invalid, the copy operation (see 5.17.4.3) origi-
nated by the command shall be terminated as described in 5.17.6.5.2.3.


5.17.6.5.2.2 Inexact validation of generic ROD tokens
A copy manager may use the SHA-256 secure hash function to:
a)
compute a hash for each generic ROD token as part of creating that generic ROD token; and
b)
compare the equivalent hash for any generic ROD token to be validated to the precomputed hash
values for all generic ROD tokens that the copy manager considers valid.
Any generic ROD token inexact validation process shall detect generic ROD tokens that were never created
by the copy manager with a certainty that is greater than or equal to that of SHA-256 hash (e.g., use of the
SHA-512 secure hash meets this requirement).
A copy manager that uses a secure hash function as the only means of generic ROD token validation is
exposed to collision attacks against that hash function. A more robust technique is to use the secure hash as
part of a keyed cryptographic integrity check (e.g., the HMAC SHA-256 message authentication code), with a
secret key that is confidential to the copy manager.
Copy managers shall not use any of the following computational techniques as the only means of generic
ROD token validation:
a)
any form of CRC;
b)
any form of arithmetic checksum;
c)
an arithmetic hash that is not a secure hash; and
d)
a secure hash with a known collision resistance that is less than that of SHA-256 (e.g., most secure
hash functions whose result contains less than 256 bits).
5.17.6.5.2.3 Validation errors for generic ROD tokens
If the copy manager determines that a generic ROD token is invalid, then the copy manager shall not perform
any of the data transfers requested by the command that specified the invalid ROD token and end command
processing as follows, if the copy manager detects:
1)
an internal inconsistency or corruption problem in the generic ROD token format, then the copy
operation (see 5.17.4.3) originated by the command shall be terminated with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
TOKEN OPERATION, TOKEN CORRUPT;
2)
a type of the generic ROD token that is not supported by the copy manager, then the copy operation
originated by the command shall be terminated with CHECK CONDITION status with the sense key
set to ILLEGAL REQUEST and the additional sense code set to INVALID TOKEN OPERATION,
UNSUPPORTED TOKEN TYPE;
3)
a generic ROD token that was created by a copy manager that is not located in the same SCSI target
device as the processing copy manager, then the how command processing is ended depends on the
contents of the REMOTE TOKENS field in the ROD Features third-party copy descriptor (see 7.8.17.8) as
follows:
A)
if REMOTE TOKENS field is set to 0h, then the copy operation originated by the command shall be
terminated with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID TOKEN OPERATION, REMOTE TOKEN USAGE NOT
SUPPORTED; or
B)
if REMOTE TOKENS field is not set to 0h and the copy manager is unable to contact the copy
manager that created the ROD token, then the copy operation originated by the command shall
be terminated with CHECK CONDITION status with the sense key set to COPY ABORTED and
the additional sense code set to COPY TARGET DEVICE NOT REACHABLE;
4)
a generic ROD token with a lifetime that has expired or an inactivity timeout that has been exceeded
(see 5.17.6.7), then the copy operation originated by the command shall be terminated with CHECK


CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to INVALID TOKEN OPERATION, TOKEN EXPIRED;
5)
a generic ROD token that has been cancelled by the copy manager (see 5.17.6.7), then the copy
operation originated by the command shall be terminated with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID TOKEN
OPERATION, TOKEN CANCELLED;
6)
a generic ROD token that has been revoked by a system administrator (see 5.17.6.7), then the copy
operation originated by the command should be terminated with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID TOKEN
OPERATION, TOKEN REVOKED;
7)
a generic ROD token that has been deleted in response to an application client request (see
5.17.6.7), then the copy operation originated by the command should be terminated with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to INVALID TOKEN OPERATION, TOKEN DELETED; and
8)
a generic ROD token that does not match any valid generic ROD token created by the copy manager,
then the copy operation originated by the command shall be terminated with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
TOKEN OPERATION, TOKEN UNKNOWN.
5.17.6.6 ROD token usage
If the ROD token’s lifetime is long enough to allow all of the following steps to be processed and no other
factors cause the ROD token to become invalid, then creation and use of the ROD token in multiple third-party
copy commands is accomplished as follows:
1)
create a ROD token (see 5.17.7.5.2) in an initial third-party copy command (e.g., EXTENDED
COPY(LID4) command (see 6.4) or POPULATE TOKEN command (see SBC-3));
2)
retrieve the ROD token or ROD tokens using the RECEIVE ROD TOKEN INFORMATION command
(see 6.26); and
3)
one or more subsequent third-party copy commands (e.g., EXTENDED COPY(LID4) command or
WRITE USING TOKEN command (see SBC-3)) may specify the ROD token in the parameter list.
Details of the how the EXTENDED COPY commands are used in the steps shown in this subclause are
described in 5.17.7.6. Details of the how the POPULATE TOKEN command and WRITE USING TOKEN
command are used in the steps shown in this subclause are described in SBC-3.


If a copy manager processes a third-party copy command that contains a valid ROD token in the parameter
list, the response depends on the relationship of the copy manager that processes the command to the copy
manager that created the ROD token as show in table 114.
A copy manager indicates that it is capable of communicating with a copy manager that is not located in the
same SCSI target device as itself by setting the REMOTE TOKENS field to a value other than 0h in the ROD
Features third-party copy descriptor (see 7.8.17.8).
Whenever one copy manager communicates with another copy manager to access the data that the ROD
token represents, the communication is modelled as the sending of EXTENDED COPY(LID4) commands (see
6.4) and RECEIVE COPY DATA(LID4) commands (see 6.20). However, any communication between copy
managers that accomplishes the equivalent of this result conforms to this standard.
EXAMPLE – The process by which one copy manager obtains all the bytes in a ROD may use an EXTENDED
COPY(LID4) command that contains the blockblock +application client segment descriptor (see 6.4.6.4) with a null block
device logical unit (see table 146 in 6.4.6.1) as the copy destination followed by a RECEIVE COPY RESULTS(LID4)
command that retrieves the held data.
In addition to converting a ROD token created by another copy manger to the data that the ROD token repre-
sents, a copy manager may indicate that it is capable of communicating with another copy manager in another
SCSI target device for the purpose of creating a ROD token by setting the REMOTE TOKENS field to 6h in the
ROD Features third-party copy descriptor (see 7.8.17.8).
Table 114 — Copy manager relationships for processing ROD tokens
Relationship between
the copy manager that
processes the command
and the copy manager that
created the ROD token
REMOTE TOKENS
field a contents
returned by the
processing copy
manager
Description
The two copy managers are
the same
n/a
No errors shall be returned based on the valid ROD
token’s contents.
The two copy managers are in
the same SCSI target device
n/a
The processing copy manager shall:
a)
communicate with the copy manager that
created the ROD token to access the data
that the ROD token represents; and
b)
not return any errors based on the valid ROD
token’s contents.
The two copy managers are in
different SCSI target devices
0h
The processing copy manager shall terminate the
copy operation (see 5.17.4.3) originated by the
command as described in 5.17.6.5.2.3.
not 0h
The processing copy manager:
a)
shall attempt to communicate with the
copy manager that created the ROD token
to access the data that the ROD token
represents; and
b)
may return errors based on the inability
to locate or communicate with the copy
manager that created the ROD token
(see 5.17.6.5.2.3).
a The REMOTE TOKENS field is in the ROD Features third-party copy descriptor (see 7.8.17.8).


5.17.6.7 ROD token lifetime
When a ROD token is created, the copy manager that creates the ROD token assigns it a lifetime interval
based on inputs to the ROD token creation process (e.g., the REQUESTED ROD TOKEN LIFETIME field in the ROD
CSCD descriptor (see 6.4.5.9)) that is used as follows:
a)
until the lifetime elapses, the copy manger should not make the ROD token invalid; and
b)
after the lifetime elapses, the copy manager should invalidate the ROD token.
When a ROD token is created, the copy manager that creates the ROD token assigns it an inactivity timeout
that is based on inputs to the ROD token creation process (e.g., the REQUESTED ROD TOKEN INACTIVITY TIMEOUT
field in the ROD CSCD descriptor (see 6.4.5.9)) that is used as follows:
a)
after the completion of a third-party copy command that originates a copy operation (see table 107 in
5.17.3) that specifies the ROD token, the copy manager should not make the ROD token invalid
before the inactivity timeout has expired; and
b)
after the inactivity timeout has expired, the copy manager should invalidate the ROD token.
A ROD token may be invalidated for reasons other than its lifetime elapsing or inactivity timeout expiring,
including the following:
a)
an application client request to delete a ROD token (e.g., setting the DEL_TKN bit to one in the ROD
CSCD descriptor (see 6.4.5.9) of an EXTENDED COPY command);
b)
a ROD token cancellation made by the copy manager in response to operating conditions (e.g., point
in time copy (see 5.17.6.2.3) processing requirements, excessive writes to the represented data,
resource reclamation to create a new ROD token); and
c)
a system administrator request to revoke a ROD token for management reasons.
If any of the conditions described in this subclause cause a ROD token to become invalid, then the copy
manager shall maintain a record of them for reporting purposes (see 5.17.6.5.2.3) for at least the lifetime of
the ROD token established at the time the ROD token was created, and should be maintained a record for
twice the lifetime of the ROD token.
