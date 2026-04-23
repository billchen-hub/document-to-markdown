# 5.3.2 Suspending and resuming device-specific background functions

b)
may include regular, device specific self testing or saving of device specific data;
c)
may require the logical unit to be in a different power condition to be performed (e.g. a logical unit may
require being in the active power condition to access the medium for some functions);
d)
may be enabled or disabled via the EBF bit in the Informational Exceptions Control mode page (see
applicable command standard);
e)
shall be affected by the PERF bit and the LOGERR bit in the Informational Exceptions Control mode
page, if the background function is associated with informational exceptions;
f)
should be processed relative to power conditions based on the setting in the PM_BG_PRECEDENCE field
in the Power Condition mode page (see 7.5.13);
g)
may have impact on the SCSI target device’s performance (e.g., if a logical unit is performing a
background function, and the device server receives a command from an application client that
requires access to the logical unit, then the logical unit may take a short period of time (e.g., two
seconds) to suspend the background function before the logical unit is able to process the command);
h)
shall not affect power condition timers as defined in the Power Condition mode page;
i)
shall not affect timers defined in the Background Control mode page (see SBC-3); and
j)
shall have no negative impact on the reliability of the logical unit.
5.3.2 Suspending and resuming device-specific background functions
The SCSI target device shall suspend a device specific background function in progress if:
a)
any of the following are true:
A)
a command or task management function is processed that requires the device-specific
background function to be suspended; or
B)
a SCSI event (e.g., a reset event) (see SAM-5) occurs that requires the device-specific
background function to be suspended;
or
b)
all of the following are true:
A)
a power condition timer defined in the Power Condition mode page (see 7.5.13) expires;
B)
the PM_BG_PRECEDENCE field in the Power Condition mode page is set to 00b or 10b; and
C) the SCSI target device is unable to continue performing the device-specific background function
in the power condition associated with the timer that expired.
If a device-specific background function is suspended, the device server shall not stop any process that
causes a device-specific background function to be initiated (e.g., not stop any timers or counters associated
with device-specific background functions).
A suspended device specific background function may be resumed if:
a)
there are no commands in the task set to be processed;
b)
there are no task management functions to be processed;
c)
there are no SCSI events to be processed;
d)
no ACA condition (see SAM-5) exists;
e)
the PM_BG_PRECEDENCE field in the Power Condition mode page (see 7.5.13) is set to 00b or 10b; or
f)
the PM_BG_PRECEDENCE field in the Power Condition mode page is set to 10b, and no power condition
timer defined in the Power Condition mode page has expired.


5.4 Downloading and activating microcode
SCSI target device implementations may use microcode (e.g., firmware) that is stored in nonvolatile storage.
Microcode may be changeable by an application client using the WRITE BUFFER command (see 6.49). The
WRITE BUFFER command provides multiple methods for downloading microcode to the SCSI target device
and activating the microcode.
Downloading and activating microcode involves the following steps:
1)
Download: the application client transfers microcode from the Data-Out buffer to the device server in
one or more WRITE BUFFER commands;
2)
Save: after receiving the complete microcode, if defined by the download microcode mode, the
device server saves the microcode to nonvolatile storage; and
3)
Activate: after receiving the complete microcode and after saving it to nonvolatile storage if defined
by the download microcode mode, the SCSI target device begins using the new microcode for the first
time after an event defined by the download microcode mode.
After power on or hard reset, the SCSI target device shall use the last microcode that was saved to nonvolatile
storage.


