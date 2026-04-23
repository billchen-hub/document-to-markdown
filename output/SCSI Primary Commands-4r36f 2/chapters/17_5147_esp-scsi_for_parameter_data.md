# 5.14.7 ESP-SCSI for parameter data

B)
the CbCS capability key from the credential (see 5.14.6.8.12) in which the CbCS capability
descriptor was received by the secure CDB originator as the cryptographic key.
The enforcement manager shall validate the CbCS capability descriptor and the INTEGRITY CHECK VALUE field
as described in 5.14.6.8.13.2.
5.14.7 ESP-SCSI for parameter data
5.14.7.1 Overview
Subclause 5.14.7 defines a method for transferring encrypted and/or integrity checked parameter data in
Data-In Buffers, Data-Out Buffers, variable length CDBs (see 4.2.3), and extended CDBs (see 4.2.4). The
method is based on the Encapsulating Security Payload (see RFC 4303) standard developed by the IETF.
Because of the constrained usage of ESP-SCSI parameter data in Data-In Buffers and/or Data-Out Buffers,
the method defined in this standard differs from the one found in RFC 4303.
5.14.7.2 ESP-SCSI required inputs
Prior to using the ESP-SCSI descriptors defined in 5.14.7, an SA shall be created (see 5.14.2.3) with SA
parameters that conform to the requirements defined in 5.14.2.2 and to the following:
a)
the USAGE_TYPE SA parameter shall be set to a value for which ESP-SCSI usage is defined in table
74 (see 5.14.2.2);
b)
the USAGE_DATA SA parameter shall contain at least the following:
A)
the algorithm identifier and key length for the encryption algorithm (e.g., the ALGORITHM IDENTIFIER
field and KEY LENGTH field from the ENCR IKEv2-SCSI cryptographic algorithm descriptor (see
7.7.3.6.2) in the IKEv2-SCSI SAUT Cryptographic Algorithms payload (see 7.7.3.5.14) negotiated
by an IKEv2-SCSI SA creation protocol (see 5.14.4)); and
B)
the algorithm identifier for the integrity algorithm (e.g., the ALGORITHM IDENTIFIER field from the
INTEG IKEv2-SCSI cryptographic algorithm descriptor (see 7.7.3.6.4) in the IKEv2-SCSI SAUT
Cryptographic Algorithms payload (see 7.7.3.5.14) negotiated by an IKEv2-SCSI SA creation
protocol (see 5.14.4));
and
c)
the KEYMAT SA parameter shall consist of the shared keys described in 5.14.4.8.6.
ESP-SCSI depends on the following additional information derived from the contents of the USAGE_DATA SA
parameter:
a)
the encryption algorithm identifier shall indicate:
A)
the absence of encryption by having the value ENCR_NULL (see table 104 in 5.14.8);
B)
the size of the initialization vector, if any (e.g., as shown in table 547 (see 7.7.3.6.2));
C) the size of the salt bytes, if any (e.g., as shown in table 547 (see 7.7.3.6.2));
D) for combined mode encryption algorithms, the size of the integrity check value (i.e., the
algorithm's MAC size as shown in table 547 (see 7.7.3.6.2));
and
b)
the integrity algorithm identifier shall indicate:
A)
the use of a combined mode encryption algorithm by having the value AUTH_COMBINED (see
table 104 in 5.14.8);
B)
for non-combined mode encryption algorithms, the size of the integrity check value (e.g., as
shown in table 551 (see 7.7.3.6.4)).


