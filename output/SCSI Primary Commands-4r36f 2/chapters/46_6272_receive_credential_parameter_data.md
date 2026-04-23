# 6.27.2 RECEIVE CREDENTIAL parameter data

The format of the MAM ATTRIBUTE field is defined in table 438 (see 7.4.1). If the ATTRIBUTE IDENTIFIER field in the
MAM ATTRIBUTE field is set to any value other than 0401h (i.e., MEDIUM SERIAL NUMBER), the command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
6.27.2 RECEIVE CREDENTIAL parameter data
6.27.2.1 RECEIVE CREDENTIAL parameter data encryption
The RECEIVE CREDENTIAL parameter data shall be one of the ESP-SCSI Data-In Buffer descriptors shown
in table 99 (see 5.14.7.5.1). The SA specified by the AC_SAI field and the DS_SAI field in the CDB shall be used
to construct the ESP-SCSI Data-In Buffer descriptor as described in 5.14.7.5.
Before processing the parameter data, the application client should validate and decrypt the ESP-SCSI
Data-In Buffer descriptor as described in 5.14.7.5. If any errors are detected by the validation and decryption
processing, the parameter data should be ignored.
6.27.2.2 RECEIVE CREDENTIAL decrypted parameter data
Before encryption and after decryption, the UNENCRYPTED BYTES field (see 5.14.7.3) that are used to compute
the ENCRYPTED OR AUTHENTICATED DATA field (see 5.14.7.5) contents shall contain a CbCS credential (see
table 263).
Table 263 — CbCS credential format
Bit
Byte
Reserved
CREDENTIAL FORMAT (1h)
Reserved
(MSB)
CREDENTIAL LENGTH (n-3)
(LSB)
(MSB)
CAPABILITY LENGTH (k-5)
(LSB)
CbCS capability descriptor (see 6.27.2.3)
•••
k
k+1
(MSB)
CAPABILITY KEY LENGTH (n-(k-4))
•••
k+4
(LSB)
k+5
CAPABILITY KEY

•••
n


The CREDENTIAL FORMAT field (see table 264) indicates the format of the credential.
The CREDENTIAL LENGTH field indicates the number of bytes that follow in the credential including the capability
length, the CbCS capability descriptor, the capability key length, and the capability key.
The CAPABILITY LENGTH field indicates the number of bytes that follow in the capability.
The contents of the CbCS capability descriptor are defined in 6.27.2.3.
The CAPABILITY KEY LENGTH field indicates the number of bytes that follow in the capability key.
The CAPABILITY KEY field contains an integrity check value that is computed and used as described in
5.14.6.8.12.
Table 264 — Credential format values
Value
Description
0h
Reserved
1h
The format defined by this standard
2h to Fh
Reserved


6.27.2.3 CbCS capability descriptor
6.27.2.3.1 Overview
A CbCS capability descriptor (see table 265) specifies the commands that are allowed by the CbCS extension
descriptor in which it appears.
The DESIGNATION TYPE field (see table 266) specifies the format of the Designation descriptor.
The KEY VERSION field specifies which working key (see 5.14.6.8.11), is being used to compute the capability
key (see 5.14.6.8.12) for this CbCS capability.
Table 265 — CbCS capability descriptor format
Bit
Byte
DESIGNATION TYPE
KEY VERSION
CBCS METHOD
(MSB)
CAPABILITY EXPIRATION TIME

•••
(LSB)
(MSB)
INTEGRITY CHECK VALUE ALGORITHM

•••
(LSB)
PERMISSIONS BIT MASK

•••
(MSB)
POLICY ACCESS TAG

•••
(LSB)
DESIGNATION DESCRIPTOR

•••
DISCRIMINATOR

•••

Table 266 — DESIGNATION TYPE field
Code
Description
DESIGNATION DESCRIPTOR
field format reference
0h
Reserved
1h
Logical unit designation descriptor
6.27.2.3.2
2h
MAM attribute designation descriptor
6.27.2.3.3
3h to Fh
Reserved


