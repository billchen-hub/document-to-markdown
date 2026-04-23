# 7.7.3 IKEv2-SCSI

7.7.2.3.2 IKEv2-SCSI device server capabilities parameter data format
The IKEv2-SCSI device server capabilities parameter data (see table 519) indicates the IKEv2 transforms
(i.e., key exchange protocols and authentication protocols) supported by the device server for IKEv2-SCSI.
The PARAMETER DATA LENGTH field indicates the number of bytes that follow in the parameter data.
The IKEv2-SCSI SA Creation Capabilities payload (see 7.7.3.5.12) indicates the algorithms supported by
IKEv2-SCSI in the Key Exchange step (see 5.14.4.6) and Authentication step (see 5.14.4.7).
NOTE 62 - The primary content of the IKEv2-SCSI device server capabilities SA creation capabilities
parameter data is an IKEv2-SCSI payload (see 7.7.3.5) because the IKEv2-SCSI SA Creation Capabilities
payload is used by the device server and application client in the construction of other IKEv2-SCSI payloads
(see 5.14.4).
7.7.3 IKEv2-SCSI
7.7.3.1 Overview
If the SECURITY PROTOCOL field in a SECURITY PROTOCOL OUT command (see 6.41) or a SECURITY
PROTOCOL IN command (see 6.40) is set to 41h, then the command is part of an IKEv2-SCSI CCS (see
5.14.4) and is used to transfer IKEv2-SCSI protocol information to or from the device server.
In an IKEv2-SCSI CCS, a defined sequence of SECURITY PROTOCOL OUT and SECURITY PROTOCOL IN
commands are sent by the application client and processed by the device server as summarized in 5.14.4.1.
The IKEv2-SCSI SECURITY PROTOCOL OUT CDB format is described in 7.7.3.3.
The IKEv2-SCSI SECURITY PROTOCOL IN CDB format is described in 7.7.3.2.
The IKEv2-SCSI SECURITY PROTOCOL OUT command and the IKEv2-SCSI SECURITY PROTOCOL IN
command use the same parameter data format, and this format is described in 7.7.3.4. A significant
component of the IKEv2-SCSI parameter data format is one or more IKE payloads, and the format of IKE
payloads is described in 7.7.3.5.
If the IKEv2-SCSI SA creation protocol is supported (see 7.7.1), the SA creation capabilities protocol (see
7.7.2) shall also be supported.
Table 519 — IKEv2-SCSI device server capabilities parameter data
Bit
Byte
(MSB)
PARAMETER DATA LENGTH (n-3)

•••
(LSB)
IKEv2-SCSI SA Creation Capabilities payload
(see 7.7.3.5.12)

•••
n


7.7.3.2 IKEv2-SCSI SECURITY PROTOCOL IN CDB description
The IKEv2-SCSI SECURITY PROTOCOL IN CDB has the format defined in 6.40 with the additional require-
ments described in this subclause.
If the SECURITY PROTOCOL field is set to IKEv2-SCSI (i.e., 41h) in a SECURITY PROTOCOL IN command, the
SECURITY PROTOCOL SPECIFIC field (see table 520) identifies the IKEv2-SCSI step (see 5.14.4.1) that the
device server is to process. If the IKEv2-SCSI SA creation protocol is supported (see 7.7.1), the SECURITY
PROTOCOL IN command support requirements are shown in table 520.
If an IKEv2-SCSI SECURITY PROTOCOL IN command is received with the INC_512 bit is set to one while the
device server is maintaining state for an IKEv2-SCSI CCS on the I_T_L nexus on which the command was
received (see 5.14.4.1), then:
a)
the SECURITY PROTOCOL IN command shall be terminated with CHECK CONDITION status, with
the sense key set to NOT READY, and the additional sense code set to LOGICAL UNIT NOT READY,
SA CREATION IN PROGRESS; and
b)
the device server shall continue the IKEv2-SCSI CCS by preparing to receive another SECURITY
PROTOCOL IN command or SECURITY PROTOCOL OUT command, as appropriate.
If an IKEv2-SCSI SECURITY PROTOCOL IN command is received with the INC_512 bit set to one while the
device server is not maintaining state for an IKEv2-SCSI CCS (see 5.14.4.1), then the SECURITY
PROTOCOL IN command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
Table 520 — SECURITY PROTOCOL SPECIFIC field as defined by the IKEv2-SCSI SECURITY PROTOCOL
IN command
Code
Description
Support
References
Usage
Data format
0000h to 00FFh
Restricted
RFC 4306
RFC 4306
0100h to 0101h
Reserved
0102h
Key Exchange step
Mandatory
5.14.4.6.3
7.7.3.4
0103h
Authentication step
Mandatory
5.14.4.7.3
7.7.3.4
0104h to EFFFh
Reserved
F000h to FFFFh
Vendor Specific


7.7.3.3 IKEv2-SCSI SECURITY PROTOCOL OUT CDB description
The IKEv2-SCSI SECURITY PROTOCOL OUT CDB has the format defined in 6.41 with the additional
requirements described in this subclause.
If the SECURITY PROTOCOL field is set to IKEv2-SCSI (i.e., 41h) in a SECURITY PROTOCOL OUT command,
the SECURITY PROTOCOL SPECIFIC field (see table 521) identifies the IKEv2-SCSI step (see 5.14.4.1) that the
device server is to process. If the IKEv2-SCSI SA creation protocol is supported (see 7.7.1), the SECURITY
PROTOCOL IN command support requirements are shown in table 521.
If an IKEv2-SCSI SECURITY PROTOCOL OUT command is received with the INC_512 bit is set to one while
the device server is maintaining state for an IKEv2-SCSI CCS on the I_T_L nexus on which the command was
received (see 5.14.4.1), then:
a)
the SECURITY PROTOCOL OUT command shall be terminated with CHECK CONDITION status,
with the sense key set to NOT READY, and the additional sense code set to LOGICAL UNIT NOT
READY, SA CREATION IN PROGRESS; and
b)
the device server shall continue the IKEv2-SCSI CCS by preparing to receive another SECURITY
PROTOCOL OUT command or SECURITY PROTOCOL IN command, as appropriate.
If an IKEv2-SCSI SECURITY PROTOCOL OUT command is received with the INC_512 bit is set to one while
the device server is not maintaining state for an IKEv2-SCSI CCS (see 5.14.4.1), then the SECURITY
PROTOCOL OUT command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
Any IKEv2-SCSI SECURITY PROTOCOL OUT command with a transfer length of up to 16 384 bytes shall
not be terminated with an error due to the number of bytes to be transferred and processed.
Table 521 — SECURITY PROTOCOL SPECIFIC field as defined by the IKEv2-SCSI SECURITY PROTOCOL
OUT command
Code
Description
Support
References
Usage
Data format
0000h to 00FFh
Restricted
RFC 4306
RFC 4306
0100h to 0101h
Reserved
0102h
Key Exchange step
Mandatory
5.14.4.6.3
7.7.3.4
0103h
Authentication step
Mandatory
5.14.4.7.3
7.7.3.4
0104h
Delete operation
Mandatory
5.14.4.11
7.7.3.4
0105h to EFFFh
Reserved
F000h to FFFFh
Vendor Specific


7.7.3.4 IKEv2-SCSI parameter data format
Table 522 shows the parameter list format used by a SECURITY PROTOCOL OUT command and the
parameter data format used by a SECURITY PROTOCOL IN command if the SECURITY PROTOCOL field is set
to IKEv2-SCSI (i.e., 41h).
Table 522 — IKEv2-SCSI SECURITY PROTOCOL OUT command and SECURITY PROTOCOL IN
command parameter data
Bit
Byte
IKEv2-SCSI header

Restricted (see RFC 4306)

•••

(MSB)
IKE_SA APPLICATION CLIENT SAI

•••
(LSB)

Restricted (see RFC 4306)

•••

(MSB)
IKE_SA DEVICE SERVER SAI

•••
(LSB)
NEXT PAYLOAD
MAJOR VERSION (2h)
MINOR VERSION
EXCHANGE TYPE
Reserved
INTTR
VERSION
RSPNS
Reserved
(MSB)
MESSAGE ID

•••
(LSB)
(MSB)
IKE LENGTH (n+1)

•••
(LSB)
IKEv2-SCSI payloads
IKEv2-SCSI payload [first] (see 7.7.3.5)
•••
•••
IKEv2-SCSI payload [last] (see 7.7.3.5)
•••
n


The IKE_SA APPLICATION CLIENT SAI field specifies the value that is or is destined to become the AC_SAI SA
parameter (see 5.14.2.2) in the generated SA (see 5.14.4.9). The AC_SAI is chosen by the application client
to uniquely identify its representation of the SA that is being negotiated or managed (e.g., deleted).
If the device server receives an IKEv2-SCSI header with the IKE_SA APPLICATION CLIENT SAI field set to zero,
then the error shall be processed as described in 7.7.3.8.
To increase procedural integrity checking, the application client should compare the IKE_SA APPLICATION
CLIENT SAI field contents in any SECURITY PROTOCOL IN parameter data it receives to the value that the
application client is maintaining for the IKEv2-SCSI CCS or SA management. If the two values are not
identical, the application client should abandon the IKEv2-SCSI CCS, if any, and notify the device server that
the IKEv2-SCSI CCS, if any, is being abandoned as described in 5.14.4.10.
Except in the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2), the IKE_SA DEVICE
SERVER SAI field specifies the value that is or is destined to become the DS_SAI SA parameter in the
generated SA. The DS_SAI is chosen by the device server in accordance with the requirements in 5.14.2.1 to
uniquely identify its representation of the SA that is being negotiated. In the Key Exchange step SECURITY
PROTOCOL OUT command the IKE_SA DEVICE SERVER SAI field is reserved.
To increase procedural integrity checking, the application client should compare the IKE_SA DEVICE SERVER SAI
field contents in the Authentication step SECURITY PROTOCOL IN parameter data it receives to the value
that the application client is maintaining for the IKEv2-SCSI CCS. If the two values are not identical, the appli-
cation client should abandon the IKEv2-SCSI CCS and notify the device server that the IKEv2-SCSI CCS is
being abandoned as described in 5.14.4.10.


The device server shall validate the contents of the IKE_SA APPLICATION CLIENT SAI field and the IKE_SA DEVICE
SERVER SAI field as shown in table 523.
Table 523 — IKEv2-SCSI header checking of SAIs
Contents of SECURITY
PROTOCOL SPECIFIC field
in SECURITY
PROTOCOL OUT CDB
Expected contents for …
Device server action if expected field
contents not received
IKE_SA
APPLICATION
CLIENT
SAI field
IKE_SA
DEVICE
SERVER
SAI field
0102h
(i.e., Key Exchange step)
any value
reserved
No actions taken based on expected field con-
tents
0103h
(i.e., Authentication step)
A match with the SAI
values maintained for an
IKEv2-SCSI CCS on the
I_T_L nexus on which the
command was received
The device server shall:
a)
terminate the SECURITY PROTOCOL
OUT command with CHECK CONDITION
status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code
set to SA CREATION PARAMETER
VALUE REJECTED; and
b)
continue the IKEv2-SCSI CCS by
preparing to receive another Authenti-
cation step SECURITY PROTOCOL
OUT command
0104h
(i.e., Delete operation)
If at least one IKEv2-SCSI
CCS is being maintained
for the I_T_L nexus on
which the command was
received, then:
a)
a match with the SAI
values maintained
for an IKEv2-SCSI
CCS; or
b)
a match with the SAI
values maintained
for any active SA
The device server shall:
a)
terminate the SECURITY PROTOCOL
OUT command with CHECK CONDITION
status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code
set to SA CREATION PARAMETER
VALUE REJECTED; and
b)
continue the IKEv2-SCSI CCS by
preparing to receive another Authenti-
cation step SECURITY PROTOCOL
OUT command
If no IKEv2-SCSI CCS is
being maintained for the
I_T_L nexus on which the
command was received,
then a match with the SAI
values maintained for any
active SA
The SECURITY PROTOCOL OUT command
shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST


