# 7.5.8 Control mode page

The PAGE CODE field and SUBPAGE CODE field (see 7.5.1) identify the format and parameters defined for that
mode page. Some page codes are defined as applying to all device types and other page codes are defined
for the specific device type. The page codes that apply to a specific device type are defined in the command
standard for that device type. The applicability of each subpage code matches that of the page code with
which it is associated.
If a mode page is in the page_0 mode page format, then the mode page shall be the one for which the
contents of a MODE SENSE command SUBPAGE CODE field (see 6.13.1) are set to zero.
When using the MODE SENSE command, if page code 00h (vendor specific mode page) is implemented, the
device server shall return that mode page last in response to a request to return all mode pages (page code
3Fh). When using the MODE SELECT command, this mode page should be sent last.
The PAGE LENGTH field specifies the length in bytes of the mode parameters that follow. If the application client
does not set this value to the value that is returned for the mode page by the MODE SENSE command, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST. The logical unit may
implement a mode page that is less than the full mode page length defined, provided no field is truncated and
the PAGE LENGTH field correctly specifies the actual length implemented.
The mode parameters for each mode page are defined in the following subclauses, or in the mode parameters
subclause in the command standard for the specific device type. Mode parameters not implemented by the
logical unit shall be set to zero.
7.5.8 Control mode page
The Control mode page (see table 457) provides controls over SCSI features that are applicable to all device
types (e.g., task set management and error logging). If a field in this mode page is changed while there is a
command already in the task set, it is vendor specific whether the old or new value of the field applies to that
command. The mode page policy (see 7.5.2) for this mode page shall be shared, or per I_T nexus.
Table 457 — Control mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (0Ah)
PAGE LENGTH (0Ah)
TST
TMF_ONLY
DPICZ
D_SENSE
GLTSD
RLEC
QUEUE ALGORITHM MODIFIER
NUAR
QERR
Obsolete
VS
RAC
UA_INTLCK_CTRL
SWP
Obsolete
ATO
TAS
ATMPE
RWWP
Reserved
AUTOLOAD MODE

Obsolete

(MSB)
BUSY TIMEOUT PERIOD
(LSB)
(MSB)
EXTENDED SELF-TEST COMPLETION TIME
(LSB)


The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit, PAGE CODE field, and PAGE LENGTH field shall be set as shown in table 457 for the Control mode
page.
A task set type (TST) field (see table 458) specifies the type of task set in the logical unit.
Regardless of the mode page policy (see 7.5.2) for the Control mode page, the shared mode page policy shall
be applied to the TST field. If the most recent MODE SELECT changes the setting of this field, then the device
server shall establish a unit attention condition (see SAM-5) for the initiator port associated with every I_T
nexus except the I_T nexus on which the MODE SELECT command was received, with the additional sense
code set to MODE PARAMETERS CHANGED.
The allow task management functions only (TMF_ONLY) bit set to zero specifies that the device server shall
process commands with the ACA task attribute received on the faulted I_T nexus while an ACA condition is
established (see SAM-5). A TMF_ONLY bit set to one specifies that the device server shall complete all
commands received on the faulted I_T nexus with an ACA ACTIVE status while an ACA condition is estab-
lished.
A disable protection information check if protect field is zero (DPICZ) bit set to zero indicates that checking of
protection information bytes is enabled. A DPICZ bit set to one indicates that checking of protection information
is disabled on commands with:
a)
the RDPROTECT field (see SBC-3) set to zero;
b)
the VRPROTECT field (see SBC-3) set to zero; or
c)
the ORPROTECT field (see SBC-3) set to zero.
A descriptor format sense data (D_SENSE) bit set to zero specifies that the device server shall return fixed
format sense data (see 4.5.3) when returning sense data in the same I_T_L_Q nexus transaction as the
status. A D_SENSE bit set to one specifies that the device server shall return descriptor format sense data (see
4.5.2) when returning sense data in the same I_T_L_Q nexus transaction as the status, except as defined in
4.5.1. If an application client enables reporting of referrals in sense data (see SBC-3), then the application
client should be able to handle up to 252 bytes of sense data.
A global logging target save disable (GLTSD) bit set to zero specifies that the logical unit implicitly saves, at
vendor specific intervals, each log parameter in which the TSD bit (see 7.3) is set to zero. A GLTSD bit set to
one specifies that the logical unit shall not implicitly save any log parameters.
A report log exception condition (RLEC) bit set to one specifies that the device server shall report log exception
conditions as described in 7.3. A RLEC bit set to zero specifies that the device server shall not report log
exception conditions.
Table 458 — Task set type (TST) field
Code
Description
000b
The logical unit maintains one task set for all I_T nexuses
001b
The logical unit maintains separate task sets for each I_T nexus
010b to 111b
Reserved


