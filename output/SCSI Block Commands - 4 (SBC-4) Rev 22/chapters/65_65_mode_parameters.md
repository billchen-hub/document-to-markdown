# 6.5 Mode parameters

6.5 Mode parameters
6.5.1 Mode pages overview
The mode pages and their corresponding page codes and subpage codes for direct access block devices are
shown in table 229. See 6.5.2 for a description of block descriptors.
Table 229 — Mode page codes and subpage codes for direct access block devices (part 1 of 2)
Mode page name
Page code
Subpage code
Reference
Application Tag
0Ah
02h
6.5.3
ATA Power Condition
1Ah
F1h
SAT-4
Background Control
1Ch
01h
6.5.4
Background Operation Control
0Ah
06h
6.5.5
Caching
08h
00h
6.5.6
Command Duration Limit A
0Ah
03h
SPC-6
Command Duration Limit B
0Ah
04h
SPC-6
Command Duration Limit T2A
0Ah
07h
SPC-6
Command Duration Limit T2B
0Ah
08h
SPC-6
Control
0Ah
00h
SPC-6
Control Extension
0Ah
01h
SPC-6
Disconnect-Reconnect
02h
00h
SPC-6
Enclosure Services Management a
14h
00h
SES-3
IO Advice Hints Grouping
0Ah
05h
6.5.7
Informational Exceptions Control
1Ch
00h
6.5.8
Logical Block Provisioning
1Ch
02h
6.5.9
PATA Control
0Ah
F1h
SAT-4
Power Condition
1Ah
00h
SPC-6
Power Consumption
1Ah
01h
SPC-6
Protocol-Specific Logical Unit
18h
00h
SPC-6
Protocol-Specific Port
19h
00h
SPC-6
Read-Write Error Recovery
01h
00h
6.5.10
Return all mode pages and subpages b
3Fh
FFh
SPC-6
Return all mode pages not including subpages b
3Fh
00h
SPC-6
Return all subpages for the specified mode page code b
00h to 3Eh
FFh
SPC-6
Note: SPC-6 contains a listing of mode page and subpage codes in numeric order.
a Valid only if the ENCSERV bit is set to one in the standard INQUIRY data (see SPC-6).
b Valid only for the MODE SENSE command.
c All subpage codes of the following mode page codes are obsolete: 03h, 04h, 05h, 09h, 0Bh, 0Ch, 0Dh,
and 10h.
d The following mode page code and subpage code combinations are vendor specific and do not require
a page format:
a)
mode page code 00h with subpage code 00h; and
b)
mode page codes 20h to 3Eh with all subpage codes.


The mode parameter list, including the mode parameter header, is described in SPC-6. Direct access block
devices support zero or one mode parameter block descriptors (i.e., the block descriptor is shared by all the
logical blocks on the medium) (see 6.5.2).
The MEDIUM TYPE field in the mode parameter header (see SPC-6) shall be set to 00h.
The DEVICE-SPECIFIC PARAMETER field in the mode parameter header (see SPC-6) for direct access block
devices is shown in table 230.
If the medium is write-protected (i.e., as a result of mechanisms outside the scope of this standard), or the
software write protect (SWP) bit in the Control mode page (see SPC-6) is set to one, then the device server
shall set the WP bit to one when returning a DEVICE-SPECIFIC PARAMETER field in response to a MODE SENSE
command. If the medium is not write-protected and the SWP bit is set to zero, then the device server shall set
the WP bit to zero when returning a DEVICE-SPECIFIC PARAMETER field in response to a MODE SENSE
command.
The write protect (WP) bit for mode data sent with a MODE SELECT command shall be ignored by the device
server.
The DPOFUA bit is reserved for mode data sent with a MODE SELECT command.
If the device server does not support the DPO bit and the FUA bit (see 4.15) being set to one, then the device
server shall set the DPO and FUA supported (DPOFUA) bit to zero when returning a DEVICE-SPECIFIC PARAMETER
field in response to a MODE SENSE command. If the device server supports the DPO bit and the FUA bit being
set to one, then the device server shall set the DPOFUA bit to one when returning a DEVICE-SPECIFIC PARAMETER
field in response to a MODE SENSE command.
Verify Error Recovery
07h
00h
6.5.11
Zoned Block Device Control
0Ah
0Fh
ZBC-2
Obsolete c
Vendor specific d
Reserved
all other page and subpage code
combinations for direct access block
devices
Table 230 — DEVICE-SPECIFIC PARAMETER field for direct access block devices
Bit
WP
Reserved
DPOFUA
Reserved
Table 229 — Mode page codes and subpage codes for direct access block devices (part 2 of 2)
Mode page name
Page code
Subpage code
Reference
Note: SPC-6 contains a listing of mode page and subpage codes in numeric order.
a Valid only if the ENCSERV bit is set to one in the standard INQUIRY data (see SPC-6).
b Valid only for the MODE SENSE command.
c All subpage codes of the following mode page codes are obsolete: 03h, 04h, 05h, 09h, 0Bh, 0Ch, 0Dh,
and 10h.
d The following mode page code and subpage code combinations are vendor specific and do not require
a page format:
a)
mode page code 00h with subpage code 00h; and
b)
mode page codes 20h to 3Eh with all subpage codes.


6.5.2 Mode parameter block descriptors
6.5.2.1 Mode parameter block descriptors overview
If a device server returns a mode parameter block descriptor, then the device server shall return a short LBA
mode parameter block descriptor (see 6.5.2.2) in the mode parameter data in response to:
a)
a MODE SENSE (6) command; or
b)
a MODE SENSE (10) command with the LLBAA bit set to zero.
 A device server may return a long LBA mode parameter block descriptor (see 6.5.2.3) in the mode parameter
data in response to a MODE SENSE (10) command with the LLBAA bit set to one.
If an application client sends a mode parameter block descriptor in the mode parameter list, then the
application client sends a short LBA mode parameter block descriptor (see 6.5.2.2) for a MODE SELECT (6)
command.
If an application client sends a mode parameter block descriptor in the mode parameter list, then the
application client may send a long LBA mode parameter block descriptor (see 6.5.2.3) for a MODE
SELECT (10) command.
Support for the mode parameter block descriptors is optional.
If the device server supports changing the block descriptor parameters by a MODE SELECT command, the
number of logical blocks is changed, and the Application Tag mode page is supported, then the device server
shall set:
a)
the current value of the ATMPE bit to zero in the Control mode page (see SPC-6); and
b)
the saved value, if saving is implemented, of the ATMPE bit to zero in the Control mode page.
If the device server supports changing the block descriptor parameters by a MODE SELECT command and
the number of logical blocks or the logical block length is changed, then the device server establishes a unit
attention condition of:
a)
CAPACITY DATA HAS CHANGED as described in 4.10; and
b)
MODE PARAMETERS CHANGED as described in SPC-6.
6.5.2.2 Short LBA mode parameter block descriptor
Table 231 defines the short LBA mode parameter block descriptor for direct access block devices used:
a)
with the MODE SELECT (6) and MODE SENSE (6) commands; and
b)
with the MODE SELECT (10) and MODE SENSE (10) commands when the LONGLBA bit is set to zero
in the mode parameter header (see SPC-6).
A device server shall respond to a MODE SENSE command (see SPC-6) by reporting the number of logical
blocks specified in the NUMBER OF LOGICAL BLOCKS field sent in the last MODE SELECT command that
Table 231 — Short LBA mode parameter block descriptor
Bit
Byte
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
Reserved
(MSB)
LOGICAL BLOCK LENGTH
•••
(LSB)