The NEXT PAYLOAD field (see table 524) identifies the first IKEv2-SCSI payload that follows the IKEv2-SCSI
header.
The MAJOR VERSION field shall contain the value 2h. If a device server receives an IKEv2-SCSI header with a
MAJOR VERSION field containing a value other than 2h, then the error shall be processed as described in
7.7.3.8.
The MINOR VERSION field is reserved.
Table 524 — NEXT PAYLOAD field
Code
IKE Payload Name
Support requirements in
SECURITY PROTOCOL …
Reference
IN
OUT
00h
No Next Payload
Mandatory
7.7.3.5.2
01h to 20h
Reserved
21h
Security Association
Prohibited a
RFC 4306
22h
Key Exchange
Mandatory
7.7.3.5.3
23h
Identification – Application Client
Prohibited
Mandatory
7.7.3.5.4
24h
Identification – Device Server
Mandatory
Prohibited
7.7.3.5.4
25h
Certificate
Optional
7.7.3.5.5
26h
Certificate Request
Optional
7.7.3.5.6
27h
Authentication
Mandatory
7.7.3.5.7
28h
Nonce
Mandatory
7.7.3.5.8
29h
Notify
Prohibited
Mandatory
7.7.3.5.9
2Ah
Delete
Prohibited
Mandatory
7.7.3.5.10
2Bh
Vendor ID
Prohibited
RFC 4306
2Ch
Traffic Selector – Application Client
Prohibited
RFC 4306
2Dh
Traffic Selector – Device Server
Prohibited
RFC 4306
2Eh
Encrypted
Mandatory
7.7.3.5.11
2Fh
Configuration
Prohibited
RFC 4306
30h
Extensible Authentication
Prohibited
RFC 4306
31h to 7Fh
Restricted
RFC 4306
80h
IKEv2-SCSI SA Creation Capabilities
Mandatory
7.7.3.5.12
81h
IKEv2-SCSI SA Cryptographic Algorithms
Mandatory
7.7.3.5.13
82h
IKEv2-SCSI SAUT Cryptographic Algorithms
Mandatory
7.7.3.5.14
83h
IKEv2-SCSI Timeout Values
Mandatory
7.7.3.5.15
84h to BFh
Reserved
C0h to FFh
Vendor Specific
a The Security Association payload type value is not used in IKEv2-SCSI. The IKEv2-SCSI SA
Cryptographic Algorithms payload (i.e., 81h) and IKEv2-SCSI SAUT Cryptographic Algorithms payload
(i.e., 82h) are used instead.


The EXCHANGE TYPE field is reserved.
The initiator (INTTR) bit shall be set to:
a)
one for SECURITY PROTOCOL OUT commands; and
b)
zero for SECURITY PROTOCOL IN commands.
If a device server receives an IKEv2-SCSI header with the INTTR bit set to zero, then the error shall be
processed as described in 7.7.3.8.
If an application client receives an IKEv2-SCSI header with the INTTR bit set to one, it should abandon the
IKEv2-SCSI CCS and notify the device server that the IKEv2-SCSI CCS is being abandoned as described in
5.14.4.10.
The VERSION bit is reserved.
The response (RSPNS) bit shall be set to:
a)
zero for SECURITY PROTOCOL OUT commands; and
b)
one for SECURITY PROTOCOL IN commands.
If a device server receives an IKEv2-SCSI header with the RSPNS bit set to one, then the error shall be
processed as described in 7.7.3.8.
If an application client receives an IKEv2-SCSI header with the RSPNS bit set to zero, it should abandon the
IKEv2-SCSI CCS and notify the device server that the IKEv2-SCSI CCS is being abandoned as described in
5.14.4.10.
The MESSAGE ID field (see table 525) identifies the function of the parameter data.
If the device server receives a SECURITY PROTOCOL OUT command with an invalid MESSAGE ID field in its
IKEv2-SCSI header, then the error shall be processed as described in 7.7.3.8.
If the application client receives an invalid MESSAGE ID field in the parameter data for a SECURITY
PROTOCOL IN command, the application client should abandon the IKEv2-SCSI CCS and notify the device
server that the IKEv2-SCSI CCS is being abandoned as described in 5.14.4.10.
The IKE LENGTH field specifies the total number of bytes in the parameter data, including the IKEv2-SCSI
header and all the IKEv2-SCSI payloads.
NOTE 63 - The contents of the IKE LENGTH field differ from those found in most SCSI length fields, however,
they are consistent with the IKEv2 usage (see RFC 4306).
Table 525 — MESSAGE ID field
Code
Description
0000 0000h
Key Exchange step SECURITY PROTOCOL OUT command (see
5.14.4.6.2) or SECURITY PROTOCOL IN command (see 5.14.4.6.3)
0000 0001h
Authentication step SECURITY PROTOCOL OUT command (see
5.14.4.7.2) or SECURITY PROTOCOL IN command (see 5.14.4.7.3)
0000 0002h
Delete operation in a SECURITY PROTOCOL OUT command
0000 0003h to 0000 FFFFh
Reserved


Each IKEv2-SCSI payload (see 7.7.3.5) contains specific data related to the operation being performed. A
specific combination of IKEv2-SCSI payloads is specified for each operation (e.g., Key Exchange) as summa-
rized in 5.14.4.2. The Encryption payload (see 7.7.3.6.2) nests one set of IKEv2-SCSI payloads inside
another.
Based on the contents of the SECURITY PROTOCOL SPECIFIC field in the SECURITY PROTOCOL OUT CDB, the
device server shall:
a)
validate the contents of the NEXT PAYLOAD field in the IKEv2-SCSI header as shown in table 526,
before performing any decryption or integrity checking; and
b)
validate that the number of instances of each next payload value shown in table 526 occur in the
parameter data, after the encrypted data, if any, is decrypted and integrity checked (i.e., if the NEXT
PAYLOAD field in the IKEv2-SCSI header contains 2Eh, after the Encrypted payload is decrypted and
integrity checked).
If the next payload values in the IKEv2-SCSI header and the unencrypted SECURITY PROTOCOL OUT
parameter data do not meet the requirements shown in table 526 for the listed SECURITY PROTOCOL SPECIFIC
field contents, then the error shall be processed as described in 7.7.3.8.
Based on the contents of the SECURITY PROTOCOL SPECIFIC field in the SECURITY PROTOCOL IN CDB, the
device server shall:
a)
place one of the next payload values allowed by table 526 in the NEXT PAYLOAD field in the
IKEv2-SCSI header; and
b)
include the number of instances of each next payload value shown in table 526 in the parameter data
either before or after encryption, if applicable (i.e., if the NEXT PAYLOAD field in the IKEv2-SCSI header
contains 2Eh, before the contents of the Encrypted payload are encrypted and integrity check value is
computed).
Table 526 — Next payload values in SECURITY PROTOCOL OUT/IN parameter data (part 1 of 3)
Next payload value
Next payload
value allowed
in IKEv2-SCSI
header
Number of times
a next payload
value is allowed
SECURITY PROTOCOL OUT command with
SECURITY PROTOCOL SPECIFIC field set to 0102h (i.e., Key Exchange step)
Authentication step
not skipped
(see 5.14.4.1)
83h (i.e., IKEv2-SCSI Timeout Values)
Yes
81h (i.e., IKEv2-SCSI SA Cryptographic Algorithms)
Yes
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
No
22h (i.e., Key Exchange)
Yes
28h (i.e., Nonce)
Yes
00h (i.e., No Next Payload)
No
All other next payload codes
No


SECURITY PROTOCOL OUT command with
SECURITY PROTOCOL SPECIFIC field set to 0102h (i.e., Key Exchange step)
Authentication step
skipped
(see 5.14.4.1)
83h (i.e., IKEv2-SCSI Timeout Values)
Yes
81h (i.e., IKEv2-SCSI SA Cryptographic Algorithms)
Yes
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
Yes
22h (i.e., Key Exchange)
Yes
28h (i.e., Nonce)
Yes
00h (i.e., No Next Payload)
No
All other next payload codes
No
SECURITY PROTOCOL IN command with
SECURITY PROTOCOL SPECIFIC field set to 0102h (i.e., Key Exchange step)
Authentication step
not skipped
(see 5.14.4.1)
81h (i.e., IKEv2-SCSI SA Cryptographic Algorithms)
Yes
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
No
22h (i.e., Key Exchange)
Yes
28h (i.e., Nonce)
Yes
26h (i.e., Certificate Request)
Yes
0 or more
00h (i.e., No Next Payload)
No
All other next payload codes
No
SECURITY PROTOCOL IN command with
SECURITY PROTOCOL SPECIFIC field set to 0102h (i.e., Key Exchange step)
Authentication step
skipped
(see 5.14.4.1)
81h (i.e., IKEv2-SCSI SA Cryptographic Algorithms)
Yes
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
Yes
22h (i.e., Key Exchange)
Yes
28h (i.e., Nonce)
Yes
26h (i.e., Certificate Request)
Yes
0 or more
00h (i.e., No Next Payload)
No
All other next payload codes
No
Table 526 — Next payload values in SECURITY PROTOCOL OUT/IN parameter data (part 2 of 3)
Next payload value
Next payload
value allowed
in IKEv2-SCSI
header
Number of times
a next payload
value is allowed


SECURITY PROTOCOL OUT command with
SECURITY PROTOCOL SPECIFIC field set to 0103h (i.e., Authentication step)
2Eh (i.e., Encrypted)
Yes
23h (i.e., Identification – Application Client)
No
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
No
25h (i.e., Certificate)
No
0 or more
26h (i.e., Certificate Request)
No
0 or more
29h (i.e., Notify)
No
0 or 1
27h (i.e., Authentication)
No
00h (i.e., No Next Payload)
No
All other next payload codes
No
SECURITY PROTOCOL IN command with
SECURITY PROTOCOL SPECIFIC field set to 0103h (i.e., Authentication step)
2Eh (i.e., Encrypted)
Yes
24h (i.e., Identification – Device Server)
No
82h (i.e., IKEv2-SCSI SAUT Cryptographic Algorithms)
No
25h (i.e., Certificate)
No
0 or more
27h (i.e., Authentication)
No
00h (i.e., No Next Payload)
No
All other next payload codes
No
SECURITY PROTOCOL OUT command with
SECURITY PROTOCOL SPECIFIC field set to 0104h (i.e., Delete operation)
2Eh (i.e., Encrypted)
Yes
2Ah (i.e., Delete)
No
00h (i.e., No Next Payload)
No
All other next payload codes
No
Table 526 — Next payload values in SECURITY PROTOCOL OUT/IN parameter data (part 3 of 3)
Next payload value
Next payload
value allowed
in IKEv2-SCSI
header
Number of times
a next payload
value is allowed


7.7.3.5 IKEv2-SCSI payloads
7.7.3.5.1 IKEv2-SCSI payload format
Each IKEv2-SCSI payload (see table 527) is composed of a header and data that is specific to the payload
type.
The NEXT PAYLOAD field identifies the IKEv2-SCSI payload that follows this IKEv2-SCSI payload using one of
the code values shown in table 524 (see 7.7.3.4).
If a device server receives an IKEv2-SCSI payload that it does not recognize (e.g., an IKEv2-SCSI payload
identified by a next payload value of 01h) with the critical (CRIT) bit set to one, then the error shall be
processed as described in 7.7.3.8.
If an application client receives an IKEv2-SCSI payload that it does not recognize with the CRIT bit set to one,
then the application client should abandon the IKEv2-SCSI CCS and notify the device server that it is
abandoning the IKEv2-SCSI CCS as described in 5.14.4.10.
If an application client or device server receives an IKEv2-SCSI payload that it does not recognize with the
CRIT bit set to zero, then it should use the NEXT PAYLOAD field and the IKE PAYLOAD LENGTH field to skip
processing of the unrecognized IKEv2-SCSI payload and continue processing at the next IKEv2-SCSI
payload.
The IKE PAYLOAD LENGTH field specifies the total number of bytes in the payload, including the IKEv2-SCSI
payload header. The value in the IKE PAYLOAD LENGTH field need not be a multiple of two or four (i.e., no byte
alignment is maintained among IKEv2-SCSI payloads).
NOTE 64 - The contents of the IKE PAYLOAD LENGTH field differ from those found in most SCSI length fields,
however, they are consistent with the IKEv2 usage (see RFC 4306).
The format and contents of the IKEv2-SCSI payload-specific data depends on the value in the NEXT PAYLOAD
field of:
a)
the IKEv2-SCSI header (see 7.7.3.4), if this is the first IKEv2-SCSI payload in the parameter data; or
b)
the previous IKEv2-SCSI payload, in all other cases.
Table 527 — IKEv2-SCSI payload format
Bit
Byte
IKEv2-SCSI payload header
NEXT PAYLOAD
CRIT
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
IKEv2-SCSI payload-specific data
•••
n


