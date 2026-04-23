# SBC feature sets

Annex H
(normative)
SBC feature sets
H.1 Overview
This annex defines SCSI feature sets (see SPC-6) for block devices.
Table H.1 lists the feature sets.
H.2 SBC Base 2010 feature set
H.2.1 SBC Base 2010 feature set overview
The SBC Base 2010 feature set includes features intended for use by operating system direct access block
storage device class drivers during operating system initialization and runtime. The features defined in this
feature set are intended to provide compatibility with software designed for device servers that don’t support
16 byte media access commands.
Device servers that support the SBC Base 2010 feature set may also support the SBC Base 2016 feature set
(see clause H.3)
Table H.1 — Feature sets
Feature set
Feature set code
Reference
Reserved
0000h
SBC Base 2010
0102h
Clause H.2
SBC Base 2016
0101h
Clause H.3
Basic Provisioning 2016
0103h
Clause H.4
Drive Maintenance 2016
0104h
Clause H.5
Reserved
all others


Table H.2 lists the commands that are mandatory or have additional mandatory requirements for support of
the SBC Base 2010 feature set.
Table H.3 lists the SBC Base 2010 mandatory block descriptors and mode pages.
Table H.2 — Commands mandatory for the SBC Base 2010 feature set
Command
Additional requirements
reference
Reference
FORMAT UNIT
H.3.3.1  a
5.4
INQUIRY
n/a
SPC-6
MODE SELECT (10)
H.3.4  a
SPC-6
MODE SENSE (10)
H.3.4  a
SPC-6
READ (10)
n/a
5.16
READ CAPACITY (10)
H.2.2.1
5.20
REPORT LUNS
n/a
SPC-6
REQUEST SENSE
n/a
SPC-6
START STOP UNIT
n/a
5.31
SYNCHRONIZE CACHE (10)
H.2.2.2
5.33
TEST UNIT READY
n/a
SPC-6
WRITE (10)
n/a
5.40
WRITE SAME (10)
H.2.2.3
5.52
a The additional requirements for this command are the same as the SBC Base 2016
additional requirements for this command.
Table H.3 — Block descriptor and mode pages mandatory for the SBC Base 2010 feature set
Mode page
Additional requirements
reference
Reference
Block descriptors
Mode parameter block descriptor
H.3.4.1  a
6.5.2
Mode pages
Caching
H.3.4.2  a
6.5.6
Control
H.3.4.3  a
SPC-6
Control Extension
n/a
SPC-6
Read-Write Error Recovery
H.3.4.5  a
6.5.10
a The additional requirements for this block descriptor or mode page are the same as
the SBC Base 2016 additional requirements for this block descriptor or mode page.


Table H.4 lists the SBC Base 2010 feature set VPD pages.
H.2.2 SBC Base 2010 feature set commands
H.2.2.1 READ CAPACITY (10) command
The requirements for the READ CAPACITY (10) command are the same as the requirements for the READ
CAPACITY (16) command in the SBC Base 2016 feature set (see H.3.3.2).
H.2.2.2 SYNCHRONIZE CACHE (10) command
The requirements for the SYNCHRONIZE CACHE (10) command are the same as the requirements for the
SYNCHRONIZE CACHE (16) command in the SBC Base 2016 feature set (see H.3.3.6).
H.2.2.3 WRITE SAME (10) command
The requirements for the WRITE SAME (10) command are the same as the requirements for the WRITE
SAME (16) command in the SBC Base 2016 feature set (see H.3.3.7).
H.3 SBC Base 2016 feature set
H.3.1 SBC Base 2016 feature set overview
The SBC Base 2016 feature set includes features used by operating system direct access block storage
device class drivers during operating system initialization and runtime. The features defined in this feature set
provide application clients with the versions of the commands that offer the largest LBA range and most
extensibility of commands in an SBC base feature set (e.g., requires support of the 16 byte versions of
commands that have both 10 byte and 16 byte versions).
Device servers that support the SBC Base 2016 feature set may support the SBC Base 2010 feature set (see
clause H.2).
Table H.4 — VPD pages mandatory for the SBC Base 2010 feature set
VPD page
Additional requirements
reference
Reference
ATA Information  a
n/a
SAT-4
Block Device Characteristics
H.3.5.1  b
6.6.2
Device Identification  c
n/a
SPC-6
Extended INQUIRY Data  c
H.3.5.3  b
SPC-6
Mode Page Policy  c
n/a
SPC-6
SCSI Feature Sets  c
n/a
SPC-6
Supported VPD Pages  c
n/a
SPC-6
Power Condition
n/a
SPC-6
a Mandatory for devices that implement SAT-4, optional for all other device types
b The additional requirements for this command are the same as the SBC Base 2016
additional requirements for this command.
c VPD page shall be available without incurring any medium access delays even if the
device server is not ready for other commands (i.e., the device server shall not
return ASCII spaces (20h) in ASCII fields and zeros in other fields until the data is
available from the media).


