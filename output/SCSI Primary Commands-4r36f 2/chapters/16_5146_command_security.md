# 5.14.6 Command security

a computational step may be skipped if a bit or set of bits in an input is zero). A progress indication that
advances based on the computation structure (e.g., count of computational steps) may reveal the time taken
by content-dependent portions of the computation, and reveal information about the inputs.
5.14.6 Command security
5.14.6.1 Overview
SCSI command security defines techniques for protecting against inadvertent or malicious misuse of SCSI
commands to gain unauthorized access to logical units.
The following classes are used to specify SCSI command security:
a)
Secure CDB Originator class;
b)
Security Manager class;
c)
Enforcement Manager class; and
d)
Secure CDB Processor class.
The relationship between those classes varies depending on the implemented security technique.
5.14.6.2 Secure CDB Originator class
The Secure CDB Originator class is a kind of application client that originates SCSI commands to which it has
attached a security CDB extension (see 4.2.4) that allows an enforcement manager to determine if the SCSI
command may be processed by the addressed logical unit.
The secure CDB originator interacts with the security manager to determine:
a)
the types of the SCSI commands it is allowed to send to the Secure CDB processor; and
b)
the content of the security CDB extension to be attached to the SCSI commands.
5.14.6.3 Secure CDB Processor class
The Secure CDB Processor class is a kind of device server that processes SCSI commands that have an
attached security extension, if an enforcement manager allows that type of SCSI command from the origi-
nating application client to be processed.
The secure CDB processor determines if a SCSI command is allowed to be processed by communicating the
following information to the enforcement manager:
a)
the CDB of the SCSI command to be processed; and
b)
the security CDB extension, if any, attached to the SCSI command to be processed.
The secure CDB processor shall always allow the processing of the following commands when they do not
have an attached security CDB extension:
a)
INQUIRY;
b)
REPORT LUNS;
c)
REPORT SUPPORTED OPERATION CODES;
d)
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS;
e)
REPORT TARGET PORT GROUPS; and
f)
REQUEST SENSE.


5.14.6.4 Enforcement Manager class
The Enforcement Manager class is either contained within a:
a)
device server (i.e., has the same LUN as the secure CDB processor); or
b)
target device (e.g., has a W_LUN, or vendor specific presence in the SCSI target device).
The enforcement manager determines if the secure CDB processor is allowed to, or prohibited from,
processing a SCSI command using security information received from the security manager.
If a secure CDB originator has not been authenticated, the enforcement manager shall not make determina-
tions about whether a command from that secure CDB originator is permitted or prohibited.
5.14.6.5 Security Manager class
The Security Manager class contains communicates with the Secure CDB Originator class (see 5.14.6.2) and
the Enforcement Manager class (see 5.14.6.4) as shown in table 84.
The security manager:
a)
maintains SCSI command security information for the SCSI domain (e.g., authorization and authenti-
cation information);
b)
delivers to the enforcement manager the security information required by the enforcement manager to
determine if the secure CDB processor is allowed to, or prohibited from, processing a SCSI
command; and
c)
responds to requests from authenticated secure CDB originators to send SCSI commands to a
secure CDB processor as follows:
A)
if the secure CDB originator sends its authentication and an authorization request, then the
security manager responds with the authorization information necessary for the secure CDB origi-
Table 84 — Security Manager class relationships
Security Manager location
Communications mechanism for …
Secure CDB
Originator
Enforcement
Manager
An application client located in the same
SCSI device as the secure CDB originator
Outside the scope of
this standard
Via the SCSI domain’s
service delivery sub-
system (see SAM-5)
A device server located in the same SCSI
device as the secure CDB processor
Via the SCSI domain’s
service delivery sub-
system (see SAM-5)
Outside the scope of
this standard
A SCSI device contained within the same
SCSI domain as the secure CDB originator
and the secure CDB processor a
Via the SCSI domain’s
service delivery sub-
system (see SAM-5)
Via the SCSI domain’s
service delivery sub-
system (see SAM-5)
Not a SCSI device, device server, or
application client
Outside the scope of
this standard
Outside the scope of
this standard
a This SCSI device is required to contain an application client and a device server (i.e., to
contain both a SCSI Initiator Port class (see SAM-5) and a SCSI Target Port class (see
SAM-5)).


nator to generate security information to be attached to any authorized CDB that is sent to the
secure CDB processor; or
B)
if the secure CDB originator sends its authentication, an authorization request, and the security
information to be attached to CDBs, then the security manager shall only accept the request if the
secure CDB originator is authorized to send the requested SCSI commands to the requested
secure CDB processor.
5.14.6.6 The relationship between SAs and command security
As defined by this standard, SAs provide the following forms of secure communications for selected portions
of selected CDB and command parameter data:
a)
cryptographic data integrity provided by Message Authentication Code or Integrity Check Value; and
b)
confidentially provided by data encryption.
The SAs defined by this standard do not apply to data communicated in the CDBs sent from the secure CDB
originator to the secure CDB processor. The function of securing CDBs is performed by the command security
features described in 5.14.6. Command security and SAs features may be used in concert to protect both the
CDB data and the parameter data.
Authorization information (see 5.14.6.5) includes associations between:
a)
permissions to use certain commands and command options; and
b)
secure CDB originator identities.
SAs provide a mechanism for satisfying the secure CDB originator authentication requirements placed on
enforcement managers (see 5.14.6.4). Every secure CDB originator that is authenticated using an SA is
required to be authenticated using a unique SA.
Some command security techniques (e.g., the CbCS technique described in 5.14.6.8) depend on an estab-
lished secure channel between a secure CDB originator and secure CDB processor. SAs provide a
mechanism for establishing such secure channels. If SAs are used in this manner, multiple secure CDB origi-
nators may share a common SA, however, such SAs do not authenticate any specific secure CDB originator.
5.14.6.7 Command security techniques
This standard defines the following techniques for implementing command security:
a)
capability-based command security (see 5.14.6.8).
5.14.6.8 Capability-based command security technique
5.14.6.8.1 Overview
CbCS is a credential-based system that manages access to a logical unit by the coordination between shared
keys and security parameters set by the CbCS management application client (see 5.14.6.8.4) and creden-
tials generated by the CbCS management device server (see 5.14.6.8.3). The mechanism for coordination
between the CbCS management device server and the CbCS management application client is not defined in
this standard.
The CbCS protocol enables centralized management of SCSI command security.
CbCS secures access to a logical unit or a volume (see SSC-3) by providing cryptographic integrity of creden-
tials that are added to commands sent to the logical unit. This cryptographic integrity is based on mutual trust