Each shared key in KEYMAT shall be taken from the KDF generated bits in the order shown in 5.14.4.8.6. The
size of each of the shared keys in KEYMAT is determined by the negotiated encryption algorithm and integrity
algorithm as described in 5.14.4.4.
5.14.7.3 ESP-SCSI data format before encryption and after decryption
Before data bytes are encrypted and after they are decrypted, they have the format shown in table 93.
The UNENCRYPTED BYTES field contains the bytes that are to be protected via encryption or that have been
decrypted.
Before encryption, the PADDING BYTES field contains zero to 255 bytes. The number of padding bytes is:
a)
defined by the encryption algorithm; or
b)
the number needed to cause the length of all bytes prior to encryption (i.e., j+2) to be a whole multiple
of the alignment (see table 547 in 7.7.3.6.2) for the encryption algorithm being used.
The contents of the padding bytes are:
a)
defined by the encryption algorithm; or
b)
if the encryption algorithm does not define the padding bytes contents, a series of one byte binary
values starting at one and incrementing by one in each successive byte (i.e., 01h in the first padding
byte, 02h in the second padding byte, etc.).
If the encryption algorithm does not place requirements on the contents of the padding bytes (i.e., option b) is
in effect), then after decryption the contents of the padding bytes shall be verified to match the series of one
byte binary values described in this subclause. If this verification is not successful in a device server, the
device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, the additional sense code set to INVALID FIELD IN PARAMETER LIST, the SKSV bit set
to one, and SENSE KEY SPECIFIC field set to indicate the last byte in the encrypted data as defined in 4.5.2.4.2.
If this verification is not successful in an application client, the decrypted data should be ignored.
The PAD LENGTH field is set to the number of bytes in the PADDING BYTES field.
The MUST BE ZERO field is set to zero. After decryption, the contents of the MUST BE ZERO field shall be verified
to be zero. If this verification is not successful in a device server, the device server shall terminate the
command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, the additional
sense code set to INVALID FIELD IN PARAMETER LIST, the SKSV bit set to one, and SENSE KEY SPECIFIC field
Table 93 — ESP-SCSI data format before encryption and after decryption
Bit
Byte
UNENCRYPTED BYTES
•••
p-1
p
PADDING BYTES
•••
j-1
j
PAD LENGTH (j-p)
j+1
MUST BE ZERO


set to indicate the last byte in the encrypted data as defined in 4.5.2.4.2. If this verification is not successful in
an application client, the decrypted data should be ignored.
5.14.7.4 ESP-SCSI outbound data descriptors
5.14.7.4.1 Overview
If ESP-SCSI is used in a variable length CDB (see 4.2.3), an extended CDB (see 4.2.4), or parameter list data
that appears in a Data-Out Buffer, the parameter list data contains one or more descriptors selected based on
the criteria shown in table 94.
Table 94 — ESP-SCSI outbound data descriptors
Descriptor name
External
descriptor
length a
Initialization
vector
present b
Reference
ESP-SCSI CDB
No
No
table 95 in 5.14.7.4.2
No
Yes
table 96 in 5.14.7.4.2
ESP-SCSI Data-Out Buffer
No
No
table 95 in 5.14.7.4.2
No
Yes
table 96 in 5.14.7.4.2
ESP-SCSI Data-Out Buffer
without length
Yes
No
table 97 in 5.14.7.4.3
Yes
Yes
table 98 in 5.14.7.4.3
a This is determined by the data format defined for the Data-Out Buffer parameter
data. If the format includes a length for the ESP-SCSI descriptor, then the answer to
this question is yes.
b This is determined from the USAGE_DATA SA parameter (see 5.14.7.2).


5.14.7.4.2 ESP-SCSI CDBs or Data-Out Buffer parameter lists including a descriptor length
If the USAGE_DATA SA parameter (see 5.14.7.2) indicates an encryption algorithm whose initialization vector
size is zero, then the variable length CDB (see 4.2.3), extended CDB (see 4.2.4), or Data-Out Buffer
parameter list descriptor shown in table 95 contains the ESP-SCSI data.
The DESCRIPTOR LENGTH field, DS_SAI field, DS_SQN field, ENCRYPTED OR AUTHENTICATED DATA field, and
INTEGRITY CHECK VALUE field are defined after table 96 in this subclause.
Table 95 — ESP-SCSI CDBs or Data-Out Buffer parameter list descriptor without initialization vector
Bit
Byte
(MSB)
DESCRIPTOR LENGTH (n-1)
(LSB)