Table H.5 lists the commands that are mandatory or have additional mandatory requirements for support of
the SBC Base 2016 feature set.
Table H.6 lists the SBC Base 2016 mandatory block descriptors and mode pages .
Table H.5 — Commands mandatory for the SBC Base 2016 feature set
Command
Additional requirements
reference
Reference
FORMAT UNIT
H.3.3.1
5.4
INQUIRY
n/a
SPC-6
MODE SELECT (10)
H.3.4
SPC-6
MODE SENSE (10)
H.3.4
SPC-6
READ (16)
n/a
5.18
READ CAPACITY (16)
H.3.3.2
5.21
REPORT LUNS
n/a
SPC-6
REPORT SUPPORTED OPERATION
CODES
H.3.3.3
SPC-6
REPORT SUPPORTED TASK
MANAGEMENT FUNCTIONS
H.3.3.4
SPC-6
REQUEST SENSE
H.3.3.5
SPC-6
START STOP UNIT
n/a
5.31
SYNCHRONIZE CACHE (16)
H.3.3.6
5.34
TEST UNIT READY
n/a
SPC-6
WRITE (16)
n/a
5.42
WRITE SAME (16)
H.3.3.7
5.53
Table H.6 — Block descriptor and mode pages mandatory for the SBC Base 2010 feature set
Mode page
Additional requirements
reference
Reference
Block descriptors
Mode parameter block descriptor
H.3.4.1
6.5.2
Mode pages
Caching
H.3.4.2
6.5.6
Control
H.3.4.3
SPC-6
Control Extension
n/a
SPC-6
Information Exceptions Control
H.3.4.4
6.5.8
Read-Write Error Recovery
H.3.4.5
6.5.10


Table H.7 lists the SBC Base 2016 feature set VPD pages.
H.3.2 SBC Base 2016 feature set model
The device server shall support the Discovery 2016 feature set (see SPC-6).
If the device server supports LBAs greater than FFFF_FFFFh, then the device server shall support descriptor
format sense data (see SPC-6).
If the device server implements a volatile writeback cache (see 4.15), then the device server shall:
a)
set the V_SUP bit to one in the Extended INQUIRY Data VPD page (see SPC-6); and
b)
support the FUA bit set to one in commands performing write operations.
If the device server implements a non-volatile writeback cache that may become volatile (see 4.15.10), then
the device server shall:
a)
set the NV_SUP bit to one in the Extended INQUIRY Data VPD page (see SPC-6).
H.3.3 SBC Base 2016 feature set commands
H.3.3.1 FORMAT UNIT command
If the device server does not implement logical block provisioning, then the default initialization pattern shall
be set to all zeros. If the device server implements logical block provisioning then the default initialization
pattern shall be set to all zeros or the provisioning initialization pattern.
The device server shall support the following bits in the FORMAT UNIT CDB (see 5.4.1):
a)
the LONGLIST bit set to one (i.e., long parameter list header is supported);
b)
the FMTDATA bit set to one (i.e., parameter list is supported); and
c)
if protection information is supported, then the FMTPINFO field in the CDB and the PROTECTION FIELD
USAGE field in the parameter data.
The device server shall support the following bits in the FORMAT UNIT parameter list header (see 5.4.2.2):
a)
the FOV bit set to one (i.e., format options are supported);
Table H.7 — VPD pages mandatory for the SBC Base 2016 feature set
VPD page
Additional requirements
reference
Reference
ATA Information  a
n/a
SAT-4
Block Device Characteristics
H.3.5.1
6.6.2
Block Limits
H.3.5.2
6.6.4
Device Identification  b
n/a
SPC-6
Extended INQUIRY Data  b
H.3.5.3
SPC-6
Mode Page Policy  b
n/a
SPC-6
SCSI Feature Sets  b
n/a
SPC-6
Supported VPD Pages  b
n/a
SPC-6
Power Condition
n/a
SPC-6
a Mandatory for devices that implement SAT-4, optional for all other device types
b VPD page shall be available without incurring any medium access delays even if the
device server is not ready for other commands (i.e., the device server shall not
return ASCII spaces (20h) in ASCII fields and zeros in other fields until the data is
available from the media).