and key exchanges between the CbCS management device server, CbCS management application client,
and the enforcement manager.
Different levels of protection and security are achieved by using different CbCS methods. The following CbCS
methods are defined by this standard:
a)
the BASIC CbCS method (see 5.14.6.8.8.2) provides protection against errors but does not prevent
unauthorized access caused by means of malicious attacks (e.g., identity spoofing and network
attacks); and
b)
the CAPKEY CbCS method (see 5.14.6.8.8.3) enforces application client authentication and provides
cryptographic integrity of credentials. It protects against the following types of unauthorized access
attacks:
A)
Without cryptographic message integrity in the service delivery subsystem:
a)
illegal use of credentials beyond their original scope and life span;
b)
forging or stealing credentials; and
c)
using malformed credentials;
and
B)
with cryptographic message integrity in the service delivery subsystem:
a)
network errors and malicious message modifications; and
b)
message replay attacks.
CbCS also supports rapid revocation of credentials, per SCSI target device and per logical unit.
CbCS does not define task management function security.
CbCS (see figure 15) is composed of the following classes:
a)
Security Manager class (see 5.14.6.8.2) that contains the following classes:
A)
CbCS Management Device Server class (see 5.14.6.8.3); and
B)
CbCS Management Application Client class (see 5.14.6.8.4);
b)
SCSI Initiator Device class (see SAM-5) that contains the following class:
A)
Secure CDB Originator class (see 5.14.6.8.5);
and
c)
SCSI Target Device class (see SAM-5) that contains the following classes:
A)
Secure CDB Processor class (see 5.14.6.8.6); and
B)
Enforcement Manager class (see 5.14.6.8.7).


Figure 15 shows the flow of transactions between the components of a CbCS capable SCSI domain.
Figure 15 — CbCS overview class diagram
0..1
1..*
1..*
Note: See SAM-5
for details on
classes shown in
the shaded area.
Security Manager
1..*
1..*
0..1
Secure CDB Processor
Processes CbCS information()
Secure CDB Originator
Request CbCS capabilities()
Request CbCS capability keys()
requests authorization
delivers capabilities and shared keys
CbCS Management Device Server
Decision database[1]
Authenticate secure CDB originator()
CbCS Management Application Client
Exchange shared keys()
Send security parameters()
Enforcement Manager
Exchange shared keys()
Receive security parameters()
Validate SCSI commands()
exchanges shared keys
0..1
0..1
Application Client
SCSI Initiator Device
Level 1 Hierarchical Logical Unit
SCSI Target Device
SCSI Device
SCSI Domain
Logical Unit
Device Server
1..*
1..*
1..*
requests
command validation
validates SCSI
commands
{Each instance of
a SCSI Target
Device class that
contains a secure
CDB processor
shall contain at least
one enforcement
manager.}


Each instance of CbCS shall contain:
a)
one security manager that shall contain:
A)
one CbCS management device server; and
B)
one CbCS management application;
b)
one or more SCSI initiator devices that shall contain:
A)
one or more secure CDB originators;
and
c)
one or more SCSI target devices that shall contain:
A)
one secure CDB processor per logical unit; and
B)
the following:
a)
one enforcement manager per secure CDB processor;
b)
one enforcement manager per SCSI target device; or
c)
both.
5.14.6.8.2 Security Manager class
The Security Manager class for the CbCS technique manages access of secure CDB originators to logical
units or volumes (see SSC-3). The security manager uses a decision database to obtain the authorization
information required for deciding the type and duration of access granted to secure CDB originator to a given
logical unit or volume (see SSC-3). The security manager communicates with secure CDB originators to
provide them CbCS credentials (see 5.14.6.8.12), and with enforcement managers to exchange shared keys
(see 5.14.6.8.11) and send CbCS parameters (see 5.14.6.8.15).
The security manager may be located and may communicate with secure CDB originators and enforcement
managers as follows:
a)
if the security manager is a SCSI device contained within the same SCSI domain as the secure CDB
originator and the enforcement manager, then the security manager shall contain an application client
and use the application client to communicate to the enforcement manager, and the security manager
shall contain a device server and use the device server to communicate with secure CDB originators;
b)
if the security manager is an application client located in the same device as the secure CDB origi-
nators, the security manager shall communicate to the enforcement manager via the SCSI domain's
service delivery subsystem, and the security manager may communicate with the secure CDB origi-
nators by means outside the scope of this standard; and
c)
if the security manager is a device server located in the same device as the secure CDB processor,
the security manager shall communicate to the secure CDB originators via the SCSI domain's service
delivery subsystem, and the security manager may communicate with the enforcement manager by
means outside the scope of this standard.
The security manager's device server is called the CbCS management device server (see 5.14.6.8.3). The
security manager's application client is called the CbCS management application client (see 5.14.6.8.4).
If the security manager is a SCSI device, the security manager shall perform CbCS management using the
CbCS management device server and the CbCS management application client as follows:
a)
the CbCS management device server (see 5.14.6.8.3) provides access policy controls to secure CDB
originators using policy-coordinated CbCS capabilities; and
b)
the CbCS management application client (see 5.14.6.8.4) prevents unsecured access to a logical unit
or a volume (see SSC-3) in concert with:
A)
the CbCS management device server (see 5.14.6.8.3);
B)
the enforcement manager; and
C) the secure CDB processor.


CbCS management is confined to the CbCS management application client and CbCS management device
server. The communication of CbCS management information may occur in a manner outside the scope of
this standard.
5.14.6.8.3 CbCS Management Device Server class
5.14.6.8.3.1 CbCS Management Device Server class overview
The CbCS Management Device Server class returns a CbCS capability and a CbCS capability key (i.e.,
Capability-Key) with each CbCS credential giving the secure CDB originator access to a specific logical unit,
and optionally to a volume (see SSC-3).
This standard defines the RECEIVE CREDENTIAL command (see 6.27) that the secure CDB originator may
use to request a CbCS capability and a CbCS capability key from a CbCS management device server.
Commands to and responses from the CbCS management device server are protected by use of an SA
whose creation included the Authentication Step (see 6.27).
The CbCS management device server shall set the CBCS bit to zero in any Extended INQUIRY Data VPD
page (see 7.8.7) that it returns.
5.14.6.8.3.2 Decision Database attribute
The Decision Database attribute is used to obtain the authorization information required for deciding the type
and duration of access granted to a secure CDB originator for a given logical unit or volume (see SSC-3)
within a SCSI target device. CbCS Credentials are prepared by the CbCS management device server based
on the contents of that Decision Database attribute.
5.14.6.8.4 CbCS Management Application Client class
The CbCS Management Application Client class exchanges shared keys (see 5.14.6.8.11) with and sends
CbCS parameters (see 5.14.6.8.15) to the enforcement manager using SECURITY PROTOCOL OUT
commands (see 6.41) and SECURITY PROTOCOL IN commands (see 6.40) transferred over the SCSI
domain’s service delivery subsystem.
The CbCS capability keys are computed by the CbCS management device server using shared keys that are
shared between the:
a)
enforcement manager;
b)
CbCS management application client; and
c)
CbCS management device server.
The shared keys are managed by the security manager.
5.14.6.8.5 Secure CDB Originator class
The Secure CDB Originator class requests CbCS capabilities and CbCS capability keys from the CbCS
management device server for a specific logical unit or volume (see SSC-3). The secure CDB originator
sends the CbCS capability and integrity check value to the logical unit's secure CDB processor as part of a
CbCS extended CDB as described in 5.14.6.8.16.
For more information on the Secure CDB Originator class see 5.14.6.2.


