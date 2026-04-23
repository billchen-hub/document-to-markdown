# 4.6 Physical blocks

Each logical block is referenced by a unique LBA, which is either four bytes in length or eight bytes in length.
The LBAs on a logical unit shall begin with zero and shall be contiguous up to the last LBA on the logical unit.
The last LBA is [n-1], where [n] is the number of logical blocks accessible by an application client.
For this standard, the RETURNED LOGICAL BLOCK ADDRESS field in the READ CAPACITY (10) parameter data
(see 5.20.2) and the READ CAPACITY (16) parameter data (see 5.21.2) indicates the value of [n-1].
Other command standards (e.g., ZBC-2) may define the contents of the RETURNED LOGICAL BLOCK ADDRESS
field to be less than [n-1].
Each LBA has a logical block provisioning state (see 4.7) of mapped, deallocated, or anchored.
Some commands support only four-byte LOGICAL BLOCK ADDRESS fields (e.g., READ (10), and WRITE (10)).
If the capacity of the logical unit exceeds that accessible with four-byte LBAs, then the device server returns
the RETURNED LOGICAL BLOCK ADDRESS field set to FFFF_FFFFh in the READ CAPACITY (10) parameter data,
indicating that an application client should:
a)
enable descriptor format sense data (see SPC-6) in the Control mode page (see SPC-6) and in any
REQUEST SENSE commands (see SPC-6) it sends; and
b)
use commands with eight-byte LOGICAL BLOCK ADDRESS fields (e.g., READ (16), and WRITE (16)).
NOTE 1 - If a command requests access to an LBA greater than FFFF_FFFFh, fixed format sense data is
used, and an error occurs for that LBA, then there is no field in the sense data large enough to report that LBA
as having an error (see 4.18).
If a command is received that references or attempts to access a logical block that exceeds the capacity of the
medium, then the device server shall terminate the command (e.g., with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS
OUT OF RANGE). The device server:
a)
should terminate the command before processing; and
b)
may terminate the command after the device server has transferred some, all, or none of the data.
The location of a logical block on the medium is not required to have a relationship to the location of any other
logical block. However, in a direct access block device with rotating media (see 4.3.2), the time to access a
logical block at LBA [x+1] after accessing LBA [x] is often less than the time to access some other logical
block.
4.6 Physical blocks
4.6.1 Overview
A physical block is a set of data bytes on the medium accessed by the device server as a unit. A physical
block may contain:
a)
a portion of a logical block (i.e., there are multiple physical blocks in the logical block)(e.g., a physical
block length of 512 bytes with a logical block length of 2 048 bytes);
b)
a single complete logical block; or
c)
more than one logical block (i.e., there are multiple logical blocks in the physical block)(e.g., a
physical block length of 4 096 bytes with a logical block length of 512 bytes).
Each physical block may include additional information (e.g., an ECC which may be used for medium defect
management (see 4.13)), which may not be accessible to the application client.
If the device server supports the creation of pseudo unrecovered errors (see 4.18.2), then the device server
shall have the capability of marking individual logical blocks as containing pseudo unrecovered errors.
Logical blocks may or may not be aligned to physical block boundaries. A mechanism for establishing the
alignment is not defined by this standard.


Figure 2 shows examples of where there are one or more physical blocks per logical block, and LBA 0 is
aligned to a physical block boundary. The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field and the
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2) indicate the alignment.
Figure 2 — One or more physical blocks per logical block examples
LBA 0
LBA 1
LBA 2
LBA 3
LBA 0
PB
3 physical blocks per logical block:
Key:
LBA n = logical block with LBA n
PB = physical block
LBA 1
...
LBA 0
LBA 1
LBA 2
...
...
...
LBA 5
LBA 6
LBA 7
LBA 8
LBA 9
...
...
LBA 3
LBA 4
2 physical blocks per logical block:
LBA 4
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
PB
The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field is set to 0h (i.e., indicating one or more
physical blocks per logical block).
The LOWEST ALIGNED LOGICAL BLOCK ADDRESS field is set to 0000h (i.e., indicating that LBA 0 is
located at the beginning of a physical block).
1 physical block per logical block:
LBA 2
PB
PB
PB
LBA 0
PB
4 physical blocks per logical block:
LBA 1
PB
PB
PB
PB
PB
PB
PB
...
...
LBA 10
PB


