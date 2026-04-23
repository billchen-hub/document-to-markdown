# 6.32.1 REPORT IDENTIFYING INFORMATION command overview

The format of the REPORT ALL ROD TOKENS parameter data is shown in table 278.
The AVAILABLE DATA field shall contain the number of bytes that follow in the parameter data. The contents of
the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
Each ROD management token is a 96-byte token that contains the fields described in 5.17.6.4, and repre-
sents a ROD token that meets the criteria described in this subclause.
6.32 REPORT IDENTIFYING INFORMATION command
6.32.1 REPORT IDENTIFYING INFORMATION command overview
The REPORT IDENTIFYING INFORMATION command (see table 279) requests that the device server send
identifying information (see 5.6) to the application client. This command uses the MAINTENANCE IN CDB
format (see 4.2.2.3.3). The REPORT IDENTIFYING INFORMATION command is an extension to the
REPORT PERIPHERAL DEVICE/COMPONENT DEVICE IDENTIFIER service action of the MAINTENANCE
IN command defined in SCC-2.
The device server shall return the same identifying information regardless of the I_T nexus being used to
retrieve the identifying information.
Table 278 — Parameter data for the REPORT ALL ROD TOKENS command
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)

•••

(LSB)
Reserved

•••
ROD management token list
ROD management token [first]

•••
•••
n-95
ROD management token [last]
•••
n


Processing a REPORT IDENTIFYING INFORMATION command may require the enabling of a nonvolatile
memory within the logical unit. If the nonvolatile memory is not ready, the command shall be terminated with
CHECK CONDITION status, and not wait for the nonvolatile memory to become ready. The sense key shall
be set to NOT READY and the additional sense code shall be set as described in table 334 (see 6.47). This
information should allow the application client to determine the action required to cause the device server to
become ready.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 279 for the REPORT
IDENTIFYING INFORMATION command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 279 for the REPORT IDENTI-
FYING INFORMATION command.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The INFORMATION TYPE field (see table 280) specifies the type of information to be reported. If the specified
information type is not implemented by the device server, then the command shall be terminated with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-5.
Table 279 — REPORT IDENTIFYING INFORMATION command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (05h)
Reserved
Restricted (see SCC-2)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
INFORMATION TYPE
Reserved
CONTROL
Table 280 — INFORMATION TYPE field
Code
Description
Reference
0000000b
Peripheral device identifying information (see 5.6).
6.32.2
0000010b
Peripheral device text identifying information (see 5.6).
6.32.2
1111111b
Identifying information supported – The parameter data contains a list of
supported identifying information types and the maximum length of each.
6.32.3
xxxxxx1b
Restricted
SCC-2
All other
Reserved
