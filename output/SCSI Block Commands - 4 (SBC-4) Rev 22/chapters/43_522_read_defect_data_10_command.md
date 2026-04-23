# 5.22 READ DEFECT DATA (10) command

The number of protection information intervals is calculated as follows:
number of protection information intervals = 2(p_i exponent)
where:
p_i exponent
is the contents of the P_I EXPONENT field.
The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field is shown in table 89.
A logical block provisioning management enabled (LBPME) bit set to one indicates that the logical unit
implements logical block provisioning management (i.e., is resource provisioned or thin provisioned)
(see 4.7.3). An LBPME bit set to zero indicates that the logical unit does not implement logical block
provisioning management (e.g., is fully provisioned (see 4.7.2)).
The logical block provisioning read zeros (LBPRZ) bit shall be set to one if the LBPRZ field (see 6.6.7) is set to
xx1b. The LBPRZ bit shall be set to zero if the LBPRZ field is not set to xx1b.
The LOWEST ALIGNED LOGICAL BLOCK ADDRESS field indicates the LBA of the first logical block that is located at
the beginning of a physical block (see 4.6).
5.22 READ DEFECT DATA (10) command
5.22.1 READ DEFECT DATA (10) command overview
The READ DEFECT DATA (10) command (see table 90) requests that the device server transfer parameter
data (see 5.22.2) containing a four-byte header, the PLIST, and/or the GLIST to the Data-In Buffer.
If the device server is unable to access a specified defect list as a result of a medium error, then the device
server shall terminate the command with CHECK CONDITION status with the sense key set to MEDIUM
ERROR and the additional sense code set to DEFECT LIST NOT FOUND.
If the device server is unable to access a specified defect list as a result of an error other than a medium error
or because a specified defect list does not exist, then the device server shall either:
1)
terminate the command with CHECK CONDITION status with the sense key set to NO SENSE and
the additional sense code set to DEFECT LIST NOT FOUND; or
2)
return only the READ DEFECT DATA parameter data header, with the DEFECT LIST LENGTH field set to
zero.
Device servers may or may not return a defect list until after a successful completion of a FORMAT UNIT
command (see 5.3).
NOTE 12 - Migration from the READ DEFECT DATA (10) command to the READ DEFECT DATA (12)
command is recommended for all implementations.
Table 89 — LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field
Code
Description
One or more physical blocks per logical block a
n > 0
2n logical blocks per physical block
a The number of physical blocks per logical block is not reported.


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 90 for the READ
DEFECT DATA (10) command.
Table 91 defines the request PLIST (REQ_PLIST) bit and the request GLIST (REQ_GLIST) bit.
The DEFECT LIST FORMAT field specifies the address descriptor format type (see 6.2) that the device server
should use for the defect list. A device server unable to return the requested address descriptor format shall
return the address descriptors in their default format and indicate that format type in the DEFECT LIST FORMAT
field in (see 5.22.2 and 5.23.2).
If the requested defect list format and the returned defect list format are not the same, then the device server
shall transfer the defect data and then terminate the command with CHECK CONDITION status with the
sense key set to RECOVERED ERROR and the additional sense code set to DEFECT LIST NOT FOUND.
The ALLOCATION LENGTH field is defined in SPC-6. If the length of the address descriptors that the device
server has to report is greater than the maximum value that is able to be specified by the ALLOCATION LENGTH
field, then the device server shall transfer no data and shall terminate the command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
CDB.
The CONTROL byte is defined in SAM-6.
Table 90 — READ DEFECT DATA (10) command
Bit
Byte
OPERATION CODE (37h)
Reserved
Reserved
REQ_PLIST
REQ_GLIST
DEFECT LIST FORMAT
Reserved
•••
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL
Table 91 — REQ_PLIST bit and REQ_GLIST bit
REQ_PLIST
REQ_GLIST
Description
The device server shall return only the first four bytes of the READ DEFECT
DATA parameter data (i.e., the parameter data header), with the DEFECT LIST
LENGTH field set to zero.
The device server shall return the READ DEFECT DATA parameter data header
and include the GLIST, if any, in the defect list.
The device server shall return the READ DEFECT DATA parameter
data header and include the PLIST, if any, in the defect list.
The device server shall return the READ DEFECT DATA parameter data header
and include the both the PLIST, if any, and the GLIST, if any, in the defect list.
Whether the PLIST and GLIST are merged or not is vendor specific.