7.7.3.5.2 No Next payload
A NEXT PAYLOAD field that is set to 00h (i.e., No Next payload) specifies that no more IKEv2-SCSI payloads
follow the current payload. The IKEv2-SCSI No Next payload contains no bytes and has no format.
7.7.3.5.3 Key Exchange payload
The Key Exchange payload (see table 528) transfers Diffie-Hellman shared key exchange data between an
application client and a device server or vice versa.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Key Exchange payload.
The DIFFIE-HELLMAN GROUP NUMBER field specifies the least significant 16 bits from ALGORITHM IDENTIFIER field
in the D-H IKEv2-SCSI algorithm descriptor (see 7.7.3.6.5) in the IKEv2-SCSI SA Cryptographic Algorithms
payload (see 7.7.3.5.13).
The KEY EXCHANGE DATA field specifies the sender's Diffie-Hellman public value for this key exchange. The
binary representation of key exchange data is defined in the reference cited for the Diffie-Hellman group that
is used (see table 553).
When a prime modulus (i.e., mod p) Diffie-Hellman group is used, the length of the Diffie-Hellman public value
shall be equal to the length of the prime modulus over which the exponentiation was performed as shown in
table 553 (see 7.7.3.6.5). Zero bits shall be prepended to the KEY EXCHANGE DATA field if necessary.
Diffie-Hellman exponential reuse and reuse of analogous Diffie-Hellman public values for Diffie-Hellman
mechanisms not based on exponentiation should not be performed, but if performed it shall be constrained
(e.g., requirements regarding when Diffie-Hellman information is discarded) as defined in RFC 4306. The
freshness and randomness of the random nonces are critical to the security of IKEv2-SCSI when
Diffie-Hellman exponentials and public values are reused (see RFC 4306).
Table 528 — Key Exchange payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
(MSB)
DIFFIE-HELLMAN GROUP NUMBER
(LSB)
Reserved
KEY EXCHANGE DATA
•••
n


7.7.3.5.4 Identification – Application Client payload and Identification – Device Server payload
The Identification – Application Client payload (see table 529) transfers identification information from the
application client to the device server. The Identification – Device Server payload (see table 529) transfers
identification information from the device server to the application client.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Identification – Application Client payload and the Identification – Device
Server payload.
The ID TYPE field describes the contents of the IDENTIFICATION DATA field and shall contain one of the named
values shown in table 530.
The contents of the IDENTIFICATION DATA field depend on the value in the ID TYPE field.
Table 529 — Identification payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
ID TYPE
Reserved

IDENTIFICATION DATA
•••
n
Table 530 — ID TYPE field
Code
Name a
Contents of the IDENTIFICATION DATA field
09h
ID_DER_ASN1_DN
The value of a certificate subject field (see RFC 5280)
0Ah
ID_DER_ASN1_GN
The value of a name contained in a Subject Alternative
Name (i.e., SubjectAltName) certificate extension (see
RFC 5280)
0Bh
ID_KEY_ID
Arbitrary identity data (e.g., initiator port names, target
port names, and SCSI device names)
0Ch
ID_FC_NAME
FC-SP-2 certificates that certify a Fibre Channel name
as an identity to be used (see RFC 4595 and FC-SP-2)
all other values
Prohibited
a See RFC 4306 and RFC 4595 for additional information about the associated identification
data for these names.


When the Certificate payload is included in the parameter data, the identity in the Identification – Application
Client payload or Identification – Device Server payload is not required to match anything in the Certificate
payload (see RFC 4306). A mechanism outside the scope of this standard shall be provided to configure any
application client or device server to require a match between the identity in an Identification payload and the
subject name or subject alternative name in a Certificate payload.
If a device server receives an Identification – Application Client payload that does not conform to the require-
ments in RFC 4306 or the requirements in this subclause, then the IKEv2-SCSI CCS state maintained for the
I_T_L nexus shall be abandoned as described in 7.7.3.8.3.
If an application client receives an Identification – Device Server payload that does not conform to the require-
ments in RFC 4306 or the requirements in this subclause, then the application client should abandon the
IKEv2-SCSI CCS and notify the device server that it is abandoning the IKEv2-SCSI CCS as described in
5.14.4.10.
7.7.3.5.5 Certificate payload
The Certificate payload (see table 531) delivers a requested identity authentication certificate. The protocol for
using Certificate payloads is described in 5.14.4.3.3.4.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Certificate payload.
Table 531 — Certificate payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
CERTIFICATE ENCODING
CERTIFICATE DATA
•••
n


The CERTIFICATE ENCODING field describes the contents of the CERTIFICATE DATA field and shall contain one of
the values shown in table 532.
The contents of the CERTIFICATE DATA field depend on the value in the CERTIFICATE ENCODING field.
The relationship between the Certificate payload and the Identification payload is described in 7.7.3.5.4.
Device servers that support certificates should support a mechanism outside the scope of this standard for
replacing certificates and have the ability to store more than one certificate to facilitate such replacements.
7.7.3.5.6 Certificate Request payload
The Certificate Request payload (see table 533) allows an application client or device server to request the
use of certificates as part of identity authentication and to name one or more trust anchors (see RFC 4306) for
the certificate verification process. The Certificate payload (see table 531) delivers a requested identity
authentication certificate. The protocol for using Certificate Request payloads is described in 5.14.4.3.3.4.
Table 532 — CERTIFICATE ENCODING field
Code
Description
Reference
00h
Reserved
01h to 03h
Prohibited
Annex D
04h
X.509 Certificate - Signature
RFC 4306
05h to 0Ah
Prohibited
Annex D
0Bh
Raw RSA Key
RFC 4306 and RFC 4718
0Ch to 0Dh
Prohibited
Annex D
0Eh to C8h
Restricted
IANA
C9h to FFh
Reserved
Table 533 — Certificate Request payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
CERTIFICATE ENCODING
Certification authority list
(MSB)
CERTIFICATE AUTHORITY [first]
•••
(LSB)
•••
n-19
(MSB)
CERTIFICATE AUTHORITY [last]
•••
n
(LSB)


The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Certificate Request payload.
The value in the CERTIFICATE ENCODING field (see table 532 in 7.7.3.5.5) indicates the type or format of certif-
icate being requested. Multiple Certificate Request payloads may be included in the parameter data trans-
ferred by a single command. If the parameter data contains more than one Certificate Request payload, each
Certificate Request payload should have a different value in the CERTIFICATE ENCODING field.
Each CERTIFICATION AUTHORITY field contains an indicator of a trusted authority for the certificate type indicated
by the CERTIFICATE ENCODING field in this Certificate Request payload. The indicator is a SHA-1 hash of the
public key of a trusted Certification Authority. The indicator is encoded as the SHA-1 hash of the Subject
Public Key Info element from the Trust Anchor certificate (see RFC 5280).
Device servers that support certificates should support a mechanism outside the scope of this standard for
replacing certification authority values, and shall have the ability to store one or more certification authority
values to facilitate such replacements.
7.7.3.5.7 Authentication payload
The Authentication payload (see table 534) allows the application client and a device server to verify that the
data transfers in their IKEv2-SCSI CCS have not be compromised by a man-in-the-middle attack (see
5.14.1.4).
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Authentication payload.
The AUTH METHOD field indicates the authentication algorithm to be applied to this Authentication payload. The
AUTH METHOD field contains the least significant eight bits of the ALGORITHM IDENTIFIER field in an
SA_AUTH_OUT or an SA_AUTH_IN algorithm descriptor (see 7.7.3.6.6) from the Key Exchange step (see
5.14.4.6).
If the contents of the AUTH METHOD field in the parameter data for the Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2) do not match the least significant eight bits in the ALGORITHM
Table 534 — Authentication payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
AUTH METHOD
Reserved

AUTHENTICATION DATA
•••
n


IDENTIFIER field in the SA_AUTH_OUT algorithm descriptor in the IKEv2-SCSI SA Cryptographic Algorithms
payload (see 7.7.3.5.13) in the Key Exchange step, then:
a)
the SECURITY PROTOCOL OUT command shall be terminated with CHECK CONDITION status,
with the sense key set to ABORTED COMMAND and the additional sense code set to AUTHENTI-
CATION FAILED; and
b)
the device server shall abandon the IKEv2-SCSI CCS (see 5.14.4.10).
If the contents of the AUTH METHOD field in the parameter data for the Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.7.3) do not match the least significant eight bits in the ALGORITHM
IDENTIFIER field in the SA_AUTH_IN algorithm descriptor in the IKEv2-SCSI SA Cryptographic Algorithms
payload in the Key Exchange step, then application client should abandon the IKEv2-SCSI CCS and notify the
device server that it is abandoning the IKEv2-SCSI CCS as described in 5.14.4.10.
In the Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2) parameter list, the
AUTHENTICATION DATA field contains the result of applying the algorithm specified by the ALGORITHM IDENTIFIER
field in the SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor in the IKEv2-SCSI SA Crypto-
graphic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see 5.14.4.6) as described in table
555 (see 7.7.3.6.6) and this subclause to the following concatenation of bytes:
1)
all the bytes in the Data-In Buffer returned by the Device Server Capabilities step (see 5.14.4.5)
SECURITY PROTOCOL IN command;
2)
all the bytes in the Data-Out Buffer sent by the Key Exchange step SECURITY PROTOCOL OUT
command (see 5.14.4.6.2) in the same IKEv2-SCSI CCS for which GOOD status was returned;
3)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Nonce payload (see
7.7.3.5.8) that was received in the Key Exchange step SECURITY PROTOCOL IN command in the
same IKEv2-SCSI CCS; and
4)
all the bytes produced by applying the PRF selected by the PRF IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) to
the following inputs:
1)
the SK_pi shared key (see 5.14.4.4); and
2)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Identification –
Application Client payload (see 7.7.3.5.4).
While processing the Authentication step SECURITY PROTOCOL OUT command, the device server shall
verify the contents of the AUTHENTICATION DATA field by applying the algorithm specified by the ALGORITHM
IDENTIFIER field in the SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor in the IKEv2-SCSI SA
Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see 5.14.4.6) as described in
table 555 (see 7.7.3.6.6) and this subclause to the following concatenation of bytes:
1)
all the bytes in the Data-In Buffer that the device server returned to any application client in response
to the last received Device Server Capabilities step SECURITY PROTOCOL IN command;
2)
all the bytes in the Data-Out Buffer received in the Key Exchange step SECURITY PROTOCOL OUT
command (see 5.14.4.6.2) in the same IKEv2-SCSI CCS for which GOOD status was returned;
3)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Nonce payload (see
7.7.3.5.8) sent in the Key Exchange step SECURITY PROTOCOL IN command in the same
IKEv2-SCSI CCS; and
4)
all the bytes produced by applying the PRF selected by the PRF IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) to
the following inputs:
1)
the SK_pi shared key (see 5.14.4.4); and
2)
all the bytes received in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Identifi-
cation – Application Client payload (see 7.7.3.5.4) of the parameter list being processed.