The QUEUE ALGORITHM MODIFIER field (see table 459) specifies restrictions on the algorithm used for reordering
commands having the SIMPLE task attribute (see SAM-5).
A value of zero in the QUEUE ALGORITHM MODIFIER field specifies that the device server shall order the
processing sequence of commands having the SIMPLE task attribute such that data integrity is maintained for
that I_T nexus (i.e., if the transmission of new SCSI transport protocol requests is halted at any time, the final
value of all data observable on the medium shall be the same as if all the commands had been processed with
the ORDERED task attribute).
A value of one in the QUEUE ALGORITHM MODIFIER field specifies that the device server may reorder the
processing sequence of commands having the SIMPLE task attribute in any manner. Any data integrity
exposures related to command sequence order shall be explicitly handled by the application client through the
selection of appropriate commands and task attributes.
A no unit attention on release (NUAR) bit set to one specifies that the device server shall not establish a unit
attention condition as described in 5.13.11.2.2. A NUAR bit set to zero specifies that the device server shall
establish a unit attention condition as described in 5.13.11.2.2.
Table 459 — QUEUE ALGORITHM MODIFIER field
Code
Description
0h
Restricted reordering
1h
Unrestricted reordering allowed
2h to 7h
Reserved
8h to Fh
Vendor specific


The queue error management (QERR) field (see table 460) specifies how the device server shall handle other
commands when one command is terminated with CHECK CONDITION status (see SAM-5). The task set
type (see the TST field definition in this subclause) defines which other commands are affected. If the TST field
equals 000b, then all commands from all I_T nexuses are affected. If the TST field equals 001b, then only
commands from the same I_T nexus as the command that is terminated with CHECK CONDITION status are
affected.
The report a check (RAC) bit provides control of reporting long busy conditions or CHECK CONDITION status.
A RAC bit set to one specifies that the device server should return CHECK CONDITION status rather than
returning BUSY status if the reason for returning the BUSY status may persist for a longer time than that
specified by the BUSY TIMEOUT PERIOD field. A RAC bit set to zero specifies that the device server may return
BUSY status regardless of the length of time the reason for returning BUSY status may persist.
Table 460 — Queue error management (QERR) field
Code
Definition
00b
If an ACA condition is established, the affected commands in the task set shall resume after
the ACA condition is cleared (see SAM-5). Otherwise, all commands other than the command
that received the CHECK CONDITION status shall be processed as if no error occurred.
01b
All the affected commands in the task set shall be aborted when the CHECK CONDITION
status is sent. If the TAS bit is set to zero, the device server shall establish a unit attention
condition (see SAM-5) for the initiator port associated with every I_T nexus that had
commands aborted except for the I_T nexus on which the CHECK CONDITION status was
returned, with the additional sense code set to COMMANDS CLEARED BY ANOTHER
INITIATOR. If the TAS bit is set to one, all affected commands in the task set for I_T nexuses
other than the I_T nexus for which the CHECK CONDITION status was sent shall be
completed with TASK ABORTED status and no unit attention shall be established. For the I_T
nexus to which the CHECK CONDITION status is sent, no status shall be sent for the
commands that are aborted.
10b
Reserved
11b
Affected commands in the task set belonging to the I_T nexus on which a CHECK CONDI-
TION status is returned shall be aborted when the status is sent.


