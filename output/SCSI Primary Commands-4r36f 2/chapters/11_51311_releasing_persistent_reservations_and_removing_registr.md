# 5.13.11 Releasing persistent reservations and removing registrations

5.13.11 Releasing persistent reservations and removing registrations
5.13.11.1 Overview
The application client may use service actions to:
a)
release persistent reservations and remove registrations (see 5.13.11.2); and
b)
begin the process of recovering from lost reservation information, if any (see 5.13.5.3 and 5.13.11.3).
5.13.11.2 Service actions that release persistent reservations and remove registrations
5.13.11.2.1 Overview
An application client may release or preempt the persistent reservation by issuing one of the following
commands through a registered I_T nexus with the RESERVATION KEY field set to the reservation key value that
is registered with the logical unit for that I_T nexus:
a)
a PERSISTENT RESERVE OUT command with RELEASE service action from a persistent reser-
vation holder (see 5.13.11.2.2);
b)
a PERSISTENT RESERVE OUT command with PREEMPT service action specifying the reservation
key of the persistent reservation holder or holders (see 5.13.11.2.4);
c)
a PERSISTENT RESERVE OUT command with PREEMPT AND ABORT service action specifying
the reservation key of the persistent reservation holder or holders (see 5.13.11.2.6);
d)
a PERSISTENT RESERVE OUT command with CLEAR service action (see 5.13.11.2.7); or
e)
if the I_T nexus is the persistent reservation holder and the persistent reservation is not an all regis-
trants type, then a PERSISTENT RESERVE OUT command with REGISTER service action or
REGISTER AND IGNORE EXISTING KEY service action with the SERVICE ACTION RESERVATION KEY
field set to zero (see 5.13.11.2.3).
Table 71 defines processing for a persistent reservation released or preempted by an application client based
on the reservation type.
An application client may remove registrations by issuing one of the following commands through a registered
I_T nexus with the RESERVATION KEY field set to the reservation key value that is registered with the logical unit
for that I_T nexus:
a)
a PERSISTENT RESERVE OUT command with PREEMPT service action with the SERVICE ACTION
RESERVATION KEY field set to the reservation key (see 5.13.11.2.4) to be removed;
Table 71 — Processing for a released or preempted persistent reservation
Reservation Type
Processing
Write Exclusive – Registrants Only or
Exclusive Access – Registrants Only
This persistent reservation shall be released if the persis-
tent reservation holder (see 5.13.10) of this reservation
type becomes unregistered.
Write Exclusive – All Registrants or
Exclusive Access – All Registrants
This persistent reservation shall be released if:
a)
the registration for the last registered I_T nexus
is removed; or
b)
the type or scope is changed.
Write Exclusive or Exclusive Access
This persistent reservation shall be released if the persis-
tent reservation holder (see 5.13.10) of this reservation
type becomes unregistered.


b)
a PERSISTENT RESERVE OUT command with PREEMPT AND ABORT service action with the
SERVICE ACTION RESERVATION KEY field set to the reservation key (see 5.13.11.2.6) to be removed;
c)
a PERSISTENT RESERVE OUT command with CLEAR service action (see 5.13.11.2.7); or
d)
a PERSISTENT RESERVE OUT command with REGISTER service action or REGISTER AND
IGNORE EXISTING KEY service action with the SERVICE ACTION RESERVATION KEY field set to zero
(see 5.13.11.2.3).
After a reservation key (i.e., registration) has been removed, no information shall be reported for that unregis-
tered I_T nexus in subsequent READ KEYS service actions until the I_T nexus is registered again (see
5.13.7).
If the persist through power loss capability is not enabled, loss of power also causes persistent reservations to
be released and registrations to be removed. If the most recent APTPL value received by the device server is
zero (see 6.16.3), a power cycle:
a)
releases all persistent reservations; and
b)
removes all registered reservation keys (see 5.13.7).
5.13.11.2.2 Releasing
Only the persistent reservation holder (see 5.13.10) is allowed to release a persistent reservation.
An application client releases the persistent reservation by issuing a PERSISTENT RESERVE OUT
command with RELEASE service action through an I_T nexus that is a persistent reservation holder with the
following parameters:
a)
RESERVATION KEY field set to the value of the reservation key that is registered with the logical unit for
the I_T nexus; and
b)
TYPE field and SCOPE field set to match the persistent reservation being released.
In response to a persistent reservation release request from the persistent reservation holder the device
server shall perform a release by doing the following as an uninterrupted series of actions:
a)
release the persistent reservation;
b)
not remove any registration(s);
c)
if the NUAR bit (see 7.5.8) is set to zero and the released persistent reservation is either a registrants
only type or an all registrants type persistent reservation, then the device server shall establish a unit
attention condition for the initiator port associated with every registered I_T nexus other than I_T
nexus on which the PERSISTENT RESERVE OUT command with RELEASE service action was
received, with the additional sense code set to RESERVATIONS RELEASED;
d)
if the NUAR bit is set to one and the released persistent reservation is either a registrants only type or
an all registrants type persistent reservation, then the device server shall not establish a unit attention
condition; and
e)
if the persistent reservation is of any other type, the device server shall not establish a unit attention
condition.
The established persistent reservation shall not be altered and the device server shall terminate the command
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID RELEASE OF PERSISTENT RESERVATION, for a PERSISTENT RESERVE OUT
command that specifies the release of a persistent reservation if:
a)
the requesting I_T nexus is a persistent reservation holder (see 5.13.10); and
b)
the SCOPE and TYPE fields do not match the scope and type of the established persistent reservation.


