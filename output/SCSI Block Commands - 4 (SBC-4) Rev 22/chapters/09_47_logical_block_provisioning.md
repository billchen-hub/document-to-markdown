# 4.7 Logical block provisioning

the newest LPS Misalignment log parameter (i.e. parameter code with the greatest value) is equal to the value
of the MAX_LPSM field in the LPS Misalignment Count log parameter (i.e. the log is full), then the device server
shall not append additional LPS Misalignment log parameters to the LPS Misalignment log page.
The MWR field (see 6.5.10) specifies how misaligned write commands are processed. If the device server
processes a misaligned write command, and the MWR field is set to:
a)
00b (i.e. DISABLED), then the device server shall process that write command without adding a log
parameter in the LPS Misalignment log page (see 6.4.6);
b)
01b (i.e. ENABLED), then the device server shall:
1)
process that write command;
2)
add a log parameter in the LPS Misalignment log page, if the log is not full; and
3)
if that write command completes without error, complete the command with GOOD status with the
sense key set to COMPLETED and the additional sense code set to MISALIGNED WRITE
COMMAND;
or
c)
10b (i.e. TERMINATE), then the device server shall:
1)
add a log parameter in the LPS Misalignment log page, if the page is not full; and
2)
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to MISALIGNED WRITE COMMAND.
4.7 Logical block provisioning
4.7.1 Logical block provisioning overview
Each LBA in a logical unit is either mapped or unmapped. For LBAs that are mapped, there is a known
relationship between the LBA and one or more physical blocks that contain logical block data. For LBAs that
are unmapped, the relationship between the LBA and a physical block is not defined. Figure 6 shows two
examples of the relationship between mapped and unmapped LBAs and physical blocks in a logical unit. One
example shows one LBA per physical block and one example shows two LBAs per physical block. The
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field is defined in the READ CAPACITY (16) parameter data
(see 5.21.2).
Figure 6 — Examples of the relationship between mapped and unmapped LBAs and physical blocks
Key:
LBA n = logical block with LBA n
PB = physical block
Unmapped = the relationship between the LBA(s) and a physical block is not defined
LBA 0
LBA 1
LBA 2
LBA 3
LBA 5
LBA 6
LBA 7
LBA 4
PB
PB
Unmapped
PB
Unmapped Unmapped
PB
PB
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 0h (i.e., 20 logical blocks per physical block):
PB
Unmapped
PB
Unmapped
LBA 0
LBA 1
LBA 2
LBA 3
LBA 5
LBA 6
LBA 7
LBA 4
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 1h (i.e., 21 logical blocks per physical block):


Each unmapped LBA is either anchored or deallocated. Anchored and deallocated are states in the LBP state
machine (see 4.7.4) that have the following properties:
a)
a write command that specifies an anchored LBA does not require allocation of additional LBA
mapping resources for that LBA; and
b)
a write command that specifies a deallocated LBA may require allocation of LBA mapping resources.
Depending on the logical block provisioning types (see table 5), the quantity of LBA mapping resources
available to a logical unit may be greater than, equal to, or less than the quantity required to store logical block
data for every LBA.
Table 5 list the logical block provisioning states supported by each type of logical block provisioning.
4.7.2 Fully provisioned logical unit
The device server shall map every LBA in a fully provisioned logical unit. A fully provisioned logical unit shall
provide enough LBA mapping resources to contain all logical blocks for the logical unit’s capacity as reported
in the READ CAPACITY (10) parameter data (see 5.20.2) and the READ CAPACITY (16) parameter data
(see 5.21.2). The device server shall not cause any LBA on a fully provisioned logical unit to become
unmapped (i.e., anchored or deallocated).
A fully provisioned logical unit does not support logical block provisioning management (see 4.7.3). A fully
provisioned logical unit may support the GET LBA STATUS (16) command (see 5.6) and the GET LBA
STATUS (32) command (see 5.7).
The device server in a fully provisioned logical unit shall set the LBPME bit to zero in the READ CAPACITY (16)
parameter data (see 5.21.2).
4.7.3 Logical block provisioning management
4.7.3.1 Logical block provisioning management overview
A logical unit that supports logical block provisioning management (i.e., implements unmapped LBAs, unmap
operations, and related actions) shall be either:
a)
resource provisioned (see 4.7.3.2); or
b)
thin provisioned (see 4.7.3.3).
A logical unit that supports logical block provisioning management may change from resource provisioned to
thin provisioned as resources become unavailable. If the logical unit transitions from resource provisioned to
thin provisioned, then the logical unit shall change the PROVISIONING TYPE field to 010b (i.e., the logical unit is
thin provisioned) in the Logical Block Provisioning VPD page (see 6.6.7) and establish a unit attention
condition with the additional sense code set to INQUIRY DATA HAS CHANGED as described in SPC-6.
A logical unit that supports logical block provisioning management shall implement the LBP state machine
(see 4.7.4) for each LBA.
Table 5 — Logical block provisioning states supported by logical block provisioning type
Type
Logical block provisioning states
Reference
Mapped
Unmapped
Anchored
Deallocated
Fully provisioned
Mandatory
Prohibited
Prohibited
4.7.2
Resource provisioned
Mandatory
Optional
Optional
4.7.3.2
Thin provisioned
Mandatory
Optional
Mandatory
4.7.3.3


