# 7.7.1 Security protocol information description

7.7 Security protocol parameters
7.7.1 Security protocol information description
7.7.1.1 Overview
The purpose of security protocol information security protocol (i.e., the SECURITY PROTOCOL field set to 00h in
a SECURITY PROTOCOL IN command) is to transfer security protocol related information from the logical
unit. A SECURITY PROTOCOL IN command in which the SECURITY PROTOCOL field is set to 00h is not
associated with an previous SECURITY PROTOCOL OUT command and shall be processed without regard
for whether a SECURITY PROTOCOL OUT command has been processed.
If the SECURITY PROTOCOL IN command is supported, the SECURITY PROTOCOL field set to 00h shall be
supported as defined in this standard.
7.7.1.2 CDB description
If the SECURITY PROTOCOL field is set to 00h in a SECURITY PROTOCOL IN command, the SECURITY
PROTOCOL SPECIFIC field (see table 509) contains a single numeric value as defined in 3.6.
All other CDB fields for SECURITY PROTOCOL IN command shall meet the requirements stated in 6.40.
Each time a SECURITY PROTOCOL IN command with the SECURITY PROTOCOL field set to 00h is received,
the device server shall transfer the data defined in 7.7.1 starting with byte 0.
Table 509 — SECURITY PROTOCOL SPECIFIC field for SECURITY PROTOCOL IN protocol 00h
Code
Description
Support
Reference
0000h
Supported security protocol list
Mandatory
7.7.1.3
0001h
Certificate data
Mandatory
7.7.1.4
0002h
Security compliance information
Optional
7.7.1.5
all others
Reserved


7.7.1.3 Supported security protocols list description
If the SECURITY PROTOCOL field is set to 00h and the SECURITY PROTOCOL SPECIFIC field is set to 0000h in a
SECURITY PROTOCOL IN command, then the parameter data shall have the format shown in table 510.
The SUPPORTED SECURITY PROTOCOL LIST LENGTH field indicates the total length, in bytes, of the supported
security protocol list that follows.
Each SUPPORTED SECURITY PROTOCOL field in the supported security protocols list shall contain one of the
security protocol values supported by the logical unit. The values shall be listed in ascending order starting
with 00h.
The total data length shall conform to the ALLOCATION LENGTH field requirements (see 6.40). Pad bytes may be
appended to meet this length. Pad bytes shall have a value of 00h.
Table 510 — Supported security protocols SECURITY PROTOCOL IN parameter data
Bit
Byte
Reserved

•••
(MSB)
SUPPORTED SECURITY PROTOCOL LIST LENGTH
(m-7)
(LSB)
Supported security protocol list
SUPPORTED SECURITY PROTOCOL [first] (00h)
•••
m
SUPPORTED SECURITY PROTOCOL [last]
m+1
Pad bytes (optional)
•••
n


7.7.1.4 Certificate data description
7.7.1.4.1 Certificate overview
A certificate is either an X.509 Public Key Certificate (see 7.7.1.4.2) or an X.509 Attribute Certificate (see
7.7.1.4.3) depending on the capabilities of the logical unit.
If the SECURITY PROTOCOL field is set to 00h and the SECURITY PROTOCOL SPECIFIC field is set to 0001h in a
SECURITY PROTOCOL IN command, then the parameter data shall have the format shown in table 511.
The CERTIFICATE LENGTH field indicates the total length, in bytes, of the certificate or certificates that follow.
The length may include more than one certificates. If the device server doesn’t have a certificate to transfer,
the CERTIFICATE LENGTH field shall be set to 0000h.
The contents of the CERTIFICATE field are defined in 7.7.1.4.2 and 7.7.1.4.3.
The total data length shall conform to the ALLOCATION LENGTH field requirements (see 6.40). Pad bytes may be
appended to meet this length. Pad bytes shall have a value of 00h.
7.7.1.4.2 Public Key certificate description
RFC 5280 defines the certificate syntax for certificates consistent with X.509v3 Public Key Certificate Specifi-
cation. Any further restrictions beyond the requirements of RFC 5280 are yet to be defined by T10.
7.7.1.4.3 Attribute certificate description
RFC 3281 defines the certificate syntax for certificates consistent with X.509v2 Attribute Certificate Specifi-
cation. Any further restrictions beyond the requirements of RFC 3281 are yet to be defined by T10.
Table 511 — Certificate data SECURITY PROTOCOL IN parameter data
Bit
Byte
Reserved
(MSB)
CERTIFICATE LENGTH (m-3)
(LSB)
CERTIFICATE