Reserved

(MSB)
DS_SAI

•••
(LSB)
(MSB)
DS_SQN

•••
(LSB)

ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


If the USAGE_DATA SA parameter indicates an indicates an encryption algorithm whose initialization vector
size (i.e., s) is greater than zero, the variable length CDB (see 4.2.3), extended CDB (see 4.2.4), or Data-Out
Buffer parameter data descriptor shown in table 96 contains the ESP-SCSI data.
The DESCRIPTOR LENGTH field specifies the number of bytes that follow in the ESP-SCSI CDB or ESP-SCSI
Data-Out Buffer parameter list descriptor.
The DS_SAI field is set to the value in the DS_SAI SA parameter (see 5.14.2.2) for the SA that is being used to
prepare the ESP-SCSI CDB or ESP-SCSI Data-Out Buffer parameter list descriptor. If the DS_SAI value is not
known to the device server, the device server shall terminate the command with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, the additional sense code set to INVALID FIELD IN
PARAMETER LIST, the SKSV bit set to one, and SENSE KEY SPECIFIC field set as defined in 4.5.2.4.2.
The DS_SQN field should be set to one plus the value in the application client’s DS_SQN SA parameter (see
5.14.2.2) for the SA that is being used to prepare the ESP-SCSI CDB or ESP-SCSI Data-Out Buffer
parameter list descriptor. Before sending the ESP-SCSI CDB or ESP-SCSI Data-Out Buffer parameter list, the
application client should copy the contents of the DS_SQN field to its DS_SQN SA parameter.
The device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, the additional sense code set to INVALID FIELD IN PARAMETER LIST, the SKSV bit set
to one, and SENSE KEY SPECIFIC field set as defined in 4.5.2.4.2 if any of the following conditions are detected:
a)
the DS_SQN field is set to zero;
b)
the value in the DS_SQN field is less than or equal to the value in the device server’s DS_SQN SA
parameter; or
Table 96 — ESP-SCSI CDBs or Data-Out Buffer full parameter list descriptor
Bit
Byte
(MSB)
DESCRIPTOR LENGTH (n-1)
(LSB)

Reserved

(MSB)
DS_SAI

•••
(LSB)
(MSB)
DS_SQN

•••
(LSB)
(MSB)
INITIALIZATION VECTOR

•••
16+s-1
(LSB)
16+s
ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


c)
the value in the DS_SQN field is greater than 32 plus the value in the device server’s DS_SQN SA
parameter.
If the DS_SQN SA parameter is equal to FFFF FFFF FFFF FFFFh, the device server shall delete the SA.
The INITIALIZATION VECTOR field, if any, contains a value that is used as an input into the encryption algorithm
and/or integrity algorithm specified by the SA specified by the DS_SAI field. The INITIALIZATION VECTOR field is
not encrypted. The encryption algorithm and/or integrity algorithm may define additional requirements for the
INITIALIZATION VECTOR field.
The ENCRYPTED OR AUTHENTICATED DATA field contains:
a)
if an encryption algorithm for the SA specified by the DS_SAI field is not ENCR_NULL, encrypted data
bytes for the following:
1)
the bytes in the UNENCRYPTED BYTES field (see 5.14.7.3);
2)
the bytes in the PADDING BYTES field (see 5.14.7.3);
3)
the PAD LENGTH field byte (see 5.14.7.3); and
4)
the MUST BE ZERO field byte (see 5.14.7.3);
or
b)
otherwise, the unencrypted data bytes.
If the integrity algorithm for the SA specified by the DS_SAI field is AUTH_COMBINED (see 5.14.7.2), then the
AAD input to the encryption algorithm is composed of the following bytes, in order:
1)
the bytes in the DS_SAI field; and
2)
the bytes in the DS_SQN field.
The INTEGRITY CHECK VALUE field contains a value that is computed as follows:
a)
if the integrity algorithm is not AUTH_COMBINED, the integrity check value is computed using the
specified integrity algorithm with the following bytes as inputs, in order:
1)
the bytes in the DS_SAI field;
2)
the bytes in the DS_SQN field;
3)
the bytes in the INITIALIZATION VECTOR field, if any; and
4)
the bytes in the ENCRYPTED OR AUTHENTICATED DATA field after encryption, if any, has been
performed;
or
b)
if the integrity algorithm is AUTH_COMBINED, the integrity check value is computed as an additional
output of the specified encryption algorithm.
Upon receipt of ESP-SCSI CDB or ESP-SCSI Data-Out Buffer parameter data, the device server shall
compute an integrity check value for the ESP-SCSI CDB or ESP-SCSI Data-Out Buffer parameter data as
specified by the algorithms specified by the SA specified by the DS_SAI field using the inputs shown in this
subclause. If the computed integrity check value does not match the value in the INTEGRITY CHECK VALUE field,
the device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, the additional sense code set to INVALID FIELD IN PARAMETER LIST, the SKSV bit set
to one, and SENSE KEY SPECIFIC field set as defined in 4.5.2.4.2.
If the command is not terminated due to a sequence number error or a mismatch between the computed
integrity check value and the contents of the INTEGRITY CHECK VALUE field, then the device server shall copy
the contents of the received DS_SQN field to its DS_SQN SA parameter.


