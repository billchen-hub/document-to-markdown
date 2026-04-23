# 5.52 WRITE SAME (10) command

5.51 WRITE LONG (16) command
The WRITE LONG (16) command (see table 145) requests that the device server mark a logical block as
containing an error. If a cache contains the specified logical block, then the device server shall invalidate that
logical block in the cache.
This command uses the SERVICE ACTION OUT (16) CDB format (see clause A.2).
The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the values shown
in table 145 for the WRITE LONG (16) command.
See the WRITE LONG (10) command (see 5.50) for the definitions of the fields in this command.
5.52 WRITE SAME (10) command
The WRITE SAME (10) command (see table 146) requests that the device server transfer a single logical
block from the Data-Out Buffer and for each LBA in the specified range of LBAs:
a)
perform a write operation using the contents of that logical block; or
b)
perform an unmap operation.
The device server writes (i.e., subsequent read operations behave as if the device server wrote) the single
block of user data received from the Data-Out Buffer to each logical block without modification (see 4.7.3.4.4).
If the medium is formatted with protection information and the WRPROTECT field is set to 000b, then the device
server shall write the LOGICAL BLOCK GUARD field, APPLICATION TAG field, and LOGICAL BLOCK REFERENCE TAG
field (see 4.21) for each logical block as described in table 133 (i.e., code equal to 000b row of table 133).
If:
a)
the medium is formatted with protection information;
b)
the WRPROTECT field is not set to 000b or a reserved value (see table 133); and
c)
the protection information from the Data-Out Buffer is set to FFFF_FFFF_FFFF_FFFFh,
then the device server shall write FFFF_FFFF_FFFF_FFFFh to the protection information for each logical
block.
Table 145 — WRITE LONG (16) command
Bit
Byte
OPERATION CODE (9Fh)
Obsolete
WR_UNCOR
Obsolete
SERVICE ACTION (11h)
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
Reserved
Obsolete
Reserved
CONTROL


If:
a)
the medium is formatted with type 1 or type 2 protection information;
b)
the WRPROTECT field is not set to 000b or a reserved value (see table 133); and
c)
the protection information from the Data-Out Buffer is not set to FFFF_FFFF_FFFF_FFFFh,
then:
a)
the device server shall write the value from the LOGICAL BLOCK REFERENCE TAG field (see 4.21)
received in the logical block from the Data-Out Buffer into the corresponding LOGICAL BLOCK
REFERENCE TAG field of the first logical block written. The device server shall write the value of the
previous LOGICAL BLOCK REFERENCE TAG field plus one into each of the subsequent LOGICAL BLOCK
REFERENCE TAG fields;
b)
if the ATO bit is set to one in the Control mode page (see SPC-6) and the and the ATMPE bit is set to
zero in the Control mode page, then the device server shall write the logical block application tag
received in the logical block from the Data-Out Buffer into the corresponding LOGICAL BLOCK
APPLICATION TAG field (see 4.21) of each logical block;
c)
if the ATO bit is set to one in the Control mode page and the and the ATMPE bit is set to zero in the
Control mode page, then the device server shall write the value defined in the Application Tag mode
page (see 6.5.3) into the corresponding LOGICAL BLOCK APPLICATION TAG field of each logical block;
d)
if the ATO bit is set to zero in the Control mode page, then the device server may write any value into
the LOGICAL BLOCK APPLICATION TAG field of each logical block; and
e)
the device server shall write the value from the LOGICAL BLOCK GUARD field (see 4.21) received in the
logical block from the Data-Out Buffer into the corresponding LOGICAL BLOCK GUARD field of each
logical block.
If:
a)
the medium is formatted with type 3 protection information;
b)
the WRPROTECT field is not set to 000b or a reserved value (see table 133); and
c)
the protection information from the Data-Out Buffer is not set to FFFF_FFFF_FFFF_FFFFh,
then:
a)
if the ATO bit is set to one in the Control mode page (see SPC-6), then the device server shall write the
value from the LOGICAL BLOCK REFERENCE TAG field and the LOGICAL BLOCK APPLICATION TAG field
received in the logical block from the Data-Out Buffer into the corresponding LOGICAL BLOCK
REFERENCE TAG field of each logical block;
b)
if the ATO bit is set to zero in the Control mode page, then the device server may write any value into
the LOGICAL BLOCK REFERENCE TAG field of each logical block; and
c)
the device server shall write the value from the LOGICAL BLOCK GUARD field and the LOGICAL BLOCK
APPLICATION TAG field received in the logical block from the Data-Out Buffer into the corresponding
LOGICAL BLOCK GUARD field of each logical block.


NOTE 21 - Migration from the WRITE SAME (10) command to the WRITE SAME (16) command is
recommended for all implementations.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 146 for the
WRITE SAME (10) command.
See the WRITE (10) command (see 5.40) for the definition of the WRPROTECT field.
If the logical unit supports logical block provisioning management (see 4.7.3), then the ANCHOR bit in the CDB,
the UNMAP bit in the CDB, and the ANC_SUP bit (see 6.6.7) determine how the device server processes the
command as described in table 147.
Table 146 — WRITE SAME (10) command
Bit
Byte
OPERATION CODE (41h)
WRPROTECT
ANCHOR
UNMAP
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
Table 147 — UNMAP bit, ANCHOR bit, and ANC_SUP bit relationships
UNMAP bit a
ANCHOR bit
ANC_SUP bit b
Action
0 or 1
Write c
0 or 1
Error d
0 or 1
Deallocate request
(see 4.7.3.4.4)
Error d
Anchor request
(see 4.7.3.4.4)
a The device server in a logical unit that supports logical block provisioning management (see 4.7.3) may
implement the UNMAP bit.
b See the Logical Block Provisioning VPD page (see 6.6.7).
c The device server shall perform the specified write operation to each LBA specified by the command.
d The device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.


The device server shall ignore the UNMAP bit and the ANCHOR bit, or the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN CDB if:
a)
the logical unit is fully provisioned (i.e., the LBPME bit is set to zero in the READ CAPACITY (16)
parameter data (see 5.21.2)); and
b)
the UNMAP bit is set to one or the ANCHOR bit is set to one.
See the PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field.
See the PRE-FETCH (10) command (see 5.13) and 4.22 for the definition of the GROUP NUMBER field.
The NUMBER OF LOGICAL BLOCKS field specifies the number of contiguous logical blocks that are requested be
unmapped or written, starting with the logical block referenced by the LBA specified by the LOGICAL BLOCK
ADDRESS field.
If the NUMBER OF LOGICAL BLOCKS field is set to zero and:
a)
the WSNZ bit is set to zero (see 6.6.4), then the number of contiguous logical blocks that are requested
to be unmapped or written includes all of the logical blocks starting with the LBA specified in the
LOGICAL BLOCK ADDRESS field and ending with the last logical block on the medium; or
b)
the WSNZ bit is set to one, then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set
to INVALID FIELD IN CDB.
If the number of contiguous logical blocks requested to be unmapped or written by the NUMBER OF LOGICAL
BLOCKS field exceeds the value indicated in the MAXIMUM WRITE SAME LENGTH field (see 6.6.4), then the device
server shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB.
See the WRITE (10) command (see 5.40) for the definition of the CONTROL byte.
5.53 WRITE SAME (16) command
The WRITE SAME (16) command (see table 148) requests that the device server perform the actions defined
for the WRITE SAME (10) command (see 5.52).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 148 for the
WRITE SAME (16) command.
Table 148 — WRITE SAME (16) command
Bit
Byte
OPERATION CODE (93h)
WRPROTECT
ANCHOR
UNMAP
 Obsolete
NDOB
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
