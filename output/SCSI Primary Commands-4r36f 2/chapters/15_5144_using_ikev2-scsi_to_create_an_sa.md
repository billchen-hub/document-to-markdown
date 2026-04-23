# 5.14.4 Using IKEv2-SCSI to create an SA

5.14.3.4 AES-XCBC-PRF-128 IKEv2-based iterative KDF
If the KDF_ID is 8002 0004h, the KDF is a combination of the:
a)
AES-XCBC-PRF-128 secure hash function defined in RFC 4434 (see 2.5) and RFC 3566; and
b)
IKEv2-based iterative KDF technique (see 5.14.3.2).
The technique requires the following inputs from or related to the SA parameters:
a)
AC_SAI;
b)
DS_SAI;
c)
AC_NONCE;
d)
DS_NONCE;
e)
KEY_SEED; and
f)
the number of KEYMAT bits that are to be produced.
The IKEv2-based iterative KDF (see 5.14.3.2) is applied with the following inputs:
a)
IFUNC (see 5.14.3.2) is the AES-XCBC-PRF-128 secure hash function with the translation of inputs
names shown in table 79;
b)
KEY_SEED is the KEY_SEED SA parameter; and
c)
STRING contains the concatenated contents of the following SA parameters:
1)
AC_NONCE;
2)
DS_NONCE;
3)
AC_SAI; and
4)
DS_SAI.
5.14.4 Using IKEv2-SCSI to create an SA
5.14.4.1 Overview
The IKEv2-SCSI protocol is a subset of the IKEv2 protocol (see RFC 4306) that this standard defines for use
in the creation and maintenance of an SA.
An IKEv2-SCSI SA creation transaction shall only be initiated by the application client.
The IKEv2-SCSI protocol creates the following pair of IKE SAs (see RFC 4306):
a)
an SA that protects data transferred from the application client to the device server; and
b)
an SA that protects data transferred from the device server to the application client.
Table 79 — RFC 3566 parameter translations for the KDF based on AES-XCBC-PRF-128
RFC 3566 Parameter
Translation
K (i.e., key)
KEY_SEED SA parameter
M (i.e., message)
STRING as defined in this subclause and used in 5.14.3.2


An IKEv2-SCSI SA creation transaction consists of the following steps:
1)
Device Server Capabilities step (see 5.14.4.5): The application client determines the device
server's cryptographic capabilities;
2)
Key Exchange step (see 5.14.4.6): The application client and device server:
A)
perform a key exchange;
B)
determine SAIs;
C) generate the shared keys used for SA management (e.g., SA creation and deletion) (see
5.14.4.8); and
D) may complete the generation of the SA (see 5.14.4.9);
and
3)
Authentication step (see 5.14.4.7): Unless omitted by application client and device server negotia-
tions in the previous steps, the application client and device server:
A)
authenticate:
a)
each other;
b)
the key exchange; and
c)
the capability selection;
and
B)
complete the generation of the SA (see 5.14.4.9).
The values in the SECURITY PROTOCOL field and the SECURITY PROTOCOL SPECIFIC field in the SECURITY
PROTOCOL IN command (see 6.40) and SECURITY PROTOCOL OUT command (see 6.41) identify the step
of the IKEv2-SCSI protocol (see 7.7.3.2).
The Key Exchange step and the Authentication step depend on the results from the Device Server Capabil-
ities step in order to create an SA. During the Key Exchange step, the application client and device server
perform independent computations to construct the following sets of shared keys:
a)
shared keys that are used by the Authentication step;
b)
shared keys that are used by the Authentication step and to delete the SA; and
c)
shared keys that are used by SCSI usage type specific operations that obtain security from the
generated SA.
More details about these shared keys are provided in 5.14.4.4.
An application client may or may not:
a)
proceed to the Key Exchange step after the Device Server Capabilities step; or
b)
perform a separate Device Server Capabilities step for each IKEv2-SCSI SA creation transaction.
If the device server's capabilities have changed since the Device Server Capabilities step, the Authentication
step returns an error, and the Key Exchange step may return an error.
Changes in the device server’s capabilities do not take effect until at least one application client has been
notified of the new capabilities via the parameter data returned by the Device Server Capabilities step.
After a Device Server Capabilities step, the application client performs SA creation by sending a sequence of
two or four IKEv2-SCSI commands over a single I_T_L nexus to the device server. The following commands
constitute an IKEv2-SCSI CCS:
a)
if the Authentication step is skipped (see 5.14.4.3.4):
1)
a Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2); and
2)
a Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3);
or


b)
if the Authentication step is performed:
1)
a Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2);
2)
a Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3);
3)
an Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2); and
4)
an Authentication step SECURITY PROTOCOL IN command (see 5.14.4.7.3).
The device server shall process each command in the IKEv2-SCSI CCS to completion before returning status.
While a command in the IKEv2-SCSI CCS is being processed by the device server, the application client may
use the REQUEST SENSE command (see 5.14.5) to ascertain the device server’s progress for the command.
If an error is encountered, the device server or application client may abandon the IKEv2-SCSI CCS before
the SA is created (see 5.14.4.10).
The device server shall maintain state for the IKEv2-SCSI CCS on a given I_T_L nexus from the time the Key
Exchange step SECURITY PROTOCOL OUT command is completed with GOOD status until one of the
following occurs:
a)
the IKEv2-SCSI CCS completes successfully;
b)
the IKEv2-SCSI CCS is abandoned as described in 5.14.4.10;
c)
the SA being created by the IKEv2-SCSI CCS is deleted as described in 5.14.4.11;
d)
the number of seconds specified in the IKEV2-SCSI PROTOCOL TIMEOUT field of the IKEv2-SCSI Timeout
Values payload (see 7.7.3.5.15) in the Key Exchange step SECURITY PROTOCOL OUT parameter
data elapses and none of the following commands have been received:
A)
the next command in the IKEv2-SCSI CCS; or
B)
a REQUEST SENSE command;
or
e)
one of the following event related SCSI device conditions (see SAM-5) occurs:
A)
power cycle;
B)
hard reset;
C) logical unit reset; or
D) I_T nexus loss.
If the device server receives a SECURITY PROTOCOL OUT command or SECURITY PROTOCOL IN
command with the SECURITY PROTOCOL field set to IKEv2-SCSI (i.e., 41h) on an I_T_L nexus other than the
one for which IKEv2-SCSI CCS state is being maintained, then:
a)
an additional IKEv2-SCSI CCS may be started; or
b)
the device server may terminate the command with CHECK CONDITION status, with the sense key
set to ABORTED COMMAND, and the additional sense code set to CONFLICTING SA CREATION
REQUEST.
Except for the PERSISTENT RESERVE OUT command (see 5.13.4) and the cases described in this
subclause, a device server that is maintaining a IKEv2-SCSI CCS state on a particular I_T_L nexus shall not
alter its processing of new commands received on that I_T_L nexus.
If all of the following conditions are true:
a)
the device server includes the following algorithm descriptors in the IKEv2-SCSI SA Creation Capabil-
ities payload (see 7.7.3.5.12) in the parameter data returned by the Device Server Capabilities step
SECURITY PROTOCOL IN command (see 5.14.4.5):
A)
an SA_AUTH_OUT algorithm descriptor (see 7.7.3.6.6) with the ALGORITHM IDENTIFIER field set to
SA_AUTH_NONE; and
B)
an SA_AUTH_IN algorithm descriptor (see 7.7.3.6.6) with the ALGORITHM IDENTIFIER field set to
SA_AUTH_NONE;


and
b)
the application client sends the following algorithm descriptors to the device server in the IKEv2-SCSI
SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step SECURITY
PROTOCOL OUT command (see 5.14.4.6.2):
A)
an SA_AUTH_OUT algorithm descriptor with the
ALGORITHM
IDENTIFIER field set to
SA_AUTH_NONE; and
B)
an SA_AUTH_IN algorithm
descriptor
with the
ALGORITHM
IDENTIFIER
field
set to
SA_AUTH_NONE;
then:
a)
the Authentication step is skipped;
b)
the IKEv2-SCSI CCS consists of the two Key Exchange step commands;
c)
the device server requires the IKEv2-SCSI SAUT Cryptographic Algorithms payload (see 7.7.3.5.14)
to be present in the parameter data sent by the Key Exchange step SECURITY PROTOCOL OUT
command;
d)
the device server returns the IKEv2-SCSI SAUT Cryptographic Algorithms payload in the parameter
data returned by the Key Exchange step SECURITY PROTOCOL IN command; and
e)
SA creation occurs upon the completion of the Key Exchange step.
Operation of an IKEv2-SCSI CCS depends on SA_AUTH_NONE being used in both the Authentication step
SECURITY PROTOCOL OUT command and the Authentication step SECUIRTY PROTOCOL IN command,
or SA_AUTH_NONE not being used by either command. Processing requirements placed on the SECURITY
PROTOCOL OUT command during the Key Exchange step (see 7.7.3.6.6) ensure that this dependency is
maintained.
If no other errors are detected and any of the following conditions are true:
a)
the device server does not include an SA_AUTH_OUT algorithm descriptor with the ALGORITHM
IDENTIFIER field set to SA_AUTH_NONE in the IKEv2-SCSI SA Creation Capabilities payload in the
parameter data returned by the Device Server Capabilities step SECURITY PROTOCOL IN
command;
b)
the device server does not include an SA_AUTH_IN algorithm descriptor with the ALGORITHM
IDENTIFIER field set to SA_AUTH_NONE in the IKEv2-SCSI SA Creation Capabilities payload in the
parameter data returned by the Device Server Capabilities step SECURITY PROTOCOL IN
command; or
c)
the application client does not set the ALGORITHM IDENTIFIER field to SA_AUTH_NONE in the
SA_AUTH_OUT algorithm descriptor and the SA_AUTH_IN algorithm descriptor in the IKEv2-SCSI
SA Cryptographic Algorithms payload sent to the device server in the Key Exchange step SECURITY
PROTOCOL OUT command;
then:
a)
the Authentication step is processed;
b)
the IKEv2-SCSI CCS consists of the two Key Exchange step commands and two Authentication step
commands;
c)
the device server requires the IKEv2-SCSI SAUT Cryptographic Algorithms payload to be absent
from the parameter data sent by the Key Exchange step SECURITY PROTOCOL OUT command;
d)
the device server omits the IKEv2-SCSI SAUT Cryptographic Algorithms payload from the parameter
data returned by the Key Exchange step SECURITY PROTOCOL IN command;
e)
the device server requires the IKEv2-SCSI SAUT Cryptographic Algorithms payload to be present in
the parameter data sent by the Authentication step SECURITY PROTOCOL OUT command;
f)
the device server returns the IKEv2-SCSI SAUT Cryptographic Algorithms payload in the parameter
data returned by the Authentication step SECURITY PROTOCOL IN command; and


