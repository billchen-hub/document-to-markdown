# 5.13.7 Registering

5.13.6.3 Reporting the persistent reservation
An application client may send a PERSISTENT RESERVE IN command with READ RESERVATION service
action to receive the persistent reservation information.
In response to a PERSISTENT RESERVE IN command with READ RESERVATION service action the device
server shall report the following information for the persistent reservation, if any:
a)
the current PRgeneration value (see 6.15.2);
b)
the registered reservation key, if any, associated with the I_T nexus that holds the persistent reser-
vation (see 5.13.10). If the persistent reservation is an all registrants type, the registered reservation
key reported shall be zero; and
c)
the scope and type of the persistent reservation, if any.
If an application client uses a different reservation key for each I_T nexus, the application client may use the
reservation key to associate the persistent reservation with the I_T nexus that holds the persistent reser-
vation. This association is done using techniques that are outside the scope of this standard.
5.13.6.4 Reporting full status
An application client may send a PERSISTENT RESERVE IN command with READ FULL STATUS service
action to receive all information about registrations and the persistent reservation, if any.
In response to a PERSISTENT RESERVE IN command with READ FULL STATUS service action the device
server shall report the current PRgeneration value (see 6.15.2) and, for every I_T nexus that is currently regis-
tered, the following information:
a)
the registered reservation key;
b)
whether the I_T nexus is a persistent reservation holder;
c)
if the I_T nexus is a persistent reservation holder, the scope and type of the persistent reservation;
d)
the relative target port identifier identifying the target port of the I_T nexus; and
e)
a TransportID identifying the initiator port of the I_T nexus.
5.13.7 Registering
To establish a persistent reservation the application client shall first register an I_T nexus with the device
server. An application client registers with a logical unit by issuing a PERSISTENT RESERVE OUT command
with REGISTER service action or REGISTER AND IGNORE EXISTING KEY service action.
If the I_T nexus has an established registration, an application client may remove the reservation key (see
5.13.11.2.3). This is accomplished by issuing a PERSISTENT RESERVE OUT command with a REGISTER
service action or a REGISTER AND IGNORE EXISTING KEY service action as shown in table 67 and table
68, respectively.
If an I_T nexus has not yet established a reservation key or the reservation key and registration have been
removed, an application client may register that I_T nexus and zero or more specified unregistered I_T
nexuses by issuing a PERSISTENT RESERVE OUT command with REGISTER service action as defined in
table 67.


If the I_T nexus has an established registration, the application client may change the reservation key by
issuing a PERSISTENT RESERVE OUT command with REGISTER service action as defined in table 67.
Table 67 — Register behaviors for a REGISTER service action
Command
I_T nexus
status
Parameter list fields a
Results
RESERVATION
KEY
SERVICE ACTION
RESERVATION
KEY
SPEC_I_PT
received
on an
unregistered
I_T nexus
zero
zero
ignore
Do nothing except return GOOD status.
non-zero
zero
Register the I_T nexus on which the com-
mand was received with the value specified
in the SERVICE ACTION RESERVATION KEY field.
one
Register the I_T nexus on which the com-
mand was received and each unregistered
I_T nexus specified in the parameter list with
the value specified in the SERVICE ACTION
RESERVATION KEY field. b
non-zero
ignore
ignore
Return RESERVATION CONFLICT status.
received on
a registered
I_T nexus
Not equal to
I_T nexus
reservation
key
ignore
ignore
Return RESERVATION CONFLICT status.
Equal to
I_T nexus
reservation
key
zero
zero
Unregister the I_T nexus on which the
command was received (see 5.13.11.2.3).
one
Return CHECK CONDITION status. c
non-zero
zero
Change the reservation key of the I_T nexus
on which the command was received to the
value specified in the SERVICE ACTION RESER-
VATION KEY field.
one
Return CHECK CONDITION status. c
a For requirements regarding the parameter list fields not shown in this table see 6.16.3.
b If any I_T nexus specified in the parameter list is registered, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST. Devices compliant with previous versions of this
standard may return an additional sense code set to INVALID FIELD IN CDB.
c The sense key shall be set to ILLEGAL REQUEST, and the additional sense code shall be set to
INVALID FIELD IN PARAMETER LIST. Devices compliant with previous versions of this standard may
return an additional sense code set to INVALID FIELD IN CDB.