If the verification of the contents of the AUTHENTICATION DATA field is not successful, then:
a)
the SECURITY PROTOCOL OUT command shall be terminated with CHECK CONDITION status,
with the sense key set to ABORTED COMMAND and the additional sense code set to AUTHENTI-
CATION FAILED; and
b)
the device server shall abandon the IKEv2-SCSI CCS (see 5.14.4.10).
For the Authentication step SECURITY PROTOCOL IN command (see 5.14.4.7.3) parameter list, the device
server shall compute the AUTHENTICATION DATA field contents by applying the algorithm specified by the
ALGORITHM IDENTIFIER field in the SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor in the
IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see 5.14.4.6)
as described in table 555 (see 7.7.3.6.6) and this subclause to the following concatenation of bytes:
1)
all the bytes in the Data-In Buffer that the device server returned to any application client in response
to the last received Device Server Capabilities step SECURITY PROTOCOL IN command;
2)
all the bytes in the Data-In Buffer sent by the most recent Key Exchange step SECURITY
PROTOCOL IN command (see 5.14.4.6.3) in the same IKEv2-SCSI CCS for which GOOD status was
returned;
3)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Nonce payload (see
7.7.3.5.8) received in the Key Exchange step SECURITY PROTOCOL OUT command in the same
IKEv2-SCSI CCS; and
4)
all the bytes produced by applying the PRF selected by the PRF IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) to
the following inputs:
1)
the SK_pr shared key (see 5.14.4.4); and
2)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Identification –
Device Server payload (see 7.7.3.5.4).
After GOOD status is received for the Authentication step SECURITY PROTOCOL IN command, the appli-
cation client should verify the contents of the AUTHENTICATION DATA field by applying the algorithm specified by
the ALGORITHM IDENTIFIER field in the SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor in the
IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see 5.14.4.6)
as described in table 555 (see 7.7.3.6.6) and this subclause to the following concatenation of bytes:
1)
all the bytes in the Data-In Buffer returned by the Device Server Capabilities step (see 5.14.4.5)
SECURITY PROTOCOL IN command;
2)
all the bytes in the Data-In Buffer returned by the most recent Key Exchange step SECURITY
PROTOCOL IN command (see 5.14.4.6.3) in the same IKEv2-SCSI CCS for which GOOD status was
returned;
3)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Nonce payload (see
7.7.3.5.8) sent in the Key Exchange step SECURITY PROTOCOL OUT command in the same
IKEv2-SCSI CCS; and
4)
all the bytes produced by applying the PRF selected by the PRF IKEv2-SCSI cryptographic algorithm
descriptor (see 7.7.3.6.3) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) to
the following inputs:
1)
the SK_pr shared key (see 5.14.4.4); and
2)
all the bytes in the IKEv2-SCSI payload-specific data part (see 7.7.3.5.1) of the Identification –
Device Server payload (see 7.7.3.5.4) received in the SECURITY PROTOCOL IN parameter
data.
If the verification of the contents of the AUTHENTICATION DATA field is not successful, then the application client
should abandon the IKEv2-SCSI CCS and notify the device server that it is abandoning the IKEv2-SCSI CCS
as described in 5.14.4.10.


If the AUTH METHOD field is set to 01h (i.e., RSA Digital Signature) the RSA digital signature shall be encoded
with the EMSA-PKCS1-v1_5 signature encoding method as defined in RFC 2437 (see RFC 4718).
7.7.3.5.8 Nonce payload
The Nonce payload (see table 535) transfers one random nonce from the application client to the device
server or from the device server to the application client.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Nonce payload.
In the Key Exchange step SECURITY PROTOCOL OUT command (see 5.14.4.6.2) the NONCE DATA field
specifies the application client’s random nonce.
In the Key Exchange step SECURITY PROTOCOL IN command (see 5.14.4.6.3) the NONCE DATA field
indicates the device server’s random nonce.
The requirements that RFC 4306 places on the nonce data shall apply to this standard.
Table 535 — Nonce payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
NONCE DATA
•••
n


7.7.3.5.9 Notify payload
This standard uses the Notify payload (see table 536) only to provide initial contact notification from the appli-
cation client to the device server.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Notify payload.
The PROTOCOL ID field is set to one. If the device server receives a PROTOCOL ID field set to a value other than
one, then the IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in
7.7.3.8.3.
The SAI SIZE field is set to eight. If the device server receives a value other than eight in the SAI SIZE field, then
the IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3.
The NOTIFY MESSAGE TYPE field is set to 16 384 (i.e., INITIAL_CONTACT). If the device server receives a
value other than 16 384 in the NOTIFY MESSAGE TYPE field, then the IKEv2-SCSI CCS state maintained for the
I_T_L nexus shall be abandoned as described in 7.7.3.8.3.
The SAI field specifies the device server’s SAI. If the contents of the SAI field are not identical to the contents of
the IKE_SA DEVICE SERVER SAI field in the IKEv2-SCSI header (see 7.7.3.4), then the IKEv2-SCSI CCS state
maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3.
Unless an error is detected, the device server shall process the Notify payload as described in 5.14.4.7.2.
Table 536 — Notify payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (0010h)
(LSB)
PROTOCOL ID (01h)
SAI SIZE (08h)
(MSB)
NOTIFY MESSAGE TYPE (4000h)
(LSB)

Restricted (see RFC 4306)

•••

(MSB)
SAI

•••
(LSB)


7.7.3.5.10 Delete payload
The Delete payload (see table 537) requests the deletion of an existing SA or the abandonment of an
IKEv2-SCSI CCS that is in progress.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Delete payload.
The PROTOCOL ID field is set to one. If the device server receives a PROTOCOL ID field set to a value other than
one, then the error shall be processed as described in 7.7.3.8.3.
The SAI SIZE field is set to eight. If the device server receives a value other than eight in the SAI SIZE field, then
the error shall be processed as described in 7.7.3.8.3.
The AC_SAI field specifies the AC_SAI SA parameter value for the SA to be deleted. If the contents of the
AC_SAI field do not match the contents of the IKE_SA APPLICATION CLIENT SAI field in the IKEv2-SCSI header
(see 7.7.3.4), then the error shall be processed as described in 7.7.3.8.3.
The DS_SAI field specifies the DS_SAI SA parameter value for the SA to be deleted. If the contents of the
DS_SAI field do not match the contents of the IKE_SA DEVICE SERVER SAI field in the IKEv2-SCSI header (see
7.7.3.4), then the error shall be processed as described in 7.7.3.8.3.
Table 537 — Delete payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (0018h)
(LSB)
PROTOCOL ID (01h)
SAI SIZE (08h)
(MSB)
NUMBER OF SAIS (0002h)
(LSB)

Restricted (see RFC 4306)

•••

(MSB)
AC_SAI

•••
(LSB)

Restricted (see RFC 4306)

•••

(MSB)
DS_SAI

•••
(LSB)


If the device server is maintaining SA parameters for which the AC_SAI matches the contents of the AC_SAI
field and the DS_SAI matches the contents of the DS_SAI field, that set of SA parameters shall be deleted.
If the device server is maintaining state for an IKEv2-SCSI CCS on the I_T_L nexus on which the command
was received, the IKEv2-SCSI CCS shall be abandoned (see 5.14.4.10) if:
a)
the contents of the AC_SAI field match the application client’s SAI in the maintained state; and
b)
the contents of the DS_SAI field match the device server’s SAI in the maintained state.
7.7.3.5.11 Encrypted payload
7.7.3.5.11.1 Combined mode encryption
The following types of encryption algorithms are used in the Encrypted payload:
a)
non-combined modes that use separate algorithms to encrypt/decrypt and integrity check the
Encrypted payload; and
b)
combined modes in which a single encryption algorithm does both encryption/decryption and integrity
checking.
The ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.4) in
the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see
5.14.4.6) indicates the type of encryption algorithm to be applied to the Encrypted payload for IKEv2-SCSI
functions as follows:
a)
if the ALGORITHM IDENTIFIER field is not set to AUTH_COMBINED, a non-combined mode encryption
algorithm is being used; or
b)
if the ALGORITHM IDENTIFIER field is set to AUTH_COMBINED, a combined mode encryption algorithm
is being used.
If the Encrypted payload is in parameter data that is not associated with an active IKEv2-SCSI CCS, then the
integrity checking algorithm identifier that selects between combined and non-combined mode encryption is
found in the MGMT_DATA SA parameter (see 5.14.4.9).


7.7.3.5.11.2 Encrypted payload introduction
The Encrypted payload transfers (see table 538) one or more other IKEv2-SCSI payloads that are encrypted
and integrity checked from the application client to the device server and vice versa.
If IKEv2-SCSI parameter data contains the Encrypted payload, then the Encrypted payload is the first payload
in the parameter data (i.e., the NEXT PAYLOAD field in the IKEv2-SCSI header (see 7.7.3.5.1) contains 2Eh).
Since the NEXT PAYLOAD field in an Encrypted payload identifies the first payload in the CIPHERTEXT field, there
is no way to identify a payload following the Encrypted payload, and none are allowed.
The NEXT PAYLOAD field identifies the first IKEv2-SCSI payload in the CIPHERTEXT field using the coded values
shown in table 524 (see 7.7.3.5.1).
The CRIT bit and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the Encrypted payload.
The IKE PAYLOAD LENGTH field specifies the number of bytes that follow in the Encrypted payload. The number
of bytes in the CIPHERTEXT field is equal to the number of bytes in the plaintext (see table 539).
The INITIALIZATION VECTOR field specifies the initialization vector encryption algorithm input value. The size of
the initialization vector is defined by the encryption algorithm as shown in table 547 (see 7.7.3.6.2).
The CIPHERTEXT field contains an output of the encryption algorithm specified by the ALGORITHM IDENTIFIER
field in the ENCR IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.2) in the IKEv2-SCSI SA
Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key Exchange step (see 5.14.4.6) using the inputs:
a)
IKEv2-SCSI AAD is an encryption algorithm input as follows:
A)
if a non-combined mode encryption algorithm is being used (see 7.7.3.5.11.1), then no AAD input
is needed or provided; or
B)
if a combined mode encryption algorithm is being used (see 7.7.3.5.11.1), then the AAD
described in 7.7.3.5.11.3 is an input;
Table 538 — Encrypted payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
INITIALIZATION VECTOR
•••
i-1
i
CIPHERTEXT
•••
k-1
k
INTEGRITY CHECK VALUE
•••
n


b)
the contents of the INITIALIZATION VECTOR field (see table 547);
c)
the plaintext data shown in table 539; and
d)
the shared key value, key length, and salt value (see table 547 in 7.7.3.6.2) if any, for one of the
following shared keys:
A)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2) or the parameter data for a Delete operation
SECURITY PROTOCOL OUT command (see 5.14.4.11) that affects an active IKEv2-SCSI CCS,
then the SK_ei shared key (see 5.14.4.4) for the IKEv2-SCSI CCS;
B)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.7.3), then the SK_er shared key (see 5.14.4.4) for the
IKEv2-SCSI CCS.; or
C) if the Encrypted payload appears in the parameter data for a Delete operation SECURITY
PROTOCOL OUT command (see 5.14.4.11) that does not affect an active IKEv2-SCSI CCS, then
the SK_ei shared key (see 5.14.4.4) from the MGMT_DATA SA parameter (see 5.14.4.9).
NOTE 65 - Salt values (see table 547 in 7.7.3.6.2) are used only by combined mode encryption algorithms
(see 7.7.3.5.11.1).
If the Encrypted payload appears in the parameter data for a Delete operation SECURITY PROTOCOL OUT
command that does not affect an active IKEv2-SCSI CCS, then the encryption algorithm identifier stored in
the MGMT_DATA SA parameter indicates the encryption algorithm to use.
The INTEGRITY CHECK VALUE field contains the integrity check value that is computed as described in
7.7.3.5.11.1 (e.g., if the integrity algorithm is AUTH_COMBINED, then the integrity check value is an output of
the encryption algorithm). The size of the integrity check value is defined by the integrity algorithm or
encryption algorithm, depending on which algorithm computes the value.
If the integrity algorithm specified by the ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic
algorithm descriptor in the IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) in the Key
Exchange step is not AUTH_COMBINED, then the contents of the INTEGRITY CHECK VALUE field are computed
by processing the integrity check algorithm specified by the ALGORITHM IDENTIFIER field in the INTEG
IKEv2-SCSI cryptographic algorithm descriptor using the following inputs:
a)
a byte string composed of:
1)
the AAD described in 7.7.3.5.11.3;
2)
the contents of the INITIALIZATION VECTOR field (see table 538); and
3)
the ciphertext that is the result of encrypting the plaintext data;
and
b)
the shared key value from one of the following shared keys:
A)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2) or the parameter data for a Delete operation
SECURITY PROTOCOL OUT command (see 5.14.4.11) that affects an active IKEv2-SCSI CCS,
then the SK_ai shared key (see 5.14.4.4) for the IKEv2-SCSI CCS;
B)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.7.3), then the SK_ar shared key (see 5.14.4.4) for the
IKEv2-SCSI CCS.; or
C) if the Encrypted payload appears in the parameter data for a Delete operation SECURITY
PROTOCOL OUT command (see 5.14.4.11) that does not affect an active IKEv2-SCSI CCS, then
the SK_ai shared key (see 5.14.4.4) from the MGMT_DATA SA parameter (see 5.14.4.9).
If the Encrypted payload appears in the parameter data for a Delete operation SECURITY PROTOCOL OUT
command that does not affect an active IKEv2-SCSI CCS, then the integrity checking algorithm identifier
stored in the MGMT_DATA SA parameter indicates the integrity checking algorithm to use.