g)
SA creation occurs upon the completion of the Authentication step.
SA participants should perform the Authentication step unless man-in-the-middle attacks (see 5.14.1.4) are
not of concern or are prevented by a means outside the scope of this standard (e.g., physical security of the
transport).
Omission of the Authentication step provides no defense against a man-in-the-middle adversary that is
capable of modifying SCSI commands. Such an adversary is able to insert itself as an intermediary on the
created SA without knowledge of the SA participants, thereby completely subverting the intended security.
Omission of the Authentication step is only appropriate in environments where the absence of such adver-
saries is assured by other means (e.g., a direct physical connection between the systems on which the appli-
cation client and device server or use of end-to-end security in the SCSI transport protocol such as FC-SP-2).
5.14.4.2 IKEv2-SCSI Protocol summary
This subclause summarizes the IKE-v2-SCSI payloads (see 7.7.3.5) that are exchanged between an appli-
cation client and a device server during all steps of an IKEv2-SCSI SA creation transaction using message
diagrams. Each IKEv2-SCSI step (see 5.14.4.1) is shown in a separate figure. The contents of a payload
(e.g., Key Exchange) may not be the same in both directions of transfer.
Figure 11 shows the Device Server Capabilities step (see 5.14.4.5). The Device Server Capabilities step
consists of a SECURITY PROTOCOL IN command carrying an IKEv2-SCSI SA Creation Capabilities payload
(see 7.7.3.5.12). The IKEv2-SCSI header is not used.
The IKEv2-SCSI SA Creation Capabilities payload indicates the device server's capabilities for SA creation.
Application Client
Device Server
Figure 11 — IKEv2-SCSI Device Server Capabilities step
IKEv2-SCSI SA Creation Capabilities
Key:
payload(s)
Parameter data transferred using a SECURITY
PROTOCOL IN command (see 6.40)
payload
Required payload


Figure 12 shows the Key Exchange step (see 5.14.4.6). The Key Exchange step consists of a SECURITY
PROTOCOL OUT command followed by a SECURITY PROTOCOL IN command.
The IKEv2-SCSI Timeout Values payload (see 7.7.3.5.15) contains timeouts for SA creation and usage.
The IKEv2-SCSI SA Cryptographic Algorithms payloads (see 7.7.3.5.13) are used to select and agree on the
cryptographic algorithms used for creating the SA.
If the Authentication step is skipped (see 5.14.4.1), the IKEv2-SCSI SAUT Cryptographic Algorithms payloads
(see 7.7.3.5.14) are used to select and agree on usage of the SA and the cryptographic algorithms used by
the created SA. If the Authentication step is processed (i.e., not skipped), the SA usage and algorithms
selection is performed during the Authentication step.
The Key Exchange payload (see 7.7.3.5.3) and Nonce payload (see 7.7.3.5.8) are part of the key and nonce
exchanges that are used to generate the IKEv2-SCSI keys and SA keys.
The Certificate Request payload or payloads (see 7.7.3.5.6) enables the device server to request a certificate
from the application client. If the Authentication step is being skipped (see 5.14.4.1), the device server shall
not include any Certificate Request payloads in the parameter data. Use of the Certificate Request payload is
described in 5.14.4.3.3.4.
Application Client
Device Server
Figure 12 — IKEv2-SCSI Key Exchange step
IKEv2-SCSI header — IKEv2-SCSI Timeout Values —
IKEv2-SCSI SA Cryptographic Algorithms — <<IKEv2-SCSI
SAUT Cryptographic Algorithms>> — Key Exchange — Nonce
Key:
payload(s)
Parameter list data transferred using a SECURITY
PROTOCOL OUT command (see 6.41)
payload(s)
Parameter data transferred using a SECURITY
PROTOCOL IN command (see 6.40)
IKEv2-SCSI header — IKEv2-SCSI Cryptographic Algorithms —
<<IKEv2-SCSI SAUT Cryptographic Algorithms>> —
Key Exchange — Nonce — [Certificate Request]
payload
Required payload
[payload]
Optional payload
<<payload>>
Required if Authentication step skipped (see 5.14.4.1),
otherwise absent


Figure 13 shows the Authentication step (see 5.14.4.7). The Authentication step consists of a SECURITY
PROTOCOL OUT command followed by a SECURITY PROTOCOL IN command.
An Encrypted payload (see 7.7.3.5.11) contains all other Authentication step payloads that are protected using
the cryptographic algorithms determined by the IKEv2-SCSI SA Cryptographic Algorithms payloads (see
7.7.3.5.13) in the Key Exchange step (see figure 12).
The Identification payloads (see 7.7.3.5.4) contain the identities to be authenticated. These identities are not
required to be SCSI names or identifiers.
The IKEv2-SCSI SAUT Cryptographic Algorithms payloads (see 7.7.3.5.14) are used to select and agree on
usage of the SA and the cryptographic algorithms used by the created SA.
The Certificate payload or payloads (see 7.7.3.5.5) respond to the Certificate Request payload(s) sent by the
device server in the Key Exchange step SECURITY PROTOCOL IN command.
The Certificate Request payload or payloads (see 7.7.3.5.6) allows an application client to request the delivery
of a Certificate payload (see 7.7.3.5.5) in the parameter data for the Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.3.3.4).
The Notify payload (see 7.7.3.5.9) provides a means for the application client to inform the device server that
this is the only SA being used between them, and that the device server should discard state for any other
SAs created by the same application client.
The Authenticate payloads (see 7.7.3.5.7) authenticate not only the SA participants, but also the entire
protocol sequence (e.g., the Authenticate payloads prevent a man-in-the-middle attack from succeeding).
Application Client
Device Server
Figure 13 — IKEv2-SCSI Authentication step
IKEv2-SCSI header — Encrypted( Identification – Application
Client — IKEv2-SCSI SAUT Cryptographic Algorithms — [Certifi-
cate] — [Certificate Request] — [Notify] — Authentication )
Key:
payload(s)
Parameter list data transferred using a SECURITY
PROTOCOL OUT command (see 6.41)
payload(s)
Parameter data transferred using a SECURITY
PROTOCOL IN command (see 6.40)
IKEv2-SCSI header — Encrypted( Identification – Device Server
— IKEv2-SCSI SAUT Cryptographic Algorithms — [Certificate] —
Authentication )
payload
Required payload
[payload]
Optional payload


Figure 14 shows the Delete operation (see 5.14.4.11). The Delete operation consists of a SECURITY
PROTOCOL OUT command.
An Encrypted payload (see 7.7.3.5.11) contains the Delete payload that is protected using the cryptographic
algorithms determined by the IKEv2-SCSI SA Cryptographic Algorithms payloads (see 7.7.3.5.13) in the Key
Exchange step that was used to create the SA.
The Delete payload (see 7.7.3.5.10) specifies the SA to be deleted.
5.14.4.3 IKEv2-SCSI Authentication
5.14.4.3.1 Overview
IKEv2-SCSI authentication includes these security functions:
a)
the application client and device server each establish an identity by demonstrating knowledge of a
secret authentication key associated with that identity;
b)
the application client demonstrates knowledge of the current device server capability information; and
c)
the application client and device server check the integrity of the current IKEv2-SCSI CCS.
An IKEv2 SCSI authentication algorithm accomplishes these functions by generating and verifying authenti-
cation data based on a concatenation of bytes that includes device server capability information and the
specified portion of the IKEv2-SCSI parameter data (see 7.7.3.5.7) from the IKEv2-SCSI Key Exchange step
(see 5.14.4.6).
An authentication key associated with an identity is used to generate authentication data. IKEv2-SCSI
transfers the authentication data in the AUTHENTICATION DATA field of the IKEv2-SCSI Authentication payload
(see 7.7.3.5.7). The recipient of an IKEv2-SCSI Authentication payload uses a verification key associated with
the identity to verify the authentication data. The identity is:
a)
transferred in the IDENTIFICATION DATA field of the appropriate IKEv2-SCSI Identification payload (see
7.7.3.5.4); or
b)
obtained from a certificate transferred in the IKEv2-SCSI Certificate payload (see 7.7.3.5.5).
IKEv2-SCSI Authentication is bidirectional (i.e., both the application client and the device server authenticate).
IKEv2-SCSI Authentication is skipped when the application client and device server agree to do so during the
Key Exchange step (see 5.14.4.3.4).
Application Client
Device Server
Figure 14 — IKEv2-SCSI Delete operation
IKEv2-SCSI header — Encrypted( Delete )
Key:
payload(s)
Parameter list data transferred using a SECURITY
PROTOCOL OUT command (see 6.41)
payload
Required payload