Table 57 defines the WRITE BUFFER download microcode modes with respect to the steps described in this
subclause.
If microcode is activated due to processing a WRITE BUFFER command with a mode that causes activation
after processing (i.e., for modes 04h (see 6.49.5), 06h (see 6.49.7), and 0Fh (see 6.49.12)), the device server
shall establish a unit attention condition (see SAM-5) for the initiator port associated with every I_T nexus
except the I_T nexus on which the WRITE BUFFER command was received with the additional sense code
set to MICROCODE HAS BEEN CHANGED. The application client on the I_T nexus on which the WRITE
Table 57 — WRITE BUFFER download microcode modes
Mode
Down-
load a
Save b
Activate c
Download microcode and activate (i.e., 04h)
yes d
no
yes
Download microcode, save, and activate (i.e., 05h)
yes d
yes
optional
Download microcode with offsets and activate (i.e., 06h)
yes e
no
yes
Download microcode with offsets, save, and activate (i.e., 07h)
yes e
yes
optional
Download microcode with offsets, save, and defer activate (i.e., 0Eh) f
yes e
yes
no
Download microcode with offsets, select activation events, save, and
defer activate (i.e., 0Dh) f
yes e
yes
no
Activate deferred microcode (i.e., 0Fh) g
no
no
yes
a Entries in the Download column are as follows. For modes labeled yes, the application client delivers
microcode in the WRITE BUFFER command(s). For modes labeled no, the application client does not
deliver microcode with the WRITE BUFFER command.
b Entries in the Save column are as follows. For modes labeled yes, the device server shall save the
microcode to nonvolatile storage for use after each subsequent power on or hard reset, and shall not
return GOOD status for the final command in the WRITE BUFFER sequence (i.e., the series of WRITE
BUFFER commands that downloads the microcode) until the microcode has been saved. For modes
labeled no, the device server shall discard the microcode on the next power on or hard reset.
c Entries in the Activate column are as follows. For modes labeled yes, the device server shall activate
the microcode after completion of the final command in the WRITE BUFFER sequence (i.e., the series
of WRITE BUFFER commands that downloads the microcode and activates it). For modes labeled
optional, the device server may or may not activate the microcode image upon completion of the final
command in the WRITE BUFFER sequence. For modes labeled no, the device server shall not activate
the microcode upon completion of the final command in the WRITE BUFFER sequence.
d The application client delivers microcode in a vendor specific number of WRITE BUFFER commands
(i.e., a WRITE BUFFER sequence). The device server should require that the microcode be delivered in
a single command. The device server shall perform any required verification of the microcode prior to
returning GOOD status for the final WRITE BUFFER command in a sequence (i.e., the WRITE
BUFFER command delivering the last part of the microcode).
e The application client delivers microcode in one or more WRITE BUFFER commands, specifying a
buffer ID and buffer offset in each command. If the device server does not receive the necessary
WRITE BUFFER commands required to deliver the complete microcode before a logical unit reset
occurs, an I_T nexus loss occurs, or a WRITE BUFFER command specifying a different download
microcode mode is processed, the device server shall discard the new microcode. If the device server
determines that it is processing the final WRITE BUFFER command (i.e., the WRITE BUFFER
command delivering the last part of the microcode), it shall perform any required verification of the
microcode prior to returning GOOD status for the command.
f
Microcode downloaded with this mode is defined as deferred microcode.
g Support for mode 0Fh is mandatory if either mode 0Dh or mode 0Eh is supported.


BUFFER command was transferred should respond to GOOD status for the WRITE BUFFER command the
same way that it responds to a unit attention condition with an additional sense code set to MICROCODE
HAS BEEN CHANGED (e.g., assume a hard reset has occurred).
If microcode is activated due to processing a WRITE BUFFER command with a mode that optionally causes
activation after processing (i.e., for modes 05h (see 6.49.6) and 07h (see 6.49.8)), then the device server shall
establish a unit attention condition (see SAM-5) based on the setting of the ACTIVATE MICROCODE field in the
Extended INQUIRY VPD page (see 7.8.7).
If microcode is activated due to power on or hard reset, then the device server may establish a unit attention
condition (see SAM-5) for the initiator port associated with every I_T nexus with the additional sense code set
to MICROCODE HAS BEEN CHANGED in addition to the unit attention condition for the power on or hard
reset.
If deferred microcode (see table 57) is activated due to a command defined by its command standard as
causing deferred microcode to be activated (e.g., the FORMAT UNIT command and the START STOP UNIT
command in SBC-3), then the device server:
a)
shall establish a unit attention condition (see SAM-5) for the initiator port associated with every I_T
nexus with the additional sense code set to MICROCODE HAS BEEN CHANGED; and
b)
may establish other unit attention condition(s) as defined for the command (e.g., CAPACITY DATA
HAS CHANGED for the FORMAT UNIT command).
If new microcode is saved before deferred microcode is activated, then that deferred microcode is not
activated.
Table 58 summarizes how the WRITE BUFFER download microcode modes process the BUFFER ID field, the
BUFFER OFFSET field, and the PARAMETER LIST LENGTH field in the WRITE BUFFER CDB.
If the device server is unable to process a WRITE BUFFER command with a download microcode mode
because of a vendor specific condition (e.g., the device server requires the microcode be delivered in order,
and the BUFFER OFFSET field is not equal to the contents of the previous WRITE BUFFER command’s BUFFER
OFFSET field plus the contents of the previous WRITE BUFFER command’s PARAMETER LIST LENGTH field),
then the device server shall terminate the command with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to COMMAND SEQUENCE ERROR.
Table 58 — WRITE BUFFER download microcode field processing
Mode
BUFFER ID field, BUFFER OFFSET
field, and PARAMETER LIST
LENGTH field processing
Download microcode and activate (i.e., 04h)
vendor specific
Download microcode, save, and activate (i.e., 05h)
vendor specific
Download microcode with offsets and activate (i.e., 06h)
6.49.7
Download microcode with offsets, save, and activate (i.e., 07h)
6.49.7
Download microcode with offsets, select activation events, save, and
defer activate (i.e., 0Dh)
6.49.7 and 6.49.10
Download microcode with offsets, save, and defer activate (i.e., 0Eh)
6.49.7
Activate deferred microcode (i.e., 0Fh)
ignored


