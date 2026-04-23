# 5.17 READ (12) command

is specifying that the logical blocks accessed by the command are not likely to be accessed again in the near
future and are not to be put in the cache nor retained by the cache. If the DPO bit is set to zero, then the
application client is specifying that the logical blocks accessed by this command are likely to be accessed
again in the near future.
A force unit access (FUA) bit set to one specifies that the device server shall read the logical blocks from:
a)
the specified data pattern for that LBA (e.g., the data pattern for unmapped data (see 4.7.4.4));
b)
the non-volatile cache, if any; or
c)
the medium.
If the FUA bit is set to one and a volatile cache contains a more recent version of a logical block than the
non-volatile cache, if any, or the medium, then, before reading the logical block, the device server shall write
the logical block to:
a)
the non-volatile cache, if any; or
b)
the medium.
An FUA bit set to zero specifies that the device server may read the logical blocks from:
a)
the volatile cache, if any;
b)
the specified data pattern for that LBA (e.g., the data pattern for unmapped data (see 4.7.4.4))
c)
the non-volatile cache, if any; or
d)
the medium.
If rebuild assist mode (see 4.19) is supported and not enabled, then the device server shall ignore the rebuild
assist recovery control (RARC) bit. If rebuild assist mode is supported and enabled, then the RARC bit specifies
that the device server shall perform read medium operations as defined in 4.19.3.2 and 4.19.3.3.
If the rebuild assist mode is not supported and the RARC bit is set to one, then the device server should
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN CDB.
See the PRE-FETCH (10) command (see 5.13) for the definition of the LOGICAL BLOCK ADDRESS field.
See the PRE-FETCH (10) command and 4.22 for the definition of the GROUP NUMBER field.
The TRANSFER LENGTH field specifies the number of contiguous logical blocks of data that shall be read and
transferred to the Data-In Buffer, starting with the logical block referenced by the LBA specified by the LOGICAL
BLOCK ADDRESS field. A TRANSFER LENGTH field set to zero specifies that no logical blocks shall be read or
transferred. This condition shall not be considered an error. Any other value specifies the number of logical
blocks that shall be read and transferred. If the specified LBA and the specified transfer length exceed the
capacity of the medium (see 4.5), then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
LOGICAL BLOCK ADDRESS OUT OF RANGE. The TRANSFER LENGTH field is constrained by the MAXIMUM
TRANSFER LENGTH field (see 6.6.4).
The CONTROL byte is defined in SAM-6.
5.17 READ (12) command
The READ (12) command (see table 80) requests that the device server perform the actions defined for the
READ (10) command (see 5.16).
NOTE 10 - Migration from the READ (12) command to the READ (16) command is recommended for all
implementations.


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 80 for the READ
(12) command.
The CONTROL byte is defined in SAM-6.
See the READ (10) command (see 5.16) for the definitions of the other fields in this command.
Table 80 — READ (12) command
Bit
Byte
OPERATION CODE (A8h)
RDPROTECT
DPO
FUA
RARC
Obsolete
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
Restricted
for
MMC-6
Reserved
GROUP NUMBER
CONTROL


5.18 READ (16) command
The READ (16) command (see table 81) requests that the device server perform the actions defined for the
READ (10) command (see 5.16).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 81 for the
READ (16) command.
The command duration  limit (see SAM-6) is indicated in the command duration limit descriptor (see SPC-6).
Which command duration limit descriptor, if any, applies to this command is specified by the DLD2 bit, the DLD1
bit, and the DLD0 bit, as shown in table 82. The CDLP field and the RWCDLP bit in the REPORT SUPPORTED
OPERATION CODES parameter data (see SPC-6) indicate that the command duration limit descriptor is in:
a)
the Command Duration Limit A mode page (see SPC-6);
b)
the Command Duration Limit B mode page (see SPC-6);
c)
the Command Duration Limit T2A mode page (see SPC-6); or
d)
the Command Duration Limit T2B mode page (see SPC-6).
Table 81 — READ (16) command
Bit
Byte
OPERATION CODE (88h)
RDPROTECT
DPO
FUA
RARC
Obsolete
DLD2
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
TRANSFER LENGTH
•••
(LSB)
DLD1
DLD0
GROUP NUMBER
CONTROL
Table 82 — Duration limit descriptor DLD bits
Duration limit descriptor bits
Description
DLD2
DLD1
DLD0
0b
0b
0b
Command is not a duration limited command (see SAM-6)
0b
0b
1b
First command duration limit descriptor
0b
1b
0b
Second command duration limit descriptor
0b
1b
1b
Third command duration limit descriptor
1b
0b
0b
Fourth command duration limit descriptor
1b
0b
1b
Fifth command duration limit descriptor
1b
1b
0b
Sixth command duration limit descriptor
1b
1b
1b
Seventh command duration limit descriptor


The CONTROL byte is defined in SAM-6.
See the READ (10) command (see 5.16) for the definitions of the other fields in this command.
5.19 READ (32) command
The READ (32) command (see table 83) requests that the device server perform the actions defined for the
READ (10) command (see 5.16).
The device server shall only process a READ (32) command if type 2 protection is enabled (see 4.21.2.4).
The OPERATION CODE field, the ADDITIONAL CDB LENGTH field, and the SERVICE ACTION field are defined in SPC-6
and shall be set to the values shown in table 83 for the READ (32) command.
The CONTROL byte is defined in SAM-6.
Table 83 — READ (32) command
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
SERVICE ACTION (0009h)
(LSB)
RDPROTECT
DPO
FUA
RARC
Obsolete
Reserved
Reserved
DLD2
DLD1
DD0
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