The device server in a logical unit that supports logical block provisioning management:
a)
shall support the Logical Block Provisioning VPD page (see 6.6.7);
b)
may supply a provisioning group designation descriptor as defined in the Logical Block Provisioning
VPD page;
c)
may support logical block provisioning thresholds (see 4.7.3.7.1);
d)
may support the GET LBA STATUS (16) command (see 5.6);
e)
may support the GET LBA STATUS (32) command (see 5.7)
f)
should support the Block Limits VPD page (see 6.6.4); and
g)
shall support at least one of the following unmap mechanisms:
A) the UNMAP command (see 5.35);
B) the UNMAP bit in the WRITE SAME (10) command (see 5.52);
C) the UNMAP bit in the WRITE SAME (16) command (see 5.53); or
D) the UNMAP bit in the WRITE SAME (32) command (see 5.54).
If the device server supports:
a)
the UNMAP bit in the WRITE SAME (10) command or in the WRITE SAME (16) command; and
b)
the WRITE SAME (32) command (see 5.54),
then the device server shall support the UNMAP bit in the WRITE SAME (32) command.
If a device server supports the UNMAP command and the Block Limits VPD page, then the device server
shall:
a)
set the MAXIMUM UNMAP LBA COUNT field (see 6.6.4) to a value greater than or equal to one; and
b)
set the MAXIMUM UNMAP DESCRIPTOR COUNT field  (see 6.6.4) to a value greater than or equal to one.
4.7.3.2 Resource provisioned logical unit
A resource provisioned logical unit shall support logical block provisioning management (see 4.7.3.1).
The device server shall map, anchor, or deallocate each LBA in a resource provisioned logical unit. A
resource provisioned logical unit shall provide LBA mapping resources sufficient to map all LBAs for the
logical unit’s capacity as indicated in the RETURNED LOGICAL BLOCK ADDRESS field of the READ CAPACITY (10)
parameter data (see 5.20.2) and the READ CAPACITY (16) parameter data (see 5.21.2). A resource
provisioned logical unit may provide resources in excess of this requirement.
The device server in a resource provisioned logical unit:
a)
shall set the LBPME bit to one in the READ CAPACITY (16) parameter data (see 5.21.2);
b)
shall set the PROVISIONING TYPE field to 001b (i.e., resource provisioned) in the Logical Block
Provisioning VPD page (see 6.6.7); and
c)
may set the ANC_SUP bit to one in the Logical Block Provisioning VPD page.
The initial condition of every LBA in a resource provisioned logical unit is anchored (see 4.7.4.1) or dellocated.
4.7.3.3 Thin provisioned logical unit
A thin provisioned logical unit shall support logical block provisioning management (see 4.7.3.1).
The device server in a thin provisioned logical unit may indicate a larger capacity in the RETURNED LOGICAL
BLOCK ADDRESS field in the READ CAPACITY (10) parameter data (see 5.20.2) and the READ CAPACITY (16)
parameter data (see 5.21.2) than the number of LBA mapping resources available for mapping LBAs in the
logical unit.
The device server shall map, anchor, or deallocate each LBA in a thin provisioned logical unit (see table 5). A
thin provisioned logical unit is not required to provide LBA mapping resources sufficient to map all LBAs for
the logical unit’s capacity as indicated in the RETURNED LOGICAL BLOCK ADDRESS field of the READ
CAPACITY (10) parameter data (see 5.20.2) and the READ CAPACITY (16) parameter data (see 5.21.2).