The unit attention interlocks control (UA_INTLCK_CTRL) field (see table 461) controls the clearing of unit
attention conditions reported in the same I_T_L_Q nexus transaction as a CHECK CONDITION status and
whether returning a status of BUSY, TASK SET FULL or RESERVATION CONFLICT results in the estab-
lishment of a unit attention condition (see SAM-5).
A software write protect (SWP) bit set to one specifies that the logical unit shall inhibit writing to the medium
after writing all cached or buffered write data, if any. If the SWP bit is set to one, all commands requiring writes
to the medium shall be terminated with CHECK CONDITION status, with the sense key set to DATA
PROTECT, and the additional sense code set to WRITE PROTECTED. If the SWP bit is set to one and the
device type's command standard defines a write protect (WP) bit in the DEVICE-SPECIFIC PARAMETER field in the
mode parameter header, then the WP bit shall be set to one for subsequent MODE SENSE commands. A SWP
bit set to zero specifies that the logical unit may allow writing to the medium, depending on other write inhibit
mechanisms implemented by the logical unit. If the SWP bit is set to zero, the value of the WP bit, if defined, is
device type specific. For a list of commands affected by the SWP bit and details of the WP bit see the command
standard for the specific device type.
An application tag owner (ATO) bit set to zero specifies that the device server may modify the contents of the
LOGICAL BLOCK APPLICATION TAG field and, depending on the protection type, may modify the contents of the
LOGICAL BLOCK REFERENCE TAG field (see SBC-3). If the ATO bit is set to one the device server shall not modify
the LOGICAL BLOCK APPLICATION TAG field and, depending on the protection type, shall not modify the contents
of the LOGICAL BLOCK REFERENCE TAG field.
A task aborted status (TAS) bit set to zero specifies that aborted commands shall be terminated by the device
server without any response to the application client. A TAS bit set to one specifies that commands aborted by
the actions of an I_T nexus other than the I_T nexus on which the command was received shall be completed
with TASK ABORTED status (see SAM-5).
Table 461 — Unit attention interlocks control (UA_INTLCK_CTRL) field
Code
Definition
00b
The logical unit shall clear any unit attention condition reported in the same I_T_L_Q nexus
transaction as a CHECK CONDITION status and shall not establish a unit attention condition
when a command is completed with BUSY, TASK SET FULL, or RESERVATION CONFLICT
status.
01b
Reserved a
10b a
The logical unit shall not clear any unit attention condition reported in the same I_T_L_Q nexus
transaction as a CHECK CONDITION status and shall not establish a unit attention condition
when a command is completed with BUSY, TASK SET FULL, or RESERVATION CONFLICT
status.
11b a
The logical unit shall not clear any unit attention condition reported in the same I_T_L_Q nexus
transaction as a CHECK CONDITION status and shall establish a unit attention condition for the
initiator port associated with the I_T nexus on which the BUSY, TASK SET FULL, or RESER-
VATION CONFLICT status is being returned. Depending on the status, the additional sense
code shall be set to PREVIOUS BUSY STATUS, PREVIOUS TASK SET FULL STATUS, or
PREVIOUS RESERVATION CONFLICT STATUS. Until it is cleared by a REQUEST SENSE
command, a unit attention condition shall be established only once for a BUSY, TASK SET
FULL, or RESERVATION CONFLICT status regardless to the number of commands completed
with one of those status codes.
a A REQUEST SENSE command still clears any unit attention condition that it reports.


