# 5.58 WRITE STREAM (32) command

5.57 WRITE STREAM (16) command
The WRITE STREAM (16) command (see table 156) requests that the device server perform the actions
defined for the WRITE (10) command (see 5.40).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 156 for the WRITE
STREAM (16) command.
The stream identifier (STR_ID) field specifies the stream identifier associated with this command as described
in 4.32.
See the WRITE (10) command (see 5.33) for the definitions of the other fields in this command.
5.58 WRITE STREAM (32) command
The WRITE STREAM (32) command (see table 157) requests that the device server perform the actions
defined for the WRITE (32) command (see 5.43).
Table 156 — WRITE STREAM (16) command
Bit
Byte
OPERATION CODE (9Ah)
WRPROTECT
DPO
FUA
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
STR_ID
(LSB)
(MSB)
TRANSFER LENGTH
(LSB)
Reserved
GROUP NUMBER
CONTROL


The device server shall process a WRITE STREAM (32) command only if type 2 protection is enabled
(see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 157 for the WRITE STREAM (32) command.
See the WRITE STREAM (16) command (see 5.57) for the definition of the STR_ID field.
See the WRITE (32) command (see 5.43) for the definitions of the other fields in this command.
Table 157 — WRITE STREAM (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
STR_ID
Reserved
GROUP NUMBER
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (0010h)
(LSB)
WRPROTECT
DPO
FUA
Reserved
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG
•••
(LSB)
(MSB)
EXPECTED LOGICAL BLOCK APPLICATION TAG
(LSB)
(MSB)
LOGICAL BLOCK APPLICATION TAG MASK
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
