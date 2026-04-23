# 5.35 UNMAP command

5.35 UNMAP command
5.35.1 UNMAP command overview
The UNMAP command (see table 120) requests that the device server cause one or more LBAs to be
unmapped (see 4.7.3).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 120 for the UNMAP
command.
For a thin provisioned logical unit (see 4.7.3.3) with the ANC_SUP bit set to one in the Logical Block
Provisioning VPD page (see 6.6.7):
a)
if the ANCHOR bit is set to zero, then any LBA on which an unmap operation (see 4.7.3.4) is performed
shall either become deallocated (see 4.7.4.6) or anchored (see 4.7.4.7) and should become deallo-
cated; and
b)
if the ANCHOR bit is set to one, then any LBA on which an unmap operation is performed shall become
anchored.
For a thin provisioned logical unit (see 4.7.3.3) with the ANC_SUP bit set to zero in the Logical Block
Provisioning VPD page:
a)
if the ANCHOR bit is set to zero, then any LBA on which an unmap operation is performed shall become
deallocated; and
b)
if the ANCHOR bit is set to one, then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to INVALID FIELD IN CDB.
For a resource provisioned logical unit (see 4.7.3.2), the ANCHOR bit shall be ignored and any LBA on which an
unmap operation is performed shall become anchored (i.e., the command is processed as if the ANCHOR bit is
set to one).
For a thin provisioned logical unit or a resource provisioned logical unit any LBA on which an unmap operation
is not performed does not change logical block provisioning state.
See the PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
The PARAMETER LIST LENGTH field specifies the length in bytes of the UNMAP parameter list that is available to
be transferred from the Data-Out Buffer. If the parameter list length is greater than zero and less than eight,
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
Table 120 — UNMAP command
Bit
Byte
OPERATION CODE (42h)
Reserved
ANCHOR
Reserved
•••
Reserved
GROUP NUMBER
(MSB)
PARAMETER LIST LENGTH
(LSB)
CONTROL


to ILLEGAL REQUEST and the additional sense code set to PARAMETER LIST LENGTH ERROR. A
PARAMETER LIST LENGTH set to zero specifies that no data shall be transferred.
The CONTROL byte is defined in SAM-6.
5.35.2 UNMAP parameter list
The UNMAP parameter list (see table 121) contains an UNMAP parameter list header and block descriptors.
Each UNMAP block descriptor specifies a range of LBAs for which each LBA is processed as specified by the
ANCHOR bit in the CDB (see 5.35.1).The LBAs specified in the block descriptors may contain overlapping LBA
extents, and may be in any order.
The UNMAP DATA LENGTH field specifies the length in bytes of the following data that is available to be
transferred from the Data-Out Buffer. The unmap data length does not include the number of bytes in the
UNMAP DATA LENGTH field.
The UNMAP BLOCK DESCRIPTOR DATA LENGTH field specifies the length in bytes of the UNMAP block descriptors
that are available to be transferred from the Data-Out Buffer. The unmap block descriptor data length should
be a multiple of 16. If the unmap block descriptor data length is not a multiple of 16, then the last unmap block
descriptor is incomplete and shall be ignored. If the UNMAP BLOCK DESCRIPTOR DATA LENGTH field is set to zero,
then no unmap block descriptors are included in the UNMAP parameter list. This condition shall not be
considered an error.
If any UNMAP block descriptors in the UNMAP block descriptor list are truncated as a result of the parameter
list length in the CDB, then that UNMAP block descriptor shall be ignored.
Table 121 — UNMAP parameter list
Bit
Byte
(MSB)
UNMAP DATA LENGTH (n - 1)
(LSB)
(MSB)
UNMAP BLOCK DESCRIPTOR DATA LENGTH (n - 7)
(LSB)
Reserved
•••
UNMAP block descriptor list (if any)
UNMAP block descriptor [first] (see table 122) (if any)
•••
•••
n - 15
UNMAP block descriptor [last] (see table 122) (if any)
•••
n
