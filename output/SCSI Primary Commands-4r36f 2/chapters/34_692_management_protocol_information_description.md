# 6.9.2 Management protocol information description

Any association between a previous MANAGEMENT PROTOCOL OUT command and the data transferred by
a MANAGEMENT PROTOCOL IN command depends on the protocol specified by the MANAGEMENT
PROTOCOL field (see table 189). If the device server has no data to transfer (e.g., the results for any previous
MANAGEMENT PROTOCOL OUT commands are not yet available), the device server may transfer data
indicating it has no other data to transfer.
The format of the data transferred depends on the protocol specified by the MANAGEMENT PROTOCOL field (see
table 189).
The device server shall retain data resulting from a MANAGEMENT PROTOCOL OUT command, if any, until
one of the following events is processed:
a)
transfer of the data via a MANAGEMENT PROTOCOL IN command from the same I_T_L nexus as
defined by the protocol specified by the MANAGEMENT PROTOCOL field (see table 189);
b)
logical unit reset (see SAM-5); or
c)
I_T nexus loss (see SAM-5) associated with the I_T nexus that sent the MANAGEMENT PROTOCOL
OUT command.
If the data is lost due to one of these events the application client may send a new MANAGEMENT
PROTOCOL OUT command to retry the operation.
6.9.2 Management protocol information description
6.9.2.1 Overview
The purpose of the management protocol information management protocol (i.e., the MANAGEMENT PROTOCOL
field set to 00h in a MANAGEMENT PROTOCOL IN command) is to transfer management protocol related
information from the logical unit. A MANAGEMENT PROTOCOL IN command in which the MANAGEMENT
PROTOCOL field is set to 00h is not associated with any previous MANAGEMENT PROTOCOL OUT command
and shall be processed without regard for whether a MANAGEMENT PROTOCOL OUT command has been
processed.
If the MANAGEMENT PROTOCOL IN command is supported, the MANAGEMENT PROTOCOL value of 00h shall
be supported as defined in this standard.
6.9.2.2 CDB description
If the MANAGEMENT PROTOCOL field is set to 00h in a MANAGEMENT PROTOCOL IN command, the
MANAGEMENT PROTOCOL SPECIFIC1 field is reserved and the MANAGEMENT PROTOCOL SPECIFIC2 field (see table
190) contains a single numeric value as defined in 3.6.
All other CDB fields for MANAGEMENT PROTOCOL IN command shall meet the requirements stated in
6.9.1.
Each time a MANAGEMENT PROTOCOL IN command with the MANAGEMENT PROTOCOL field set to 00h is
received, the device server shall transfer the data defined 6.9.2.3 starting with byte 0.
Table 190 — MANAGEMENT PROTOCOL SPECIFIC2 field for MANAGEMENT PROTOCOL IN protocol 00h
Code
Description
Support
Reference
00h
Supported management protocol list
Mandatory
6.9.2.3
01h to FFh
Reserved


6.9.2.3 Supported management protocols list description
If the MANAGEMENT PROTOCOL field is set to 00h and the MANAGEMENT PROTOCOL SPECIFIC2 field is set to 00h in
a MANAGEMENT PROTOCOL IN command, then the parameter data shall have the format shown in table
191.
The SUPPORTED MANAGEMENT PROTOCOL LIST LENGTH field indicates the total length, in bytes, of the supported
management protocol list that follows.
Each SUPPORTED MANAGEMENT PROTOCOL field in the supported management protocols list shall contain one
of the management protocol values supported by the logical unit. The values shall be listed in ascending order
starting with 00h.
The total data length shall conform to the ALLOCATION LENGTH field requirements (see 4.2.5.6).
Table 191 — Supported management protocols MANAGEMENT PROTOCOL IN parameter data
Bit
Byte
Reserved

