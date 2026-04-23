# 6.15.3 READ RESERVATION service action

6.15.3 READ RESERVATION service action
6.15.3.1 READ RESERVATION service action introduction
The READ RESERVATION service action requests that the device server return a parameter list containing a
header and the persistent reservation, if any, that is present in the device server.
For more information on READ RESERVATION see 5.13.6.3.
6.15.3.2 Format of PERSISTENT RESERVE IN parameter data for READ RESERVATION
If no persistent reservation is held, the format for the parameter data provided in response to a PERSISTENT
RESERVE IN command with the READ RESERVATION service action is shown in table 203.
The PRGENERATION field shall be as defined for the PERSISTENT RESERVE IN command with READ KEYS
service action parameter data (see 6.15.2).
The ADDITIONAL LENGTH field shall be set to zero (see table 203), indicating that no persistent reservation is
held.
Table 203 — Format of PERSISTENT RESERVE IN parameter data for READ RESERVATION with
no reservation held
Bit
Byte
(MSB)
PRGENERATION
•••
(LSB)
(MSB)
ADDITIONAL LENGTH (00000000h)
•••
(LSB)


If a persistent reservation is held, the format for the parameter data provided in response to a PERSISTENT
RESERVE IN command with the READ RESERVATION service action is shown in table 204.
The PRGENERATION field shall be as defined for the PERSISTENT RESERVE IN command with READ KEYS
service action parameter data.
The ADDITIONAL LENGTH field indicates the number of bytes that follow and shall be set as shown in table 204.
The contents of the ADDITIONAL LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The RESERVATION KEY field shall indicate the reservation key under which the persistent reservation is held
(see 5.13.10).
The SCOPE field shall be set to LU_SCOPE (see 6.15.3.3).
The TYPE field shall indicate the persistent reservation type (see 6.15.3.4) specified in the PERSISTENT
RESERVE OUT command that created the persistent reservation.
The obsolete fields in bytes 16 to 19, byte 22, and byte 23 were defined in SPC-2.
Table 204 — Format of PERSISTENT RESERVE IN parameter data for READ RESERVATION with
a reservation held
Bit
Byte
(MSB)
PRGENERATION
•••
(LSB)
(MSB)
ADDITIONAL LENGTH (00000010h)
•••
(LSB)
(MSB)
RESERVATION KEY
•••
(LSB)
Obsolete
•••
Reserved
SCOPE
TYPE
Obsolete


6.15.3.3 Persistent reservations scope
The SCOPE field (see table 205) shall be set to LU_SCOPE, specifying that the persistent reservation applies
to the entire logical unit.
The LU_SCOPE scope shall be implemented by all device servers that implement PERSISTENT RESERVE
OUT.
Table 205 — Persistent reservation SCOPE field
Code
Name
Description
0h
LU_SCOPE
Persistent reservation applies to the full logical unit
1h to 2h
Obsolete
3h to Fh
Reserved


6.15.3.4 Persistent reservations type
The TYPE field (see table 206) specifies the characteristics of the persistent reservation being established for
all logical blocks within the logical unit. Table 65 (see 5.13.1) defines the persistent reservation types under
which each command defined in this standard is allowed to be processed. Each other command standard
defines the persistent reservation types under which each command defined in that command standard is
allowed to be processed.
Table 206 — Persistent reservation TYPE field
Code
Name
Description
0h
Obsolete
1h
Write
Exclusive
Access Restrictions: Some commands (e.g., media-access write
commands) are only allowed for the persistent reservation holder (see
5.13.10).
Persistent Reservation Holder: There is only one persistent reservation
holder.
2h
Obsolete
3h
Exclusive
Access
Access Restrictions: Some commands (e.g., media-access commands)
are only allowed for the persistent reservation holder (see 5.13.10).
Persistent Reservation Holder: There is only one persistent reservation
holder.
4h
Obsolete
5h
Write
Exclusive –
Registrants
Only
Access Restrictions: Some commands (e.g., media-access write
commands) are only allowed for registered I_T nexuses.
Persistent Reservation Holder: There is only one persistent reservation
holder (see 5.13.10).
6h
Exclusive
Access –
Registrants
Only
Access Restrictions: Some commands (e.g., media-access commands)
are only allowed for registered I_T nexuses.
Persistent Reservation Holder: There is only one persistent reservation
holder (see 5.13.10).
7h
Write
Exclusive –
All
Registrants
Access Restrictions: Some commands (e.g., media-access write
commands) are only allowed for registered I_T nexuses.
Persistent Reservation Holder: Each registered I_T nexus is a persistent
reservation holder (see 5.13.10).
8h
Exclusive
Access –
All
Registrants
Access Restrictions: Some commands (e.g., media-access commands)
are only allowed for registered I_T nexuses.
Persistent Reservation Holder: Each registered I_T nexus is a persistent
reservation holder (see 5.13.10).
9h to Fh
Reserved