5.14.6.8.6 Secure CDB Processor class
The Secure CDB Processor class:
a)
receives a CbCS capability descriptor (see 6.27.2.3) from a secure CDB originator in a CbCS
extension descriptor (see 5.14.6.8.16);
b)
requests the SCSI command be validated by the enforcement manager; and
c)
if the Enforcement Manager validates the SCSI command, then the secure CDB processor processes
that SCSI command.
The secure CDB processor indicates that CbCS is applied to a logical unit by setting the CBCS bit to one in the
Extended INQUIRY Data VPD page (see 7.8.7). If the CBCS bit is set to one, the logical unit shall support the
following:
a)
Extended CDBs (see 4.2.4);
b)
CbCS extension type (see 5.14.6.8.16);
c)
SECURITY PROTOCOL IN commands (see 6.40) specifying the CbCS security protocol (see 7.7.4);
and
d)
SECURITY PROTOCOL OUT commands (see 6.41) specifying the CbCS security protocol (see
7.7.4).
For more information on the Secure CDB Processor class see 5.14.6.3.
5.14.6.8.7 Enforcement Manager class
The Enforcement Manager class:
a)
receives shared keys (see 5.14.6.8.11) and CbCS parameters (see 5.14.6.8.15) from the CbCS
management application client;
b)
authenticates the CbCS capability received from a secure CDB processor with an integrity check
value as described in 5.14.6.8.13.2;
c)
validates SCSI commands sent by secure CDB originators as described in 5.14.6.8.13.2; and
d)
if the CAPKEY CbCS method (see 5.14.6.8.8.3) is supported, supplies one security token (see
5.14.6.8.10) for each active I_T nexus to the secure CDB processor for delivery to the secure CDB
originator that is using that I_T nexus.
The enforcement manager may be contained within the secure CDB processor, or within the SCSI target
device. If the enforcement manager is contained within the secure CDB processor then, the shared keys and
CbCS parameters it uses pertain to that logical unit. If the enforcement manager is contained within the SCSI
target device then, the shared keys and CbCS parameters it uses pertain to the SCSI target device, and the
SECURITY PROTOCOL well-known logical unit (see 8.5) is used for the commands to exchange shared keys
and set CbCS parameters.
If a shared key is stored in a well known logical unit then that key is shared between all logical units within the
SCSI target device but shall only used by a logical unit if there has been no shared key assigned to that logical
unit (i.e., a shared key assigned to a logical unit always overrides any shared key assigned to a well known
logical unit).
For more information on the Enforcement Manager class see 5.14.6.4.


5.14.6.8.8 CbCS methods
5.14.6.8.8.1 Overview
The CbCS methods defined by this standard are summarized in table 85.
If a secure CDB processor receives a command for a logical unit that has CbCS enabled, the enforcement
manager shall validate the command as described in 5.14.6.8.13.2 before any other field in the CDB is
validated, including the operation code.
5.14.6.8.8.2 The BASIC CbCS method
The BASIC CbCS method validates that the CbCS capability authorizes the encapsulated command for each
CDB. It provides centrally-managed policy-driven command access control mechanism that enforces autho-
rized access based on capabilities.
The BASIC CbCS method does not validate the authenticity of the CbCS capability.
Preparing CbCS credentials for the BASIC CbCS method does not require the knowledge of CbCS shared
keys and may be done by the secure CDB originator without coordination with the CbCS management device
server. In the CbCS extension descriptor (see 5.14.6.8.16):
a)
the CbCS capability descriptor (see 6.27.2.3) CBCS METHOD field is set to BASIC;
b)
the following CbCS capability descriptor fields are ignored:
A)
the KEY VERSION field; and
B)
the INTEGRITY CHECK VALUE ALGORITHM field;
and
c)
the INTEGRITY CHECK VALUE field is set to zero.
The BASIC CbCS method controls access between the secure CDB originator and the secure CDB processor
without requiring authentication of the secure CDB originator. It is sufficient for the secure CDB processor to
request that the enforcement manager verify the CbCS capabilities sent by the secure CDB originator.
Table 85 — CbCS methods
CbCS
method
Protection provided by the
enforcement manager and
secure CDB processor
Level of security provided, including I_T
nexus security provided by SCSI transport
(e.g., FC-SP-2)
Without
I_T nexus security
With
I_T nexus security
BASIC
Protection against errors provided by
verifying that the CbCS capability allows
processing, but no validation of the
authenticity of the CbCS capability.
No protection against
attacks
Same protection as is
provided by the SCSI
transport on the I_T
nexus
CAPKEY
Protection against errors and some
attacks by both verifying that the CbCS
capability allows processing, and vali-
dating the authenticity of the CbCS
capability.
CbCS capability
authenticity assured,
but still subject to net-
work attacks (e.g.,
replay attacks)
CbCS capability
authenticity assured
and bound to an I_T
nexus; other network
attacks (e.g., data pri-
vacy) thwarted by SCSI
transport security on
the I_T nexus