If there is no persistent reservation or in response to a persistent reservation release request from a regis-
tered I_T nexus that is not a persistent reservation holder (see 5.13.10), the device server shall do the
following:
a)
not release the persistent reservation, if any;
b)
not remove any registrations; and
c)
complete the command with GOOD status.
5.13.11.2.3 Unregistering
An application client may remove a registration for an I_T nexus by issuing a PERSISTENT RESERVE OUT
command with REGISTER service action or a REGISTER AND IGNORE EXISTING KEY service action with
the SERVICE ACTION RESERVATION KEY field set to zero through that I_T nexus.
If the I_T nexus is a reservation holder, the persistent reservation is of an all registrants type, and the I_T
nexus is the last remaining registered I_T nexus, then the device server shall also release the persistent
reservation.
If the I_T nexus is the reservation holder and the persistent reservation is of a type other than all registrants,
the device server shall also release the persistent reservation. If the persistent reservation is a registrants only
type, the device server shall establish a unit attention condition for the initiator port associated with every
registered I_T nexus except for the I_T nexus on which the PERSISTENT RESERVE OUT command was
received, with the additional sense code set to RESERVATIONS RELEASED.


5.13.11.2.4 Preempting
5.13.11.2.4.1 Overview
A PERSISTENT RESERVE OUT command with PREEMPT service action or PREEMPT AND ABORT
service action is used to:
a)
preempt (i.e., replace) the persistent reservation and remove registrations (see 5.13.11.2.4.3); or
b)
remove registrations (see 5.13.11.2.5).
Table 72 lists the actions taken based on the current persistent reservation type and the SERVICE ACTION
RESERVATION KEY field in the PERSISTENT RESERVE OUT command.
See figure 9 for a description of how a device server interprets a PREEMPT service action to determine its
actions (e.g., preempt the persistent reservation, remove registration, or both preempt the persistent reser-
vation and remove registration).
Table 72 — Preempting actions
Reservation
Type
Service Action
Reservation Key
Action
Reference
All Registrants
Zero
Preempt the persistent reservation and
remove registrations.
5.13.11.2.4.
Not Zero
Remove registrations.
5.13.11.2.5
All other types
Zero
Terminate the command with CHECK CONDI-
TION status, with the sense key set to ILLE-
GAL REQUEST, and the additional sense code
set to INVALID FIELD IN PARAMETER LIST.
Reservation holder’s
reservation key
Preempt the persistent reservation and
remove registrations.
5.13.11.2.4.
Any other, non-zero
reservation key
Remove registrations.
5.13.11.2.5


Figure 9 — Device server interpretation of PREEMPT service action
Requesting
I_T nexus
registered?
Existing
persistent
reservation?
PREEMPT service action
a) Remove registrations pointed to by
the SERVICE ACTION RESERVATION KEY
b) Release persistent reservation
c) Create persistent reservation using
    new type and scope