If the logical unit does not support anchored LBAs (i.e, the ANC_SUP bit is set to zero in the Logical Block
Provisioning VPD page (see 6.6.7)), then:
a)
every unmapped LBA in the logical unit shall be deallocated; and
b)
the device server shall terminate every command that specifies anchoring an LBA (e.g., a WRITE
SAME command with the ANCHOR bit set to one (see 5.52)).
The device server in a thin provisioned logical unit shall set:
a)
the LBPME bit to one in the READ CAPACITY (16) parameter data (see 5.21.2); and
b)
the PROVISIONING TYPE field to 010b (i.e., thin provisioned) in the Logical Block Provisioning VPD page
(see 6.6.7).
The initial condition of every LBA in a thin provisioned logical unit is deallocated (see 4.7.4.1).
4.7.3.4 Unmapping LBAs
4.7.3.4.1 Unmapping overview
A logical unit that supports logical block provisioning management shall support unmapping of LBAs.
The logical block provisioning state of an LBA may change to unmapped (i.e., deallocated (see 4.7.4.6) or
anchored (see 4.7.4.7)) as a result of:
a)
an unmap request (see 4.7.3.4.2);
b)
an autonomous LBA transition (see 4.7.3.5) (e.g., following a FORMAT UNIT command (see 5.4) or a
write command that sets the logical block data to zero); or
c)
other commands that result in LBAs being initialized to unmapped (e.g., a SANITIZE command
(see 5.30)).
4.7.3.4.2 Processing unmap requests
Application clients use unmap commands (see 4.2.2) to request that LBAs be unmapped. For each LBA that
is requested to be unmapped, the device server shall:
a)
perform an unmap operation (see 4.7.3.4.3) on the LBA; or
b)
make no change to the logical block provisioning state of the LBA.
The application client determines the logical block provisioning state of LBAs using the GET LBA STATUS
(16) command (see 5.6) or the GET LBA STATUS (32) command (see 5.7).
Application clients should not rely on an UNMAP command (see 5.35) to cause specific data (e.g., zeros) to
be returned by subsequent read operations on the specified LBAs. To produce consistent results for
subsequent read operations, a write command (e.g., the WRITE SAME command) should be used to write
user data.
EXAMPLE - To ensure that subsequent read operations return all zeros in a logical block, the application client should use
the WRITE SAME (16) command with the NDOB bit set to one. If the UNMAP bit is set to one, then the device server may
unmap the logical blocks specified by the WRITE SAME (16) command as described in 4.7.3.4.4.
4.7.3.4.3 Unmap operations
An unmap operation:
a)
results in a single LBA becoming either deallocated or anchored;
b)
may change the relationship between one LBA and one or more physical blocks; and
c)
may change the logical block data that is returned in response to a subsequent read command
specifying that LBA.
The data in all other mapped LBAs on the medium shall be preserved. Performing an unmap operation (e.g.,
to change from anchored to deallocated, or remain in the same logical block provisioning state) on an
unmapped LBA shall not be considered an error.


An unmap operation may or may not release LBA mapping resources.
An application client may use an unmap command (see 4.2.2) to request that the device server perform an
unmap operation on each specified LBA. A single unmap command may result in zero or more unmap
operations.
4.7.3.4.4 WRITE SAME command and unmap operations
A WRITE SAME command (see 5.52, 5.53, and 5.54) may be used to request unmap operations that
deallocate or anchor the specified LBAs. If unmap operations are requested in a WRITE SAME command,
then for each specified LBA:
a)
if the Data-Out Buffer of the WRITE SAME command is the same as the logical block data returned by
a read operation from that LBA while in the unmapped state (see 4.7.4.4), then:
1)
the device server performs the actions described in table 6; and
2)
if an unmap operation is not performed in step 1), then the device server shall perform the
specified write operation to that LBA;
or
b)
if the Data-Out Buffer of the WRITE SAME command is not the same as the logical block data
returned by a read operation from that LBA while in the unmapped state (see 4.7.4.4), then the device
server shall perform the specified write operation to that LBA.
A WRITE SAME command shall not cause an LBA to become unmapped if unmapping that LBA creates a
case in which a subsequent read of that unmapped LBA is able to return logical block data that differs from the
Data-Out Buffer for that WRITE SAME command (see 4.7.4.4).
If the device server does not support allowing a WRITE SAME command to request unmap operations, then
the device server shall:
a)
perform the write operations specified by the WRITE SAME command; and
b)
not perform any unmap operations.
The device server shall perform the write operations specified by a WRITE SAME command and shall not
perform any unmap operations if the device server sets the LBPRZ field to xx1b  (see 6.6.7), and:
a)
any bit in the user data transferred from the Data-Out Buffer is not zero; or
b)
the protection information, if any, transferred from the Data-Out Buffer is not set to
FFFF_FFFF_FFFF_FFFFh.
The device server shall perform the write operations specified by a WRITE SAME command and shall not
perform any unmap operations, if the device server sets the LBPRZ field to 010b and:
a)
the user data transferred from the Data-Out Buffer is not set to the provisioning initialization pattern; or
Table 6 — WRITE SAME command and unmap operations
Logical block
provisioning
management type
Unmap operations that request to
deallocate the specified LBA
Unmap operations that request to
anchor the specified LBA
Thin provisioned
logical unit
a) should perform an unmap operation to
deallocate the LBA (see 4.7.4.6.1); or
b) may perform an unmap operation to
anchor the LBA (see 4.7.4.7.1)
should perform an unmap operation
to anchor the LBA
Resource provisioned
logical unit
a) should perform an unmap operation to
anchor the LBA; or
b) may perform an unmap operation to
deallocate the LBA
should perform an unmap operation
to anchor the LBA