5.14.6.8.8.3 The CAPKEY CbCS method
The CAPKEY CbCS method provides centrally-managed policy-driven command access control mechanism
that enforces authorized access based on capabilities.
In addition, the CAPKEY CbCS method assures the integrity and authenticity of the CbCS capability trans-
ferred with each command.
The CAPKEY CbCS method provides for security of commands delivered to the secure CDB processor.
When used in conjunction with a secure service delivery subsystem, it provides additional protection against
network attacks (see 5.14.6.8.8.1).
Each capability (see 5.14.6.8.13) is cryptographically associated with a capability key, and the pair is returned
to a secure CDB originator (see 5.14.6.8.5) in credential (see 5.14.6.8.12) in response to a RECEIVE
CREDENTIAL command (see 6.27).
If the capability is associated with a specific command using a CbCS extension descriptor (see 5.14.6.8.16),
an integrity check value is computed using the capability key and a CbCS security token (see 5.14.6.8.10).
The enforcement manager (see 5.14.6.8.7) validates this integrity check value as described in 5.14.6.8.13.3.
5.14.6.8.9 CbCS trust assumptions
After the logical unit is trusted (i.e., after a secure CDB originator authenticates that it is communicating with a
specific logical unit), the secure CDB originator trusts the secure CDB processor and the enforcement
manager to do the following:
a)
deny any access attempt from any application client that is not authorized by the security manager;
and
b)
deny access from any application client that does not perform the CbCS protocols and functions
defined by this standard.
The CbCS management device server and the CbCS management application client are trusted after:
a)
the CbCS management device server is authenticated by the secure CDB originator; and
b)
the CbCS management application client is authenticated by the CbCS Enforcement Manager.
The CbCS management device server and the CbCS management application client are trusted to do the
following:
a)
securely store long-lived shared keys and capability keys;
b)
grant credentials to secure CDB originators according to access control policies that are outside the
scope of this standard; and
c)
perform the defined security functions.
The service delivery subsystem between the secure CDB originator and the secure CDB processor is not
trusted. However, the CbCS security model for CbCS methods other than BASIC is defined so that commands
generated by the secure CDB originator are processed by the secure CDB processor only after the secure
CDB originator interacts with both the CbCS management device server and the secure CDB processor as
defined in this standard.


The communications trust requirements shown in table 86 provide a basis for the CbCS trust assumptions.
5.14.6.8.10 CbCS security tokens
A CbCS security token is a random nonce that is at least eight bytes in length that is chosen by the
enforcement manager (see 5.14.6.8.7) and returned to a secure CDB originator (see 5.14.6.8.5) by the secure
CDB processor (see 5.14.6.8.6) in response to a SECURITY PROTOCOL IN command (see 6.40) with the
SECURITY PROTOCOL field set to 07h (i.e., CbCS) and the SECURITY PROTOCOL SPECIFIC field set to 3Fh (i.e., the
Security Token CbCS page) as described in 7.7.4.3.4.
The security token shall be unique to each instance of an I_T nexus known to the secure CDB processor and
enforcement manager. Security tokens shall be reset and maintained as described in this subclause.
Each security token shall contain at least as many bytes as the largest cipher block size for all the integrity
checking algorithms supported by the SCSI target device (see 7.7.4.3.3).
If a hard reset, logical unit reset, or I_T nexus loss is detected by the secure CDB processor, the enforcement
manager shall be notified of the event once for each affected I_T nexus. In response to such a notification the
enforcement manager shall discard the security token, if any, associated with the affected I_T nexus.
After a power on, the enforcement manager shall discard all security tokens, if any, that it had been
maintaining before the power on.
In response to a request for a security token for a given I_T nexus from the secure CDB processor, the
enforcement manager shall do one of the following:
a)
return the security token value, if any, that is being maintained for the specified I_T nexus to the
secure CDB processor; or
b)
if no security token is being maintained for the specified I_T nexus, then:
1)
a security token shall be prepared;
2)
the security token shall be returned to the secure CDB processor; and
Table 86 — CbCS communications trust requirement
For connections between
CbCS cryptographic communications
trust requirements
Requirement
level
secure CDB originator and
secure CDB processor
Message integrity b
Optional a
secure CDB originator and
CbCS management application client
Message confidentiality c and integrity b
Mandatory
CbCS management application client and
enforcement manager
Message integrity b
Mandatory
CbCS management application client and
CbCS management device server
Message confidentiality c and integrity b
Mandatory
a If this requirement is not met, then the conditions that table 85 (see 5.14.6.8.8) show for an I_T
nexus without security apply.
b Message integrity algorithms are those that table 104 (see 5.14.8) describes as integrity checking
(i.e., AUTH) algorithms.
c Message confidentiality algorithms are those that table 104 (see 5.14.8) describes as encryption
algorithms.


3)
the security token shall be maintained in association with the specified I_T nexus until one of the
events described in this subclause causes it to be discarded.
5.14.6.8.11 CbCS shared keys
5.14.6.8.11.1 Overview
Cryptographic integrity checking for CbCS capabilities depends on the following hierarchy of shared keys that
is specific to the CbCS model:
1)
a master key that is composed of:
A)
an authentication key; and
B)
a generation key;
and
2)
up to 16 working keys whose values are generated from the generation key component of the master
key.
Each CbCS shared key set shall support:
a)
one master key; and
b)
at least two working keys.
Each CbCS shared key in a set has an associated identifier (see 5.14.6.8.11.2) that describes the CbCS
shared key to the objects that are managing it without revealing the CbCS shared key’s value.
Coordinated sets of CbCS shared keys that conform to this hierarchy are maintained by:
a)
the CbCS management application client (see 5.14.6.8.4);
b)
the CbCS management device server (see 5.14.6.8.3); and
c)
the enforcement manager (see 5.14.6.8.7).
The mechanism for coordinating CbCS shared key sets between the CbCS management application client
and the CbCS management device server is outside the scope of this standard.
The following security protocols are provided by this standard for coordinating CbCS shared key sets between
the CbCS management application client and the enforcement manager:
a)
a Diffie-Hellman key exchange protocol for changing all the components of the master key (see
5.14.6.8.11.4); and
b)
mechanisms that invalidate a working key or set a working key based on the generation key
component of the current master key (see 5.14.6.8.11.5).
These key management protocols associate a key identifier with each shared key (i.e., master key or working
key). The CbCS management application client may use these key identifiers to describe the shared key in
some way (e.g., when the shared key was last refreshed or how the intended use of the shared key). Key
identifiers shall not be used to contain shared key values.
Within any SCSI target device that contains an enforcement manager, sets of CbCS shared keys are
maintained as follows:
a)
a separate set of per-logical unit CbCS shared keys for a logical unit that has CbCS enabled;
b)
one target-wide set of CbCS shared keys that are accessible to all logical units that have CbCS
enabled; or
c)
both a target-wide set of CbCS shared keys and per-logical unit sets of CbCS shared keys.