contained a mode parameter block descriptor. If no MODE SELECT command with a mode parameter block
descriptor has been received then the current number of logical blocks shall be returned. To determine the
number of logical blocks at which the logical unit is currently formatted, the application client shall use a READ
CAPACITY command (see 5.20 and 5.21) rather than the MODE SENSE command.
In response to a MODE SENSE command, the device server may return a value of zero indicating that it does
not report the number of logical blocks in the short LBA mode parameter block descriptor.
In response to a MODE SENSE command, if the number of logical blocks on the medium exceeds the
maximum value that is able to be specified in the NUMBER OF LOGICAL BLOCKS field, then the device server
shall return a value of FFFF_FFFFh.
If the logical unit does not support changing its capacity by changing the NUMBER OF LOGICAL BLOCKS field
using the MODE SELECT command (see SPC-6), then the value in the NUMBER OF LOGICAL BLOCKS field is
ignored. If the device supports changing its capacity by changing the NUMBER OF LOGICAL BLOCKS field, then
the NUMBER OF LOGICAL BLOCKS field is interpreted as follows:
a)
if the NUMBER OF LOGICAL BLOCKS field is set to zero, then the logical unit shall retain its current
capacity if the logical block length has not changed. If the NUMBER OF LOGICAL BLOCKS field is set to
zero and the content of the LOGICAL BLOCK LENGTH field (i.e., new logical block length) is different than
the current logical block length, then the logical unit shall be set to its maximum capacity when the
new logical block length takes effect (i.e., after a successful FORMAT UNIT command);
b)
if the NUMBER OF LOGICAL BLOCKS field is greater than zero and less than or equal to its maximum
capacity, then the logical unit shall be set to that number of logical blocks. If the content of the LOGICAL
BLOCK LENGTH field is the same as the current logical block length, then the logical unit shall not
become format corrupt. This capacity setting shall be retained through power cycles, hard resets,
logical unit resets, and I_T nexus losses. If the content of the LOGICAL BLOCK LENGTH field is the same
as the current logical block length, then this capacity setting shall take effect on successful completion
of the MODE SELECT command. If the content of the LOGICAL BLOCK LENGTH field (i.e., new logical
block length) is different than the current logical block length, then this capacity setting shall take
effect when the new logical block length takes effect (i.e., after a successful FORMAT UNIT
command);
c)
if the NUMBER OF LOGICAL BLOCKS field is set to a value greater than the maximum capacity of the
device and less than FFFF_FFFFh, then the device server shall terminate the MODE SELECT
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST. The logical unit shall retain its
previous logical block descriptor settings; or
d)
if the NUMBER OF LOGICAL BLOCKS field is set to FFFF_FFFFh, then the logical unit shall be set to its
maximum capacity. If the content of the LOGICAL BLOCK LENGTH field is the same as the current logical
block length, then the logical unit shall not become format corrupt. This capacity setting shall be
retained through power cycles, hard resets, logical unit resets, and I_T nexus losses. If the content of
the LOGICAL BLOCK LENGTH field is the same as the current logical block length, then this capacity
setting shall take effect on successful completion of the MODE SELECT command. If the content of
the LOGICAL BLOCK LENGTH field (i.e., new logical block length) is different than the current logical block
length, then this capacity setting shall take effect when the new logical block length takes effect (i.e.,
after a successful FORMAT UNIT command).
If the device server supports changing its logical unit’s capacity by changing the NUMBER OF LOGICAL BLOCKS
field, is in a logical unit that supports logical block provisioning management, and the capacity is increased,
then the additional LBAs shall be in the initial provisioning management condition as specified in 4.7.3.2 or
4.7.3.3.
The LOGICAL BLOCK LENGTH field specifies the length in bytes of user data in each logical block. No change
shall be made to any logical blocks on the medium until a format operation (see 5.4) is initiated by an
application client.
A device server shall respond to a MODE SENSE command (see SPC-6) by reporting the length of the logical
blocks as specified in the LOGICAL BLOCK LENGTH field sent in the last MODE SELECT command that
contained a mode parameter block descriptor (e.g., if the logical block length is 512 bytes and a MODE
SELECT command occurs with the LOGICAL BLOCK LENGTH field set to 520 bytes, any MODE SENSE


commands  returns 0000_0208h in the LOGICAL BLOCK LENGTH field). If no MODE SELECT command with a
block descriptor has been received then the current logical block length shall be returned. To determine the
logical block length at which the logical unit is currently formatted, the application client shall use a READ
CAPACITY command (see 5.20 and 5.21) rather than a MODE SENSE command.
6.5.2.3 Long LBA mode parameter block descriptor
Table 232 defines the long LBA mode parameter block descriptor for direct access block devices used with the
MODE SELECT (10) command and MODE SENSE (10) command when the LONGLBA bit is set to one in the
mode parameter header (see SPC-6).
A device server shall respond to a MODE SENSE command (see SPC-6) by reporting the number of logical
blocks specified in the NUMBER OF LOGICAL BLOCKS field sent in the last MODE SELECT command that
contained a mode parameter block descriptor. If no MODE SELECT command with a mode parameter block
descriptor has been received then the current number of logical blocks shall be returned. To determine the
number of logical blocks at which the logical unit is currently formatted, the application client shall use a READ
CAPACITY command (see 5.20 and 5.21) rather than a MODE SENSE command.
In response to a MODE SENSE command, the device server may return a value of zero indicating that it does
not report the number of logical blocks in the long LBA mode parameter block descriptor.
If the logical unit does not support changing its capacity by changing the NUMBER OF LOGICAL BLOCKS field
using the MODE SELECT command (see SPC-6), then the value in the NUMBER OF LOGICAL BLOCKS field is
ignored. If the device supports changing its capacity by changing the NUMBER OF LOGICAL BLOCKS field, then
the NUMBER OF LOGICAL BLOCKS field is interpreted as follows:
a)
if the NUMBER OF LOGICAL BLOCKS field is set to zero, then the logical unit shall retain its current
capacity if the logical block length has not changed. If the NUMBER OF LOGICAL BLOCKS field is set to
zero and the content of the LOGICAL BLOCK LENGTH field (i.e., new logical block length) is different than
the current logical block length, then the logical unit shall be set to its maximum capacity when the
new logical block length takes effect (i.e., after a successful FORMAT UNIT command);
b)
if the NUMBER OF LOGICAL BLOCKS field is greater than zero and less than or equal to its maximum
capacity, then the logical unit shall be set to that number of logical blocks. If the content of the LOGICAL
BLOCK LENGTH field is the same as the current logical block length, then the logical unit shall not
become format corrupt. This capacity setting shall be retained through power cycles, hard resets,
logical unit resets, and I_T nexus losses. If the content of the LOGICAL BLOCK LENGTH field is the same
as the current logical block length, then this capacity setting shall take effect on successful completion
of the MODE SELECT command. If the content of the LOGICAL BLOCK LENGTH field (i.e., new logical
block length) is different than the current logical block length, then this capacity setting shall take
effect when the new logical block length takes effect (i.e., after a successful FORMAT UNIT
command);
Table 232 — Long LBA mode parameter block descriptor
Bit
Byte
(MSB)
NUMBER OF LOGICAL BLOCKS
•••
(LSB)
Reserved
•••
(MSB)
LOGICAL BLOCK LENGTH
•••
(LSB)


c)
if the NUMBER OF LOGICAL BLOCKS field is set to a value greater than the maximum capacity of the
device and less than FFFF_FFFF_FFFF_FFFFh, then the device server shall terminate the MODE
SELECT command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN PARAMETER LIST. The logical unit shall
retain its previous block descriptor settings; or
d)
if the NUMBER OF LOGICAL BLOCKS field is set to FFFF_FFFF_FFFF_FFFFh, then the logical unit shall
be set to its maximum capacity. If the content of the LOGICAL BLOCK LENGTH field is the same as the
current logical block length, then the logical unit shall not become format corrupt. This capacity setting
shall be retained through power cycles, hard resets, logical unit resets, and I_T nexus losses. If the
content of the LOGICAL BLOCK LENGTH field is the same as the current logical block length, then this
capacity setting shall take effect on successful completion of the MODE SELECT command. If the
content of the LOGICAL BLOCK LENGTH field (i.e., new logical block length) is different than the current
logical block length, then this capacity setting shall take effect when the new logical block length takes
effect (i.e., after a successful FORMAT UNIT command).
If the device server supports changing its logical unit’s capacity by changing the NUMBER OF LOGICAL BLOCKS
field, supports logical block provisioning management, and the capacity is increased, then the additional LBAs
shall be in the initial provisioning management condition as specified in 4.7.3.2 or 4.7.3.3.
The LOGICAL BLOCK LENGTH field specifies the length in bytes of user data in each logical block. No change
shall be made to any logical blocks on the medium until a format operation (see 5.3) is initiated by an
application client.
A device server shall respond to a MODE SENSE command (see SPC-6) by reporting the length of the logical
blocks as specified in the LOGICAL BLOCK LENGTH field sent in the last MODE SELECT command that
contained a mode parameter block descriptor (e.g., if the logical block length is 512 bytes and a MODE
SELECT command occurs with the LOGICAL BLOCK LENGTH field set to 520 bytes, any MODE SENSE
commands returns 0000_0208h in the LOGICAL BLOCK LENGTH field). If no MODE SELECT command with a
block descriptor has been received then the current logical block length shall be returned. To determine the
logical block length at which the logical unit is currently formatted, the application client shall use a READ
CAPACITY command (see 5.20 and 5.21) rather than a MODE SELECT command.
6.5.3 Application Tag mode page
6.5.3.1 Overview
The Application Tag mode page (see table 233) specifies the logical block application tag that a device server
configured for protection information (see 4.21.2) shall use for each LBA range if:
a)
the ATO bit in the Control mode page (see SPC-6) is set to one;
b)
the ATMPE bit in the Control mode page (see SPC-6) is set to one; and
c)
the WRPROTECT field requirements (see table 133) specify use of the Application tag mode page.
The mode page policy (see SPC-6) for this page shall be shared.