5.14.7.4.3 ESP-SCSI Data-Out Buffer parameter lists for externally specified descriptor length
If the USAGE_DATA SA parameter (see 5.14.7.2) indicates an encryption algorithm whose initialization vector
size is zero and the length of the ESP-SCSI Data-Out Buffer parameter list descriptor appears elsewhere in
the parameter list, then the Data-Out Buffer parameter list descriptor shown in table 97 contains the
ESP-SCSI data.
The DS_SAI field, DS_SQN field, ENCRYPTED OR AUTHENTICATED DATA field, and INTEGRITY CHECK VALUE field are
defined in 5.14.7.4.2.
Table 97 — ESP-SCSI Data-Out Buffer parameter list descriptor without length and initialization vector
Bit
Byte

Reserved

•••

(MSB)
DS_SAI

•••
(LSB)
(MSB)
DS_SQN

•••
(LSB)

ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


If the USAGE_DATA SA parameter indicates an indicates an encryption algorithm whose initialization vector
size (i.e., s) is greater than zero and the length of the ESP-SCSI Data-Out Buffer parameter list descriptor
appears elsewhere in the parameter list, the Data-Out Buffer parameter list descriptor shown in table 98
contains the ESP-SCSI data.
The DS_SAI field, DS_SQN field, INITIALIZATION VECTOR field, ENCRYPTED OR AUTHENTICATED DATA field, and
INTEGRITY CHECK VALUE field are defined in 5.14.7.4.2.
5.14.7.5 ESP-SCSI Data-In Buffer parameter data descriptors
5.14.7.5.1 Overview
A device server shall transfer ESP-SCSI parameter data descriptors in a Data-In Buffer only in response to a
request that specifies an SA using the AC_SAI SA parameter and DS_SAI SA parameter values (see
5.14.2.2). If the specified combination of AC_SAI and DS_SAI values in a command that requests the transfer
of ESP-SCSI parameter data descriptors is not known to the device server, the device server shall terminate
the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, the additional
sense code set to INVALID FIELD IN PARAMETER LIST or to INVALID FIELD IN CDB, the SKSV bit set to
one, and SENSE KEY SPECIFIC field set as defined in 4.5.2.4.2.
Table 98 — ESP-SCSI Data-Out Buffer parameter list descriptor without length
Bit
Byte

Reserved

•••

(MSB)
DS_SAI

•••
(LSB)
(MSB)
DS_SQN

•••
(LSB)
(MSB)
INITIALIZATION VECTOR

•••
16+s-1
(LSB)
16+s
ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