The enforcement manager in any logical unit that has CbCS enabled shall have access to at least one set of
CbCS shared keys.
If an enforcement manager has access to both a target-wide set of CbCS shared keys and a per-logical unit
set of CbCS shared keys, then a working key defined in the per-logical unit set of CbCS shared keys, if any,
shall be used instead of the equivalent working key from the target-wide set of CbCS shared keys.
All CbCS shared keys should be retired from active use (i.e., set, changed, or discarded) often enough to
thwart key attacks. How often to retire CbCS shared keys from active use is outside the scope of this
standard.
The shared keys in a CbCS shared key set and the CbCS pages used to manage them between the CbCS
management application client and the enforcement manager are summarized in table 87.
5.14.6.8.11.2 CbCS shared key identifiers
CbCS shared key identifiers (see table 88) are set by the CbCS pages (see table 87 in 5.14.6.8.11.1) that
change the values of a CbCS shared key and reported by the Current CbCS Parameters CbCS page (see
7.7.4.3.5).
Table 87 — Summary of CbCS shared keys
CbCS shared key
Applicable CbCS page
Data
direction
Capability
protection
Reference
Master
Authentication,
and
Generation
Current CbCS Parameters a
In
Working key
7.7.4.3.5
Set Master Key – Seed Exchange
Set Master Key – Seed Exchange
Set Master Key – Change Master Key b
Out
In
Out
Authentication
key
7.7.4.5.5
7.7.4.3.6
7.7.4.5.6
Working key
Current CbCS Parameters a
In
Working key
7.7.4.3.5
Invalidate Key
Set Key
Out
Authentication
key
7.7.4.5.3
7.7.4.5.4
a Only key identifiers are returned, not shared key values.
b The new authentication key computed during the seed exchange is the authentication key used for this
CbCS page.
Table 88 — CbCS shared key identifier values
Value
Description
0000 0000 0000 0000h a
The associated CbCS shared key has not been modified since the
SCSI target device was manufactured
0000 0000 0000 0001h to
FFFF FFFF FFFF FFFDh
The associated CbCS shared key has a valid value that has been
set by the applicable CbCS page
FFFF FFFF FFFF FFFEh a
The associated CbCS shared key does not have a valid value
FFFF FFFF FFFF FFFFh a
The associated CbCS shared key is not supported
a The use of this value in the CbCS pages that change CbCS shared key values is reserved.


5.14.6.8.11.3 Specifying which CbCS shared key to change
The logical unit to which a SECURITY PROTOCOL IN command (see 6.40) or a SECURITY PROTOCOL
OUT command (see 6.41) that specifies one of the CbCS pages shown in table 87 (see 5.14.6.8.11.1) is
addressed determines which CbCS shared key is modified as follows:
a)
if the command is addressed to the SECURITY PROTOCOL well known logical unit (see 8.5), then
the CbCS the target-wide (see 5.14.6.8.11.1) set of CbCS shared keys is modified; or
b)
if the command is addressed to a logical unit that is not a well known logical unit, then the per-logical
unit (see 5.14.6.8.11.1) set of CbCS shared keys for the specified logical unit are modified.
5.14.6.8.11.4 Updating a CbCS master key
Both components of the CbCS master key (i.e., the authentication key and the generation key) are changed
using a single Diffie-Hellman exchange CCS as summarized in this subclause. Use of the Diffie-Hellman
exchange ensures forward secrecy of the master key.
The CbCS master key update CCS is composed of the following commands:
1)
a SECURITY PROTOCOL OUT command processing the Set Master Key – Seed Exchange CbCS
page (see 7.7.4.5.5);
2)
a SECURITY PROTOCOL IN command processing the Set Master Key – Seed Exchange CbCS
page (see 7.7.4.3.6); and
3)
a SECURITY PROTOCOL OUT command processing the Set Master Key – Change Master Key
CbCS page (see 7.7.4.5.6).
NOTE 21 - The capability key used to access the two Set Master Key – Seed Exchange CbCS pages is
different from the capability key used to access the Set Master Key – Change Master Key CbCS page (see
5.14.6.8.12.3).
The device server shall maintain CCS state for only one CbCS master key update CCS for all I_T nexuses.
The device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to COMMAND SEQUENCE ERROR, if any of the
following conditions occur:
a)
a command attempts to start a new CbCS master key update CCS while state is being maintained for
another; or
b)
a sequence of CbCS master key update CCS commands other than the one shown in this subclause
is attempted.
The device server shall discard the CbCS master key update CCS state if any of the following occur:
a)
a command in the CCS does not complete with GOOD status; or
b)
the entire CbCS master key update CCS command sequence shown in this subclause is not
completed within ten seconds of the successful completion of processing for the SECURITY
PROTOCOL OUT command for the Set Master Key – Seed Exchange CbCS page.
5.14.6.8.11.5 Changing a CbCS working keys
A working key is invalidated using the Invalidate Key CbCS page (see 7.7.4.5.3) and set to a new value using
the Set Key CbCS page (see 7.7.4.5.4).
New working keys are computed based on the applicable master key and a random number seed.


Working keys are tracked using CbCS shared key identifiers (see 5.14.6.8.11.2).
5.14.6.8.12 CbCS credentials
5.14.6.8.12.1 Overview
Each CbCS credential authorizes access to:
a)
a logical unit; or
b)
a specific volume (see SSC-3) mounted in a specific logical unit.
The applicability of CbCS credentials to the BASIC CbCS method (see 5.14.6.8.8.2) is outside the scope of
this standard.
The format of a CbCS credential is described in 6.27.2.2.
The primary components of a CbCS credential are as follows:
a)
a CbCS capability whose format and preparation are described in 5.14.6.8.13; and
b)
the CbCS capability key that is an integrity check value that is computed as follows:
A)
if the credential is to be sent to a secure CDB originator (see 5.14.6.8.5), the CbCS capability key
is computed based on a working key as described in 5.14.6.8.12.2; or
B)
if the credential is being prepared for use by the CbCS management application client (see
5.14.6.8.4), the CbCS capability key is computed based on a working key or the master key as
described in 5.14.6.8.12.3.
Regardless of how it is computed, the CbCS capability key is used as follows:
a)
by the secure CDB originator to prepare CbCS extension descriptors (see 5.14.6.8.16) sent to the
secure CDB processor (see 5.14.6.8.6);
b)
by the CbCS management application client to prepare CbCS extension descriptors sent to the
enforcement manager (see 5.14.6.8.7); and
c)
by the enforcement manager to validate the integrity of capabilities (see 5.14.6.8.13.3) in CbCS
extension descriptors received by the secure CDB processor.
5.14.6.8.12.2 CbCS capability key computations for the secure CDB originator
For credentials sent to the secure CDB originator (see 5.14.6.8.5), the CbCS capability key (see
5.14.6.8.12.1) is computed without knowledge of the command for which it is being prepared using the
following inputs:
a)
the integrity check value algorithm specified by the INTEGRITY CHECK VALUE ALGORITHM field (see
6.27.2.3) in the CbCS capability descriptor; and
b)
the following inputs to this integrity check value algorithm:
A)
all the bytes in the CbCS capability descriptor (see 6.27.2.3); and
B)
the working key specified by the KEY VERSION field (see 6.27.2.3) in the CbCS capability
descriptor.
5.14.6.8.12.3 CbCS capability key computations for general use
The computation of the CbCS capability key depends on the command for which the CbCS capability key is
being computed as described in this subclause. This computation is more general than the computation
described in 5.14.6.8.12.2, but it produces the same results because the secure CDB originator should not be
allowed to use the commands that produce the exceptional cases described in this subclause.


