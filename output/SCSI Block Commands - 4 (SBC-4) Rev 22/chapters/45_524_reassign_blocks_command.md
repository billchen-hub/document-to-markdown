# 5.24 REASSIGN BLOCKS command

5.24 REASSIGN BLOCKS command
5.24.1 REASSIGN BLOCKS command overview
The REASSIGN BLOCKS command (see table 95) requests that the device server perform a reassign
operation on one or more LBAs (e.g., LBAs referencing logical blocks on which unrecovered read errors
occurred) to another area on the medium set aside for this purpose and to add the physical blocks containing
those logical blocks to the GLIST. This command shall not alter the contents of the PLIST (see 4.13).
The parameter list provided in the Data-Out Buffer contains a reassign LBA list that contains the LBAs of the
logical blocks to be reassigned. The device server shall reassign the parts of the medium used for each logical
block referenced by an LBA in the reassign LBA list. More than one physical block may be reassigned by each
LBA. If the device server recovers logical block data from the original logical block, then the device server
shall perform a write medium operation to that LBA using the recovered logical block data, which writes to the
logical block referenced by the reassigned LBA.
The device server shall invalidate any of the specified LBAs that are in cache.
If the device server does not recover logical block data in a fully provisioned logical unit (see 4.7.2), then the
device server shall:
a)
write vendor specific data as the user data, if the RBWZ bit is set to zero;
b)
write zeros as the user data, if the RBWZ bit is set to one; and
c)
write a default value of FFFF_FFFF_FFFF_FFFFh as the protection information, if enabled
(see 4.21.2).
If the device server does not recover logical block data in a resource provisioned logical unit (see 4.7.3.2) or a
thin provisioned logical unit (see 4.7.3.3), then the device server shall, for each specified LBA, either:
a)
unmap the specified LBA; or
b)
perform the following operations:
A) write vendor-specific data as the user data, if the RBWZ bit is set to zero;
B) write zeros as the user data, if the RBWZ bit is set to one; and
C) write a default value of FFFF_FFFF_FFFF_FFFFh as the protection information, if enabled.
The vendor-specific data written as user data may contain remnants of the original logical block (e.g., partially
or fully recovered user data).
The data in all other logical blocks on the medium shall be preserved.
Specifying an LBA to be reassigned that previously has been reassigned causes the device server to reassign
that LBA again.
If the device server terminates the REASSIGN BLOCKS command with CHECK CONDITION status, and the
sense data COMMAND-SPECIFIC INFORMATION field contains a valid LBA, then the application client should
remove all LBAs from the reassign LBA list prior to the one returned in the COMMAND-SPECIFIC INFORMATION
field. If the sense key is set to MEDIUM ERROR and the INFORMATION field contains the valid LBA, then the
application client should insert that LBA into the reassign LBA list and reissue the REASSIGN BLOCKS
command with the new reassign LBA list. Otherwise, the application client should perform any corrective
action indicated by the sense data and then reissue the REASSIGN BLOCKS command with the new
reassign LBA list.


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 95 for the
REASSIGN BLOCKS command.
A long LBA (LONGLBA) bit set to zero specifies that the reassign LBA list in the REASSIGN BLOCKS
parameter list (see 5.24.2) contains four-byte LBAs. A LONGLBA bit set to one specifies that the reassign LBA
list in the REASSIGN BLOCKS parameter list contains eight-byte LBAs.
A long list (LONGLIST) bit set to zero specifies the REASSIGN BLOCKS short parameter list header
(see table 97) is used. A LONGLIST bit set to one specifies the REASSIGN BLOCKS long parameter list header
(see table 98) is used.
The CONTROL byte is defined in SAM-6.
5.24.2 REASSIGN BLOCKS parameter list
The REASSIGN BLOCKS parameter list (see table 96) contains a four-byte parameter list header followed by
a reassign LBA list containing one or more LBAs.
Table 95 — REASSIGN BLOCKS command
Bit
Byte
OPERATION CODE (07h)
Reserved
LONGLBA
LONGLIST
Reserved
•••
CONTROL
Table 96 — REASSIGN BLOCKS parameter list
Bit
Byte
Parameter list header (see table 97 or table 98)
•••
Reassign LBA list (if any)
Reassign LBA [first] (see table 99 or table 100)
•••
7 or 11
n-4 or n-7
Reassign LBA [last] (see table 99 or table 100)
•••
n


The REASSSIGN BLOCKS short parameter list header is shown in table 97.
The REASSSIGN BLOCKS long parameter list header is shown in table 98.
The REASSIGN LBA LENGTH field specifies the total length in bytes of the reassign LBA list. The REASSIGN LBA
LENGTH field does not include the parameter list header length and is equal to:
a)
four times the number of LBAs, if the LONGLBA bit (see 5.24) is set to zero; or
b)
eight times the number of LBAs, if the LONGLBA bit is set to one.
The REASSIGN LBA LIST field contains a list of LBAs to be reassigned. The LBAs shall be sorted in ascending
order.
If the LONGLBA bit is set to zero, then table 99 defines the format of the reassigned LBA.
The REASSIGN LOGICAL BLOCK ADDRESS field specifies an LBA to be reassigned.
Table 97 — REASSIGN BLOCKS short parameter list header
Bit
Byte
Reserved
(MSB)
REASSIGN LBA LENGTH
(LSB)
Table 98 — REASSIGN BLOCKS long parameter list header
Bit
Byte
(MSB)
REASSIGN LBA LENGTH
•••
(LSB)
Table 99 — Reassign LBA if the LONGLBA bit is set to zero
Bit
Byte
(MSB)
REASSIGN LOGICAL BLOCK ADDRESS
•••
(LSB)


If the LONGLBA bit is set to one, then table 100 defines the reassign LBA.
The REASSIGN LOGICAL BLOCK ADDRESS field specifies an LBA to be reassigned.
If a specified LBA exceeds the capacity of the medium (see 4.5), then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code should be set to LOGICAL BLOCK ADDRESS OUT OF RANGE or may be set to INVALID FIELD
IN PARAMETER LIST.
If the direct access block device has insufficient capacity to reassign all of the specified LBAs, then the device
server shall terminate the command with CHECK CONDITION status with the sense key set to HARDWARE
ERROR and the additional sense code set to NO DEFECT SPARE LOCATION AVAILABLE.
If the direct access block device is unable to complete a REASSIGN BLOCKS command without error, then
the device server shall terminate the command with CHECK CONDITION status with the appropriate sense
data (see 4.18 and SPC-6).
If one or more LBAs are not reassigned, then the device server shall report the first LBA not reassigned in the
COMMAND-SPECIFIC INFORMATION field of the sense data (see SPC-6). If:
a)
information about the first LBA not reassigned is not available;
b)
all the LBAs have been reassigned; or
c)
the first LBA not reassigned does not fit in the COMMAND-SPECIFIC INFORMATION field, then the device
server shall report the following value in the COMMAND-SPECIFIC INFORMATION field of the sense data
(see SPC-6):
A) FFFF_FFFFh if fixed format sense data is being used; or
B) FFFF_FFFF_FFFF_FFFFh if descriptor format sense data is being used.
If the REASSIGN BLOCKS command failed as a result of an unexpected unrecovered read error that would
cause the loss of data in a logical block not specified in the reassign LBA list, then the LBA of the logical block
with the unrecovered read error is reported in the INFORMATION field of the sense data (see 4.18.1).
Table 100 — Reassign LBA if the LONGLBA bit is set to one
Bit
Byte
(MSB)
REASSIGN LOGICAL BLOCK ADDRESS
•••
(LSB)