b)
the protection information, if any, transferred from the Data-Out Buffer is not set to
FFFF_FFFF_FFFF_FFFFh.
4.7.3.5 Autonomous LBA transitions
A device server may perform the following actions at any time:
a)
transition any deallocated LBA to mapped;
b)
transition any anchored LBA to mapped; or
c)
transition any deallocated LBA to anchored.
If the LBPRZ field (see 6.6.7) is set to:
a)
xx1b, and a mapped LBA references a logical block that contains:
A) user data with all bits set to zero; and
B) protection information, if any with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh;
or
b)
010b, and a mapped LBA references a logical block that contains:
A) user data set to the provisioning initialization pattern; and
B) protection information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to the CRC for the provisioning initialization
pattern;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh,
then the device server may transition that mapped LBA to anchored or deallocated at any time.
The logical block provisioning state machine (see 4.7.4) specifies additional requirements for the transitions
specified in this subclause.
4.7.3.6 Logical unit resource exhaustion considerations
4.7.3.6.1 Thin provisioned logical unit resource exhaustion considerations
If:
a)
a write operation is requested by an application client, and a temporary lack of LBA mapping
resources prevents the logical unit from performing the write operation; or
b)
an unmap operation is requested by an application client to transition an LBA to the anchored state
and a temporary lack of LBA mapping resources prevents the logical unit from anchoring the LBA,
then the device server shall terminate the command requesting the operation with CHECK CONDITION
status with the sense key set to NOT READY and the additional sense code set to LOGICAL UNIT NOT
READY, SPACE ALLOCATION IN PROGRESS. In this case, the application client should resend the
command.
If:
a)
a write operation is requested by an application client, and a persistent lack of LBA mapping
resources prevents the logical unit from performing the write operation; or
b)
an unmap operation is requested by an application client to transition an LBA to the anchored state
and a persistent lack of LBA mapping resources prevents the logical unit from anchoring the LBA,
then the device server shall terminate the command requesting the unmap operation with CHECK
CONDITION status with the sense key set to DATA PROTECT and the additional sense code set to SPACE
ALLOCATION FAILED WRITE PROTECT. This condition shall not cause the device server to set the WP bit in
the DEVICE-SPECIFIC PARAMETER field of the mode parameter header to one (see 6.5.1). In this case, recovery
actions by the application client are not defined by this standard.


A logical block provisioning threshold may be available to monitor the availability of LBA mapping resources
(see 4.7.3.7). A logical block provisioning log parameter that reports available LBA mapping resources may
be available in the Logical Block Provisioning log page (see 6.4.5).
4.7.3.6.2 Resource provisioned logical unit resource exhaustion considerations
If:
a)
a write operation is requested by an application client, and a temporary lack of LBA mapping
resources prevents the logical unit from performing the write operation; or
b)
an unmap operation is requested by an application client to transition an LBA to the anchored state
and a temporary lack of LBA mapping resources prevents the logical unit from anchoring the LBA,
then the device server shall terminate the command requesting the operation with CHECK CONDITION
status with the sense key set to NOT READY and the additional sense code set to LOGICAL UNIT NOT
READY, SPACE ALLOCATION IN PROGRESS. In this case, the application client should resend the
command.
In a resource provisioned logical unit a write operation requested by an application client shall not result in a
persistent lack of LBA mapping resources that prevents the logical unit from performing the write operation.
Therefore, a resource provisioned logical unit shall not terminate any command with CHECK CONDITION
status with the sense key set to DATA PROTECT and the additional sense code set to SPACE ALLOCATION
FAILED WRITE PROTECT.
A logical block provisioning threshold may be available to monitor the availability of LBA mapping resources
(see 4.7.3.7). A  parameter that reports available LBA mapping resources may be available in the  page
(see 6.4.5).
4.7.3.7 Logical block provisioning thresholds
4.7.3.7.1 Logical block provisioning thresholds overview
Logical block provisioning thresholds provide a mechanism for the device server to establish a unit attention
condition to notify application clients when thresholds related to logical block provisioning are crossed. Logical
block provisioning thresholds may operate on an armed increasing basis or an armed decreasing basis.
If a device server supports logical block provisioning thresholds, then the device server:
a)
shall support the Logical Block Provisioning mode page (see 6.5.9); and
b)
may support the Logical Block Provisioning log page (see 6.4.5).
Logical block provisioning thresholds may be based on threshold sets (see 4.7.3.7.2) or percentages
(see 4.7.3.7.3).
4.7.3.7.2 Threshold sets
The end points of the range over which a logical block provisioning threshold operates are defined as follows:
threshold minimum = ((threshold count × threshold set size) – (threshold set size × 0.5))
threshold maximum = ((threshold count × threshold set size) + (threshold set size × 0.5))
where:
threshold minimum
is the lowest number of LBAs in the range for this threshold;
threshold maximum
is the highest number of LBAs in the range for this threshold;
threshold count
is the center of the threshold range for this threshold (i.e., the threshold count
value as specified in the threshold descriptor in the Logical Block
Provisioning mode page); and


