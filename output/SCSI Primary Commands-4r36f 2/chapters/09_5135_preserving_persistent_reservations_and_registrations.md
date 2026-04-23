# 5.13.5 Preserving persistent reservations and registrations

A RESERVE(6) or RESERVE(10) command shall complete with GOOD status, but no reservation shall be
established and the persistent reservation shall not be changed, if the command is received from:
a)
an I_T nexus that is a persistent reservation holder; or
b)
an I_T nexus that is registered if a registrants only or all registrants type persistent reservation is
present.
In all other cases, a RESERVE(6) command, RESERVE(10) command, RELEASE(6) command, or
RELEASE(10) command shall be processed as defined in SPC-2.
5.13.4 Persistent reservations interactions with IKEv2-SCSI SA creation
If a PERSISTENT RESERVE OUT command is received while an IKEv2-SCSI CCS is in progress (see
5.14.4), the command shall be terminated with CHECK CONDITION status, with the sense key NOT READY,
and the additional sense code set to LOGICAL UNIT NOT READY, SA CREATION IN PROGRESS. The
sense key specific additional sense data may be set as described in 5.14.5.
5.13.5 Preserving persistent reservations and registrations
5.13.5.1 Preserving persistent reservations and registrations through power loss
The application client may request activation of the persist through power loss device server capability to
preserve the persistent reservation and registrations across power cycles by setting the APTPL bit to one in the
PERSISTENT RESERVE OUT parameter data sent with a REGISTER service action, REGISTER AND
IGNORE EXISTING KEY service action, REGISTER AND MOVE service action, or REPLACE LOST RESER-
VATION service action.
After the application client enables the persist through power loss capability the device server shall preserve
the persistent reservation, if any, and all current and future registrations associated with the logical unit to
which the REGISTER service action, the REGISTER AND IGNORE EXISTING KEY service action, the
REGISTER AND MOVE service action, or the REPLACE LOST RESERVATION service action was
addressed until an application client disables the persist through power loss capability. The APTPL value from
the most recent successfully completed REGISTER service action, REGISTER AND IGNORE EXISTING
KEY service action, REGISTER AND MOVE service action, or REPLACE LOST RESERVATION service
action from any application client shall determine the logical unit’s behavior in the event of a power loss.
The device server shall preserve the following information for each existing registration across any hard reset,
logical unit reset, or I_T nexus loss, and if the persist through power loss capability is enabled, across any
power cycle:
a)
for SCSI transport protocols where initiator port names are required, the initiator port name;
otherwise, the initiator port identifier;
b)
reservation key; and
c)
indication of the target port to which the registration was applied.
The device server shall preserve the following information about the existing persistent reservation across any
hard reset, logical unit reset, or I_T nexus loss, and if the persist through power loss capability is enabled,
across any power cycle:
a)
for SCSI transport protocols where initiator port names are required, the initiator port name;
otherwise, the initiator port identifier;
b)
reservation key;


c)
scope;
d)
type; and
e)
indication of the target port through which the reservation was established.
NOTE 13 - The scope of a persistent reservation is always LU_SCOPE (see 6.15.3.3). For an all registrants
type persistent reservation, only the scope and type need to be preserved.
5.13.5.2 Nonvolatile memory considerations for preserving persistent reservations and registrations
The capability of preserving persistent reservations and registrations across power cycles requires logical
units to use nonvolatile memory within the SCSI device. Any logical unit that supports the persist through
power loss capability of persistent reservation and has nonvolatile memory that is not ready shall allow the
following commands into the task set:
a)
INQUIRY;
b)
LOG SENSE;
c)
READ BUFFER;
d)
REPORT LUNS;
e)
REPORT TARGET PORT GROUPS;
f)
REQUEST SENSE;
g)
START STOP UNIT with the START bit set to one and the POWER CONDITION field set to 0h (see
SBC-3); and
h)
WRITE BUFFER.
Until nonvolatile memory has become ready after a power cycle, commands other than those listed in this
subclause shall be terminated with CHECK CONDITION status, with the sense key set to NOT READY, and
the additional sense code set as described in table 334 (see 6.47).
5.13.5.3 Loss of persistent reservation information
5.13.5.3.1 Loss of persistent reservation information overview
While the persist through power loss capability is enabled (see 5.13.5.1), the device server may detect a
failure (e.g., a hardware failure in nonvolatile memory) that causes the loss of the preserved persistent
reservation information.
The failure detected by the device server may be:
a)
recoverable through the combined actions of the device server and application client (e.g., sufficient
nonvolatile memory is available to recreate the lost persistent reservation and registrations infor-
mation) using the processes described in 5.13.5.3.2 (i.e., a recoverable lost persistent reservation); or
b)
unrecoverable, except by operator intervention (i.e., an unrecoverable lost persistent reservation).
5.13.5.3.2 Recoverable loss of persistent reservation information
If the device server detects a recoverable lost persistent reservation, the device server shall establish a recov-
erable lost persistent reservation condition. A recoverable lost persistent reservation condition is a condition in
which the device server shall:
a)
not terminate a PERSISTENT RESERVE OUT command with the REPLACE LOST RESERVATION
service action with RESERVATION CONFLICT status; and
b)
terminate with CHECK CONDITION status with the sense key set to DATA PROTECT and the
additional sense code set to PERSISTENT RESERVATION INFORMATION LOST all commands
other than:


A)
a PERSISTENT RESERVE OUT command with a REPLACE LOST RESERVATION service
action; and
B)
those commands listed in 5.13.5.2.
The device server shall clear a recoverable lost persistent reservation condition in response to:
a)
the successful processing of a PERSISTENT RESERVE OUT command with the REPLACE LOST
RESERVATION service action (see 5.13.11.3); or
b)
the recoverable lost persistent reservation becoming an unrecoverable lost persistent reservation.
The device server shall not clear a recoverable lost persistent reservation condition for any reason other than
the reasons described in this subclause.
5.13.5.3.3 Unrecoverable loss of persistent reservation information overview
If the device server detects an unrecoverable lost persistent reservation, then the device server:
a)
should operate as if it has non volatile memory that is not ready (see 5.13.5.2); or
b)
may terminate commands other than those commands listed in 5.13.5.2 with CHECK CONDITION
status with the sense key set to HARDWARE ERROR with the additional sense code set to an appro-
priate value.
5.13.6 Finding persistent reservations and reservation keys
5.13.6.1 Summary of commands for finding persistent reservations and reservation keys
The application client may obtain information about the persistent reservation and the reservation keys (i.e.,
registrations) that are present within a device server by issuing a PERSISTENT RESERVE IN command with
a READ RESERVATION service action, a READ KEYS service action, or a READ FULL STATUS service
action.
5.13.6.2 Reporting reservation keys
An application client may send a PERSISTENT RESERVE IN command with READ KEYS service action to
determine if any I_T nexuses have been registered with a logical unit through any target port.
In response to a PERSISTENT RESERVE IN with READ KEYS service action the device server shall report
the following:
a)
the current PRgeneration value (see 6.15.2); and
b)
the reservation key for every I_T nexus that is currently registered regardless of the target port
through which the registration occurred.
The PRgeneration value allows the application client to verify that the configuration of the I_T nexuses regis-
tered with a logical unit has not been modified.
Duplicate reservation keys shall be reported if multiple I_T nexuses are registered using the same reservation
key.
If an application client uses a different reservation key for each I_T nexus, the application client may use the
reservation key to uniquely identify an I_T nexus.
