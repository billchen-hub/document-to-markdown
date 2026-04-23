# 5.9 GET STREAM STATUS command

The PHYSICAL ELEMENT HEALTH field indicates the health of the physical element associated with this physical
element status descriptor, as described in table 62.
The ASSOCIATED CAPACITY field indicates the the number of logical blocks by which the capacity of the device
is reduced if the physical element associated with this physical element status descriptor becomes
depopulated. A value of FFFF_FFFF_FFFF_FFFFh indicates that the number of logical blocks by which the
capacity is reduced is not specified.
5.9 GET STREAM STATUS command
5.9.1 GET STREAM STATUS command overview
The GET STREAM STATUS command (see table 63) requests that the device server transfer parameter data
describing the status of streams (see 4.32) for the logical unit to the Data-In Buffer.
The device server may or may not process this command as an uninterrupted sequence of actions (e.g., if
concurrent operations are occurring that affect the status of streams, then the returned parameter data may
be inconsistent or out of date).
Table 62 — PHYSICAL ELEMENT HEALTH field
Code
Description
00h
Not reported.
01h to 63h a
The physical element health is within manufacturer’s specification limits.
64h
The physical element health is at manufacturer’s specification limit.
65h to CFh a
The physical element health is outside manufacturer’s specification limit.
D0h to FCh
Reserved
FDh
All operations associated with storage element depopulation have completed
and one or more completed with error.
FEh
An operation associated with storage element depopulation is in progress.
FFh
All operations associated with storage element depopulation have completed
without error.
a The device server may implement a subset of these values.


This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 63 for the GET STREAM STATUS command.
The STARTING STREAM IDENTIFIER field specifies the stream identifier of the first stream addressed by this
command (see 5.9.2.3). If the specified starting stream identifier exceeds the value indicated by the MAXIMUM
NUMBER OF STREAMS field of the Block Limits VPD page (see 6.6.4), then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to ILLEGAL FIELD IN CDB.
The ALLOCATION LENGTH field is defined in SPC-6. If, in response to a single GET STREAM STATUS
command, the device server does not send sufficient data to the Data-In Buffer to satisfy the requirement of
the application client, then the application client may send additional GET STREAM STATUS commands with
different starting stream identifier values to retrieve additional information.
The CONTROL byte is defined in SAM-6.
Table 63 — GET STREAM STATUS command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (16h)
Reserved
STARTING STREAM IDENTIFIER
Reserved
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB
Reserved
CONTROL


5.9.2 GET STREAM STATUS parameter data
5.9.2.1 GET STREAM STATUS parameter data overview
The GET STREAM STATUS parameter data (see table 64) contains an eight-byte header followed by zero or
more stream status descriptors.
The PARAMETER DATA LENGTH field shall contain the length in bytes of the stream list. The stream list length is
the number of open streams in the logical unit multiplied by eight. The contents of the STREAM LIST LENGTH
field are not altered based on the allocation length.
As a result of processing considerations not defined by this standard, two GET STREAM STATUS commands
with identical values in all CDB fields may result in two different values in the PARAMETER DATA LENGTH field.
The relationship between the PARAMETER DATA LENGTH field and the ALLOCATION LENGTH field in the CDB is
defined in SPC-6.
The NUMBER OF OPEN STREAMS field indicates the number of streams that are currently open in the logical unit.
Table 64 — GET STREAM STATUS parameter data
Bit
Byte
PARAMETER DATA LENGTH (n-7)
•••
Reserved
(MSB)
NUMBER OF OPEN STREAMS
(LSB)
Stream status descriptors
Stream status descriptor [first] (see 5.9.2.2)
•••
•••
n-8
Stream status descriptor [last] (see 5.9.2.2)
•••
n