The CbCS capability key computations described in this subclause are used:
a)
for credentials that are to be used by the CbCS management application client (see 5.14.6.8.4); and
b)
by the enforcement manager (see 5.14.6.8.7) when validating a CbCS capability descriptor (see
5.14.6.8.13).
When the enforcement manager is validating a CbCS capability descriptor, the command is determined by
inspecting the CDB that is being processed.
Based on the command associated with the credential, the CbCS capability key (see 5.14.6.8.12.1) is
computed using the following inputs:
a)
the integrity check value algorithm specified by the INTEGRITY CHECK VALUE ALGORITHM field (see
6.27.2.3) in the CbCS capability descriptor; and
b)
the following inputs to this integrity check value algorithm:
A)
all the bytes in the CbCS capability descriptor (see 6.27.2.3); and
B)
the following CbCS shared key:
a)
if the command is a SECURITY PROTOCOL IN command (see 6.40) or a SECURITY
PROTOCOL OUT command (see 6.41) with the SECURITY PROTOCOL field set to 07h (i.e.,
CbCS) and the SECURITY PROTOCOL SPECIFIC field set to a value that is greater than CFFFh,
then the following shared key is used:
A)
if the command does not access the Set Master Key - Change Key CbCS page (see
7.7.4.5.6), the authentication key component of the master key (see 5.14.6.8.11) is used;
or
B)
if the command accesses the Set Master Key - Change Key CbCS page, then the
authentication key component of the new master key (see 7.7.4.3.6) maintained in the
CbCS master key update CCS (see 5.14.6.8.11.4) is used;
or
b)
if the command is not one of those described in step b) B) a), then the working key specified
by the KEY VERSION field (see 6.27.2.3) in the CbCS capability descriptor.
5.14.6.8.13 CbCS capability descriptors
5.14.6.8.13.1 Overview
CbCS capability descriptors are components of:
a)
CbCS credentials (see 5.14.6.8.12); and
b)
CbCS extension descriptors (see 5.14.6.8.16).
The format of a CbCS capability descriptor is described in 6.27.2.3.
CbCS capability descriptors contain:
a)
information about what commands are allowed if the CbCS capability descriptor is associated with a
specific CDB via a CbCS extension descriptor;
b)
information that identifies a specific logical unit or a specific volume (see SSC-3) mounted in a
specific logical unit to which the CbCS capability is bound;
c)
an optional time limit on the validity of the CbCS capability descriptor;
d)
information that the CbCS management application client (see 5.14.6.8.4) may use to invalidate one
or more CbCS capability descriptors before the time limit expires; and
e)
information that the enforcement manager uses to cryptographically validate the CbCS capability
descriptor, if specified, as described in 5.14.6.8.13.


5.14.6.8.13.2 CbCS extension descriptor validation
The enforcement manager (see 5.14.6.8.7) shall validate the CbCS capability descriptor (see 6.27.2.3)
included in the CbCS extension descriptor (see 5.14.6.8.16). If the validation fails, the enforcement manager
shall interact with the secure CDB processor (see 5.14.6.8.6) in a way that causes the command containing
the CbCS extension descriptor to be terminated with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
The enforcement manager’s validation of a CbCS extension descriptor shall fail if any of the following condi-
tions occur:
1)
a CbCS extension descriptor is not present on a command that table 89 (see 5.14.6.8.14) shows as
requiring a CbCS capability;
2)
the command is one that table 89 (see 5.14.6.8.14) shows as never being allowed if CbCS is enabled;
3)
the CBCS METHOD field is set to a value that is less than the value in the minimum CbCS method CbCS
parameter (see 5.14.6.8.15);
4)
the CBCS METHOD field is set to a value that table 267 defines as reserved (see 6.27.2.3) or a value
that the enforcement manager does not support (see 7.7.4.3.3);
5)
if the CBCS METHOD field is set to CAPKEY and the integrity validation described in 5.14.6.8.13.3 fails;
6)
the DESIGNATION TYPE field is set to a value that table 266 defines as reserved (see 6.27.2.3);
7)
the DESIGNATION TYPE field is set to 1h (i.e., logical unit designation descriptor), and the contents of the
DESIGNATION DESCRIPTOR field in which a logical unit name (see SAM-5) is indicated does not match
the addressed logical unit;
8)
the DESIGNATION TYPE field is set to 2h (MAM attribute descriptor) and either of the following are true:
A)
the ATTRIBUTE IDENTIFIER field in the DESIGNATION DESCRIPTOR field is set to any value other than
0401h (i.e., MEDIUM SERIAL NUMBER); or
B)
the DESIGNATION DESCRIPTOR field contents do not match the MAM attribute of the volume that is
accessible via the addressed logical unit;
9)
the CAPABILITY EXPIRATION TIME field is set to a non-zero value and the value in the CAPABILITY
EXPIRATION TIME field is less than (i.e., prior to) the current time in the clock CbCS parameter (see
5.14.6.8.15);
10) the POLICY ACCESS TAG field is set to a non-zero value that does not match the policy access tag CbCS
parameter (see 5.14.6.8.15); or
11) the command in the CDB field of the extended CDB (see 4.2.4) that contains the CbCS extension
descriptor is not permitted by the PERMISSIONS BIT MASK field (see 5.14.6.8.14).
5.14.6.8.13.3 CAPKEY CbCS method capability integrity validation
If the CbCS method is CAPKEY, the enforcement manager’s validation of a CbCS capability descriptor shall
fail the integrity tests if any of the described in this subclause occur.
Before attempting to cryptographically validate the integrity of the CbCS capability descriptor, the enforcement
manager shall fail the validation if any of the following conditions occur in the CbCS capability descriptor (see
6.27.2.3):
a)
the KEY VERSION field specifies an invalid working key as follows:
A)
the command is not a SECURITY PROTOCOL IN command (see 6.40) or a SECURITY
PROTOCOL OUT command (see 6.41) with the SECURITY PROTOCOL field set to 07h (i.e., CbCS)
and the SECURITY PROTOCOL SPECIFIC field set to a value that is greater than CFFFh (i.e., the KEY
VERSION field is ignored for these commands);
B)
the per-logical unit working key (see 5.14.6.8.11), if any, specified by the KEY VERSION field is
invalid (see 5.14.6.8.11.2); and
C) the target-wide working key (see 5.14.6.8.11), if any, specified by the KEY VERSION field is invalid
(see 5.14.6.8.11.2);