b)
the IP bit set to one (i.e., an initialization pattern descriptor is supported); and
c)
the IMMED bit set to one.
H.3.3.2 READ CAPACITY (16) command
The device server shall report the following values in the READ CAPACITY (16) parameter data:
a)
the LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to a value that represents the number of
bytes that the device is able to write to the media as a unit (e.g., based on the NAND page size); and
b)
the LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0000h (i.e., LBA 0 is aligned).
H.3.3.3 REPORT SUPPORTED OPERATION CODES command
The device server shall support the following bits or fields in the CDB:
a)
the RCTD bit set to one (i.e., returning command timeouts descriptors is supported); and
b)
the REPORTING OPTIONS field set to:
A) 000b (i.e., operation codes and service actions);
B) 001b (i.e., command support data for an operation code); and
C) 010b (i.e., command support data for an operation code and service action).
The device server shall process the MODE field in the READ BUFFER command, if supported, and the MODE
field in the WRITE BUFFER command as specifying service actions.
The values reported in the command timeouts descriptors for each command shall be based on at least a
1 MiB transfer length.
H.3.3.4 REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS command
The device server shall support the following bit in the CDB:
a)
the REPD bit set to one (i.e., return extended parameter data is supported).
H.3.3.5 REQUEST SENSE command
The device server shall support the following bit in the CDB:
a)
the DESC bit set to zero; (i.e., fixed format sense data is supported).
If the device server supports LBAs greater than FFFF_FFFFh, then the device server shall support the
following bit in the CDB:
a)
the DESC bit set to one (i.e., descriptor format sense data is supported).
H.3.3.6 SYNCHRONIZE CACHE (16) command
The device server shall support the following bits or fields in the CDB:
a)
the IMMED bit set to one.
If the Extended INQUIRY Data VPD page (see SPC-6) indicates that the device server does not contain
volatile cache (i.e., the V_SUP bit is set to zero) and indicates that the device server does not contain
non-volatile cache (i.e., the NV_SUP bit is set to zero), then the device server may complete the command
without making any changes (i.e., implement the command as a no operation command).
H.3.3.7 WRITE SAME (16) command
If the device server supports the UNMAP bit in the CDB set to one, then the device server shall support the
NDOB bit set to one.


H.3.4 SBC Base 2016 feature set mode pages
H.3.4.1 Mode parameter block descriptor
If the device supports LBAs greater than FFFF_FFFFh, then the device server shall support the long LBA
mode parameter block descriptor (see 6.5.2.3).
The device server is not required to support changing its capacity by changing the number of logical blocks
field using the MODE SELECT command.
H.3.4.2 Caching mode page
If the Extended INQUIRY Data VPD page (see SPC-6) indicates that the device server contains volatile cache
(i.e., the V_SUP bit is set to one), then the device server shall support:
a)
the WCE bit set to zero; and
b)
the WCE bit set to one.
H.3.4.3 Control mode page
The device server shall support the following bits or fields:
a)
the D_SENSE bit set to one (i.e., descriptor format sense data is enabled) if the device server supports
LBAs greater than FFFF_FFFFh;
b)
the QUEUE ALGORITHM MODIFIER field set to 1h (i.e., unrestricted reordering allowed); and
c)
the QERR field set to 00b (i.e., CHECK CONDITION on one command does not affect others).
H.3.4.4 Informational Exceptions Control mode page
The device server shall support the following bits or fields:
a)
the MRIE field set to one or more values including 0h (i.e., no reporting);
b)
the EWASC bit set to zero;
c)
the EWASC bit set to one;
d)
the DEXCEPT bit set to zero; and
e)
the DEXCEPT bit set to one.
Devices that implement SAT-4 shall support the MRIE field set to 6h (i.e., only report on request).
Devices that do not implement SAT-4 shall support the MRIE field set to:
a)
0h (i.e., no reporting);
b)
2h (i.e., establish unit attention condition);
c)
4h (i.e., unconditionally generate recovered error); and
d)
6h (i.e., only report on request).
H.3.4.5 Read-Write Error Recovery mode page
The device server shall support the following bit:
a)
the AWRE bit set to one (i.e., automatic write reallocation enabled is supported).
Devices that do not implement SAT-4 shall support the following bit:
a)
the ARRE bit set to one (i.e., automatic read reallocation enabled is supported).
H.3.5 SBC Base 2016 feature set VPD pages
H.3.5.1 Block Device Characteristics VPD page
The device server shall report the MEDIUM ROTATION RATE field set to a non-zero value.


