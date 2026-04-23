# 6.32.3 IDENTIFYING INFORMATION SUPPORTED parameter data

6.32.2 IDENTIFYING INFORMATION parameter data
The REPORT IDENTIFYING INFORMATION parameter data format used if the INFORMATION TYPE field is set
to 0000000b or 0000010b is shown in table 281.
The INFORMATION LENGTH field indicates the length in bytes of the INFORMATION field. The contents of the
INFORMATION LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The INFORMATION field contains the identifying information that has the specified information type (see 6.32.1).
6.32.3 IDENTIFYING INFORMATION SUPPORTED parameter data
The REPORT IDENTIFYING INFORMATION parameter data format used if the INFORMATION TYPE field is set
to 1111111b is shown in table 282.
Table 281 — REPORT IDENTIFYING INFORMATION parameter data
Bit
Byte
Reserved
(MSB)
INFORMATION LENGTH (n-3)
(LSB)
INFORMATION
•••
n
Table 282 — REPORT IDENTIFYING INFORMATION SUPPORTED parameter data
Bit
Byte
Reserved
(MSB)
IDENTIFYING INFORMATION LENGTH (n-3)
(LSB)
Identifying information descriptor list
Identifying information descriptor [first]
(see table 283)
•••
•••
n-3
Identifying information descriptor [last]
(see table 283)
•••
n


The IDENTIFYING INFORMATION LENGTH field indicates the length in bytes of the identifying information descriptor
list. The contents of the IDENTIFYING INFORMATION LENGTH field are not altered based on the allocation length
(see 4.2.5.6).
The identifying information descriptor list contains an identifying information descriptor (see table 283) for
each identifying information type supported by the device server. The identifying information descriptors shall
be sorted in increasing order by information type.
The INFORMATION TYPE field indicates the information type (see 5.6).
The MAXIMUM INFORMATION LENGTH field indicates the maximum number of bytes supported for identifying
information that has the indicated information type (see 5.6).
Table 283 — Identifying information descriptor
Bit
Byte
INFORMATION TYPE
Reserved
Reserved
(MSB)
MAXIMUM INFORMATION LENGTH
(LSB)


6.33 REPORT LUNS command
The REPORT LUNS command (see table 284) requests that the peripheral device logical unit inventory
accessible to the I_T nexus be sent to the application client. The logical unit inventory is a list that shall include
the logical unit numbers of all logical units having a PERIPHERAL QUALIFIER value of 000b (see 6.6.2). Logical
unit numbers for logical units with PERIPHERAL QUALIFIER values other than 000b and 011b may be included in
the logical unit inventory. Logical unit numbers for logical units with a PERIPHERAL QUALIFIER value of 011b shall
not be included in the logical unit inventory.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 284 for the REPORT LUNS
command.
The SELECT REPORT field (see table 285) specifies the types of logical unit addresses that shall be reported.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
Table 284 — REPORT LUNS command
Bit
Byte
OPERATION CODE (A0h)
Reserved
SELECT REPORT
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
Table 285 — SELECT REPORT field
Code
Description
00h
The list shall contain the logical units accessible to the I_T nexus with the following
addressing methods (see SAM-5):
a)
logical unit addressing method,
b)
peripheral device addressing method;
c)
flat space addressing method;
d)
extended logical unit addressing method; and
e)
long extended logical unit addressing method.
If there are no logical units, the LUN LIST LENGTH field shall be zero.
01h
The list shall contain only well known logical units, if any. If there are no well known
logical units, the LUN LIST LENGTH field shall be zero.
02h
The list shall contain all logical units accessible to the I_T nexus.
F8h to FFh
Vendor specific
all others
Reserved