threshold set size
is the number of LBAs in each threshold set (i.e., 2(threshold exponent) LBAs
where the threshold exponent is indicated in the Logical Block Provisioning
VPD page (see 6.6.7)).
Table 7 defines the meaning of the combinations of values for the THRESHOLD RESOURCE field, the THRESHOLD
TYPE field, and the THRESHOLD ARMING field that are used for logical block provisioning thresholds. See the
Logical Block Provisioning mode page (see 6.5.9) for the definition of these fields.
4.7.3.7.3 Threshold percentages
The end points of the range over which a logical block provisioning threshold percentages operates are
defined as follows:
threshold minimum = (threshold count – (threshold percentage size × 0.5))
threshold maximum = (threshold count + (threshold percentage size × 0.5))
where:
threshold minimum
is the lowest percentage of device resources available for allocation to logical
blocks in the range for this threshold;
threshold maximum
is the highest percentage of device resources available for allocation to
logical blocks in the range for this threshold;
threshold count
is the center of the threshold range for this threshold (i.e., the threshold count
value as specified in the threshold descriptor in the Logical Block
Provisioning mode page); and
threshold set size
is the percentage of allocation resources in each threshold percentage (i.e.,
the percentage indicated by the THRESHOLD PERCENTAGE field (see 6.6.7)).
Table 7 — Threshold resource value, threshold type value, and threshold arming value for logical
block provisioning thresholds
Threshold
resource
value
Threshold
type value
Threshold
arming
value
Description
01h
000b
000b
The device server applies the threshold to the availability of
LBA mapping resources and performs notifications as the
availability of those resources decreases. a
02h
000b
001b
The device server applies the threshold to the usage of LBA
mapping resources and performs notifications as the usage of
those resources increases.
All other combinations
Reserved
a The point when availability of LBA mapping resources reaches zero corresponds to the persistent lack
of LBA mapping resources described in 4.7.3.6.1.


Table 8 defines the meaning of the combinations of values for the THRESHOLD RESOURCE field, the THRESHOLD
TYPE field, and the THRESHOLD ARMING field that are used for logical block provisioning threshold percentages.
See the Logical Block Provisioning mode page (see 6.5.9) for the definition of these fields.
4.7.3.7.4 Logical block provisioning armed decreasing thresholds
Figure 7 shows the operation of a logical block provisioning armed decreasing threshold. Figure 7 represents
the entire range of possible values over which the threshold is being applied (e.g., for an available resource,
the lowest value represents zero available resources and the highest value represents the maximum possible
number of available resources).
If enabled, reporting of armed decreasing threshold events (i.e., the THRESHOLD ARMING field is set to 000b in
the threshold descriptor in the Logical Block Provisioning mode page (see 6.5.9)) operates as shown in
figure 7.
Figure 7 — Armed decreasing threshold operation
4.7.3.7.5 Logical block provisioning armed increasing thresholds
Figure 8 shows the operation of a logical block provisioning armed increasing threshold. Figure 8 represents
the entire range of possible values over which the threshold is being applied (e.g., for tracking usage of a
resource, the lowest value represents zero resources being used and the highest value represents the
maximum possible number of resources being used).
Table 8 — Threshold resource value, threshold type value, and threshold arming value for logical
block provisioning percentages
Threshold
resource
value
Threshold
type value
Threshold
arming
value
Description
03h
001b
000b
The device server applies the threshold to the availability of
LBA mapping resources and performs notifications as the
availability of those resources decreases.
All other combinations
Reserved
Lowest value
Highest value
a
b
c
d
Threshold minimum
Threshold maximum
Threshold range
Notes:
a)
if the value to which the threshold is being applied drops below the threshold maximum for the
threshold range, then the notification trigger shall be enabled;
b)
if the value to which the threshold is being applied increases above the threshold maximum for
the threshold range, then the notification trigger shall be disabled;
c)
if the notification trigger is enabled, then the device server may disable the notification trigger
and perform logical block provisioning threshold notification (see 4.7.3.7.6); and
d)
if the notification trigger is enabled and the value to which the threshold is being applied drops
below the threshold minimum for the threshold range, then the device server shall disable the
notification trigger and perform logical block provisioning threshold notification as defined in
4.7.3.7.6.