•••
m
m+1
Pad bytes (optional)
•••
n


7.7.1.5 Security compliance information description
7.7.1.5.1 Security compliance information overview
The security compliance information parameter data contains information about security standards that apply
to this SCSI target device.
If the SECURITY PROTOCOL field is set to 00h and the SECURITY PROTOCOL SPECIFIC field is set to 0002h in a
SECURITY PROTOCOL IN command, then the parameter data shall have the format shown in table 512.
The SECURITY COMPLIANCE INFORMATION LENGTH field indicates the total length, in bytes, of the compliance
descriptors that follow.
Each compliance descriptor (see 7.7.1.5.2) contains information about a security standard that applies to this
SCSI target device. Compliance descriptors may be returned in any order.
The total data length shall conform to the ALLOCATION LENGTH field requirements (see 6.40). Pad bytes may be
appended to meet this length. Pad bytes shall have a value of 00h.
Table 512 — Security compliance information SECURITY PROTOCOL IN parameter data
Bit
Byte
(MSB)
SECURITY COMPLIANCE INFORMATION LENGTH (m-3)

•••
(LSB)
Compliance descriptors
Compliance descriptor [first]
•••
•••
Compliance descriptor [last]

•••
n
m+1
Pad bytes (optional)
•••
n


7.7.1.5.2 Compliance descriptor overview
The format of a compliance descriptor in the security compliance information SECURITY PROTOCOL IN
parameter data is shown in table 513.
The COMPLIANCE DESCRIPTOR TYPE field (see table 514) indicates the format of the descriptor specific infor-
mation. The security compliance information SECURITY PROTOCOL IN parameter data may contain more
than one compliance descriptor with the same value in the COMPLIANCE DESCRIPTOR TYPE field.
The COMPLIANCE DESCRIPTOR LENGTH field indicates the number of bytes that follow in the compliance
descriptor.
The contents of the descriptor specific information depend on the value in the COMPLIANCE DESCRIPTOR TYPE
field.
Table 513 — Compliance descriptor format
Bit
Byte
(MSB)
COMPLIANCE DESCRIPTOR TYPE
(LSB)
Reserved
(MSB)
COMPLIANCE DESCRIPTOR LENGTH (n-3)

•••
(LSB)
Descriptor specific information

•••
n
Table 514 — COMPLIANCE DESCRIPTOR TYPE field
Code
Description
Related
standards
Reference
0001h
Security requirements for cryptographic modules
FIPS 140-2
FIPS 140-3
7.7.1.5.3
all others
Reserved


7.7.1.5.3 FIPS 140 compliance descriptor
The FIPS 140 compliance descriptor (see table 515) contains information that may be used to locate infor-
mation about a FIPS 140 certificate associated with the SCSI target device. The SCSI target device may or
may not be operating in the mode specified by that certificate.
The COMPLIANCE DESCRIPTOR TYPE field and COMPLIANCE DESCRIPTOR LENGTH field are defined in 7.7.1.5.2 and
shall be set as shown in table 515 for the FIPS 140 compliance descriptor.
The REVISION field (see table 516) is an ASCII data field (see 4.3.1) that indicates the FIPS 140 revision that
applies to the SCSI target device.
The OVERALL SECURITY LEVEL field is an ASCII data field (see 4.3.1) that indicates the FIPS 140 overall
security level that is reported by NIST.
Table 515 — FIPS 140 compliance descriptor
Bit
Byte
(MSB)
COMPLIANCE DESCRIPTOR TYPE (0001h)
(LSB)
Reserved
(MSB)
COMPLIANCE DESCRIPTOR LENGTH (0000 0208h)

•••
(LSB)
REVISION
OVERALL SECURITY LEVEL
Reserved

•••
(MSB)
HARDWARE VERSION
•••
(LSB)
(MSB)
VERSION
•••
(LSB)
(MSB)
MODULE NAME
•••
(LSB)
Table 516 — REVISION field
Code
Related standard
32h
FIPS 140-2
33h
FIPS 140-3
all others