H.3.5.2 Block Limits VPD page
The device server shall report the following values:
a)
the MAXIMUM TRANSFER LENGTH field set to a value that represents at least 1 MiB (e.g., for a logical
block size of 512 bytes, at least 00000800h);
b)
the MAXIMUM WRITE SAME LENGTH field set to a value that represents at least 1 MiB (e.g., for a logical
block size of 512 bytes, at least 00008000h;
c)
the OPTIMAL TRANSFER LENGTH GRANULARITY field set to the minimum number of logical blocks that the
device server prefers for random I/O; and
d)
the OPTIMAL TRANSFER LENGTH field set to the maximum number of logical blocks that the device
server prefers for streaming I/O.
The device server is not required to support:
a)
the WSNZ bit set to zero (i.e., the WRITE SAME command NUMBER OF LOGICAL BLOCKS field set to zero
is supported).
H.3.5.3 Extended INQUIRY Data VPD page
If the device server implements a non-volatile writeback cache that may become volatile (see 4.15.10), then
the device server shall report the NV_SUP bit set to one.
If the device server implements a volatile writeback cache, then the device server shall report the V_SUP bit set
to one.
The device server is not required to support:
a)
the HEADSUP bit set to one (i.e., HEAD OF QUEUE task attribute is supported); and
b)
the ORDSUP bit set to one (i.e., ORDERED task attribute is supported).
H.4 Basic Provisioning 2016 feature set
H.4.1 Basic Provisioning 2016 feature set overview
The Basic Provisioning 2016 feature set includes features related to logical block provisioning.
Logical units that support the Basic Provisioning 2016 feature set:
a)
shall support either the SBC Base 2016 feature set (see clause H.3) or the SBC Base 2010 feature
set (see clause H.2); and
b)
should support the SBC Base 2016 feature set.
Table H.8 lists the Basic Provisioning 2016 feature set commands.
Table H.8 — Commands mandatory for the Basic Provisioning 2016 feature set
Command
Additional requirements
reference
Reference
GET LBA STATUS (16)
H.4.3.1
5.6
READ CAPACITY (16)  a
H.4.3.2
5.21
UNMAP
n/a
5.35
WRITE SAME (16)  a
H.4.3.3
5.53
a This command is required by the Base 2016 feature set (see clause H.3) and the
Base 2010 feature set (see clause H.2). This feature set adds additional
requirements.