If ESP-SCSI is used in parameter data which appears in a Data-In Buffer, the parameter data contains one or
more descriptors selected based on the criteria shown in table 99.
If ESP-SCSI parameter data descriptors are used in a Data-In Buffer, then the outbound data (see 5.14.7.4)
should include at least one ESP-SCSI descriptor using the same SA to thwart known plaintext attacks (see
5.14.1.4).
5.14.7.5.2 ESP-SCSI Data-In Buffer parameter data including a descriptor length
If the USAGE_DATA SA parameter (see 5.14.7.2) indicates an encryption algorithm whose initialization vector
size is zero, then the Data-In Buffer parameter data descriptor shown in table 100 contains the ESP-SCSI
data.
Table 99 — ESP-SCSI Data-In Buffer parameter data descriptors
Descriptor name
External
descriptor
length a
Initialization
vector
present b
Reference
ESP-SCSI Data-In Buffer
No
No
table 100 in 5.14.7.5.2
No
Yes
table 101 in 5.14.7.5.2
ESP-SCSI Data-In Buffer
without length
Yes
No
table 102 in 5.14.7.5.3
Yes
Yes
table 103 in 5.14.7.5.3
a This is determined by the data format defined for the Data-In Buffer parameter data.
If the format includes a length for the ESP-SCSI descriptor, then the answer to this
question is yes.
b This is determined from the USAGE_DATA SA parameter (see 5.14.7.2).
Table 100 — ESP-SCSI Data-In Buffer parameter data descriptor without initialization vector
Bit
Byte
(MSB)
DESCRIPTOR LENGTH (n-1)
(LSB)

Reserved

(MSB)
AC_SAI

•••
(LSB)
(MSB)
AC_SQN

•••
(LSB)

ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


The DESCRIPTOR LENGTH field, AC_SAI field, AC_SQN field, ENCRYPTED OR AUTHENTICATED DATA field, and
INTEGRITY CHECK VALUE field are defined after table 101 in this subclause.
If the USAGE_DATA SA parameter indicates an indicates an encryption algorithm whose initialization vector
size (i.e., s) is greater than zero, the Data-In Buffer parameter data descriptor shown in table 101 contains the
ESP-SCSI data.
The DESCRIPTOR LENGTH field specifies the number of bytes that follow in the ESP-SCSI Data-In Buffer
parameter data descriptor.
The AC_SAI field is set to the value in the AC_SAI SA parameter (see 5.14.2.2) for the SA that is being used to
prepare the ESP-SCSI Data-In Buffer parameter data descriptor. If the AC_SAI value is not known to the
application client, the ESP-SCSI data-in parameter data descriptor should be ignored.
The AC_SQN field is set to one plus the value in the device server’s AC_SQN SA parameter (see 5.14.2.2) for
the SA that is being used to prepare the ESP-SCSI data-on buffer parameter data descriptor. Before sending
the ESP-SCSI Data-Out Buffer parameter list as part of a command that completes with GOOD status, the
device server shall copy the contents of the AC_SQN field to its AC_SQN SA parameter. The device server
shall not send two ESP-SCSI Data-Out Buffer parameter data descriptors that contain the same values in
AC_SAI field and AC_SQN field.
If the AC_SQN SA parameter is equal to FFFF FFFF FFFF FFFFh, the device server shall delete the SA after
the Data-In Buffer parameter data containing that value is sent.
Table 101 — ESP-SCSI Data-In Buffer full parameter data descriptor
Bit
Byte
(MSB)
DESCRIPTOR LENGTH (n-1)
(LSB)

Reserved

(MSB)
AC_SAI

•••
(LSB)
(MSB)
AC_SQN

•••
(LSB)
(MSB)
INITIALIZATION VECTOR

•••
16+s-1
(LSB)
16+s
ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