The CBCS METHOD field (see table 267) specifies the CbCS method used by this CbCS capability.
The CAPABILITY EXPIRATION TIME field specifies expiration time of this CbCS capability as the number of milli-
seconds that have elapsed since midnight, 1 January 1970 UT. If the CAPABILITY EXPIRATION TIME field is set to
zero, this CbCS capability does not have an expiration time.
If the CAPABILITY EXPIRATION TIME field is not set to zero, then:
a)
the clock maintained by the CbCS management device server (see 5.14.6.8.3) should be synchro-
nized with the clock maintained by the enforcement manager (see 5.14.6.8.7). The method for
synchronizing the clocks is outside the scope of this standard, however, the protocol should be imple-
mented in a secure manner (e.g., it should not be possible for an adversary to set the clock in the
SCSI device or in the secure CDB processor backwards to enable the reuse of expired CbCS creden-
tials). The value in the enforcement manager’s clock is available in the Current CbCS Parameters
CbCS page (see 7.7.4.3.5) to assist in this synchronization;
b)
the CbCS management device server should set the CAPABILITY EXPIRATION TIME field to a value that is
at least an order of magnitude larger than the allowed deviation between the clocks.
The INTEGRITY CHECK VALUE ALGORITHM field specifies the algorithm used to compute the capability key and
other integrity check values for this CbCS capability. The value in the INTEGRITY CHECK VALUE ALGORITHM field
is selected from the codes that the Unchangeable CbCS Parameters CbCS page (see 7.7.4.3.3) lists as
supported integrity check value algorithms.
The PERMISSIONS BIT MASK field (see table 268) specifies the permissions allowed by this CbCS capability.
More than one permissions bit may be set. The relationship between commands and bits in the PERMISSIONS
BIT MASK field is defined in for the commands defined by this standard and in the command standard that
defines commands for a specific device type.
A DATA READ bit set to zero indicates a command has no read permission for user data and protection infor-
mation. A DATA READ bit set to one indicates a command has permission to read user data and protection
information.
Table 267 — CBCS METHOD field
Code
CbCS method
Reference
00h
BASIC
5.14.6.8.8.2
01h
CAPKEY
5.14.6.8.8.3
02h to EFh
Reserved
F0h to FEh
Vendor specific
FFh
Reserved
Table 268 — PERMISSIONS BIT MASK field format
Bit
Byte
DATA READ
DATA WRITE
PARM READ
PARM WRITE
SEC MGMT
RESRV
MGMT
PHY ACC
Reserved
Restricted (see applicable command standard)


A DATA WRITE bit set to zero indicates a command has no write permission for user data and protection infor-
mation. A DATA WRITE bit set to one indicates a command has permission to write user data and protection
information.
A parameter data read (PARM READ) bit set to zero indicates a command has no parameter data read
permission. A PARM READ bit set to one indicates a command has permission to read parameter data.
A parameter data write (PARM WRITE) bit set to zero indicates a command has no parameter data write
permission. A PARM WRITE bit set to one indicates a command has permission to write parameter data.
A security management (SEC MGMT) bit set to zero indicates a command has no security management
permission. A SEC MGMT bit set to one indicates a command has security management permission.
A reservation (RESRV) bit set to zero indicates a command has no persistent reservation permission. A RESRV
bit set to one indicates a has permission to make or modify persistent reservations.
A management (MGMT) bit set to zero indicates a command has no storage management permission. A MGMT
bit set to one indicates a command has storage management permission. Storage management is outside the
scope of this standard.
A physical access (PHY ACC) bit set to zero indicates a command has no permission to affect physical access
to the logical unit or volume. A PHY ACC bit set to one indicates a command has permission to affect physical
access to the logical unit or volume (see SSC-3).
If the POLICY ACCESS TAG field is set to a value other than zero, the policy access tag attribute of the logical unit
(see 5.14.6.8.15) is compared to the POLICY ACCESS TAG field contents as part of validating the CbCS
capability (see 5.14.6.8.13.2). If the POLICY ACCESS TAG field is set to zero, then no comparison is made.
The DESIGNATION DESCRIPTOR field is used during the validation of the CbCS capability (see 5.14.6.8.13.2) to
ensure that the command is being addressed to the correct logical unit or volume (see SSC-3). The format of
the DESIGNATION DESCRIPTOR field is defined by the value in the DESIGNATION TYPE field as described in table
266.
If the CREDENTIAL REQUEST TYPE field in a RECEIVE CREDENTIAL command is set to 0001h (i.e., CbCS
logical unit), then the DESIGNATION DESCRIPTOR field shall contain a logical unit designation descriptor that
matches the DESIGNATION DESCRIPTOR field (see 6.27.1.2) in the CREDENTIAL REQUEST DESCRIPTOR field in the
CDB. If the CREDENTIAL REQUEST TYPE field in a RECEIVE CREDENTIAL command is set to 0002h (i.e., CbCS
logical unit and volume), then the DESIGNATION DESCRIPTOR field shall contain a MAM attribute designation
descriptor that matches the MAM ATTRIBUTE field (see 6.27.1.3) in the CREDENTIAL REQUEST DESCRIPTOR field in
the CDB.
The DISCRIMINATOR field provides uniqueness to the CbCS capability descriptor and may be used to limit the
delegation or prevent leakage of the CbCS capability to other application clients. The CbCS management
device server (see 5.14.6.8.3) shall not return the same CbCS capability descriptor to two secure CDB origi-
nators.
The enforcement manager (see 5.14.6.8.7) shall validate each CbCS capability descriptor it receives as
described in 5.14.6.8.13.2.


