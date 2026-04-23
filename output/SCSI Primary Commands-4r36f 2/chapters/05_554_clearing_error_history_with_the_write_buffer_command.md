# 5.5.4 Clearing error history with the WRITE BUFFER command

5.5.3 Adding application client error history with the WRITE BUFFER command
An application client adds application client detected error history to the error history collected by a logical unit
by sending a WRITE BUFFER command. The application client error history may be recovered as part of the
error history (see 5.5.2) or by means outside the scope of this standard and is not used for any logical unit
related error recovery.
Error history that contains a mix of application client error history and logical unit error history may be used to
correlate an application client-detected error with errors detected internally by the logical unit.
Application clients should minimize the amount of error history they store to prevent error history overflows
(see 6.49.15).
5.5.4 Clearing error history with the WRITE BUFFER command
An application client clears the portions of the error history that the device server allows to be cleared by
sending a WRITE BUFFER command (see 6.49.15) with:
a)
the MODE field set to 1Ch (i.e., download error history);
b)
the BUFFER OFFSET field set to any value allowed by 6.49.15 (e.g., 000000h);
c)
the PARAMETER LIST LENGTH field set to 00001Ah;
d)
in the parameter list, the CLR bit set to one; and
e)
all other fields in the parameter list as 6.49.15 allows.
Clearing error history shall not:
a)
clear the error history I_T nexus, if any, if it was created with the READ BUFFER command (see
5.5.2); or
b)
release the error history snapshot, if any, if it was created with the READ BUFFER command (see
5.5.2).


5.6 Identifying information
The REPORT IDENTIFYING INFORMATION command (see 6.32) and SET IDENTIFYING INFORMATION
command (see 6.43) allow an application client to maintain one or more sets of identifying information
associated with the peripheral device.
Identifying information shall persist through power cycles (i.e., be stored in non-volatile storage), hard resets,
logical unit resets, I_T nexus losses, media format operations, and media replacement.
Table 60 defines the identifying information types.
Identifying information is changed by:
a)
the SET IDENTIFYING INFORMATION command; or
b)
a mechanism outside the scope of this standard (e.g., a system administrator may be able to change
identifying information through a management interface).
If a mechanism outside the scope of this standard changes the identifying information, then the device server
shall establish a unit attention condition for the initiator port associated with every I_T nexus with the
additional sense code set to DEVICE IDENTIFIER CHANGED.
5.7 Medium auxiliary memory
Some types of media, especially removable media, include a non-volatile memory referred to as MAM
(medium auxiliary memory). Medium auxiliary memory is used to store data describing the media and its
contents. This standard supports medium auxiliary memory with the READ ATTRIBUTE command (see 6.17)
and the WRITE ATTRIBUTE command (see 6.48). These commands are used to retrieve and store infor-
mation in the medium auxiliary memory in the form of MAM attributes.
A MAM attribute is represented in a format described in 7.4.
Table 60 — Identifying information types
Code
Description
Length
Support a
0000000b
Peripheral device identifying information – a value
describing the peripheral device (e.g., an operat-
ing system volume label).
0 to 64 bytes
Mandatory
65 to 512 bytes
Optional
0000010b
Peripheral device text identifying information – a
null-terminated (see 4.3.2) UTF-8 format string
providing an informational description of the
peripheral device (e.g., a descriptive string
entered by a system administrator).
0 to 256 bytes
Optional
xxxxxx1b
Restricted (see SCC-2)
All other values
Reserved
a These support requirements shall apply only if the REPORT IDENTIFYING INFORMATION
command and/or SET IDENTIFYING INFORMATION command are implemented.