If enabled, reporting of armed increasing threshold events (i.e., the THRESHOLD ARMING field is set to 001b in
the threshold descriptor in the Logical Block Provisioning mode page (see 6.5.9)) operates as shown in
figure 8.
Figure 8 — Armed increasing threshold operation
4.7.3.7.6 Logical block provisioning threshold notification
If the LBPERE bit is set to one in the Read-Write Error Recovery mode page (see 6.5.10), then logical block
provisioning threshold notification is enabled and the device server shall perform notification for thresholds
with the THRESHOLD TYPE field set to 000b in the threshold descriptor in the Logical Block Provisioning mode
page (see 6.5.9) as follows:
a)
if the SITUA bit is set to one in the Logical Block Provisioning mode page, then:
A) if the device server has not established a unit attention condition as a result of this threshold
being crossed since the last logical unit reset (see SAM-6) and a command through which the
device server is able to report a unit attention condition arrives on any I_T nexus, then the device
server shall establish a unit attention condition with the additional sense code set to THIN PROVI-
SIONING SOFT THRESHOLD REACHED for only the SCSI initiator port associated with the I_T
nexus on which that command was received before processing that command; or
B) if the device server has established a unit attention condition as a result of this threshold being
crossed since the last logical unit reset and a command through which the device server is able to
report a unit attention condition arrives on any I_T nexus, then the device server should establish
a unit attention condition with the additional sense code set to THIN PROVISIONING SOFT
THRESHOLD REACHED for only the SCSI initiator port associated with the I_T nexus on which
that command was received before processing that command unless establishment of the unit
attention condition causes a vendor specific frequency of unit attention conditions for this
threshold to be exceeded;
or
b)
if the SITUA bit is set to zero, then:
A) if the device server has not established a unit attention condition for the SCSI initiator port
associated with all I_T nexuses as a result of this threshold being crossed since the last logical
unit reset (see SAM-6), then the device server shall establish a unit attention condition with the
additional sense code set to THIN PROVISIONING SOFT THRESHOLD REACHED for the SCSI
initiator port associated with every I_T nexus; or
B) if the device server has established a unit attention condition for the SCSI initiator ports
associated with all I_T nexuses as a result of this threshold being crossed since the last logical
unit reset, then the device server should establish a unit attention condition with the additional
Lowest value
Highest value
a
b
c
d
Threshold minimum
Threshold maximum
Threshold range
Notes:
a)
if the value to which the threshold is being applied increases above the threshold minimum for
the threshold range, then the notification trigger shall be enabled;
b)
if the value to which the threshold is being applied decreases below the threshold minimum for
the threshold range, then the notification trigger shall be disabled;
c)
if the notification trigger is enabled, then the device server may disable the notification trigger
and perform logical block provisioning threshold notification (see 4.7.3.7.6); and
d)
if the notification trigger is enabled and the value to which the threshold is being applied
increases above the threshold maximum for the threshold range, then the device server shall
disable the notification trigger and perform logical block provisioning threshold notification as
defined in 4.7.3.7.6.


sense code set to THIN PROVISIONING SOFT THRESHOLD REACHED for the SCSI initiator
port associated with every I_T nexus, unless establishment of the unit attention condition causes
a vendor specific frequency of unit attention conditions for this threshold to be exceeded.
If a unit attention condition is established as described in this subclause, then the device server shall report
the following value in the INFORMATION field in the sense data (see SPC-6):
a)
the byte offset in the Logical Block Provisioning mode page of the first byte of the threshold descriptor
to which this threshold notification applies.
If a unit attention condition with the additional sense code set to THIN PROVISIONING SOFT THRESHOLD
REACHED is received by the application client, then the application client should reissue the command and
take further recovery actions (e.g., administrator notification or other administrator actions). These recovery
actions are not defined by this standard.
If the LBPERE bit is set to zero, then logical block provisioning threshold notification is disabled and the device
server shall not establish any unit attention condition with the additional sense code set to THIN
PROVISIONING SOFT THRESHOLD REACHED.
An additional sense code set to THIN PROVISIONING SOFT THRESHOLD REACHED is applicable to both
thin provisioned logical units (see 4.7.3.3) and resource provisioned logical units (see 4.7.3.2).
4.7.4 LBP (logical block provisioning) state machine
4.7.4.1 LBP state machine overview
The LBP (logical block provisioning) state machine describes the mapping and unmapping of a single LBA by
the device server for a thin provisioned logical unit (see 4.7.3.3) or a resource provisioned logical unit
(see 4.7.3.2). This state machine does not apply to fully provisioned logical units (see 4.7.2).
There is one instance of this state machine for each LBA. If a command requests mapping or unmapping of
more than one LBA, then there may be an independent transition in each instance of the state machine (e.g.,
each LBA may individually transition from mapped to deallocated or from anchored to deallocated).
4.7.4.2 LBP state machine for logical units supporting anchored LBAs
If the logical unit supports anchored LBAs (i.e., the ANC_SUP bit is set to one) and deallocated LBAs (i.e., is a
thin provisioned logical unit, or a resource provisioned logical unit), then this state machine consists of the
following states:
a)
LBP1:Mapped state (see 4.7.4.5);
b)
LBP2:Deallocated state (see 4.7.4.6) (initial state for thin provisioned logical units); and
c)
LBP3:Anchored state (see 4.7.4.7) (initial state for resource provisioned logical units supporting
anchored LBAs).
For thin provisioned logical units the initial state of the state machine associated with each LBA is the
LBP2:Deallocated state.
For resource provisioned logical units supporting anchored LBAs the initial state of the state machine
associated with each LBA is the LBP3:Anchored state.


Figure 9 describes the LBP state machine for a logical unit that supports anchored LBAs and deallocated
LBAs.
Figure 9 — LBP state machine (anchored LBAs supported and deallocated LBAs supported)
4.7.4.3 LBP state machine for logical units not supporting anchored LBAs
If the logical unit does not support anchored LBAs (i.e., is a thin provisioned logical unit and the ANC_SUP bit is
set to zero or a resource provisioned logical unit and the ANC_SUP bit is set to zero), then this state machine
consists of the following states:
a)
LBP1:Mapped state(see 4.7.4.5); and
b)
LBP2:Deallocated state (see 4.7.4.6).
The initial state of the state machine associated with each LBA is the LBP2:Deallocated state.
Figure 10 describes the LBP state machine for a logical unit that does not support anchored LBAs.
Figure 10 — LBP state machine (anchored LBAs not supported)
4.7.4.4 Performing read operations with respect to logical block provisioning
Table 9 defines the logical block data that a read operation shall return for a mapped LBA.
LBP1:Mapped
LBP2:Deallocated
LBP3:Anchored
LBP1:Mapped
LBP2:Deallocated


