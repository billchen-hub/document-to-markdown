# 5.7 GET LBA STATUS (32) command

The ADDITIONAL STATUS field shall be set to 00h if the REPORT TYPE field is set to 00h in the CDB and shall be
as shown in table 54 for all other values of report type.
5.6.2.3 LBA status descriptor relationships
The LBA STATUS LOGICAL BLOCK ADDRESS field in the first LBA status descriptor returned in the GET LBA
STATUS parameter data shall contain the lowest numbered LBA that is greater than or equal to the starting
logical block address specified in the CDB that meets the requirements for the specified report type. For
subsequent LBA status descriptors, the contents of the LBA STATUS LOGICAL BLOCK ADDRESS field shall contain:
a)
for a non-zero report type, the value of the lowest numbered LBA meeting the requirements for the
specified report type that is greater than or equal to the sum of the values in:
A) the LBA STATUS LOGICAL BLOCK ADDRESS field in the previous LBA status descriptor; and
B) the NUMBER OF LOGICAL BLOCKS field in the previous LBA status descriptor;
or
b)
for report type 0h, the sum of the values in:
A) the LBA STATUS LOGICAL BLOCK ADDRESS field in the previous LBA status descriptor; and
B) the NUMBER OF LOGICAL BLOCKS field in the previous LBA status descriptor.
Adjacent LBA status descriptors may have the same values for the PROVISIONING STATUS field.
5.7 GET LBA STATUS (32) command
5.7.1 GET LBA STATUS (32) command overview
The GET LBA STATUS (32) command (see table 55) requests that the device server transfer parameter data
describing the logical block provisioning status (see 4.7) and additional status for the specified LBA and zero
or more subsequent LBAs to the Data-In Buffer.
The device server may or may not process this command as an uninterrupted sequence of actions (e.g., if
concurrent operations are occurring that affect the logical block provisioning status, then the returned
parameter data may be inconsistent or out of date).
Table 54 — ADDITIONAL STATUS field
Code
Description
00h
No additional status to report.
01h
The device server has detected that each LBA in the LBA extent may return an
unrecovered error.
All others
Reserved


This command uses the variable length CDB format (see clause A.1).
The OPERATION CODE field, ADDITIONAL CDB LENGTH field, and SERVICE ACTION field are defined in SPC-6 and
shall be set to the values shown in table 55 for the GET LBA STATUS (32) command.
The CONTROL byte is defined in SAM-6.
The SCAN LENGTH field specifies the maximum number of contiguous logical blocks to be scanned for logical
blocks that meet the specified report type. A value of 0000_0000h in the SCAN LENGTH field specifies that there
is no limit on the number of logical blocks to be scanned (e.g., scan to the end of the media, or scan until the
allocation length is met).
The ELEMENT IDENTIFIER field specifies the element identifier of the physical element (see 4.36.1) for which
LBAs shall be reported based on the value in the REPORT TYPE field. If the ELEMENT IDENTIFIER field is set to
0000_0000h, then LBAs for all physical elements shall be reported based on the value in the REPORT TYPE
field.
See the GET LBA STATUS (16) command for the description of the STARTING LOGICAL BLOCK ADDESSS field,
the ALLOCATION LENGTH field, the REPORT TYPE field, and the returned parameter data (see 5.6.2).
Table 55 — GET LBA STATUS (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
•••
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (0012h)
(LSB)
REPORT TYPE
Reserved
(MSB)
STARTING LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
SCAN LENGTH
•••
(LSB)
ELEMENT IDENTIFIER
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB)