The following IKEv2-SCSI Authentication methods are defined:
a)
pre-shared key (see 5.14.4.3.2): the authentication key is also used as the verification key; and
b)
digital signature (see 5.14.4.3.3): the verification key and authentication key form a public/private
key pair. The authentication data is a digital signature based on asymmetric cryptography.
Certificates and the IKEv2-SCSI Certificate payload may be used to provide verification keys for digital signa-
tures to application clients and device servers.
5.14.4.3.2 Pre-shared key authentication
Pre-shared key authentication uses a single cryptographic algorithm to both generate and verify authenti-
cation data. A pre-shared key is associated with an identity that is transferred in the IDENTIFICATION DATA field
of the appropriate Identification payload (see 7.7.3.5.4). The pre-shared key serves as both the authentication
key and the verification key for the identity.
NOTE 15 - A pre-shared key that is not kept secret may compromise the security properties of IKEv2-SCSI.
If pre-shared key authentication is used, then the pre-shared key is the key for the cryptographic algorithm.
Authentication data is generated by applying the cryptographic algorithm with this key to the input data (e.g.,
the applicable concatenation of bytes described in 7.7.3.5.7).
Verification of the authentication data shall consist of:
1)
computing the expected contents of the AUTHENTICATION DATA field of the Authentication payload (see
7.7.3.5.7) using the input data and a verification key associated with the identity received in the Identi-
fication payload (see 7.7.3.5.4); and
2)
comparing the expected contents to the actual contents of the AUTHENTICATION DATA field.
Verification is successful if the expected contents match the actual contents, otherwise verification is not
successful.
The pre-shared key requirements in RFC 4306 shall apply to IKEv2-SCSI pre-shared keys, including the
following requirements on interfaces for provisioning pre-shared keys:
a)
ASCII strings of at least 64 bytes shall be supported;
b)
a null terminator shall not be added to any input before it is used as a pre-shared key;
c)
a hexadecimal ASCII encoding of the pre-shared key shall be supported; and
d)
ASCII encodings other than hexadecimal may be supported. Support for any such encoding shall
include specification of the algorithm for translating the encoding to a binary string as part of the
interface.
The following requirements for pre-shared keys apply in addition to those found in RFC 4306:
a)
a pre-shared key shall be associated with one identity;
b)
the same pre-shared key shall not be used to authenticate both an application client and a device
server;
c)
the same pre-shared key should not be used for a group of application clients or a group of device
servers;
d)
the means for provisioning pre-shared keys are outside the scope of this standard; and
e)
information about the size of the pre-shared key shall be stored at the same time that the pre-shared
key is stored.


5.14.4.3.3 Digital signature authentication
5.14.4.3.3.1 Overview
Digital signature authentication uses a matched pair of signature and verification cryptographic algorithms to
generate and verify authentication data that is a digital signature. A public/private key pair is associated with
an identity. The private key is used as the authentication key for the identity. The public key is used as the
verification key for the identity.
NOTE 16 - A private authentication key that is not kept secret may compromise the security properties of
IKEv2-SCSI.
If digital signature authentication is used, then the private key is the key for the signature algorithm. A digital
signature is generated by applying the signature algorithm with this private key to the input data (e.g., the
applicable concatenation of bytes described in 7.7.3.5.7).
Verification of the digital signature shall consist of using the public verification key associated with the identity
and the input data to verify the digital signature received as the contents of the AUTHENTICATION DATA field of
the Authentication payload (see 7.7.3.5.7). Verification is successful if the digital signature is a valid digital
signature over the input data, otherwise verification is not successful.
The means by which an application client or device server obtains a private authentication key are outside the
scope of this standard. An identity and associated public verification key are obtained as follows:
a)
if certificates are used for digital signature authentication, then the identity and the associated public
verification key are obtained from a certificate transferred in the first the IKEv2-SCSI Certificate
payload (see 5.14.4.3.3.4); or
b)
if certificates are not used for digital signature authentication, then the identity is transferred in the
IDENTIFICATION DATA field of the appropriate IKEv2-SCSI Identification payload (see 7.7.3.5.4) and the
public verification key may be:
A)
transferred as a raw RSA key in an IKEv2-SCSI Certificate payload (see 7.7.3.5.5); or
B)
obtained by means that are outside the scope of this standard.
If certificates are not used for digital signature authentication, the association between the identity and the
public key should be verified by means outside the scope of this standard.
5.14.4.3.3.2 Certificates and digital signature authentication
A certificate (see RFC 5280) is a data structure that contains:
a)
an identity;
b)
a public key for that identity;
c)
additional relevant information that may constrain use of the public key;
d)
the identity of a certification authority (see RFC 5280); and
e)
a digital signature generated by that certification authority.
If the identity and associated public key used to verify a digital signature are obtained from a certificate, then
the certification path from the certificate to a trust anchor should be validated (see RFC 5280). If certification
path validation is not successful, verification of the digital signature for that identity shall fail independent of
whether the digital signature is valid.
The means by which an application client or device server obtains a trust anchor are outside the scope of this
standard.


5.14.4.3.3.3 Example of certificate use for digital signature authentication
An example of certificate use involves an application client or device server that trusts a certification authority.
Based on this trust, the public key of that certification authority is used to validate a certificate presented as
part of authentication. Successful validation of that certificate establishes that the public key in that certificate
is associated with the identity in the certificate. That public key is then used to verify the digital signature in the
Authentication payload (see 7.7.3.5.7).
In this example, providing a certificate as part of the IKEv2-SCSI Authentication step (see 5.14.4.7) allows a
single certification authority public key to serve as a trust anchor (see RFC 5280) for verification of digital
signatures for any identity that has been issued a certificate by that certification authority, so that a public key
for each identity does not have to be obtained by other means.
Validating a certificate includes multiple checks beyond verifying the signature, and the validation may
traverse a certification path composed of multiple certificates (see RFC 5280).
5.14.4.3.3.4 Handling of the Certificate Request payload and the Certificate payload
As detailed in this subclause, a Certificate Request payload (see 7.7.3.5.6) in one set of parameter data
requests the delivery of a Certificate payload (see 7.7.3.5.5) in the next set of parameter data transferred. The
purpose of these IKEv2-SCSI protocol elements is as follows:
a)
each SA participant is allowed to require the delivery of a Certificate payload by the other SA partic-
ipant for use in authentication; and
b)
each Certificate Request payload indicates the trust anchors list (see RFC 4306) used by the device
server or application client when PKI-based Authentication is being used with certificates that are not
self signed (see RFC 5280).
The presence of one or more Certificate Request payloads in the Key Exchange step SECURITY
PROTOCOL IN command (see 5.14.4.6.3) parameter data indicates that the device server requires the appli-
cation client to include a Certificate payload in the parameter list for the Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2).
The presence of one or more Certificate Request payloads in the Authentication step SECURITY PROTOCOL
OUT command parameter list specifies that the application client requires the device server to return a Certif-
icate payload in the parameter data for the Authentication step SECURITY PROTOCOL IN command (see
5.14.4.7.3).
If any Certificate payloads are included in the parameter data, the first Certificate payload shall contain the
public key used to verify the Authentication payload. Additional Certificate payloads may be used to assist in
establishing a certification path from the certificate in the first payload to a trust anchor (see RFC 4306 and
RFC 5280).
The application client and device server may use different authentication methods that require or do not
require the use of Certificate payloads. The presence or absence of Certificate Request payloads and Certif-
icate payloads may vary in any of the commands described in this subclause.
5.14.4.3.4 Constraints on skipping the Authentication step
In the Device Server Capabilities step (see 5.14.4.5), the parameter data returned by the SECURITY
PROTOCOL IN command (see 7.7.2.3.2) contains the IKEv2-SCSI SA Creation Algorithms payload (see
7.7.3.5.12) that contains one or more SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptors (see
7.7.3.6.6) and one or more SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptors.


