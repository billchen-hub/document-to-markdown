# C.2.2 Detecting lack of progress in active copy operations

C.2 Tracking copy operation progress
C.2.1 Overview
The following third-party copy commands provide information that tracks the progress of a copy operation:
a)
the RECEIVE COPY STATUS(LID4) command (see 6.24);
b)
the RECEIVE COPY DATA(LID4) command (see 6.20); and
c)
the RECEIVE ROD TOKEN INFORMATION command (see 6.26).
C.2.2 Detecting lack of progress in active copy operations
Defining a datum that a copy manager is able to compute that also changes frequently enough to show
whether or not the copy manager is making progress towards completing an active copy operation is a
delicate balance.
The OPERATION COUNTER field returned in the parameter data for all the commands listed in C.2.1 is the
compromise choice for third-party copy commands, and functions as follows:
a)
each time the copy operation completes processing on a data transfer command that moves data the
OPERATION COUNTER field is incremented;
b)
this continues as long as the copy manager is able to move data;
c)
if the OPERATION COUNTER field reaches the maximum value than allowed in the field, the value wraps
to zero, but the value in the OPERATION COUNTER field still changes; and
d)
if the copy manager stops being able to move data, the value in the OPERATION COUNTER field should
stop changing.


Annex D
(Informative)
Variations between this standard and equivalent security protocols
D.1 IKEv2 protocol details and variations for IKEv2-SCSI
The IKEv2 protocol details and variations defined in RFC 4306 apply to IKEv2-SCSI (i.e., this standard) as
follows:
a)
any SECURITY PROTOCOL OUT command with a transfer length of up to 16 384 bytes is not termi-
nated with an error due to the number of bytes transferred;
b)
the timeout and retransmission mechanisms defined in RFC 4306 are not used by this standard,
instead a new payload is defined to transfer appropriate timeout values to the device server;
c)
each SCSI command used by this standard completes by conveying a status from the device server
to the application client;
d)
the IKEv2 header EXCHANGE TYPE field is reserved in this standard as a result of equivalent infor-
mation being transferred in the SECURITY PROTOCOL OUT command and SECURITY
PROTOCOL IN command CDBs;
e)
the IKEv2 header VERSION bit is reserved in this standard;
f)
this standard uses the pseudo-random functions (PRF) functions defined by RFC 4306;
g)
the key derivation functions defined and used by this standard (see 5.14.3) are equivalent to the
PRF+ found in RFC 4306;
h)
the SA creation transactions defined by this standard are not overlapped. If an application client
attempts to start a second SA creation transaction before the first is completed, the offending
command is terminated as described in 5.14.4.1, but this does not affect the SA creation transaction
that is already in progress;
i)
the NO_PROPOSAL_CHOSEN and INVALID_KE_PAYLOAD notify error types are replaced by the
SA CREATION PARAMETER VALUE INVALID additional sense code (see 7.7.3.9) because
IKEv2-SCSI has a different negotiation structure. As defined in RFC 4306, an IKEv2 initiator offers
one or more proposals to a responder without knowing what is acceptable to the responder, and
chooses a DH group without knowing whether it is acceptable to the responder. These two notify error
types allow the responder to inform the initiator that one or more of its choices are not acceptable. In
contrast, an IKEv2-SCSI application client obtains the device server capabilities in the Device
Capabilities step (see 5.14.4.5) and selects algorithms from them in the Key Exchange step (see
5.14.4.6). An error only occurs if the application client has made an invalid selection, hence the SA
CREATION PARAMETER VALUE INVALID description;
j)
IKEv2 version numbers (see RFC 4306) are used by this standard (see 7.7.3.4), but the ability to
respond to an unsupported version number with the highest version number to be used is not
supported, and this standard does not include checks for version downgrade attacks;
k)
IKEv2 cookies (see RFC 4306) are not used by this standard;
l)
IKEv2 cryptographic algorithm negotiation (see RFC 4306) is replaced by the Device Server Capabil-
ities step (see 5.14.4.5) and the Key Exchange step (see 5.14.4.6) (i.e., the IKEv2 proposal construct
is not used by this standard);
m) in this standard an SA is rekeyed by replacing it with a new SA:
A)
CHILD_SAs are not used by this standard;
B)
the RFC 4306 discussion of CHILD_SAs does not apply to this standard;
C) coexistence of the original SA and the new SA is achieved for rekeying purposes by restricting the
device server's ability to delete SAs to the following cases:
a)
expiration of a timeout (see 7.7.3.5.15);
b)
processing of an IKEv2-SCSI Delete function (see 5.14.4.11); and
c)
responding to an initial contact notification (see 7.7.3.5.9);
and


D) IKEv2 does not support rekeying notification for IKE_SAs, therefore this standard does not
support rekeying notification;
n)
the choice of authentication methods for both transfer directions is negotiated using the
SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and SA_AUTH_IN IKEv2-SCSI
cryptographic algorithm descriptor (see 7.7.3.6.6) during the Key Exchange step (see 5.14.4.6);
o)
the usage of Certificate Encodings in the Certificate payload (see 7.7.3.5.5) and Certificate Request
payload (see 7.7.3.5.6) are constrained as follows:
A)
in accordance with the recommendations in RFC 4718, Certificate Encoding values 01h-03h and
05h-0Ah are prohibited;
B)
this standard forbids the use of URL-based Certificate Encodings (i.e., Certificate Encodings
values 0Ch and 0Dh); and
C) certificate Encoding values that RFC 4306 defines as vendor specific are reserved in this
standard;
p)
deleting an SA requires knowing the SAIs (i.e., SPIs) in both directions and including both SAIs in the
Delete payload. The RFC 4306 description of the Delete payload is vague enough to allow this. The
requirement is consistent with the SCSI model for SAs;
q)
the Vendor ID payload is not used by this standard;
r)
Traffic Selectors (see RFC 4306) are not used by this standard;
s)
the requirements in RFC 4306 on nonces are be followed for the random nonces defined by this
standard;
t)
the RFC 4306 requirements on address and port agility are specific to the user datagram protocol and
the IP protocol and do not apply to this standard;
u)
keys for the Authentication step are generated as defined in RFC 4306;
v)
this standard uses a slightly modified version of the authentication calculations in RFC 4306 (see
7.7.3.5.7);
w) the RFC 4306 sections that describe the following features are not used by this standard:
A)
extensible authentication protocol methods;
B)
generating keying Material for CHILD_SAs;
C) rekeying an IKE SA using CREATE_CHILD_SA;
D) requesting an internal address;
E)
requesting the peer's version;
F)
IPComp;
G) NAT traversal; and
H) explicit congestion notification;
x)
IKEv2 Error Handling (see RFC 4306) is replaced by the use of CHECK CONDITION status and
sense data by this standard. See 7.7.3.9 for details of how errors reported in the Notify payload are
translated to sense data;
y)
IETF standards omit the Integrity transform instead of using AUTH_COMBINED;
z)
the command-response architecture of SCSI makes it difficult to protect the device server against
denial of service attacks, and no such protection is defined by this standard. Protection against denial
of service attacks against the application client is described in 7.7.3.8;
aa) IKEv2-SCSI requires Encrypted Payloads be padded to at least the 4 byte minimum alignment
required by ESP-SCSI, whereas IKEv2 imposes no such requirement; and
ab) the critical (CRIT) bit is set to one in all IKEv2-SCSI payloads defined in this standard and these
payloads are required to be recognized by all IKEv2-SCSI implementations. RFC 4306 sets the
Critical (C) bit to zero in all IKEv2 payloads defined in RFC 4306, and requires that all IKEv2 imple-
mentations recognize all payloads defined in RFC 4306; and
ac) use of the Identification payloads is required by IKEv2-SCSI, whereas IKEv2 allows the Identification
payloads to be omitted.


Where this standard uses IKE payload names (see 7.7.3.4) RFC 4306 uses the shorthand notation shown in
table D.1.
Table D.1 — IKE payload names shorthand
IKE payload name in this standard a
RFC 4306 shorthand b
Security Association
SAi or SAr
Key Exchange
KEi or KEr
Identification – Application Client
IDi
Identification – Device Server
IDr
Certificate
CERTi or CERTr
Certificate Request
CERTREQi
Authentication
AUTHi or AUTHr
Nonce
NONCEi or NONCEr
Notify
N-ICi or N-ICr
Delete
Di
Vendor ID
Vi or Vr
Traffic Selector – Application Client
TSi
Traffic Selector – Device Server
TSr
Encrypted
Ei or Er
Configuration
CPi or CPr
Extensible Authentication
EAPi or EAPr
a To facilitate future enhancements, all IKE payloads are listed in this table, but
not all entries in this table are used in this standard.
b In RFC 4306 the lowercase i indicates initiator and r indicates responder. In this
standard, the initiator is the application client and all such IKE payloads (e.g.,
KEi) appear in a SECURITY PROTOCOL OUT parameter list. The responder is
always the device server in this standard and all such IKE payloads (e.g.,
AUTHr) appear in SECURITY PROTOCOL IN parameter data.


