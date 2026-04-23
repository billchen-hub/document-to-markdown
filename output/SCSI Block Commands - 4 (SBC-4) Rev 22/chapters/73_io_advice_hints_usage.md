# IO advice hints usage

Annex G
(informative)
IO advice hints usage
G.1 Overview
This annex describes how application clients and device servers may use IO advice hints and their associated
logical block markup descriptors to provide information to a storage device to enhance access to data.
G.2 IO Advice Hints Grouping mode page
The IO Advice Hints Grouping mode page (see 6.5.7) contains the definitions of the IO advice hints (see
4.22.2) that are associated with each group number.
A device server may implement pre-defined IO advice hints that are not changeable and indicate this by
making one or more IO advice hints group descriptors in the mode page not changeable.
The application client may use the MODE SENSE command to retrieve IO advice hints group descriptors to
determine the IO advice hints that are available, and determine which IO advice hints are associated with
each group number.
If any IO advice hints group descriptors in the mode page are changeable, the application client may use a
MODE SELECT command to associate IO group numbers with IO advice hints that meet the application client
needs.
A device server may implement any combination of changeable IO advice hints group descriptors or
predefined IO advice hints group descriptors.
G.3 Issuing I/O commands with IO advice hints
G.3.1 Group numbers and I/O commands
An application client:
1)
determines the IO advice hints group descriptor appropriate for each particular type of command
using the process described in clause G.2;
2)
determines the value to specify in the GROUP NUMBER field of each command as described in
4.22.2; and
places that value into the GROUP NUMBER field of the CDB.If cache segmentation (see 4.15.2) is enabled (see
6.5.7), then the use of different group numbers by components within the application client (e.g., file system,
virtual memory swapping/paging, payroll application) allows the device server to associate an IO command
and the associated cached data with other IO commands and other cached data from that same component.
G.3.2 Possible constraints on IO advice hints
There is no method to report how an IO advice hints has been processed by the device server. The
implications of this model include the ability of the device server to ignore any, or even all, IO advice hints it
receives.
A device server may constrain the complexity of its IO advice hints implementation by ignoring one or more of
the values in the logical block markup descriptor (see 6.8) (e.g., to ignore the READ SEQUENTIALITY field, and
the READ/WRITE FREQUENCY field).


If the complexity of specifying values or locating values in the IO Advice Hints Grouping mode page (see
6.5.7) is a concern, the device server may implement the page, but indicate that one or more IO advice hints
groups descriptors (see 6.5.7) are not changeable (see SPC-6). A device server that does this should:
a)
define the unchangeable IO advice hints for groups descriptors in the lowest group numbers
supported for usage by IO advice hints; and
b)
allow at least four IO advice hints group descriptors to be changeable.
G.4 Logical block markup descriptor usage examples
G.4.1 Example usage in tiered storage device implementations
Products (e.g., SCSI target devices and ATA devices) may use the contents of an logical block markup
descriptor in ways that are not related to the contents of one field in a logical block markup descriptor in any
way that is traceable to the way the field is defined. As an example, suppose a product contains the following
storage tiers:
a)
volatile cache;
b)
non-volatile cache;
c)
solid state device storage; and
d)
magnetic media storage.
Table G.1 shows examples of how such a tiered product may interpret combinations of values in fields in an
access patterns logical block markup descriptor (see 6.8.3.1).
G.4.2 Example logical block markup descriptor values for software that sends read commands and
write commands
Table G.2 shows example mappings to access patterns logical block markup descriptors (see 6.8.3.1) from:
a)
file types in common usage; and
b)
published file system and operating system specifications for usage characteristics.
Table G.1 — Tiered product access patterns logical block markup descriptor examples
Field
Code
Field
Code
Field
Code
Data that should not be written to the solid state device storage
READ/WRITE FREQUENCY
10b
WRITE SEQUENTIALITY
see  a
OSI PROXIMITY
see  a
OVERALL FREQUENCY
10b
READ SEQUENTIALITY
see  a
ACDLU
see  a
SUBSEQUENT I/O
see  a
IO CLASS
see  a
Data that should be written to non-volatile media and not retained in cache
READ/WRITE FREQUENCY
10b
WRITE SEQUENTIALITY
see  a
OSI PROXIMITY
see  a
OVERALL FREQUENCY
01b
READ SEQUENTIALITY
see  a
ACDLU
see  a
SUBSEQUENT I/O
see  a
IO CLASS
see  a
a The contents of this field do not contribute to this example case.