If a method not defined by this standard changes the parameter data to be returned by the device server in the
Application Tag mode page, then the device server shall establish a unit attention condition for the SCSI
initiator port associated with every I_T nexus with the additional sense code set to MODE PARAMETERS
CHANGED.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field,
and the PAGE LENGTH field are defined in SPC-6.
The SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in table 233 for
the Application Tag mode page.
The application tag descriptor is defined in 6.5.3.2.
Table 233 — Application Tag mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (0Ah)
SUBPAGE CODE (02h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Reserved
•••
Application tag descriptors
Application tag descriptor [first] (see 6.5.3.2)
•••
•••
n - 24
Application tag descriptor [last] (see 6.5.3.2)
•••
n


6.5.3.2 Application tag descriptor
The application tag descriptor format is shown in table 234.
A LAST bit set to one specifies that this application tag descriptor is the last valid application tag descriptor in
the Application Tag mode page. A LAST bit set to zero specifies that the application tag descriptor is not the
last valid application tag descriptor in the Application Tag mode page.
The LOGICAL BLOCK APPLICATION TAG field specifies the value to be compared with the LOGICAL BLOCK
APPLICATION TAG field associated with an LBA within the range specified by the LOGICAL BLOCK ADDRESS field
and the LOGICAL BLOCK COUNT field within this descriptor.
The LOGICAL BLOCK ADDRESS field contains the starting LBA for this application tag descriptor. The LOGICAL
BLOCK ADDRESS field in the first Application tag descriptor shall be set to 0000_0000_0000_0000h. For
subsequent application tag descriptors in which the LOGICAL BLOCK COUNT field is not set to zero, the contents
of the LOGICAL BLOCK ADDRESS field shall contain the sum of the values in:
a)
the LOGICAL BLOCK ADDRESS field in the previous application tag descriptor; and
b)
the LOGICAL BLOCK COUNT field in the previous application tag descriptor.
For the application tag descriptor with the LAST bit set to one, the sum of the LOGICAL BLOCK ADDRESS field and
the LOGICAL BLOCK COUNT field shall equal the RETURNED LOGICAL BLOCK ADDRESS field (see 5.21.2).
If an invalid combination of the LAST bit, LOGICAL BLOCK APPLICATION TAG field, and LOGICAL BLOCK ADDRESS
field are sent by the application client, then the device server shall terminate the MODE SELECT command
(see SPC-6) with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
The LOGICAL BLOCK COUNT field specifies the number of logical blocks to which this application tag descriptor
applies.
A LOGICAL BLOCK COUNT field set to 0000_0000_0000_0000h specifies that this application tag descriptor shall
be ignored.
Table 234 — Application tag descriptor format
Bit
Byte
LAST
Reserved
Reserved
•••
(MSB)
LOGICAL BLOCK APPLICATION TAG
(LSB)
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
LOGICAL BLOCK COUNT
•••
(LSB)


6.5.4 Background Control mode page
The Background Control mode page (see table 235) provides controls over background scan operations
(see 4.23). The mode page policy (see SPC-6) for this subpage shall be shared.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field,
and the PAGE LENGTH field are defined in SPC-6.
The SPF bit, the PAGE CODE field, the SUBPAGE CODE field, and the PAGE LENGTH field shall be set to the values
shown in table 235 for the Background Control mode page.
A suspend on log full (S_L_FULL) bit set to zero specifies that the device server shall continue running a
background scan operation (see 4.23.1) even if the Background Scan Results log page (see 6.4.2) contains
the maximum number of Background Scan log parameters (see 6.4.2.3) supported by the logical unit. A
S_L_FULL bit set to one specifies that the device server shall suspend a background scan operation if the
Background Scan Results log page contains the maximum number of Background scan log parameters
supported by the logical unit.
A log only when intervention required (LOWIR) bit set to zero specifies that the device server shall log all
suspected recoverable medium errors or unrecoverable medium errors that are identified during background
scan operations in the Background Scan Results log page. A LOWIR bit set to one specifies that the device
server shall only log medium errors identified during background scan operations in the Background Scan
Results log page that require application client intervention.
An enable background medium scan (EN_BMS) bit set to zero specifies that the device server shall disable
background medium scan operations (see 4.23.3). An EN_BMS bit set to one specifies that the device server
shall enable background medium scan operations. If the EN_PS bit is also set to one, and a background
pre-scan operation is in progress, then the logical unit shall not start a background medium scan operation
until after the background pre-scan operation is halted or completed. If a background medium scan operation
is in progress when the EN_BMS bit is changed from one to zero, then the logical unit shall suspend the
Table 235 — Background Control mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (1Ch)
SUBPAGE CODE (01h)
(MSB)
PAGE LENGTH (000Ch)
(LSB)
Reserved
S_L_FULL
LOWIR
EN_BMS
Reserved
EN_PS
(MSB)
BACKGROUND MEDIUM SCAN INTERVAL TIME
(LSB)
(MSB)
BACKGROUND PRE-SCAN TIME LIMIT
(LSB)
(MSB)
MINIMUM IDLE TIME BEFORE BACKGROUND SCAN
(LSB)
(MSB)
MAXIMUM TIME TO SUSPEND BACKGROUND SCAN
(LSB)
Reserved


background medium scan operation before the device server completes the MODE SELECT command, and
the background medium scan shall remain suspended until the EN_BMS bit is set to one, at which time the
logical unit shall resume the background medium scan operation beginning with the logical block being tested
when the background medium scan operation was suspended.
An enable pre-scan (EN_PS) bit set to zero specifies that the device server shall disable background pre-scan
operations (see 4.23.2). If a background pre-scan operation is in progress when the EN_PS bit is changed from
a one to a zero, then the logical unit shall halt the background pre-scan operation before the device server
completes the MODE SELECT command. An EN_PS bit set to one specifies that the logical unit shall start a
background pre-scan operation after the next power on. Once a logical unit has completed a background
pre-scan operation, the logical unit shall not perform another background pre-scan operation unless the EN_PS
bit is set to zero, then set to one, and another power on occurs.
The BACKGROUND MEDIUM SCAN INTERVAL TIME field specifies the minimum time, in hours, between the start of
one background scan operation and the start of the next background medium scan operation. If the current
background scan operation takes longer than the value specified in the BACKGROUND MEDIUM SCAN INTERVAL
TIME field, then the logical unit shall:
a)
continue the current background scan operation until that background scan operation is complete;
and
b)
start the next background medium scan operation upon completion of the current background scan
operation.
The BACKGROUND PRE-SCAN TIME LIMIT field specifies the maximum time, in hours, for a background pre-scan
operation to complete. If the background pre-scan operation does not complete within the specified time then
the device server shall halt the background pre-scan operation. A value of zero specifies an unlimited timeout
value.
The MINIMUM IDLE TIME BEFORE BACKGROUND SCAN field specifies the time, in milliseconds, that the logical unit
shall be idle before resuming a background scan operation (e.g., after the device server has completed all of
the commands in all task sets).
The MAXIMUM TIME TO SUSPEND BACKGROUND SCAN field specifies the time, in milliseconds, that the device
server should take to start processing a command received while a logical unit is performing a background
scan operation.
6.5.5 Background Operation Control mode page
The Background Operation Control mode page (see table 236) provides controls of device server background
operation.
The PS bit is described in SPC-6.
Table 236 — Background Operation Control mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (0Ah)
SUBPAGE CODE (06h)
PAGE LENGTH (01FDh)
BO_MODE
Reserved
Reserved
•••


The SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in SPC-6 and shall be
set as shown in table 236 for the Background Operation Control mode page.
The background operation mode (BO_MODE) field specifies how host initiated advanced background
operations shall operate during read operations or write operations as shown in table 237.
6.5.6 Caching mode page
The Caching mode page (see table 238) defines the parameters that affect the use of the cache.
Table 237 — BO_MODE field
Code
Description
00b
Host initiated advanced background operation shall be suspended
during read operations and write operations and resume advanced
background operation when read operations and write operations are
complete.
01b
Host initiated advanced background operation shall continue during
read operations and write operations.
All others
Reserved
Table 238 — Caching mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (08h)
PAGE LENGTH (12h)
IC
ABPF
CAP
DISC
SIZE
WCE
MF
RCD
DEMAND READ RETENTION PRIORITY
WRITE RETENTION PRIORITY
(MSB)
DISABLE PRE-FETCH TRANSFER LENGTH
(LSB)
(MSB)
MINIMUM PRE-FETCH
(LSB)
(MSB)
MAXIMUM PRE-FETCH
(LSB)
(MSB)
MAXIMUM PRE-FETCH CEILING
(LSB)
FSW
LBCSS
DRA
Vendor specific
SYNC_PROG
NV_DIS
NUMBER OF CACHE SEGMENTS
(MSB)
CACHE SEGMENT SIZE
(LSB)
Reserved
Obsolete
•••


The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field,  and the PAGE LENGTH
field are defined in SPC-6.
The SPF bit, the PAGE CODE field, and the PAGE LENGTH field shall be set to the values shown in table 238 for
the Caching mode page.
An initiator control (IC) enable bit set to one specifies that the device server use one of the following fields to
control the caching algorithm rather than the device server’s own adaptive algorithm:
a)
the NUMBER OF CACHE SEGMENTS field, if the SIZE bit is set to zero; or
b)
the CACHE SEGMENT SIZE field, if the SIZE bit is set to one.
An abort pre-fetch (ABPF) bit set to one and a DRA bit is set to zero specify that the device server abort a
pre-fetch upon receipt of a new command. An ABPF bit set to one takes precedence over the value specified in
the MINIMUM PRE-FETCH field. An ABPF bit set to zero and a DRA bit set to zero specify that the termination of
any active pre-fetch is dependent upon Caching mode page bytes 4 through 11 and is vendor specific.
A caching analysis permitted (CAP) bit set to one specifies that the device server perform caching analysis
during subsequent operations. A CAP bit set to zero specifies that caching analysis be disabled (e.g., to reduce
overhead time or to prevent nonpertinent operations from impacting tuning values).
A discontinuity (DISC) bit set to one specifies that the device server continue the pre-fetch across time
discontinuities (e.g., across cylinders) up to the limits of the buffer, or segment, space available for the
pre-fetch. A DISC bit set to zero specifies that pre-fetches be truncated or wrapped at time discontinuities.
A size enable (SIZE) bit set to one specifies that the CACHE SEGMENT SIZE field be used to control caching
segmentation. A SIZE bit set to zero specifies that the NUMBER OF CACHE SEGMENTS field be used to control
caching segmentation. Simultaneous use of both the number of segments and the segment size is vendor
specific.
A writeback cache enable (WCE) bit set to one specifies that the device server shall perform write operations
by using write cache operations to volatile write cache, write cache operations to non-volatile cache, or write
medium operations (e.g., a write command is able to complete without error after logical block data has been
written to volatile cache but has not necessarily been written to the medium) as described in 4.15. A WCE bit
set to zero specifies that the device server shall complete a write command without error only after all logical
block data has been written without error by performing write cache operations to non-volatile cache or by
performing write medium operations to non-volatile medium. If an application client changes the WCE bit from
one to zero via a MODE SELECT command, then the device server shall perform write medium operations to
any LBAs in cache containing logical block data that is not the same as the logical block data referenced by
the corresponding LBAs on the medium before completing the MODE SELECT command.
A multiplication factor (MF) bit set to zero specifies that the device server shall interpret the MINIMUM PRE-FETCH
field and the MAXIMUM PRE-FETCH field in terms of the number of logical blocks for each of the respective types
of pre-fetch. An MF bit set to one specifies that the device server shall interpret the MINIMUM PRE-FETCH field
and the MAXIMUM PRE-FETCH field to be specified in terms of a scalar number that, when multiplied by the
number of logical blocks to be transferred for the current command, yields the number of logical blocks for
each of the respective types of pre-fetch.
A read cache disable (RCD) bit set to zero specifies that the device server shall perform read operations by
using read cache operations or read medium operations as described in 4.15. An RCD bit set to one specifies
that the device server shall perform read operations by only using read medium operations.


The DEMAND READ RETENTION PRIORITY field (see table 239) specifies the retention priority the device server
should assign for data read into the cache that has also been transferred to the Data-In Buffer.
The WRITE RETENTION PRIORITY field (see table 240) specifies the retention priority the device server should
assign for data written into the cache that has also been transferred from the cache to the medium.
An anticipatory pre-fetch occurs when data is placed in the cache that has not been requested. This may
happen in conjunction with the reading of data that has been requested. The DISABLE PRE-FETCH TRANSFER
LENGTH field, the MINIMUM PRE-FETCH field, the MAXIMUM PRE-FETCH field, and the MAXIMUM PRE-FETCH CEILING
field give an indication to the device server how it should manage the cache based on the most recent READ
command. An anticipatory pre-fetch may occur based on other information. These fields are only
recommendations to the device server and should not cause a CHECK CONDITION to occur if the device
server is not able to satisfy the request.
The DISABLE PRE-FETCH TRANSFER LENGTH field specifies the selective disabling of anticipatory pre-fetch on
long transfer lengths. The value in this field is compared to the transfer length requested by a READ
command. If the transfer length is greater than the disable pre-fetch transfer length, then an anticipatory
pre-fetch is not done for the command. Otherwise the device server should attempt an anticipatory pre-fetch.
If the DISABLE PRE-FETCH TRANSFER LENGTH field is set to zero, then all anticipatory pre-fetching is disabled for
any request for data, including those with a transfer length of zero.
The MINIMUM PRE-FETCH field specifies the number of logical blocks to pre-fetch regardless of the delays that
may be incurred in processing subsequent commands. The field contains either:
a)
a number of logical blocks, if the MF bit is set to zero; or
b)
a scalar multiplier of the value in the TRANSFER LENGTH field, if the MF bit is set to one.
The pre-fetching operation begins at the logical block after the last logical block of a READ command.
Pre-fetching shall always halt when it reaches the last logical block on the medium. Errors that occur during
the pre-fetching operation shall not be reported to the application client unless the device server is unable to
Table 239 — DEMAND READ RETENTION PRIORITY field
Code
Description
0h
The device server should not distinguish between retaining the indicated data and data placed
into the cache by other means (e.g., pre-fetch).
1h
The device server should replace data put into the cache via a READ command sooner (i.e.,
read data has lower priority) than data placed into the cache by other means (e.g., pre-fetch).
2h to Eh
Reserved
Fh
The device server should replace data placed into the cache by other means (e.g., pre-fetch)
sooner than data put into the cache via a READ command (i.e., read data has higher priority).
Table 240 — WRITE RETENTION PRIORITY field
Code
Description
0h
The device server should not distinguish between retaining the indicated data and data placed
into the cache by other means (e.g., pre-fetch).
1h
The device server should replace data put into the cache during a WRITE command or a
WRITE AND VERIFY command sooner (i.e., has lower priority) than data placed into the cache
by other means (e.g., pre-fetch).
2h to Eh
Reserved
Fh
The device server should replace data placed into the cache by other means (e.g., pre-fetch)
sooner than data put into the cache during a WRITE command or a WRITE AND VERIFY
command (i.e., has higher priority).


process subsequent commands correctly as a result of the error. In this case the error may be reported either
as:
a)
an error for that subsequent command; or
b)
a deferred error,
at the discretion of the device server and according to the rules for reporting deferred errors (see SPC-6).
If the pre-fetch has read more than the amount of data specified by the MINIMUM PRE-FETCH field, then
pre-fetching should be terminated whenever another command enters the enabled state (see SAM-6). This
requirement is ignored if the MINIMUM PRE-FETCH field value is equal to the MAXIMUM PRE-FETCH field value.
The MAXIMUM PRE-FETCH field specifies the number of logical blocks to pre-fetch if the pre-fetch does not delay
processing of subsequent commands. The field contains either:
a)
a number of logical blocks, if the MF bit is set to zero; or
b)
a scalar multiplier of the value in the TRANSFER LENGTH field, if the MF bit is set to one.
The MAXIMUM PRE-FETCH field contains the maximum amount of data to pre-fetch as a result of one READ
command. The MAXIMUM PRE-FETCH field is used in conjunction with the DISABLE PRE-FETCH TRANSFER LENGTH
field and MAXIMUM PRE- FETCH CEILING field to trade off pre-fetching new data with displacing old data already
stored in the cache.
The MAXIMUM PRE-FETCH CEILING field specifies an upper limit on the number of logical blocks computed as the
maximum pre-fetch. If this number of logical blocks is greater than the value in the MAXIMUM PRE-FETCH field,
then the number of logical blocks to pre-fetch shall be truncated to the value stored in the MAXIMUM PRE-FETCH
CEILING field.
NOTE 22 - If the MF bit is set to one, then the MAXIMUM PRE-FETCH CEILING field is useful in limiting the amount
of data to be pre-fetched.
A force sequential write (FSW) bit set to one specifies that, for commands requesting write operations to more
than one logical block, the device server shall write the logical blocks to the medium in ascending sequential
order. An FSW bit set to zero specifies that the device server may reorder the sequence of writing logical
blocks to the medium (e.g., in order to achieve faster command completion).
A logical block cache segment size (LBCSS) bit set to one specifies that the CACHE SEGMENT SIZE field units
shall be interpreted as logical blocks. An LBCSS bit set to zero specifies that the CACHE SEGMENT SIZE field units
shall be interpreted as bytes. The LBCSS bit shall not impact the units of other fields.
A disable read-ahead (DRA) bit set to one specifies that the device server shall not read into the pre-fetch
buffer any logical blocks beyond the addressed logical block(s). A DRA bit set to zero specifies that the device
server may continue to read logical blocks into the pre-fetch buffer beyond the addressed logical block(s).


The synchronize cache progress indication support (SYNC_PROG) field (see table 241) specifies device server
progress indication reporting while a SYNCHRONIZE CACHE command (see 5.33 and 5.34) is being
processed.
An NV_DIS bit set to one specifies that the device server shall disable a non-volatile cache and indicates that a
non-volatile cache is supported but disabled. An NV_DIS bit set to zero specifies that the device server may
use a non-volatile cache and indicates that a non-volatile cache may be present and enabled.
The NUMBER OF CACHE SEGMENTS field specifies the number of segments into which the device server shall
divide the cache.
The CACHE SEGMENT SIZE field specifies the segment size in bytes if the LBCSS bit is set to zero or in logical
blocks if the LBCSS bit is set to one. The CACHE SEGMENT SIZE field is valid only if the SIZE bit is set to one.
6.5.7 IO Advice Hints Grouping mode page
The IO Advice Hints Grouping mode page (see table 242) provides the application client with the means to
obtain or modify the IO advice hints of the logical unit and the group number associated with those IO advice
hints.
Table 241 — SYNC_PROG field
Code
Description
00b
The device server shall not terminate commands as a result of the synchronize cache operation
and shall not provide pollable sense data.
01b
The device server:
a)
shall not terminate commands as a result of the synchronize cache operation; and
b)
shall provide pollable sense data with the sense key set to NO SENSE, the additional sense
code set to SYNCHRONIZE CACHE OPERATION IN PROGRESS, and the PROGRESS
INDICATION field set to indicate the progress of the synchronize cache operation.
10b
The device server:
a)
shall process INQUIRY commands, REPORT LUNS commands, REPORT TARGET PORT
GROUPS commands, and REQUEST SENSE commands;
b)
may process commands that do not require resources used for the synchronize cache
operation;
c)
shall terminate commands that require resources used for the synchronize cache operation
with CHECK CONDITION status with the sense key set to NOT READY, the additional sense
code set to LOGICAL UNIT NOT READY, SYNCHRONIZE CACHE OPERATION IN
PROGRESS, and the PROGRESS INDICATION field set to indicate the progress of the
synchronize cache operation; and
d)
shall provide pollable sense data with the sense key set to NOT READY, the additional sense
code set to LOGICAL UNIT NOT READY, SYNCHRONIZE CACHE OPERATION IN
PROGRESS, and the PROGRESS INDICATION field set to indicate the progress of the
synchronize cache operation.
11b
Reserved


The mode page policy (see SPC-6) for this page shall be shared.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field,
and the PAGE LENGTH field are defined in SPC-6.
The SPF bit, the PAGE CODE field, the SUBPAGE CODE field, and the PAGE LENGTH field shall be set to the values
shown in table 242 for the IO Advice Hints Grouping mode page.
Table 242 — IO Advice Hints Grouping mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (0Ah)
SUBPAGE CODE (05h)
(MSB)
PAGE LENGTH (40Ch)
(LSB)
Reserved
•••
IO advice hints group descriptor list
IO advice hints group descriptor (group 0) (see table 243)
•••
•••
IO advice hints group descriptor (group 63) (see table 243)
•••


An IO advice hints group descriptor (see table 243) is provided for each group number. The logical block
markup descriptor (see 6.8) in each IO advice hints group descriptor affects the processing of commands as
described in 4.22.2.
The IO ADVICE HINTS MODE field specifies the mode of the logical block markup descriptor and is described in
table 244.
The cache segment enable (CS_ENBLE) bit specifies whether cache segments (see 4.15.2) are associated
with the cache ID that is the group number associated with this IO advice hints group descriptor. If the
CS_ENBLE bit is set to zero, then no independent cache segments are associated with the cache ID for the
group number associated with this IO advice hints group descriptor. If the CS_ENBLE bit is set to one, then
independent cache segments are associated with the cache ID for the group number associated with this IO
advice hints group descriptor.
The information collection enable (IC_ENABLE) bit specifies whether the information collection function
(see 4.22.1) for the group associated with this IO advice hints group descriptor is enabled. If the IC_ENABLE bit
is set to zero, then the information collection function for the group associated with this IO advice hints group
descriptor is not enabled. If the IC_ENABLE bit is set to one, then the information collection function for the
group associated with this IO advice hints group descriptor is enabled.
If the Group Statistics and Performance (n) log pages are not supported, then in the IO advice hints group
descriptors for group 0 to group 31, the IC_ENABLE bit shall be set to zero and shall not be changeable.
In the IO advice hints group descriptors for group 32 to group 63, the IC_ENABLE bit shall be set to zero, and
shall not be changeable.
The logical block markup descriptor is described in 6.8.
Table 243 — IO advice hints group descriptor
Bit
Byte
IO ADVICE HINTS MODE
Reserved
CS_ENBLE
IC_ENABLE
Reserved
•••
(MSB)
lLogical block markup descriptor (see 6.8)
•••
p-1
(LSB)
p
Pad (if any)
•••
Table 244 — IO ADVICE HINTS MODE field
Code
Description
00b
The logical block markup descriptor is valid (see 4.22.2).
01b
The logical block markup descriptor is invalid (see 4.22.2).
all others
Reserved