The device server shall allow the Authentication step to be omitted (see 5.14.4.1) if:
a)
the ALGORITHM IDENTIFIER field is set to SA_AUTH_NONE (see 7.7.3.6.6) in one of the
SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptors returned in the Device Server
Capabilities step; and
b)
the ALGORITHM IDENTIFIER field is set to SA_AUTH_NONE in one of the SA_AUTH_IN IKEv2-SCSI
cryptographic algorithm descriptors returned in the Device Server Capabilities step.
The methods for configuring a device server to return SA_AUTH_NONE are outside the scope of this
standard. Device servers shall not be manufactured to return SA_AUTH_NONE as an Authentication payload
authentication algorithm type in the Device Server Capabilities step.
In the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2), the application client
requests that the Authentication step be omitted by setting the ALGORITHM IDENTIFIER field to
SA_AUTH_NONE in:
a)
the SA_AUTH_OUT cryptographic algorithm descriptor in the IKEv2-SCSI SA Cryptographic
Algorithms payload (see 7.7.3.5.13); and
b)
the SA_AUTH_IN cryptographic algorithm descriptor in the IKEv2-SCSI SA Cryptographic Algorithms
payload.
To ensure adequate SA security, the application client should not select the SA_AUTH_NONE value as an
Authentication payload authentication algorithm type unless:
a)
an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and an SA_AUTH_IN
IKEv2-SCSI cryptographic algorithm descriptor from the Device Server Capabilities step indicates
SA_AUTH_NONE availability; and
b)
the application client is configured to omit the Authentication step.
If SA_AUTH_NONE is used, IKEv2-SCSI has no protection against man-in-the-middle attacks. Enabling
return of the SA_AUTH_NONE authentication algorithm type in the Device Capabilities step, and allowing an
application client to select SA_AUTH_NONE in the Key Exchange step are administrative security policy
decisions that absence of authentication is acceptable. Such decisions should only be made in situations
where active attacks on IKEv2-SCSI are not of concern (e.g., direct attachment of a SCSI initiator device and
a SCSI target device, or an end-to-end secure service delivery subsystem such as Fibre Channel secured by
an end-to-end FC-SP-2 SA).


5.14.4.4 Summary of IKEv2-SCSI shared keys nomenclature and shared key sizes
The IKEv2-SCSI shared keys are named as shown in table 80.
Table 80 — IKEv2-SCSI shared key names and SA shared key names
Name
Description
SA parameter that
stores this shared key
Shared keys used only during Authentication step
SK_pi
Shared key used to construct the Authentication payload (see
7.7.3.5.7) for the SECURITY PROTOCOL OUT parameter list in the
Authentication step (see 5.14.4.7.2).
shall not be stored in
any SA parameter
SK_pr
Shared key used to construct the Authentication payload for the
SECURITY PROTOCOL IN parameter data in the Authentication
step.
Shared keys used during IKEv2-SCSI SA creation and management
SK_ai a
Shared key used to integrity check the Encrypted payload in the
SECURITY PROTOCOL OUT parameter list in the:
a)
Authentication step; and
b)
IKEv2-SCSI Delete operation (see 5.14.4.11).
MGMT_DATA
SK_ar a
Shared key used to integrity check the Encrypted payload (see
7.7.3.5.11) in the SECURITY PROTOCOL IN parameter data in the
Authentication step (see 5.14.4.7.3).
SK_ei a
Shared key used to encrypt the Encrypted payload in the
SECURITY PROTOCOL OUT parameter list in the:
a)
Authentication step; and
b)
IKEv2-SCSI Delete operation.
SK_er a
Shared key used to encrypt the Encrypted payload in the
SECURITY PROTOCOL IN parameter data in the Authentication
step.
Shared key used to construct the SA keys
SK_d
Shared key material that is used as input to the KDF that generates
the KEYMAT SA parameter bytes for the SA.
KEY_SEED
a The SA keys SK_ai, SK_ar, SK_ei, and SK_er are stored in the KEYMAT SA parameter. SK_ai is
intended to be used for integrity checking data in a Data-Out Buffer. SK_ar is intended to be used for
integrity checking data in a Data-In Buffer. SK_ei is intended to be used for encrypting data in
a Data-Out Buffer. SK_er is intended to be used for encrypting data in a Data-In Buffer.


The sizes of the shared keys are determined as shown in table 81.
5.14.4.5 Device Server Capabilities step
In the Device Server Capabilities step, the application client sends a SECURITY PROTOCOL IN command
(see 6.40) with the SECURITY PROTOCOL field set to SA creation capabilities (i.e., 40h) and the SECURITY
PROTOCOL SPECIFIC field set to 0101h.
The device server returns the SECURITY PROTOCOL IN parameter data specified by the SECURITY
PROTOCOL SPECIFIC field (see 7.7.2.2) and the parameter data (see 7.7.2.3.2) contains an IKEv2-SCSI SA
Creation Capabilities payload (see 7.7.3.5.12).
Table 81 — Shared key size determination
Name
Shared key size determination
Separate encryption and
integrity checking  a, b
Combined mode encryption and
integrity checking  a, b
SK_ai and
SK_ar c
The shared key size is shown in table 551
for the value in the ALGORITHM IDENTIFIER field
of the INTEG IKEv2-SCSI cryptographic
algorithm descriptor (see 7.7.3.6.4) b.
zero d
SK_er and
SK_ei c
The shared key size is the value in the KEY
LENGTH field of the ENCR IKEv2-SCSI
cryptographic algorithm descriptor (see
7.7.3.6.2) b.
The shared key size is the value in the KEY
LENGTH field of the ENCR IKEv2-SCSI
cryptographic algorithm descriptor plus the
number of salt bytes shown in table 547 (see
7.7.3.6.2) b.
SK_pi and
SK_pr c
The shared key size is equal to the PRF output length (see table 549) associated with the
value in the ALGORITHM IDENTIFIER field of the PRF IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see
7.7.3.5.13).
SK_d
a The use of combined mode encryption and integrity checking is indicated by the AUTH_COMBINED
value in the ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor
(see 7.7.3.6.4).
b For the shared keys used to create an SA, the algorithm descriptor is located in an IKEv2-SCSI SA
Cryptographic Algorithms payload (see 7.7.3.5.13). For the shared keys used after the SA is created
(i.e., the KEYMAT SA parameter), the algorithm descriptor is located in an IKEv2-SCSI SAUT
Cryptographic Algorithms payload (see 7.7.3.5.14).
c To accommodate two shared keys of the specified size, the shared key length shown is doubled for the
purposes of shared key generation.
d In combined mode encryption and integrity checking, the SK_er and SK_ei are used for both encryption
and integrity checking.


In the Device Server Capabilities step, the device server shall return parameter data containing the
IKEv2-SCSI cryptographic algorithm descriptors (see 7.7.3.6) in at least one complete row shown in table 82.
In the Device Server Capabilities step, the device server shall return parameter data containing one
SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field is set to
SA_AUTH_NONE and one SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM
IDENTIFIER field is set to SA_AUTH_NONE if any of the following are true:
a)
the ALGORITHM IDENTIFIER field is set to SA_AUTH_NONE in one of the SA_AUTH_OUT IKEv2-SCSI
cryptographic algorithm descriptors returned in the Device Server Capabilities step; or
b)
the ALGORITHM IDENTIFIER field is set to SA_AUTH_NONE in one of the SA_AUTH_IN IKEv2-SCSI
cryptographic algorithm descriptors returned in the Device Server Capabilities step.
The device server capabilities returned in the SECURITY PROTOCOL IN parameter data may be changed at
any time by means that are outside the scope of this standard, however, such changes shall not take effect
until at least one application client has been notified of the new capabilities in the parameter data returned by
the Device Server Capabilities step SECURITY PROTOCOL IN command. Management applications may
ensure that their device server capabilities changes take effect by sending a Device Server Capabilities step
SECURITY PROTOCOL IN command to the device server after the changes have been made.
If the device server capabilities change (i.e., upon completion of the processing for a Device Server Capabil-
ities step SECURITY PROTOCOL IN command that reported changed information in its parameter data), then
the device server shall establish a unit attention condition for the initiator port associated with every I_T nexus
except the I_T nexus on which the Device Server Capabilities step SECURITY PROTOCOL IN command was
received (see SAM-5), with the additional sense code set to SA CREATION CAPABILITIES DATA HAS
CHANGED.
The Device Server Capabilities step participates in the negotiation to skip the Authentication step as
described in 5.14.4.3.4.
Table 82 — Device Server Capabilities step parameter data requirements
IKEv2-SCSI cryptographic algorithm descriptor
ENCR
(see 7.7.3.6.2)
PRF
(see 7.7.3.6.3)
INTEG
(see 7.7.3.6.4)
D-H
(see 7.7.3.6.5)
SA_AUTH_OUT
(see 7.7.3.6.6)
SA_AUTH_IN
(see 7.7.3.6.6)
The ALGORITHM
IDENTIFIER field
set to
8001 0014h
(i.e., AES-GCM)
and the KEY
LENGTH field
set to 0010h
The ALGORITHM
IDENTIFIER field
set to
8002 0005h
(i.e., IKEv2-use
based on
SHA-256)
The ALGORITHM
IDENTIFIER field
set to
F003 0001h
(i.e., AUTH_
COMBINED)
The ALGORITHM
IDENTIFIER field
set to
8004 000Eh
(i.e., 2 048-bit
MODP group
(finite field
D-H))
The ALGORITHM
IDENTIFIER field
set to
00F9 0001h
(i.e., RSA
Digital
Signature)
The ALGORITHM
IDENTIFIER field
set to
00F9 0001h
(i.e., RSA
Digital
Signature)
The ALGORITHM
IDENTIFIER field
set to
8001 000Ch
(i.e., AES-CBC)
and the KEY
LENGTH field set
to 0020h
The ALGORITHM
IDENTIFIER field
set to
8002 0007h
(i.e., IKEv2-use
based on
SHA-512)
The ALGORITHM
IDENTIFIER field
set to
8003 000Eh
(i.e.,
AUTH_HMAC_
SHA2_
512_256)
The ALGORITHM
IDENTIFIER field
set to
8004 0015h
(i.e., 521-bit
random ECP
group)
The ALGORITHM
IDENTIFIER field
set to
00F9 000Bh
(i.e., ECDSA
with SHA-512
on the
P-521 curve)
The ALGORITHM
IDENTIFIER field
set to
00F9 000Bh
(i.e., ECDSA
with SHA-512
on the
P-521 curve)


