# 5.14.3 Key derivation functions

5.14.2.3 Creating an SA
The SECURITY PROTOCOL IN command (see 6.40) and SECURITY PROTOCOL OUT command (see
6.41) security protocols shown in table 75 are used to create SAs. The process of creating an SA establishes
the SA parameter (see 5.14.2.2) values as follows:
a)
initial values for:
A)
AC_SQN set as described in 5.14.4.9; and
B)
DS_SQN set as described in 5.14.4.9;
b)
unchanging values for the lifetime of the SA:
A)
AC_SAI;
B)
DS_SAI;
C) TIMEOUT;
D) KDF_ID;
E)
KEYMAT;
F)
USAGE_TYPE;
G) USAGE_DATA; and
H) MGMT_DATA;
and
c)
values that are zero (see 5.14.4.9) upon completion of SA creation:
A)
KEY_SEED;
B)
AC_NONCE; and
C) DS_NONCE.
5.14.3 Key derivation functions
5.14.3.1 KDFs overview
A KDF produces KEYMAT from in input KEY_SEED and STRING as follows:
KEYMAT = KDF( KEY_SEED, STRING )
Where:
KEY_SEED is a SA Parameter (see 5.14.2.2); and
STRING is a specified sequence of bytes.
Table 75 — Security protocols that create SAs
Security
Protocol
Code
Description
References
40h
SA creation capabilities
7.7.2
41h
IKEv2-SCSI
5.14.4 and 7.7.3


Table 76 summarizes the KDFs defined by this standard.
5.14.3.2 IKEv2-based iterative KDF
To produce a sufficient number of bits in KEYMAT, the IKEv2-based (see RFC 4306) iterative KDF applies
IFUNC, a function that has the same inputs as a KDF (see 5.14.3.1), as follows:
1)
initialize PREV_OUTPUT to a null string (i.e., a string that contains no bits);
2)
repeat the following function for values of N that increment from one by one to a maximum of 255 or
until the total number of bits returned by all invocations of IFUNC equals or exceeds the number of
KEYMAT bits that are to be produced, whichever occurs first:
TN = IFUNC( KEY_SEED, ( PREV_OUTPUT || STRING || a byte containing the value N ) )
and
3)
concatenate the TN values (e.g., T1 or T1 || T2 || T3) and return as many of the resulting bits as
specified by the number of KEYMAT bits that are to be produced input parameter, starting with the first
bit in T1.
Protocols that call the IFUNC function to generate KEYMAT should ensure that the number of KEYMAT bits
requested does not cause N to exceed 255. If N reaches 256, then:
1)
the requested number of KEYMAT bits is not returned by IFUNC; and
2)
the request to produce KEYMAT shall be terminated with an error.
5.14.3.3 HMAC-based KDFs
If the KDF_ID is one of those shown in table 77, the KDF is a combination of the:
a)
HMAC function defined in FIPS 198-1 (see 2.7);
b)
secure hash function shown in table 77 for the specified KDF_ID value; and
c)
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
Table 76 — KDFs summary
Security
Algorithm
Code
(see table 104)
Description
Reference
8002 0002h
IKEv2-based iterative HMAC KDF based on SHA-1
5.14.3.3
8002 0005h
IKEv2-based iterative HMAC KDF based on SHA-256
5.14.3.3
8002 0006h
IKEv2-based iterative HMAC KDF based on SHA-384
5.14.3.3
8002 0007h
IKEv2-based iterative HMAC KDF based on SHA-512
5.14.3.3
8002 0004h
IKEv2-based iterative KDF based on AES-128 in XCBC mode
5.14.3.4


f)
KEYMAT size, in bits.
The USAGE_TYPE SA parameter and USAGE_DATA SA parameter (see 5.14.2.2) specify the KEYMAT size
as part of the security protocol that performs SA creation (see 5.14.2.3).
The IKEv2-based iterative KDF technique (see 5.14.3.2) is applied with the following inputs:
a)
IFUNC (see 5.14.3.2) is the HMAC function defined in FIPS 198-1 with the translation of inputs names
shown in table 77;
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
Details of the hash functions that act as inputs to the FIPS 198-1 HMAC function are shown in table 78.
Table 77 — HMAC-based KDFs
FIPS 198-1 inputs
selected by KDF_ID
KDF_ID (see table 76)
8002 0002h
8002 0005h
8002 0006h
8002 0007h
H (i.e., hash function)
SHA-1
(see table 78)
SHA-256
(see table 78)
SHA-384
(see table 78)
SHA-512
(see table 78)
B (i.e., hash input block size) a
L (i.e., hash output block size)  a, b
K (i.e., key)
KEY_SEED SA parameter
text
STRING as defined in this subclause and used in 5.14.3.2
a In accordance with FIPS 198-1, all sizes are shown in bytes.
b The HMAC-based KDFs defined by this standard do not truncate (i.e., FIPS 198-1 Lambda equals
the L shown in this table).
Table 78 — Hash functions used by HMAC based on KDF_ID
KDF_ID
(see table 76)
Function
Description
8002 0002h
SHA-1
HMAC input H is the SHA-1 secure hash function defined in
FIPS 180-4 (see 2.7).
8002 0005h
SHA-256
HMAC input H is the SHA-256 secure hash function defined in
FIPS 180-4.
8002 0006h
SHA-384
HMAC input H is the SHA-384 secure hash function defined in
FIPS 180-4.
8002 0007h
SHA-512
HMAC input H is the SHA-512 secure hash function defined in
FIPS 180-4.