If the device server detects a digital signature validation failure while processing a WRITE BUFFER command
that downloads microcode, it shall terminate the command with CHECK CONDITION status, with the sense
key set to ABORTED COMMAND, and the additional sense code set to DIGITAL SIGNATURE VALIDATION
FAILURE.
The MULTI I_T NEXUS MICROCODE DOWNLOAD field (see table 57) in the Extended INQUIRY Data VPD page
(see 7.8.7) indicates how the device server handles concurrent attempts to download microcode using the
WRITE BUFFER command download microcode modes from multiple I_T nexuses.
Table 59 — MULTI I_T NEXUS MICROCODE DOWNLOAD field (part 1 of 2)
Code
Description
0h
The handling of concurrent WRITE BUFFER download microcode operations from
multiple I_T nexus is vendor specific.
1h
For modes that download microcode (see table 57), the device server shall:
a)
if a WRITE BUFFER command with the BUFFER OFFSET field set to zero is
received on any I_T nexus, the command shall be processed as described
elsewhere in this subclause. This shall establish the I_T nexus for the WRITE
BUFFER sequence, and cause any microcode downloaded on another I_T nexus
to be discarded;
b)
if a WRITE BUFFER command with the BUFFER OFFSET field set to a non-zero
value is received on the established I_T nexus for the WRITE BUFFER
sequence, the command shall be processed as described elsewhere in this
subclause; and
c)
if a WRITE BUFFER command with the BUFFER OFFSET field set to a non-zero
value is received on an I_T nexus that is different from the established I_T nexus
for the WRITE BUFFER sequence, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and
the additional sense code set to COMMAND SEQUENCE ERROR.
If a WRITE BUFFER command with mode 0Fh (i.e., activate deferred microcode) is
received on an I_T nexus that is different from the established I_T nexus for the WRITE
BUFFER sequence, then the device server shall terminate the WRITE BUFFER
command with mode 0Fh with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to COMMAND SEQUENCE
ERROR. Any deferred microcode shall not be invalidated.
2h
For modes that download microcode (see table 57), the device server shall allow con-
current sequences of WRITE BUFFER commands to be processed as described else-
where in this subclause on more than one I_T nexus.
If a WRITE BUFFER command with mode 0Fh (i.e., activate deferred microcode) is
received on an I_T nexus that is different from the established I_T nexus for the WRITE
BUFFER sequence, then the device server shall process the command as described
elsewhere in this subclause.


For all WRITE BUFFER command modes that download microcode (see table 57), the COMMAND SPECIFIC
field (see 6.35.4.2) located in the command timeouts descriptor of the parameter data returned by the
REPORT SUPPORTED OPERATION CODES command (see 6.35) indicates the maximum time that access
to the SCSI device is limited or not possible through any SCSI ports associated with a logical unit that
processes a WRITE BUFFER command that activates microcode.
5.5 Error history
5.5.1 Error history overview
Error history is optional data collected by a logical unit to aid in troubleshooting errors.
The READ BUFFER command (see 6.18.9) provides a method for retrieving error history from the logical unit
(see 5.5.2).
The WRITE BUFFER command (see 6.49.15) provides a method for inserting application client error history
into the error history (see 5.5.3) and for clearing the error history (see 5.5.4).
The format of the application client error history is defined by the manufacturer of the application client. The
format of the error history, including how the application client error history, if any, is incorporated into the error
history, is defined by the manufacturer of the logical unit.
3h
For modes that download microcode (see table 57), the device server shall:
a)
if a WRITE BUFFER command with the BUFFER OFFSET field set to zero is
received on any I_T nexus, the command shall be processed as described
elsewhere in this subclause. This shall establish the I_T nexus for the WRITE
BUFFER sequence, and cause any microcode downloaded on another I_T nexus
to be discarded;
b)
if a WRITE BUFFER command with the BUFFER OFFSET field set to a non-zero
value is received on the established I_T nexus for the WRITE BUFFER
sequence, the command shall be processed as described elsewhere in this
subclause; and
c)
if a WRITE BUFFER command with the BUFFER OFFSET field set to a non-zero
value is received on an I_T nexus that is different from the established I_T nexus
for the WRITE BUFFER sequence, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and
the additional sense code set to COMMAND SEQUENCE ERROR.
If a WRITE BUFFER command with mode 0Fh (i.e., activate deferred microcode) is
received on an I_T nexus that is different from the established I_T nexus for the WRITE
BUFFER sequence, then the device server shall process the command as described
elsewhere in this subclause.
4h to Fh
Reserved
Table 59 — MULTI I_T NEXUS MICROCODE DOWNLOAD field (part 2 of 2)
Code
Description