NOTE 17 - The Device Server Capabilities step has no IKEv2 exchange equivalent in RFC 4306. This step
replaces most of IKEv2's negotiation by having the application client obtain the supported capabilities from
the device server.
5.14.4.6 IKEv2-SCSI Key Exchange step
5.14.4.6.1 Overview
The Key Exchange step consists of a Diffie-Hellman key exchange with nonces (see RFC 4306) and is
accomplished as follows:
1)
a SECURITY PROTOCOL OUT command (see 5.14.4.6.2);
2)
a SECURITY PROTOCOL IN command (see 5.14.4.6.3); and
3)
key exchange completion (see 5.14.4.6.4)
NOTE 18 - The Key Exchange step corresponds to the IKEv2 IKE_SA_INIT exchange in RFC 4306, except
that determination of device server capabilities has been moved to the Device Server Capabilities step.
5.14.4.6.2 Key Exchange step SECURITY PROTOCOL OUT command
To send its key exchange message to the device server, the application client sends a SECURITY
PROTOCOL OUT command (see 6.41) with the SECURITY PROTOCOL field set to IKEv2-SCSI (i.e., 41h) and
the SECURITY PROTOCOL SPECIFIC field set to 0102h. The parameter list consists of an IKEv2-SCSI header (see
7.7.3.4) and the following:
1)
an IKEv2-SCSI Timeout Values payload (see 7.7.3.5.15);
2)
an IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13);
3)
if the Authentication step is skipped (see 5.14.4.1), an IKEv2-SCSI SAUT Cryptographic Algorithms
payload (see 7.7.3.5.14);
4)
a Key Exchange payload (see 7.7.3.5.3); and
5)
a Nonce payload (see 7.7.3.5.8).
The IKEv2-SCSI Timeout Values payload contains the inactivity timeouts that apply to this IKEv2-SCSI SA
creation transaction and the SA that is created.
The IKEv2-SCSI SA Cryptographic Algorithms payload selects the cryptographic algorithms from among
those returned in the Device Server Capabilities step (see 5.14.4.5) to be used in the creation of the SA.
If the Authentication step is skipped, the IKEv2-SCSI SAUT Cryptographic Algorithms payload contains the
following information about the SA to be created:
a)
the cryptographic algorithms selected by the application client from among those returned in the
Device Server Capabilities step; and
b)
the usage data (see 7.7.3.5.14), if any, that is specific to the SA.
If the application client is unable to select a set of algorithms that are appropriate for the intended creation and
usage of the SA, the application client should not perform the Key Exchange step to request the creation of an
SA.
IKEv2-SCSI SA Cryptographic Algorithms payload error checking requirements that ensure a successful
negotiation of SA creation algorithms are described in 7.7.3.5.13 and 7.7.3.6.
IKEv2-SCSI SAUT Cryptographic Algorithms payload error checking requirements needed to ensure a
successful SA creation are described in 7.7.3.5.14 and 7.7.3.6.


The Key Exchange payload contains the application client's Diffie-Hellman value.
The Nonce payload contains the application client's random nonce.
5.14.4.6.3 Key Exchange step SECURITY PROTOCOL IN command
If the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2) completes with GOOD
status, the application client sends a SECURITY PROTOCOL IN command (see 6.40) with the SECURITY
PROTOCOL field set to IKEv2-SCSI (i.e., 41h) and the SECURITY PROTOCOL SPECIFIC field set to 0102h to obtain
the device server's key exchange message.
The parameter data returned by the device server in response to the SECURITY PROTOCOL IN command
shall contain an IKEv2-SCSI header (see 7.7.3.4) and the following:
1)
an IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13);
2)
if the Authentication step is skipped (see 5.14.4.1), an IKEv2-SCSI SAUT Cryptographic Algorithms
payload (see 7.7.3.5.14);
3)
a Key Exchange payload (see 7.7.3.5.3);
4)
a Nonce payload (see 7.7.3.5.8); and
5)
zero or more Certificate Request payloads (see 7.7.3.5.6).
As part of processing of the Key Exchange step SECURITY PROTOCOL IN command, the device server
shall:
a)
associate the SECURITY PROTOCOL IN command to the last Key Exchange step SECURITY
PROTOCOL OUT command received on the I_T_L nexus. If the device server is maintaining state for
at least one IKEv2-SCSI CCS and the device server is unable to establish this association, then:
A)
the SECURITY PROTOCOL IN command shall be terminated with CHECK CONDITION status,
with the sense key set to NOT READY, and the additional sense code set to LOGICAL UNIT NOT
READY, SA CREATION IN PROGRESS; and
B)
the device server shall continue the IKEv2-SCSI CCS.
If the device is not maintaining state for at least one IKEv2-SCSI CSS, then the SECURITY
PROTOCOL IN command shall be terminated with CHECK CONDITION status, with the sense key
set to ILLEGAL REQUEST, and the additional sense code set to COMMAND SEQUENCE ERROR.
b)
return the device server’s SAI in the IKEv2-SCSI header IKE_SA DEVICE SERVER SAI field;
c)
return the IKEv2-SCSI SA Cryptographic Algorithms payload containing:
A)
the SA creation cryptographic algorithms supplied by the application client in the Key Exchange
step SECURITY PROTOCOL OUT command parameter list; and
B)
the device server's SAI in the SAI field (see 7.7.3.5.13);
d)
if the Authentication step is skipped, return the IKEv2-SCSI SAUT Cryptographic Algorithms payload
containing:
A)
the SA usage cryptographic algorithms supplied by the application client in the Key Exchange
step SECURITY PROTOCOL OUT command parameter list; and
B)
the device server's SAI in the SAI field (see 7.7.3.5.14);
e)
return information about the completed Diffie-Hellman exchange with the Key Exchange payload; and
f)
return the device server’s random nonce in the Nonce payload.
If the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) completes with GOOD
status, the application client should copy the device server’s SAI from the IKE_SA DEVICE SERVER SAI field in
the IKEv2-SCSI header to the state it is maintaining for the IKEv2-SCSI CCS.
Except for the SAI field, the application client should compare the fields in the IKEv2-SCSI SA Cryptographic
Algorithms payload and the IKEv2-SCSI SAUT Cryptographic Algorithms payload, if any, to the values sent in


the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2). If the application client
detects differences in the contents of the payloads other than in the SAI field, the application client should
abandon the IKEv2-SCSI CCS and notify the device server that the IKEv2-SCSI CCS is being abandoned as
described in 5.14.4.10.
5.14.4.6.4 Key Exchange step completion
Before completing the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) with GOOD
status the device server shall complete the Key Exchange step as described in this subclause.
Upon receipt of GOOD status for the Key Exchange step SECURITY PROTOCOL IN command the appli-
cation client should complete the Key Exchange step as described in this subclause.
If the Key Exchange step does not end with the IKEv2-SCSI CCS being abandoned (see 5.14.4.10), then the
contents of the SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and SA_AUTH_IN
IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.6) in the IKEv2-SCSI SA Cryptographic
Algorithms payload specify how the shared key exchanged by the Key Exchange step SECURITY
PROTOCOL OUT command and the Key Exchange step SECURITY PROTOCOL IN command is used to
generate additional shared keys as follows:
a)
if the ALGORITHM IDENTIFIER field in both descriptors contain SA_AUTH_NONE, then the SA partici-
pants generate the SA, including the generation of the shared keys used for SA management (e.g.,
SA creation and management) and the shared keys used by the created SA as defined in 5.14.4.9; or
b)
if the ALGORITHM IDENTIFIER field in both descriptors contain a value other than SA_AUTH_NONE,
then the SA participants generate shared keys (see 5.14.4.8.3) for the following:
A)
seeding the Authentication step generation of the shared keys used by the created SA; and
B)
SA creation and management.
5.14.4.6.5 After the Key Exchange step
Processing of the IKEv2-SCSI CCS subsequent to completion of the Key Exchange step (see 5.14.4.6.4)
depends on the contents of the SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and
SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.6) in the IKEv2-SCSI SA Crypto-
graphic Algorithms payload as follows:
a)
if the ALGORITHM IDENTIFIER field in both descriptors contain SA_AUTH_NONE, then processing of the
IKEv2-SCSI CCS is finished and the generated SA is ready for use; or
b)
if the ALGORITHM IDENTIFIER field in both descriptors contain a value other than SA_AUTH_NONE,
then processing of the IKEv2-SCSI CCS continues as follows:
A)
the Authentication step is performed (see 5.14.4.7); and
B)
the SA participants generate the SA, including the generation of the shared keys used for SA
management and the shared keys used by the created SA as defined in 5.14.4.9.
5.14.4.7 IKEv2-SCSI Authentication step
5.14.4.7.1 Overview
The Authentication step performs the following functions:
a)
authenticates both the application client and the device server;
b)
protects the previous steps of the protocol; and
c)
cryptographically binds the authentication and the previous steps to the created SA.