While computing the encrypted CIPHERTEXT field contents for an Encrypted payload, the plaintext shown in
table 539 is used.
Each IKEv2-SCSI payload (see 7.7.3.5) contains specific data related to the operation being performed. A
specific combination of IKEv2-SCSI payloads is needed for each operation (e.g., Authentication) as summa-
rized in 5.14.4.2.
The PADDING BYTES field contains zero to 255 bytes. The number of padding bytes is:
a)
defined by the encryption algorithm; or
b)
any number of bytes that causes the length of all plaintext bytes (i.e., l+2) to be a whole multiple of the
alignment (see table 547 in 7.7.3.6.2) for the encryption algorithm being used.
The contents of the padding bytes are:
a)
defined by the encryption algorithm; or
b)
if the encryption algorithm does not define the padding bytes contents, a series of one byte binary
values starting at one and incrementing by one in each successive byte (i.e., 01h in the first padding
byte, 02h in the second padding byte, etc.).
If the encryption algorithm does not place requirements on the contents of the padding bytes (i.e., option b) is
in effect), then after decryption the contents of the padding bytes shall be verified to match the series of one
byte binary values described in this subclause. If this verification is not successful in a device server, the error
shall be processed as described in 7.7.3.8.2. If this verification is not successful in an application client, the
decrypted data should be ignored.
The PAD LENGTH field specifies the number of bytes in the PADDING BYTES field.
7.7.3.5.11.3 IKEv2-SCSI AAD
The AAD defined by this standard for IKEv2-SCSI use is as follows:
1)
all the bytes in the IKEv2-SCSI Header (see 7.7.3.4); and
Table 539 — Plaintext format for Encrypted payload CIPHERTEXT field
Bit
Byte
IKEv2-SCSI payloads
IKEv2-SCSI payload [first] (see 7.7.3.5)
•••
•••
IKEv2-SCSI payload [last] (see 7.7.3.5)
•••
n
p
PADDING BYTES (if any)
•••
k-1
k
PAD LENGTH (k-p)


2)
all the bytes in the IKEv2-SCSI Payload Header (see 7.7.3.5.1) of the Encrypted payload (see
7.7.3.5.11).
7.7.3.5.11.4 Processing a received Encrypted payload
Before performing any checks of data contained in the CIPHERTEXT field, the contents of the INTEGRITY CHECK
VALUE field and CIPHERTEXT field shall be integrity checked and decrypted based on the contents of the IKE_SA
APPLICATION CLIENT SAI field and the IKE_SA DEVICE SERVER SAI field in the IKEv2-SCSI header (see 7.7.3.4) as
described in this subclause.
Computation of the comparison integrity check value and decryption of an Encrypted payload is performed as
follows:
1)
if a non-combined mode encryption algorithm is being used (see 7.7.3.5.11.1), then the comparison
integrity check value is computed by performing the integrity check algorithm specified by the
ALGORITHM IDENTIFIER field in the INTEG IKEv2-SCSI cryptographic algorithm descriptor using the
following inputs:
A)
a byte string composed of:
1)
the AAD described in 7.7.3.5.11.3;
2)
the contents of the INITIALIZATION VECTOR field (see table 538) in the Encrypted payload; and
3)
the contents of the ciphertext field (see table 538) in the Encrypted payload;
and
B)
the shared key value from one of the following shared keys:
a)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2) or the parameter data for a Delete operation
SECURITY PROTOCOL OUT command (see 5.14.4.11) that affects an active IKEv2-SCSI
CCS (see 3.1.72), then the SK_ai shared key (see 5.14.4.4) for the IKEv2-SCSI CCS;
b)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.7.3), then the SK_ar shared key (see 5.14.4.4) for the
IKEv2-SCSI CCS; or
c)
if the Encrypted payload appears in the parameter data for a Delete operation SECURITY
PROTOCOL OUT command (see 5.14.4.11) that does not affect an active IKEv2-SCSI CCS,
then the SK_ai shared key (see 5.14.4.4) from the MGMT_DATA SA parameter (see 3.1.133
and 5.14.4.9);
and
2)
decrypt the CIPHERTEXT field to produce plaintext data – and if a combined mode encryption algorithm
is being used (see 7.7.3.5.11.1), produce the comparison integrity check value – using the encryption
algorithm specified by the ALGORITHM IDENTIFIER field in the ENCR IKEv2-SCSI cryptographic
algorithm descriptor (see 7.7.3.6.2) in the IKEv2-SCSI SA Cryptographic Algorithms payload (see
7.7.3.5.13) in the Key Exchange step (see 5.14.4.6) using the inputs:
A)
IKEv2-SCSI AAD is an input to the encryption algorithm as follows:
a)
if a non-combined mode encryption algorithm is being used (see 7.7.3.5.11.1), then no AAD
input is needed or provided; or
b)
if a combined mode encryption algorithm is being used (see 7.7.3.5.11.1), then the AAD
described in 7.7.3.5.11.3 is an input;
B)
the contents of the INITIALIZATION VECTOR field (see table 538) in the Encrypted payload;
C) the contents of the ciphertext field (see table 538) in the Encrypted payload; and
D) the shared key value, key length, and salt value (see table 547 in 7.7.3.6.2) if any, for one of the
following shared keys:
a)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL OUT command (see 5.14.4.7.2), or the parameter data for a Delete operation
SECURITY PROTOCOL OUT command (see 5.14.4.11) that affects an active IKEv2-SCSI
CCS (see 3.1.72), then the SK_ei shared key (see 5.14.4.4) for the IKEv2-SCSI CCS;


b)
if the Encrypted payload appears in the parameter data for an Authentication step SECURITY
PROTOCOL IN command (see 5.14.4.7.3), then the SK_er shared key (see 5.14.4.4) for the
IKEv2-SCSI CCS; or
c)
if the Encrypted payload appears in the parameter data for a Delete operation SECURITY
PROTOCOL OUT command (see 5.14.4.11) that does not affect an active IKEv2-SCSI CCS,
then the SK_ei shared key (see 5.14.4.4) from the MGMT_DATA SA parameter (see 3.1.133
and 5.14.4.9).
If the Encrypted payload appears in the parameter data for a Delete operation SECURITY PROTOCOL OUT
command that does not affect an active IKEv2-SCSI CCS, then the integrity checking algorithm identifier
value and encryption algorithm identifier value that are stored in the MGMT_DATA SA parameter indicate the
integrity checking algorithm to use.
If the comparison integrity check value differs from the value in the INTEGRITY CHECK VALUE field of the
Encrypted payload:
a)
the application client should abandon the IKEv2-SCSI CCS and notify the device server that it is
abandoning the IKEv2-SCSI CCS as described in 5.14.4.10; and
b)
the device server shall respond to the mismatch as follows:
A)
if the IKEv2-SCSI header (see 7.7.3.4) specifies an attempt to provide authentication data for or
the deletion of an IKE-v2-SCSI CCS on the I_T_L nexus on which the command was received,
then:
a)
the SECURITY PROTOCOL OUT command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
SA CREATION PARAMETER VALUE REJECTED; and
b)
the device server shall continue the IKEv2-SCSI CCS by preparing to receive another
Authentication step SECURITY PROTOCOL OUT command;
or
B)
if the IKEv2-SCSI header (see 7.7.3.4) specifies the deletion of an active SA, then the SECURITY
PROTOCOL OUT command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.


7.7.3.5.12 IKEv2-SCSI SA Creation Capabilities payload
The IKEv2-SCSI SA Creation Capabilities payload (see table 540) lists all the security algorithms that the
device server allows to be used in an IKEv2-SCSI CCS. Events that are outside the scope of this standard
may change the contents of the IKEv2-SCSI SA Creation Capabilities payload at any time.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The NEXT PAYLOAD field is set to zero (i.e., No Next Payload) in the IKEv2-SCSI SA Creation Capabilities
payload.
The CRIT bit is set to one in the IKEv2-SCSI SA Creation Capabilities payload.
The NUMBER OF ALGORITHM DESCRIPTORS field specifies the number of IKEv2-SCSI cryptographic algorithm
descriptors that follow in the IKEv2-SCSI SA Creation Capabilities payload.
Each IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6) describes one combination of security
algorithm and algorithm attributes that the device server allows to be used in an IKEv2-SCSI CCS. If more
than one set of algorithm attributes (e.g., key length) is allowed for any allowed security algorithm, a different
SCSI cryptographic algorithms descriptor shall be included for each set of algorithm attributes.
The SCSI cryptographic algorithms descriptors shall be ordered by:
1)
increasing algorithm type;
2)
increasing algorithm identifier within the same algorithm type; and
3)
increasing key length, if any, within the same algorithm identifier.
Table 540 — IKEv2-SCSI SA Creation Capabilities payload format
Bit
Byte
NEXT PAYLOAD (00h)
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)
Reserved
NUMBER OF ALGORITHM DESCRIPTORS
IKEv2-SCSI cryptographic algorithm descriptors
IKEv2-SCSI cryptographic algorithm descriptor
[first] (see 7.7.3.6)
•••
•••
IKEv2-SCSI cryptographic algorithm descriptor
[last] (see 7.7.3.6)
•••
n


The algorithms allowed may be a subset of the algorithms supported by the device server.
The method for changing which of the device server supported algorithms are allowed is outside the scope of
this standard, but changes in allowed algorithms do not take effect until the new list is returned to any appli-
cation client in an IKEv2-SCSI SA Creation Capabilities payload.
7.7.3.5.13 IKEv2-SCSI SA Cryptographic Algorithms payload
The IKEv2-SCSI SA Cryptographic Algorithms payload (see table 541) lists the security algorithms that are
being used in the creation and management (e.g., deletion) of an SA using an IKEv2-SCSI CCS.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the IKEv2-SCSI SA Cryptographic Algorithms payload.
The USAGE DATA LENGTH field is set to zero in the IKEv2-SCSI SA Cryptographic Algorithms payload.
The NUMBER OF ALGORITHM DESCRIPTORS field specifies the number of IKEv2-SCSI cryptographic algorithm
descriptors that follow in the IKEv2-SCSI SA Cryptographic Algorithms payload. If a device server receives a
NUMBER OF ALGORITHM DESCRIPTORS field that does not contain six, then the error shall be processed as
described in 7.7.3.8.3.
Table 541 — IKEv2-SCSI SA Cryptographic Algorithms payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)

Reserved

•••

(MSB)
USAGE DATA LENGTH (0000h)
(LSB)

Reserved

•••

NUMBER OF ALGORITHM DESCRIPTORS
IKEv2-SCSI cryptographic algorithm descriptors