6.27.2.3.2 Logical unit designation descriptor format
If the DESIGNATION TYPE field is set to 0001h (i.e., logical unit designation descriptor), then the format of the
DESIGNATION DESCRIPTOR field is as shown in table 269.
The format of the DESIGNATION DESCRIPTOR field is defined in table 592 (see 7.8.6.1) with the following
additional requirements:
a)
the DESIGNATOR TYPE field shall contain 3h (i.e., NAA);
b)
the ASSOCIATION field shall 00b (i.e., logical unit); and
c)
the DESIGNATOR LENGTH field shall set to a value that is smaller than 17.
6.27.2.3.3 Volume designation descriptors
If the DESIGNATION TYPE field is set to 0002h (i.e., volume unit designation descriptor), then the format of the
DESIGNATION DESCRIPTOR field is as shown in table 270.
The format of the MAM ATTRIBUTE field is defined in table 438 (see 7.4.1) with the following additional require-
ments:
a)
the MAM ATTRIBUTE field shall contain 0401h (i.e., MEDIUM SERIAL NUMBER); and
b)
the ATTRIBUTE LENGTH field shall contain 0020h.
Table 269 — Logical unit designation descriptor format
Bit
Byte
DESIGNATION DESCRIPTOR

•••

Reserved

•••
Table 270 — Volume designation descriptor format
Bit
Byte

MAM ATTRIBUTE

•••
Reserved


6.28 RECEIVE DIAGNOSTIC RESULTS command
The RECEIVE DIAGNOSTIC RESULTS command (see table 271) requests that data be sent to the appli-
cation client Data-In Buffer. The data is either data based on the most recent SEND DIAGNOSTIC command
(see 6.42) or is a diagnostic page specified by the PAGE CODE field.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 271 for the RECEIVE
DIAGNOSTIC RESULTS command.
A page code valid (PCV) bit set to zero specifies that the device server return parameter data based on the
most recent SEND DIAGNOSTIC command (e.g., the diagnostic page with the same page code as that
specified in the most recent SEND DIAGNOSTIC command). The response to a RECEIVE DIAGNOSTIC
RESULTS command with the PCV bit set to zero is vendor specific if:
a)
the most recent SEND DIAGNOSTIC command was not a SEND DIAGNOSTIC command defining
parameter data to return;
b)
a RECEIVE DIAGNOSTIC RESULTS command with a PCV bit set to one has been processed since
the last SEND DIAGNOSTIC command was processed; or
c)
no SEND DIAGNOSTIC command defining parameter data to return has been processed since
power on, hard reset, or logical unit reset.
A page code valid (PCV) bit set to one specifies that the device server return the diagnostic page specified in
the PAGE CODE field. Page code values are defined in 7.2 or in another command standard.
NOTES
Logical units compliant with previous versions of this standard (e.g., SPC-2) may transfer more than one
diagnostic page in the parameter data if the PCV bit is set to zero and the previous SEND DIAGNOSTIC
command sent more than one diagnostic page in the parameter list.
To ensure that the diagnostic command information is not destroyed by a command sent from another
I_T nexus, the logical unit should be reserved.
Although diagnostic software is generally device-specific, this command and the SEND DIAGNOSTIC
command provide a means to isolate the operating system software from the device-specific diagnostic
software. The operating system may remain device-independent.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
See 7.2 for RECEIVE DIAGNOSTIC RESULTS diagnostic page format definitions.
Table 271 — RECEIVE DIAGNOSTIC RESULTS command
Bit
Byte
OPERATION CODE (1Ch)
Reserved
PCV
PAGE CODE
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL


6.29 REMOVE I_T NEXUS command
The REMOVE I_T NEXUS command (see table 272) requests that the device server establish an I_T nexus
loss (see SAM-5) for the logical unit containing the device server for each specified I_T nexus. This command
uses the MAINTENANCE OUT CDB format (see 4.2.2.3.4).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 272 for the REMOVE I_T
NEXUS command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 272 for the REMOVE I_T
NEXUS command.
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter data that shall be transferred
from the application client to the device server. A parameter list length value of zero specifies that no data
shall be transferred and no I_T nexuses shall be removed.
The CONTROL byte is defined in SAM-5.
If the parameter list length results in the truncation of the header or any I_T nexus descriptor, then the device
server:
a)
shall not remove any I_T nexuses; and
b)
shall terminate the command with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
Table 272 — REMOVE I_T NEXUS command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (0Ch)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


Table 273 shows the format of the REMOVE I_T NEXUS parameter list.
The I_T NEXUS DESCRIPTOR LIST LENGTH field specifies the length in bytes of the I_T nexus descriptor list.
The I_T nexus descriptor list contains one or more I_T nexus descriptors (see table 274). The I_T nexus
descriptors may appear in the I_T nexus descriptor list in any order. The device server shall process the I_T
nexus descriptors in order. The device server shall ignore any I_T nexus descriptor that describes an I_T
nexus not known to the logical unit.
The device server shall not remove any I_T nexuses and shall terminate the command with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST if any of the I_T nexus descriptors describe:
a)
the same I_T nexus as that through which the REMOVE I_T NEXUS command is received; or
b)
an I_T nexus that does not support the I_T NEXUS RESET task management function.
The RELATIVE TARGET PORT IDENTIFIER field specifies the relative target port identifier of the target port of the
I_T nexus to be reset.
Table 273 — REMOVE I_T NEXUS parameter list format
Bit
Byte
Reserved
(MSB)
I_T NEXUS DESCRIPTOR LIST LENGTH (n-3)
 (LSB)
I_T nexus descriptor list
I_T nexus descriptor [first]
•••
•••
I_T nexus descriptor [last]
•••
n
Table 274 — I_T nexus descriptor
Bit
Byte
(MSB)
RELATIVE TARGET PORT IDENTIFIER
 (LSB)
(MSB)
TRANSPORTID LENGTH (n-3)
 (LSB)
TRANSPORTID
•••
n


The TRANSPORTID LENGTH field specifies the length in bytes of the TRANSPORTID field.
The TRANSPORTID field specifies a TransportID (see 7.6.4) identifying the initiator port of the I_T nexus to be
reset.
6.30 REPORT ALIASES command
The REPORT ALIASES command (see table 275) requests that the device server return the alias list. This
command uses the MAINTENANCE IN CDB format (see 4.2.2.3.3). The alias list is managed using the
CHANGE ALIASES command (see 6.2). If the CHANGE ALIASES command is supported, the REPORT
ALIASES command shall also be supported.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 275 for the REPORT
ALIASES command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 275 for the REPORT
ALIASES command.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
Table 275 — REPORT ALIASES command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (0Bh)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL


The parameter data returned by a REPORT ALIASES command (see table 276) contains zero or more alias
entries.
The ADDITIONAL LENGTH field indicates the number of bytes in the remaining parameter data. The contents of
the ADDITIONAL LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The NUMBER OF ALIASES field indicates the number of alias entries in the alias list and shall not be changed if
the CDB contains an insufficient allocation length.
The parameter data shall include one alias entry for each alias in the alias list. The format of an alias entry is
described in 6.2.2.
Table 276 — REPORT ALIASES parameter data
Bit
Byte
(MSB)
ADDITIONAL LENGTH (n-3)

•••
 (LSB)
Reserved
Reserved
(MSB)
NUMBER OF ALIASES (x)

(LSB)
Alias entry (or entries)
Alias entry 0 (see 6.2.2)
•••
•••
Alias entry x (see 6.2.2)
•••
n


6.31 REPORT ALL ROD TOKENS command
The REPORT ALL ROD TOKENS command (see table 277) is a third-party copy command (see 5.17.3) that
returns a ROD management token (see 5.17.6.4) for each ROD token with fields defined in the ROD token
body that was created by and is known to the copy manager.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 277 for the REPORT ALL
ROD TOKENS command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 277 for the REPORT ALL
ROD TOKENS command.
The ALLOCATION LENGTH field are defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
In response to the REPORT ALL ROD TOKENS command, the copy manager shall return one or more ROD
management tokens. Each ROD management token shall represent a ROD token that:
a)
has fields defined in the ROD token body;
b)
was created by copy manager that is processing the REPORT ALL ROD TOKENS command; and
c)
is known to that copy manager.
Table 277 — REPORT ALL ROD TOKENS command
Bit
Byte
OPERATION CODE (84h)
Reserved
SERVICE ACTION (08h)
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