Remove registrations
pointed to by the SERVICE
ACTION RESERVATION KEY
RESERVATION
CONFLICT
status
Done
SERVICE ACTION
RESERVATION KEY
matches reservation key
of the persistent reser-
vation holder?
Done
Done
No
No
Valid
RESERVATION
KEY & SERVICE ACTION
RESERVATION
KEY?
All
Registrants
persistent
reservation?
Yes
Yes
No
No
Yes
No
SERVICE ACTION
RESERVATION KEY
is zero?
a) Remove all other registrations
b) Release persistent reservation
c) Create persistent reservation
    using new type and scope
No
Yes
Yes
No
Yes
SERVICE ACTION
RESERVATION KEY
is zero?
ILLEGAL
REQUEST
sense key
Yes
Done
Remove registrations
pointed to by the SERVICE
ACTION RESERVATION KEY


5.13.11.2.4.2 Failed persistent reservation preempt
If the preempting I_T nexus’ PREEMPT service action or PREEMPT AND ABORT service action fails (e.g.,
repeated TASK SET FULL status, repeated BUSY status, SCSI transport protocol time-out, or time-out due to
the task set being blocked due to failed initiator port or failed SCSI initiator device), the application client may
send a LOGICAL UNIT RESET task management function to the failing logical unit to remove blocking
commands and then resend the preempting service action.
5.13.11.2.4.3 Preempting persistent reservations and registration handling
An application client may preempt the persistent reservation with another persistent reservation by issuing a
PERSISTENT RESERVE OUT command with PREEMPT service action or PREEMPT AND ABORT service
action through a registered I_T nexus with the following parameters:
a)
RESERVATION KEY field set to the value of the reservation key that is registered with the logical unit for
the I_T nexus;
b)
SERVICE ACTION RESERVATION KEY field set to the value of the reservation key of the persistent reser-
vation to be preempted; and
c)
TYPE field and SCOPE field set to define a new persistent reservation. The SCOPE and TYPE of the
persistent reservation created by the preempting I_T nexus may be different than those of the
persistent reservation being preempted.
If the SERVICE ACTION RESERVATION KEY field identifies a persistent reservation holder (see 5.13.10), the device
server shall perform a preempt by doing the following as an uninterrupted series of actions:
a)
release the persistent reservation for the holder identified by the SERVICE ACTION RESERVATION KEY
field;
b)
remove the registrations for all I_T nexuses identified by the SERVICE ACTION RESERVATION KEY field,
except the I_T nexus that is being used for the PERSISTENT RESERVE OUT command. If an all
registrants persistent reservation is present and the SERVICE ACTION RESERVATION KEY field is set to
zero, then all registrations shall be removed except for that of the I_T nexus that is being used for the
PERSISTENT RESERVE OUT command;
c)
establish a persistent reservation for the preempting I_T nexus using the contents of the SCOPE and
TYPE fields;
d)
process commands as defined in 5.13.1;
e)
establish a unit attention condition for the initiator port associated with every I_T nexus that lost its
persistent reservation and/or registration, with the additional sense code set to REGISTRATIONS
PREEMPTED; and
f)
if the type or scope has changed, then for every I_T nexus whose reservation key was not removed,
except for the I_T nexus on which the PERSISTENT RESERVE OUT command was received, the
device server shall establish a unit attention condition for the initiator port associated with that I_T
nexus, with the additional sense code set to RESERVATIONS RELEASED. If the type or scope have
not changed, then no unit attention condition(s) shall be established for this reason.
After the PERSISTENT RESERVE OUT command has been completed with GOOD status, new commands
are subject to the persistent reservation restrictions established by the preempting I_T nexus.


