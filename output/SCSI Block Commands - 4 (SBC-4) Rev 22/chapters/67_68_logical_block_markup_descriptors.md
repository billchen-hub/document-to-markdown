# 6.8 Logical block markup descriptors

A type 2 protection supported (T2PS) bit set to one indicates that type 2 protection is supported for the
indicated logical block length. A T2PS bit set to zero indicates that type 2 protection is not supported for the
indicated logical block length.
A type 1 protection supported (T1PS) bit set to one indicates that type 1 protection is supported for the
indicated logical block length. A T1PS bit set to zero indicates that type 1 protection is not supported for the
indicated logical block length.
A type 0 protection supported (T0PS) bit set to one indicates that type 0 protection is supported for the
indicated logical block length. A T0PS bit set to zero indicates that type 0 protection is not supported for the
indicated logical block length.
6.7 Copy manager parameters
The copy manager parameters are device type specific data for ROD tokens (see SPC-6) created by a copy
manager for a direct access block device (see 4.28) and are shown in table 287.
The LOGICAL BLOCK LENGTH IN BYTES field, the P_TYPE field, the PROT_EN bit, the P_I_EXPONENT field, the
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field, the LBPME bit, the LBPRZ bit, and the LOWEST ALIGNED
LOGICAL BLOCK ADDRESS field are defined in 5.21.2.
6.8 Logical block markup descriptors
6.8.1 lLogical block markup descriptor overview
A logical block markup descriptor communicates information about anticipated usage of a logical block or
range of logical blocks to the device server that manages access to that logical block. The requirements, if
any, placed on a device server that receives a logical block markup descriptor are associated with the
command that causes the device server to receive one or more logical block markup descriptors. Logical
block markup descriptors are used in the IO Advice Hints Grouping mode page (see 6.5.7). Logical block
markup descriptor formats and the meanings of logical block markup descriptor fields are described in 6.8.
Table 287 — ROD token device type specific data
Bit
Byte
(MSB)
LOGICAL BLOCK LENGTH IN BYTES
•••
(LSB)
Reserved
P_TYPE
PROT_EN
P_I_EXPONENT
LOGICAL BLOCKS PER PHYSICAL BLOCK
EXPONENT
LBPME
LBPRZ
(MSB)
LOWEST ALIGNED LOGICAL BLOCK ADDRESS
(LSB)
Reserved
•••


6.8.2 Logical block markup descriptor formats and types
The format of an logical block markup descriptor is shown in table 288.
The LBM DESCRIPTOR TYPE field is shown in table 289.
6.8.3 Access patterns logical block markup descriptors
6.8.3.1 Access patterns logical block markup descriptor format
The access patterns logical block markup descriptor format is shown in table 290.
The LBM DESCRIPTOR TYPE field is defined in 6.8.2 and shall be set as shown in table 290 for the access
patterns logical block markup descriptor format.
An ACDLU bit set to one specified that any logical blocks associated with this logical block markup descriptor
have a high probability of being accessed during time intervals in which most logical blocks are not being
accessed by any read commands or write commands. If the ACDLU bit is set to zero, then any logical blocks
associated with this logical block markup descriptor have no utilization related probability of being read or
written.
Table 288 — Logical block markup descriptor format
Bit
Byte
Logical block markup descriptor type specific
data
LBM DESCRIPTOR TYPE
logical block markup descriptor type specific data
•••
n
Table 289 — LBM DESCRIPTOR TYPE field
Code
Logical block markup descriptor type
Reference
0h
Access patterns
6.8.3
all others
Reserved
Table 290 — Access patterns logical block markup descriptor format
Bit
Byte
ACDLU
Reserved
RLBSR
LBM DESCRIPTOR TYPE (0h)
OVERALL FREQUENCY
READ/WRITE FREQUENCY
WRITE SEQUENTIALITY
READ SEQUENTIALITY
IO CLASS
SUBSEQUENT I/O
OSI PROXIMITY
Reserved


The RLBSR field (see table 291) specifies information about the relations of the logical blocks associated with a
command that references this logical block markup descriptor. The device server may use this information to
optimize resource management (e.g. reduce advanced background operations).
The OVERALL FREQUENCY field (see table 292) specifies the probability that a logical block in the range
associated with this logical block markup descriptor is likely to be accessed more frequently than other logical
blocks stored on the same medium.
The READ/WRITE FREQUENCY field (see table 293) specifies whether read operations or write operations are
more probable to a logical block in the range associated with this logical block markup descriptor.
Table 291 — RLBSR field
Code
Description
00b
No information is provided about the relationship among the
logical blocks associated with the command that references
this logical block markup descriptor or the probability of
subsequent reads to these logical blocks.
01b
Logical blocks associated with the command that references
this logical block markup descriptor are related to each other
(e.g. are a file or part of the same application client data
structure). No information is provided about the probability of
subsequent reads to these logical blocks.
10b
Reserved
11b
Logical blocks associated with the command that references
this logical block markup descriptor are related to each other
and a read to any logical block in the group of related logical
blocks increases the probability of subsequent reads to other
logical blocks in that group of related logical blocks (e.g., a
device managed zoned block device may benefit from storing
these blocks in the same zone).
Table 292 — OVERALL FREQUENCY field
Code
Description
00b
Overall access frequency is unknown or equally probable.
01b
Overall accesses are less frequent than average.
10b
Overall accesses are more frequent than average.
11b
Reserved
Table 293 — READ/WRITE FREQUENCY field
Code
Description
00b
Read operation frequency versus write operation frequency is
unknown or equally probable.
01b
Read operations are more probable.
10b
Write operations are more probable.
11b
Reserved


