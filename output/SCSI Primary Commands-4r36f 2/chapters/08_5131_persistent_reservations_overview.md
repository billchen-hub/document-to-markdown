# 5.13.1 Persistent Reservations overview

5.13 Reservations
5.13.1 Persistent Reservations overview
Reservations may be used to allow a device server to process commands from a selected set of I_T nexuses
(i.e., combinations of initiator ports accessing target ports) and reject commands from I_T nexuses outside the
selected set. The device server uniquely identifies I_T nexuses using protocol specific mechanisms.
Application clients may add or remove I_T nexuses from the selected set using reservation commands. If the
application clients do not cooperate in the reservation protocol, data may be unexpectedly modified and
deadlock conditions may occur.
The persistent reservations mechanism allows multiple application clients communicating through multiple I_T
nexuses to preserve reservation operations across SCSI initiator device failures, which usually involve logical
unit resets and involve I_T nexus losses. Persistent reservations persist across recovery actions. Persistent
reservations are not reset by hard reset, logical unit reset, or I_T nexus loss.
The persistent reservation held by a failing I_T nexus may be preempted by another I_T nexus as part of its
recovery process. Persistent reservations shall be retained by the device server until released, preempted, or
cleared by mechanisms defined in this standard. Optionally, persistent reservations may be retained if power
to the SCSI target device is removed.
The PERSISTENT RESERVE OUT and PERSISTENT RESERVE IN commands provide the basic
mechanism for dynamic contention resolution in systems with multiple initiator ports accessing a logical unit.
Before a persistent reservation may be established, the application client shall register a reservation key for
each I_T nexus with the device server. Reservation keys are necessary to allow:
a)
authentication of subsequent PERSISTENT RESERVE OUT commands;
b)
identification of other I_T nexuses that are registered;
c)
identification of the reservation key(s) that have an associated persistent reservation;
d)
preemption of a persistent reservation from a failing or uncooperative I_T nexus; and
e)
multiple I_T nexuses to participate in a persistent reservation.
The reservation key provides a method for the application client to associate a protocol-independent identifier
with a registered I_T nexus. The reservation key is used in the PERSISTENT RESERVE IN command to
identify which I_T nexuses are registered and which I_T nexus, if any, holds the persistent reservation. The
reservation key is used in the PERSISTENT RESERVE OUT command to register an I_T nexus, to verify the
I_T nexus being used for the PERSISTENT RESERVE OUT command is registered, and to specify which
registrations or persistent reservation to preempt.
Reservation key values may be used by application clients to identify registered I_T nexuses, using appli-
cation specific methods that are outside the scope of this standard. This standard provides the ability to
register no more than one reservation key per I_T nexus. Multiple initiator ports may use the same reservation
key value for a logical unit accessed through the same target ports. An initiator port may use the same reser-
vation key value for a logical unit accessed through different target ports. The logical unit shall maintain a
separate reservation key for each I_T nexus, regardless of the reservation key’s value.
An application client may register an I_T nexus with multiple logical units in a SCSI target device using any
combination of unique or duplicate reservation keys. These rules provide the ability for an application client to
preempt multiple I_T nexuses with a single PERSISTENT RESERVE OUT command, but they do not provide
the ability for the application client to uniquely identify the I_T nexuses using the PERSISTENT RESERVE
commands.


See table 213 in 6.16.2 for a list of PERSISTENT RESERVE OUT service actions. See table 201 in 6.15.1 for
a list of PERSISTENT RESERVE IN service actions.
The scope (see 6.15.3.3) of a persistent reservation shall be the entire logical unit.
The type (see 6.15.3.4) of a persistent reservation defines the selected set of I_T nexuses for which the
persistent reservation places restrictions on commands.
The details of which commands are allowed under what types of reservations are described in table 65.
In table 65 and table 66 the following key words are used:
allowed: Commands received from I_T nexuses not holding the reservation or from I_T nexuses not regis-
tered if a registrants only or all registrants type persistent reservation is present should complete normally.
conflict: Commands received from I_T nexuses not holding the reservation or from I_T nexuses not regis-
tered if a registrants only or all registrants type persistent reservation is present shall not be performed and
the device server shall complete the command with RESERVATION CONFLICT status.
Commands from I_T nexuses holding a reservation should complete normally. The behavior of commands
from registered I_T nexuses if a registrants only or all registrants type persistent reservation is present is
defined in table 65 and table 66.
A command shall be checked for reservation conflicts when processing of the command begins. After that
check succeeds, the command shall not be completed with RESERVATION CONFLICT status due to a
subsequent reservation.
The time at which a reservation is established with respect to other commands being managed by the device
server is vendor specific. Successful completion of a reservation command indicates that the new reservation
is established. A reservation may apply to some or all of the commands in the task set before the completion
of the reservation command. The reservation shall apply to all commands received by the device server after
successful completion of the reservation command. Any persistent reserve service action shall be performed
as a single indivisible event.
Multiple persistent reserve service actions may be present in the task set at the same time. The order of
processing of such service actions is defined by the task set management requirements defined in SAM-5, but
each is processed as a single indivisible command without any interleaving of actions that may be required by
other reservation commands.


