# 5.25 RECEIVE ROD TOKEN INFORMATION

5.25 RECEIVE ROD TOKEN INFORMATION
5.25.1 RECEIVE ROD TOKEN INFORMATION overview
The RECEIVE ROD TOKEN INFORMATION command (see SPC-6) provides a method for an application
client to receive information about the results of a previous or current block device ROD token operation.
Table 101 shows the operations and a reference to the subclause where each topic is described.
5.25.2 RECEIVE ROD TOKEN INFORMATION parameter data for POPULATE TOKEN command
If a RECEIVE ROD TOKEN INFORMATION command (see SPC-6) specifies a list identifier that matches the
list identifier specified in a previous POPULATE TOKEN command (see 5.12) received on the same I_T
nexus, then table 102 shows the parameter data returned by the copy manager.
Table 101 — RECEIVE ROD TOKEN INFORMATION reference
Command originating
the operation
Command
reference
RECEIVE ROD TOKEN INFORMATION
returned parameter data reference
POPULATE TOKEN
5.12
5.25.2
WRITE USING TOKEN
5.59
5.25.3


The AVAILABLE DATA field, the COPY OPERATION STATUS field, the OPERATION COUNTER field, the ESTIMATED
STATUS UPDATE DELAY field, the EXTENDED COPY COMPLETION STATUS field, the LENGTH OF THE SENSE DATA FIELD
field, SENSE DATA LENGTH field, the SENSE DATA field, and the ROD TOKEN field are defined in SPC-6.
Table 102 — RECEIVE ROD TOKEN INFORMATION parameter data for POPULATE TOKEN
Bit
Byte
(MSB)
AVAILABLE DATA (n - 3)
•••
(LSB)
Reserved
RESPONSE TO SERVICE ACTION (10h)
Reserved
COPY OPERATION STATUS
(MSB)
OPERATION COUNTER
(LSB)
(MSB)
ESTIMATED STATUS UPDATE DELAY
•••
(LSB)
EXTENDED COPY COMPLETION STATUS
LENGTH OF THE SENSE DATA FIELD (m - 31)
SENSE DATA LENGTH
TRANSFER COUNT UNITS (F1h)
(MSB)
TRANSFER COUNT
•••
(LSB)
(MSB)
SEGMENTS PROCESSED (0000h)
(LSB)
Reserved
•••
SENSE DATA (if any)
•••
m
m + 1
(MSB)
ROD TOKEN DESCRIPTOR LENGTH (n - (m + 4))
•••
m + 4
(LSB)
m + 5
Restricted (see SPC-6)
m + 6
m + 7
ROD TOKEN (if any)
•••
n


The RESPONSE TO SERVICE ACTION field is defined in SPC-6 and shall be set to the value shown in table 102 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
POPULATE TOKEN command.
The TRANSFER COUNT UNITS field is defined in SPC-6 and shall be set to the value shown in table 102 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
POPULATE TOKEN command.
The TRANSFER COUNT field indicates the number of contiguous logical blocks represented by the ROD token
that were read without error starting at the LBA specified in the first block device range descriptor and
including the LBAs described in all complete block device range descriptors of the POPULATE TOKEN
command to which this response applies.
If the value in the TRANSFER COUNT field is not equal to the sum of the contents of the NUMBER OF LOGICAL
BLOCKS fields in all of the complete block device range descriptors of the POPULATE TOKEN command to
which this response applies, then the COPY OPERATION STATUS field shall be set to 3h. Other values in the
COPY OPERATION STATUS field are defined in SPC-6.
The SEGMENTS PROCESSED field is defined in SPC-6 and shall be set to the value shown in table 102 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
POPULATE TOKEN command.
The ROD TOKEN DESCRIPTOR LENGTH field is defined in SPC-6 and shall be set to the size of the ROD TOKEN
field plus two in response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER
field specifies a POPULATE TOKEN command.