The following commands shall be subjected in a vendor specific manner either to the restrictions established
by the persistent reservation being preempted or to the restrictions established by the preempting I_T nexus:
a)
a command received after the arrival, but before the completion of the PERSISTENT RESERVE OUT
command with the PREEMPT service action or the PREEMPT AND ABORT service action; or
b)
a command in the dormant command state, blocked command state, or enabled command state (see
SAM-5) at the time the PERSISTENT RESERVE OUT command with the PREEMPT service action or
the PREEMPT AND ABORT service action is received.
Completion status shall be returned for each command unless it was aborted by a PERSISTENT RESERVE
OUT command with the PREEMPT AND ABORT service action and TAS bit set to zero in the Control mode
page (see 7.5.8).
If an all registrants persistent reservation is not present, it is not an error for the persistent reservation holder
to preempt itself (i.e., a PERSISTENT RESERVE OUT with a PREEMPT service action or a PREEMPT AND
ABORT service action with the SERVICE ACTION RESERVATION KEY value equal to the persistent reservation
holder’s reservation key that is received from the persistent reservation holder). In that case, the device server
shall establish the new persistent reservation and maintain the registration.
5.13.11.2.5 Removing registrations
If a registered reservation key does not identify a persistent reservation holder (see 5.13.10), an application
client may remove the registration(s) without affecting any persistent reservations by issuing a PERSISTENT
RESERVE OUT command with PREEMPT service action through a registered I_T nexus with the following
parameters:
a)
RESERVATION KEY field set to the value of the reservation key that is registered for the I_T nexus; and
b)
SERVICE ACTION RESERVATION KEY field set to match the reservation key of the registration or registra-
tions being removed.
If the SERVICE ACTION RESERVATION KEY field does not identify a persistent reservation holder or there is no
persistent reservation holder (i.e., there is no persistent reservation), then the device server shall perform a
preempt by doing the following in an uninterrupted series of actions:
a)
remove the registrations for all I_T nexuses specified by the SERVICE ACTION RESERVATION KEY field;
b)
ignore the contents of the SCOPE and TYPE fields;
c)
process commands as defined in 5.13.1; and
d)
establish a unit attention condition for the initiator port associated with every I_T nexus that lost its
registration other than the I_T nexus on which the PERSISTENT RESERVE OUT command was
received, with the additional sense code set to REGISTRATIONS PREEMPTED.
If a PERSISTENT RESERVE OUT with a PREEMPT service action or a PREEMPT AND ABORT service
action sets the SERVICE ACTION RESERVATION KEY field to a value that does not match any registered reser-
vation key, then the device server shall complete the command with RESERVATION CONFLICT status.
It is not an error for a PERSISTENT RESERVE OUT with a PREEMPT service action or a PREEMPT AND
ABORT service action to set the RESERVATION KEY and the SERVICE ACTION RESERVATION KEY to the same
value, however, no unit attention condition is established for the I_T nexus on which the PERSISTENT
RESERVE OUT command was received. The registration is removed.


5.13.11.2.6 Preempting and aborting
The application client’s request for and the device server’s responses to a PERSISTENT RESERVE OUT
command with PREEMPT AND ABORT service action are identical to the responses to a PREEMPT service
action (see 5.13.11.2.4) except for the additions described in this subclause. If no reservation conflict
occurred, the device server shall perform the following uninterrupted series of actions:
a)
if the persistent reservation is not an all registrants type then:
A)
if the TST field is set to 000b (see 7.5.8) and the faulted I_T nexus, if any, is not the I_T nexus
associated with the persistent reservation or registration being preempted, then the task set ACA
condition shall be processed as defined in SAM-5;
B)
if the TST field is set to 000b and the faulted I_T nexus, if any, is the I_T nexus associated with the
persistent reservation or registration being preempted, then the PERSISTENT RESERVE OUT
command shall be processed without regard for the task set ACA condition; or
C) if the TST field is set to 001b, then the ACA condition shall be processed as defined in SAM-5;
b)
perform the uninterrupted series of actions described for the PREEMPT service action (see
5.13.11.2.4);
c)
all commands from the I_T nexus(es) associated with the persistent reservations or registrations
being preempted (i.e., preempted commands) except the PERSISTENT RESERVE OUT command
itself shall be aborted as defined in SAM-5;
d)
all copy operations (see 5.17.4.3) shall be aborted as if a COPY OPERATION ABORT command (see
6.3) has been received for each copy operation;
e)
after the PERSISTENT RESERVE OUT command with PREEMPT AND ABORT service action has
completed, all new commands are subject to the persistent reservation restrictions established by the
preempting I_T nexus;
f)
if the persistent reservation is not an all registrants type, then the device server shall clear any ACA
condition associated with an I_T nexus being preempted and shall abort any commands with an ACA
attribute received on that I_T nexus;
g)
if the persistent reservation is an all registrants type, then:
A)
if the service action reservation key is set to zero, the device server shall clear any ACA condition
and shall abort any commands with an ACA attribute; or
B)
if the service action reservation key is not set to zero, the device server shall do the following for
any I_T nexus registered using the specified reservation key:
a)
clear any ACA condition; and
b)
abort any commands with an ACA attribute;
and
h)
for logical units that implement the PREVENT ALLOW MEDIUM REMOVAL command (see SBC-3,
SSC-3, and SMC-3), the device server shall perform an action equivalent to the processing of a
PREVENT ALLOW MEDIUM REMOVAL command with the PREVENT field equal to zero received on
the I_T nexuses associated with the persistent reservation being preempted.
The actions described in this subclause shall be performed for all I_T nexuses that are registered with the
non-zero SERVICE ACTION RESERVATION KEY value, without regard for whether the preempted I_T nexuses hold
the persistent reservation. If the SERVICE ACTION RESERVATION KEY field is set to zero and an all registrants
persistent reservation is present, the device server shall abort all commands for all registered I_T nexuses.
5.13.11.2.7 Clearing
Any application client may release the persistent reservation and remove all registrations from a device server
by issuing a PERSISTENT RESERVE OUT command with CLEAR service action through a registered I_T
nexus with the following parameter:
a)
RESERVATION KEY field set to the value of the reservation key that is registered with the logical unit for
the I_T nexus.