D.2 ESP protocol details and variations for ESP-SCSI
The IKEv2 protocol details and variations defined in RFC 4303 apply to ESP-SCSI (i.e., this standard) as
follows:
a)
this standard requires an integrity check value (ICV field), whereas ESP allows support of confidenti-
ality-only;
b)
this standard does not support traffic flow confidentiality;
c)
this standard does not support the TCP/IP aspects of ESP (e.g., IP addresses, multicast);
d)
this standard requires anti-replay detection using the sequence number, whereas ESP makes this
optional;
e)
this standard does not support the Next Header field, but does reserve space for it in the MUST BE
ZERO field (see table 93 in 5.14.7.3);
f)
this standard requires verification of the padding bytes, when possible;
g)
there is no provision in this standard for generating 'dummy packets'; and
h)
this standard does not support out-of-order parameter data.


Annex E
(informative)
Numeric order codes
E.1 Numeric order codes introduction
This annex contains SCSI additional sense codes, operation codes, diagnostic page codes, log page codes,
mode page codes, VPD page codes, version descriptor values, and T10 IEEE binary identifiers in numeric
order as a reference. In the event of a conflict with between the codes or usage requirements in this annex
and equivalent information in the body of this standard or in any command standard, the normative codes and
usage information is correct.
The information in this annex was complete and accurate at the time of publication. However, the information
is subject to change. Technical Committee T10 of INCITS maintains an electronic copy of this information on
its world wide web site (http://www.t10.org/). In the event that the T10 world wide web site is no longer active,
access may be possible via the INCITS world wide web site (http://www.incits.org), the ANSI world wide web
site (http://www.ansi.org), the IEC site (http://www.iec.ch/), the ISO site (http://www.iso.ch/), or the ISO/IEC
JTC 1 web site (http://www.jtc1.org/).
E.2 Additional sense codes
Table E.1 is a numerical order listing of the additional sense codes (i.e., the ADDITIONAL SENSE CODE field and
ADDITIONAL SENSE CODE QUALIFIER field values returned in sense data).
Table E.1 — ASC and ASCQ assignments (part 1 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description
00h
00h
DT LPWROMAEBKVF
NO ADDITIONAL SENSE INFORMATION
00h
01h
T
FILEMARK DETECTED
00h
02h
T
END-OF-PARTITION/MEDIUM DETECTED
00h
03h
T
SETMARK DETECTED
00h
04h
T
BEGINNING-OF-PARTITION/MEDIUM DETECTED
00h
05h
T L
END-OF-DATA DETECTED
00h
06h
DT LPWROMAEBKVF
I/O PROCESS TERMINATED
00h
07h
T
PROGRAMMABLE EARLY WARNING DETECTED
00h
11h
R
AUDIO PLAY OPERATION IN PROGRESS
00h
12h
R
AUDIO PLAY OPERATION PAUSED
00h
13h
R
AUDIO PLAY OPERATION SUCCESSFULLY COMPLETED
00h
14h
R
AUDIO PLAY OPERATION STOPPED DUE TO ERROR


00h
15h
R
NO CURRENT AUDIO STATUS TO RETURN
00h
16h
DT LPWROMAEBKVF
OPERATION IN PROGRESS
00h
17h
DT L
WROMAEBKVF
CLEANING REQUESTED
00h
18h
T
ERASE OPERATION IN PROGRESS
00h
19h
T
LOCATE OPERATION IN PROGRESS
00h
1Ah
T
REWIND OPERATION IN PROGRESS
00h
1Bh
T
SET CAPACITY OPERATION IN PROGRESS
00h
1Ch
T
VERIFY OPERATION IN PROGRESS
00h
1Dh
DT
B
ATA PASS THROUGH INFORMATION AVAILABLE
00h
1Eh
DT
R
MAEBKV
CONFLICTING SA CREATION REQUEST
00h
1Fh
DT
B
LOGICAL UNIT TRANSITIONING TO ANOTHER POWER CONDITION
00h
20h
DT
P
B
EXTENDED COPY INFORMATION AVAILABLE
01h
00h
D
W
O
BK
NO INDEX/SECTOR SIGNAL
02h
00h
D
WRO
BK
NO SEEK COMPLETE
03h
00h
DT L
W
O
BK
PERIPHERAL DEVICE WRITE FAULT
03h
01h
T
NO WRITE CURRENT
03h
02h
T
EXCESSIVE WRITE ERRORS
04h
00h
DT LPWROMAEBKVF
LOGICAL UNIT NOT READY, CAUSE NOT REPORTABLE
04h
01h
DT LPWROMAEBKVF
LOGICAL UNIT IS IN PROCESS OF BECOMING READY
04h
02h
DT LPWROMAEBKVF
LOGICAL UNIT NOT READY, INITIALIZING COMMAND REQUIRED
04h
03h
DT LPWROMAEBKVF
LOGICAL UNIT NOT READY, MANUAL INTERVENTION REQUIRED
04h
04h
DT L
RO
B
LOGICAL UNIT NOT READY, FORMAT IN PROGRESS
04h
05h
DT
W
O
A
BK
F
LOGICAL UNIT NOT READY, REBUILD IN PROGRESS
04h
06h
DT
W
O
A
BK
LOGICAL UNIT NOT READY, RECALCULATION IN PROGRESS
04h
07h
DT LPWROMAEBKVF
LOGICAL UNIT NOT READY, OPERATION IN PROGRESS
04h
08h
R
LOGICAL UNIT NOT READY, LONG WRITE IN PROGRESS
04h
09h
DT LPWROMAEBKVF
LOGICAL UNIT NOT READY, SELF-TEST IN PROGRESS
04h
0Ah
DT LPWROMAEBKVF
LOGICAL UNIT NOT ACCESSIBLE, ASYMMETRIC ACCESS STATE
TRANSITION
04h
0Bh
DT LPWROMAEBKVF
LOGICAL UNIT NOT ACCESSIBLE, TARGET PORT IN STANDBY STATE
04h
0Ch
DT LPWROMAEBKVF
LOGICAL UNIT NOT ACCESSIBLE, TARGET PORT IN UNAVAILABLE
STATE
04h
0Dh
F
LOGICAL UNIT NOT READY, STRUCTURE CHECK REQUIRED
04h
10h
DT
WROM
B
LOGICAL UNIT NOT READY, AUXILIARY MEMORY NOT ACCESSIBLE
04h
11h
DT
WRO
AEB
VF
LOGICAL UNIT NOT READY, NOTIFY (ENABLE SPINUP) REQUIRED
04h
12h
M
V
LOGICAL UNIT NOT READY, OFFLINE
04h
13h
DT
R
MAEBKV
LOGICAL UNIT NOT READY, SA CREATION IN PROGRESS
04h
14h
D
B
LOGICAL UNIT NOT READY, SPACE ALLOCATION IN PROGRESS
04h
15h
M
LOGICAL UNIT NOT READY, ROBOTICS DISABLED
04h
16h
M
LOGICAL UNIT NOT READY, CONFIGURATION REQUIRED
04h
17h
M
LOGICAL UNIT NOT READY, CALIBRATION REQUIRED
Table E.1 — ASC and ASCQ assignments (part 2 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


04h
18h
M
LOGICAL UNIT NOT READY, A DOOR IS OPEN
04h
19h
M
LOGICAL UNIT NOT READY, OPERATING IN SEQUENTIAL MODE
04h
1Ah
DT
B
LOGICAL UNIT NOT READY, START STOP UNIT COMMAND IN
PROGRESS
04h
1Bh
D
B
LOGICAL UNIT NOT READY, SANITIZE IN PROGRESS
04h
1Ch
DT
MAEB
LOGICAL UNIT NOT READY, ADDITIONAL POWER USE NOT YET
GRANTED
05h
00h
DT L
WROMAEBKVF
LOGICAL UNIT DOES NOT RESPOND TO SELECTION
06h
00h
D
WROM
BK
NO REFERENCE POSITION FOUND
07h
00h
DT L
WROM
BK
MULTIPLE PERIPHERAL DEVICES SELECTED
08h
00h
DT L
WROMAEBKVF
LOGICAL UNIT COMMUNICATION FAILURE
08h
01h
DT L
WROMAEBKVF
LOGICAL UNIT COMMUNICATION TIME-OUT
08h
02h
DT L
WROMAEBKVF
LOGICAL UNIT COMMUNICATION PARITY ERROR
08h
03h
DT
ROM
BK
LOGICAL UNIT COMMUNICATION CRC ERROR (ULTRA-DMA/32)
08h
04h
DT LPWRO
K
UNREACHABLE COPY TARGET
09h
00h
DT
WRO
B
TRACK FOLLOWING ERROR
09h
01h
WRO
K
TRACKING SERVO FAILURE
09h
02h
WRO
K
FOCUS SERVO FAILURE
09h
03h
WRO
SPINDLE SERVO FAILURE
09h
04h
DT
WRO
B
HEAD SELECT FAULT
0Ah
00h
DT LPWROMAEBKVF
ERROR LOG OVERFLOW
0Bh
00h
DT LPWROMAEBKVF
WARNING
0Bh
01h
DT LPWROMAEBKVF
WARNING - SPECIFIED TEMPERATURE EXCEEDED
0Bh
02h
DT LPWROMAEBKVF
WARNING - ENCLOSURE DEGRADED
0Bh
03h
DT LPWROMAEBKVF
WARNING - BACKGROUND SELF-TEST FAILED
0Bh
04h
DT LPWRO
AEBKVF
WARNING - BACKGROUND PRE-SCAN DETECTED MEDIUM ERROR
0Bh
05h
DT LPWRO
AEBKVF
WARNING - BACKGROUND MEDIUM SCAN DETECTED MEDIUM
ERROR
0Bh
06h
DT LPWROMAEBKVF
WARNING - NON-VOLATILE CACHE NOW VOLATILE
0Bh
07h
DT LPWROMAEBKVF
WARNING - DEGRADED POWER TO NON-VOLATILE CACHE
0Bh
08h
DT LPWROMAEBKVF
WARNING - POWER LOSS EXPECTED
0Bh
09h
D
WARNING - DEVICE STATISTICS NOTIFICATION ACTIVE
0Ch
00h
T
R
WRITE ERROR
0Ch
01h
K
WRITE ERROR - RECOVERED WITH AUTO REALLOCATION
0Ch
02h
D
W
O
BK
WRITE ERROR - AUTO REALLOCATION FAILED
0Ch
03h
D
W
O
BK
WRITE ERROR - RECOMMEND REASSIGNMENT
0Ch
04h
DT
W
O
B
COMPRESSION CHECK MISCOMPARE ERROR
0Ch
05h
DT
W
O
B
DATA EXPANSION OCCURRED DURING COMPRESSION
0Ch
06h
DT
W
O
B
BLOCK NOT COMPRESSIBLE
0Ch
07h
R
WRITE ERROR - RECOVERY NEEDED
0Ch
08h
R
WRITE ERROR - RECOVERY FAILED
Table E.1 — ASC and ASCQ assignments (part 3 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


0Ch
09h
R
WRITE ERROR - LOSS OF STREAMING
0Ch
0Ah
R
WRITE ERROR - PADDING BLOCKS ADDED
0Ch
0Bh
DT
WROM
B
AUXILIARY MEMORY WRITE ERROR
0Ch
0Ch
DT LPWRO
AEBKVF
WRITE ERROR - UNEXPECTED UNSOLICITED DATA
0Ch
0Dh
DT LPWRO
AEBKVF
WRITE ERROR - NOT ENOUGH UNSOLICITED DATA
0Ch
0Eh
DT
W
O
BK
MULTIPLE WRITE ERRORS
0Ch
0Fh
R
DEFECTS IN ERROR WINDOW
0Dh
00h
DT LPWRO
A
K
ERROR DETECTED BY THIRD PARTY TEMPORARY INITIATOR
0Dh
01h
DT LPWRO
A
K
THIRD PARTY DEVICE FAILURE
0Dh
02h
DT LPWRO
A
K
COPY TARGET DEVICE NOT REACHABLE
0Dh
03h
DT LPWRO
A
K
INCORRECT COPY TARGET DEVICE TYPE
0Dh
04h
DT LPWRO
A
K
COPY TARGET DEVICE DATA UNDERRUN
0Dh
05h
DT LPWRO
A
K
COPY TARGET DEVICE DATA OVERRUN
0Eh
00h
DT
PWROMAEBK
F
INVALID INFORMATION UNIT
0Eh
01h
DT
PWROMAEBK
F
INFORMATION UNIT TOO SHORT
0Eh
02h
DT
PWROMAEBK
F
INFORMATION UNIT TOO LONG
0Eh
03h
DT
P
R
MAEBK
F
INVALID FIELD IN COMMAND INFORMATION UNIT
0Fh
00h
10h
00h
D
W
O
BK
ID CRC OR ECC ERROR
10h
01h
DT
W
O
LOGICAL BLOCK GUARD CHECK FAILED
10h
02h
DT
W
O
LOGICAL BLOCK APPLICATION TAG CHECK FAILED
10h
03h
DT
W
O
LOGICAL BLOCK REFERENCE TAG CHECK FAILED
10h
04h
T
LOGICAL BLOCK PROTECTION ERROR ON RECOVER BUFFERED
DATA
10h
05h
T
LOGICAL BLOCK PROTECTION METHOD ERROR
11h
00h
DT
WRO
BK
UNRECOVERED READ ERROR
11h
01h
DT
WRO
BK
READ RETRIES EXHAUSTED
11h
02h
DT
WRO
BK
ERROR TOO LONG TO CORRECT
11h
03h
DT
W
O
BK
MULTIPLE READ ERRORS
11h
04h
D
W
O
BK
UNRECOVERED READ ERROR - AUTO REALLOCATE FAILED
11h
05h
WRO
B
L-EC UNCORRECTABLE ERROR
11h
06h
WRO
B
CIRC UNRECOVERED ERROR
11h
07h
W
O
B
DATA RE-SYNCHRONIZATION ERROR
11h
08h
T
INCOMPLETE BLOCK READ
11h
09h
T
NO GAP FOUND
11h
0Ah
DT
O
BK
MISCORRECTED ERROR
11h
0Bh
D
W
O
BK
UNRECOVERED READ ERROR - RECOMMEND REASSIGNMENT
11h
0Ch
D
W
O
BK
UNRECOVERED READ ERROR - RECOMMEND REWRITE THE DATA
11h
0Dh
DT
WRO
B
DE-COMPRESSION CRC ERROR
11h
0Eh
DT
WRO
B
CANNOT DECOMPRESS USING DECLARED ALGORITHM
11h
0Fh
R
ERROR READING UPC/EAN NUMBER
Table E.1 — ASC and ASCQ assignments (part 4 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


11h
10h
R
ERROR READING ISRC NUMBER
11h
11h
R
READ ERROR - LOSS OF STREAMING
11h
12h
DT
WROM
B
AUXILIARY MEMORY READ ERROR
11h
13h
DT LPWRO
AEBKVF
READ ERROR - FAILED RETRANSMISSION REQUEST
11h
14h
D
READ ERROR - LBA MARKED BAD BY APPLICATION CLIENT
12h
00h
D
W
O
BK
ADDRESS MARK NOT FOUND FOR ID FIELD
13h
00h
D
W
O
BK
ADDRESS MARK NOT FOUND FOR DATA FIELD
14h
00h
DT L
WRO
BK
RECORDED ENTITY NOT FOUND
14h
01h
DT
WRO
BK
RECORD NOT FOUND
14h
02h
T
FILEMARK OR SETMARK NOT FOUND
14h
03h
T
END-OF-DATA NOT FOUND
14h
04h
T
BLOCK SEQUENCE ERROR
14h
05h
DT
W
O
BK
RECORD NOT FOUND - RECOMMEND REASSIGNMENT
14h
06h
DT
W
O
BK
RECORD NOT FOUND - DATA AUTO-REALLOCATED
14h
07h
T
LOCATE OPERATION FAILURE
15h
00h
DT L
WROM
BK
RANDOM POSITIONING ERROR
15h
01h
DT L
WROM
BK
MECHANICAL POSITIONING ERROR
15h
02h
DT
WRO
BK
POSITIONING ERROR DETECTED BY READ OF MEDIUM
16h
00h
D
W
O
BK
DATA SYNCHRONIZATION MARK ERROR
16h
01h
D
W
O
BK
DATA SYNC ERROR - DATA REWRITTEN
16h
02h
D
W
O
BK
DATA SYNC ERROR - RECOMMEND REWRITE
16h
03h
D
W
O
BK
DATA SYNC ERROR - DATA AUTO-REALLOCATED
16h
04h
D
W
O
BK
DATA SYNC ERROR - RECOMMEND REASSIGNMENT
17h
00h
DT
WRO
BK
RECOVERED DATA WITH NO ERROR CORRECTION APPLIED
17h
01h
DT
WRO
BK
RECOVERED DATA WITH RETRIES
17h
02h
DT
WRO
BK
RECOVERED DATA WITH POSITIVE HEAD OFFSET
17h
03h
DT
WRO
BK
RECOVERED DATA WITH NEGATIVE HEAD OFFSET
17h
04h
WRO
B
RECOVERED DATA WITH RETRIES AND/OR CIRC APPLIED
17h
05h
D
WRO
BK
RECOVERED DATA USING PREVIOUS SECTOR ID
17h
06h
D
W
O
BK
RECOVERED DATA WITHOUT ECC - DATA AUTO-REALLOCATED
17h
07h
D
WRO
BK
RECOVERED DATA WITHOUT ECC - RECOMMEND REASSIGNMENT
17h
08h
D
WRO
BK
RECOVERED DATA WITHOUT ECC - RECOMMEND REWRITE
17h
09h
D
WRO
BK
RECOVERED DATA WITHOUT ECC - DATA REWRITTEN
18h
00h
DT
WRO
BK
RECOVERED DATA WITH ERROR CORRECTION APPLIED
18h
01h
D
WRO
BK
RECOVERED DATA WITH ERROR CORR. & RETRIES APPLIED
18h
02h
D
WRO
BK
RECOVERED DATA - DATA AUTO-REALLOCATED
18h
03h
R
RECOVERED DATA WITH CIRC
18h
04h
R
RECOVERED DATA WITH L-EC
18h
05h
D
WRO
BK
RECOVERED DATA - RECOMMEND REASSIGNMENT
18h
06h
D
WRO
BK
RECOVERED DATA - RECOMMEND REWRITE
18h
07h
D
W
O
BK
RECOVERED DATA WITH ECC - DATA REWRITTEN
Table E.1 — ASC and ASCQ assignments (part 5 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


18h
08h
R
RECOVERED DATA WITH LINKING
19h
00h
D
O
K
DEFECT LIST ERROR
19h
01h
D
O
K
DEFECT LIST NOT AVAILABLE
19h
02h
D
O
K
DEFECT LIST ERROR IN PRIMARY LIST
19h
03h
D
O
K
DEFECT LIST ERROR IN GROWN LIST
1Ah
00h
DT LPWROMAEBKVF
PARAMETER LIST LENGTH ERROR
1Bh
00h
DT LPWROMAEBKVF
SYNCHRONOUS DATA TRANSFER ERROR
1Ch
00h
D
O
BK
DEFECT LIST NOT FOUND
1Ch
01h
D
O
BK
PRIMARY DEFECT LIST NOT FOUND
1Ch
02h
D
O
BK
GROWN DEFECT LIST NOT FOUND
1Dh
00h
DT
WRO
BK
MISCOMPARE DURING VERIFY OPERATION
1Dh
01h
D
B
MISCOMPARE VERIFY OF UNMAPPED LBA
1Eh
00h
D
W
O
BK
RECOVERED ID WITH ECC CORRECTION
1Fh
00h
D
O
K
PARTIAL DEFECT LIST TRANSFER
20h
00h
DT LPWROMAEBKVF
INVALID COMMAND OPERATION CODE
20h
01h
DT
PWROMAEBK
ACCESS DENIED - INITIATOR PENDING-ENROLLED
20h
02h
DT
PWROMAEBK
ACCESS DENIED - NO ACCESS RIGHTS
20h
03h
DT
PWROMAEBK
ACCESS DENIED - INVALID MGMT ID KEY
20h
04h
T
ILLEGAL COMMAND WHILE IN WRITE CAPABLE STATE
20h
05h
T
Obsolete
20h
06h
T
ILLEGAL COMMAND WHILE IN EXPLICIT ADDRESS MODE
20h
07h
T
ILLEGAL COMMAND WHILE IN IMPLICIT ADDRESS MODE
20h
08h
DT
PWROMAEBK
ACCESS DENIED - ENROLLMENT CONFLICT
20h
09h
DT
PWROMAEBK
ACCESS DENIED - INVALID LU IDENTIFIER
20h
0Ah
DT
PWROMAEBK
ACCESS DENIED - INVALID PROXY TOKEN
20h
0Bh
DT
PWROMAEBK
ACCESS DENIED - ACL LUN CONFLICT
20h
0Ch
T
ILLEGAL COMMAND WHEN NOT IN APPEND-ONLY MODE
21h
00h
DT
WRO
BK
LOGICAL BLOCK ADDRESS OUT OF RANGE
21h
01h
DT
WROM
BK
INVALID ELEMENT ADDRESS
21h
02h
R
INVALID ADDRESS FOR WRITE
21h
03h
R
INVALID WRITE CROSSING LAYER JUMP
22h
00h
D
ILLEGAL FUNCTION (USE 20 00, 24 00, OR 26 00)
23h
00h
DT
P
B
INVALID TOKEN OPERATION, CAUSE NOT REPORTABLE
23h
01h
DT
P
B
INVALID TOKEN OPERATION, UNSUPPORTED TOKEN TYPE
23h
02h
DT
P
B
INVALID TOKEN OPERATION, REMOTE TOKEN USAGE NOT
SUPPORTED
23h
03h
DT
P
B
INVALID TOKEN OPERATION, REMOTE ROD TOKEN CREATION NOT
SUPPORTED
23h
04h
DT
P
B
INVALID TOKEN OPERATION, TOKEN UNKNOWN
23h
05h
DT
P
B
INVALID TOKEN OPERATION, TOKEN CORRUPT
23h
06h
DT
P
B
INVALID TOKEN OPERATION, TOKEN REVOKED
Table E.1 — ASC and ASCQ assignments (part 6 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


23h
07h
DT
P
B
INVALID TOKEN OPERATION, TOKEN EXPIRED
23h
08h
DT
P
B
INVALID TOKEN OPERATION, TOKEN CANCELLED
23h
09h
DT
P
B
INVALID TOKEN OPERATION, TOKEN DELETED
23h
0Ah
DT
P
B
INVALID TOKEN OPERATION, INVALID TOKEN LENGTH
24h
00h
DT LPWROMAEBKVF
INVALID FIELD IN CDB
24h
01h
DT LPWRO
AEBKVF
CDB DECRYPTION ERROR
24h
02h
T
Obsolete
24h
03h
T
Obsolete
24h
04h
F
SECURITY AUDIT VALUE FROZEN
24h
05h
F
SECURITY WORKING KEY FROZEN
24h
06h
F
NONCE NOT UNIQUE
24h
07h
F
NONCE TIMESTAMP OUT OF RANGE
24h
08h
DT
R
MAEBKV
INVALID XCDB
25h
00h
DT LPWROMAEBKVF
LOGICAL UNIT NOT SUPPORTED
26h
00h
DT LPWROMAEBKVF
INVALID FIELD IN PARAMETER LIST
26h
01h
DT LPWROMAEBKVF
PARAMETER NOT SUPPORTED
26h
02h
DT LPWROMAEBKVF
PARAMETER VALUE INVALID
26h
03h
DT LPWROMAE
K
THRESHOLD PARAMETERS NOT SUPPORTED
26h
04h
DT LPWROMAEBKVF
INVALID RELEASE OF PERSISTENT RESERVATION
26h
05h
DT LPWRO
A
BK
DATA DECRYPTION ERROR
26h
06h
DT LPWRO
K
TOO MANY TARGET DESCRIPTORS
26h
07h
DT LPWRO
K
UNSUPPORTED TARGET DESCRIPTOR TYPE CODE
26h
08h
DT LPWRO
K
TOO MANY SEGMENT DESCRIPTORS
26h
09h
DT LPWRO
K
UNSUPPORTED SEGMENT DESCRIPTOR TYPE CODE
26h
0Ah
DT LPWRO
K
UNEXPECTED INEXACT SEGMENT
26h
0Bh
DT LPWRO
K
INLINE DATA LENGTH EXCEEDED
26h
0Ch
DT LPWRO
K
INVALID OPERATION FOR COPY SOURCE OR DESTINATION
26h
0Dh
DT LPWRO
K
COPY SEGMENT GRANULARITY VIOLATION
26h
0Eh
DT
PWROMAEBK
INVALID PARAMETER WHILE PORT IS ENABLED
26h
0Fh
F
INVALID DATA-OUT BUFFER INTEGRITY CHECK VALUE
26h
10h
T
DATA DECRYPTION KEY FAIL LIMIT REACHED
26h
11h
T
INCOMPLETE KEY-ASSOCIATED DATA SET
26h
12h
T
VENDOR SPECIFIC KEY REFERENCE NOT FOUND
27h
00h
DT
WRO
BK
WRITE PROTECTED
27h
01h
DT
WRO
BK
HARDWARE WRITE PROTECTED
27h
02h
DT
WRO
BK
LOGICAL UNIT SOFTWARE WRITE PROTECTED
27h
03h
T
R
ASSOCIATED WRITE PROTECT
27h
04h
T
R
PERSISTENT WRITE PROTECT
27h
05h
T
R
PERMANENT WRITE PROTECT
27h
06h
R
F
CONDITIONAL WRITE PROTECT
27h
07h
D
B
SPACE ALLOCATION FAILED WRITE PROTECT
Table E.1 — ASC and ASCQ assignments (part 7 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


28h
00h
DT LPWROMAEBKVF
NOT READY TO READY CHANGE, MEDIUM MAY HAVE CHANGED
28h
01h
DT
WROM
B
IMPORT OR EXPORT ELEMENT ACCESSED
28h
02h
R
FORMAT-LAYER MAY HAVE CHANGED
28h
03h
M
IMPORT/EXPORT ELEMENT ACCESSED, MEDIUM CHANGED
29h
00h
DT LPWROMAEBKVF
POWER ON, RESET, OR BUS DEVICE RESET OCCURRED
29h
01h
DT LPWROMAEBKVF
POWER ON OCCURRED
29h
02h
DT LPWROMAEBKVF
SCSI BUS RESET OCCURRED
29h
03h
DT LPWROMAEBKVF
BUS DEVICE RESET FUNCTION OCCURRED
29h
04h
DT LPWROMAEBKVF
DEVICE INTERNAL RESET
29h
05h
DT LPWROMAEBKVF
TRANSCEIVER MODE CHANGED TO SINGLE-ENDED
29h
06h
DT LPWROMAEBKVF
TRANSCEIVER MODE CHANGED TO LVD
29h
07h
DT LPWROMAEBKVF
I_T NEXUS LOSS OCCURRED
2Ah
00h
DT L
WROMAEBKVF
PARAMETERS CHANGED
2Ah
01h
DT L
WROMAEBKVF
MODE PARAMETERS CHANGED
2Ah
02h
DT L
WROMAE
K
LOG PARAMETERS CHANGED
2Ah
03h
DT LPWROMAE
K
RESERVATIONS PREEMPTED
2Ah
04h
DT LPWROMAE
RESERVATIONS RELEASED
2Ah
05h
DT LPWROMAE
REGISTRATIONS PREEMPTED
2Ah
06h
DT LPWROMAEBKVF
ASYMMETRIC ACCESS STATE CHANGED
2Ah
07h
DT LPWROMAEBKVF
IMPLICIT ASYMMETRIC ACCESS STATE TRANSITION FAILED
2Ah
08h
DT
WROMAEBKVF
PRIORITY CHANGED
2Ah
09h
D
CAPACITY DATA HAS CHANGED
2Ah
0Ah
DT
ERROR HISTORY I_T NEXUS CLEARED
2Ah
0Bh
DT
ERROR HISTORY SNAPSHOT RELEASED
2Ah
0Ch
F
ERROR RECOVERY ATTRIBUTES HAVE CHANGED
2Ah
0Dh
T
DATA ENCRYPTION CAPABILITIES CHANGED
2Ah
10h
DT
M
E
V
TIMESTAMP CHANGED
2Ah
11h
T
DATA ENCRYPTION PARAMETERS CHANGED BY ANOTHER I_T
NEXUS
2Ah
12h
T
DATA ENCRYPTION PARAMETERS CHANGED BY VENDOR SPECIFIC
EVENT
2Ah
13h
T
DATA ENCRYPTION KEY INSTANCE COUNTER HAS CHANGED
2Ah
14h
DT
R
MAEBKV
SA CREATION CAPABILITIES DATA HAS CHANGED
2Ah
15h
T
M
V
MEDIUM REMOVAL PREVENTION PREEMPTED
2Bh
00h
DT LPWRO
K
COPY CANNOT EXECUTE SINCE HOST CANNOT DISCONNECT
2Ch
00h
DT LPWROMAEBKVF
COMMAND SEQUENCE ERROR
2Ch
01h
TOO MANY WINDOWS SPECIFIED
2Ch
02h
INVALID COMBINATION OF WINDOWS SPECIFIED
2Ch
03h
R
CURRENT PROGRAM AREA IS NOT EMPTY
2Ch
04h
R
CURRENT PROGRAM AREA IS EMPTY
2Ch
05h
B
ILLEGAL POWER CONDITION REQUEST
Table E.1 — ASC and ASCQ assignments (part 8 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


2Ch
06h
R
PERSISTENT PREVENT CONFLICT
2Ch
07h
DT LPWROMAEBKVF
PREVIOUS BUSY STATUS
2Ch
08h
DT LPWROMAEBKVF
PREVIOUS TASK SET FULL STATUS
2Ch
09h
DT LPWROM
EBKVF
PREVIOUS RESERVATION CONFLICT STATUS
2Ch
0Ah
F
PARTITION OR COLLECTION CONTAINS USER OBJECTS
2Ch
0Bh
T
NOT RESERVED
2Ch
0Ch
D
ORWRITE GENERATION DOES NOT MATCH
2Dh
00h
T
OVERWRITE ERROR ON UPDATE IN PLACE
2Eh
00h
R
INSUFFICIENT TIME FOR OPERATION
2Fh
00h
DT LPWROMAEBKVF
COMMANDS CLEARED BY ANOTHER INITIATOR
2Fh
01h
D
COMMANDS CLEARED BY POWER LOSS NOTIFICATION
2Fh
02h
DT LPWROMAEBKVF
COMMANDS CLEARED BY DEVICE SERVER
30h
00h
DT
WROM
BK
INCOMPATIBLE MEDIUM INSTALLED
30h
01h
DT
WRO
BK
CANNOT READ MEDIUM - UNKNOWN FORMAT
30h
02h
DT
WRO
BK
CANNOT READ MEDIUM - INCOMPATIBLE FORMAT
30h
03h
DT
R
M
K
CLEANING CARTRIDGE INSTALLED
30h
04h
DT
WRO
BK
CANNOT WRITE MEDIUM - UNKNOWN FORMAT
30h
05h
DT
WRO
BK
CANNOT WRITE MEDIUM - INCOMPATIBLE FORMAT
30h
06h
DT
WRO
B
CANNOT FORMAT MEDIUM - INCOMPATIBLE MEDIUM
30h
07h
DT L
WROMAEBKVF
CLEANING FAILURE
30h
08h
R
CANNOT WRITE - APPLICATION CODE MISMATCH
30h
09h
R
CURRENT SESSION NOT FIXATED FOR APPEND
30h
0Ah
DT
WRO
AEBK
CLEANING REQUEST REJECTED
30h
0Ch
T
WORM MEDIUM - OVERWRITE ATTEMPTED
30h
0Dh
T
WORM MEDIUM - INTEGRITY CHECK
30h
10h
R
MEDIUM NOT FORMATTED
30h
11h
M
INCOMPATIBLE VOLUME TYPE
30h
12h
M
INCOMPATIBLE VOLUME QUALIFIER
30h
13h
M
CLEANING VOLUME EXPIRED
31h
00h
DT
WRO
BK
MEDIUM FORMAT CORRUPTED
31h
01h
D
L
RO
B
FORMAT COMMAND FAILED
31h
02h
R
ZONED FORMATTING FAILED DUE TO SPARE LINKING
31h
03h
D
B
SANITIZE COMMAND FAILED
32h
00h
D
W
O
BK
NO DEFECT SPARE LOCATION AVAILABLE
32h
01h
D
W
O
BK
DEFECT LIST UPDATE FAILURE
33h
00h
T
TAPE LENGTH ERROR
34h
00h
DT LPWROMAEBKVF
ENCLOSURE FAILURE
35h
00h
DT LPWROMAEBKVF
ENCLOSURE SERVICES FAILURE
35h
01h
DT LPWROMAEBKVF
UNSUPPORTED ENCLOSURE FUNCTION
35h
02h
DT LPWROMAEBKVF
ENCLOSURE SERVICES UNAVAILABLE
35h
03h
DT LPWROMAEBKVF
ENCLOSURE SERVICES TRANSFER FAILURE
Table E.1 — ASC and ASCQ assignments (part 9 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


35h
04h
DT LPWROMAEBKVF
ENCLOSURE SERVICES TRANSFER REFUSED
35h
05h
DT L
WROMAEBKVF
ENCLOSURE SERVICES CHECKSUM ERROR
36h
00h
L
RIBBON, INK, OR TONER FAILURE
37h
00h
DT L
WROMAEBKVF
ROUNDED PARAMETER
38h
00h
B
EVENT STATUS NOTIFICATION
38h
02h
B
ESN - POWER MANAGEMENT CLASS EVENT
38h
04h
B
ESN - MEDIA CLASS EVENT
38h
06h
B
ESN - DEVICE BUSY CLASS EVENT
38h
07h
D
THIN PROVISIONING SOFT THRESHOLD REACHED
39h
00h
DT L
WROMAE
K
SAVING PARAMETERS NOT SUPPORTED
3Ah
00h
DT L
WROM
BK
MEDIUM NOT PRESENT
3Ah
01h
DT
WROM
BK
MEDIUM NOT PRESENT - TRAY CLOSED
3Ah
02h
DT
WROM
BK
MEDIUM NOT PRESENT - TRAY OPEN
3Ah
03h
DT
WROM
B
MEDIUM NOT PRESENT - LOADABLE
3Ah
04h
DT
WRO
B
MEDIUM NOT PRESENT - MEDIUM AUXILIARY MEMORY ACCESSIBLE
3Bh
00h
T L
SEQUENTIAL POSITIONING ERROR
3Bh
01h
T
TAPE POSITION ERROR AT BEGINNING-OF-MEDIUM
3Bh
02h
T
TAPE POSITION ERROR AT END-OF-MEDIUM
3Bh
03h
L
TAPE OR ELECTRONIC VERTICAL FORMS UNIT NOT READY
3Bh
04h
L
SLEW FAILURE
3Bh
05h
L
PAPER JAM
3Bh
06h
L
FAILED TO SENSE TOP-OF-FORM
3Bh
07h
L
FAILED TO SENSE BOTTOM-OF-FORM
3Bh
08h
T
REPOSITION ERROR
3Bh
09h
READ PAST END OF MEDIUM
3Bh
0Ah
READ PAST BEGINNING OF MEDIUM
3Bh
0Bh
POSITION PAST END OF MEDIUM
3Bh
0Ch
T
POSITION PAST BEGINNING OF MEDIUM
3Bh
0Dh
DT
WROM
BK
MEDIUM DESTINATION ELEMENT FULL
3Bh
0Eh
DT
WROM
BK
MEDIUM SOURCE ELEMENT EMPTY
3Bh
0Fh
R
END OF MEDIUM REACHED
3Bh
11h
DT
WROM
BK
MEDIUM MAGAZINE NOT ACCESSIBLE
3Bh
12h
DT
WROM
BK
MEDIUM MAGAZINE REMOVED
3Bh
13h
DT
WROM
BK
MEDIUM MAGAZINE INSERTED
3Bh
14h
DT
WROM
BK
MEDIUM MAGAZINE LOCKED
3Bh
15h
DT
WROM
BK
MEDIUM MAGAZINE UNLOCKED
3Bh
16h
R
MECHANICAL POSITIONING OR CHANGER ERROR
3Bh
17h
F
READ PAST END OF USER OBJECT
3Bh
18h
M
ELEMENT DISABLED
3Bh
19h
M
ELEMENT ENABLED
3Bh
1Ah
M
DATA TRANSFER DEVICE REMOVED
Table E.1 — ASC and ASCQ assignments (part 10 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


3Bh
1Bh
M
DATA TRANSFER DEVICE INSERTED
3Bh
1Ch
T
TOO MANY LOGICAL OBJECTS ON PARTITION TO SUPPORT
OPERATION
3Ch
00h
3Dh
00h
DT LPWROMAE
K
INVALID BITS IN IDENTIFY MESSAGE
3Eh
00h
DT LPWROMAEBKVF
LOGICAL UNIT HAS NOT SELF-CONFIGURED YET
3Eh
01h
DT LPWROMAEBKVF
LOGICAL UNIT FAILURE
3Eh
02h
DT LPWROMAEBKVF
TIMEOUT ON LOGICAL UNIT
3Eh
03h
DT LPWROMAEBKVF
LOGICAL UNIT FAILED SELF-TEST
3Eh
04h
DT LPWROMAEBKVF
LOGICAL UNIT UNABLE TO UPDATE SELF-TEST LOG
3Fh
00h
DT LPWROMAEBKVF
TARGET OPERATING CONDITIONS HAVE CHANGED
3Fh
01h
DT LPWROMAEBKVF
MICROCODE HAS BEEN CHANGED
3Fh
02h
DT LPWROM
BK
CHANGED OPERATING DEFINITION
3Fh
03h
DT LPWROMAEBKVF
INQUIRY DATA HAS CHANGED
3Fh
04h
DT
WROMAEBK
COMPONENT DEVICE ATTACHED
3Fh
05h
DT
WROMAEBK
DEVICE IDENTIFIER CHANGED
3Fh
06h
DT
WROMAEB
REDUNDANCY GROUP CREATED OR MODIFIED
3Fh
07h
DT
WROMAEB
REDUNDANCY GROUP DELETED
3Fh
08h
DT
WROMAEB
SPARE CREATED OR MODIFIED
3Fh
09h
DT
WROMAEB
SPARE DELETED
3Fh
0Ah
DT
WROMAEBK
VOLUME SET CREATED OR MODIFIED
3Fh
0Bh
DT
WROMAEBK
VOLUME SET DELETED
3Fh
0Ch
DT
WROMAEBK
VOLUME SET DEASSIGNED
3Fh
0Dh
DT
WROMAEBK
VOLUME SET REASSIGNED
3Fh
0Eh
DT LPWROMAE
REPORTED LUNS DATA HAS CHANGED
3Fh
0Fh
DT LPWROMAEBKVF
ECHO BUFFER OVERWRITTEN
3Fh
10h
DT
WROM
B
MEDIUM LOADABLE
3Fh
11h
DT
WROM
B
MEDIUM AUXILIARY MEMORY ACCESSIBLE
3Fh
12h
DT LPWR
MAEBK
F
iSCSI IP ADDRESS ADDED
3Fh
13h
DT LPWR
MAEBK
F
iSCSI IP ADDRESS REMOVED
3Fh
14h
DT LPWR
MAEBK
F
iSCSI IP ADDRESS CHANGED
40h
00h
D
RAM FAILURE (SHOULD USE 40 NN)
40h
NNh
DT LPWROMAEBKVF
DIAGNOSTIC FAILURE ON COMPONENT NN (80h-FFh)
41h
00h
D
DATA PATH FAILURE (SHOULD USE 40 NN)
42h
00h
D
POWER-ON OR SELF-TEST FAILURE (SHOULD USE 40 NN)
43h
00h
DT LPWROMAEBKVF
MESSAGE ERROR
44h
00h
DT LPWROMAEBKVF
INTERNAL TARGET FAILURE
44h
01h
DT
P
MAEBKVF
PERSISTENT RESERVATION INFORMATION LOST
44h
71h
DT
B
ATA DEVICE FAILED SET FEATURES
45h
00h
DT LPWROMAEBKVF
SELECT OR RESELECT FAILURE
46h
00h
DT LPWROM
BK
UNSUCCESSFUL SOFT RESET
Table E.1 — ASC and ASCQ assignments (part 11 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


47h
00h
DT LPWROMAEBKVF
SCSI PARITY ERROR
47h
01h
DT LPWROMAEBKVF
DATA PHASE CRC ERROR DETECTED
47h
02h
DT LPWROMAEBKVF
SCSI PARITY ERROR DETECTED DURING ST DATA PHASE
47h
03h
DT LPWROMAEBKVF
INFORMATION UNIT iuCRC ERROR DETECTED
47h
04h
DT LPWROMAEBKVF
ASYNCHRONOUS INFORMATION PROTECTION ERROR DETECTED
47h
05h
DT LPWROMAEBKVF
PROTOCOL SERVICE CRC ERROR
47h
06h
DT
MAEBKVF
PHY TEST FUNCTION IN PROGRESS
47h
7Fh
DT
PWROMAEBK
SOME COMMANDS CLEARED BY ISCSI PROTOCOL EVENT
48h
00h
DT LPWROMAEBKVF
INITIATOR DETECTED ERROR MESSAGE RECEIVED
49h
00h
DT LPWROMAEBKVF
INVALID MESSAGE ERROR
4Ah
00h
DT LPWROMAEBKVF
COMMAND PHASE ERROR
4Bh
00h
DT LPWROMAEBKVF
DATA PHASE ERROR
4Bh
01h
DT
PWROMAEBK
INVALID TARGET PORT TRANSFER TAG RECEIVED
4Bh
02h
DT
PWROMAEBK
TOO MUCH WRITE DATA
4Bh
03h
DT
PWROMAEBK
ACK/NAK TIMEOUT
4Bh
04h
DT
PWROMAEBK
NAK RECEIVED
4Bh
05h
DT
PWROMAEBK
DATA OFFSET ERROR
4Bh
06h
DT
PWROMAEBK
INITIATOR RESPONSE TIMEOUT
4Bh
07h
DT
PWROMAEBK
F
CONNECTION LOST
4Ch
00h
DT LPWROMAEBKVF
LOGICAL UNIT FAILED SELF-CONFIGURATION
4Dh
NNh
DT LPWROMAEBKVF
TAGGED OVERLAPPED COMMANDS (NN = TASK TAG)
4Eh
00h
DT LPWROMAEBKVF
OVERLAPPED COMMANDS ATTEMPTED
4Fh
00h
50h
00h
T
WRITE APPEND ERROR
50h
01h
T
WRITE APPEND POSITION ERROR
50h
02h
T
POSITION ERROR RELATED TO TIMING
51h
00h
T
RO
ERASE FAILURE
51h
01h
R
ERASE FAILURE - INCOMPLETE ERASE OPERATION DETECTED
52h
00h
T
CARTRIDGE FAULT
53h
00h
DT L
WROM
BK
MEDIA LOAD OR EJECT FAILED
53h
01h
T
UNLOAD TAPE FAILURE
53h
02h
DT
WROM
BK
MEDIUM REMOVAL PREVENTED
53h
03h
M
MEDIUM REMOVAL PREVENTED BY DATA TRANSFER ELEMENT
53h
04h
T
MEDIUM THREAD OR UNTHREAD FAILURE
53h
05h
M
VOLUME IDENTIFIER INVALID
53h
06h
M
VOLUME IDENTIFIER MISSING
53h
07h
M
DUPLICATE VOLUME IDENTIFIER
53h
08h
M
ELEMENT STATUS UNKNOWN
54h
00h
P
SCSI TO HOST SYSTEM INTERFACE FAILURE
55h
00h
P
SYSTEM RESOURCE FAILURE
55h
01h
D
O
BK
SYSTEM BUFFER FULL
Table E.1 — ASC and ASCQ assignments (part 12 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


55h
02h
DT LPWROMAE
K
INSUFFICIENT RESERVATION RESOURCES
55h
03h
DT LPWROMAE
K
INSUFFICIENT RESOURCES
55h
04h
DT LPWROMAE
K
INSUFFICIENT REGISTRATION RESOURCES
55h
05h
DT
PWROMAEBK
INSUFFICIENT ACCESS CONTROL RESOURCES
55h
06h
DT
WROM
B
AUXILIARY MEMORY OUT OF SPACE
55h
07h
F
QUOTA ERROR
55h
08h
T
MAXIMUM NUMBER OF SUPPLEMENTAL DECRYPTION KEYS
EXCEEDED
55h
09h
M
MEDIUM AUXILIARY MEMORY NOT ACCESSIBLE
55h
0Ah
M
DATA CURRENTLY UNAVAILABLE
55h
0Bh
DT LPWROMAEBKVF
INSUFFICIENT POWER FOR OPERATION
55h
0Ch
DT
P
B
INSUFFICIENT RESOURCES TO CREATE ROD
55h
0Dh
DT
P
B
INSUFFICIENT RESOURCES TO CREATE ROD TOKEN
56h
00h
57h
00h
R
UNABLE TO RECOVER TABLE-OF-CONTENTS
58h
00h
O
GENERATION DOES NOT EXIST
59h
00h
O
UPDATED BLOCK READ
5Ah
00h
DT LPWRO
BK
OPERATOR REQUEST OR STATE CHANGE INPUT
5Ah
01h
DT
WROM
BK
OPERATOR MEDIUM REMOVAL REQUEST
5Ah
02h
DT
WRO
A
BK
OPERATOR SELECTED WRITE PROTECT
5Ah
03h
DT
WRO
A
BK
OPERATOR SELECTED WRITE PERMIT
5Bh
00h
DT LPWROM
K
LOG EXCEPTION
5Bh
01h
DT LPWROM
K
THRESHOLD CONDITION MET
5Bh
02h
DT LPWROM
K
LOG COUNTER AT MAXIMUM
5Bh
03h
DT LPWROM
K
LOG LIST CODES EXHAUSTED
5Ch
00h
D
O
RPL STATUS CHANGE
5Ch
01h
D
O
SPINDLES SYNCHRONIZED
5Ch
02h
D
O
SPINDLES NOT SYNCHRONIZED
5Dh
00h
DT LPWROMAEBKVF
FAILURE PREDICTION THRESHOLD EXCEEDED
5Dh
01h
R
B
MEDIA FAILURE PREDICTION THRESHOLD EXCEEDED
5Dh
02h
R
LOGICAL UNIT FAILURE PREDICTION THRESHOLD EXCEEDED
5Dh
03h
R
SPARE AREA EXHAUSTION PREDICTION THRESHOLD EXCEEDED
5Dh
10h
D
B
HARDWARE IMPENDING FAILURE GENERAL HARD DRIVE FAILURE
5Dh
11h
D
B
HARDWARE IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
12h
D
B
HARDWARE IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
13h
D
B
HARDWARE IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
14h
D
B
HARDWARE IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
15h
D
B
HARDWARE IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
16h
D
B
HARDWARE IMPENDING FAILURE START UNIT TIMES TOO HIGH
5Dh
17h
D
B
HARDWARE IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
18h
D
B
HARDWARE IMPENDING FAILURE CONTROLLER DETECTED
Table E.1 — ASC and ASCQ assignments (part 13 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


5Dh
19h
D
B
HARDWARE IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
1Ah
D
B
HARDWARE IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
1Bh
D
B
HARDWARE IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
1Ch
D
B
HARDWARE IMPENDING FAILURE DRIVE CALIBRATION RETRY
COUNT
5Dh
20h
D
B
CONTROLLER IMPENDING FAILURE GENERAL HARD DRIVE FAILURE
5Dh
21h
D
B
CONTROLLER IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
22h
D
B
CONTROLLER IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
23h
D
B
CONTROLLER IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
24h
D
B
CONTROLLER IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
25h
D
B
CONTROLLER IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
26h
D
B
CONTROLLER IMPENDING FAILURE START UNIT TIMES TOO HIGH
5Dh
27h
D
B
CONTROLLER IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
28h
D
B
CONTROLLER IMPENDING FAILURE CONTROLLER DETECTED
5Dh
29h
D
B
CONTROLLER IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
2Ah
D
B
CONTROLLER IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
2Bh
D
B
CONTROLLER IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
2Ch
D
B
CONTROLLER IMPENDING FAILURE DRIVE CALIBRATION RETRY
COUNT
5Dh
30h
D
B
DATA CHANNEL IMPENDING FAILURE GENERAL HARD DRIVE
FAILURE
5Dh
31h
D
B
DATA CHANNEL IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
32h
D
B
DATA CHANNEL IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
33h
D
B
DATA CHANNEL IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
34h
D
B
DATA CHANNEL IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
35h
D
B
DATA CHANNEL IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
36h
D
B
DATA CHANNEL IMPENDING FAILURE START UNIT TIMES TOO HIGH
5Dh
37h
D
B
DATA CHANNEL IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
38h
D
B
DATA CHANNEL IMPENDING FAILURE CONTROLLER DETECTED
5Dh
39h
D
B
DATA CHANNEL IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
3Ah
D
B
DATA CHANNEL IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
3Bh
D
B
DATA CHANNEL IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
3Ch
D
B
DATA CHANNEL IMPENDING FAILURE DRIVE CALIBRATION RETRY
COUNT
5Dh
40h
D
B
SERVO IMPENDING FAILURE GENERAL HARD DRIVE FAILURE
5Dh
41h
D
B
SERVO IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
42h
D
B
SERVO IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
43h
D
B
SERVO IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
44h
D
B
SERVO IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
45h
D
B
SERVO IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
46h
D
B
SERVO IMPENDING FAILURE START UNIT TIMES TOO HIGH
Table E.1 — ASC and ASCQ assignments (part 14 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


5Dh
47h
D
B
SERVO IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
48h
D
B
SERVO IMPENDING FAILURE CONTROLLER DETECTED
5Dh
49h
D
B
SERVO IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
4Ah
D
B
SERVO IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
4Bh
D
B
SERVO IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
4Ch
D
B
SERVO IMPENDING FAILURE DRIVE CALIBRATION RETRY COUNT
5Dh
50h
D
B
SPINDLE IMPENDING FAILURE GENERAL HARD DRIVE FAILURE
5Dh
51h
D
B
SPINDLE IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
52h
D
B
SPINDLE IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
53h
D
B
SPINDLE IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
54h
D
B
SPINDLE IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
55h
D
B
SPINDLE IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
56h
D
B
SPINDLE IMPENDING FAILURE START UNIT TIMES TOO HIGH
5Dh
57h
D
B
SPINDLE IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
58h
D
B
SPINDLE IMPENDING FAILURE CONTROLLER DETECTED
5Dh
59h
D
B
SPINDLE IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
5Ah
D
B
SPINDLE IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
5Bh
D
B
SPINDLE IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
5Ch
D
B
SPINDLE IMPENDING FAILURE DRIVE CALIBRATION RETRY COUNT
5Dh
60h
D
B
FIRMWARE IMPENDING FAILURE GENERAL HARD DRIVE FAILURE
5Dh
61h
D
B
FIRMWARE IMPENDING FAILURE DRIVE ERROR RATE TOO HIGH
5Dh
62h
D
B
FIRMWARE IMPENDING FAILURE DATA ERROR RATE TOO HIGH
5Dh
63h
D
B
FIRMWARE IMPENDING FAILURE SEEK ERROR RATE TOO HIGH
5Dh
64h
D
B
FIRMWARE IMPENDING FAILURE TOO MANY BLOCK REASSIGNS
5Dh
65h
D
B
FIRMWARE IMPENDING FAILURE ACCESS TIMES TOO HIGH
5Dh
66h
D
B
FIRMWARE IMPENDING FAILURE START UNIT TIMES TOO HIGH
5Dh
67h
D
B
FIRMWARE IMPENDING FAILURE CHANNEL PARAMETRICS
5Dh
68h
D
B
FIRMWARE IMPENDING FAILURE CONTROLLER DETECTED
5Dh
69h
D
B
FIRMWARE IMPENDING FAILURE THROUGHPUT PERFORMANCE
5Dh
6Ah
D
B
FIRMWARE IMPENDING FAILURE SEEK TIME PERFORMANCE
5Dh
6Bh
D
B
FIRMWARE IMPENDING FAILURE SPIN-UP RETRY COUNT
5Dh
6Ch
D
B
FIRMWARE IMPENDING FAILURE DRIVE CALIBRATION RETRY COUNT
5Dh
FFh
DT LPWROMAEBKVF
FAILURE PREDICTION THRESHOLD EXCEEDED (FALSE)
5Eh
00h
DT LPWRO
A
K
LOW POWER CONDITION ON
5Eh
01h
DT LPWRO
A
K
IDLE CONDITION ACTIVATED BY TIMER
5Eh
02h
DT LPWRO
A
K
STANDBY CONDITION ACTIVATED BY TIMER
5Eh
03h
DT LPWRO
A
K
IDLE CONDITION ACTIVATED BY COMMAND
5Eh
04h
DT LPWRO
A
K
STANDBY CONDITION ACTIVATED BY COMMAND
5Eh
05h
DT LPWRO
A
K
IDLE_B CONDITION ACTIVATED BY TIMER
5Eh
06h
DT LPWRO
A
K
IDLE_B CONDITION ACTIVATED BY COMMAND
5Eh
07h
DT LPWRO
A
K
IDLE_C CONDITION ACTIVATED BY TIMER
Table E.1 — ASC and ASCQ assignments (part 15 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


5Eh
08h
DT LPWRO
A
K
IDLE_C CONDITION ACTIVATED BY COMMAND
5Eh
09h
DT LPWRO
A
K
STANDBY_Y CONDITION ACTIVATED BY TIMER
5Eh
0Ah
DT LPWRO
A
K
STANDBY_Y CONDITION ACTIVATED BY COMMAND
5Eh
41h
B
POWER STATE CHANGE TO ACTIVE
5Eh
42h
B
POWER STATE CHANGE TO IDLE
5Eh
43h
B
POWER STATE CHANGE TO STANDBY
5Eh
45h
B
POWER STATE CHANGE TO SLEEP
5Eh
47h
BK
POWER STATE CHANGE TO DEVICE CONTROL
5Fh
00h
60h
00h
LAMP FAILURE
61h
00h
VIDEO ACQUISITION ERROR
61h
01h
UNABLE TO ACQUIRE VIDEO
61h
02h
OUT OF FOCUS
62h
00h
SCAN HEAD POSITIONING ERROR
63h
00h
R
END OF USER AREA ENCOUNTERED ON THIS TRACK
63h
01h
R
PACKET DOES NOT FIT IN AVAILABLE SPACE
64h
00h
R
ILLEGAL MODE FOR THIS TRACK
64h
01h
R
INVALID PACKET SIZE
65h
00h
DT LPWROMAEBKVF
VOLTAGE FAULT
66h
00h
AUTOMATIC DOCUMENT FEEDER COVER UP
66h
01h
AUTOMATIC DOCUMENT FEEDER LIFT UP
66h
02h
DOCUMENT JAM IN AUTOMATIC DOCUMENT FEEDER
66h
03h
DOCUMENT MISS FEED AUTOMATIC IN DOCUMENT FEEDER
67h
00h
A
CONFIGURATION FAILURE
67h
01h
A
CONFIGURATION OF INCAPABLE LOGICAL UNITS FAILED
67h
02h
A
ADD LOGICAL UNIT FAILED
67h
03h
A
MODIFICATION OF LOGICAL UNIT FAILED
67h
04h
A
EXCHANGE OF LOGICAL UNIT FAILED
67h
05h
A
REMOVE OF LOGICAL UNIT FAILED
67h
06h
A
ATTACHMENT OF LOGICAL UNIT FAILED
67h
07h
A
CREATION OF LOGICAL UNIT FAILED
67h
08h
A
ASSIGN FAILURE OCCURRED
67h
09h
A
MULTIPLY ASSIGNED LOGICAL UNIT
67h
0Ah
DT LPWROMAEBKVF
SET TARGET PORT GROUPS COMMAND FAILED
67h
0Bh
DT
B
ATA DEVICE FEATURE NOT ENABLED
68h
00h
A
LOGICAL UNIT NOT CONFIGURED
69h
00h
A
DATA LOSS ON LOGICAL UNIT
69h
01h
A
MULTIPLE LOGICAL UNIT FAILURES
69h
02h
A
PARITY/DATA MISMATCH
6Ah
00h
A
INFORMATIONAL, REFER TO LOG
6Bh
00h
A
STATE CHANGE HAS OCCURRED
Table E.1 — ASC and ASCQ assignments (part 16 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


6Bh
01h
A
REDUNDANCY LEVEL GOT BETTER
6Bh
02h
A
REDUNDANCY LEVEL GOT WORSE
6Ch
00h
A
REBUILD FAILURE OCCURRED
6Dh
00h
A
RECALCULATE FAILURE OCCURRED
6Eh
00h
A
COMMAND TO LOGICAL UNIT FAILED
6Fh
00h
R
COPY PROTECTION KEY EXCHANGE FAILURE - AUTHENTICATION
FAILURE
6Fh
01h
R
COPY PROTECTION KEY EXCHANGE FAILURE - KEY NOT PRESENT
6Fh
02h
R
COPY PROTECTION KEY EXCHANGE FAILURE - KEY NOT
ESTABLISHED
6Fh
03h
R
READ OF SCRAMBLED SECTOR WITHOUT AUTHENTICATION
6Fh
04h
R
MEDIA REGION CODE IS MISMATCHED TO LOGICAL UNIT REGION
6Fh
05h
R
DRIVE REGION MUST BE PERMANENT/REGION RESET COUNT
ERROR
6Fh
06h
R
INSUFFICIENT BLOCK COUNT FOR BINDING NONCE RECORDING
6Fh
07h
R
CONFLICT IN BINDING NONCE RECORDING
70h
NNh
T
DECOMPRESSION EXCEPTION SHORT ALGORITHM ID OF NN
71h
00h
T
DECOMPRESSION EXCEPTION LONG ALGORITHM ID
72h
00h
R
SESSION FIXATION ERROR
72h
01h
R
SESSION FIXATION ERROR WRITING LEAD-IN
72h
02h
R
SESSION FIXATION ERROR WRITING LEAD-OUT
72h
03h
R
SESSION FIXATION ERROR - INCOMPLETE TRACK IN SESSION
72h
04h
R
EMPTY OR PARTIALLY WRITTEN RESERVED TRACK
72h
05h
R
NO MORE TRACK RESERVATIONS ALLOWED
72h
06h
R
RMZ EXTENSION IS NOT ALLOWED
72h
07h
R
NO MORE TEST ZONE EXTENSIONS ARE ALLOWED
73h
00h
R
CD CONTROL ERROR
73h
01h
R
POWER CALIBRATION AREA ALMOST FULL
73h
02h
R
POWER CALIBRATION AREA IS FULL
73h
03h
R
POWER CALIBRATION AREA ERROR
73h
04h
R
PROGRAM MEMORY AREA UPDATE FAILURE
73h
05h
R
PROGRAM MEMORY AREA IS FULL
73h
06h
R
RMA/PMA IS ALMOST FULL
73h
10h
R
CURRENT POWER CALIBRATION AREA ALMOST FULL
73h
11h
R
CURRENT POWER CALIBRATION AREA IS FULL
73h
17h
R
RDZ IS FULL
74h
00h
T
SECURITY ERROR
74h
01h
T
UNABLE TO DECRYPT DATA
74h
02h
T
UNENCRYPTED DATA ENCOUNTERED WHILE DECRYPTING
74h
03h
T
INCORRECT DATA ENCRYPTION KEY
74h
04h
T
CRYPTOGRAPHIC INTEGRITY VALIDATION FAILED
Table E.1 — ASC and ASCQ assignments (part 17 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


74h
05h
T
ERROR DECRYPTING DATA
74h
06h
T
UNKNOWN SIGNATURE VERIFICATION KEY
74h
07h
T
ENCRYPTION PARAMETERS NOT USEABLE
74h
08h
DT
R
M
E
VF
DIGITAL SIGNATURE VALIDATION FAILURE
74h
09h
T
ENCRYPTION MODE MISMATCH ON READ
74h
0Ah
T
ENCRYPTED BLOCK NOT RAW READ ENABLED
74h
0Bh
T
INCORRECT ENCRYPTION PARAMETERS
74h
0Ch
DT
R
MAEBKV
UNABLE TO DECRYPT PARAMETER LIST
74h
0Dh
T
ENCRYPTION ALGORITHM DISABLED
74h
10h
DT
R
MAEBKV
SA CREATION PARAMETER VALUE INVALID
74h
11h
DT
R
MAEBKV
SA CREATION PARAMETER VALUE REJECTED
74h
12h
DT
R
MAEBKV
INVALID SA USAGE
74h
21h
T
DATA ENCRYPTION CONFIGURATION PREVENTED
74h
30h
DT
R
MAEBKV
SA CREATION PARAMETER NOT SUPPORTED
74h
40h
DT
R
MAEBKV
AUTHENTICATION FAILED
74h
61h
V
EXTERNAL DATA ENCRYPTION KEY MANAGER ACCESS ERROR
74h
62h
V
EXTERNAL DATA ENCRYPTION KEY MANAGER ERROR
74h
63h
V
EXTERNAL DATA ENCRYPTION KEY NOT FOUND
74h
64h
V
EXTERNAL DATA ENCRYPTION REQUEST NOT AUTHORIZED
74h
6Eh
T
EXTERNAL DATA ENCRYPTION CONTROL TIMEOUT
74h
6Fh
T
EXTERNAL DATA ENCRYPTION CONTROL ERROR
74h
71h
DT
R
M
E
V
LOGICAL UNIT ACCESS NOT AUTHORIZED
74h
79h
D
SECURITY CONFLICT IN TRANSLATED DEVICE
75h
00h
76h
00h
77h
00h
78h
00h
79h
00h
7Ah
00h
7Bh
00h
7Ch
00h
7Dh
00h
7Eh
00h
Table E.1 — ASC and ASCQ assignments (part 18 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description


7Fh
00h
80h
xxh
\
Through
>
Vendor specific
FFh
xxh
/
xxh
80h
\
Through
>
Vendor specific qualification of standard ASC
xxh
FFh
/
All codes not shown are reserved.
Table E.1 — ASC and ASCQ assignments (part 19 of 19)
.D – Direct Access Block Device (SBC-3)
Device Column key
. T – Sequential Access Device (SSC-4)
blank = code not used
.
L – Printer Device (SSC)
not blank = code used
.
P – Processor Device (SPC-2)
.
. W – Write Once Block Device (SBC)
.
.
R – C/DVD Device (MMC-6)
.
.
O – Optical Memory Block Device (SBC)
.
.
. M – Media Changer Device (SMC-3)
.
.
.
A – Storage Array Device (SCC-2)
.
.
.
E – SCSI Enclosure Services device (SES-3)
.
.
.
. B – Simplified Direct-Access (Reduced Block) device (RBC)
.
.
.
.
K – Optical Card Reader/Writer device (OCRW)
.
.
.
.
V – Automation/Device Interface device (ADC-3)
.
.
.
.
. F – Object-based Storage Device (OSD-2)
.
.
.
.
.
ASC ASCQ
DT LPWROMAEBKVF
Description