Table H.9 lists the Basic Provisioning 2016 feature set VPD pages.
H.4.2 SBC Basic Provisioning 2016 feature set model additional requirements
The device server shall support logical block provisioning management (see 4.7.3.1).
If the logical unit is thin provisioned (see 4.7.3.3), then the device server shall support:
a)
at least two logical block provisioning thresholds (see 4.7.3.7); and
b)
the logical block provisioning log page (see 6.4.5).
H.4.3 Basic Provisioning 2016 feature set commands
H.4.3.1 GET LBA STATUS (16) command
The device server shall return only as many LBA status descriptors as it is able to return within the nominal
command processing timeout reported in the command timeouts descriptor in the REPORT SUPPORTED
OPERATION CODES command (see SPC-6).
H.4.3.2 READ CAPACITY (16) command
The device server shall report the LBPME bit set to one (i.e., logical block provisioning management is
implemented) in the READ CAPACITY (16) parameter data.
H.4.3.3 WRITE SAME (16) command
The device server shall support the following bits in the CDB:
a)
the UNMAP bit set to one; and
b)
the NDOB bit set to one.
H.4.4 SBC Basic Provisioning 2016 feature set VPD pages
H.4.4.1 Block Limits VPD page
The device server shall report the following values:
a)
the MAXIMUM UNMAP LBA COUNT field set to at least the value of the MAXIMUM WRITE SAME LENGTH field;
b)
the MAXIMUM UNMAP BLOCK DESCRIPTOR COUNT field set to at least 0000_0040h (i.e., 64 descriptors);
and
c)
if the logical unit has an optimal unmap granularity, then the OPTIMAL UNMAP GRANULARITY field set to a
non-zero value.
H.4.4.2 Logical Block Provisioning VPD page
The device server shall report the following values:
a)
the LBPU bit set to one (i.e., UNMAP command supported);
b)
the LBPWS bit set to one (i.e., WRITE SAME (16) command UNMAP bit is supported); and
c)
the PROVISIONING TYPE field set to 001b (i.e., resource provisioned) or 010b (i.e., thin provisioned).
The device server shall not report the LBPRZ field set to 000b (i.e., unmapped LBA data is vendor specific).
Table H.9 — VPD pages mandatory for the Basic Provisioning 2016 feature set
VPD page
Additional requirements
reference
Reference
Block Limits
H.4.4.1
6.6.4
Logical Block Provisioning
H.4.4.2
6.6.7


The device server is not required to report the ANC_SUP bit set to one.
H.5 Drive Maintenance 2016 feature set
H.5.1 Drive Maintenance 2016 feature set overview
The Drive Maintenance 2016 feature set includes features intended for use by maintenance application
clients.
Logical units that support the Drive Maintenance 2016 feature set:
a)
shall support either the SBC Base 2016 feature set (see clause H.3) or the SBC Base 2010 feature
set (see clause H.2); and
b)
should support the SBC Base 2016 feature set.
Table H.10 lists the Drive Maintenance 2016 feature set commands.
Table H.11 lists the Drive Maintenance 2016 feature set VPD pages.
Table H.10 — Commands mandatory for the Drive Maintenance 2016 feature set
Command
Additional requirements
reference
Reference
FORMAT UNIT
n/a
5.4
LOG SELECT
n/a
SPC-6
LOG SENSE
n/a
SPC-6
READ BUFFER (10)
H.5.2.1
SPC-6
READ DEFECT DATA (12)
H.5.2.2
5.23
REASIGN BLOCKS
H.5.2.3
5.24
SANITIZE
H.5.2.4
5.30
SEND DIAGNOSTICS
H.5.2.5
SPC-6
RECEIVE DIAGNOSTIC RESULTS
n/a
SPC-6
WRITE BUFFER
H.5.2.6
SPC-6
WRITE LONG (16)
n/a
5.51
Table H.11 — VPD pages mandatory for the Drive Maintenance 2016 feature set
VPD page
Additional requirements
reference
Reference
Extended INQUIRY Data
n/a
SPC-6
Block Device Characteristics
H.5.3.1
6.6.2
Power Consumption
n/a
SPC-6


Table H.12 lists the Drive Maintenance 2016 feature set log pages.
H.5.2 Drive Maintenance 2016 feature set commands
H.5.2.1 READ BUFFER (10) command
The device server shall support the following modes:
a)
03h (i.e., descriptor); and
b)
1Ch (i.e., error history).
H.5.2.2 READ DEFECT DATA (12) command
The device server shall support the same address descriptor format types that it supports in the FORMAT
UNIT command.
H.5.2.3 REASSIGN BLOCKS command
If the device server supports LBAs greater than FFFF_FFFFh, then the device server shall support the
following bits in the CDB:
a)
the LONGLBA bit set to one; and
b)
the LONGLIST bit set to one.
H.5.2.4 SANITIZE command
The device server shall support the following bits in the CDB:
a)
the IMMED bit set to one; and
b)
the AUSE bit set to one.
The logical unit shall support the following service actions:
a)
EXIT FAILURE MODE.
If the logical unit is a memory media device (e.g., a solid state drive), then the logical unit shall:
a)
support the BLOCK ERASE service action; and
b)
unmap the entire capacity upon completion.
Table H.12 — Log pages mandatory for the Drive Maintenance 2016 feature set
Log page
Additional requirements
reference
Reference
Supported Log Pages n/a SPC-6
n/a
SPC-6
Supported Log Pages and Subpages
n/a
SPC-6
Background Scan
H.5.4.1
6.4.2.1
Informational Exceptions
n/a
SPC-6
Non-Medium Error
n/a
SPC-6
Non-volatile Cache
n/a
6.4.7
Read Error Counters
H.5.4.2
SPC-6
Self-Test Results
n/a
SPC-6
Solid State Media
n/a
6.4.9
Start-Stop Cycle Counter
H.5.4.3
SPC-6
Temperature
H.5.4.4
SPC-6


If the logical unit is a rotating media device (e.g., a hard disk drive), then the logical unit shall support the
OVERWRITE service action with:
a)
the INVERT bit set to zero;
b)
the TEST field set to 00b;
c)
the OVERWRITE COUNT field set to 01h;
d)
the INITIALIZATION PATTERN LENGTH field set to 0004h; and
e)
the INITIALIZATION PATTERN field set to 00000000h.
H.5.2.5 SEND DIAGNOSTIC command
The logical unit shall support a default self-test.
If the logical unit supports an extended self-test, then the device server shall support:
a)
the EXTENDED SELF-TEST COMPLETION TIME field in the Control mode page; and
b)
the EXTENDED SELF-TEST COMPLETION MINUTES field in the Extended INQUIRY Data VPD page.
The device server is not required to support:
a)
the Translate Address Output diagnostic page; or
b)
the Translate Address Input diagnostic page.
H.5.2.6 WRITE BUFFER command
The logical unit shall support the following modes:
a)
0Dh (i.e., download microcode with offsets, select activation events, save, and defer activate); and
b)
0Fh (i.e., activate deferred microcode).
The device server is not required to support the following modes:
a)
00h (i.e., combined header and data);
b)
02h (i.e., data);
c)
0Ah (i.e., write data to echo buffer);
d)
1Ah (i.e., enable expander communications protocol and echo buffer); and
e)
1Bh (i.e., disable expander communications protocol).
H.5.3 Drive Maintenance 2016 feature set VPD pages
H.5.3.1 Block Device characteristics VPD page
The device server shall report the following values:
a)
the RBWZ bit set to one (i.e., REASSIGN BLOCKS writes zeros if the logical block data is not
recovered).
H.5.4 Drive Maintenance 2016 feature set log pages
H.5.4.1 Background Scan Results log page
The device server shall report the following log parameters:
a)
Background Scan Status, as required by 6.4.2.1; and
b)
at least 256 Background Scan Results log parameters.
H.5.4.2 Read Error Counters log page
The device server shall report the following log parameters:
a)
0006h (i.e., total uncorrected errors).


H.5.4.3 Start-Stop Cycle Counter log page
The device server shall report the following log parameters:
a)
Date of Manufacture; and
b)
Accounting Date.
H.5.4.4 Temperature log page
The device server shall report the following log parameters:
a)
Temperature, as required by SPC-6; and
b)
Reference Temperature.