IKEv2-SCSI cryptographic algorithm descriptor
[first] (see 7.7.3.6)
•••
•••
IKEv2-SCSI cryptographic algorithm descriptor
[last] (see 7.7.3.6)
•••
n


Each IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6) describes one combination of security
algorithm and algorithm attributes to be used during the IKEv2-SCSI CCS.
The IKEv2-SCSI cryptographic algorithm descriptors are ordered as follows:
1)
one ENCR IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.2);
2)
one PRF IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.3);
3)
one INTEG IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.4);
4)
one D-H IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.5);
5)
one SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.6).
6)
one SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.6).
If a device server receives an IKEv2-SCSI SA Cryptographic Algorithms payload that does not contain the
IKEv2-SCSI cryptographic algorithm descriptors described in this subclause in the order described in this
subclause, then the error shall be processed as described in 7.7.3.8.3.
If the device server receives an IKEv2-SCSI SA Cryptographic Algorithms payload that contains an ENCR
IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set to ENCR_NULL, then
the error shall be processed as described in 7.7.3.8.3.
In the Key Exchange step SECURITY PROTOCOL IN parameter data (see 5.14.4.6.3), the device server
returns the IKEv2-SCSI SA Cryptographic Algorithms payload received during the Key Exchange step
SECURITY PROTOCOL OUT command (see 5.14.4.6.2) to confirm acceptance of the algorithms.


7.7.3.5.14 IKEv2-SCSI SAUT Cryptographic Algorithms payload
The IKEv2-SCSI SAUT Cryptographic Algorithms payload (see table 542) lists the usage type of and security
algorithms to be used by the SA that is created as a result of an IKEv2-SCSI CCS.
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the IKEv2-SCSI SAUT Cryptographic Algorithms payload.
The SA TYPE field specifies the usage type for the SA and is selected from among those listed in table 74 (see
5.14.2.2). An error shall be processed as described in 7.7.3.8.3 if any of the following conditions occur:
a)
the device server receives an SA usage type whose use the device server does not allow;
b)
an SA usage type between 8000h and BFFFh inclusive is received in a Key Exchange step
SECURITY PROTOCOL OUT command (see 5.14.4.6.2); or
Table 542 — IKEv2-SCSI SAUT Cryptographic Algorithms payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (n+1)
(LSB)

Reserved

(MSB)
SA TYPE
(LSB)
(MSB)
USAGE DATA LENGTH (j)
(LSB)
USAGE DATA

•••
16+j-1
16+j
Reserved

16+j+1
16+j+2
16+j+3
NUMBER OF ALGORITHM DESCRIPTORS
IKEv2-SCSI cryptographic algorithm descriptors
16+j+4
IKEv2-SCSI cryptographic algorithm descriptor
[first] (see 7.7.3.6)
•••
•••
IKEv2-SCSI cryptographic algorithm descriptor
[last] (see 7.7.3.6)
•••
n


c)
an SA usage type between A000h and CFFFh inclusive is received for which the device server is
unable to verify the applicable usage type constraints.
The method for changing which of the device server supported SA usage types are allowed is outside the
scope of this standard.
The USAGE DATA LENGTH field specifies number of bytes of usage data that follow.
The size and format of the usage data depends on the SA type (see table 74 in 5.14.2.2). If the device server
receives a USAGE DATA LENGTH field that contains a value that is inconsistent with the SA type, then the
error shall be processed as described in 7.7.3.8.3.
The USAGE DATA field contains information to be stored in the USAGE_DATA SA parameter (see 3.1.133) if the
SA is generated (see 5.14.4.9).
The NUMBER OF ALGORITHM DESCRIPTORS field specifies the number of IKEv2-SCSI cryptographic algorithm
descriptors that follow in the IKEv2-SCSI SAUT Cryptographic Algorithms payload. If a device server receives
a NUMBER OF ALGORITHM DESCRIPTORS field that contains a value other than two, then the error shall be
processed as described in 7.7.3.8.3.
Each IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6) describes one combination of security
algorithm and algorithm attributes to be used by the SA created as a result of the IKEv2-SCSI CCS. The
IKEv2-SCSI cryptographic algorithm descriptors are ordered as follows:
1)
one ENCR IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.2); and
2)
one INTEG IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.4).
If a device server receives an IKEv2-SCSI SAUT Cryptographic Algorithms payload that does not contain the
IKEv2-SCSI cryptographic algorithm descriptors described in this subclause in the order described in this
subclause, then the error shall be processed as described in 7.7.3.8.3.


7.7.3.5.15 IKEv2-SCSI Timeout Values payload
The IKEv2-SCSI Timeout Values payload (see table 543) specifies the timeout intervals associated with an
IKEv2-SCSI CCS
The NEXT PAYLOAD field, CRIT bit, and IKE PAYLOAD LENGTH field are described in 7.7.3.5.1.
The CRIT bit is set to one in the IKEv2-SCSI Timeout Values payload.
The NUMBER OF TIMEOUT VALUES field specifies the number of four-byte timeout values that follow. If the
number of timeout values is less than two, then the IKEv2-SCSI CCS state maintained for the I_T_L nexus
shall be abandoned as described in 7.7.3.8.3.
The IKEV2-SCSI PROTOCOL TIMEOUT field specifies the number of seconds that the device server shall wait for
the next command in the IKEv2-SCSI CCS. If the timeout expires before the device server receives an
IKEv2-SCSI CCS command, the device server shall abandon the IKEv2-SCSI CCS as described in 5.14.4.10.
The IKEV2-SCSI SA INACTIVITY TIMEOUT field specifies the number of seconds that the device server shall wait for
the next command that uses an SA. This value is copied to the TIMEOUT SA parameter when the SA is
generated (see 5.14.4.9).
The device server shall replace any timeout value that is set to zero with a value of ten (i.e., ten seconds).
The maximum value for the protocol timeout should be long enough to allow the application client to continue
the IKEv2-SCSI CCS, but short enough that if an incomplete IKEv2-SCSI CCS is abandoned, the device
server discards the state for that IKEv2-SCSI CCS and becomes available to for another IKEv2-SCSI CCS
without excessive delay.
Table 543 — IKEv2-SCSI Timeout Values payload format
Bit
Byte
NEXT PAYLOAD
CRIT (1b)
Reserved
(MSB)
IKE PAYLOAD LENGTH (0010h)
(LSB)
Reserved
NUMBER OF TIMEOUT VALUES (02h)
(MSB)
IKEV2-SCSI PROTOCOL TIMEOUT

•••
(LSB)
(MSB)
IKEV2-SCSI SA INACTIVITY TIMEOUT

•••
(LSB)


7.7.3.6 IKEv2-SCSI cryptographic algorithm descriptors
7.7.3.6.1 Overview
Each IKEv2-SCSI cryptographic algorithm descriptor (see table 544) specifies one algorithm used for
encryption, integrity checking, key generation, or authentication.
The ALGORITHM TYPE field (see table 545) specifies the type of cryptographic algorithm to which the
IKEv2-SCSI cryptographic algorithm descriptor applies.
The IKE DESCRIPTOR LENGTH field is set to 12 (i.e., the total number of bytes in the IKEv2-SCSI SA Crypto-
graphic Algorithms descriptor including the ALGORITHM TYPE field and reserved byte).
NOTE 66 - The contents of the IKE DESCRIPTOR LENGTH field differ from those found in most SCSI length
fields, however, they are consistent with the IKEv2 usage (see RFC 4306).
Table 544 — IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
ALGORITHM ATTRIBUTES

•••
Table 545 — ALGORITHM TYPE field
Code
Name
Description
Reference
01h
ENCR
Encryption algorithm
7.7.3.6.2
02h
PRF
Pseudo-random function
7.7.3.6.3
03h
INTEG
Integrity algorithm
7.7.3.6.4
04h
D-H
Diffie-Hellman group
7.7.3.6.5
05h to F0h
Restricted
RFC 4306
F9h
SA_AUTH_OUT
IKEv2-SCSI authentication algorithm
for SECURITY PROTOCOL OUT data
7.7.3.6.6
FAh
SA_AUTH_IN
IKEv2-SCSI authentication algorithm
for SECURITY PROTOCOL IN data
7.7.3.6.6
All others
Reserved


The contents of the ALGORITHM IDENTIFIER field and ALGORITHM ATTRIBUTES field depend on the contents of the
ALGORITHM TYPE field (see table 545). The ALGORITHM ATTRIBUTES field is reserved in some IKEv2-SCSI SA
Cryptographic Algorithms descriptor formats.
7.7.3.6.2 Encryption algorithm (ENCR) IKEv2-SCSI cryptographic algorithm descriptor
If the ALGORITHM TYPE field is set to ENCR (i.e., 01h) in an IKEv2-SCSI cryptographic algorithm descriptor (see
table 546), then the descriptor specifies an encryption algorithm to be applied during the IKEv2-SCSI Authen-
tication step (see 5.14.4.7), SA deletion operation (see 5.14.4.11), and when the SA created by the
IKEv2-SCSI is applied to user data.
The ALGORITHM TYPE field and IKE DESCRIPTOR LENGTH field are described in 7.7.3.6.1.
Table 546 — ENCR IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE (01h)
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
Reserved
(MSB)
KEY LENGTH
(LSB)


The ALGORITHM IDENTIFIER field (see table 547) specifies the encryption algorithm to which the ENCR
IKEv2-SCSI cryptographic algorithm descriptor applies.
ENCR_NULL indicates that encryption is not to be applied when the SA created by the IKEv2-SCSI is applied
to user data.
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains an IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13) that
contains:
a)
an ENCR IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set to
ENCR_NULL;
b)
the following combination of IKEv2-SCSI cryptographic algorithm descriptors (see 7.7.3.6.4):
A)
an INTEG IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to a value other than AUTH_COMBINED; and
Table 547 — ENCR ALGORITHM IDENTIFIER field
Code
Description
Salt a
length
(bytes)
IV b
length
(bytes)
Align-
ment c
(bytes)
Key
length
(bytes)
Support
Reference
8001 000Bh
ENCR_NULL d
n/a
Mandatory
8001 000Ch
AES-CBC d
n/a
Optional
RFC 3602
Prohibited
Optional
8001 0010h
AES-CCM
with a 16 byte
MAC e
Optional
RFC 4309
and
RFC 5282
Prohibited
Optional
8001 0014h
AES-GCM
with a 16 byte
MAC e
Optional
RFC 4106
and
RFC 5282
Prohibited
Optional
8001 0400h to
8001 FFFFh
Vendor Specific
0000 0000h to
0000 FFFFh
Restricted
IANA
All other values
Reserved
a See RFC 4106 and RFC 4309.
b Initialization Vector.
c The alignment required in the plaintext prior to encryption.
d If the INTEG cryptographic algorithm descriptor (see 7.7.3.6.4) in the same IKEv2-SCSI SA
Cryptographic Algorithms payload or the same IKEv2-SCSI SAUT Cryptographic Algorithms payload
as this ENCR cryptographic algorithm descriptor has the ALGORITHM IDENTIFIER field set to
AUTH_COMBINED, then the error shall be processed as described in 7.7.3.8.3.
e If the INTEG cryptographic algorithm descriptor (see 7.7.3.6.4) in the same IKEv2-SCSI SA
Cryptographic Algorithms payload or the same IKEv2-SCSI SAUT Cryptographic Algorithms payload
as this ENCR cryptographic algorithm descriptor does not have the ALGORITHM IDENTIFIER field set to
AUTH_COMBINED, then the error shall be processed as described in 7.7.3.8.3.


