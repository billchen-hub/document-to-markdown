# 6.2.1 CHANGE ALIASES command introduction

6.2 CHANGE ALIASES command
6.2.1 CHANGE ALIASES command introduction
The CHANGE ALIASES command (see table 119) requests that the device server maintain and make
changes to a list of associations between eight byte alias values and SCSI target device or SCSI target port
designations. This command uses the MAINTENANCE OUT CDB format (see 4.2.2.3.4). A designation
contains a name and optional identifier information that specifies a SCSI target device or SCSI target port (see
6.2.2). The alias list may be queried by the application client via the REPORT ALIASES command (see 6.30).
If the REPORT ALIASES command is supported, the CHANGE ALIASES command shall also be supported.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 119 for the CHANGE
ALIASES command.
The SERVICE ACTION field is defined in 4.2.5.2 and shall be set as shown in table 119 for the CHANGE
ALIASES command.
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter data that shall be transferred
from the application client to the device server. A parameter list length value of zero specifies that no data
shall be transferred and no changes shall be made in the alias list.
The CONTROL byte is defined in SAM-5.
If the parameter list length results in the truncation of the header or any alias entry, then the device server
shall make no changes to the alias list and terminate the command with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH
ERROR.
On successful completion of a CHANGE ALIASES command, the device server shall maintain an association
of each assigned eight byte alias value to the SCSI target device or SCSI target port designation. These
associations shall be cleared by a logical unit reset or I_T nexus loss. The device server shall maintain a
separate alias list for each I_T nexus.
A CHANGE ALIASES command may add, change or remove entries from the alias list. Alias list entries not
referenced in the CHANGE ALIASES parameter data shall not be changed.
Table 119 — CHANGE ALIASES command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (0Bh)
Reserved

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
Reserved
CONTROL


NOTE 24 - An application client may use alias values to reference SCSI target devices or SCSI target ports in
third party commands (e.g., EXTENDED COPY). The alias list provides a mechanism for eight byte third party
identifier fields to reference a third party device or port whose name or addressing information is longer than
eight bytes. (E.g., an application may use the CHANGE ALIASES command to establish an association
between an alias value and a SCSI target device or target port designation. Then, it may send an EXTENDED
COPY command containing in the parameter data an alias CSCD descriptor (see 6.4.5.7) that includes this
alias value. At the completion of the EXTENDED COPY command the application should clear this entry from
the device server’s alias list by sending a CHANGE ALIASES command that requests association of the alias
value to a NULL DESIGNATION (see 6.2.4.2) alias format.)
If the device server has insufficient resources to make all requested changes to the alias list, then the device
server shall make no changes to the alias list and shall terminate the command with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INSUFFICIENT
RESOURCES.
The parameter data for a CHANGE ALIASES command (see table 120) contains zero or more alias entries. If
the device server processes a CHANGE ALIASES command that contains at least one alias entry while there
exists any other enabled command that references an alias entry in the alias list, then the device server shall
terminate the CHANGE ALIASES command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to OPERATION IN PROGRESS.
The PARAMETER DATA LENGTH field should contain the number of bytes of alias entries, and shall be ignored by
the device server.
The format of an alias entry is described in 6.2.2.
Table 120 — CHANGE ALIASES parameter list
Bit
Byte
(MSB)
PARAMETER DATA LENGTH (n-3)

•••
 (LSB)
Reserved

•••
Alias entry (or entries)
Alias entry 0 (see 6.2.2)
•••
•••
Alias entry x (see 6.2.2)
•••
n


6.2.2 Alias entry format
One alias entry (see table 121) describes one alias reported via the REPORT ALIASES command (see 6.30)
or to be changed via the CHANGE ALIASES command.
The ALIAS VALUE field is set to the numeric alias value that the device server shall associate with the SCSI
target device or target port specified by the values in the PROTOCOL IDENTIFIER, FORMAT CODE and DESIGNATION
fields.
The PROTOCOL IDENTIFIER field (see table 122) specifies that the alias entry designation is independent of
SCSI transport protocol or the SCSI transport protocol to which the alias entry applies.
The FORMAT CODE field contents combined with the PROTOCOL IDENTIFIER field contents defines the format of
the DESIGNATION field. The subclauses that describe each PROTOCOL IDENTIFIER field usage (see table 122)
define the applicable FORMAT CODE field values.
The DESIGNATION LENGTH field specifies the number of bytes of the DESIGNATION field. The DESIGNATION
LENGTH value shall be a multiple of four.
Table 121 — Alias entry format
Bit
Byte
(MSB)
ALIAS VALUE
•••
(LSB)
PROTOCOL IDENTIFIER
Reserved
FORMAT CODE
Reserved
(MSB)
DESIGNATION LENGTH (n-15)
(LSB)
DESIGNATION
•••
n
Table 122 — Alias entry PROTOCOL IDENTIFIER field
Code
Description
Reference
00h to 0Fh
Protocol specific designation
7.6.2
10h to 7Fh
Reserved
80h
Protocol independent designation
6.2.4
81h to FFh
Reserved