Alternatively, an application client may establish a reservation key for an I_T nexus without regard for whether
one has previously been established by issuing a PERSISTENT RESERVE OUT command with REGISTER
AND IGNORE EXISTING KEY service action as defined in table 68.
If a PERSISTENT RESERVE OUT command with a REGISTER service action or a REGISTER AND
IGNORE EXISTING KEY service action is attempted, but there are insufficient device server resources to
complete the operation, then the device server shall terminate the command with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INSUFFICIENT REGIS-
TRATION RESOURCES.
In response to a PERSISTENT RESERVE OUT command with a REGISTER service action or a REGISTER
AND IGNORE EXISTING KEY service action the device server shall perform a registration for each specified
I_T nexus by doing the following as an uninterrupted series of actions:
a)
process the registration request regardless of any persistent reservations;
b)
process the APTPL bit;
c)
ignore the contents of the SCOPE and TYPE fields;
d)
associate the reservation key specified in the SERVICE ACTION RESERVATION KEY field with the I_T
nexus being registered, where:
A)
the I_T nexus(es) being registered are shown in table 69; and
B)
regardless of how the I_T nexus initiator port is specified, the association for the initiator port is
based on either the initiator port name on SCSI transport protocols where initiator port names are
required or the initiator port identifier on SCSI transport protocols where initiator port names are
not required;
e)
register the reservation key specified in the SERVICE ACTION RESERVATION KEY field without changing
any persistent reservation that may exist; and
f)
retain the reservation key specified in the SERVICE ACTION RESERVATION KEY field and associated infor-
mation.
Table 68 — Register behaviors for a REGISTER AND IGNORE EXISTING KEY service action
Command
I_T nexus
status
Parameter list
fields a
Results
SERVICE ACTION
RESERVATION KEY
received on an
unregistered
I_T nexus
zero
Do nothing except return GOOD status.
non-zero
Register the I_T nexus on which the command was received
with the value specified in the SERVICE ACTION RESERVATION
KEY field.
received on a
registered
I_T nexus
zero
Unregister the I_T nexus on which the command was received
(see 5.13.11.2.3).
non-zero
Change the reservation key of the I_T nexus on which the
command was received to the value specified in the SERVICE
ACTION RESERVATION KEY field.
a The RESERVATION KEY field is ignored when processing a REGISTER AND IGNORE EXISTING KEY
service action. For requirements regarding other parameter list fields not shown in this table see
6.16.3.


After the registration request has been processed, the device server shall then allow other PERSISTENT
RESERVE OUT commands from the registered I_T nexus to be processed. The device server shall retain the
reservation key until the key is changed as described in this subclause or removed as described in 5.13.11.
Any PERSISTENT RESERVE OUT command service action received from an unregistered I_T nexus, other
than the REGISTER or the REGISTER AND IGNORE EXISTING KEY service action, shall be completed with
RESERVATION CONFLICT status.
It is not an error for an I_T nexus that is registered to be registered again with the same reservation key or a
new reservation key. A registration shall have no effect on any other registrations (e.g., if more than one I_T
nexus is registered with the same reservation key and one of those I_T nexuses registers again it has no
effect on the other I_T nexus’ registrations). A registration that contains a non-zero value in the SERVICE
ACTION RESERVATION KEY field shall have no effect on any persistent reservations (i.e., the reservation key for
an I_T nexus may be changed without affecting any previously created persistent reservation).
Multiple I_T nexuses may be registered with the same reservation key. An application client may use the
same reservation key for other I_T nexuses and logical units.
Table 69 — I_T Nexuses being registered
SPEC_I_PT a
ALL_TG_PT
I_T nexus(es) being registered
Initiator port
Target port
The port’s names or identifiers to be registered are determined from the I_T
nexus on which the PERSISTENT RESERVE OUT command was received
The port’s name or identifier to be
registered is determined from the I_T
nexus on which the PERSISTENT
RESERVE OUT command was
received
Register all of the target ports in the
SCSI target device
a) The port’s name or identifier to be
registered is determined from the
I_T nexus on which the PERSIS-
TENT RESERVE OUT command
was received; and
b) Specified by each TransportID in
the additional parameter data (see
6.16.3)
The port’s name or identifier to be
registered is determined from the I_T
nexus on which the PERSISTENT
RESERVE OUT command was
received
a) The port’s name or identifier to be
registered is determined from the
I_T nexus on which the PERSIS-
TENT RESERVE OUT command
was received; and
b) Specified by each TransportID in
the additional parameter data
Register all of the target ports in the
SCSI target device
a If the SPEC_I_PT bit is set to one and the service action is REGISTER AND IGNORE EXISTING KEY,
then the device server shall terminate the command with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.


