# 4.13 Medium defects

4.12 Write protection
Write protection prevents the alteration of the medium by logical block access commands issued to the device
server. Write protection is controlled by:
a)
the user of the medium through manual intervention (e.g., a mechanical lock on the SCSI target
device);
b)
hardware controls (e.g., tabs on the medium’s housing); or
c)
software write protection.
All sources of write protection are independent. If present, any write protection shall cause otherwise valid
logical block access commands that request alteration of the medium to be terminated by the device server
with CHECK CONDITION status with the sense key set to DATA PROTECT and the appropriate additional
sense code for the condition. Only when all write protections are disabled shall the device server process
logical block access commands that request alteration of the medium.
Hardware write protection results when a physical attribute of the SCSI target device or its medium is changed
to specify that writing shall be prohibited. Changing the state of the hardware write protection requires
physical intervention, either with the SCSI target device or its medium. If allowed by the SCSI target device,
then changing the hardware write protection while the medium is mounted results in vendor specific behavior
that may include the writing of previously buffered data (e.g., data in cache).
Software write protection results when the device server is marked as write protected by the application client
using the SWP bit in the Control mode page (see SPC-6). Changing the state of software write protection shall
not prevent previously accepted logical block data (e.g., logical block data in cache) from being written to the
medium.
The device server reports the status of write protection in the device server and on the medium with the
DEVICE-SPECIFIC PARAMETER field (see 6.5.1).
4.13 Medium defects
4.13.1 Medium defects overview
Any medium has the potential for medium defects that cause data to be lost. Therefore, physical blocks and/or
logical blocks may contain additional information that allows the detection of changes to the logical block data
caused by medium defect or other phenomena. The additional information may also allow the logical block
data to be reconstructed following the detection of such a change (e.g., ECC bytes).
A medium defect causes:
a)
a recovered error if the device server is able to read or write a logical block within the logical unit’s
recovery limits; or
b)
an unrecovered error if the device server is unable to read or write a logical block within the logical
unit’s recovery limits,
where the logical unit’s recovery limits are:
a)
specified in the Read-Write Error Recovery mode page (see 6.5.10);
b)
specified in the Verify Error Recovery mode page (see 6.5.11); or
c)
vendor specific, if the device server does not implement the Read-Write Error Recovery mode page or
the Verify Error Recovery mode page.
Direct access block devices may allow an application client to use the features of the WRITE LONG
commands (see 5.50 and 5.51) to create a pseudo uncorrectable error. Processing and clearing pseudo
uncorrectable errors is described in 4.18.2.


The device server maintains the defect lists shown in table 11.
The READ DEFECT DATA commands (see 5.22 and 5.23) allow an application client to request that the
device server return the PLIST and/or the GLIST.
The FORMAT UNIT command allows an application client to request that the device server clear the GLIST.
During a format operation, the device server shall not assign LBAs to any physical block in:
a)
the PLIST, if the PLIST is specified to be used; or
b)
the GLIST, if the GLIST is specified to be used.
A device server performs automatic reassignment of defects as specified by the settings in the Read-Write
Error Recovery mode page (see 6.5.10).
The device server does not perform automatic read reassignment for an LBA referencing a logical block on
which an unrecovered error has occurred. If the application client is notified by the device server that an
unrecovered error occurred (e.g., as indicated by a read command being terminated with CHECK
CONDITION status with the sense key set to MEDIUM ERROR and the additional sense code set to
UNRECOVERED READ ERROR) and:
a)
the application client is able to regenerate the logical block data for the LBA (e.g., in a redundancy
group, the application client regenerates logical block data from the logical block data on the other
logical units in the redundancy group) and the AWRE bit is set to one in the Read-Write Error Recovery
mode page, then the application client may send a write command with that regenerated logical block
data to trigger automatic write reassignment;
b)
the application client is able to regenerate the logical block data for the LBA and the AWRE bit is set to
zero in the Read-Write Error Recovery mode page, then the application client may:
1)
send a REASSIGN BLOCKS command to perform a reassign operation on the LBA; and
2)
send a write command with that regenerated logical block data;
or
c)
the application client is unable to regenerate the logical block data for the LBA, then the application
client may send a REASSIGN BLOCKS command to request that the device server perform a
reassign operation on the LBA.
Table 11 — Defect lists (i.e., PLIST and GLIST)
Defect list
Source
Content
PLIST
(i.e., primary
defect list)
Manufacturer
Address descriptors (see 6.2) for physical blocks that
contain permanent medium defects and never contain
logical block data
GLIST
(i.e., grown
defect list)
FORMAT UNIT
commands (see 5.4)
Address descriptors for physical blocks detected by the
device server to have medium defects during an optional
certification process performed during a format operation
Address descriptors for physical blocks specified in the
FORMAT UNIT parameter list (see 5.4.2)
REASSIGN BLOCKS
commands (see 5.24)
Address descriptors for physical blocks referenced by the
LBAs specified in the reassign LBA list (see 5.24.2)
Read medium
operations
Address descriptors for physical blocks that have been
reassigned as the result of automatic read reassignment
Write medium
operations
Address descriptors for physical blocks that have been
reassigned as the result of automatic write reassignment


