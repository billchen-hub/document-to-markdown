# 5.14.2 Security associations

There are a wide variety of active attacks (e.g., spoofing, replay, insertion, deletion, known plaintext, and
modification of communications). Man-in-the-middle attacks are a class of active attacks that involve the
attacker inserting itself in the middle of communication, enabling it to intercept all communications without the
knowledge of the communicating parties for various purposes (e.g., insertion, deletion, replay, modification
and/or inspection via decryption of the communications).
5.14.1.5 SCSI security considerations
The application of communication security techniques (see RFC 3552) is defined by command standards.
This subclause describes specific design considerations in applying the threat model (see 5.14.1.3) to all
SCSI device types.
SCSI environments tend not to be fully connected (i.e., there are restrictions on the SCSI device servers with
which a SCSI application client is able to communicate) due to the following mechanisms:
a)
physical and logical connectivity restrictions (e.g., in SCSI to SCSI gateways across different trans-
ports);
b)
LUN mapping and masking; and
c)
transport zoning.
The resulting connectivity is more limited than the Internet security assumption that an off-path attacker is able
to transmit to an arbitrary victim (see RFC 3552).
SCSI security designs are also influenced by SCSI being a client-server distributed service model (see
SAM-5) that is realized over a number of different SCSI transport protocols and interconnects.
Security functionality may be defined as part of a command set or at the SCSI transport level. Some SCSI
transport protocols (e.g., Fibre Channel and iSCSI) define security functionality that provides confidentiality,
cryptographic integrity, and peer entity authentication for all communicated data. However, there are situations
in which some or all of those mechanisms are not used and there are SCSI communications whose scope
spans more than one SCSI transport protocol (e.g., via a gateway between iSCSI and FCP). Security that is
defined by a command set is appropriate for such situations.
5.14.2 Security associations
5.14.2.1 Principles of SAs
Before an application client and device server begin applying security functions (e.g., data integrity checking,
data encryption) to messages (i.e., data that is transferred in either direction between them), they perform a
security protocol to create at least one SA (see 5.14.2.3). The result of the SA creation protocol is two sets of
SA parameters (see 5.14.2.2), one that is maintained by the application client and one that is maintained by
the device server.
In this model, SAs decouple the process of creating a security relationship from its usage in processing
security functions. This decoupling allows either the creation or the usage of an SA to be upgraded in
response to changing security threats without requiring both processes to be upgraded simultaneously.


Figure 10 shows the relationship between application clients and device servers with respect to SAs.
In both the application client and the device server, the SA parameters are modeled as being stored in an
indexed array and the SAI (i.e., the AC_SAI or the DS_SAI in figure 10) identifies one set of SA parameters
within that array. The application client and device server are not required to store the parameters for any
given SA in the same array locations. In order to support this implementation flexibility, a single SA is modeled
as having two different SAI values (i.e., one for the application client and one for the device server).
The device server shall maintain a single SA parameters table for all I_T nexuses.
SAs shall not be preserved across a power cycle, hard reset, or logical unit reset. SAs shall not be affected by
an I_T nexus loss.
Figure 10 — SA relationships
Application Client
SA Parameters
Table
One Set of SA
Parameters
Device Server
SA Parameters
Table
One Set of SA
Parameters
AC_SAI 
DS_SAI 
SA


5.14.2.2 SA parameters
Each SAI shall identify at least the SA parameters defined in table 73. Individual security protocols define how
the SA parameters are generated and/or used by that security protocol.
Table 73 — Minimum SA parameters (part 1 of 3)
Name
Description
Size (bytes) a
Scope b
Min.
Max.
SA parameters that identify and manage the SA.
AC_SAI
The SAI used by the application client to identify the
SA. c
Public
DS_SAI
The SAI used by the device server to identify the SA. c
Public
TIMEOUT
The number of seconds that may elapse after the com-
pletion of an SA access operation (i.e., SA creation or
SA usage by a command) before the device server
should discard the state associated with this SA (e.g.,
the SA parameters). If SA state is discarded because no
SA access operations are received during the specified
interval, then the device server shall respond to further
attempts to access the SA as if the SA had never been
created. This parameter shall not be set to zero.
Public
SA parameters that are incorporated in messages to prevent message replay attacks.
AC_SQN
A sequence number that is incremented for each
response message received by an application client on
which a security function is performed and used to
detect replay attacks (see 5.14.1.4).
Public
DS_SQN
A sequence number that is incremented for each
request message received by a device server on which
a security function is performed and used to detect
replay attacks.
Public
a These size values are guidelines. Specific security protocols may place more exacting size
requirements on SA parameters.
b Public SA parameters may be transferred outside a SCSI device unencrypted. Secret SA parameters
shall not be transferred outside a SCSI device. Fields within a protocol specific SA parameter are
Shared or Secret as defined by the applicable SA creation protocol.
c SAI values between 0 and 255, inclusive, are reserved.
d Nonce SA parameters shall be at least half the size of the KEY_SEED SA parameter.
e The number of bits of entropy in the KEY_SEED SA parameter should be as close to the number of
bits in the KEY_SEED SA parameter as possible (see RFC 3766).