6.5.8 Informational Exceptions Control mode page
The Informational Exceptions Control mode page (see table 245) defines the methods used by the device
server to control the processing and reporting of informational exception conditions. Informational exception
conditions are defined as any event that the device server reports or logs as failure predictions (i.e., with the
ADDITIONAL SENSE CODE field set to 5Dh (e.g., FAILURE PREDICTION THRESHOLD EXCEEDED)) or
warnings (i.e., with the ADDITIONAL SENSE CODE field set to 0Bh (e.g., WARNING)).
Informational exception conditions may occur while a logical unit is processing:
a)
a background self-test (see SPC-6);
b)
device specific background functions (see SPC-6);
c)
a command; or
d)
other device specific events.
An informational exception condition may occur at any time (e.g., the condition may be asynchronous to any
commands issued by an application client).
The mode page policy for this mode page shall be shared or per I_T nexus (see SPC-6).
Storage devices that support SMART (Self-Monitoring Analysis and Reporting Technology) for predictive
failure software should use informational exception conditions.
The PS bit, the SPF bit, the PAGE CODE field, and the PAGE LENGTH field are described in SPC-6.
The SPF bit, the PAGE CODE field, and the PAGE LENGTH field shall be set to the values shown in table 245 for
the Informational Exceptions Control mode page.
If the performance (PERF) bit is set to zero, then the device server may process informational exception
conditions that cause delays in processing other operations (e.g., processing a command). If the PERF bit is
set to one, then the device server shall not process informational exception conditions that cause delays in
processing other operations. A PERF bit set to one may cause the device server to disable some or all of the
processing of informational exception conditions, thereby limiting the reporting of informational exception
conditions.
If device specific background functions (see SPC-6) are implemented by the logical unit, and the enable
background function (EBF) bit is set to one, then the device server shall enable device specific background
functions. If the EBF bit is set to zero, then the device server shall disable device specific background
functions. Background functions with separate enable control bits (e.g., the background medium scan
(see 4.23)) are not controlled by the EBF bit.
The enable warning (EWASC) bit specifies if the device server enables reporting of warnings (see table 246).
Table 245 — Informational Exceptions Control mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (1Ch)
PAGE LENGTH (0Ah)
PERF
Reserved
EBF
EWASC
DEXCPT
TEST
EBACKERR
LOGERR
Reserved
MRIE
(MSB)
INTERVAL TIMER
•••
(LSB)
(MSB)
REPORT COUNT
•••
(LSB)


The disable exception control (DEXCPT) bit specifies if the device server disables reporting of failure
predictions (see table 246).
The TEST bit specifies if the device server creates a test device failure prediction (see table 246).
If an informational exception condition occurs that is not the result of the logical unit processing a background
self-test (see SPC-6) or device specific background function (see SPC-6), then the device server:
a)
shall use the definitions for the combination of the values in the EWASC bit, the DEXCPT bit, and the
TEST bit shown in table 246 for processing informational exception conditions if the MRIE field is set
from 2h to 6h;
b)
may use the definitions for the combination of the values in the EWASC bit, the DEXCPT bit, and the
TEST bit shown table 246 for processing informational exception conditions if the MRIE field is set from
Ch to Fh; and
c)
shall ignore the EWASC bit, the DEXCPT bit, and the TEST bit if the MRIE field is set to any value other
than 2h to 6h or Ch to Fh.
If an informational exception condition occurs while the logical unit is processing a background self-test
(see SPC-6) or background function (see SPC-6), then the enable background error (EBACKERR) bit
determines how the device server processes the informational exception as defined in the following:
a)
if the EBACKERR bit is set to zero, then the device server shall disable reporting of informational
exception conditions that occur during the processing of background self-tests and background
functions;
b)
if the EBACKERR bit is set to one, then, for informational exception conditions that occur during the
processing of background self-tests and background functions, the device server shall:
A) enable reporting of the informational exception conditions;
B) use the method for reporting the informational exception conditions as determined by contents of
the MRIE field; and
Table 246 — Definitions for the combinations of values in EWASC, DEXCPT, and TEST
EWASC DEXCPT
TEST
Description
The device server shall process informational exception conditions as follows:
a)
failure prediction processing shall be enabled a; and
b)
warning processing shall be disabled.
The device server shall process informational exception conditions as follows:
a)
failure prediction processing shall be enabled a; and
b)
warning processing shall be enabled a.
The device server shall process informational exception conditions as follows:
a)
failure prediction processing shall be disabled; and
b)
warning processing shall be disabled.
The device server shall process informational exception conditions as follows:
a)
failure prediction processing shall be disabled; and
b)
warning processing shall be enabled a.
The device server shall set the additional sense code to FAILURE PREDICTION
THRESHOLD EXCEEDED (FALSE) a.
The device server shall terminate the MODE SELECT command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
a If applicable based on the value in the MRIE field (e.g., 2h to 6h), then the values in the LOGERR bit, the
INTERVAL TIMER field, and the REPORT COUNT field determine how the informational exception condition
is processed.


C) report the informational exception conditions as soon as the method specified in the MRIE field
occurs (i.e., the INTERVAL TIMER field and REPORT COUNT field do not apply for background self-test
errors and errors that occur during background functions);
and
c)
logging by the device server of informational exception conditions is determined by the value in the
LOGERR bit.
A LOGERR bit set to zero specifies that the device server may log any informational exception conditions in the
Informational Exceptions log page (see SPC-6). A LOGERR bit set to one specifies that the device server shall
log informational exception conditions in the Informational Exceptions log page.
The method of reporting informational exceptions (MRIE) field (see table 247) specifies the method that shall
be used by the device server to report:
a)
informational exception conditions if the specified code value is supported by the device server; and
b)
background self-test errors and device specific background function errors with the ADDITIONAL SENSE
CODE field set to 0Bh or 5Dh if the EBACKERR bit is set to one and the specified code value is
supported by the device server.
A device server that supports the Informational Exceptions Control mode page shall support at least one code
value other than zero in the MRIE field.
The priority of reporting multiple informational exceptions is vendor specific.
Table 247 — Method of reporting informational exceptions (MRIE) field (part 1 of 2)
Code
Description
0h
No reporting of informational exception condition: The device server shall not report
information exception conditions.
1h
Obsolete
2h
Establish unit attention condition: The device server shall report informational exception
conditions by establishing a unit attention condition (see SAM-6) for the SCSI initiator port
associated with every I_T nexus, with the additional sense code set to indicate the cause of
the informational exception condition.a
3h
Conditionally generate recovered error: The device server shall report informational
exception conditions, if the reporting of recovered errors is allowed b, by modifying the
completion of the next command processed without encountering any errors, regardless of
the I_T nexus on which the command was received. The modification shall be to terminate
the command with CHECK CONDITION status with the sense key set to RECOVERED
ERROR and the additional sense code set to indicate the cause of the informational
exception condition.
4h
Unconditionally generate recovered error: The device server shall report informational
exception conditions, regardless of whether the reporting of recovered errors is allowed b, by
modifying the completion of the next command processed without encountering any errors,
regardless of the I_T nexus on which the command was received. The modification shall be to
terminate the command with CHECK CONDITION status with the sense key set to
RECOVERED ERROR and the additional sense code set to indicate the cause of the
informational exception condition.
a The device server terminates the command to report the unit attention condition for the informational
exception condition (i.e., the device server does not process the command except to report the unit
attention condition) (see SAM-6).
b This is controlled by the PER bit (see 6.5.10) or the PER bit (see 6.5.11).


The INTERVAL TIMER field specifies the period in 100 millisecond increments that the device server shall use for
reporting that an informational exception condition has occurred (see table 248). After an informational
exception condition has been reported, the interval timer shall be started. An INTERVAL TIMER field set to zero
or FFFF_FFFFh specifies that the period for reporting an informational exception condition is vendor specific.
The REPORT COUNT field specifies the maximum number of times the device server may report an
informational exception condition to the application client. A REPORT COUNT field set to zero specifies that there
is no limit on the number of times the device server may report an informational exception condition.
The device server shall use the values in the INTERVAL TIMER field and the REPORT COUNT field based on the
value in the MRIE field as shown in table 248.
5h
Generate no sense: The device server shall report informational exception conditions by
modifying the completion of the next command processed without encountering any errors,
regardless of the I_T nexus on which the command was received. The modification shall be to
terminate the command with CHECK CONDITION status with the sense key set to NO SENSE
and the additional sense code set to indicate the cause of the informational exception
condition.
6h
Only report informational exception condition on request: The device server shall provide
pollable sense data (see SPC-6) with the sense key set to NO SENSE and the additional
sense code set to indicate the cause of the informational exception condition. To find out about
information exception conditions, the application client polls the device server by issuing a
REQUEST SENSE command.
7h to Bh
Reserved
Ch to Fh
Vendor specific
Table 248 — Use of the INTERVAL TIMER field and the REPORT COUNT field based on the MRIE field
MRIE a
Description
2h to 6h
If reporting of an informational exception condition is enabled (see table 247), then the device
server shall:
1) report an informational exception condition when the condition is first detected; and
2) if the value in the REPORT COUNT field is not equal to one, then:
1)
if the INTERVAL TIMER field is not set to zero or FFFF_FFFFh, then wait the time
specified in the INTERVAL TIMER field, and, if that informational exception condition still
exists, report the informational exception again; and
2)
while the informational exception condition exists, continue to report the informational
exception condition after waiting the time specified in the INTERVAL TIMER field until the
condition has been reported the number of times specified by the REPORT COUNT field.
Ch to Fh
The device server may use or may ignore the values in the INTERVAL TIMER field and the
REPORT COUNT field to report the informational exception condition based on the device
specific implementation.
a For values in the MRIE field (see table 247) not shown in this table, the INTERVAL TIMER field and the
REPORT COUNT field shall be ignored.
Table 247 — Method of reporting informational exceptions (MRIE) field (part 2 of 2)
Code
Description
a The device server terminates the command to report the unit attention condition for the informational
exception condition (i.e., the device server does not process the command except to report the unit
attention condition) (see SAM-6).
b This is controlled by the PER bit (see 6.5.10) or the PER bit (see 6.5.11).