4.13.2 Generation of defect lists
This standard defines address descriptor formats for describing defects (see 6.2). Table 12 lists the defects
that each address descriptor format is capable of describing.
For a direct access block device using rotating media (see 4.3.2), to represent two or more sequential
physical blocks on the same track using a pair of address descriptors:
a)
the MADS bit shall be set to one in the first address descriptor;
b)
the MADS bit shall be set to zero in the second address descriptor;
c)
the CYLINDER NUMBER field in the first address descriptor shall be equal to the CYLINDER NUMBER field
in the second address descriptor;
d)
the HEAD NUMBER field in the first address descriptor shall be equal to the HEAD NUMBER field in the
second address descriptor;
e)
for a pair of extended bytes from index format address descriptors, the BYTES FROM INDEX field in the
first address descriptor shall be less than the BYTES FROM INDEX field in the second address
descriptor; and
f)
for a pair of extended physical sector format address descriptors, the SECTOR NUMBER field in the first
address descriptor shall be less than the SECTOR NUMBER field in the second address descriptor.
For a direct access block device using rotating media, to represent two or more sequential tracks on the same
head using a pair of address descriptors:
a)
the MADS bit shall be set to one in the first address descriptor;
b)
the MADS bit shall be set to zero in the second address descriptor;
Table 12 — Address descriptor formats
Format
Single
physical
block
Multiple sequential
physical blocks
Reference
Entire track
Range
Short block format
yes
no
no
6.2.2
Extended bytes from index format
yes a
yes e
yes i
6.2.3
Extended physical sector format
yes b
yes f
yes i
6.2.4
Long block format
yes
no
no
6.2.5
Bytes from index format
yes c
yes g
no
6.2.6
Physical sector format
yes d
yes h
no
6.2.7
a Describes a single physical block with the MADS bit set to zero and the BYTES FROM INDEX field set to a
value other than FFF_FFFFh.
b Describes a single physical block with the MADS bit set to zero and the SECTOR NUMBER field set to a
value other than FFF_FFFFh.
c Describes a single physical block with the BYTES FROM INDEX field set to a value other than
FFFF_FFFFh.
d Describes a single physical block with the SECTOR NUMBER field set to a value other than FFFF_FFFFh.
e Describes an entire track with the BYTES FROM INDEX field set to FFF_FFFFh.
f
Describes an entire track with the SECTOR NUMBER field set to FFF_FFFFh.
g Describes an entire track with the BYTES FROM INDEX field set to FFFF_FFFFh.
h Describes an entire track with the SECTOR NUMBER field set to FFFF_FFFFh.
i
Describes a range with a pair of address descriptors using the same address descriptor format in which:
a)
the first address descriptor describes the starting location and has the MADS bit set to one;
b)
the second address descriptor describes the ending location and has the MADS bit set to zero; and
c)
the ending location is after the starting location.