•••
(MSB)
SUPPORTED MANAGEMENT PROTOCOL LIST LENGTH
(n-7)
(LSB)
Supported management protocol list
SUPPORTED MANAGEMENT PROTOCOL [first] (00h)
•••
n
SUPPORTED MANAGEMENT PROTOCOL [last]


6.10 MANAGEMENT PROTOCOL OUT command
The MANAGEMENT PROTOCOL OUT command (see table 192) is used to send data to the logical unit. The
data sent specifies one or more operations to be performed by the logical unit. The format and function of the
operations depends on the contents of the MANAGEMENT PROTOCOL field (see table 192). Depending on the
protocol specified by the MANAGEMENT PROTOCOL field, the application client may use the MANAGEMENT
PROTOCOL IN command (see 6.9) to retrieve data derived from these operations.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 192 for the MANAGEMENT
PROTOCOL OUT command.
The MANAGEMENT PROTOCOL field (see table 193) specifies which management protocol is being used.
The contents of the MANAGEMENT PROTOCOL SPECIFIC1 field and MANAGEMENT PROTOCOL SPECIFIC2 field depend
on the protocol specified by the MANAGEMENT PROTOCOL field (see table 193).
The PARAMETER LIST LENGTH field is defined in 4.2.5.5.
The CONTROL byte is defined in SAM-5.
Table 192 — MANAGEMENT PROTOCOL OUT command
Bit
Byte
OPERATION CODE (A4h)
Reserved
SERVICE ACTION (10h)
MANAGEMENT PROTOCOL
MANAGEMENT PROTOCOL SPECIFIC1

•••
(MSB)
PARAMETER LIST LENGTH

•••
(LSB)
MANAGEMENT PROTOCOL SPECIFIC2
CONTROL
Table 193 — MANAGEMENT PROTOCOL field in MANAGEMENT PROTOCOL OUT command
Code
Description
Reference
00h to 2Fh
Reserved
30h to 35h
Defined by the SNIA
3.1.171
36h to EFh
Reserved
F0h to FFh
Vendor Specific


Any association between a MANAGEMENT PROTOCOL OUT command and a subsequent MANAGEMENT
PROTOCOL IN command depends on the protocol specified by the MANAGEMENT PROTOCOL field (see table
193). Each management protocol shall define whether:
a)
the device server shall complete the command with GOOD status as soon as it determines the data
has been correctly received. An indication that the data has been processed is obtained by sending a
MANAGEMENT PROTOCOL IN command and receiving the results in the associated data transfer;
or
b)
the device server shall complete the command with GOOD status only after the data has been
successfully processed and an associated MANAGEMENT PROTOCOL IN command is not required.
The format of the data transferred depends on the protocol specified by the MANAGEMENT PROTOCOL field (see
table 193).
6.11 MODE SELECT(6) command
The MODE SELECT(6) command (see table 194) provides a means for the application client to specify
medium, logical unit, or peripheral device parameters to the device server. Device servers that implement the
MODE SELECT(6) command shall also implement the MODE SENSE(6) command. Application clients
should issue MODE SENSE(6) prior to each MODE SELECT(6) to determine supported mode pages, page
lengths, and other parameters.
NOTE 32 - Implementations should migrate from the MODE SELECT(6) command to the MODE
SELECT(10) command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 194 for the MODE
SELECT(6) command.
If an application client sends a MODE SELECT command that changes any parameters applying to other I_T
nexuses, the device server shall establish a unit attention condition (see SAM-5) for the initiator port
associated with every I_T nexus except the I_T nexus on which the MODE SELECT command was received,
with the additional sense code set to MODE PARAMETERS CHANGED.
A page format (PF) bit set to zero specifies that all parameters after the block descriptors are vendor specific.
A PF bit set to one specifies that the MODE SELECT parameters following the header and block descriptor(s)
are structured as pages of related parameters and are as defined in this standard.
A save pages (SP) bit set to zero specifies that the device server shall perform the specified MODE SELECT
operation, and shall not save any mode pages. If the logical unit implements no distinction between current
Table 194 — MODE SELECT(6) command
Bit
Byte
OPERATION CODE (15h)
Reserved
PF
Reserved
SP
Reserved
PARAMETER LIST LENGTH
CONTROL


