# 6.4.3 Shared EXTENDED COPY parameter list fields

The EXTENDED COPY(LID4) command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB if the IMMED bit
is set to one and:
a)
the G_SENSE bit is set to one; or
b)
the LIST ID USAGE field (see 6.4.3.2) is set to 11b.
For interoperability with the EXTENDED COPY command defined in SPC-3, the HEADER CSCD DESCRIPTOR
TYPE CODE field shall be set as shown in table 126.
The LIST IDENTIFIER field is defined in 6.4.3.2.
The CSCD DESCRIPTOR LIST LENGTH field is defined in 6.4.3.4.
The SEGMENT DESCRIPTOR LIST LENGTH field is defined in 6.4.3.5.
The INLINE DATA LENGTH field is defined in 6.4.3.6.
The CSCD descriptors are defined in 6.4.3.4 and 6.4.5.
The segment descriptors are defined in 6.4.3.5 and 6.4.6.
The inline data is defined in 6.4.3.6.
6.4.3 Shared EXTENDED COPY parameter list fields
6.4.3.1 STR bit
A sequential striped (STR) bit set to one specifies to the copy manager that the majority of the block device
references in the parameter list represent sequential access of several striped block devices. This may be
used by the copy manager to perform reads from a copy source block device at any time and in any order
during processing of an EXTENDED COPY command as described in 6.4.5.3. A STR bit set to zero specifies
to the copy manager that disk references, if any, may not be sequential.


6.4.3.2 LIST IDENTIFIER field and LIST ID USAGE field
The LIST IDENTIFIER field identifies the copy operation (see 5.17.4.3) originated by the EXTENDED COPY
command to the copy manager as described in 5.17.4.2. The usage of the LIST IDENTIFIER field depends on the
EXTENDED COPY command being processed and contents of the LIST ID USAGE field as follows:
a)
if the command being processed is an EXTENDED COPY(LID4) command (see 6.4), then the LIST ID
USAGE field specifies the usage of the LIST IDENTIFIER field as shown in table 128; and
b)
if the command being processed is an EXTENDED COPY(LID1) command (see 6.5), then the LIST ID
USAGE field specifies the usage of the LIST IDENTIFIER field as shown in table 129.
Table 128 — LIST ID USAGE field for the EXTENDED COPY(LID4) command
Value
Meaning
00b
The contents of the LIST IDENTIFIER field are defined in 5.17.4.2.
The list identifier value may be used to abort (see 6.3) or to request status for a specific
command sent on a specific I_T nexus (e.g., using the RECEIVE COPY STATUS(LID4)
command (see 6.24)). The copy manager shall hold data, if any, for retrieval by the application
client as described in 5.17.4.5.
01b
Reserved
10b
The contents of the LIST IDENTIFIER field are defined in 5.17.4.2.
The list identifier value may be used to abort (see 6.3) or to request status for a specific
command sent on a specific I_T nexus (e.g., using the RECEIVE COPY STATUS(LID4)
command (see 6.24)). The copy manager may discard all held data (see 5.17.4.5) accessible to
the application client. If the application client requests delivery of data that has been discarded
as a result of the LIST ID USAGE field being set to 10b, then the copy manager shall respond as if
the EXTENDED COPY(LID4) command has not been processed.
11b
If the LIST IDENTIFIER field is not set to zero, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST.
The copy manager shall discard all data accessible to the application client (e.g., using the
RECEIVE COPY STATUS(LID4) command (see 6.24)). If the application client requests delivery
of data that has been discarded as a result the LIST ID USAGE field being set to 11b then the copy
manager shall respond as if the EXTENDED COPY(LID4) command has not been processed.
If the parameter list contains any segment descriptors (see 6.4.6) that require data to be held for
the application client (e.g., the blockblock +application client segment descriptor (see
6.4.6.4)), then the copy operation (see 5.17.4.3) originated by the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN PARAMETER LIST, and no segment descriptors
shall be processed (see 5.17.7.3).


Table 129 — LIST ID USAGE field for the EXTENDED COPY(LID1) command
Value
SNLID bit a
Meaning
00b
0 or 1
The contents of the LIST IDENTIFIER field are defined in 5.17.4.2.
The list identifier value may be used to abort (see 6.3) or to request status for a
specific command sent on a specific I_T nexus (e.g., using the RECEIVE COPY
STATUS(LID4) command (see 6.24)). The copy manager shall hold data, if any,
for retrieval by the application client as described in 5.17.4.5.
01b
Reserved
10b
0 or 1
The contents of the LIST IDENTIFIER field are defined in 5.17.4.2.
The list identifier value may be used to abort (see 6.3) or to request status for a
specific command sent on a specific I_T nexus (e.g., using the RECEIVE COPY
STATUS(LID4) command (see 6.24)). The copy manager may discard all held
data (see 5.17.4.5) accessible to the application client. If the application client
requests delivery of data that has been discarded as a result of the LIST ID
USAGE field being set to 10b, then the copy manager shall respond as if the
EXTENDED COPY(LID1) command has not been processed.
11b
The copy manager shall:
a)
terminate the command with CHECK CONDITION status with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST; or
b)
process the command as if the LIST ID USAGE field is set to 10b.
If the LIST IDENTIFIER field is not set to zero, then the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
The copy manager shall discard all data accessible to the application client
(e.g., using the RECEIVE COPY STATUS(LID4) command (see 6.24)). If the
application client requests delivery of data that has been discarded as a result
the LIST ID USAGE field being set to 11b then the copy manager shall respond as
if the EXTENDED COPY(LID1) command has not been processed.
If the parameter list contains any segment descriptors (see 6.4.6) that require
data to be held for the application client (e.g., the blockblock +application
client segment descriptor (see 6.4.6.4)), then the copy operation (see 5.17.4.3)
originated by the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST, and no segment descriptors
shall be processed (see 5.17.7.3).
a Refers to the SNLID bit in the parameter data for the RECEIVE COPY OPERATING PARAMETERS
command (see 6.22).


