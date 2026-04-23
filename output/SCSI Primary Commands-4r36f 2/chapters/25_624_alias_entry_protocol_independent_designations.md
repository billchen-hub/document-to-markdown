# 6.2.4 Alias entry protocol independent designations

The zero-padded (see 4.3.2) DESIGNATION field should designate a unique SCSI target device or target port
using the following:
a)
a SCSI device name or a target port name; and
b)
optionally, one or more target port identifiers or SCSI transport protocol specific identifiers.
6.2.3 Alias designation validation
The device server shall not validate any designation at the time of processing either the REPORT ALIASES or
CHANGE ALIASES command. Such validation shall occur only when the device server consults the alias list
to resolve an alias to a designation in the context of third-party commands (e.g., EXTENDED COPY) or any
other command that requires reference to the alias list.
If a designation identifies a unique SCSI target device or target port that is within a SCSI domain accessible to
the device server, the designation is considered valid.
Based on the SCSI transport protocol specific requirements for a given designation format, a designation that
does not identify a unique SCSI target device or target port within the SCSI domains accessible to the device
server is considered invalid.
NOTE 25 - For example, a designation may be considered invalid if the device server has no ports on the
SCSI domain of the designated SCSI target device or target port.
A designation having both name and identifier information may be inconsistent if the device server is not able
to access the named SCSI target device or target port through one or more of the names or identifiers in the
designation. In such cases, the designation shall be treated as valid or invalid according to the SCSI transport
protocol specific requirements.
Notes
For example, in FCP-4 both an N_Port and World Wide Name for a SCSI port may be given in a desig-
nation. The designation definition may require that the N_Port be that of the named port. In that case, the
designation is invalid. Alternatively, the designation definition may view the N_Port as a hint for the
named FC Port accessible to the device server through a different D_ID. In that case, the designation is
valid and designates the named FC Port.
If only name information is provided in a designation, it is assumed that the device server has access to
a mechanism for resolving names to identifiers. Access to such a service is SCSI transport protocol
specific and vendor specific.
6.2.4 Alias entry protocol independent designations
6.2.4.1 Alias entry protocol independent designations overview
The protocol independent alias entry designations have a protocol identifier of 80h and one of the format
codes shown in table 123.
Table 123 — Protocol independent alias entry format codes
Format
Code
Name
Designation
Length (bytes)
Designation
Contents
Reference
00h
NULL DESIGNATION
none
6.2.4.2
01h to FFh
Reserved


6.2.4.2 NULL DESIGNATION alias format
In response to an alias entry with the NULL DESIGNATION format, the device server shall remove the
specified alias value from the alias list. Application clients should use the NULL DESIGNATION format in a
CHANGE ALIASES command to remove an alias entry from the alias list if that alias entry is no longer
needed. The NULL DESIGNATION format shall not appear in REPORT ALIASES parameter data.
6.3 COPY OPERATION ABORT command
The COPY OPERATION ABORT command (see table 124) is a third-party copy command (see 5.17.3) that
requests that the copy manager abort the specified copy operation (see 5.17.4.3) as described in 5.17.4.7.
Whether the copy operation is being processed in the foreground or background, the effect of the COPY
OPERATION ABORT command is equivalent to an ABORT TASK task management function (see SAM-5 and
5.17.4.6).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 124 for the COPY
OPERATION ABORT command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 124 for the COPY
OPERATION ABORT command.
The LIST IDENTIFIER field is defined in 5.17.4.2 and 6.4.3.2, and specifies the copy operation to be aborted. If
the copy manager is not processing a copy operation with the specified list identifier, the copy manager shall
terminate the COPY OPERATION ABORT command with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-5.
Table 124 — COPY OPERATION ABORT command
Bit
Byte
OPERATION CODE (83h)
Reserved
SERVICE ACTION (1Ch)
(MSB)
LIST IDENTIFIER

•••
(LSB)
Reserved

•••
CONTROL


6.4 EXTENDED COPY(LID4) command
6.4.1 EXTENDED COPY(LID4) command introduction
The EXTENDED COPY(LID4) command (see table 125) provides a means to copy data from one set of copy
sources (e.g., a set of source logical units) to a set of copy destinations (e.g., a set of destination logical units).
The transfers requested by an EXTENDED COPY command are managed by a copy manager (see SAM-5
and 5.17.2).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 125 for the EXTENDED
COPY(LID4) command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 125 for the EXTENDED
COPY(LID4) command.
The PARAMETER LIST LENGTH field is defined in 4.2.5.5. A parameter list length of zero specifies that the copy
manager shall not transfer any data or alter any internal state, and this shall not be considered an error. If the
parameter list length causes truncation of the parameter list, then no data shall be transferred and the
EXTENDED COPY command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH ERROR.
The CONTROL byte is defined in SAM-5.
Table 125 — EXTENDED COPY(LID4) command
Bit
Byte
OPERATION CODE (83h)
Reserved
SERVICE ACTION (01h)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL
