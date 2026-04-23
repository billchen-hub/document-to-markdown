# 4.15 Caches

c)
the CYLINDER NUMBER field in the first address descriptor shall be less than the CYLINDER NUMBER field
in the second address descriptor;
d)
the HEAD NUMBER field in the first address descriptor shall be equal to the HEAD NUMBER field in the
second address descriptor;
e)
for a pair of extended bytes from index format address descriptors, the BYTES FROM INDEX field in the
first address descriptor and the second address descriptor shall be equal to FFF_FFFFh; and
f)
for a pair of extended physical sector format address descriptors, the SECTOR NUMBER field in the first
address descriptor and the second address descriptor shall be equal to FFF_FFFFh.
4.14 Write and unmap failures
If any write command that is not an atomic write command, does not complete successfully (e.g., the
command completed with CHECK CONDITION status, or the command was being processed at the time of a
power loss or an incorrect demount of a removable medium), then any data in the logical blocks referenced by
the LBAs specified by that command is indeterminate. Before sending a read command or verify command
specifying any LBAs that were specified by a write command that did not complete successfully, the
application client should resend that write command. If an application client sends a read command or verify
command specifying any LBAs that were specified by a write command that did not complete successfully
before resending that write command, then the device server may return old data, new data, vendor-specific
data, or any combination thereof for the logical blocks referenced by the specified LBAs.
If logical block provisioning (see 4.7) is supported and one or more unmap commands have not completed
when a power loss, medium error, or hardware error occurs, then the logical block provisioning state of the
LBAs requested to be unmapped by any of those commands may or may not have changed. The application
client should resend that unmap command.
4.15 Caches
4.15.1 Caches overview
Direct access block devices may implement caches. A cache is an area of temporary storage in the direct
access block device (e.g., to enhance performance) separate from the medium that is not directly accessible
by the application client.
A cache stores logical block data.
A cache may be volatile or non-volatile. A volatile cache does not retain data through power cycles. A
non-volatile cache retains data through power cycles. There may be a limit on the amount of time a
non-volatile cache is able to retain data without power (see 4.15.10).
4.15.2 Cache segments
The cache may be divided into cache segments. The device server may allow application client control over
cache segments using the following in the Caching mode page (see 6.5.6):
a)
the IC bit;
b)
the NUMBER OF CACHE SEGMENTS field;
c)
the CACHE SEGMENT SIZE field; and
d)
the SIZE bit.
Cache segments may be grouped where each group is identified by a cache ID. An application client may
request that a specific group of cache segments be used for an IO through the use of IO advice hints
(see 4.30). The GROUP NUMBER field in each command specifies the cache ID of the cache segments to use
during the processing of that command.The algorithms used to manage the data in each cache segment is not
defined by this standard. How cache segments are associated with cache IDs is not defined by this standard.


4.15.3 Read caching
While processing read commands and verify commands, the device server may use the cache to store logical
blocks that the application client may request at some future time. The algorithm used to manage the cache is
not part of this standard. However, parameters are provided (see 6.5.6) to advise the device server about
future requests, or to restrict the use of cache for a particular request.
4.15.4 Write caching
While processing write commands, the device server may perform a write cache operation to store logical
block data that is to be written to the medium at a later time with a write medium operation. This is called
writeback caching. A write command may complete prior to logical blocks being written to the medium. As a
result of using writeback caching there is a period of time during which the logical block data may be lost if:
a)
power to the SCSI target device is lost and a volatile cache is being used; or
b)
a hardware failure occurs.
There is also the possibility of an error occurring during the subsequent write medium operation. If an error
occurs during the write medium operation, then the error may be reported as a deferred error on a later
command. The application client may request that writeback caching be disabled with the Caching mode page
(see 6.5.6) to prevent detected write errors from being reported as deferred errors. Even with writeback
caching disabled, undetected write errors may occur. Verify commands (e.g., VERIFY and WRITE AND
VERIFY) may be used to detect those errors.
If processing a write command results in logical block data in cache that is different from the logical block data
on the medium, then the device server shall retain that logical block data in cache until a write medium
operation is performed using that logical block data. After the write medium operation is complete, the device
server may retain that logical block data in cache.
4.15.5 Command interactions with caches
The application client may affect behavior of the cache with:
a)
the PRE-FETCH commands (see 5.13 and 5.14);
b)
the SYNCHRONIZE CACHE commands (see 5.33 and 5.34); and
c)
the Caching mode page (see 6.5.6).
When the cache becomes full of logical block data, the device server may replace the logical block data in the
cache with new logical block data. The disable page out (DPO) bit in the CDBs of read commands, verify
commands, and write commands allows the application client to influence the replacement of logical block
data in the cache. A read command, verify command, or a write command with a DPO bit set to one is a hint to
the device server that the logical blocks specified by that command are not likely to be accessed in the near
future and should not be put in the cache or retained by the cache.
Application clients may use the force unit access (FUA) bit in the CDBs of read commands (e.g., see 5.16) or
write commands (e.g., see 5.40) to specify that the device server shall access:
a)
the medium;
b)
non-volatile cache; or
c)
the specified data pattern for that LBA (e.g., the data pattern for unmapped data (see 4.7.4.4)).
Setting the DPO bit to one (e.g., see 5.16) and the FUA bit to one in all read commands and all write commands
has the same effect as bypassing the volatile cache.
4.15.6 Write operation and write medium operation interactions with caches
For each LBA accessed by a write operation:
1)
if a cache contains more recent logical block data for that LBA than the medium, then the device
server shall:
A) perform a write cache operation to that LBA to update the logical block data in the cache;


B) invalidate that LBA in the cache and perform a write medium operation to that LBA; or
C) perform a write cache operation to that LBA to update the logical block data in the cache and
perform a write medium operation to that LBA.
For each LBA accessed by a write medium operation that is not part of a write operation:
1)
if a cache contains more recent logical block data for that LBA than the medium, then the device
server shall:
A) perform a write cache operation to that LBA to update the logical block data in the cache; or
B) invalidate that LBA in the cache, before the device server performs the write medium operation to
that LBA.
4.15.7 Read operation and read medium operation interactions with caches
For each LBA accessed by a read operation:
1)
if a cache contains more recent logical block data for that LBA than the medium, then the device
server shall perform a read cache operation from that LBA; or
2)
the device server shall perform a read medium operation from that LBA.
For each LBA accessed by a read medium operation that is not part of a read operation:
1)
if a cache contains more recent logical block data for the LBA than the medium, then the device
server shall perform a write medium operation to that LBA; and
2)
the device server may invalidate that LBA in the cache, before the device server performs the read
medium operation from that LBA.
4.15.8 Verify medium operation interactions with caches
For each LBA accessed by a verify medium operation:
1)
if a cache contains more recent logical block data for the LBA than the medium, then the device
server shall perform a write medium operation to that LBA;
2)
the device server may invalidate that LBA in the cache; and
3)
before the device server performs the verify medium operation from that LBA.
4.15.9 Unmap operation interactions with caches
During an unmap operation, the device server changes any logical block data in the cache for the LBA
unmapped by the operation so that any logical block data transferred by the device server to the Data-In
Buffer while processing a subsequent read command reflects the results of the unmap operation (see
4.7.4.6.1 and 4.7.4.7.1).
4.15.10 Power loss effects on caches
The power, if any, needed to maintain a non-volatile cache may decrease to the point that the device server is
unable to ensure the non-volatility of the cache for a vendor specific interval of time (e.g., the battery voltage
becomes too low too sustain cache contents beyond a vendor specific time). If this occurs and the Extended
INQUIRY Data VPD page (see SPC-6) indicates that the device server contains non-volatile cache (i.e.,
NV_SUP bit set to one), then:
a)
if the reporting of informational exceptions control warnings is enabled (i.e., the EWASC bit is set to
one in the Information Exceptions Control mode page (see 6.5.8)), then the device server shall report
the degraded non-volatile cache as specified in the Information Exceptions Control mode page with
an additional sense code set to WARNING - DEGRADED POWER TO NON-VOLATILE CACHE; or
b)
if the reporting of informational exceptions control warnings is disabled (i.e., the EWASC bit is set to
zero in the Information Exceptions Control mode page), then the device server shall establish a unit
attention condition (see SAM-6) for the SCSI initiator port associated with every I_T nexus with the
additional sense code set to WARNING - DEGRADED POWER TO NON-VOLATILE CACHE.


Non-volatile caches may become volatile (e.g., battery voltage becomes too low to sustain cache contents
when power is lost). If non-volatile caches become volatile, then logical block data transferred for read
commands or write commands in which the force unit access (FUA) bit in the CDB is set to one may bypass
the cache.
If a non-volatile cache becomes volatile, then the device server shall set the REMAINING NON-VOLATILE TIME
field to zero in the Non-volatile Cache log page (see 6.4.7).
If non-volatile cache becomes volatile and the Extended INQUIRY Data VPD page (see SPC-6) indicates that
the device server contains non-volatile cache (i.e., the NV_SUP bit is set to one), then:
a)
if the reporting of informational exceptions control warnings is enabled (i.e., the EWASC bit is set to
one in the Information Exceptions Control mode page (see 6.5.8)), then the device server shall report
the change in the cache as specified in the Information Exceptions Control mode page with the
additional sense code set to WARNING - NON-VOLATILE CACHE NOW VOLATILE; or
b)
if the reporting of informational exceptions control warnings is disabled (i.e., the EWASC bit is set to
zero in the Information Exceptions Control mode page), then the device server shall establish a unit
attention condition (see SAM-6) for the SCSI initiator port associated with every I_T nexus with the
additional sense code set to WARNING - NON-VOLATILE CACHE NOW VOLATILE.
If:
a)
a power on or hard reset occurs;
b)
the Extended INQUIRY Data VPD page indicates that the device server contains a non-volatile cache
(i.e., the NV_SUP bit is set to one); and
c)
the non-volatile cache is currently volatile,
then the device server shall establish a unit attention condition for the SCSI initiator port associated with every
I_T nexus with the additional sense code set to WARNING - NON-VOLATILE CACHE NOW VOLATILE.
4.16 Implicit head of queue command processing
Each of the following commands defined by this standard may be processed by the task manager as if it has a
HEAD OF QUEUE task attribute (see SAM-6), even if the command is received with a SIMPLE task attribute or an
ORDERED task attribute:
a)
the READ CAPACITY (10) command (see 5.20); and
b)
the READ CAPACITY (16) command (see 5.21).
The following command defined by this standard shall be processed by the task manager as if it has a HEAD
OF QUEUE task attribute, even if the command is received with a SIMPLE task attribute or an ORDERED task
attribute:
a)
the SANITIZE command (see 5.30).
See SPC-6 for additional commands subject to implicit HEAD OF QUEUE command processing. See SAM-6 for
additional rules on implicit head of queue processing.