Table 9 — Logical block data returned by a read operation from a mapped LBA
Condition
Logical block data returned
The LBA became mapped as the result of a format
operation or sanitize operation and no write command
has specified that LBA since the LBA became
mapped.
The logical block data that was written to that
LBA by the format operation or the sanitize
operation.
The LBA became mapped as the result of a write
command and no additional write command has
specified that LBA since the LBA was mapped.
The logical block data that was written to that
LBA by that write command.
The LBA became mapped as the result of an
autonomous transition, and no write command has
specified that LBA since the LBA was mapped.
The logical block data returned is the same as if
that autonomous transition had not occurred and
the LBA had remained unmapped (see table 10).
A write command has specified that LBA since that
LBA was mapped.
The logical block data that was most recently
written to that LBA.


Table 10 defines the logical block data that a read operation shall return for an unmapped LBA.
After a read operation returns a value for an LBA, subsequent read operations from that LBA shall return the
same value until a subsequent command alters the logical block data in that LBA (e.g., a write command or an
unmap command (see table 34)).
4.7.4.5 LBP1:Mapped state
4.7.4.5.1 LBP1:Mapped state description
Upon entry into this state, the relationship between the LBA and the physical block(s) that contains the logical
block for that LBA shall be established.
Table 10 — Logical block data returned by a read operation from an unmapped LBA
LBPRZ
field a
Method used to
unmap the LBA
Logical block data returned
000b
see b
The value specified to be written if the write operation had been performed.
see c
Logical block data containing:
a)
user data set to a vendor-specific value that is not obtained from any
other LBA; and
b)
protection information, if any, set to FFFF_FFFF_FFFF_FFFFh.
xx1b
Any
Logical block data containing:
a)
user data set to zero; and
b)
protection information, if any, with the:
A)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h (i.e., the
valid CRC for user data in which all bits are set to zero);
B)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
C)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh.
010b
Any
Logical block data containing:
a)
user data set to the provisioning initialization pattern; and
b)
protection information, if any, with the:
A)
LOGICAL BLOCK GUARD field set to FFFFh or set to the CRC for the
provisioning initialization pattern;
B)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
C)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh.
a The LBPRZ field is in the Logical Block Provisioning VPD page (see 6.6.7).
b A command for which the device server is allowed to perform either:
a)
a write with specified logical block data; or
b)
an unmap operation if the logical block data returned by read operations from unmapped LBAs
matches  the logical block data specified for the command that resulted in the unmap operation.
These commands are:
a)
a FORMAT UNIT command specifying an initialization pattern;
b)
a SANITIZE command specifying a sanitize overwrite operation; and
c)
a WRITE SAME command with the UNMAP bit set to one.
c These methods include but are not limited to:
a)
a FORMAT UNIT command not specifying an initialization pattern;
b)
a REASSIGN BLOCKS command;
c)
a SANITIZE command specifying a sanitize block erase operation or a sanitize cryptographic erase
operation; and
d)
an UNMAP command.


If this state was entered from the LBP2:Deallocated state (see 4.7.4.6), then the device server shall allocate
LBA mapping resources, if any, required to map the LBA.
If this state was entered from the LBP3:Anchored state (see 4.7.4.7), then:
a)
the device server shall not allocate LBA mapping resources; and
b)
the resource exhaustion conditions described in 4.7.3.6.1 shall not occur.
4.7.4.5.2 Transition LBP1:Mapped to LBP2:Deallocated
This transition shall occur after:
a)
an unmap operation that results in the deallocation of the LBA that was mapped.
This transition may occur at any time if the LBPRZ field (see 6.6.7) is set to:
a)
xx1b, and the mapped LBA references a logical block that contains:
A) user data with all bits set to zero; and
B) protection information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh;
or
b)
010b, and a mapped LBA references a logical block that contains;
A) user data set to the provisioning initialization pattern; and
B) protection information, if any,with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to the CRC for the provisioning initialization
pattern;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh.
4.7.4.5.3 Transition LBP1:Mapped to LBP3:Anchored
This transition shall occur after:
a)
an unmap operation that results in the anchoring of the LBA that was mapped.
This transition may occur at any time if the LBPRZ field (see 6.6.7) is set to:
a)
xx1b, and the mapped LBA references a logical block that contains:
A) user data with all bits set to zero; and
B) protection information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh;
or
b)
010b, and a mapped LBA references a logical block that contains;
A) user data set to the provisioning initialization pattern; and
B) protection information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to the CRC for the provisioning initialization
pattern;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh.
4.7.4.6 LBP2:Deallocated state
4.7.4.6.1 LBP2:Deallocated state description
While in this state:
a)
there shall be no relationship between the LBA and any physical block(s); and