An application tag mode page enabled (ATMPE) bit set to zero specifies that the Application Tag mode page
(see SBC-3) is disabled and the contents of logical block application tags are not defined by this standard. An
ATMPE bit set to one specifies that the Application Tag mode page is enabled.
If:
a)
the ATMPE is set to one;
b)
the ATO bit is set to one;
c)
the value in the DPICZ bit allows protection information checking for the specified command; and
d)
the APP_CHK bit is set to one in the Extended INQUIRY VPD page (see 7.8.7);
then:
knowledge of the value of the Application Tag shall come from the values in the Application Tag mode
page as specified by the DPICZ bit.
A reject write without protection (RWWP) bit set to zero specifies that the device server shall process write
commands that are specified to include user data without protection information (e.g., a WRITE(10) command
with the WRPROTECT field set to 000b (see SBC-3)). A RWWP bit set to one specifies that the device server in a
logical unit that has been formatted with protection information shall terminate with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB any write command that is specified to include user data without protection information.
The AUTOLOAD MODE field specifies the action to be taken by a removable medium device server at the time
when a medium is inserted. For devices other than removable medium devices, this field is reserved. Table
462 shows the usage of the AUTOLOAD MODE field.
The BUSY TIMEOUT PERIOD field specifies the maximum time, in 100 milliseconds increments, that the appli-
cation client allows for the device server to return BUSY status for unanticipated conditions that are not a
routine part of commands from the application client. This value may be rounded down as defined in 5.9. A
0000h value in this field is undefined by this standard. An FFFFh value in this field is defined as an unlimited
period.
The EXTENDED SELF-TEST COMPLETION TIME field specifies advisory data that is the time in seconds that the
device server requires to complete an extended self-test provided the device server is not interrupted by
subsequent commands and no errors occur during processing of the self-test. The application client should
expect this time to increase significantly if other commands are sent to the logical unit while a self-test is in
progress or if errors occur during the processing of the self-test. Device servers supporting SELF-TEST CODE
field values other than 000b for the SEND DIAGNOSTIC command (see 6.42) shall support the EXTENDED
SELF-TEST COMPLETION TIME field. The EXTENDED SELF-TEST COMPLETION TIME field is not changeable. A value
of FFFFh indicates that the extended self-test takes 65 535 seconds or longer. If the value is FFFFh, then
refer to the EXTENDED SELF-TEST COMPLETION MINUTES field in the Extended INQUIRY Data VPD page(see
7.8.7).
Table 462 — AUTOLOAD MODE field
Code
Definition
000b
Medium shall be loaded for full access.
001b
Medium shall be loaded for medium auxiliary memory access only.
010b
Medium shall not be loaded.
011b to 111b
Reserved


7.5.9 Control Extension mode page
The Control Extension mode page (see table 463) is a subpage of the Control mode page (see 7.5.8) and
provides controls over SCSI features that are applicable to all device types. The mode page policy (see 7.5.2)
for this mode page shall be shared. If a field in this mode page is changed while there is a command already
in the task set, it is vendor specific whether the old or new value of the field applies to that command.
The PS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field shall be set as shown in table 463 for
the Control Extension mode page.
A SCSI precedence (SCSIP) bit set to one specifies that the timestamp changed using a SET TIMESTAMP
command (see 6.46) shall take precedence over methods outside the scope of this standard. A SCSIP bit set to
zero specifies that methods outside this standard may change the timestamp and that the SET TIMESTAMP
command is illegal.
A timestamp changeable by methods outside this standard (TCMOS) bit set to one specifies that the timestamp
may be initialized by methods outside the scope of this standard. A TCMOS bit set to zero specifies that the
timestamp shall not be changed by any method except those defined by this standard.
An implicit asymmetric logical unit access enabled (IALUAE) bit set to one specifies that implicitly managed
transitions between primary target port asymmetric access states (see 5.16.2) are allowed. An IALUAE bit set
to zero specifies that implicitly managed transitions between primary target port asymmetric access states be
disallowed and indicates that implicitly managed transitions between primary target port asymmetric access
states are disallowed or not supported.
The INITIAL COMMAND PRIORITY field specifies the priority that may be used as the command priority (see
SAM-5) for commands received by the logical unit on any I_T nexus (i.e., on any I_T_L nexus) where a priority
has not been modified by a SET PRIORITY command (see 6.44). If a MODE SELECT command specifies an
initial command priority value that is different than the current initial command priority, then the device server
shall set any priorities that have not be set with a SET PRIORITY command to a value different than the new
initial command priority value to the new priority. The device server shall establish a unit attention condition for
the initiator port associated with every I_T_L nexus that receives a new priority, with the additional sense code
set to PRIORITY CHANGED.
Table 463 — Control Extension mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (0Ah)
SUBPAGE CODE (01h)
 (MSB)
PAGE LENGTH (001Ch)
 (LSB)
Reserved
TCMOS
SCSIP
IALUAE
Reserved
INITIAL COMMAND PRIORITY
MAXIMUM SENSE DATA LENGTH
Reserved
•••