Maintaining the interval timer and the report counter across power cycles, hard resets, logical unit resets, and
I_T nexus losses by the device server is vendor specific.
6.5.9 Logical Block Provisioning mode page
6.5.9.1 Overview
The Logical Block Provisioning mode page (see table 249) specifies the parameters that a device server that
supports logical block provisioning threshold values (see 4.7.3.7) shall use to report logical block provisioning
threshold notifications (see 4.7.3.7.6). The mode page policy (see SPC-6) for this page shall be shared.
If a method not defined by this standard changes the parameter data to be returned by a device server in the
Logical Block Provisioning mode page, then the device server shall establish a unit attention condition for the
SCSI initiator port associated with every I_T nexus with the additional sense code set to MODE
PARAMETERS CHANGED.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field,
and the PAGE LENGTH field are defined in SPC-6.
The SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in table 249 for
the Logical Block Provisioning mode page.
A single initiator threshold unit attention (SITUA) bit set to one specifies that the logical block provisioning
threshold notification unit attention condition is established on a single I_T nexus as described in 4.7.3.7.6. A
SITUA bit set to zero specifies that the logical block provisioning threshold notification unit attention condition is
established on multiple I_T nexuses as described in 4.7.3.7.6.
The threshold descriptors are defined in 6.5.9.2.
Table 249 — Logical Block Provisioning mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (1Ch)
SUBPAGE CODE (02h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Reserved
SITUA
Reserved
•••
Threshold descriptors
Threshold descriptor [first] (see 6.5.9.2)
•••
•••
n - 7
Threshold descriptor [last] (see 6.5.9.2)
•••
n


6.5.9.2 Threshold descriptor format
The threshold descriptor format is shown in table 250.
An ENABLED bit set to one specifies that the threshold is enabled. An ENABLED bit set to zero specifies that the
threshold is disabled.
The THRESHOLD TYPE field (see table 251) specifies the type of this threshold.
The THRESHOLD ARMING field (see table 252) specifies the arming method used for operation of this threshold.
The THRESHOLD RESOURCE field specifies the resource of this threshold. The contents of this field are as
defined for parameters codes  0000h to 00FFh (see table 196) in the Logical Block Provisioning log page
(see 6.4.5).
The valid combinations of the THRESHOLD TYPE field, the THRESHOLD ARMING field, and the THRESHOLD
RESOURCE field are shown in table 7 and table 8.
The THRESHOLD COUNT field specifies the center of the threshold range for this threshold expressed as:
a)
a number of threshold sets (i.e., the number of LBA mapping resources expressed as a number of
threshold sets), if the value in the THRESHOLD TYPE field is set to 000b; or
Table 250 — Threshold descriptor format
Bit
Byte
ENABLED
Reserved
THRESHOLD TYPE
THRESHOLD ARMING
THRESHOLD RESOURCE
Reserved
(MSB)
THRESHOLD COUNT
•••
(LSB)
Table 251 — THRESHOLD TYPE field
Code
Description
000b
If the THRESHOLD COUNT field specifies a soft threshold, the threshold is enabled,  and that
threshold is reached, then the device server shall establish a unit attention condition as
described in 4.7.3.7.6.
001b
If the THRESHOLD COUNT field specifies a percentage threshold, the threshold is enabled, and
that threshold is reached, then the device server shall establish a unit attention condition as
described in 4.7.3.7.6
All others
Reserved
Table 252 — THRESHOLD ARMING field
Code
Description
Reference
000b
The threshold operates as an armed decreasing threshold.
4.7.3.7.4
001b
The threshold operates as an armed increasing threshold.
4.7.3.7.5
All others
Reserved


b)
a percentage value, if the value in the THRESHOLD TYPE field is set to 001b.
6.5.10 Read-Write Error Recovery mode page
The Read-Write Error Recovery mode page (see table 253) specifies the error recovery parameters the
device server shall use during:
a)
read medium operations; or
b)
write medium operations.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, and the PAGE LENGTH
field are defined in SPC-6.
The SPF bit, the PAGE CODE field, and the PAGE LENGTH field shall be set to the values shown in table 253 for
the Read-Write Error Recovery mode page.
An automatic write reassignment enabled (AWRE) bit set to zero specifies that the device server shall not
perform automatic write reassignment.
An AWRE bit set to one specifies that the device server shall enable automatic write reassignment for LBAs
referencing logical blocks for which a recovered error or unrecovered error occurs during a write medium
operation. Automatic write reassignment shall be performed only if the device server has the valid data (e.g.,
original data in a buffer or recovered from the medium). The valid data shall be placed in the logical block
referenced by the reassigned LBA. The device server shall report any failures that occur during the reassign
operation. Error reporting as specified by the error recovery bits (i.e., the PER bit, and the DTE bit) shall be
performed only after completion of the reassign operation.
An automatic read reassignment enabled (ARRE) bit set to zero specifies that the device server shall not
perform automatic read reassignment.
An ARRE bit set to one specifies that the device server shall enable automatic read reassignment for LBAs
referencing logical blocks for which a recovered error occurs during a read medium operation. All error
recovery actions required by the error recovery bits shall be processed. Automatic read reassignment shall
then be performed only if the device server recovers the data without error. The recovered data shall be
placed in the logical block referenced by the reassigned LBA. The device server shall report any failures that
Table 253 — Read-Write Error Recovery mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (01h)
PAGE LENGTH (0Ah)
AWRE
ARRE
TB
RC
Obsolete
Error recovery bits
Obsolete
PER
DTE
READ RETRY COUNT
Obsolete
Obsolete
Obsolete
LBPERE
MWR
Reserved
Restricted for MMC-6
WRITE RETRY COUNT
Reserved
(MSB)
RECOVERY TIME LIMIT
(LSB)


occur during the reassign operation. Error reporting as specified by the error recovery bits shall be performed
only after completion of the reassign operation.
A transfer block (TB) bit set to zero specifies that if an unrecovered read error occurs during a read medium
operation, then the device server shall not transfer any data for that logical block to the Data-In Buffer. A TB bit
set to one specifies that if an unrecovered read error occurs during a read medium operation, then the device
server shall transfer pseudo read data (e.g., data already in a buffer or any other vendor specific data) for that
logical block before returning CHECK CONDITION status. The data returned in this case is vendor specific.
The value of the TB bit does not specify any action for recovered read errors.
A read continuous (RC) bit set to zero specifies that error recovery operations that cause delays during the
data transfer are acceptable. Data shall not be fabricated.
An RC bit set to one specifies the device server shall transfer the entire requested length of data without
adding delays during the data transfer to perform error recovery procedures. The device server may transfer
pseudo read data in order to maintain a continuous flow of data. The device server shall assign priority to the
RC bit over conflicting bits within this byte.
NOTE 23 - The RC bit set to one is useful for image processing, audio, or video applications.
A post error (PER) bit set to one specifies that if a recovered read error occurs while processing a read
command or a write command, then the device server shall terminate the command with CHECK CONDITION
status with the sense key set to RECOVERED ERROR. A PER bit set to zero specifies that if a recovered read
error occurs while processing a read command or a write command, then the device server shall perform error
recovery procedures within the limits established by the error recovery parameters and not terminate the
specified command with CHECK CONDITION status with the sense key set to RECOVERED ERROR (e.g.,
the device server may terminate the specified command with CHECK CONDITION status with the sense key
set to MEDIUM ERROR if an uncorrectable error is detected based on the established limits during the error
recovery process). If the DTE bit is set to one, then the PER bit shall be set to one.
A data terminate on error (DTE) bit set to one specifies that, upon detection of a recovered error, the device
server shall terminate the data transfer to the Data-In Buffer for a read command or the data transfer to the
Data-Out Buffer for a write command upon detection of a recovered error. A DTE bit set to zero specifies that,
upon detection of a recovered error, the device server shall not terminate the data transfer to the Data-In
Buffer for a read command or the data transfer to the Data-Out Buffer for a write command.