Annex I
(informative)
Using storage element depopulation
Storage element depopulation may be used when a logical unit is suboptimal.
A device server indicates a suboptimal condition of a storage element to an application client by establishing
an informational exception condition with the additional sense code set to WARNING - PHYSICAL ELEMENT
STATUS CHANGE (see 4.36.2).
The application client may determine which storage elements have a physical element health (see 5.8.2.2)
that is outside the manufacturer’s specification limit using the GET PHYSICAL ELEMENT STATUS command
(see 5.8).
If the application client determines that a storage element that is outside manufacturer’s specification limit and
should be depopulated, then the application client may send a REMOVE ELEMENT AND TRUNCATE
command that specifies:
a)
the element identifier of the storage element to be depopulated; and
b)
the requested capacity, if any.
The REMOVE ELEMENT AND TRUNCATE command requests storage element depopulation (see 4.36.3). If
the application client requires logical block data to be initialized after a storage element depopulation has
completed, then the application client should initialize all logical block data.
To determine when the operations described in 4.36.3 have completed, the application client may use a
REQUEST SENSE command to retrieve pollable sense data (see SPC-6). To determine which storage
element has been depopulated, the application client may use a GET PHYSICAL ELEMENT STATUS
command.
A sequence of REMOVE ELEMENT AND TRUNCATE commands may be used to depopulate multiple
storage elements. A device server may have a limit on the number of storage elements that may be
depopulated. If the device server is requested to depopulate a storage element in excess of this limit, then the
device server may terminate that request (see 5.26).
Storage elements may transition outside manufacturer's specification limit during the time other storage
elements are being depopulated. If a storage element transitions outside manufacturer's specification limit
during processing of a storage element depopulation for a different storage element, the device server notifies
the application client of that storage element status change as described in 4.36.2.
The RESTORE ELEMENTS AND REBUILD command (see 5.29) restores storage elements that had
previously been depopulated. The device server indicates which storage elements, if any, are able to be
affected by a RESTORE ELEMENTS AND REBUILD command using the RALWD bit (see 5.8.2.2) in the GET
PHYSICAL ELEMENT STATUS parameter data.
The RESTORE ELEMENTS AND REBUILD command requests storage element restoration (see 4.36.4). A
successful storage element restoration restores at least one storage element and may result in an increase in
the number of LBA resources. The storage element restoration is not required to preserve logical block data.
After a storage element restoration has completed, the host may initialize all logical block data.
To determine when the operations described in 4.36.4 have completed, the application client may use a
REQUEST SENSE command to retrieve pollable sense data (see SPC-6). To determine which storage
elements have been restored, the application client may use a GET PHYSICAL ELEMENT STATUS
command.


Annex J
(informative)
Rebuild assist using the GET LBA STATUS command
J.1 Overview
This annex describes an example of an application client rebuilding data from a SCSI device with a physical
element failure. This examples uses the following commands:
a)
the GET PHYSICAL ELEMENT STATUS command (see 5.8);
b)
the GET LBA STATUS (32) command (see 5.7); and
c)
write commands.
J.2 Discovery process
This example show how an application client is able to discover what LBAs are affected on a block storage
device with a capacity of 2_147_483_648 bytes, a logical block length of 4_096 bytes, and the physical
element identified by identifier 7 with a health status of 65. The discovery process for the LBAs that are
affected by the failure of a this physical element consists of following sequence. The application client issues
a GET PHYSICAL ELEMENT STATUS command with:
a)
the STARTING ELEMENT field set to 0000h;
b)
the FILTER field set to 01b (i.e., physical elements with a health outside manufacturers specification
limit or depopulated); and
c)
the REPORT TYPE field set to 1h (i.e., storage elements).
In this example the GET PHYSICAL ELEMENT STATUS command returns one descriptor in the parameter
data. That descriptor contains:
a)
an element identifier of 0007h;
b)
a physical element type of 01h; and
c)
a physical element health of 65h.
The application client then issues a GET LBA STATUS (32) command with:
a)
the REPORT TYPE field set to 00h (i.e., return descriptors for all LBAs);
b)
the STARTING LOGICAL BLOCK ADDRESS field set to 0000_0000h;
c)
the SCAN LENGTH field set to FFFFh; and
d)
the ELEMENT IDENTIFIER field set to 0007h.
Any LBAs from 0000_0000h to 0000_FFFFh that are mapped to physical element 0007h are included in the
returned parameter data.
The application client then issues a GET LBA STATUS (32) command with:
a)
the REPORT TYPE field set to 00h;
b)
the STARTING LOGICAL BLOCK ADDRESS field set to 0001_0000h;
c)
the SCAN LENGTH field set to FFFFh; and
d)
the ELEMENT IDENTIFIER field set to 0007h.
Any LBAs from 0001_0000h to 0001_FFFFh that are mapped to physical element 0007h are included in the
returned parameter data.
The application client continues issuing GET LBA STATUS (32) commands incrementing the STARTING
LOGICAL BLOCK ADDRESS field by 1_0000h for each command until it issues a GET LBA STATUS (32)
command with a STARTING LOGICAL BLOCK ADDRESS field set to 0079_0000h.