The Authentication step is accomplished as follows:
1)
a SECURITY PROTOCOL OUT command (see 5.14.4.7.2); and
2)
a SECURITY PROTOCOL IN command (see 5.14.4.7.3).
The parameter data for both commands shall be encrypted and integrity protected using the algorithms and
keys determined in the Key Exchange step (see 5.14.4.6).
NOTE 19 - The Authentication step corresponds to the IKEv2 IKE_AUTH exchange in RFC 4306.
5.14.4.7.2 Authentication step SECURITY PROTOCOL OUT command
To send its authentication message to the device server, the application client sends a SECURITY
PROTOCOL OUT command (see 6.41) with the SECURITY PROTOCOL field set to IKEv2-SCSI (i.e., 41h) and
the SECURITY PROTOCOL SPECIFIC field set to 0103h. The parameter data consists of the IKEv2-SCSI header
(see 7.7.3.4) and an Encrypted payload (see 7.7.3.5.11) that:
a)
is integrity checked and encrypted in one of the following ways:
A)
using separate algorithms as follows:
a)
integrity checked using the following:
A)
the algorithm specified by the INTEG IKEv2-SCSI algorithm descriptor (see 7.7.3.6.4) in
the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) from the Key
Exchange step (see 5.14.4.6); and
B)
the SK_ai shared key (see 5.14.4.4);
and
b)
encrypted using the following:
A)
the algorithm specified by the ENCR IKEv2-SCSI algorithm descriptor (see 7.7.3.6.2) in
the IKEv2-SCSI SA Cryptographic Algorithms payload from the Key Exchange step; and
B)
the SK_ei shared key (see 5.14.4.4);
or
B)
using a combined integrity check and encryption algorithm that uses the following (i.e., if the
INTEG IKEv2-SCSI algorithm descriptor indicates AUTH_COMBINED):
a)
the algorithm specified by the ENCR IKEv2-SCSI algorithm descriptor in the IKEv2-SCSI SA
Cryptographic Algorithms payload; and
b)
the SK_ei shared key with additional salt bytes as described in 5.14.4.8.1 and table 81 (see
5.14.4.4);
and
b)
contains the following:
1)
an Identification – Application Client payload (see 7.7.3.5.4);
2)
an IKEv2-SCSI SAUT Cryptographic Algorithms payload (see 7.7.3.5.14);
3)
zero or more Certificate payloads (see 7.7.3.5.5);
4)
zero or more Certificate Request payloads (see 7.7.3.5.6);
5)
zero or one Notify payload (see 7.7.3.5.9); and
6)
an Authentication payload (see 7.7.3.5.7).
Before performing any checks on data contained in the Encrypted payload, the device server shall validate the
SECURITY PROTOCOL OUT command parameter data as follows:
a)
the device server shall compare the IKE_SA APPLICATION CLIENT SAI field and the IKE_SA DEVICE SERVER
SAI field in the IKEv2-SCSI header to the SAI values it is maintaining for the IKEv2-SCSI CCS, if any,
being maintained for the I_T_L nexus on which the SECURITY PROTOCOL OUT command was
received as described in 7.7.3.4; and
b)
the device server shall decrypt and check the integrity of the Encrypted payload as described in
7.7.3.5.11.4.


Errors detected during the decryption and integrity checking of the Encrypted payload shall be handled as
described in 7.7.3.8.2.
In the SECURITY PROTOCOL OUT command parameter list, the application client:
a)
sends information about the SA usage and cryptographic algorithms;
b)
sends its identity in the Identification – Application Client payload;
c)
sends information proving its knowledge of the secret corresponding to its identity in the Authenti-
cation payload; and
d)
integrity protects the Key Exchange step and the Authentication step using the Authentication
payload.
The application client may include the Notify payload to send an initial contact notification to the device server.
If sent, the initial contact notification specifies that the application client has no stored state for any SAs with
the device server other than the SA that is being created.
In response to receipt of an initial contact notification, the device server should delete all other SAs that were
authenticated with a SECURITY PROTOCOL OUT command that contained the same Identification - Appli-
cation Client payload data as that which is present in the SECURITY PROTOCOL OUT command that the
device server is processing.
If the device server deletes other SAs in response to an initial contact notification, it shall do so only after the
successful completion of the Authentication step SECURITY PROTOCOL OUT command. If an error occurs
during the Authentication SECURITY PROTOCOL OUT command, the device server shall ignore the initial
contact notification.
If the device server is unable to proceed with SA creation for any reason (e.g., the verification of the Authenti-
cation payload fails), the SECURITY PROTOCOL OUT command shall be terminated with CHECK
CONDITION status, with the sense key set to ABORTED COMMAND, and the additional sense code set to an
appropriate value. The additional sense code AUTHENTICATION FAILED shall be used if verification of the
Authentication payload fails, or if authentication fails for any other reason.
5.14.4.7.3 Authentication step SECURITY PROTOCOL IN command
If the Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2) completes with GOOD
status, the application client sends a SECURITY PROTOCOL IN command (see 6.40) with the SECURITY
PROTOCOL field set to IKEv2-SCSI (i.e., 41h) and the SECURITY PROTOCOL SPECIFIC field set to 0103h to obtain
the device server's authentication message. The parameter data consists of the IKEv2-SCSI header (see
7.7.3.4) and an Encrypted payload (see 7.7.3.5.11) that:
a)
is integrity checked and encrypted in one of the following ways:
A)
using separate algorithms as follows:
a)
integrity checked using the following:
A)
the algorithm specified by the INTEG IKEv2-SCSI algorithm descriptor (see 7.7.3.6.4) in
the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) from the Key
Exchange step (see 5.14.4.6); and
B)
the SK_ar shared key (see 5.14.4.4);
and
b)
encrypted using the following:
A)
the algorithm specified by the ENCR IKEv2-SCSI algorithm descriptor (see 7.7.3.6.2) in
the IKEv2-SCSI SA Cryptographic Algorithms payload from the Key Exchange step; and
B)
the SK_er shared key (see 5.14.4.4);
or


B)
using a combined integrity check and encryption algorithm that uses the following (i.e., if the
INTEG IKEv2-SCSI algorithm descriptor indicates AUTH_COMBINED):
a)
the algorithm specified by the ENCR IKEv2-SCSI algorithm descriptor in the IKEv2-SCSI SA
Cryptographic Algorithms payload from the Key Exchange step; and
b)
the SK_er shared key with additional salt bytes as described in 5.14.4.8.1 and table 81 (see
5.14.4.4);
and
b)
contains the following:
1)
an Identification – Device Server payload (see 7.7.3.5.4);
2)
an IKEv2-SCSI SAUT Cryptographic Algorithms payload (see 7.7.3.5.14);
3)
zero or more Certificate payloads (see 5.14.4.3.3.4); and
4)
an Authentication payload (see 7.7.3.5.7).
In the SECURITY PROTOCOL IN parameter data, the device server:
a)
confirms information about the SA usage and cryptographic algorithms;
b)
sends its identity in the Identification – Device Server payload;
c)
authenticates its identity; and
d)
protects the integrity of the prior step messages using the Authentication payload.
Before completing the SECURITY PROTOCOL IN command with GOOD status, the device server shall
generate the SA as described in 5.14.4.9.
The application client should verify the Authentication payload as described in 7.7.3.5.7. The Certificate
payload(s) are used as part of this verification for PKI-based authentication. If the Authentication payload is
verified and no other error occurs the application client should generate the SA as described in 5.14.4.9.
If the application client is unable to proceed with SA creation for any reason (e.g., the verification of the
Authentication payload fails), the application client should:
a)
not use the SA for any additional activities; and
b)
notify the device server that the IKEv2-SCSI CCS is being abandoned as described in 5.14.4.10.
The application client should compare the fields in the IKEv2-SCSI SAUT Cryptographic Algorithms payload
to the values sent in the Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2). If the
application client detects differences in the contents of the payloads, the application client should abandon the
IKEv2-SCSI CCS and notify the device server that the IKEv2-SCSI CCS is being abandoned as described in
5.14.4.10.
5.14.4.8 Generating shared keys
5.14.4.8.1 Overview
If the Authentication step is skipped (see 5.14.4.1), then shared key generation is performed as described in
5.14.4.8.2 and is summarized as follows:
a)
the shared keys for SA management (e.g., SA creation and deletion) are generated at the same time
as the shared keys used by the created SA; and
b)
all the shared keys are generated during completion of the Key Exchange step (see 5.14.4.6.4).