The application client should ignore the ESP-SCSI data-in parameter data descriptor if any of the following
conditions are detected:
a)
the AC_SQN field is set to zero;
b)
the value in the AC_SQN field is less than or equal to the value in the application client’s AC_SQN SA
parameter; or
c)
the value in the AC_SQN field is greater than 32 plus the value in the application client’s AC_SQN SA
parameter.
The INITIALIZATION VECTOR field, if any, contains a value that is used as an input into the encryption algorithm
and/or integrity algorithm specified by the SA specified by the AC_SAI field. The INITIALIZATION VECTOR field is
not encrypted. The encryption algorithm and/or integrity algorithm may define additional requirements for the
INITIALIZATION VECTOR field.
The ENCRYPTED OR AUTHENTICATED DATA field contains:
a)
if an encryption algorithm specified by the SA specified by the AC_SAI field is not ENCR_NULL,
encrypted data bytes for the following:
1)
the bytes in the UNENCRYPTED BYTES field (see 5.14.7.3);
2)
the bytes in the PADDING BYTES field (see 5.14.7.3);
3)
the PAD LENGTH field byte (see 5.14.7.3); and
4)
the MUST BE ZERO field byte (see 5.14.7.3);
or
b)
otherwise, the unencrypted data bytes.
If the integrity algorithm for the SA specified by the AC_SAI field is AUTH_COMBINED (see 5.14.7.2), then the
AAD input to the encryption algorithm is composed of the following bytes, in order:
1)
the bytes in the AC_SAI field; and
2)
the bytes in the AC_SQN field;
The INTEGRITY CHECK VALUE field contains a value that is computed as follows:
a)
if the integrity algorithm is not AUTH_COMBINED, the integrity check value is computed using the
specified integrity algorithm with the following bytes as inputs, in order:
1)
the bytes in the AC_SAI field;
2)
the bytes in the AC_SQN field;
3)
the bytes in the INITIALIZATION VECTOR field, if any; and
4)
the bytes in the ENCRYPTED OR AUTHENTICATED DATA field after encryption, if any, has been
performed;
or
b)
if the integrity algorithms is AUTH_COMBINED, the integrity check value is computed as an additional
output of the specified encryption algorithm.
Upon receipt of ESP-SCSI Data-In Buffer parameter data, the application client should compute an integrity
check value for the ESP-SCSI parameter data as specified by the algorithms specified by the SA specified by
the AC_SAI field using the inputs shown in this subclause. If the computed integrity check value does not match
the value in the INTEGRITY CHECK VALUE field, the results returned by the command should be ignored.
The application client should copy the contents of the AC_SQN field to its AC_SQN SA parameter if all of the
following are true:
a)
the command completed with GOOD status;


b)
the ESP-SCSI data-in parameter data descriptor was not ignored due to inconsistency problems with
the AC_SQN field; and
c)
the computed integrity check value matched the contents of the INTEGRITY CHECK VALUE field.
5.14.7.5.3 ESP-SCSI Data-In Buffer parameter data for externally specified descriptor length
If the USAGE_DATA SA parameter (see 5.14.7.2) indicates an encryption algorithm whose initialization vector
size is zero and the length of the ESP-SCSI Data-In Buffer parameter data descriptor appears elsewhere in
the parameter data, then the Data-In Buffer parameter data descriptor shown in table 102 contains the
ESP-SCSI data.
The AC_SAI field, AC_SQN field, ENCRYPTED OR AUTHENTICATED DATA field, and INTEGRITY CHECK VALUE field are
defined in 5.14.7.5.2.
Table 102 — ESP-SCSI Data-In Buffer parameter data descriptor without length and initialization
vector
Bit
Byte

Reserved

•••

(MSB)
AC_SAI

•••
(LSB)
(MSB)
AC_SQN

•••
(LSB)

ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


If the USAGE_DATA SA parameter indicates an indicates an encryption algorithm whose initialization vector
size (i.e., s) is greater than zero and the length of the ESP-SCSI Data-In Buffer parameter data descriptor
appears elsewhere in the parameter data, the Data-In Buffer parameter data descriptor shown in table 103
contains the ESP-SCSI data.
The AC_SAI field, AC_SQN field, INITIALIZATION VECTOR field, ENCRYPTED OR AUTHENTICATED DATA field, and
INTEGRITY CHECK VALUE field are defined in 5.14.7.5.2.
Table 103 — ESP-SCSI Data-In Buffer parameter data descriptor without length
Bit
Byte

