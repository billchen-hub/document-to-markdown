# 6.27.1 RECEIVE CREDENTIAL command description

6.27 RECEIVE CREDENTIAL command
6.27.1 RECEIVE CREDENTIAL command description
6.27.1.1 Overview
The RECEIVE CREDENTIAL command (see table 258) allows a secure CDB originator (see 5.14.6.2) to
receive a credential from a security manager device server (e.g., a CbCS management device server (see
5.14.6.8.3)) for use in a CDB (e.g., use in the CbCS extension descriptor (see 5.14.6.8.16)).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 258 for the RECEIVE
CREDENTIAL command.
The ADDITIONAL CDB LENGTH field is defined in 4.2.3.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 258 for the RECEIVE
CREDENTIAL command.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The AC_SAI field is set to the value of the AC_SAI SA parameter (see 5.14.2.2) for the SA to be used to
encrypt the parameter data as described in 6.27.2.1.
Table 258 — RECEIVE CREDENTIAL command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved

•••
ADDITIONAL CDB LENGTH (n-7)
(MSB)
SERVICE ACTION (1800h)
(LSB)
(MSB)
ALLOCATION LENGTH
(LSB)
(MSB)
AC_SAI

•••
(LSB)

ENCRYPTED REQUEST DESCRIPTOR

•••
n


The ENCRYPTED REQUEST DESCRIPTOR field shall contain an ESP-SCSI CDB descriptor (see 5.14.7.4). Before
encryption and after decryption, the UNENCRYPTED BYTES field (see 5.14.7.3) that are used to compute the
ENCRYPTED OR AUTHENTICATED DATA field (see 5.14.7.4) contents shall have the format shown in table 259.
The CREDENTIAL REQUEST TYPE field (see table 260) specifies type of credential being requested and the
format of the CREDENTIAL REQUEST DESCRIPTOR field.
The CREDENTIAL REQUEST DESCRIPTOR field specifies the information needed to request the credential as
described in table 260.
The CONTROL byte is defined in SAM-5.
If return of the requested credential is not permitted, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
ACCESS DENIED - NO ACCESS RIGHTS.
The DS_SAI field in the ENCRYPTED REQUEST DESCRIPTOR field is set to the value of the DS_SAI SA parameter
(see 5.14.2.2) for the SA to be used to encrypt the unencrypted bytes and the parameter data as described.
If the device server is not maintaining an SA with an AC_SAI SA parameter that matches the AC_SAI field
contents and a DS_SAI SA parameter that matches the DS_SAI field contents, then the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
If the device server is maintaining the SA specified by the AC_SAI field and the DS_SAI field, then the SA shall
be verified for use by this RECEIVE CREDENTIAL command as follows:
a)
the USAGE_TYPE SA parameter (see 5.14.2.2) shall be verified to be equal to 82h (i.e., CbCS
authentication and credential encryption; and
b)
the USAGE_DATA SA parameter (see 5.14.2.2) shall be verified not to contain an ALGORITHM
IDENTIFIER field (see 7.7.3.6) that is set to ENCR_NULL based on the contents the IKEv2-SCSI SAUT
Cryptographic Algorithm payload (see 7.7.3.5.14) for the ENCR algorithm type (see 7.7.3.6.2) during
creation of the SA (see 5.14.2.3).
Table 259 — RECEIVE CREDENTIAL command unencrypted bytes format
Bit
Byte
(MSB)
CREDENTIAL REQUEST TYPE
(LSB)
CREDENTIAL REQUEST DESCRIPTOR

•••
n
Table 260 — CREDENTIAL REQUEST TYPE field
Code
Description
Reference
0001h
CbCS logical unit
6.27.1.2
0002h
CbCS logical unit and volume
6.27.1.3
all other codes
Reserved


If any of these SA verifications fails, the command shall be terminated with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
6.27.1.2 CbCS logical unit credential request descriptor
If the credential request type field is set to 0001h (i.e., CbCS logical unit), then the format of the CREDENTIAL
REQUEST DESCRIPTOR field is as shown in table 261.
The format of the DESIGNATION DESCRIPTOR field is defined in table 592 (see 7.8.6.1). The command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB if any of the fields in the DESIGNATION DESCRIPTOR field are set as
follows:
a)
the DESIGNATOR TYPE field is set to any value other than 3h (i.e., NAA);
b)
the ASSOCIATION field is set to any value other than 00b (i.e., logical unit) or 10b (i.e., SCSI target
device); or
c)
the DESIGNATOR LENGTH field is set to a value that is larger than 16.
6.27.1.3 CbCS logical unit and volume credential request descriptor
If the credential request type field is set to 0002h (i.e., CbCS logical unit and volume), then the format of the
CREDENTIAL REQUEST DESCRIPTOR field is as shown in table 262.
The format of the DESIGNATION DESCRIPTOR field is defined in table 592 (see 7.8.6.1). The command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB if any of the fields in the DESIGNATION DESCRIPTOR field are set as
follows:
a)
the DESIGNATOR TYPE field is set to any value other than 3h (i.e., NAA);
b)
the ASSOCIATION field is set to any value other than 00b (i.e., logical unit) or 10b (i.e., SCSI target
device); or
c)
the DESIGNATOR LENGTH field is set to a value that is larger than 16.
Table 261 — CbCS logical unit credential request descriptor format
Bit
Byte
DESIGNATION DESCRIPTOR

•••
Table 262 — CbCS logical unit and volume credential request descriptor format
Bit
Byte
DESIGNATION DESCRIPTOR

•••

MAM ATTRIBUTE

•••