If the Authentication step is processed (i.e., not skipped), then shared key generation is performed as
described in 5.14.4.8.3 and is summarized as follows:
a)
the shared keys for SA management (e.g., SA creation and deletion) are generated during the
completion of the Key Exchange step (see 5.14.4.6.4); and
b)
the shared keys used by the created SA are generated during SA generation (see 5.14.4.9).
Regardless of when the SA management shared keys (e.g., used for SA creation and deletion) and shared
keys (see 5.14.4.4) used by the created SA are generated, the organization of the shared keys depends on
the type of encryption and integrity checking algorithm being used as follows:
a)
if an encryption algorithm that requires separate integrity checking is used, then separate shared keys
are generated for each algorithm; or
b)
if an encryption algorithm that includes integrity checking is used (i.e., if the ALGORITHM IDENTIFIER field
in the INTEG IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.4) contains
AUTH_COMBINED), then no shared keys are generated for the integrity checking algorithm but
additional key material is generated to act as a salt (see table 547 in 7.7.3.6.2) for the combined mode
encryption algorithm.
5.14.4.8.2 Generating shared keys when the Authentication step is skipped
If the Authentication step is skipped (see 5.14.4.1), then the shared keys for SA management are generated
at the same time as the shared keys for use by the created SA.
As part of completing the Key Exchange step (see 5.14.4.6.4), the SA participants generate all necessary
shared keys as follows:
1)
generate SKEYSEED (see RFC 4306) as described in 5.14.4.8.4;
2)
generate the shared keys used for SA management as described in 5.14.4.8.5;
3)
as part of generating the SA (see 5.14.4.9) (i.e., as part of completing the Key Exchange step as
described in 5.14.4.6.4), generate the shared keys for use by the created SA as described in
5.14.4.8.6 and store them in the KEYMAT SA parameter.
5.14.4.8.3 Generating shared keys when the Authentication step is processed
If the Authentication step is not skipped (see 5.14.4.1), then:
1)
the shared keys for SA management are generated during completion of the Key Exchange step (see
5.14.4.6.4) as follows;
1)
generate SKEYSEED (see RFC 4306) as described in 5.14.4.8.4; and
2)
generate the shared keys used for SA management as described in 5.14.4.8.5;
and
2)
the shared keys for use by the created SA are generated during SA generation (see 5.14.4.9), near
the end of processing for the Authentication step (see 5.14.4.7) as described in 5.14.4.8.6 and store
them in the KEYMAT SA parameter.
5.14.4.8.4 Initializing shared key generation
5.14.4.8.4.1 Initializing for SA creation shared key generation
The SA parameters are initialized for the KDF function used to generate SA creation shared keys as follows:
1)
generate the input to the PRF function by performing the last steps of the key exchange algorithm
selected by the ALGORITHM IDENTIFIER field in the D-H IKEv2-SCSI algorithm descriptor (see 7.7.3.6.5)


in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) using at least the contents
of one of the following fields as inputs to those last steps:
A)
the KEY EXCHANGE DATA field in the Key Exchange payload (see 7.7.3.5.3) in the Key Exchange
SECURITY PROTOCOL OUT command (see 5.14.4.6.2) parameter data; and
B)
the KEY EXCHANGE DATA field in the Key Exchange payload in the Key Exchange SECURITY
PROTOCOL IN command (see 5.14.4.6.3) parameter data;
2)
generate SKEYSEED (see RFC 4306) using the output from step 1) and the PRF selected by the
ALGORITHM IDENTIFIER field in the PRF IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.3)
in the IKEv2-SCSI SA Cryptographic Algorithms payload;
3)
store the generated SKEYSEED value in the KEY_SEED SA parameter;
4)
store the contents of the IKE_SA APPLICATION CLIENT SAI field from the IKEv2-SCSI Header (see
7.7.3.4) from the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the
AC_SAI SA parameter;
5)
store the contents of the IKE_SA DEVICE SERVER SAI field from the IKEv2-SCSI Header (see 7.7.3.4)
from the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the DS_SAI
SA parameter;
6)
store the contents of the NONCE DATA field from the Nonce payload (see 7.7.3.5.8) from the parameter
data for the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2) in the
AC_NONCE SA parameter; and
7)
store the contents of the NONCE DATA field from the Nonce payload (see 7.7.3.5.8) from the parameter
data for the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the
DS_NONCE SA parameter.
5.14.4.8.4.2 Initializing for generation of shared keys used by the created SA
The SA parameters are initialized for the KDF function used to generate the shared keys that will be used by
the created SA as follows:
1)
store the SK_d value that was generated along with the other shared keys used in SA creation (see
5.14.4.8.5) in the KEY_SEED SA parameter;
2)
store the contents of the IKE_SA APPLICATION CLIENT SAI field from the IKEv2-SCSI Header (see
7.7.3.4) from the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the
AC_SAI SA parameter;
3)
store the contents of the IKE_SA DEVICE SERVER SAI field from the IKEv2-SCSI Header (see 7.7.3.4)
from the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the DS_SAI
SA parameter;
4)
store the contents of the NONCE DATA field from the Nonce payload (see 7.7.3.5.8) from the parameter
data for the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2) in the
AC_NONCE SA parameter; and
5)
store the contents of the NONCE DATA field from the Nonce payload (see 7.7.3.5.8) from the parameter
data for the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) in the
DS_NONCE SA parameter.
5.14.4.8.5 Generating shared keys used for SA management
The shared keys used for SA management (e.g., SA creation and deletion) are generated using the
SKEYSEED generated during initialization (see 5.14.4.8.4) and the steps described in this subclause.
Which shared keys are generated for SA management depends on:
a)
whether the encryption algorithm includes integrity checking as indicated by the contents of the
ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor (see
7.7.3.6.4) of the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13), and
b)
whether the Authentication step is skipped (see 5.14.4.1).


Using the contents of the initialized SA parameters (see 5.14.4.8.4.1), the INTEG ALGORITHM IDENTIFIER field,
and the KDF selected by the ALGORITHM IDENTIFIER field in the PRF IKEv2-SCSI cryptographic algorithm
descriptor in the IKEv2-SCSI SA Cryptographic Algorithms payload the following shared keys (see 5.14.4.4)
are generated in the order shown:
a)
if the INTEG ALGORITHM IDENTIFIER field is not set to AUTH_COMBINED, then generate the following
shared keys (see 5.14.4.4):
A)
if the Authentication step is not skipped, generate the following shared keys:
1)
SK_d;
2)
SK_ai;
3)
SK_ar;
4)
SK_ei;
5)
SK_er;
6)
SK_pi; and
7)
SK_pr;
or
B)
if the Authentication step is skipped, then generate the following shared keys:
1)
SK_d;
2)
SK_ai;
3)
SK_ar;
4)
SK_ei; and
5)
SK_er;
or
b)
if the INTEG ALGORITHM IDENTIFIER field is set to AUTH_COMBINED, then generate the following
shared keys:
A)
if the Authentication step is not skipped, generate the following shared keys:
1)
SK_d;
2)
SK_ei with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4);
3)
SK_er with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4);
4)
SK_pi; and
5)
SK_pr;
or
B)
if the Authentication step is skipped, then generate the following shared keys:
1)
SK_d;
2)
SK_ei with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4); and
3)
SK_er with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4).
The shared keys thus generated are combined with other data and stored in the MGMT_DATA SA parameter
as described in 5.14.4.9.
How to determine the sizes of the shared keys to be generated is summarized in table 81 (see 5.14.4.4).
5.14.4.8.6 Generating shared keys for use by the created SA
As part of completing the Authentication step and generating the SA (see 5.14.4.9), the SA participants
initialize the SA parameters for performing a KDF (see 5.14.4.8.4.2), and use the KDF selected by the
ALGORITHM IDENTIFIER field in the PRF IKEv2-SCSI cryptographic algorithm descriptor in the Key Exchange
step IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) to generate the following shared keys
(see 5.14.4.4) in the order shown and store them in the KEYMAT SA parameter:
a)
if the ALGORITHM IDENTIFIER field in the ENCR IKEv2-SCSI cryptographic algorithm descriptor (see
7.7.3.6.2) contains ENCR_NULL in the IKEv2-SCSI SAUT Cryptographic Algorithms payload (see
7.7.3.5.14), then generate the following shared keys:
1)
SK_ai;