If two EXTENDED COPY commands are received with the LIST ID USAGE field set to 00b or 10b, then the one
received more recently shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST, and
no segment descriptors shall be processed (see 5.17.7.3), if:
a)
the copy operation (see 5.17.4.3) originated by the EXTENDED COPY command received less
recently:
A)
contained a LIST IDENTIFIER field set to a specific value (e.g., a LIST IDENTIFIER field set to 50h); and
B)
the parameter list is in one format (i.e., EXTENDED COPY(LID4) command parameter list format
or EXTENDED COPY(LID1) command parameter list format);
and
b)
the EXTENDED COPY command received more recently:
A)
contains a LIST IDENTIFIER field set to the same value (e.g., a LIST IDENTIFIER field set to 50h); and
B)
 the parameter list in the other format.
The copy manager may respond as if the EXTENDED COPY command had never been received, if an
EXTENDED COPY command that had the LIST ID USAGE field set to 10b or 11b in its parameter list is specified
by the LIST IDENTIFIER field in one of the following commands:
a)
the RECEIVE COPY STATUS(LID4) command (see 6.24);
b)
the RECEIVE COPY STATUS(LID1) command (see 6.25);
c)
the RECEIVE COPY DATA(LID4) command (see 6.20);
d)
the RECEIVE COPY DATA(LID1) command (see 6.21);
e)
the RECEIVE COPY FAILURE DETAILS(LID1) command (see 6.23); and
f)
the RECEIVE ROD TOKEN INFORMATION command (see 6.26).
6.4.3.3 PRIORITY field
The PRIORITY field specifies the priority of data transfers resulting from this EXTENDED COPY command
relative to data transfers resulting from other commands being processed by the device server contained
within the same logical unit as the copy manager. All commands other than third-party copy commands have
a priority of 1h. Priority 0h is the highest priority, with increasing values in the PRIORITY field indicating lower
priorities.
6.4.3.4 CSCD DESCRIPTOR LIST LENGTH field and CSCD descriptor list
The CSCD DESCRIPTOR LIST LENGTH field specifies the length in bytes of the CSCD descriptor list that follows
the parameter list header (see 5.17.7.1). An EXTENDED COPY command may reference one or more
CSCDs. Each CSCD is described by a CSCD descriptor (see 6.4.5).
The maximum number of CSCD descriptors permitted within a parameter list is indicated by the MAXIMUM
CSCD DESCRIPTOR COUNT field in the Third-party Copy VPD page Parameter Data descriptor (see 7.8.17.5),
and in the response for the RECEIVE COPY OPERATING PARAMETERS command (see 6.22). If the
number of CSCD descriptors exceeds the allowed number, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to TOO
MANY TARGET DESCRIPTORS.
6.4.3.5 SEGMENT DESCRIPTOR LIST LENGTH field and segment descriptor list
The SEGMENT DESCRIPTOR LIST LENGTH field specifies the length in bytes of the segment descriptor list that
follows the CSCD descriptors (see 5.17.7.1). See 6.4.6 for a detailed description of the segment descriptors.
The maximum number of segment descriptors permitted within a parameter list is indicated by the MAXIMUM
SEGMENT DESCRIPTOR COUNT field in the Third-party Copy VPD page Parameter Data descriptor (see


7.8.17.5), and in the response for the RECEIVE COPY OPERATING PARAMETERS command (see 6.22). If
the number of segment descriptors exceeds the allowed number, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to TOO MANY SEGMENT DESCRIPTORS.
The maximum combined length of the CSCD descriptors and segment descriptors permitted within a
parameter list is indicated by the MAXIMUM DESCRIPTOR LIST LENGTH field in the Third-party Copy VPD page
Parameter Data descriptor (see 7.8.17.5), and in the response for the RECEIVE COPY OPERATING PARAM-
ETERS command (see 6.22). If the combined length of the CSCD descriptors and segment descriptors
exceeds the allowed value, the command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
6.4.3.6 INLINE DATA LENGTH field and inline data
The INLINE DATA LENGTH field specifies the number of bytes of inline data, following the last segment descriptor
(see 5.17.7.1). A value of zero specifies that no inline data is present.
The inline data contains information that is available for:
a)
reference by CSCD descriptors; or
b)
transfer by the copy manager in response to segment descriptors.
6.4.4 Descriptor type codes
CSCD descriptors, the CSCD descriptor extension, and segment descriptors share a single set of code values
(see table 130) that identify the type of descriptor.
Table 130 — EXTENDED COPY descriptor type codes
Descriptor type
Description
Reference
00h to BFh
Segment descriptors
6.4.6
C0h to DFh
Vendor specific descriptors
E0h to FEh
CSCD descriptors
6.4.5
FFh a
CSCD descriptor extension
6.4.5.2
a Use of this descriptor type code is reserved except in byte 32 of a 64 byte CSCD
descriptor (e.g., the IPv6 CSCD descriptor described in 7.6.3.9).