and saved mode pages and the SP bit is set to zero, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB. An SP bit set to one specifies that the device server shall perform the specified
MODE SELECT operation, and shall save to a nonvolatile vendor specific location all the saveable mode
pages including any sent in the Data-Out Buffer. Mode pages that are saved are specified by the parameter
saveable (PS) bit that is returned in the first byte of each mode page by the MODE SENSE command (see
7.5). If the PS bit is set to one in the MODE SENSE data, then the mode page shall be saveable by issuing a
MODE SELECT command with the SP bit set to one. If the logical unit does not implement saved mode pages
and the SP bit is set to one, then the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The PARAMETER LIST LENGTH field specifies the length in bytes of the mode parameter list that shall be
contained in the Data-Out Buffer. A parameter list length of zero specifies that the Data-Out Buffer shall be
empty. This condition shall not be considered an error.
If the parameter list length results in the truncation of any mode parameter header, mode parameter block
descriptor(s), or mode page, then the command shall be terminated with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to PARAMETER LIST LENGTH
ERROR.
The CONTROL byte is defined in SAM-5.
The mode parameter list for the MODE SELECT and MODE SENSE commands is defined in 7.5. Parts of
each mode parameter list are defined in a device-type dependent manner. Definitions for the parts of each
mode parameter list that are unique for each device-type may be found in the applicable command standards.
The device server shall terminate the MODE SELECT command with CHECK CONDITION status, set the
sense key to ILLEGAL REQUEST, set the additional sense code to INVALID FIELD IN PARAMETER LIST,
and shall not change any mode parameters in response to any of the following conditions:
a)
if the application client sets any field that is reported as not changeable by the device server to a value
other than its current value;
b)
if the application client sets any field in the mode parameter header or block descriptor(s) to an unsup-
ported value;
c)
if an application client sends a mode page with a page length not equal to the page length returned by
the MODE SENSE command for that mode page;
d)
if the application client sends an unsupported value for a mode parameter and rounding is not imple-
mented for that mode parameter; or
e)
if the application client sets any reserved field in the mode parameter list to a non-zero value and the
device server checks reserved fields.
If the application client sends a value for a mode parameter that is outside the range supported by the device
server and rounding is implemented for that mode parameter, the device server handles the condition by
either:
a)
rounding the parameter to an acceptable value and terminating the command as described in 5.9; or
b)
terminating the command with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
A device server may alter any mode parameter in any mode page, even those reported as non-changeable,
as a result of changes to other mode parameters.
The device server validates the non-changeable mode parameters against the current values that existed for
those mode parameters prior to the MODE SELECT command.


NOTE 33 - The current values calculated by the device server may affect the application client's operation.
The application client may issue a MODE SENSE command after each MODE SELECT command, to
determine the current values.
6.12 MODE SELECT(10) command
The MODE SELECT(10) command (see table 195) provides a means for the application client to specify
medium, logical unit, or peripheral device parameters to the device server. See the MODE SELECT(6)
command (6.11) for a description of the fields and operation of this command. Application clients should issue
MODE SENSE(10) prior to each MODE SELECT(10) to determine supported mode pages, page lengths, and
other parameters. Device servers that implement the MODE SELECT(10) command shall also implement the
MODE SENSE(10) command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 195 for the MODE
SELECT(10) command.
The CONTROL byte is defined in SAM-5.
See the MODE SELECT(6) command (6.11) for a description of the other fields and operation of this
command.
Table 195 — MODE SELECT(10) command
Bit
Byte
OPERATION CODE (55h)
Reserved
PF
Reserved
SP
Reserved

•••
(MSB)
PARAMETER LIST LENGTH
(LSB)
CONTROL