Using the values shown in table 294:
a)
the WRITE SEQUENTIALITY field specifies whether sequential write operations or random write opera-
tions are more probable to a logical block in the range associated with this logical block markup
descriptor; and
b)
the READ SEQUENTIALITY field specifies whether sequential read operations or random read operations
are more probable to a logical block in the range associated with this logical block markup descriptor.
The IO CLASS field (see table 295) specifies the classification of user data that is associated with this logical
block markup descriptor.
The SUBSEQUENT I/O field (see table 296) specifies the probability that the application client may be delaying
the sending of additional read commands or write commands to the device server until the completion of a
read command or a write command for a logical block associated with this logical block markup descriptor
(e.g., commands are being delayed by the application client's file system until the completion of write
Table 294 — WRITE SEQUENTIALITY field and READ SEQUENTIALITY field
Code
Description
00b
Access sequentiality is unknown or equally probable.
01b
Random operations are more probable.
10b
Sequential operations are more probable.
11b
Reserved
Table 295 — IO CLASS field
Code
Description
0h
None specified
1h
IOs that specify this logical block markup descriptor are related to user data that describes
other user data (e.g. file system meta-data). a
4h
IOs that specify this logical block markup descriptor are related to a small collection of user
data where small is defined by the application client. a
5h
IOs that specify this logical block markup descriptor are related to a large collection of user
data where large is defined by the application client. a
all others
Reserved
a See Differentiated Storage Services


commands to logical blocks in a file system allocation bit map that are associated with this logical block
markup descriptor).
The OSI PROXIMITY field (see table 297) specifies the probability that any logical block associated with this
logical block markup descriptor is likely to be accessed during an operating system or file system initialization
operation (e.g., a boot block).
Methods to determine whether an operating system or file system initialization operation is in progress are
outside the scope of this standard.
EXAMPLE - Possible sources of knowledge about when an operating system initialization operation is occurring depend
on the system in which the device server is participating and include prior knowledge of which LBA accesses are
associated with an operating system initialization or detection of a power on event.
6.8.3.2 Access patterns logical block markup descriptor usage considerations
Device servers may ignore all or part of the information contained in an access patterns logical block markup
descriptor.
EXAMPLE 1 - A device server that processes only the OVERALL FREQUENCY field.
EXAMPLE 2 - A device server that processes all logical block markup descriptor fields except the WRITE SEQUENTI-
ALITY field and the READ SEQUENTIALITY field.
EXAMPLE 3 - In a product with a focus on sequential writes (e.g., a disk drive based on shingled magnetic recording), the
device server ignores all values in all fields except a WRITE SEQUENTIALITY field that is set to 10b.
Although Annex G shows some possible combinations of the fields in an access patterns logical block markup
descriptor, this standard places no requirements on how the device server interprets the interactions, if any,
between the fields in an access patterns logical block markup descriptor.
Table 296 — SUBSEQUENT I/O field
Code
Description
00b
The probability is unknown whether the application client is delaying the
sending of commands to the device server until completion of a read command
or a write command for a logical block associated with this logical block markup
descriptor.
01b
The probability is low that the application client is delaying the sending of
commands to the device server until completion of a read command or a write
command for a logical block associated with this logical block markup
descriptor.
10b
The probability is high that the application client is delaying the sending of
commands to the device server until completion of a read command or a write
command for a logical block associated with this logical block markup
descriptor.
11b
Reserved
Table 297 — OSI PROXIMITY field
Code
Description
00b
Access during initialization probability is unknown or equally probable.
01b
Accesses are not probable during an initialization process.
10b
Accesses are probable during an initialization process.
11b
Reserved


Annex A
(informative)
Numeric order codes
A.1 Variable length CDBs
 Commands that use operation code 7Fh in table 34 use the variable length command format defined in
SPC-6 and are differentiated by service action codes as described in table A.1.
Table A.1 — Variable length command service action code assignments
Operation code/service
action code
Description
7Fh/0000h
Reserved
7Fh/0001h
Reserved
7Fh/0002h
Reserved
7Fh/0003h
Obsolete (XDREAD (32))
7Fh/0004h
Obsolete (XDWRITE (32))
7Fh/0005h
Reserved
7Fh/0006h
Obsolete (XPWRITE (32))
7Fh/0007h
Obsolete (XDWRITEREAD (32))
7Fh/0008h
Reserved
7Fh/0009h
READ (32)
7Fh/000Ah
VERIFY (32)
7Fh/000Bh
WRITE (32)
7Fh/000Ch
WRITE AND VERIFY (32)
7Fh/000Dh
WRITE SAME (32)
7Fh/000Eh
ORWRITE (32)
7Fh/000Fh
WRITE ATOMIC (32)
7Fh/0010h
WRITE STREAM (32)
7Fh/0011h
WRITE SCATTERED (32)
7F/0012h
GET LBA STATUS (32)
7Fh/0013h to 07FFh
Reserved
7Fh/0800h to FFFFh
See SPC-6