5.25.3 RECEIVE ROD TOKEN INFORMATION parameter data for WRITE USING TOKEN command
If a RECEIVE ROD TOKEN INFORMATION command (see SPC-6) specifies a list identifier that matches the
list identifier specified in a previous WRITE USING TOKEN command (see 5.59) received on the same I_T
nexus, then table 103 shows the parameter data returned by the copy manager.
The AVAILABLE DATA field, the COPY OPERATION STATUS field, the OPERATION COUNTER field, the ESTIMATED
STATUS UPDATE DELAY field, the EXTENDED COPY COMPLETION STATUS field, the LENGTH OF THE SENSE DATA FIELD
field, the SENSE DATA LENGTH field, and the SENSE DATA field are defined in SPC-6.
The RESPONSE TO SERVICE ACTION field is defined in SPC-6 and shall be set to the value shown in table 103 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
WRITE USING TOKEN command.
Table 103 — RECEIVE ROD TOKEN INFORMATION parameter data for WRITE USING TOKEN
Bit
Byte
(MSB)
AVAILABLE DATA (n - 3)
(LSB)
Reserved
RESPONSE TO SERVICE ACTION (11h)
Reserved
COPY OPERATION STATUS
(MSB)
OPERATION COUNTER
(LSB)
(MSB)
ESTIMATED STATUS UPDATE DELAY
•••
(LSB)
EXTENDED COPY COMPLETION STATUS
LENGTH OF THE SENSE DATA FIELD ((n - 4) - 31)
SENSE DATA LENGTH
TRANSFER COUNT UNITS (F1h)
(MSB)
TRANSFER COUNT
•••
(LSB)
(MSB)
SEGMENTS PROCESSED (0000h)
(LSB)
Reserved
•••
SENSE DATA (if any)
•••
n - 4
n - 3
Restricted (see SPC-6)
n


The TRANSFER COUNT UNITS field is defined in SPC-6 and shall be set to the value shown in table 103 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
WRITE USING TOKEN command.
The TRANSFER COUNT field indicates the number of contiguous logical blocks that were written without error
starting with the LBA specified in the first block device range descriptor and including the LBAs specified in all
block device range descriptors of the WRITE USING TOKEN command to which this response applies.
If the value in the TRANSFER COUNT field is not equal to the sum of the contents of the NUMBER OF LOGICAL
BLOCKS fields in all of the complete block device range descriptors of the WRITE USING TOKEN command to
which this response applies, then the COPY OPERATION STATUS field shall be set to 3h. Other values in the
COPY OPERATION STATUS field are defined in SPC-6.
The SEGMENTS PROCESSED field is defined in SPC-6 and shall be set to the value shown in table 103 in
response to a RECEIVE ROD TOKEN INFORMATION command in which the LIST IDENTIFIER field specifies a
POPULATE TOKEN command.
5.26 REMOVE ELEMENT AND TRUNCATE command
The REMOVE ELEMENT AND TRUNCATE command (see table 104) requests that the device server
perform a storage element depopulation (see 4.36.3).
If deferred microcode has been saved and not activated (see SPC-6), then the device server shall terminate
this command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT NOT READY, MICROCODE ACTIVATION REQUIRED.
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 104 for the REMOVE ELEMENT AND TRUNCATE command.
The REQUESTED CAPACITY field specifies the capacity in logical blocks (i.e. one greater than the number of
logical blocks returned by the READ CAPACITY command) of the media upon completion of the command. A
value of zero specifies that the device server shall choose the resultant capacity of the media. If the device
server is unable to set the capacity of the medium to the specified value, then the device server shall:
a)
not change the capacity of the media; and
b)
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB.
Table 104 — REMOVE ELEMENT AND TRUNCATE command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (18h)
(MSB)
REQUESTED CAPACITY
•••
(LSB)
(MSB)
ELEMENT IDENTIFIER
•••
(LSB)
Reserved
CONTROL
