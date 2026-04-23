# 6.13.6 Initial responses

6.13.3 Changeable values
A PC field value of 01b requests that the device server return a mask denoting those mode parameters that
are changeable. In the mask, the bits in the fields of the mode parameters that are changeable all shall be set
to one and the bits in the fields of the mode parameters that are non-changeable (i.e., defined by the logical
unit) all shall be set to zero.
If the logical unit does not implement changeable parameters mode pages and the device server receives a
MODE SENSE command with 01b in the PC field, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB.
An attempt to change a non-changeable mode parameter using the MODE SELECT command shall result in
an error condition (see 6.11).
The application client should issue a MODE SENSE command with the PC field set to 01b and the PAGE CODE
field set to 3Fh to determine which mode pages are supported, which mode parameters within the mode
pages are changeable, and the supported length of each mode page prior to issuing any MODE SELECT
commands.
6.13.4 Default values
A PC field value of 10b requests that the device server return the default values of the mode parameters.
Unsupported parameters shall be set to zero. Default values should be accessible even if the logical unit is not
ready.
6.13.5 Saved values
A PC field value of 11b requests that the device server return the saved values of the mode parameters. Mode
parameters not supported by the logical unit shall be set to zero. If saved values are not implemented, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to SAVING PARAMETERS NOT SUPPORTED.
The method of saving parameters is vendor specific. The parameters are preserved in such a manner that
they are retained while the device is powered down. All saveable mode pages should be considered saved if
a MODE SELECT command issued with the SP bit set to one has completed with a GOOD status or after the
successful completion of a FORMAT UNIT command.
6.13.6 Initial responses
After a logical unit reset, the device server shall respond in the following manner:
a)
if default values are requested, report the default values;
b)
if saved values are requested, report valid restored mode parameters, or restore the mode param-
eters and report them. If the saved values of the mode parameters are not able to be accessed from
the nonvolatile vendor specific location, the command shall be terminated with CHECK CONDITION
status, with the sense key set to NOT READY. If saved parameters are not implemented, respond as
defined in 6.13.5; or
c)
if current values are requested and the current values have been sent by the application client via a
MODE SELECT command, the current values shall be returned. If the current values have not been
sent, the device server shall return:


A)
the saved values, if saving is implemented and saved values are available; or
B)
the default values.
6.14 MODE SENSE(10) command
The MODE SENSE(10) command (see table 199) provides a means for a device server to report parameters
to an application client. It is a complementary command to the MODE SELECT(10) command. Device servers
that implement the MODE SENSE(10) command shall also implement the MODE SELECT(10) command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 199 for the MODE
SENSE(10) command.
If the Long LBA Accepted (LLBAA) bit is set to one, the device server is allowed to return parameter data with
the LONGLBA bit equal to one (see 7.5.5). If LLBAA bit is set to zero, the LONGLBA bit shall be zero in the
parameter data returned by the device server.
The CONTROL byte is defined in SAM-5.
See the MODE SENSE(6) command (6.13) for a description of the other fields and operation of this
command.
Table 199 — MODE SENSE(10) command
Bit
Byte
OPERATION CODE (5Ah)
Reserved
LLBAA
DBD
Reserved
PC
PAGE CODE
SUBPAGE CODE
Reserved

•••
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL


6.15 PERSISTENT RESERVE IN command
6.15.1 PERSISTENT RESERVE IN command introduction
The PERSISTENT RESERVE IN command (see table 200) requests that the device server return information
about persistent reservations and reservation keys (i.e., registrations) that are active within a device server.
This command is used in conjunction with the PERSISTENT RESERVE OUT command (see 6.16).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 200 for the PERSISTENT
RESERVE IN command.
The SERVICE ACTION field is defined in 4.2.5.2. The service action codes for the PERSISTENT RESERVE IN
command are defined in table 201.
The ALLOCATION LENGTH field is defined in 4.2.5.6. The PERSISTENT RESERVE IN parameter data includes a
length field that indicates the number of parameter data bytes that follow in the parameter data. The allocation
length should be set to a value large enough to include the length field for the specified service action.
The CONTROL byte is defined in SAM-5.
Table 200 — PERSISTENT RESERVE IN command
Bit
Byte
OPERATION CODE (5Eh)
Reserved
SERVICE ACTION
Reserved

•••
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL
Table 201 — PERSISTENT RESERVE IN service action codes
Code
Name
Description
Reference
00h
READ KEYS
Reads all registered reservation keys
(i.e., registrations) as described in
5.13.6.2
6.15.2
01h
READ RESERVATION
Reads the current persistent reservations
as described in 5.13.6.3
6.15.3
02h
REPORT CAPABILITIES
Returns capability information
6.15.4
03h
READ FULL STATUS
Reads complete information about
all registrations and the persistent
reservations, if any
6.15.5
04h to 1Fh
Reserved
Reserved


6.15.2 READ KEYS service action
The READ KEYS service action requests that the device server return a parameter list containing a header
and a list of each currently registered I_T nexus’ reservation key. If multiple I_T nexuses have registered with
the same key, then that key value shall be listed multiple times, once for each such registration.
For more information on READ KEYS see 5.13.6.2.
The format for the parameter data provided in response to a PERSISTENT RESERVE IN command with the
READ KEYS service action is shown in table 202.
The Persistent Reservations Generation (PRGENERATION) field shall contain the value of a 32-bit wrapping
counter maintained by the device server that shall be incremented every time a PERSISTENT RESERVE
OUT command requests a REGISTER service action, a REGISTER AND IGNORE EXISTING KEY service
action, a REGISTER AND MOVE service action, a CLEAR service action, a PREEMPT service action, or a
PREEMPT AND ABORT service action. The counter shall not be incremented by a PERSISTENT RESERVE
IN command, by a PERSISTENT RESERVE OUT command that performs a RESERVE or RELEASE service
action, or by a PERSISTENT RESERVE OUT command that is terminated due to an error or reservation
conflict. Regardless of the APTPL bit value the PRgeneration value shall be set to zero by a power on.
The ADDITIONAL LENGTH field indicates the number of bytes in the Reservation key list. The contents of the
ADDITIONAL LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The reservation key list contains the 8-byte reservation keys for all I_T nexuses that have been registered
(see 5.13.7).
Table 202 — PERSISTENT RESERVE IN parameter data for READ KEYS
Bit
Byte
(MSB)
PRGENERATION
•••
(LSB)
(MSB)
ADDITIONAL LENGTH (n-7)
•••
(LSB)
Reservation key list
(MSB)
Reservation key [first]
•••
(LSB)
•••
n-7
(MSB)
Reservation key [last]
•••
n
(LSB)
