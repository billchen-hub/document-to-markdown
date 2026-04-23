# 5.33 SYNCHRONIZE CACHE (10) command

5.32.2 STREAM CONTROL parameter data
The STREAM CONTROL parameter data is shown in table 117.
The PARAMETER LENGTH field indicates the length of the parameter data and shall be set as shown in table 117
for the STREAM CONTROL parameter data.
If the STR_CTL field was set to 01b (i.e., open) in the STREAM CONTROL command, then the device server
shall set the ASSIGNED_STR_ID field to a non zero value that is not currently assigned to an open stream by the
device server and open that stream. If the STR_CTL field was not set to 01b in the STREAM CONTROL
command, then the ASSIGNED_STR_ID field is reserved.
5.33 SYNCHRONIZE CACHE (10) command
The SYNCHRONIZE CACHE (10) command (see table 118) requests that, for each logical block whose
logical block data is in the volatile cache and has not already been written to the non-volatile cache, if any, or
the medium, the device server either:
a)
perform a write medium operation to the LBA using the logical block data in volatile cache; or
b)
write the logical block to the non-volatile cache, if any.
NOTE 13 - Migration from the SYNCHRONIZE CACHE (10) command to the SYNCHRONIZE CACHE (16)
command is recommended for all implementations.
Table 117 — STREAM CONTROL parameter data
Bit
Byte
PARAMETER LENGTH (07h)
Reserved
•••
(MSB)
ASSIGNED_STR_ID
(LSB)
Reserved


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 118 for the
SYNCHRONIZE CACHE (10) command.
See the PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field.
See the PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
An immediate (IMMED) bit set to zero specifies that the device server shall not return status until the
synchronize cache operation has been completed. An IMMED bit set to one specifies that the device server
shall return status as soon as the CDB has been validated. If the IMMED bit is set to one, and the device server
does not support the IMMED bit, then the device server shall terminate the command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB.
If the IMMED bit is set to one and the synchronize cache operation has not completed, then the SYNC_PROG
field (see 6.5.6) defines the device server behavior while the synchronize cache command is being
processed.
A NUMBER OF LOGICAL BLOCKS field set to a non-zero value specifies the number of logical blocks that shall be
synchronized, starting with the logical block referenced by the LBA specified by the LOGICAL BLOCK ADDRESS
field. A NUMBER OF LOGICAL BLOCKS field set to zero specifies that all logical blocks starting with the one
referenced by the LBA specified in the LOGICAL BLOCK ADDRESS field to the last logical block on the medium
shall be synchronized. If the specified LBA and the specified number of logical blocks exceed the capacity of
the medium (see 4.5), then the device server shall terminate the command with CHECK CONDITION status
with the sense key set to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK
ADDRESS OUT OF RANGE.
A logical block within the range that is not in cache is not considered an error.
The CONTROL byte is defined in SAM-6.
Table 118 — SYNCHRONIZE CACHE (10) command
Bit
Byte
OPERATION CODE (35h)
Reserved
Obsolete
IMMED
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
GROUP NUMBER
(MSB)
NUMBER OF LOGICAL BLOCKS
(LSB)
CONTROL


5.34 SYNCHRONIZE CACHE (16) command
The SYNCHRONIZE CACHE (16) command (see table 119) requests that the device server perform the
actions defined for the SYNCHRONIZE CACHE (10) command (see 5.33).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 119 for the
SYNCHRONIZE CACHE (16) command.
See the SYNCHRONIZE CACHE (10) command (see 5.33) for the definitions of the other fields in this
command.
Table 119 — SYNCHRONIZE CACHE (16) command
Bit
Byte
OPERATION CODE (91h)
Reserved
Obsolete
IMMED
Reserved
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL
