# 5.11 ORWRITE (32) command

5.11 ORWRITE (32) command
The ORWRITE (32) command (see table 69) requests that the device server perform one of the following
ORWRITE command (see 4.27) operations:
a)
a change generation and clear operation (see 4.27.3); or
b)
a set operation (see 4.27.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 69 for the ORWRITE (32) command.
The CONTROL byte is defined in SAM-6.
Table 69 — ORWRITE (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
BMOP
Reserved
PREVIOUS GENERATION PROCESSING
Reserved
Reserved
GROUP NUMBER
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (000Eh)
(LSB)
ORPROTECT
DPO
FUA
Reserved
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
EXPECTED ORWGENERATION
•••
(LSB)
(MSB)
NEW ORWGENERATION
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)


The bitmap operation (BMOP) field specifies the operation as described in table 70.
The PREVIOUS GENERATION PROCESSING field specifies the policy for performing future set operations that is to
be established in the device server by a successful change generation and clear operation (see 4.27.2.2).
See the ORWRITE (16) command (see 5.10) for the definitions of the FUA bit, the DPO bit, the ORPROTECT field,
the LOGICAL BLOCK ADDRESS field, the TRANSFER LENGTH field, and the GROUP NUMBER field.
The EXPECTED ORWGENERATION field contains a code that is compared with generation codes established and
maintained by the device server.
The NEW ORWGENERATION field specifies the current ORWgeneration code that is to be established in the
device server by a successful change generation and clear operation (see 4.27.3).
The device server shall:
a)
check protection information from the read operations based on the ORPROTECT field as described in
table 67; and
b)
check protection information transferred from the Data-Out Buffer based on the ORPROTECT field as
described in table 68.
The order of the user data and protection information checks and comparisons is vendor specific.
Table 70 — BMOP field
Code
Description
000b
The device server shall perform a set operation (see 4.27.4), and the contents of the
PREVIOUS GENERATION PROCESSING field and NEW ORWGENERATION field shall be
ignored.
001b
The device server shall perform a change generation and clear operation (see 4.27.3).
All others
Reserved