The combinations of the error recovery bits (i.e., the PER bit, and the DTE bit) are shown in table 254.
Table 254 — Error recovery bit combinations (part 1 of 2)
PER
DTE
Description b
The device server shall perform the full number of retries as specified in the READ
RETRY COUNT field for read medium operations, the WRITE RETRY COUNT field for
write medium operations, and the VERIFY RETRY COUNT field (see 6.5.11) for verify
medium operations and shall perform error correction in an attempt to recover the
data.
The device server shall not report recovered read errors or write errors. The
device server shall terminate a command performing a read medium operation or
a write medium operation with CHECK CONDITION status before the transfer
count is exhausted only if an unrecovered error is detected.
If an unrecovered read error occurs during a read medium operation, then the
transfer block (TB) bit determines whether the data for the logical block with the
unrecovered read error is transferred to the Data-In Buffer.
Invalid mode. The PER bit is set to one if the DTE bit is set to one. a
The device server shall perform the full number of retries as specified in the READ
RETRY COUNT field for read medium operations, the WRITE RETRY COUNT field for
write medium operations, the VERIFY RETRY COUNT field (see 6.5.11) for verify
medium operations, and shall perform error correction in an attempt to recover the
data.
The device server shall terminate a command performing a read medium
operation or write medium operation with CHECK CONDITION status before the
transfer count is exhausted only if an unrecovered error is detected.
If an unrecovered read error occurs during a read medium operation, the transfer
block (TB) bit determines whether the data for the logical block with the
unrecovered read error is transferred to the Data-In Buffer.
If a recovered error occurs while the device server is performing a read medium
operation or write medium operation, then, after the operation is complete, the
device server shall terminate the command with CHECK CONDITION status with
the sense key set to RECOVERED ERROR. The INFORMATION field in the sense
data contains the LBA of the last recovered error that occurred during the
command (see 4.18.1).
a If an invalid combination of the error recovery bits is sent by an application client, then the
device server shall terminate the MODE SELECT command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
b This table is used by both the Read Write Error Recovery mode page and the Verify Error
Recovery mode page (see 6.5.11). When used for the Read Write Error Recovery mode
page, rules about the VERIFY RETRY COUNT field are not applicable.  When used for the
Verify Error Recovery mode page, rules about the READ RETRY COUNT field, the WRITE RETRY
COUNT field, and write medium operations are not applicable and rules about read medium
operations are applicable to verify medium operations.


The READ RETRY COUNT field specifies the number of times that the device server shall attempt its recovery
algorithm during read medium operations.
The WRITE RETRY COUNT field specifies the number of times that the device server shall attempt its recovery
algorithm during write medium operations.
A logical block provisioning error reporting enabled (LBPERE) bit set to one specifies that logical block
provisioning threshold notification is enabled. A LBPERE bit set to zero specifies that logical block provisioning
threshold notification is disabled (see 4.7.3.7.6).
A misaligned write reporting (MWR) field (see table 255) specifies the behavior of the device server with
respect to physical block misalignment reporting (see 4.6.2).
The device server shall perform the full number of retries as specified in the READ
RETRY COUNT field for read medium operations, the WRITE RETRY COUNT field for
write medium operations, the VERIFY RETRY COUNT field (see 6.5.11) for verify
medium operations, and shall perform error correction in an attempt to recover the
data.
The device server shall terminate a command performing a read medium
operation or write medium operation with CHECK CONDITION status before the
transfer count is exhausted if any error, either recovered or unrecovered, is
detected. The INFORMATION field in the sense data contains the LBA of the error
(see 4.18.1).
If a recovered read error occurs during a read medium operation, then the device
server shall transfer the recovered read data for the logical block with the
recovered read error before returning CHECK CONDITION status.
If an unrecovered read error occurs during a read medium operation, the transfer
block (TB) bit determines whether the data for the logical block with the
unrecovered read error is transferred to the Data-In Buffer.
Table 255 — MWR field
Code
Name
Description
00b
DISABLED
Complete and do not report misaligned write operations
01b
ENABLED
Complete and report misaligned write operations
10b
TERMINATE
Terminate and report misaligned write operations
11b
Reserved
Table 254 — Error recovery bit combinations (part 2 of 2)
PER
DTE
Description b
a If an invalid combination of the error recovery bits is sent by an application client, then the
device server shall terminate the MODE SELECT command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
b This table is used by both the Read Write Error Recovery mode page and the Verify Error
Recovery mode page (see 6.5.11). When used for the Read Write Error Recovery mode
page, rules about the VERIFY RETRY COUNT field are not applicable.  When used for the
Verify Error Recovery mode page, rules about the READ RETRY COUNT field, the WRITE RETRY
COUNT field, and write medium operations are not applicable and rules about read medium
operations are applicable to verify medium operations.


A RECOVERY TIME LIMIT field set to a non-zero value specifies in milliseconds the maximum time duration that
the device server shall use for data error recovery procedures during read medium operations and during
write medium operations. The device server may round this value as described in SPC-6. The limit in this field
specifies the maximum error recovery time allowed for any individual logical block. A RECOVERY TIME LIMIT field
set to zero specifies that the device server shall use its default value.
If both a retry count and a recovery time limit are specified, then the field that specifies the recovery action
with the shortest recovery time shall have precedence.
To disable all types of correction and retries, the application client should set:
a)
the PER bit to one;
b)
the DTE bit to one;
c)
the READ RETRY COUNT field to 00h;
d)
the WRITE RETRY COUNT field to 00h; and
e)
the RECOVERY TIME LIMIT field to 0000h.
6.5.11 Verify Error Recovery mode page
The Verify Error Recovery mode page (see table 256) specifies the error recovery parameters the device
server shall use during verify medium operations (e.g., from VERIFY commands and the verify medium
operations of the WRITE AND VERIFY commands). Verify medium operations do not trigger automatic read
reassignment.
The parameters saveable (PS) bit, the subpage format (SPF) bit, the PAGE CODE field, and the PAGE LENGTH
field are defined in SPC-6.
The SPF bit, the PAGE CODE field, and the PAGE LENGTH field shall be set to the values shown in table 256 for
the Verify Error Recovery mode page.
The PER bit and the DTE bit (i.e., the error recovery bits) are defined in 6.5.10. The combinations of these bits
are shown in table 254.
The VERIFY RETRY COUNT field specifies the number of times that the device server shall attempt its recovery
algorithm during a verify medium operation.
The VERIFY RECOVERY TIME LIMIT field specifies in milliseconds the maximum time duration that the device
server shall use error recovery procedures to recover data for an individual logical block during a verify
medium operation. The device server may round this value as described in SPC-6.
Table 256 — Verify Error Recovery mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (07h)
PAGE LENGTH (0Ah)
Reserved
Obsolete
Error recovery bits
Obsolete
PER
DTE
VERIFY RETRY COUNT
Obsolete
Reserved
•••
(MSB)
VERIFY RECOVERY TIME LIMIT
(LSB)


If both a verify retry count and a verify recovery time limit are specified, then the one that requires the least
time for data error recovery actions shall have priority.
To disable all types of correction and retries, the application client should set:
a)
the PER bit to one;
b)
the DTE bit to one;
c)
the VERIFY RETRY COUNT field to 00h; and
d)
the VERIFY RECOVERY TIME LIMIT field to 0000h.