For each command, this standard or a command standard defines the conditions that result in the command
being completed with RESERVATION CONFLICT. Command standards define the conditions either in the
device model or in the descriptions of each specific command.
Table 65 — SPC-4 commands that are allowed in the presence of various reservations (part 1 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T
nexus
From
registered
I_T nexus
(RR all
types)
From not registered
I_T nexus
Write
Excl
Excl
Access
Write Excl
RR
Excl Acc-
ess – RR
ACCESS CONTROL IN
Allowed
Allowed
Allowed
Allowed
Allowed
ACCESS CONTROL OUT
Allowed
Allowed
Allowed
Allowed
Allowed
CHANGE ALIASES
Conflict
Conflict
Allowed
Conflict
Conflict
COPY OPERATION ABORT
Conflict
Conflict
Allowed
Conflict
Conflict
EXTENDED COPY(LID4)
Conflict
Conflict
Allowed
Conflict
Conflict
EXTENDED COPY(LID1)
Conflict
Conflict
Allowed
Conflict
Conflict
INQUIRY
Allowed
Allowed
Allowed
Allowed
Allowed
LOG SELECT
Conflict
Conflict
Allowed
Conflict
Conflict
LOG SENSE
Allowed
Allowed
Allowed
Allowed
Allowed
MANAGEMENT PROTOCOL IN
Allowed
Conflict
Allowed
Allowed
Conflict
MANAGEMENT PROTOCOL OUT
Conflict
Conflict
Allowed
Conflict
Conflict
MODE SELECT(6) / MODE SELECT(10)
Conflict
Conflict
Allowed
Conflict
Conflict
MODE SENSE(6) / MODE SENSE(10)
Allowedb
Conflict
Allowed
Allowedb
Conflict
PERSISTENT RESERVE IN
Allowed
Allowed
Allowed
Allowed
Allowed
PERSISTENT RESERVE OUT
see table 66
READ ATTRIBUTE
Allowedb
Conflict
Allowed
Allowedb
Conflict
READ BUFFER
Allowedb
Conflict
Allowed
Allowedb
Conflict
READ MEDIA SERIAL NUMBER
Allowed
Allowed
Allowed
Allowed
Allowed
RECEIVE CREDENTIAL
Conflict
Conflict
Allowed
Conflict
Conflict
RECEIVE COPY DATA(LID4)
Allowed
Allowed
Allowed
Allowed
Allowed
RECEIVE COPY DATA(LID1)
Allowedb Allowedb
Allowed
Allowedb
Allowedb
Key: Excl=Exclusive, RR=Registrants Only or All Registrants
a Exceptions to the behavior of the RESERVE and RELEASE commands described in SPC-2 are
defined in 5.13.3.
b Logical units claiming compliance with previous versions of this standard (e.g., SPC-2, SPC-3) may
return RESERVATION CONFLICT status in this case. Logical units may report whether certain
commands are allowed in the ALLOW COMMANDS field of the parameter data returned by the
PERSISTENT RESERVE IN command with REPORT CAPABILITIES service action (see 6.15.4).


RECEIVE COPY OPERATING
PARAMETERS
Allowedb Allowedb
Allowed
Allowedb
Allowedb
RECEIVE COPY FAILURE
DETAILS(LID1)
Allowedb Allowedb
Allowed
Allowedb
Allowedb
RECEIVE COPY STATUS(LID4)
Allowed
Allowed
Allowed
Allowed
Allowed
RECEIVE COPY STATUS(LID1)
Allowedb Allowedb
Allowed
Allowedb
Allowedb
RECEIVE ROD TOKEN INFORMATION
Allowed
Allowed
Allowed
Allowed
Allowed
RECEIVE DIAGNOSTIC RESULTS
Allowedb
Conflict
Allowed
Allowedb
Conflict
RELEASE(6)/
RELEASE(10)
As defined in SPC-2 a
REMOVE I_T NEXUS
Conflict
Conflict
Allowed
Conflict
Conflict
REPORT ALIASES
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT ALL ROD TOKENS
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT IDENTIFYING INFORMATION
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT LUNS
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT PRIORITY
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT SUPPORTED OPERATION
CODES
Allowedb
Conflict
Allowed
Allowedb
Conflict
REPORT SUPPORTED TASK
MANAGEMENT FUNCTIONS
Allowedb
Conflict
Allowed
Allowedb
Conflict
REPORT TARGET PORT GROUPS
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT TIMESTAMP
Allowed
Allowed
Allowed
Allowed
Allowed
REQUEST SENSE
Allowed
Allowed
Allowed
Allowed
Allowed
RESERVE(6) / RESERVE(10)
As defined in SPC-2 a
SECURITY PROTOCOL IN
Allowed
Conflict
Allowed
Allowed
Conflict
SECURITY PROTOCOL OUT
Conflict
Conflict
Allowed
Conflict
Conflict
Table 65 — SPC-4 commands that are allowed in the presence of various reservations (part 2 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T
nexus
From
registered
I_T nexus
(RR all
types)
From not registered
I_T nexus
Write
Excl
Excl
Access
Write Excl
RR
Excl Acc-
ess – RR
Key: Excl=Exclusive, RR=Registrants Only or All Registrants
a Exceptions to the behavior of the RESERVE and RELEASE commands described in SPC-2 are
defined in 5.13.3.
b Logical units claiming compliance with previous versions of this standard (e.g., SPC-2, SPC-3) may
return RESERVATION CONFLICT status in this case. Logical units may report whether certain
commands are allowed in the ALLOW COMMANDS field of the parameter data returned by the
PERSISTENT RESERVE IN command with REPORT CAPABILITIES service action (see 6.15.4).


SEND DIAGNOSTIC
Conflict
Conflict
Allowed
Conflict
Conflict
SET IDENTIFYING INFORMATION
Conflict
Conflict
Allowed
Conflict
Conflict
SET PRIORITY
Conflict
Conflict
Allowed
Conflict
Conflict
SET TARGET PORT GROUPS
Conflict
Conflict
Allowed
Conflict
Conflict
SET TIMESTAMP
Conflict
Conflict
Allowed
Conflict
Conflict
TEST UNIT READY
Allowedb Allowedb
Allowed
Allowed b
Allowed b
WRITE ATTRIBUTE
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE BUFFER
Conflict
Conflict
Allowed
Conflict
Conflict
Table 65 — SPC-4 commands that are allowed in the presence of various reservations (part 3 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T
nexus
From
registered
I_T nexus
(RR all
types)
From not registered
I_T nexus
Write
Excl
Excl
Access
Write Excl
RR
Excl Acc-
ess – RR
Key: Excl=Exclusive, RR=Registrants Only or All Registrants
a Exceptions to the behavior of the RESERVE and RELEASE commands described in SPC-2 are
defined in 5.13.3.
b Logical units claiming compliance with previous versions of this standard (e.g., SPC-2, SPC-3) may
return RESERVATION CONFLICT status in this case. Logical units may report whether certain
commands are allowed in the ALLOW COMMANDS field of the parameter data returned by the
PERSISTENT RESERVE IN command with REPORT CAPABILITIES service action (see 6.15.4).


5.13.2 Third party persistent reservations
Except for all registrants type reservations, a reservation holder (see 5.13.10) may move the persistent reser-
vation to a third party (e.g., a copy manager supporting the EXTENDED COPY command) using the
REGISTER AND MOVE service action (see 5.13.8). A copy manager supporting the EXTENDED COPY
command may be instructed to move the persistent reservation to a specified I_T nexus using the third party
persistent reservations source I_T nexus segment descriptor (see 6.4.6.18).
5.13.3 Exceptions to SPC-2 RESERVE and RELEASE behavior
This subclause defines exceptions to the behavior of the RESERVE and RELEASE commands defined in
SPC-2. The RESERVE and RELEASE commands are obsolete in this standard, except for the behavior
defined in this subclause. Device servers that operate using the exceptions described in this subclause shall
set the CRH bit to one in the parameter data returned by the REPORT CAPABILITIES service action of the
PERSISTENT RESERVE IN command (see 6.15.4).
A RELEASE(6) or RELEASE(10) command shall complete with GOOD status, but the persistent reservation
shall not be released, if the command is received from:
a)
an I_T nexus that is a persistent reservation holder (see 5.13.10); or
b)
an I_T nexus that is registered if a registrants only or all registrants type persistent reservation is
present.
Table 66 — PERSISTENT RESERVE OUT service actions that are allowed in the presence of
various reservations
Service action
Addressed logical unit has a persistent
reservation held by another I_T nexus
Command is from
a registered
I_T nexus
Command is from
a not registered
I_T nexus
CLEAR
Allowed
Conflict
PREEMPT
Allowed
Conflict
PREEMPT AND ABORT
Allowed
Conflict
REGISTER
Allowed
Allowed
REGISTER AND IGNORE EXISTING KEY
Allowed
Allowed
REGISTER AND MOVE
Conflict
Conflict
RELEASE
Allowed a
Conflict
REPLACE LOST RESERVATION
Allowed b
Conflict b
RESERVE
Conflict
Conflict
a The reservation is not released (see 5.13.11.2.2).
b If the device server has detected that persistent reservation information has been
lost, then the command shall be processed as described in 5.13.5.3.