2)
SK_ar;
and
b)
if the ALGORITHM IDENTIFIER field in the ENCR IKEv2-SCSI cryptographic algorithm descriptor does not
contain ENCR_NULL in the IKEv2-SCSI SAUT Cryptographic Algorithms payload, then generate the
following shared keys:
A)
if the ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor
(see 7.7.3.6.4) does not contain AUTH_COMBINED in the IKEv2-SCSI SAUT Cryptographic
Algorithms payload (see 7.7.3.5.14), then generate the following shared keys:
1)
SK_ai;
2)
SK_ar;
3)
SK_ei; and
4)
SK_er;
or
B)
if the ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor
contains AUTH_COMBINED in the IKEv2-SCSI SAUT Cryptographic Algorithms payload, then
generate the following shared keys:
1)
SK_ei with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4); and
2)
SK_er with additional salt bytes as described in 5.14.4.8.1 and table 81 (see 5.14.4.4).
How to determine the sizes of the shared keys to be generated is summarized in table 81 (see 5.14.4.4).
5.14.4.9 IKEv2-SCSI SA generation
Depending on whether or not the Authentication step was skipped (see 5.14.4.1), the SA participants shall
generate shared keys as described in 5.14.4.8.
The SA participants shall initialize the SA parameters as follows:
1)
KEYMAT shall be set as follows:
A)
if the Authentication step is skipped, KEYMAT shall be set as described in 5.14.4.8.2; or
B)
if the Authentication step is processed, KEYMAT shall be set as described in 5.14.4.8.3;
and
2)
the other SA parameters shall be set as follows:
A)
AC_SAI shall be set to the value in the IKE_SA APPLICATION CLIENT SAI field in the IKEv2-SCSI
header (see 7.7.3.4) in the Key Exchange step SECURITY PROTOCOL OUT command (see
5.14.4.6.2);
B)
DS_SAI shall be set to the value in the IKE_SA DEVICE SERVER SAI field in the IKEv2-SCSI header
in the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3);
C) TIMEOUT shall be set to the IKEV2-SCSI SA INACTIVITY TIMEOUT field in the IKEv2-SCSI Timeout
Values payload (see 7.7.3.5.15) in the Key Exchange step SECURITY PROTOCOL OUT
command;
D) KDF_ID shall be set to the value in the ALGORITHM IDENTIFIER field in the PRF IKEv2-SCSI crypto-
graphic algorithm descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms
payload (see 7.7.3.5.13);
E)
AC_SQN shall be set to one;
F)
DS_SQN shall be set to one;
G) AC_NONCE shall be set to zero;
H) DS_NONCE shall be set to zero;
I)
KEY_SEED shall be set to zero;
J)
USAGE_TYPE shall be set to the value in the SA TYPE field in the IKEv2-SCSI SAUT Crypto-
graphic Algorithms payload (see 7.7.3.5.14) in the Key Exchange step SECURITY PROTOCOL
OUT command;


K)
USAGE_DATA shall contain at least the following values from the IKEv2-SCSI SAUT Crypto-
graphic Algorithms payload (see 7.7.3.5.14) in either the Key Exchange step SECURITY
PROTOCOL OUT command or the Authentication step SECURITY PROTOCOL OUT command:
a)
the ALGORITHM IDENTIFIER field and KEY LENGTH field from the ENCR IKEv2-SCSI crypto-
graphic algorithm descriptor (see 7.7.3.6.2);
b)
the ALGORITHM IDENTIFIER field from the INTEG IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.4); and
c)
the contents, if any, of the USAGE DATA field;
and
L)
MGMT_DATA shall contain at least the following values:
a)
from the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key
Exchange step SECURITY PROTOCOL OUT command:
A)
the ALGORITHM IDENTIFIER field and KEY LENGTH field from the ENCR IKEv2-SCSI crypto-
graphic algorithm descriptor (see 7.7.3.6.2); and
B)
the ALGORITHM IDENTIFIER field from the INTEG IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.4);
b)
from the shared keys generated for SA management (see 5.14.4.8.5), the following shared
keys and salt bytes:
A)
the value of SK_ai, if any;
B)
the value of SK_ar, if any;
C) the value of SK_ei, with additional salt bytes, if any; and
D) the value of SK_er, with additional salt bytes, if any;
and
c)
the next value of the MESSAGE ID field in the IKEv2-SCSI header.
NOTE 20 - The inclusion of the algorithm identifiers and key length in MGMT_DATA SA parameter enables
the SA to apply the same encryption and integrity algorithms that IKEv2-SCSI negotiated to future
IKEv2-SCSI SECURITY PROTOCOL OUT commands and IKEv2-SCSI SECURITY PROTOCOL IN
commands, if any.


5.14.4.10 Abandoning an IKEv2-SCSI CCS
The occurrence of errors in either the application client or the device server may require that an IKEv2-SCSI
CCS be abandoned.
A device server shall indicate that it has abandoned an IKEv2-SCSI CCS, if any, by terminating an
IKEv2-SCSI CCS command (see 5.14.4.1) received on the I_T_L nexus for which the IKEv2-SCSI CCS state
is being maintained with any combination of status and sense data other than those shown in table 83.
As part of abandoning an IKEv2-SCSI CCS, the device server shall:
a)
discard all maintained state (see 5.14.4.1); and
b)
prepare to allow a future Key Exchange step SECURITY PROTOCOL OUT command received on
any I_T_L nexus to start a new IKEv2-SCSI CCS.
After a device server abandons an IKEv2-SCSI CCS, the device server shall respond to all new IKEv2-SCSI
protocol commands as if an IKEv2-SCSI CCS had never been started.
Table 83 — IKEv2-SCSI command terminations that do not abandon the CCS
IKEv2-SCSI CCS command
Status
(Sense Key)
Additional Sense
Code
Description
SECURITY PROTOCOL OUT
SECURITY PROTOCOL IN
GOOD
(n/a)
n/a
Indicates IKEv2-SCSI CCS is
progressing as described in
this standard
Key Exchange step
SECURITY PROTOCOL OUT
(see 5.14.4.6.2)
CHECK
CONDITION
(ABORTED
COMMAND)
CONFLICTING SA
CREATION REQUEST
At least one IKEv2-SCSI CCS
is already active, and attempts
to start another are blocked
until the first CCS completes
SECURITY PROTOCOL OUT
SECURITY PROTOCOL IN
CHECK
CONDITION
(NOT
READY)
LOGICAL UNIT NOT
READY, SA CREATION
IN PROGRESS
Device server is busy process-
ing another command in the
IKEv2-SCSI CCS associated
with this I_T_L nexus or a dif-
ferent IKEv2-SCSI CCS asso-
ciated with a different I_T_L
nexus
SECURITY PROTOCOL IN
CHECK
CONDITION
(ILLEGAL
REQUEST)
INVALID FIELD IN CDB
Incorrect SECURITY
PROTOCOL IN CDB format
Authentication step
SECURITY PROTOCOL OUT
(see 5.14.4.7.2)
UNABLE TO
DECRYPT
PARAMETER LIST
Device server is unable to
decrypt the Encrypted payload
(see 7.7.3.5.11) or the integrity
check fails
SECURITY PROTOCOL OUT
SA CREATION
PARAMETER VALUE
REJECTED
To adapt to possible denial of
service attacks, a condition for
which the optimal response
includes an additional sense
code of SA CREATION
PARAMETER VALUE INVALID
and the abandonment of the
CCS is not causing the CCS
to be abandoned


An application client should not abandon an IKEv2-SCSI CCS when the next command in the CCS is a
SECURITY PROTOCOL IN command. Instead, the application client should send the appropriate SECURITY
PROTOCOL IN command and then abandon the IKEv2-SCSI CCS.
An application client should specify that it has abandoned an IKEv2-SCSI CCS by sending an IKEv2-SCSI
Delete operation (see 5.14.4.11) with application client SAI and device server SAI information that matches
that of the IKEv2-SCSI CCS being abandoned.
5.14.4.11 Deleting an IKEv2-SCSI SA
As part of deleting an SA, both sets of SA parameters (see 5.14.2.2) are deleted as follows:
1)
the application client uses the information in its SA parameters to prepare an IKEv2-SCSI Delete
operation that requests deletion of the device server’s SA parameters;
2)
the application client deletes its SA parameters and any associated data;
3)
the application client sends the IKEv2-SCSI Delete operation prepared in step 1) to the device server;
4)
in response to the IKEv2-SCSI Delete operation, the device server deletes its SA parameters and any
associated data.
The IKEv2-SCSI Delete operation is a SECURITY PROTOCOL OUT command with the SECURITY PROTOCOL
field set to IKEv2-SCSI (i.e., 41h) and the SECURITY PROTOCOL SPECIFIC field set to 0104h. The parameter data
consists of the IKEv2-SCSI header (see 7.7.3.4) and an Encrypted payload (see 7.7.3.5.11) that contains the
one Delete payload (see 7.7.3.5.10).
The Delete payload should conform to the requirements described in 7.7.3.5.10.
The device server shall process a valid Delete operation SECURITY PROTOCOL OUT command regardless
of whether or not IKEv2-SCSI CCS state is being maintained for the I_T_L nexus on which the command is
received.
The application client SAI and device server SAI information in a valid Delete operation may or may not
identify an IKEv2-SCSI CCS for which state is being maintained for the I_T_L nexus on which the command is
received (see 7.7.3.5.11).
5.14.5 Security progress indication
The cryptographic calculations required by some security protocols are capable of consuming significant
amounts of time in the device server. While cryptographic security calculations are in progress, the device
server shall provide pollable REQUEST SENSE data (see 5.11.2) with:
a)
the sense key set to NOT READY;
b)
the additional sense code set to LOGICAL UNIT NOT READY, SA CREATION IN PROGRESS; and
c)
the PROGRESS INDICATION field set to indicate the progress of the device server in performing the
necessary cryptographic calculations.
The device server shall not use the progress indication to report the detailed progress of cryptographic
computations that take a variable amount of time based on their inputs. The device server may use the
progress indication to report synthetic progress that does not reveal the detailed progress of the computation
(e.g., divide a constant expected time for the computation by 10 and advance the progress indication in 10%
increments based on the elapsed time as compared to the expected time).
The requirements in this subclause apply to implementations of Diffie-Hellman computations and operations
involving any keys (e.g., RSA) that optimize operations on large numbers based on the values of inputs (e.g.,