Reserved

•••

(MSB)
AC_SAI

•••
(LSB)
(MSB)
AC_SQN

•••
(LSB)
(MSB)
INITIALIZATION VECTOR

•••
16+s-1
(LSB)
16+s
ENCRYPTED OR AUTHENTICATED DATA
•••
i-1
i
(MSB)
INTEGRITY CHECK VALUE

•••
n
(LSB)


5.14.8 Security algorithm codes
Table 104 lists the security algorithm codes used in security protocol parameter data.
Table 104 — Security algorithm codes (part 1 of 2)
Code
Description
Reference
Encryption algorithms
0001 000Ch
CBC-AES-256-HMAC-SHA-1
IEEE 1619.1
0001 0010h
CCM-128-AES-256
IEEE 1619.1
0001 0014h
GCM-128-AES-256
IEEE 1619.1
0001 0016h
XTS-AES-256-HMAC-SHA-512
IEEE 1619.1
8001 000Bh a
ENCR_NULL
7.7.3.6.2
8001 000Ch a
AES-CBC
RFC 3602
8001 0010h a
AES-CCM with a 16 byte MAC
RFC 4309
8001 0014h a
AES-GCM with a 16 byte MAC
RFC 4106
8001 0400h to
8001 FFFFh
Vendor specific
PRF and KDF algorithms b
8002 0002h a
IKEv2-use based on SHA-1
table 549
(see 7.7.3.6.3)
8002 0004h a
IKEv2-use based on AES-128 in CBC mode
8002 0005h a
IKEv2-use based on SHA-256
8002 0007h a
IKEv2-use based on SHA-512
8002 0400h to
8002 FFFFh
Vendor specific
Integrity checking (i.e., AUTH) algorithms
8003 0002h a
AUTH_HMAC_SHA1_96
RFC 2404
8003 000Ch a
AUTH_HMAC_SHA2_256_128
RFC 4868
8003 000Eh a
AUTH_HMAC_SHA2_512_256
RFC 4868
F003 0000h
AUTH_COMBINED
7.7.3.6.4
8003 0400h to
8003 FFFFh
Vendor specific
a The lower order 16 bits of this code value are assigned to match an IANA assigned value, if any, for an
equivalent IKEv2 encryption algorithm and values of 800xh in the high order 16 bits have x selected to
match the IANA assigned IKEv2 transform type (e.g., 8001h – Encryption Algorithms, 8002h – PRFs
and KDFs).
b PRFs are equivalent to the prf() functions defined in RFC 4306. KDFs are equivalent to the prf+()
functions defined in RFC 4306.
c The low order 8 bits of this code value are assigned to match the auth method field in the Authentication
payload (see 7.7.3.5.7).