or
b)
the INTEGRITY CHECK VALUE ALGORITHM field is set to a value that is:
A)
not one of those that table 104 (see 5.14.8) lists as being an integrity checking (i.e., AUTH)
algorithm;
B)
is AUTH_COMBINED; or
C) is a value that the enforcement manager does not support (see 7.7.4.3.3).
If no integrity checking configuration errors are found in the CbCS capability descriptor, the enforcement
manager shall:
1)
compute the CbCS capability key for the CbCS capability descriptor as described in 5.14.6.8.12.3;
and
2)
compute the expected contents of CbCS extension descriptor INTEGRITY CHECK VALUE field (see
5.14.6.8.16), using the following inputs:
A)
the integrity check value algorithm specified by the INTEGRITY CHECK VALUE ALGORITHM field (see
6.27.2.3) in the CbCS capability descriptor; and
B)
the following inputs to this integrity check value algorithm:
a)
all the bytes in the security token (see 5.14.6.8.10) for the I_T nexus on which the command
was received as the string for which the integrity check value is to be computed; and
b)
the CbCS capability key computed in step 1) as the cryptographic key.
The enforcement manager shall fail the validation if the contents of CbCS extension descriptor INTEGRITY
CHECK VALUE field do not match the computed expected contents of CbCS extension descriptor INTEGRITY
CHECK VALUE field.
5.14.6.8.14 Association between commands and permission bits
The PERMISSIONS BIT MASK field in the CbCS capability (see 6.27.2.3) specifies which commands are allowed
by the CbCS capability. When processing commands with the CbCS extension, the enforcement manager
shall verify that the bits applicable to the encapsulated SCSI command are all set to one in the PERMISSIONS
BIT MASK field before processing the command. The associations between commands and permission bits are
defined in table 89 and table 90 for commands defined in this standard.
Table 89 — Associations between commands and permissions (part 1 of 3)
Command
PERMISSIONS BIT MASK bits a
DATA
READ
DATA
WRITE
PARM
READ
PARM
WRITE
SEC
MGMT
RESRV
MGMT
ACCESS CONTROL IN
never allow b
ACCESS CONTROL OUT
never allow b
CHANGE ALIASES
always allow c
COPY OPERATION ABORT
never allow b
a The command in the CDB field of the extended CDB (see 4.2.4) that contains the CbCS extension
descriptor shall be allowed only if all of the bits marked with a 1 in the row for that command are set
in the PERMISSIONS BIT MASK field of the CbCS capability in the CbCS extension descriptor. The
permissions bits represented by the empty cells in a row are ignored.
b If the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see 7.8.7), this command shall
never be allowed.
c This command shall always be allowed regardless of whether the CbCS extension descriptor is present
and if the CbCS extension descriptor is present regardless of the value in the PERMISSIONS BIT MASK
field.


EXTENDED COPY(LID4)
never allow b
EXTENDED COPY(LID1)
never allow b
INQUIRY
always allow c
LOG SELECT
LOG SENSE
MANAGEMENT PROTOCOL IN
MANAGEMENT PROTOCOL OUT
MODE SELECT(6)
MODE SELECT(10)
MODE SENSE(6)
MODE SENSE(10)
PERSISTENT RESERVE IN
PERSISTENT RESERVE OUT
READ ATTRIBUTE
READ BUFFER
READ MEDIA SERIAL NUMBER
RECEIVE COPY DATA(LID4)
always allow c
RECEIVE COPY DATA(LID1)
never allow b
RECEIVE COPY OPERATING PARAMETERS
never allow b
RECEIVE COPY FAILURE DETAILS(LID1)
never allow b
RECEIVE COPY STATUS(LID4)
always allow c
RECEIVE COPY STATUS(LID1)
never allow b
RECEIVE ROD TOKEN INFORMATION
always allow c
RECEIVE CREDENTIAL
always allow c
RECEIVE DIAGNOSTIC RESULTS
REMOVE I_T NEXUS
never allow b
REPORT ALIASES
always allow c
Table 89 — Associations between commands and permissions (part 2 of 3)
Command
PERMISSIONS BIT MASK bits a
DATA
READ
DATA
WRITE
PARM
READ
PARM
WRITE
SEC
MGMT
RESRV
MGMT
a The command in the CDB field of the extended CDB (see 4.2.4) that contains the CbCS extension
descriptor shall be allowed only if all of the bits marked with a 1 in the row for that command are set
in the PERMISSIONS BIT MASK field of the CbCS capability in the CbCS extension descriptor. The
permissions bits represented by the empty cells in a row are ignored.
b If the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see 7.8.7), this command shall
never be allowed.
c This command shall always be allowed regardless of whether the CbCS extension descriptor is present
and if the CbCS extension descriptor is present regardless of the value in the PERMISSIONS BIT MASK
field.


The usage of the PERMISSIONS BIT MASK field for the SECURITY PROTOCOL IN command and the
SECURITY PROTOCOL OUT command depend on the following characteristics as shown in table 90:
a)
the contents of the SECURITY PROTOCOL field; and
REPORT ALL ROD TOKENS
always allow c
REPORT IDENTIFYING INFORMATION
REPORT LUNS
always allow c
REPORT PRIORITY
REPORT SUPPORTED OPERATION CODES
always allow c
REPORT SUPPORTED TASK MANAGEMENT
FUNCTIONS
always allow c
REPORT TARGET PORT GROUPS
always allow c
REPORT TIMESTAMP
REQUEST SENSE
SECURITY PROTOCOL IN
see table 90
SECURITY PROTOCOL OUT
see table 90
SEND DIAGNOSTIC
SET IDENTIFYING INFORMATION
SET PRIORITY
SET TARGET PORT GROUPS
SET TIMESTAMP
TEST UNIT READY
always allow c
WRITE ATTRIBUTE
WRITE BUFFER
Table 89 — Associations between commands and permissions (part 3 of 3)
Command
PERMISSIONS BIT MASK bits a
DATA
READ
DATA
WRITE
PARM
READ
PARM
WRITE
SEC
MGMT
RESRV
MGMT
a The command in the CDB field of the extended CDB (see 4.2.4) that contains the CbCS extension
descriptor shall be allowed only if all of the bits marked with a 1 in the row for that command are set
in the PERMISSIONS BIT MASK field of the CbCS capability in the CbCS extension descriptor. The
permissions bits represented by the empty cells in a row are ignored.
b If the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see 7.8.7), this command shall
never be allowed.
c This command shall always be allowed regardless of whether the CbCS extension descriptor is present
and if the CbCS extension descriptor is present regardless of the value in the PERMISSIONS BIT MASK
field.