In response to this request the device server shall perform a clear by doing the following as part of an uninter-
rupted series of actions:
a)
release the persistent reservation, if any;
b)
remove all registration(s);
c)
ignore the contents of the SCOPE and TYPE fields;
d)
continue normal processing of any commands from any I_T nexus that have been accepted by the
device server as allowed (i.e., nonconflicting); and
e)
establish a unit attention condition for the initiator port associated with every registered I_T nexus
other than the I_T nexus on which the PERSISTENT RESERVE OUT command with CLEAR service
action was received, with the additional sense code set to RESERVATIONS PREEMPTED.
NOTE 14 - Application clients should not use the CLEAR service action except during recovery operations
that are associated with a specific initiator port, since the effect of the CLEAR service action defeats the
persistent reservations features that protect data integrity.
5.13.11.3 Replacing lost reservations
A PERSISTENT RESERVE OUT command with the REPLACE LOST RESERVATION service action is used
to:
a)
begin a recovery process for the lost persistent reservation that is managed by application clients; and
b)
cause the device server to stop terminating commands due to a lost persistent reservation (see
5.13.5.3).
If the device server has not detected that persistent reservation information has been lost (see 5.13.5.3), then
the device server shall terminate a PERSISTENT RESERVE OUT command with the REPLACE LOST
RESERVATION service action with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID RELEASE OF PERSISTENT RESERVATION.
An application client may replace lost reservation information by issuing a PERSISTENT RESERVE OUT
command with the REPLACE LOST RESERVATION service action with the following parameters:
a)
RESERVATION KEY field set to zero;
b)
SERVICE ACTION RESERVATION KEY field set to the value of the new reservation key (i.e., the value used
to replace the lost reservation key value); and
c)
TYPE field and SCOPE field set to define a new persistent reservation. The scope and type of the new
persistent reservation may be different than those of the lost persistent reservation.
To process a valid PERSISTENT RESERVE OUT command with the REPLACE LOST RESERVATION
service action the device server shall perform the following as an uninterrupted series of actions:
a)
remove the prior registrations for all I_T nexuses, if any, without establishing unit attention conditions;
b)
establish a registration for the I_T nexus that is being used for the PERSISTENT RESERVE OUT
command using the service action reservation key;
c)
release any persistent reservations known to the device server;
d)
establish a new persistent reservation for the I_T nexus that is being used for the PERSISTENT
RESERVE OUT command using the contents of the SCOPE and TYPE fields;
e)
set the PRgeneration value to zero; and
f)
stop terminating commands due to a lost persistent reservation (see 5.13.5.3).
After the PERSISTENT RESERVE OUT command with the REPLACE LOST RESERVATION service action
has been completed with GOOD status, new commands are subject to the new persistent reservation restric-
tions established by the command.
