# 5.3 COMPARE AND WRITE command

The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the value shown
in table 35 for the BACKGROUND CONTROL command.
The background operation control (BO_CTL) field specifies that the device server shall control host initiated
advanced background operations as described in 4.31. The BO_CTL field is described in table 36.
The background operation time (BO_TIME) field specifies the maximum time that the device server shall have
to perform host initiated advanced background operations in units of 100 ms (see 4.31). The BO_TIME field is
ignored if the BO_CTL field is not set to 01b. A BO_TIME field set to 00h specifies that there is no limit to the time
that the device server may perform host initiated advanced background operations.
The CONTROL byte is defined in SAM-6.
5.3 COMPARE AND WRITE command
The COMPARE AND WRITE command (see table 37) requests that the device server perform the following
as an uninterrupted sequence of actions (see 4.25):
1)
perform read operations from the specified LBAs;
2)
perform a compare operation on only the user data (i.e., not on the protection information) from:
A) the read operations; and
B) the compare instance transferred from the Data-Out Buffer;
3)
if the compare operation indicates a match, then perform the following operations:
1)
check the protection information, if any, in the write instance transferred from the Data-Out Buffer
based on the contents of the WRPROTECT field as shown in table 133; and
2)
perform write operations to the LBAs specified by this command using the write instance;
and
4)
if the compare operation does not indicate a match, then terminate the command with CHECK
CONDITION status with the sense key set to MISCOMPARE and the additional sense code set to
MISCOMPARE DURING VERIFY OPERATION. In the sense data (see 4.18 and SPC-6) the offset
from the start of the Data-Out Buffer to the first byte of data that was not equal shall be reported in the
INFORMATION field.
The Data-Out Buffer contains two instances of logical block data:
1)
the compare instance, in which:
A) the user data is used for the compare operation; and
B) the protection information, if any, is not used;
and
2)
the write instance, in which:
A) the user data is used for the write operations; and
B) the protection information, if any, is used for the write operations.
Table 36 — BO_CTL field
Code
Description
00b
Do not change host initiated advanced background operations.
01b
Start host initiated advanced background operations.
10b
Stop host initiated advanced background operations.
11b
Reserved


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 37 for the
COMPARE AND WRITE command.
See the WRITE (10) command for the definition of the WRPROTECT field.
See the READ (10) command (see 5.16) for the definition of the DPO bit. See the READ (10) command
(see 5.16) for the definition of the FUA bit specifying behavior for the read operations. See the WRITE (10)
command (see 5.40) for the definition of the FUA bit specifying behavior for the write operations.
The LOGICAL BLOCK ADDRESS field specifies the LBA of the first logical block (see 4.5) to be accessed by the
device server (e.g., the first LBA accessed by both a read operation and a write operation). If the specified
LBA exceeds the capacity of the medium, then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
LOGICAL BLOCK ADDRESS OUT OF RANGE.
The NUMBER OF LOGICAL BLOCKS field specifies:
a)
the number of contiguous logical blocks on which read operations shall be performed, starting with the
LBA specified by the LOGICAL BLOCK ADDRESS field;
b)
the number of contiguous logical blocks that shall be transferred from the Data-Out Buffer for the
compare operation; and
c)
if the compare operation indicates a match, then the number of contiguous logical blocks that shall be
transferred from the Data-Out Buffer and on which write operations shall be performed, starting with
the LBA specified by the LOGICAL BLOCK ADDRESS field.
A NUMBER OF LOGICAL BLOCKS field set to zero specifies that no read operations shall be performed, no logical
block data shall be transferred from the Data-Out Buffer, no compare operations shall be performed, and no
write operations shall be performed. This condition shall not be considered an error.
If the specified LBA and the specified number of logical blocks exceed the capacity of the medium (see 4.5),
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS OUT OF RANGE.
If the number of logical blocks exceeds the value in the MAXIMUM COMPARE AND WRITE LENGTH field (see 6.6.4),
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
See the PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
Table 37 — COMPARE AND WRITE command
Bit
Byte
OPERATION CODE (89h)
WRPROTECT
DPO
FUA
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
•••
NUMBER OF LOGICAL BLOCKS
Reserved
GROUP NUMBER
CONTROL