The CONTROL byte is defined in SAM-5.
The REPORT LUNS command shall return CHECK CONDITION status only if the device server is unable to
return the requested report of the logical unit inventory.
If a REPORT LUNS command is received from an I_T nexus with a pending unit attention condition (i.e.,
before the device server reports CHECK CONDITION status), the device server shall perform the REPORT
LUNS command (see SAM-5).
The REPORT LUNS parameter data should be returned even though the device server is not ready for other
commands. The report of the logical unit inventory should be available without incurring any media access
delays. If the device server is not ready with the logical unit inventory or if the inventory list is null for the
requesting I_T nexus and the SELECT REPORT field set to 02h, then the device server shall provide a default
logical unit inventory that contains at least LUN 0 or the REPORT LUNS well known logical unit (see 8.2). A
non-empty peripheral device logical unit inventory that does not contain either LUN 0 or the REPORT LUNS
well known logical unit is valid.
If a REPORT LUNS command is received for a logical unit that the SCSI target device does not support and
the device server is not capable of returning the logical unit inventory, then the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to LOGICAL UNIT NOT SUPPORTED.
The device server shall report those devices in the logical unit inventory using the format shown in table 286.
The LUN LIST LENGTH field shall contain the length in bytes of the LUN list that is available to be transferred.
The LUN list length is the number of logical unit numbers in the logical unit inventory multiplied by eight. The
contents of the LUN LIST LENGTH field are not altered based on the allocation length (see 4.2.5.6).
Table 286 — REPORT LUNS parameter data format
Bit
Byte
(MSB)
LUN LIST LENGTH (n-7)
•••
(LSB)
Reserved
•••
LUN list
LUN [first]
•••
•••
n-7
LUN [last]
•••
n


6.34 REPORT PRIORITY command
The REPORT PRIORITY command (see table 287) requests the priority that has been assigned to one or
more I_T nexuses associated with the logical unit (i.e., I_T_L nexuses). This command uses the MAINTE-
NANCE IN CDB format (see 4.2.2.3.3).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 287 for the REPORT
PRIORTY command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 287 for the REPORT
PRIORTY command.
The PRIORITY REPORTED field (see table 288) specifies the information to be returned in the parameter data.
The ALLOCATION LENGTH field is defined in 4.2.5.6. The allocation length should be at least four.
The CONTROL byte is defined in SAM-5.
Table 287 — REPORT PRIORITY command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (0Eh)
PRIORITY REPORTED
Reserved
Reserved

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CONTROL
Table 288 — PRIORITY REPORTED field
Code
Description
00b
Only the priority for the I_T nexus on which the command was
received shall be reported in the REPORT PRIORITY parameter data.
01b
The priority for each I_T nexus that is not set to the initial command
priority shall be reported in the REPORT PRIORITY parameter data.
10b to 11b
Reserved


The format of the parameter data returned by the REPORT PRIORITY command is shown in table 289.
The PRIORITY PARAMETER DATA LENGTH field indicates the number of bytes of parameter data that follow. The
contents of the PRIORITY PARAMETER DATA LENGTH field are not altered based on the allocation length (see
4.2.5.6).
Each priority descriptor (see table 290) contains priority information for a single I_T_L nexus.
The CURRENT PRIORITY field indicates the priority assigned to the I_T_L nexus represented by this descriptor. If
the PRIORITY REPORTED field in this command is set to 00b and the priority for the I_T_L nexus associated with
this command is set to the initial command priority, then the CURRENT PRIORITY field shall be set to zero. The
priority assigned to an I_T_L nexus may be used as a command priority for commands received via that I_T_L
nexus (see SAM-5).
Table 289 — REPORT PRIORITY parameter data format
Bit
Byte
(MSB)
PRIORITY PARAMETER DATA LENGTH (n-3)

•••
 (LSB)
Priority descriptors
Priority descriptor [first] (see table 290)
•••
•••
Priority descriptor [last] (see table 290)
•••
n
Table 290 — Priority descriptor format
Bit
Byte
Reserved
CURRENT PRIORITY
Reserved
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
Reserved
Reserved
(MSB)
ADDITIONAL DESCRIPTOR LENGTH (n-7)
(LSB)
TransportID
•••
n