Figure 3 shows examples of where there are one or more logical blocks per physical block, and LBA 0 is
aligned to a physical block boundary. The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field and the
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2) indicate the alignment.
Figure 3 — One or more logical blocks per physical block examples
Figure 4 shows examples of where there are two logical blocks per physical block, and different LBAs are
aligned to physical block boundaries. The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field and the
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2) indicate the alignment.
Figure 4 — Two logical blocks per physical block alignment examples
Key:
LBA n = logical block with LBA n
PB = physical block
PB
PB
PB
PB
PB
...
...
LBA 0
LBA 1
LBA 2
LBA 3
LBA 5
LBA 6
LBA 7
LBA 8
LBA 9
LBA 4
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 1h (i.e., 21 logical blocks per physical block):
PB
PB
...
...
LBA 0
LBA 1
LBA 2
LBA 3
LBA 5
LBA 6
LBA 7
LBA 4
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 2h (i.e., 22 logical blocks per physical block):
PB
LBA 0
LBA 1
LBA 2
LBA 3
LBA 5
LBA 6
LBA 7
LBA 4
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 3h (i.e., 23 logical blocks per physical block):
...
...
LBA 8
LBA 9 LBA 10 LBA 11
PB
LBA 10 LBA 11
PB
The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field is set to a non-zero value (i.e., indicating more
than one logical block per physical block).
The LOWEST ALIGNED LOGICAL BLOCK ADDRESS field is set to 0000h (i.e., indicating that LBA 0 is located
at the beginning of a physical block).
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0000h:
LBA 0
PB
LBA 1
PB
PB
PB
PB
Key:
LBA n = logical block with LBA n
PB = physical block
...
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0001h:
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
LBA 7
LBA 8
LBA 9
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 1h (i.e., 21 logical blocks per physical block):
LBA 0
PB
LBA 1
PB
PB
PB
PB
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
LBA 7
LBA 8
...
...
...
LBA 9 LBA 10
PB


Figure 5 shows examples of where there are four logical blocks per physical block, and different LBAs are
aligned to physical block boundaries. The LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field and the
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2) indicate the alignment.
Figure 5 — Four logical blocks per physical block alignment examples
If there is more than one logical block per physical block, then not all of the logical blocks are aligned to the
physical block boundaries. When using logical block access commands (see 4.2.2), application clients should:
a)
specify an LBA that is aligned to a physical block boundary; and
b)
access an integral number of physical blocks, provided that the access does not go beyond the last
LBA on the medium.
See annex D for an example method in which application clients may use alignment information to determine
optimal performance for logical block access.
4.6.2 Physical block misaligned write reporting
A misaligned write command is a write command that specifies a:
a)
LOGICAL BLOCK ADDRESS field that does not correspond to the first LBA of a physical block; or
b)
TRANSFER LENGTH field that is not a multiple of the number of logical blocks per physical block (see
table 89) and the number of logical blocks per physical block is greater than one.
The LPS Misalignment log page (see 6.4.6) reports misaligned write command information. The oldest
reported misaligned write command is identified by a parameter code value of 0001h, with each successive
time ordered misaligned write command identified by successively numbered parameter codes.
The maximum number of reportable LPS Misalignment log parameters supported by the device server is
indicated in the MAX_LPSM field in the LPS Misalignment Count log parameter. If the parameter code value for
Key:
LBA n = logical block with LBA n
PB = physical block
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0000h:
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0001h:
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0002h:
LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0003h:
LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field set to 2h (i.e., 22 logical blocks per physical block):
LBA 0
PB
LBA 1
PB
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
LBA 7
PB
PB
PB
PB
PB
PB
LBA 0
PB
LBA 1
PB
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
LBA 7
LBA 8
...
LBA 0
LBA 1
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
LBA 7
LBA 0
LBA 1
LBA 2
LBA 3
LBA 4
LBA 5
LBA 6
PB
LBA 9 LBA 10
LBA 7
LBA 8
LBA 8
LBA 9
...
...
...
...
...
...
...