5.15 Self-test operations
5.15.1 Overview
The SEND DIAGNOSTIC command (see 6.42) provides methods for an application client to request that a
SCSI target device perform self test operations. This standard defines the following self-tests:
a)
the default self-test (see 5.15.2);
b)
the short self-test (see 5.15.3); and
c)
the extended self-test (see 5.15.3).
Diffie-Hellman algorithms
8004 000Eh a
2 048-bit MODP group (finite field D-H)
RFC 3526
8004 000Fh a
3 072-bit MODP group (finite field D-H)
RFC 3526
8004 0010h a
4 096-bit MODP group (finite field D-H)
RFC 3526
8004 0013h a
256-bit random ECP group
RFC 4753
8004 0015h a
521-bit random ECP group
RFC 4753
8004 0400h to
8004 FFFFh
Vendor specific
SA Authentication payload authentication algorithms
00F9 0000h c
SA_AUTH_NONE
5.14.4.3.4 and 7.7.3.6.6
00F9 0001h c
RSA Digital Signature with SHA-1
RFC 4306
00F9 0002h c
Shared Key Message Integrity Code
RFC 4306
00F9 0009h c
ECDSA with SHA-256 on the P-256 curve
RFC 4754
00F9 000Bh c
ECDSA with SHA-512 on the P-521 curve
RFC 4754
00F9 00C9h to
00F9 00FFh
Vendor specific
Other algorithms
0000 0000h to
0000 FFFFh
Restricted
IANA
All other values
Reserved
Table 104 — Security algorithm codes (part 2 of 2)
Code
Description
Reference
a The lower order 16 bits of this code value are assigned to match an IANA assigned value, if any, for an
equivalent IKEv2 encryption algorithm and values of 800xh in the high order 16 bits have x selected to
match the IANA assigned IKEv2 transform type (e.g., 8001h – Encryption Algorithms, 8002h – PRFs
and KDFs).
b PRFs are equivalent to the prf() functions defined in RFC 4306. KDFs are equivalent to the prf+()
functions defined in RFC 4306.
c The low order 8 bits of this code value are assigned to match the auth method field in the Authentication
payload (see 7.7.3.5.7).


5.15.2 Default self-test
The default self-test is mandatory for all SCSI target device types that support the SEND DIAGNOSTIC
command. The operations performed for the default self-test are not defined by this standard. An application
client requests that a SCSI target device perform a default self-test by setting the SELFTEST bit to one in the
SEND DIAGNOSTIC command (see 6.42).
An application client may use the DEVOFFL bit and the UNITOFFL bit in the SEND DIAGNOSTIC command to
allow the device server to perform operations during a default self-test that affect conditions for one or more
logical units in the SCSI target device (e.g., if the DEVOFFL bit is set to one, then the device server may clear
established reservations while performing the test, and if the UNITOFFL bit is set to one, then the logical unit
may alter its medium while performing the test).
While a SCSI target device is performing a default self-test, the device server shall terminate all commands
received while the self-test is in progress, except INQUIRY, REPORT LUNS, and REQUEST SENSE, with
CHECK CONDITION status with the sense key set to NOT READY and the additional sense code set to
LOGICAL UNIT NOT READY, SELF-TEST IN PROGRESS. If the device server receives an INQUIRY
command, a REPORT LUNS command, or a REQUEST SENSE command while performing a default
self-test, then the device server shall process the command.
If the SCSI target device detects no errors during a default self-test, then the device server shall complete the
command with GOOD status. If the SCSI target device detects an error during the test, then the device server
shall terminate the command with CHECK CONDITION status with the sense key set to HARDWARE
ERROR and the additional sense code set to indicate the cause of the error.
5.15.3 The short self-test and extended self-test
The short self-test and the extended self-test are optional. An application client requests that a SCSI target
device perform one of these self-tests by the SELFTEST bit to zero and specifying an appropriate value in the
SELF-TEST CODE field in the SEND DIAGNOSTIC command (see 6.42).
The criteria for the short self-test are that the test has one or more segments and completes in two minutes or
less. The criteria for the extended self-test are that the test is has one or more segments and that the
completion time required by the SCSI target device to complete the extended self-test is reported in the
EXTENDED SELF-TEST COMPLETION MINUTES field in the Extended INQUIRY Data VPD page (see 7.8.7), the
EXTENDED SELF-TEST COMPLETION TIME field in the Control mode page (see 7.5.8), or both.
The tests performed in the segments are vendor specific and may be the same for the short self-test and the
extended self-test.
The following are examples of segments:
a)
an electrical segment wherein the logical unit tests its own electronics. The tests in this segment are
vendor specific, but some examples of tests that may be included are:
A)
a buffer RAM test;
B)
a read/write circuitry test; or
C) a test of the read/write heads;
b)
a seek/servo segment wherein a device tests it capability to find and servo on data tracks; and
c)
a read/verify scan segment wherein a device performs read scanning of some or all of the medium
surface.