There are three types of MAM attributes (see table 61).
Depending on that attribute type, MAM attributes have the states shown in table 62.
5.8 Multiple target port and initiator port behavior
SAM-5 specifies the behavior of logical units being accessed by application clients through more than one
initiator port and/or through more than one target port. Additional initiator ports and target ports allow the
definition of multiple I_T nexuses through which the device server may be reached. Multiple I_T nexuses may
be used to improve the availability of logical units in the presence of certain types of failures and to improve
the performance between an application client and logical unit when some I_T nexuses may be busy.
Table 61 — Types of MAM attributes
Attribute
Type
Attribute Source
Example
Readable
with READ
ATTRIBUTE
Writable
with WRITE
ATTRIBUTE
Medium
Permanently stored in the medium
auxiliary memory during manufacture.
Media Serial
Number
Yes
No
Device
Maintained by the device server.
Load Count
Yes
No
Host
Maintained by the application client.
Backup Date
Yes
Yes
Table 62 — MAM attribute states
Attribute
Type
Attribute State
Description
Medium
or
Device
Read Only
An application client may read the contents of the MAM attribute with the
READ ATTRIBUTE command, but an attempt to clear or change the MAM
attribute using the WRITE ATTRIBUTE command shall result in the device
server terminating the command with CHECK CONDITION status. If the
READ ONLY bit (see 7.4.1) is set to one, the attribute is in the read only state.
Unsupported
The device server does not support the MAM attribute and shall not return it
in response to a READ ATTRIBUTE command.
Unavailable
The MAM attribute exists but it is not available at this time. The device
server shall not return it in response to a READ ATTRIBUTE command.
Host
Nonexistent
A host attribute does not exist in the medium auxiliary memory until a
WRITE ATTRIBUTE command creates it.
Read/Write
The MAM attribute has been created using the WRITE ATTRIBUTE
command. After the MAM attribute has been created, the contents may be
altered using subsequent WRITE ATTRIBUTE commands. A read/write
MAM attribute may be returned to the nonexistent state using a WRITE
ATTRIBUTE command with the attribute length set to zero. If the READ ONLY
bit (see 7.4.1) is set to zero, the MAM attribute is in the read/write state.
Unsupported
The device server does not support the MAM attribute and shall not return it
in response to a READ ATTRIBUTE command.


If one target port is being used by an initiator port, accesses attempted through other target port(s) may:
a)
receive a status of BUSY; or
b)
be accepted as if the other target port(s) were not in use.
The device server shall indicate the presence of multiple target ports by setting the MULTIP bit to one in its
standard INQUIRY data.
Only the following operations allow one I_T nexus to interact with the commands of other I_T nexuses:
a)
the PERSISTENT RESERVE OUT with PREEMPT service action preempts persistent reservations
(see 5.13.11.2.4);
b)
the PERSISTENT RESERVE OUT with PREEMPT AND ABORT service action preempts and aborts
persistent reservations (see 5.13.11.2.6);
c)
The PERSISTENT RESERVE OUT with CLEAR service action releases persistent reservations for all
I_T nexuses (see 5.13.11.2.7); and
d)
commands and task management functions that allow one I_T nexus to abort commands received on
a different I_T nexus (see SAM-5).
5.9 Parameter rounding
Certain parameters sent to a device server with various commands contain a range of values. Device servers
may choose to implement only selected values from this range. If the device server receives a value that it
does not support, the device server shall:
a)
terminate the command (e.g., by returning CHECK CONDITION status with ILLEGAL REQUEST
sense key); or
b)
round the value received to a supported value.
If parameter rounding is implemented, a device server that receives a parameter value that is not an exact
supported value shall adjust the value to one that it supports and shall return CHECK CONDITION status, with
the sense key set to RECOVERED ERROR, and the additional sense code set to ROUNDED PARAMETER.
The application client should send an appropriate command to learn what value the device server has
selected.
The device server shall reject unsupported values unless rounding is permitted in the description of the
parameter. When the description of a parameter states that rounding is permitted, the device server should
adjust maximum-value fields down to the next lower supported value than the one specified by the application
client. Minimum-value fields should be rounded up to the next higher supported value than the one specified
by the application client. In some cases, the type of rounding (i.e., up or down) is described in the definition of
the parameter.
5.10 Parsing variable-length parameter lists and parameter data
Parameter lists and parameter data (e.g., diagnostic pages, mode pages, log pages, and VPD pages) often
include length fields indicating the size of the parameter list or parameter data (e.g., the MODE DATA LENGTH
field in the mode parameter header (see 7.5.5)). Parameter lists and parameter data often include descriptor
lists and descriptor length fields containing the length of the descriptors in the descriptor lists (e.g., the DESIG-
NATOR LENGTH field in the designation descriptor used in the Device Identification VPD page (see 7.8.6.1)).
