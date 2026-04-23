# 4.17 Reservations

4.17 Reservations
Reservation restrictions are placed on commands as a result of access qualifiers associated with the type of
reservation. See SPC-6 for a description of reservations. The details of commands that are allowed under
what types of reservations are described in table 13.
Commands from I_T nexuses holding a reservation should complete normally. Table 13 specifies the behavior
of commands from registered I_T nexuses when a registrants only or all registrants type persistent reservation
is present.
For each command, this standard or SPC-6 defines the conditions that result in the device server completing
the command with RESERVATION CONFLICT status.
Table 13 — SBC-4 commands that are allowed in the presence of various reservations (part 1 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T nexus
From
registered
I_T nexus
(RR all
types)
From I_T nexus not
registered
Write
Exclusive
Exclusive
Access
Write
Exclusive
- RR
Exclusive
Access
- RR
BACKGROUND CONTROL
Conflict
Conflict
Allowed
Conflict
Conflict
COMPARE AND WRITE
Conflict
Conflict
Allowed
Conflict
Conflict
FORMAT UNIT
Conflict
Conflict
Allowed
Conflict
Conflict
FORMAT WITH PRESET
Conflict
Conflict
Allowed
Conflict
Conflict
GET LBA STATUS
Allowed
Conflict
Allowed
Allowed
Conflict
GET PHYSICAL ELEMENT STATUS
Allowed
Conflict
Allowed
Allowed
Conflict
GET STREAM STATUS
Allowed
Conflict
Allowed
Allowed
Conflict
ORWRITE
Conflict
Conflict
Allowed
Conflict
Conflict
POPULATE TOKEN
Allowed
Conflict
Allowed
Allowed
Conflict
PRE-FETCH
Allowed
Conflict
Allowed
Allowed
Conflict
Key:
RR = Registrants Only or All Registrants
Allowed = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present should complete
normally.
Conflict = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present shall not be
performed, and the device server shall complete the command with RESERVATION CONFLICT status.
a The device server in logical units claiming compliance with SBC-2 may complete the command with
RESERVATION CONFLICT status. Device servers may report whether certain commands are allowed
in the PERSISTENT RESERVE IN command REPORT CAPABILITIES service action parameter data
ALLOW COMMANDS field (see SPC-6).


PREVENT ALLOW MEDIUM REMOVAL
(Prevent=0)
Allowed
Allowed
Allowed
Allowed
Allowed
PREVENT ALLOW MEDIUM REMOVAL
(Prevent 0)
Conflict
Conflict
Allowed
Conflict
Conflict
READ
Allowed
Conflict
Allowed
Allowed
Conflict
READ CAPACITY
Allowed
Allowed
Allowed
Allowed
Allowed
READ DEFECT DATA
Allowed a
Conflict
Allowed
Allowed a
Conflict
REASSIGN BLOCKS
Conflict
Conflict
Allowed
Conflict
Conflict
REMOVE ELEMENT AND TRUNCATE
Conflict
Conflict
Allowed
Conflict
Conflict
REPORT REFERRALS
Allowed
Allowed
Allowed
Allowed
Allowed
REPORT PROVISIONING
INITIALIZATION PATTERN
Allowed
Allowed
Allowed
Allowed
Allowed
RESTORE ELEMENTS AND REBUILD
Conflict
Conflict
Allowed
Conflict
Conflict
SANITIZE
Conflict
Conflict
Allowed
Conflict
Conflict
START STOP UNIT with START bit set to
one and POWER CONDITION field set to 0h
Allowed
Allowed
Allowed
Allowed
Allowed
START STOP UNIT with START bit set to
zero or POWER CONDITION field set to a
value other than 0h
Conflict
Conflict
Allowed
Conflict
Conflict
STREAM CONTROL
Conflict
Conflict
Allowed
Conflict
Conflict
SYNCHRONIZE CACHE
Conflict
Conflict
Allowed
Conflict
Conflict
UNMAP
Conflict
Conflict
Allowed
Conflict
Conflict
VERIFY
Allowed
Conflict
Allowed
Allowed
Conflict
WRITE
Conflict
Conflict
Allowed
Conflict
Conflict
Table 13 — SBC-4 commands that are allowed in the presence of various reservations (part 2 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T nexus
From
registered
I_T nexus
(RR all
types)
From I_T nexus not
registered
Write
Exclusive
Exclusive
Access
Write
Exclusive
- RR
Exclusive
Access
- RR
Key:
RR = Registrants Only or All Registrants
Allowed = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present should complete
normally.
Conflict = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present shall not be
performed, and the device server shall complete the command with RESERVATION CONFLICT status.
a The device server in logical units claiming compliance with SBC-2 may complete the command with
RESERVATION CONFLICT status. Device servers may report whether certain commands are allowed
in the PERSISTENT RESERVE IN command REPORT CAPABILITIES service action parameter data
ALLOW COMMANDS field (see SPC-6).
