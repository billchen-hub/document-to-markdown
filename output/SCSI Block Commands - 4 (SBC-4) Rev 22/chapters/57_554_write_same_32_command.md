# 5.54 WRITE SAME (32) command

A NDOB bit set to zero specifies that the device server shall process the command using logical block data
from the Data-Out Buffer. A NDOB bit set to one specifies that:
a)
the device server shall not transfer data from the Data-Out Buffer;
b)
if the Logical Block Provisioning VPD page (see 6.6.7) is not supported or the LBPRZ field (see 6.6.7)
is set to 000b or xx1b, then the device server shall process the command as if the Data-Out Buffer
contained user data set to all zeroes and protection information, if any, containing:
A) the LOGICAL BLOCK GUARD field set to FFFFh;
B) the LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh; and
C) the LOGICAL BLOCK APPLICATION TAG field set to FFFFh;
and
c)
if the LBPRZ field is set to 010b, then the device server shall process the command as if the Data-Out
Buffer contained user data set to the provisioning initialization pattern and protection information, if
any, containing:
A) the LOGICAL BLOCK GUARD field set to FFFFh;
B) the LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh; and
C) the LOGICAL BLOCK APPLICATION TAG field set to FFFFh.
See the WRITE SAME (10) command (see 5.52) for the definitions of the other fields in this command.
5.54 WRITE SAME (32) command
The WRITE SAME (32) command (see table 149) requests that the device server perform the actions defined
for the WRITE SAME (10) command (see 5.52).
The device server shall process a WRITE SAME (32) command only if type 2 protection is enabled
(see 4.21.2.4).


The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 149 for the WRITE SAME (32) command.
See the WRITE SAME (10) command (see 5.52) for the definitions of the CONTROL byte, the GROUP NUMBER
field, the WRPROTECT field, the LOGICAL BLOCK ADDRESS field, the NUMBER OF LOGICAL BLOCKS field, the UNMAP
bit, and the ANCHOR bit.
See the WRITE SAME (16) command (see 5.53) for the definition of the NDOB bit.
If checking of the LOGICAL BLOCK REFERENCE TAG field is enabled (see table 133 in 5.40), then the EXPECTED
INITIAL LOGICAL BLOCK REFERENCE TAG field contains the value of the LOGICAL BLOCK REFERENCE TAG field
expected in the protection information of the first logical block accessed by the command instead of a value
based on the LBA (see 4.21.3).
If the ATO bit is set to one in the Control mode page (see SPC-6) and checking of the LOGICAL BLOCK
APPLICATION TAG field is enabled (see table 133 in 5.40), then the LOGICAL BLOCK APPLICATION TAG MASK field
contains a value that is a bit mask for enabling the checking of the LOGICAL BLOCK APPLICATION TAG field in
every instance of protection information for each logical block accessed by the command. A LOGICAL BLOCK
Table 149 — WRITE SAME (32) command
Bit
Byte
OPERATION CODE (7Fh)
CONTROL
Reserved
•••
Reserved
GROUP NUMBER
ADDITIONAL CDB LENGTH (18h)
(MSB)
SERVICE ACTION (000Dh)
(LSB)
WRPROTECT
ANCHOR
UNMAP
 Obsolete
NDOB
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
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