SA parameters that are used by security functions to derive the secret keys that are applied to messages
(e.g., for encryption).
AC_NONCE d
A random nonce value that is generated by the applica-
tion client and used as an input to the key derivation
security algorithm specified by the KDF_ID SA parame-
ter during the derivation of an encryption key.
Public
DS_NONCE d
A random nonce value that is generated by the device
server and used as an input to the key derivation secu-
rity algorithm specified by the KDF_ID SA parameter
during the derivation of an encryption key.
Public
KEY_SEED e
A value that is known only to the application client and
device server that are creating this SA that in combina-
tion with the applicable nonce is used to derive the
KEYMAT SA parameter. The KEY_SEED SA parameter
shall be set to zero as part of completing the SA
creation function.
Secret
KDF_ID
A security algorithm (see 5.14.8) coded value that iden-
tifies the KDF used by the application client and device
server.
Public
SA parameters that are used by security functions to secure messages between the application client and
device server.
KEYMAT
A value that is known only to the application client and
device server that are participating in this SA that may
be subdivided into one or more key values that are used
in security functions that secure messages. The con-
tents of KEYMAT depend on the USAGE_TYPE SA
parameter value.
1 024
Secret
Table 73 — Minimum SA parameters (part 2 of 3)
Name
Description
Size (bytes) a
Scope b
Min.
Max.
a These size values are guidelines. Specific security protocols may place more exacting size
requirements on SA parameters.
b Public SA parameters may be transferred outside a SCSI device unencrypted. Secret SA parameters
shall not be transferred outside a SCSI device. Fields within a protocol specific SA parameter are
Shared or Secret as defined by the applicable SA creation protocol.
c SAI values between 0 and 255, inclusive, are reserved.
d Nonce SA parameters shall be at least half the size of the KEY_SEED SA parameter.
e The number of bits of entropy in the KEY_SEED SA parameter should be as close to the number of
bits in the KEY_SEED SA parameter as possible (see RFC 3766).


The USAGE_TYPE SA parameter (see table 74) provides an indication of how the SA is to be used.
SA parameters that are used by SA management functions.
USAGE_TYPE
A coded value (see table 74) that indicates how the SA
is used.
Public
USAGE_DATA
Information associated with how the SA is used (e.g.,
cryptographic algorithms and key sizes). The contents
of USAGE_DATA depend on the USAGE_TYPE SA
parameter value.
1 024
Public
MGMT_DATA
SA data that is used in ways defined by the SA creation
protocol to perform SA management functions (e.g.,
deletion of the SA).
1 024
Protocol
specific
Table 74 — USAGE_TYPE SA parameter
Code a
Description
USAGE_TYPE SA parameter
Reference
Usage model
Description
0000h to 0080h
Reserved
0081h
Tape data encryption
ESP-SCSI b
None c
SSC-3
0082h to 8000h
Reserved
8001h
CbCS authentication and
credential encryption
ESP-SCSI b
None c
5.14.6.8
8002h to FFFFh
Reserved
a USAGE_TYPE values between 8000h and CFFFh inclusive place additional constraints on how an
SA is to be created as described in 7.7.3.5.14.
b ESP-SCSI usage is defined in 5.14.7.
c The USAGE DATA LENGTH field in the IKEv2-SCSI SAUT Cryptographic Algorithms payload (see
7.7.3.5.14) shall contain zero.
Table 73 — Minimum SA parameters (part 3 of 3)
Name
Description
Size (bytes) a
Scope b
Min.
Max.
a These size values are guidelines. Specific security protocols may place more exacting size
requirements on SA parameters.
b Public SA parameters may be transferred outside a SCSI device unencrypted. Secret SA parameters
shall not be transferred outside a SCSI device. Fields within a protocol specific SA parameter are
Shared or Secret as defined by the applicable SA creation protocol.
c SAI values between 0 and 255, inclusive, are reserved.
d Nonce SA parameters shall be at least half the size of the KEY_SEED SA parameter.
e The number of bits of entropy in the KEY_SEED SA parameter should be as close to the number of
bits in the KEY_SEED SA parameter as possible (see RFC 3766).
