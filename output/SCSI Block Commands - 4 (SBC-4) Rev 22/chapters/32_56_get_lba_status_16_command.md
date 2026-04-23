# 5.6 GET LBA STATUS (16) command

5.6 GET LBA STATUS (16) command
5.6.1 GET LBA STATUS (16) command overview
The GET LBA STATUS (16) command (see table 48) requests that the device server transfer parameter data
describing the logical block provisioning status (see 4.7) and additional status for the specified LBA and zero
or more subsequent LBAs to the Data-In Buffer.
The device server may or may not process this command as an uninterrupted sequence of actions (e.g., if
concurrent operations are occurring that affect the logical block provisioning status, then the returned
parameter data may be inconsistent or out of date).
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 48 for the GET LBA
STATUS (16) command.
The SERVICE ACTION field is defined in SPC-6 and shall be set to the value shown in table 48 for the GET LBA
STATUS (16) command.
The STARTING LOGICAL BLOCK ADDRESS field specifies the LBA of the first logical block addressed by this
command. If the specified starting LBA exceeds the capacity of the medium (see 4.5), then the device server
shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to LOGICAL BLOCK ADDRESS OUT OF RANGE.
The ALLOCATION LENGTH field is defined in SPC-6. In response to a GET LBA STATUS (16) command, the
device server may send less data to the Data-In Buffer than is specified by the allocation length. If, in
response to a single GET LBA STATUS (16) command, the device server does not send sufficient data to the
Data-In Buffer to satisfy the requirement of the application client, then, to retrieve additional information, the
application client may send additional GET LBA STATUS (16) commands with different starting LBA values.
Table 48 — GET LBA STATUS (16) command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (12h)
(MSB)
STARTING LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
ALLOCATION LENGTH
•••
(LSB)
REPORT TYPE
CONTROL


The REPORT TYPE field specifies the type of LBA status descriptors to return as shown in table 49.
The CONTROL byte is defined in SAM-6.
5.6.2 GET LBA STATUS parameter data
5.6.2.1 GET LBA STATUS parameter data overview
The GET LBA STATUS parameter data (see table 50) contains an eight-byte header followed by one or more
LBA status descriptors.
The PARAMETER DATA LENGTH field indicates the number of bytes of parameter data that follow. The value in
the PARAMETER DATA LENGTH field shall be:
a)
set to 4, if there are no status descriptors to report;
Table 49 — REPORT TYPE field
Code
Description
00h
Return descriptors for all LBAs
01h
Return descriptors for all LBAs using only non-zero provisioning status
(see table 53)
02h
Return descriptors for all LBAs that are mapped (see 4.7.4.5)
03h
Return descriptors for all LBAs that are deallocated (see 4.7.4.6)
04h
Return descriptors for all LBAs that are anchored (see 4.7.4.7)
10h
Return descriptors for LBAs that may return an unrecovered error
All others
Reserved
Table 50 — GET LBA STATUS parameter data
Bit
Byte
(MSB)
PARAMETER DATA LENGTH (n - 3)
•••
(LSB)
Reserved
•••
Reserved
COMPLETION CONDITION
RTP
LBA status descriptors
LBA status descriptor [first] (see 5.6.2.2)
•••
•••
n - 15
LBA status descriptor [last] (see 5.6.2.2) (if any)
•••
n


b)
at least 20 (i.e., the available parameter data shall contain at least one LBA status descriptor), if there
are any status descriptors to report; and
c)
four added to a multiple of 16 (i.e., the available parameter data shall end on a boundary between
LBA status descriptors).
As a result of processing considerations not defined by this standard, two GET LBA STATUS commands with
identical values in all CDB fields may result in two different values in the PARAMETER DATA LENGTH field.
The relationship between the PARAMETER DATA LENGTH field and the ALLOCATION LENGTH field in the CDB is
defined in SPC-6.
The COMPLETION CONDITION field indicates the condition that caused completion of the GET LBA STATUS
command. The COMPLETION CONDITION field is described in table 51.
If the command completes by reaching the capacity of the medium and any other condition at the same time,
then the COMPLETION CONDITION field shall be set to 011b.
The report type processed (RTP) bit indicates whether the value in the REPORT TYPE field was processed. If the
RTP bit is set to zero, then the REPORT TYPE field was not processed (i.e., the GET LBA STATUS parameter
data is returned as if the REPORT TYPE field was set to 00h). If the RTP bit is set to one, then the REPORT TYPE
field was processed. If a device server supports the REPORT TYPE field set to a non-zero value, then the RTP bit
shall be set to one.
Table 51 — COMPLETION CONDITION field
Code
Description
000b
No indication of the completion condition.
001b
The command completed as a result of meeting the allocation length.
010b a
The command completed as a result of completing the scan length.
011b
The command completed as a result of reaching the capacity of the medium
(see 4.5).
all others
Reserved
a This only applies to the GET LBA STATUS (32) command


5.6.2.2 LBA status descriptor
The LBA status descriptor (see table 52) contains LBA status information for one or more LBAs.
The LBA STATUS LOGICAL BLOCK ADDRESS field contains the first LBA of the LBA extent for which this descriptor
reports LBA status.
The NUMBER OF LOGICAL BLOCKS field contains the number of logical blocks in that LBA extent. The device
server should return the largest possible value in the NUMBER OF LOGICAL BLOCKS field.
The PROVISIONING STATUS field is shown in table 53.
If the logical unit is fully provisioned (see 4.7.2), then the PROVISIONING STATUS field for all LBAs shall be set to:
a)
0h (i.e., mapped or unknown), if the RTP bit is set to zero;
b)
0h (i.e., mapped or unknown), if the REPORT TYPE field is set to 00h in the CDB and the RTP bit is set to
one; or
c)
3h (i.e., mapped), if the REPORT TYPE field is not set to 00h in the CDB and the RTP bit is set to one.
Table 52 — LBA status descriptor format
Bit
Byte
(MSB)
LBA STATUS LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
Reserved
PROVISIONING STATUS
ADDITIONAL STATUS
Reserved
Table 53 — PROVISIONING STATUS field
Code
Description
Allowed for report
types
0h
Each LBA in the LBA extent is mapped (see 4.7.4.5) or has an
unknown state.
00h
1h
Each LBA in the LBA extent is deallocated (see 4.7.4.6).
00h, 01h, 03h, 10h
2h
Each LBA in the LBA extent is anchored (see 4.7.4.7).
00h, 01h, 04h, 10h
3h
Each LBA in the LBA extent is mapped.
01h, 02h, 10h
4h
Each LBA in the LBA extent has an unknown provisioning
status.
01h, 10h
All others
Reserved