5.13.8 Registering and moving the reservation
The PERSISTENT RESERVE OUT command REGISTER AND MOVE service action is used to register a
specified I_T nexus (see table 70) and move the reservation to establish that I_T nexus as the reservation
holder.
If a PERSISTENT RESERVE OUT command with a REGISTER AND MOVE service action is attempted, but
there are insufficient device server resources to complete the operation, then the device server shall terminate
the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INSUFFICIENT REGISTRATION RESOURCES.
Table 70 — Register behaviors for a REGISTER AND MOVE service action
Command
I_T nexus
status
Parameter list fields a
Results
RESERVATION
KEY
SERVICE ACTION
RESERVATION
KEY
UNREG
received on
an unregis-
tered
I_T nexus
ignore
ignore
ignore
Return RESERVATION CONFLICT status. d
received on
the registered
I_T nexus of
reservation
holder
Not equal to
I_T nexus
reservation
key
ignore
ignore
Return RESERVATION CONFLICT status.
Equal to
I_T nexus
reservation
key
zero
ignore
Return CHECK CONDITION status. b
non-zero c
zero
The I_T nexus on which PERSISTENT
RESERVE OUT command was received shall
remain registered. See this subclause for the
registration and the move specifications.
one
The I_T nexus on which PERSISTENT
RESERVE OUT command was received shall
be unregistered (see 5.13.11.2.3) upon com-
pletion of command processing. See this sub-
clause for the registration and the move
specifications.
received on a
registered I_T
nexus that is
not the reser-
vation holder
ignore
ignore
ignore
Return RESERVATION CONFLICT status.
a For requirements regarding other parameter list fields not shown in this table see 6.16.4.
b The sense key shall be set to ILLEGAL REQUEST, and the additional sense code shall be set to
INVALID FIELD IN PARAMETER LIST. Devices compliant with previous versions of this standard may
return an additional sense code set to INVALID FIELD IN CDB.
c The application client and backup application should use the same reservation key.
d Devices compliant with previous versions of this standard may return CHECK CONDITION status with
the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB.