b)
the device server should deallocate LBA mapping resources after they are no longer in use.
For an LBA in this state, an unmap operation that specifies deallocation of the LBA shall not cause a transition
from this state.
The device server shall process a read command specifying an LBA in this state (i.e., a deallocated LBA) as
described in table 10.
4.7.4.6.2 Transition LBP2:Deallocated to LBP1:Mapped
This transition:
a)
shall occur after a write operation to the LBA that was deallocated; or
b)
may occur at any time for reasons not defined by this standard.
4.7.4.6.3 Transition LBP2:Deallocated to LBP3:Anchored
This transition:
a)
shall occur after an unmap operation that results in anchoring of the LBA that was deallocated; or
b)
may occur at any time for reasons not defined by this standard.
4.7.4.7 LBP3:Anchored state
4.7.4.7.1 LBP3:Anchored state description
Upon entry into this state:
a)
LBA mapping resources shall be associated with the LBA; and
b)
there may or may not be a relationship between the LBA and physical block(s).
If this state was entered from the LBP2:Deallocated state, then the device server shall allocate LBA mapping
resources, if any, required to anchor the LBA.
If this state was entered from the LBP1:Mapped state, then:
a)
the device server shall not allocate LBA mapping resources;
b)
the device server relies on LBA mapping resources already allocated to the LBA; and
c)
the resource exhaustion conditions described in 4.7.3.6.1 shall not occur.
For an LBA in this state, an unmap operation that specifies anchoring of the LBA shall not cause a transition
from of this state.
The device server shall process a read command specifying an LBA in this state (i.e., an anchored LBA) as
described in table 10.
4.7.4.7.2 Transition LBP3:Anchored to LBP1:Mapped
This transition:
a)
shall occur after a write operation to the LBA that was anchored; or
b)
may occur at any time for reasons not defined by this standard.
4.7.4.7.3 Transition LBP3:Anchored to LBP2:Deallocated
This transition shall occur after:
a)
an unmap operation that results in the deallocation of the LBA that was anchored.


4.8 Data de-duplication
Data de-duplication is the ability of a device server to recognize redundant or duplicate data and reduce the
number of duplicate or redundant copies of the data while maintaining the application client supplied LBAs of
the duplicate or redundant copies of the data. De-duplication shall not affect protection information, if any.
Logical units that support data de-duplication may report a count of LBA resources that have been made
available as a result of being de-duplicated (see 6.4.5.5).
Data de-duplication may impact the number of LBA Mapping resources indicated in the Logical Block
Provisioning log page (see 6.4.5) (e.g., the value indicated in the Available LBA Mapping Resource Count log
parameter (see 6.4.5.2) and the Used LBA Mapping Resource Count log parameter (see 6.4.5.3) may not
change as a result of successful write operations that contain data that is de-duplicated or successful unmap
operations on LBAs that contain data that has been de-duplicated).
4.9 Ready state
A direct access block device is ready when the device server is capable of processing logical block access
commands that require access to the medium (see 4.2.2).
A direct access block device using a removable medium (see 4.4) is not ready until a volume is mounted and
other conditions are met (see 4.3). While a direct access block device is not ready the device server shall
terminate logical block access commands with CHECK CONDITION status with the sense key set to NOT
READY and the appropriate additional sense code for the condition.
Some direct access block devices may be switched from being ready to being not ready by using the START
STOP UNIT command (see 5.31).
To make a direct access block device ready, an application client may be required to issue a START STOP
UNIT command:
a)
with a START bit set to one and the POWER CONDITION field set to 0h (i.e., START_VALID); or
b)
with the POWER CONDITION field set to 1h (i.e., ACTIVE).
4.10 Initialization
A direct access block device may require initialization of its medium prior to processing logical block access
commands. This initialization is requested by an application client using a FORMAT UNIT command (see 5.4).
Parameters related to the format (e.g., logical block length) may be set with a MODE SELECT command (see
SPC-6 and 6.5.2) prior to the format operation. Some direct access block devices are initialized by means not
defined by this standard. The time when the initialization occurs is vendor specific.
Direct access block devices using a non-volatile medium may save the parameters related to the format and
only require initialization once. However, some mode parameters may require initialization after each logical
unit reset. A catastrophic failure of the direct access block device may require that an application client send a
FORMAT UNIT command to recover from the failure.
Direct access block devices that use a volatile medium may require initialization after each logical unit reset
prior to the processing of logical block access commands (see 4.2.2). Mode parameters may also require
initialization after logical unit resets.
NOTE 2 - It is possible that mode parameter block descriptors read with a MODE SENSE command before a
FORMAT UNIT completes contain information not reflecting the true state of the medium.
A direct access block device may become format corrupt after processing a MODE SELECT command that
changes parameters (e.g., the logical block length) related to the medium format. During this time, the device
server may terminate logical block access commands with CHECK CONDITION status with the sense key set
to NOT READY and the appropriate additional sense code for the condition.