6.13 MODE SENSE(6) command
6.13.1 MODE SENSE(6) command introduction
The MODE SENSE(6) command (see table 196) provides a means for a device server to report parameters to
an application client. It is a complementary command to the MODE SELECT(6) command. Device servers
that implement the MODE SENSE(6) command shall also implement the MODE SELECT(6) command.
NOTE 34 - Implementations should migrate from the MODE SENSE(6) command to the MODE SENSE(10)
command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 196 for the MODE
SENSE(6) command.
A disable block descriptors (DBD) bit set to zero specifies that the device server may return zero or more block
descriptors in the returned MODE SENSE data (see 7.5). A DBD bit set to one specifies that the device server
shall not return any block descriptors in the returned MODE SENSE data.
The page control (PC) field specifies the type of mode parameter values to be returned in the mode pages.
The PC field is defined in table 197.
The PC field only affects the mode parameters within the mode pages, however the PS bit, SPF bit, PAGE CODE
field, SUBPAGE CODE field, and PAGE LENGTH field should return current values (i.e., as if PC is set to 00b). The
mode parameter header and mode parameter block descriptor should return current values.
Some SCSI target devices may not distinguish between current and saved mode parameters and report
identical values in response to a PC field of either 00b or 11b. See also the description of the save pages (SP)
bit in the MODE SELECT command.
Table 196 — MODE SENSE(6) command
Bit
Byte
OPERATION CODE (1Ah)
Reserved
DBD
Reserved
PC
PAGE CODE
SUBPAGE CODE
ALLOCATION LENGTH
CONTROL
Table 197 — Page control (PC) field
Code
Type of parameter
Reference
00b
Current values
6.13.2
01b
Changeable values
6.13.3
10b
Default values
6.13.4
11b
Saved values
6.13.5


The PAGE CODE and SUBPAGE CODE fields (see table 198) specify which mode pages and subpages to return.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
An application client may request any one or all of the supported mode pages from the device server. If an
application client issues a MODE SENSE command with a page code or subpage code value not imple-
mented by the logical unit, the command shall be terminated with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
If an application client requests all supported mode pages, the device server shall return the supported pages
in ascending page code order beginning with mode page 01h. If mode page 00h is implemented, the device
server shall return mode page 00h after all other mode pages have been returned.
If the PC field and the PAGE CODE field are both set to zero, the device server should return a mode parameter
header and block descriptor, if applicable.
The mode parameter list for all device types for MODE SELECT and MODE SENSE is defined in 7.5. Parts of
the mode parameter list are specifically defined for each device type. Definitions for the parts of each mode
parameter list that are unique for each device-type may be found in the applicable command standards.
6.13.2 Current values
A PC field value of 00b requests that the device server return the current values of the mode parameters. The
current values returned are:
a)
the current values of the mode parameters established by the last successful MODE SELECT
command;
b)
the saved values of the mode parameters if a MODE SELECT command has not successfully
completed since the mode parameters were restored to their saved values (see 6.11); or
c)
the default values of the mode parameters if a MODE SELECT command has not successfully
completed since the mode parameters were restored to their default values (see 6.11).
Table 198 — Mode page code usage in MODE SENSE commands for all devices
Page Code
Subpage Code
Description
00h
vendor specific
Vendor specific (does not require page format)
01h to 3Eh
00h
See specific device types (page_0 format)
01h to DFh
See specific device types (sub_page format)
E0h to FEh
Vendor specific (sub_page format)
FFh
Return all subpages (see specific device types) for the specified
device specific mode page in the page_0 format for subpage 00h
and in the sub_page format for subpages 01h to FEh
3Fh
00h
Return all subpage 00h mode pages in page_0 format
01h to FEh
Reserved
FFh
Return all subpages for all mode pages in the page_0 format for
subpage 00h and in the sub_page format for subpages 01h to
FEh