b)
the contents of the SECURITY PROTOCOL SPECIFIC field.
Command standards may describe the associations between commands and permission bits for the
commands that they define. The processing requirements for those associations are the same as those
described in this standard.
5.14.6.8.15 CbCS parameters
5.14.6.8.15.1 Overview
CbCS parameters:
a)
provide the CbCS Management Application Client class (see 5.14.6.8.4) with a means to control the
operation of the Enforcement Manager class (see 5.14.6.8.7);
b)
allow the Secure CDB Processor class (see 5.14.6.8.6) to receive security tokens and other CbCS
information from the Enforcement Manager class; and
c)
allow any application client to receive basic operational CbCS information from the Enforcement
Manager class.
CbCS parameters that are not changeable indicate which CbCS features and algorithms are supported. An
application client may retrieve the unchangeable CbCS parameters by using the SECURITY PROTOCOL IN
command to return the Unchangeable CbCS Parameters CbCS page (see 7.7.4.3.3).
Table 90 — Associations between security protocol commands and permissions
Command
SECURITY
PROTOCOL
field
SECURITY
PROTOCOL
SPECIFIC
field
Description
SECURITY PROTOCOL IN
00h
any
Always allowed regardless of whether the CbCS
extension descriptor is present and if the CbCS
extension descriptor is present regardless of the
value in the PERMISSIONS BIT MASK field
SECURITY PROTOCOL IN
07h
0000h to
003Fh
SECURITY PROTOCOL IN
07h
0040h to
FFFFh
Allowed only if the CbCS extension descriptor
is present and the SEC MGMT bit is set to one in
the PERMISSIONS BIT MASK field
SECURITY PROTOCOL OUT
any
any


The CbCS parameters with values that change in response to various conditions are summarized in table 91.
The security token CbCS parameter is described in 5.14.6.8.10.
The minimum CbCS method parameter indicates the minimum allowable CbCS method (see 5.14.6.8.8) to be
used in capabilities (see 6.27.2.3) processed by an enforcement manager (see 5.14.6.8.7). The initial
minimum CbCS method CbCS parameter provides an initial value for the minimum CbCS method CbCS
parameter for dynamically created logical units.
The policy access tag parameter indicates the allowable contents of the POLICY ACCESS TAG field in capabilities
(see 6.27.2.3) processed by an enforcement manager (see 5.14.6.8.7). The initial policy access tag CbCS
Table 91 — Summary of changeable CbCS parameters
Parameter
Support
Applicable CbCS page
Data
direction
Capability
protection
Reference
CbCS parameters that are updated automatically based on I_T nexus
Security token
Optional a
Security Token
In
None
7.7.4.3.4
CbCS parameters that provide initial values for dynamically created logical units b
Initial minimum
CbCS method
Optional
Current CbCS Parameters
In
Working key
7.7.4.3.5
Set Minimum CbCS Method c
Out
Working key
7.7.4.5.2
Initial policy
access tag
Optional
Current CbCS Parameters
In
Working key
7.7.4.3.5
Set Policy Access Tag d
Out
Working key
7.7.4.5.1
CbCS parameters that affect the CbCS enforcement manager processing
Minimum CbCS
method
Mandatory
Current CbCS Parameters
In
Working key
7.7.4.3.5
Set Minimum CbCS Method c
Out
Working key
7.7.4.5.2
Policy Access
Tag
Mandatory
Current CbCS Parameters
In
Working key
7.7.4.3.5
Set Policy Access Tag d
Out
Working key
7.7.4.5.1
Clock
Mandatory
Current CbCS Parameters
In
Working key
7.7.4.3.5
CbCS Shared
keys and CbCS
shared key
identifiers
Optional a
see 5.14.6.8.11
a Mandatory if the CAPKEY CbCS method (see 5.14.6.8.8.3) is supported.
b SCSI target devices that do not dynamically create logical units may not implement these CbCS
parameters. Retrieving and setting these CbCS parameters is possible only if the SECURITY
PROTOCOL well known logical unit (see 8.5) is implemented. SCSI target devices that dynamically
create logical units but do not implement the SECURITY PROTOCOL well known logical unit shall
provide a means outside the scope of this standard for managing the values of these CbCS parameters.
c If a Set Minimum CbCS Method CbCS page is processed by the SECURITY PROTOOCL well known
logical unit, then the initial Minimum CbCS Method CbCS parameter is changed. If a Set Minimum
CbCS Method CbCS page is processed by any logical unit other than the SECURITY PROTOOCL well
known logical unit, then the minimum CbCS method CbCS parameter for that logical unit is changed.
d If a Set Policy Access Tag CbCS page is processed by the SECURITY PROTOOCL well known logical
unit, then the initial policy access tag CbCS parameter is changed. If a Set Policy Access Tag CbCS
page is processed by any logical unit other than the SECURITY PROTOOCL well known logical unit,
then the policy access tag CbCS parameter for that logical unit is changed.


parameter provides an initial value for the policy access tag CbCS parameter for dynamically created logical
units.
The clock CbCS parameter indicates the time used by the enforcement manager (see 5.14.6.8.7) when evalu-
ating the contents of the CAPABILITY EXPIRATION TIME field in a capability (see 6.27.2.3). The clock CbCS
parameter is timestamp (see 5.2) and its value is managed using the same mechanisms that are used to
manage a timestamp.
The CbCS shared keys and CbCS shared key identifiers are described in 5.14.6.8.11.
5.14.6.8.16 CbCS extension descriptor format
The CbCS extension descriptor (see table 92) allows the capability-based command security technique (see
5.14.6.8) to used with a SCSI command via the parameters defined in this subclause. Support for the CbCS
extension descriptor is mandatory if the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see
7.8.7). If an extended CDB (see 4.2.4) includes a CbCS extension descriptor the CDB field may contain any
CDB defined in this standard or any command standard.
The EXTENSION TYPE field is defined in 4.2.4.2 and shall be set as shown in table 92 for the CbCS extension
descriptor.
The CbCS capability descriptor is defined in 6.27.2.3.
The contents of INTEGRITY CHECK VALUE field depend on the contents of the CBCS METHOD field in the CbCS
capability descriptor as follows:
a)
if the CBCS METHOD field is not set to CAPKEY or a vendor specific value (see table 267 in 6.27.2.3),
then the INTEGRITY CHECK VALUE field is reserved;
b)
if the CBCS METHOD field is set to a vendor specific value, then the contents of the INTEGRITY CHECK
VALUE field are vendor specific; or
c)
if the CBCS METHOD field is set to CAPKEY, then the INTEGRITY CHECK VALUE field contains an integrity
check value that is computed using the integrity check value algorithm specified by the INTEGRITY
CHECK VALUE ALGORITHM field in the CbCS capability descriptor (see 6.27.2.3) and the following inputs
to the integrity check value algorithm:
A)
all the bytes in the security token (see 5.14.6.8.10) for the I_T nexus on which the command is
being sent as the string for which the integrity check value is to be computed; and
Table 92 — CbCS extension descriptor format
Bit
Byte
EXTENSION TYPE (40h)
Reserved

CbCS capability descriptor (see 6.27.2.3)

•••

(MSB)
INTEGRITY CHECK VALUE

•••
(LSB)