If a PERSISTENT RESERVE OUT command with a REGISTER AND MOVE service action is received and
the established persistent reservation is a Write Exclusive - All Registrants type or Exclusive Access - All
Registrants type reservation, then the device server shall complete the command with RESERVATION
CONFLICT status.
If a PERSISTENT RESERVE OUT command with a REGISTER AND MOVE service action is received and
there is no persistent reservation established, then the device server shall terminate the command with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN CDB.
If a PERSISTENT RESERVE OUT command with a REGISTER AND MOVE service action specifies a Trans-
portID that is the same as the initiator port of the I_T nexus on which the command received, then the device
server shall terminate the command with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
In response to a PERSISTENT RESERVE OUT command with a REGISTER AND MOVE service action the
device server shall perform a register and move by doing the following as an uninterrupted series of actions:
a)
process the APTPL bit;
b)
ignore the contents of the SCOPE and TYPE fields;
c)
associate the reservation key specified in the SERVICE ACTION RESERVATION KEY field with the I_T
nexus specified as the destination of the register and move, where:
A)
the I_T nexus is specified by the TransportID and the RELATIVE TARGET PORT IDENTIFIER field (see
6.16.4); and
B)
regardless of the TransportID format used, the association for the initiator port is based on either
the initiator port name on SCSI transport protocols where initiator port names are required or the
initiator port identifier on SCSI transport protocols where initiator port names are not required;
d)
register the reservation key specified in the SERVICE ACTION RESERVATION KEY field;
e)
retain the reservation key specified in the SERVICE ACTION RESERVATION KEY field and associated infor-
mation;
f)
release the persistent reservation for the persistent reservation holder (i.e., the I_T nexus on which
the command was received);
g)
move the persistent reservation to the specified I_T nexus using the same scope and type as the
persistent reservation released in  item f); and
h)
if the UNREG bit is set to one, unregister (see 5.13.11.2.3) the I_T nexus on which PERSISTENT
RESERVE OUT command was received.
It is not an error for a REGISTER AND MOVE service action to register an I_T nexus that is already registered
with the same reservation key or a different reservation key.
5.13.9 Reserving
An application client creates a persistent reservation by issuing a PERSISTENT RESERVE OUT command
with RESERVE service action through a registered I_T nexus with the following parameters:
a)
RESERVATION KEY set to the value of the reservation key that is registered with the logical unit for the
I_T nexus; and
b)
TYPE field and SCOPE field set to the persistent reservation being created.
Only one persistent reservation is allowed at a time per logical unit and that persistent reservation has a scope
of LU_SCOPE.


If the device server receives a PERSISTENT RESERVE OUT command from an I_T nexus other than a
persistent reservation holder (see 5.13.10) that attempts to create a persistent reservation when a persistent
reservation already exists for the logical unit, then the device server shall complete the command with
RESERVATION CONFLICT status.
If a persistent reservation holder attempts to modify the type or scope of an existing persistent reservation, the
device server shall complete the command with RESERVATION CONFLICT status.
If the device server receives a PERSISTENT RESERVE OUT command with RESERVE service action where
the TYPE field and the SCOPE field contain the same values as the existing type and scope from a persistent
reservation holder, then it shall not make any change to the existing persistent reservation and shall complete
the command with GOOD status.
See 5.13.1 for information on when a persistent reservation takes effect.
5.13.10 Persistent reservation holder
The persistent reservation holder is determined by the type of the persistent reservation as follows:
a)
for a persistent reservation of the type Write Exclusive – All Registrants or Exclusive Access – All
Registrants, the persistent reservation holder is any registered I_T nexus; or
b)
for all other persistent reservation types, the persistent reservation holder is the I_T nexus:
A)
for which the reservation was established with a PERSISTENT RESERVE OUT command with
the RESERVE service action, the PREEMPT service action, the PREEMPT AND ABORT service
action, or the REPLACE LOST RESERVATION service action; or
B)
to which the reservation was moved by a PERSISTENT RESERVE OUT command with
REGISTER AND MOVE service action.
A persistent reservation holder has its reservation key returned in the parameter data from a PERSISTENT
RESERVE IN command with READ RESERVATION service action as follows:
a)
for a persistent reservation of the type Write Exclusive – All Registrants or Exclusive Access – All
Registrants, the reservation key shall be set to zero; or
b)
for all other persistent reservation types, the reservation key shall be set to the registered reservation
key for the I_T nexus that holds the persistent reservation.
It is not an error for a persistent reservation holder to send a PERSISTENT RESERVE OUT command with
RESERVE service action to the reserved logical unit with TYPE and SCOPE fields that match those of the
persistent reservation (see 5.13.9).
A persistent reservation holder is allowed to release the persistent reservation using the PERSISTENT
RESERVE OUT command with RELEASE service action (see 5.13.11.2.2).
If the registration of the persistent reservation holder is removed (see 5.13.11.2), the reservation shall be
released. If the persistent reservation holder is more than one I_T nexus, the reservation shall not be released
until the registrations for all persistent reservation holder I_T nexuses are removed.
