# 6.4.2 EXTENDED COPY(LID4) parameter data

6.4.2 EXTENDED COPY(LID4) parameter data
The format of the EXTENDED COPY(LID4) parameter list (see 5.17.7.1) is shown in table 126.
Table 126 — EXTENDED COPY(LID4) parameter list (part 1 of 2)
Bit
Byte
PARAMETER LIST FORMAT (01h)
Reserved
STR
LIST ID USAGE
PRIORITY
(MSB)
HEADER CSCD DESCRIPTOR LIST LENGTH (0020h)
(LSB)
Reserved

•••

Reserved
G_SENSE
IMMED
HEADER CSCD DESCRIPTOR TYPE CODE (FFh)
Reserved

(MSB)
LIST IDENTIFIER

•••

(LSB)
Reserved

•••

(MSB)
CSCD DESCRIPTOR LIST LENGTH (n-47)
(LSB)
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


The PARAMETER LIST FORMAT field (see table 127) specifies the format of the EXTENDED COPY(LID4)
parameter list and shall be set as shown in table 126 for the EXTENDED COPY(LID4) command defined in
this standard.
The STR bit is defined in 6.4.3.1.
The LIST ID USAGE field is defined in 6.4.3.2.
The PRIORITY field is defined in 6.4.3.3.
The HEADER CSCD DESCRIPTOR LIST LENGTH field shall be set as shown in table 126. For compatibility with
SPC-3, this field specifies the length of one CSCD descriptor (i.e., a target descriptor in SPC-3 terms) in which
the descriptor type is invalid. The EXTENDED COPY(LID4) command parameter list format replaces this
descriptor with the fields shown in table 126.
The good with sense data (G_SENSE) bit specifies whether the copy manager is required to return sense data
with GOOD status. If the G_SENSE bit is set to zero, then the copy manager shall not associate sense data with
any command that completes with GOOD status. If the G_SENSE bit is set to one and the EXTENDED
COPY(LID4) command completes with GOOD status, then the copy manager shall associate sense data with
the GOOD status in which the sense key is set to COMPLETED, the additional sense code is set to
EXTENDED COPY INFORMATION AVAILABLE, and the COMMAND-SPECIFIC INFORMATION field is set to
number of segment descriptors the copy manager has processed.
The immediate (IMMED) bit specifies whether the copy manager returns status for the EXTENDED
COPY(LID4) command before the first segment descriptor is processed (see 5.17.7.2). Processing of the
IMMED bit is described in 5.17.4.3.
Segment descriptor list
n+1
Segment descriptor [first] (see 6.4.6)
•••
•••
Segment descriptor [last] (see 6.4.6)
•••
m
m+1
Inline data
•••
k
Table 127 — PARAMETER LIST FORMAT field
Code
Description
01h
The format shown in table 126
all others
Reserved
Table 126 — EXTENDED COPY(LID4) parameter list (part 2 of 2)
Bit
Byte