B)
an ENCR IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to a value that table 547 describes as requiring AUTH_COMBINED as the integrity check
algorithm;
or
c)
the following combination of IKEv2-SCSI cryptographic algorithm descriptors:
A)
an INTEG IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to AUTH_COMBINED; and
B)
an ENCR IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to a value that table 547 does not describe as requiring AUTH_COMBINED as the integrity check
algorithm.
The KEY LENGTH field specifies the number of bytes in the shared key for the encryption algorithm to which the
ENCR IKEv2-SCSI cryptographic algorithm descriptor applies.
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains:
a)
no ENCR IKEv2-SCSI cryptographic algorithm descriptors;
b)
more than one ENCR IKEv2-SCSI cryptographic algorithm descriptor;
c)
an ENCR IKEv2-SCSI cryptographic algorithm descriptor that does not appear in the SA Creations
Capabilities payload (see 7.7.3.5.12) last returned by the device server to any application client (i.e.,
an ENCR IKEv2-SCSI cryptographic algorithm descriptor for a combination of algorithm identifier and
key length that the device server has not reported as one of its SA creation capabilities); or
d)
an ENCR IKEv2-SCSI cryptographic algorithm descriptor that contains:
A)
an algorithm identifier that is not shown in table 547; or
B)
a key length that:
a)
does not match one of the values shown in table 547; or
b)
is not supported by the device server.
7.7.3.6.3 Pseudo-random function (PRF) IKEv2-SCSI cryptographic algorithm descriptor
If the ALGORITHM TYPE field is set to PRF (i.e., 02h) in an IKEv2-SCSI cryptographic algorithm descriptor (see
table 548), then the descriptor specifies the pseudo-random function and KDF to be used during the Key
Exchange step completion (see 5.14.4.6.4).
The ALGORITHM TYPE field and IKE DESCRIPTOR LENGTH field are described in 7.7.3.6.1.
Table 548 — PRF IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE (02h)
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
Reserved

•••


The ALGORITHM IDENTIFIER field (see table 549) specifies PRF and KDF to which the PRF IKEv2-SCSI crypto-
graphic algorithm descriptor applies.
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains:
a)
no PRF IKEv2-SCSI cryptographic algorithm descriptors;
b)
more than one PRF IKEv2-SCSI cryptographic algorithm descriptor;
c)
a PRF IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that does
not appear in the SA Creations Capabilities payload (see 7.7.3.5.12) last returned by the device
server to any application client; or
d)
an PRF IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that is not
shown in table 549.
Table 549 — PRF ALGORITHM IDENTIFIER field
Code
Description
Support
Output
length
(bytes)
Reference
PRF a
KDF b
8002 0002h
IKEv2-use based on SHA-1
Optional
RFC 2104
5.14.3.3
8002 0004h
IKEv2-use based on AES-128
in CBC mode
Optional
RFC 4434
5.14.3.4
8002 0005h
IKEv2-use based on SHA-256
Optional
RFC 4868
5.14.3.3
8002 0007h
IKEv2-use based on SHA-512
Optional
RFC 4868
5.14.3.3
8002 0400h to
8002 FFFFh
Vendor Specific
0000 0000h to
0000 FFFFh
Restricted
IANA
All others
Reserved
a PRFs are equivalent to the prf() functions defined in RFC 4306.
b KDFs are equivalent to the prf+() functions defined in RFC 4306.


7.7.3.6.4 Integrity algorithm (INTEG) IKEv2-SCSI cryptographic algorithm descriptor
If the ALGORITHM TYPE field is set to INTEG (i.e., 03h) in an IKEv2-SCSI cryptographic algorithm descriptor
(see table 550), then the descriptor specifies an integrity checking (i.e., data authentication) algorithm to be
applied during the IKEv2-SCSI Authentication step (see 5.14.4.7) and when the SA created by the
IKEv2-SCSI is applied to user data.
The ALGORITHM TYPE field and IKE DESCRIPTOR LENGTH field are described in 7.7.3.6.1.
The ALGORITHM IDENTIFIER field (see table 551) specifies integrity checking algorithm and shared key length to
which the INTEG IKEv2-SCSI cryptographic algorithm descriptor applies.
The AUTH_COMBINED integrity checking algorithm is used with encryption algorithms that include integrity
checking as described in 7.7.3.6.2. The AUTH_COMBINED algorithm identifier specifies that no additional
integrity check is performed, as indicated by the zero-length key.
Table 550 — INTEG IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE (03h)
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
Reserved

•••
Table 551 — INTEG ALGORITHM IDENTIFIER field
Code
IKEv2 Name
ICV a
length
(bytes)
Key
length
(bytes)
Support
Reference
8003 0002h
AUTH_HMAC_SHA1_96
Optional
RFC 2404
8003 000Ch
AUTH_HMAC_SHA2_256_128
Optional
RFC 4868
8003 000Eh
AUTH_HMAC_SHA2_512_256
Optional
RFC 4868
F003 0001h
AUTH_COMBINED
n/a
Optional
this
subclause
8003 0400h to
8003 FFFFh
Vendor Specific
0000 0000h to
0000 FFFFh
Restricted
IANA
All others
Reserved
a Integrity Check Value.


The key length used with an integrity checking algorithm is determined by the algorithm identifier as shown in
table 551.
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains:
a)
no INTEG IKEv2-SCSI cryptographic algorithm descriptors;
b)
more than one INTEG IKEv2-SCSI cryptographic algorithm descriptor;
c)
an INTEG IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that
does not appear in the SA Creations Capabilities payload (see 7.7.3.5.12) last returned by the device
server to any application client; or
d)
an INTEG IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that is
not shown in table 551.
7.7.3.6.5 Diffie-Hellman group (D-H) IKEv2-SCSI cryptographic algorithm descriptor
If the ALGORITHM TYPE field is set to D-H (i.e., 04h) in an IKEv2-SCSI cryptographic algorithm descriptor (see
table 552), then the descriptor specifies Diffie-Hellman group and Diffie-Hellman algorithm used during the
IKEv2-SCSI Key Exchange step (see 5.14.4.6) to derive a shared key that is known only to the application
client and device server.
The ALGORITHM TYPE field and IKE DESCRIPTOR LENGTH field are described in 7.7.3.6.1.
Table 552 — D-H IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE (04h)
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
Reserved

•••


The ALGORITHM IDENTIFIER field (see table 553) specifies Diffie-Hellman algorithm, group, and shared key
length to which the D-H IKEv2-SCSI cryptographic algorithm descriptor applies.
The key length of the public value transferred in the KEY EXCHANGE DATA field (see 7.7.3.5.3) is determined by
the algorithm identifier as shown in table 553.
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains:
a)
no D-H IKEv2-SCSI cryptographic algorithm descriptors;
b)
more than one D-H IKEv2-SCSI cryptographic algorithm descriptor;
c)
a D-H IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that does
not appear in the SA Creations Capabilities payload (see 7.7.3.5.12) last returned by the device
server to any application client; or
d)
an D-H IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier that is not
shown in table 553.
Table 553 — D-H ALGORITHM IDENTIFIER field
Code
Description
Key
length
(bytes)
Support
Reference
8004 000Eh
2 048-bit MODP group (finite field D-H)
Optional
RFC 3526
8004 000Fh
3 072-bit MODP group (finite field D-H)
Optional
RFC 3526
8004 0010h
4 096-bit MODP group (finite field D-H)
Optional
RFC 3526
8004 0013h
256-bit random ECP group
Optional
RFC 4753 a
8004 0015h
521-bit random ECP group
Optional
RFC 4753 a
8004 0400h to
8004 FFFFh
Vendor Specific
0000 0000h to
0000 FFFFh
Restricted
IANA
All others
Reserved
a The RFC Errata for RFC 4753 modify the binary representation of ECP key exchange data. The
modified binary representation shall be used, see http://rfc-editor.org/errata_search.php?rfc=4753.


7.7.3.6.6 IKEv2-SCSI authentication algorithm IKEv2-SCSI cryptographic algorithm descriptor
If the ALGORITHM TYPE field is set to SA_AUTH_OUT (i.e., F9h) in an IKEv2-SCSI cryptographic algorithm
descriptor (see table 554), then the descriptor specifies Authentication payload authentication algorithm used
by the IKEv2-SCSI Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2).
If the ALGORITHM TYPE field is set to SA_AUTH_IN (i.e., FAh) in an IKEv2-SCSI cryptographic algorithm
descriptor (see table 554), then the descriptor specifies Authentication payload authentication algorithm used
by the IKEv2-SCSI Authentication step SECURITY PROTOCOL IN command (see 5.14.4.7.3).
The ALGORITHM TYPE field and IKE DESCRIPTOR LENGTH field are described in 7.7.3.6.1.
Table 554 — SA_AUTH_OUT and SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor format
Bit
Byte
ALGORITHM TYPE (F9h or FAh)
Reserved
(MSB)
IKE DESCRIPTOR LENGTH (000Ch)
(LSB)
(MSB)
ALGORITHM IDENTIFIER

•••
(LSB)
Reserved

•••


The ALGORITHM IDENTIFIER field (see table 555) specifies Authentication payload authentication algorithm to
which the SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor or SA_AUTH_IN IKEv2-SCSI
cryptographic algorithm descriptor applies.
SA_AUTH_NONE specifies the omission of the IKEv2-SCSI Authentication step (see 5.14.4.7) as follows:
a)
the presence of an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and an
SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to SA_AUTH_NONE is an SA Creation Capabilities payload (see 7.7.3.5.12) indicates that the device
server is allowed to negotiate the omission of the IKEv2-SCSI Authentication step; and
b)
the presence of an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor and an
SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set
to SA_AUTH_NONE is an IKEv2-SCSI SA Cryptographic Algorithms payload (see 7.7.3.5.13)
indicates the following based upon the command whose parameter data carries the payload:
A)
in the parameter list for a Key Exchange SECURITY PROTOCOL OUT command (see
5.14.4.6.2), SA_AUTH_NONE specifies that the application client is requesting that the
IKEv2-SCSI Authentication step be skipped; and
B)
in the parameter data for a Key Exchange SECURITY PROTOCOL IN command (see 5.14.4.6.3),
SA_AUTH_NONE indicates that the device server has agreed to skip the IKEv2-SCSI Authenti-
cation step.
If it is reported by a device server in its capabilities and selected by an application client, then the IKEv2-SCSI
Authentication step is skipped and the resulting SAs are not authenticated.
Table 555 — SA_AUTH_OUT and SA_AUTH_IN ALGORITHM IDENTIFIER field
Code
Description
Support
Reference
Authentication
Reference a
00F9 0000h
SA_AUTH_NONE
Optional
this subclause
n/a
00F9 0001h
RSA Digital Signature with SHA-1 b
Optional
RFC 4306
5.14.4.3.3
00F9 0002h
Shared Key Message Integrity Code
Optional
RFC 4306  c, d
5.14.4.3.2
00F9 0009h
ECDSA with SHA-256 on the P-256
curve b
Optional
RFC 4754
5.14.4.3.3
00F9 000Bh
ECDSA with SHA-512 on the P-521
curve b
Optional
RFC 4754
5.14.4.3.3
00F9 00C9h to
00F9 00FFh
Vendor Specific
Optional
0000 0000h to
0000 FFFFh
Restricted
Prohibited
IANA
All others
Reserved
a Description of how the algorithm shall be used to generate and verify the contents of the
AUTHENTICATION DATA field of the Authentication Payload.
b Use of certificates with this digital signature authentication algorithm is optional.
c The 17 ASCII character non-terminated pre-shared key pad string "Key Pad for IKEv2" specified by
RFC 4306 is replaced by the 22 ASCII character non-terminated pre-shared key pad string 'Key Pad for
IKEv2-SCSI'.
d The pre-shared key requirements used by this standard (see 5.14.4.3.2) apply in addition to those found
in RFC 4306.


An SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field set to
SA_AUTH_NONE shall not appear in an IKEv2-SCSI SA Cryptographic Algorithms payload except as
described in 5.14.4.3.4.
The Shared Key Message Integrity Code is based on a pre-shared key (see 5.14.4.3.2) that is associated with
the identity in the Identification payload (see 7.7.3.5.4).
The IKEv2-SCSI CCS state maintained for the I_T_L nexus shall be abandoned as described in 7.7.3.8.3 if
the parameter list contains:
a)
no SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptors;
b)
no SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptors;
c)
more than one SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor;
d)
more than one SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor;
e)
an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm
identifier that does not appear in the SA Creations Capabilities payload (see 7.7.3.5.12) last returned
by the device server to any application client;
f)
an SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier
that does not appear in the SA Creations Capabilities payload last returned by the device server to
any application client;
g)
an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm
identifier that is not shown in table 555;
h)
an SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor that contains an algorithm identifier
that is not shown in table 555;
i)
an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER
field set to SA_AUTH_NONE, and an SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor
with the ALGORITHM IDENTIFIER field set to a value other than SA_AUTH_NONE; or
j)
an SA_AUTH_IN IKEv2-SCSI cryptographic algorithm descriptor with the ALGORITHM IDENTIFIER field
set to SA_AUTH_NONE, and an SA_AUTH_OUT IKEv2-SCSI cryptographic algorithm descriptor
with the ALGORITHM IDENTIFIER field set to a value other than SA_AUTH_NONE.


7.7.3.7 Errors in IKEv2-SCSI security protocol commands
For a single I_T_L nexus, the device server shall ensure that the two or four IKEv2-SCSI CCS commands are
processed in the order described in 5.14.4.1 based only on the contents of the CDB (i.e., the SECURITY
PROTOCOL OUT parameter data shall not be processed unless the tests in table 556 specify the processing
of the command) using the tests and responses shown in table 556.
Table 556 — IKEv2-SCSI command ordering processing requirements on a single I_T_L nexus (part 1
of 2)
IKEv2-SCSI
SECURITY
PROTOCOL OUT
command or
SECURITY
PROTOCOL IN
command received
Time
Before Key
Exchange
step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After a Key
Exchange
step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After a Key
Exchange
step
SECURITY
PROTOCOL
IN command
returns
GOOD status
After an
Authenticati
on step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After an
Authenticati
on step
SECURITY
PROTOCOL
IN command
returns
GOOD status
Key Exchange step
SECURITY
PROTOCOL OUT
command
Process the
command as
described in
this standard
Do not
process the
command a
Do not
process the
command a
Do not
process the
command a
Same as
before Key
Exchange
step
SECURITY
PROTOCOL
OUT
command
Key Exchange step
SECURITY
PROTOCOL IN
command
No
IKEv2-SCSI
CCS exists b
Process the
command as
described in
this standard
Repeat
processing
of the
command c
Do not
process the
command a
Do not
process the
command a
a The command shall be terminated and the IKEv2-SCSI CCS shall be continued as follows:
a)
the command shall be terminated with CHECK CONDITION status, with the sense key set to NOT
READY, and the additional sense code set to LOGICAL UNIT NOT READY, SA CREATION IN
PROGRESS; and
b)
the device server shall continue the IKEv2-SCSI CCS by preparing to receive another
IKEv2-SCSI CCS SECURITY PROTOCOL OUT command.
b The command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
c Processing of the SECURITY PROTOCOL IN commands in an IKEv2-SCSI CCS may be repeated.
The device server should save the information necessary to repeat processing of these commands
until the number of seconds specified in the IKEV2-SCSI PROTOCOL TIMEOUT field of the IKEv2-SCSI
Timeout Values payload (see 7.7.3.5.15) have elapsed since the processing of the Authentication step
SECURITY PROTOCOL OUT command that completed with GOOD status.


The processing shown in table 556 shall be performed before parameter data error handling described in
7.7.3.8.
Authentication step
SECURITY
PROTOCOL OUT
command
No
IKEv2-SCSI
CCS exists b
Do not
process the
command a
Process the
command as
described in
this standard
Do not
process the
command a
Do not
process the
command a
Authentication step
SECURITY
PROTOCOL IN
command
Do not
process the
command a
Do not
process the
command a
Process the
command as
described in
this standard
Repeat
processing
of the
command c
Command with an
invalid field in the
CDB
No
IKEv2-SCSI
CCS exists b
Do not
process the
command a
Do not
process the
command a
Do not
process the
command a
No
IKEv2-SCSI
CCS exists b
Table 556 — IKEv2-SCSI command ordering processing requirements on a single I_T_L nexus (part 2
of 2)
IKEv2-SCSI
SECURITY
PROTOCOL OUT
command or
SECURITY
PROTOCOL IN
command received
Time
Before Key
Exchange
step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After a Key
Exchange
step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After a Key
Exchange
step
SECURITY
PROTOCOL
IN command
returns
GOOD status
After an
Authenticati
on step
SECURITY
PROTOCOL
OUT
command
returns
GOOD status
After an
Authenticati
on step
SECURITY
PROTOCOL
IN command
returns
GOOD status
a The command shall be terminated and the IKEv2-SCSI CCS shall be continued as follows:
a)
the command shall be terminated with CHECK CONDITION status, with the sense key set to NOT
READY, and the additional sense code set to LOGICAL UNIT NOT READY, SA CREATION IN
PROGRESS; and
b)
the device server shall continue the IKEv2-SCSI CCS by preparing to receive another
IKEv2-SCSI CCS SECURITY PROTOCOL OUT command.
b The command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
c Processing of the SECURITY PROTOCOL IN commands in an IKEv2-SCSI CCS may be repeated.
The device server should save the information necessary to repeat processing of these commands
until the number of seconds specified in the IKEV2-SCSI PROTOCOL TIMEOUT field of the IKEv2-SCSI
Timeout Values payload (see 7.7.3.5.15) have elapsed since the processing of the Authentication step
SECURITY PROTOCOL OUT command that completed with GOOD status.


7.7.3.8 Errors in IKEv2-SCSI security protocol parameter data
7.7.3.8.1 Overview
Errors in the parameter data transferred to the device sever by an IKEv2-SCSI SECURITY PROTOCOL OUT
command are classified (see table 557) based on the ease with which they may be used to mount denial of
service attacks against IKEv2-SCSI SA creation operations by an attacker that has not participated
as the application client or device server in the Key Exchange step SECURITY PROTOCOL OUT command
(see 5.14.4.6.2) that started the IKEv2-SCSI CCS.
7.7.3.8.2 Errors with high denial of service attack potential
Errors detected before or during the decryption and integrity checking of an Encrypted payload in an Authenti-
cation step SECURITY PROTOCOL OUT command or a Delete operation SECURITY PROTOCOL OUT
command have a high potential for being a denial of service attack against one or more application clients
(see table 557 in 7.7.3.8.1).
The device server shall respond to these SECURITY PROTOCOL OUT command errors as follows:
a)
the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to SA CREATION PARAMETER VALUE
REJECTED; and
b)
the device server shall continue the IKEv2-SCSI CCS, if any, by preparing to receive an Authenti-
cation step SECURITY PROTOCOL OUT command.
If a specific field is the cause for returning the SA CREATION PARAMETER VALUE REJECTED additional
sense code, then the SKSV bit may be set to one. If the SKSV bit is set to one, then the SENSE KEY SPECIFIC field
shall be set as defined in 4.5.2.4.2.
Table 557 — IKEv2-SCSI parameter error categories
Denial of service
attack potential
Applicable SECURITY
PROTOCOL OUT
commands
Error handling description
Reference
High a
Authentication step, and
Delete operation
If possible, the IKEv2-SCSI
CCS state maintained for an
I_T_L nexus is not changed
7.7.3.8.2
Minimal b
Key Exchange step,
Authentication step, and
Delete operation
The IKEv2-SCSI CCS state
maintained for an I_T_L nexus
is abandoned
7.7.3.8.3
a Attacks capable of causing significant harm by sending a malformed IKEv2-SCSI SECURITY
PROTOCOL OUT command to the device server.
b Attacks that produce no significant harm, or collusive attacks (i.e., attacks that require knowledge
of the IKEv2-SCSI CCS shared keys and participation in the IKEv2-SCSI CCS). Collusive attacks
depend on collusion between the attacker and the application client (i.e., require the application
client to act against its own best interests). Abandoning the IKEv2-SCSI CCS is a justified
response to such attacks.


7.7.3.8.3 Errors with minimal denial of service attack potential
The errors that have minimal denial of service attack potential for IKEv2-SCSI SA creation (see table 557 in
7.7.3.8.1) are:
a)
all errors detected for a Key Exchange step SECURITY PROTOCOL OUT command or its associated
parameter data (e.g., errors detected in the IKEv2-SCSI header) that is attempting to establish a new
IKEv2-SCSI CCS on an I_T_L nexus; and
b)
all errors that are detected after the Encrypted payload has been successfully decrypted and integrity
checked in an Authentication step SECURITY PROTOCOL OUT command (see 5.14.4.7.2) or a
Delete operation SECURITY PROTOCOL OUT command (see 5.14.4.11).
The device server shall respond to these SECURITY PROTOCOL OUT command errors by terminating the
command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to SA CREATION PARAMETER VALUE INVALID. The state being maintained for an
IKEv2-SCSI CCS on the I_T_L nexus on which the command was received, if any, shall be abandoned (see
5.14.4.10).
If a specific field is the cause for returning the SA CREATION PARAMETER VALUE INVALID additional sense
code, then the SKSV bit shall be set to one and SENSE KEY SPECIFIC field shall be set as defined in 4.5.2.4.2.


7.7.3.9 Translating IKEv2 errors
IKEv2 (see RFC 4306) defines an error reporting mechanism based on the Notify payload. This standard
translates such error reports into the device server and application actions defined in this subclause.
If a device server is required by IKEv2 to report an error using a Notify payload, the device server shall
translate error into CHECK CONDITION status with the sense key and additional sense code shown in table
558. The device server shall terminate the SECURITY PROTOCOL OUT command (see 6.41) that trans-
ferred the parameter list in which the IKE requirements for one or more payloads (see 7.7.3.5) require use of
the Notify payload to report an error. The SECURITY PROTOCOL OUT command shall be terminated as
described in this subclause. The device server shall not report the IKE errors described in this subclause by
terminating a SECURITY PROTOCOL IN command (see 6.40) with CHECK CONDITION status.
If an application client detects an IKEv2 error that RFC 4306 requires to be reported with a Notify payload, the
application client then the application client should abandon the IKEv2-SCSI CCS and notify the device server
that it is abandoning the IKEv2-SCSI CCS as described in 5.14.4.10.
Table 558 — IKEv2 Notify payload error translations for IKEv2-SCSI
IKEv2 (see RFC 4306)
IKEv2-SCSI
Error Type
Description
Additional sense code
Sense key
0000h
Reserved
0001h
UNSUPPORTED_CRITICAL_
PAYLOAD
SA CREATION PARAMETER
NOT SUPPORTED
ILLEGAL REQUEST
0004h
INVALID_IKE_SPI
SA CREATION PARAMETER
VALUE INVALID
or
SA CREATION PARAMETER
VALUE REJECTED
0005h
INVALID_MAJOR_VERSION
0007h
INVALID_SYNTAX a
0009h
INVALID_MESSAGE_ID
000Bh
INVALID_SPI
SA CREATION PARAMETER
VALUE INVALID b
000Eh
NO_PROPOSAL_CHOSEN c
SA CREATION PARAMETER
VALUE INVALID
0011h
INVALID_KE_PAYLOAD c
0018h
AUTHENTICATION_FAILED
AUTHENTICATION FAILED
ABORTED COMMAND
0022h to
0027h
See RFC 4306 d
n/a
n/a
2000h to
3FFFh
Vendor Specific
All others
Restricted (see RFC 4306)
a This sense key and one of the additional sense codes shown shall be returned for a syntax error within
an Encrypted payload (see 7.7.3.5.11) regardless of conflicting IKEv2 requirements.
b SA CREATION PARAMETER VALUE INVALID shall be used for an invalid SAI in an IKEv2-SCSI
SECURITY PROTOCOL IN or SECURITY PROTOCOL OUT. The additional sense code for an invalid
SAI in all other commands is specified by the applicable usage type definition (see table 74 in 5.14.2.2).
c An application client recovers by restarting processing with the Device Capabilities step (see 5.14.4.5)
to rediscover the device server's capabilities.
d These IKEv2 Error Types are used for features that are not supported by IKEv2-SCSI SA creation.