Table G.2 — Sending device access patterns logical block markup descriptor examples  (part 1 of 2)
Field
Code
Field
Code
Field
Code
LBMd value: 90h, A5h, 52h, 00h
Data type: swap/page file
Applicable published specifications
Microsoft®: FILE_TYPE_NOTIFICATION_GUID_PAGE_FILE
Linux: None known
READ/WRITE FREQUENCY
10b
WRITE SEQUENTIALITY
01b
OSI PROXIMITY
10b
OVERALL FREQUENCY
10b
READ SEQUENTIALITY
01b
ACDLU
1b
SUBSEQUENT I/O
00b
IO CLASS
5h
RLBSR
01b
LBMd value: 03h, 00h, 56h, 00h
Data type: hibernate file
Applicable published specifications
Microsoft®:
FILE_TYPE_NOTIFICATION_GUID_HIBERNATION_FILE
Linux: None known
READ/WRITE FREQUENCY
00b
WRITE SEQUENTIALITY
00b
OSI PROXIMITY
10b
OVERALL FREQUENCY
00b
READ SEQUENTIALITY
00b
ACDLU
0b
SUBSEQUENT I/O
01b
IO CLASS
5h
RLBSR
11b
LBMd value: 00h, 55h, 06h, 00h
Data type: system initialization
(e.g., registry)
Applicable published specifications
Microsoft®: None known
Linux: None known
READ/WRITE FREQUENCY
01b
WRITE SEQUENTIALITY
01b
OSI PROXIMITY
10b
OVERALL FREQUENCY
01b
READ SEQUENTIALITY
01b
ACDLU
0b
SUBSEQUENT I/O
01b
IO CLASS
0h
RLBSR
00b
LBMd value: 01h, 05h, 14h, 00h
Data type: general file system
metadata  c
(e.g., directory files)
Applicable published specifications
Microsoft®: None known
Linux: None known
READ/WRITE FREQUENCY
00b
WRITE SEQUENTIALITY
01b
OSI PROXIMITY
00b
OVERALL FREQUENCY
00b
READ SEQUENTIALITY
01b
ACDLU
0b
SUBSEQUENT I/O
01b
IO CLASS
1h
RLBSR
01b
LBMd value: 00h, 05h, x0h
a,00h
Data type: random access
Applicable published specifications
Microsoft®: None known
Linux: FADV_RANDOM
Key:
LBMd = logical block markup descriptor
Note 1 - Microsoft information obtained from
http://msdn.microsoft.com/en-us/library/windows/desktop/hh404249%28v=vs.85%29.aspx.
Note 2 - Linux information obtained from http://linux.die.net/man/2/fadvise.
a Where x represents the io_class value.
b The application client should select the io_class value (e.g., 4h or 5h) appropriate to the size of the
object.
c File system metadata accessed during normal operation of the file system (e.g. security information,
time stamps, directories).
d File system metadata accessed during mounting of the file system (e.g., superblock, bitmaps,
mapping tables).


READ/WRITE FREQUENCY
00b
WRITE SEQUENTIALITY
01b
OSI PROXIMITY
00b
OVERALL FREQUENCY
00b
READ SEQUENTIALITY
01b
ACDLU
0b
SUBSEQUENT I/O
00b
IO CLASS
see  b
RLBSR
00b
LBMd value: 00h, 0Ah, x0h  a,
00h
Data type: sequential access
Applicable published specifications
Microsoft®: None known
Linux: FADV_SEQUENTIAL
READ/WRITE FREQUENCY
00b
WRITE SEQUENTIALITY
10b
OSI PROXIMITY
00b
OVERALL FREQUENCY
00b
READ SEQUENTIALITY
10b
ACDLU
0b
SUBSEQUENT I/O
00b
IO CLASS
see  b
RLBSR
00b
LBMd value: 30h,AAh,1Ah,00h
Data type: circular log that
contains metadata
Applicable published specifications
Microsoft®: None known
Linux: None known
READ/WRITE FREQUENCY
10b
WRITE SEQUENTIALITY
10b
OSI PROXIMITY
10b
OVERALL FREQUENCY
10b
READ SEQUENTIALITY
10b
ACDLU
0b
SUBSEQUENT I/O
10b
IO CLASS
1h
RLBSR
11b
LBMd value: 30h,A5h,1Ah,00h
Data type: critical filesystem
metadata  d
Applicable published specifications
Microsoft®: None known
Linux: None known
READ/WRITE FREQUENCY
10b
WRITE SEQUENTIALITY
01b
OSI PROXIMITY
10b
OVERALL FREQUENCY
10b
READ SEQUENTIALITY
01b
ACDLU
0b
SUBSEQUENT I/O
10b
IO CLASS
1h
RLBSR
11b
Table G.2 — Sending device access patterns logical block markup descriptor examples  (part 2 of 2)
Field
Code
Field
Code
Field
Code
Key:
LBMd = logical block markup descriptor
Note 1 - Microsoft information obtained from
http://msdn.microsoft.com/en-us/library/windows/desktop/hh404249%28v=vs.85%29.aspx.
Note 2 - Linux information obtained from http://linux.die.net/man/2/fadvise.
a Where x represents the io_class value.
b The application client should select the io_class value (e.g., 4h or 5h) appropriate to the size of the
object.
c File system metadata accessed during normal operation of the file system (e.g. security information,
time stamps, directories).
d File system metadata accessed during mounting of the file system (e.g., superblock, bitmaps,
mapping tables).


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
