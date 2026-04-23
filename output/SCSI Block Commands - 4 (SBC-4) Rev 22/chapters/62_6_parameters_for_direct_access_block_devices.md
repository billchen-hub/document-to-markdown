# 6 Parameters for direct access block devices

6 Parameters for direct access block devices
6.1 Parameters for direct access block devices introduction
Table 160 shows the parameters for direct access block devices defined in clause 6 and a reference to the
subclause where each parameter type is defined.
6.2 Address descriptors
6.2.1 Address descriptor overview
This subclause describes the address descriptors (see table 161) used for:
a)
the FORMAT UNIT command (see 5.4);
b)
the READ DEFECT DATA commands (see 5.22 and 5.23);
c)
the Translate Address Input diagnostic page (see 6.3.4) for the SEND DIAGNOSTIC command (see
SPC-6); and
d)
the Translate Address Output diagnostic page (see 6.3.5) for the RECEIVE DIAGNOSTIC RESULTS
command (see SPC-6).
The format type of an address descriptor is:
a)
specified in the DEFECT LIST FORMAT field (see 5.4.1);
b)
indicated in the DEFECT LIST FORMAT field (see 5.22.2 and 5.23.2);
c)
specified in the SUPPLIED FORMAT field and the TRANSLATE FORMAT field for the Translate Address
Output diagnostic page; or
d)
indicated in the SUPPLIED FORMAT field and the TRANSLATE FORMAT field for the Translate Address Input
diagnostic page.
Table 160 — Parameters for direct access block devices
Parameter type
Reference
Address descriptors
6.2
Diagnostic parameters
6.3
Log parameters
6.4
Mode parameters
6.5
Vital product data (VPD) parameters
6.6
Copy manager parameters
6.7
Logical block markup descriptors
6.8


Table 161 defines the types of address descriptors.
6.2.2 Short block format address descriptor
A format type of 000b specifies the short block format address descriptor (see table 162).
For the FORMAT UNIT parameter list, the SHORT BLOCK ADDRESS field specifies a four-byte LBA. If the
physical block containing the logical block referenced by the specified LBA contains additional logical blocks,
then the device server may consider the LBAs of those additional logical blocks to also have been specified.
For the READ DEFECT DATA parameter data, the SHORT BLOCK ADDRESS field indicates a vendor specific
four-byte value.
For the Translate Address diagnostic pages, the SHORT BLOCK ADDRESS field contains:
a)
a four-byte LBA, if the value is less than or equal to the capacity of the medium; or
b)
a vendor specific four-byte value, if the value is greater than the capacity of the medium.
6.2.3 Extended bytes from index address descriptor
A format type of 001b specifies the extended bytes from index format address descriptor (see table 163). For
the FORMAT UNIT parameter list and the READ DEFECT DATA parameter data, this address descriptor
contains the location of a defect that:
a)
is the length of one track (see 4.3.2);
b)
is less than the length of a physical block; or
c)
starts from one address descriptor and extends to the next address descriptor.
Table 161 — Address descriptors
Type
Description
Reference
000b
Short block format address descriptor
6.2.2
001b
Extended bytes from index format address descriptor a
6.2.3
010b
Extended physical sector format address descriptor a
6.2.4
011b
Long block format address descriptor
6.2.5
100b
Bytes from index format address descriptor a
6.2.6
101b
Physical sector format address descriptor a
6.2.7
110b
Vendor specific
111b
Reserved
a This address descriptor format type is defined for direct access block devices using
rotating media (see 4.3.2).
Table 162 — Short block format address descriptor (000b)
Bit
Byte
(MSB)
SHORT BLOCK ADDRESS
•••
(LSB)


For the Translate Address diagnostic pages, this address descriptor contains the location of an LBA. For the
Translate Address Output diagnostic page (see 6.2.5), if the SUPPLIED FORMAT field is set to 001b and the
MADS bit in the ADDRESS TO TRANSLATE field is set to one, then the device server shall terminate the SEND
DIAGNOSTIC command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The CYLINDER NUMBER field contains the cylinder number (see 4.3.2).
The HEAD NUMBER field contains the head number (see 4.3.2).
A multi-address descriptor start (MADS) bit set to one specifies that this address descriptor defines the
beginning of a defect that spans multiple addresses. The defect may be a number of sequential physical
blocks on the same cylinder and head (i.e., a track) or may span a number of sequential tracks on the same
head. A MADS bit set to zero specifies that:
a)
this address descriptor defines the end of a defect if the previous address descriptor has the MADS bit
set to one; or
b)
this address descriptor defines a single track that contains one or more defects (i.e., the BYTES FROM
INDEX field contains FFF_FFFFh) or a single defect (i.e., the BYTES FROM INDEX field does not contain
FFF_FFFFh).
See 4.13.2 for valid combinations of two address descriptors that describe a defect.
The BYTES FROM INDEX field:
a)
if not set to FFF_FFFFh, contains the number of bytes from the index (e.g., from the start of the track)
to the location being described; or
b)
if set to FFF_FFFFh, specifies or indicates that the entire track is being described.
More than one logical block may be described by this address descriptor.
Table 164 defines the order of the fields used for sorting extended bytes from index format address
descriptors if the command using the address descriptors specifies sorting.
Table 163 — Extended bytes from index format address descriptor (001b)
 Bit
Byte
(MSB)
CYLINDER NUMBER
•••
(LSB)
HEAD NUMBER
MADS
Reserved
(MSB)
•••
BYTES FROM INDEX
(LSB)
Table 164 — Sorting order for extended bytes from index format address descriptors
Bit
(MSB)
•••
•••
•••
(LSB)
CYLINDER NUMBER field
HEAD NUMBER field
BYTES FROM INDEX field


6.2.4 Extended physical sector format address descriptor
A format type of 010b specifies the extended physical sector format address descriptor (see table 165). For
the FORMAT UNIT parameter list and the READ DEFECT DATA parameter data, this address descriptor
contains the location of a defect that:
a)
is the length of one track (see 4.3.2);
b)
is less than the length of a physical block; or
c)
starts from one address descriptor and extends to the next address descriptor.
For the Translate Address diagnostic pages, this address descriptor specifies the location of an LBA. For the
Translate Address Output diagnostic page (see 6.2.5), if the SUPPLIED FORMAT field is set to 010b and the
MADS bit in the ADDRESS TO TRANSLATE field is set to one, then the device server shall terminate the SEND
DIAGNOSTIC command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The CYLINDER NUMBER field contains the cylinder number (see 4.3.2).
The HEAD NUMBER field contains the head number (see 4.3.2).
A multi-address descriptor start (MADS) bit set to one specifies that this address descriptor defines the
beginning of a defect that spans multiple addresses. The defect may span a number of sequential physical
blocks on the same cylinder and head (i.e., a track) or may span a number of sequential tracks on the same
head. A MADS bit set to zero specifies that:
a)
this address descriptor defines the end of a defect if the previous address descriptor has the MADS bit
set to one; or
b)
this address descriptor defines a single track that contains one or more defects (i.e., the SECTOR
NUMBER field contains FFF_FFFFh) or a single defect (i.e., the SECTOR NUMBER field does not contain
FFF_FFFFh).
See 4.13.2 for valid combinations of two address descriptors that describe a defect.
The SECTOR NUMBER field:
a)
if not set to FFF_FFFFh, contains the sector number (see 4.3.2) of the location being described; or
b)
if set to FFF_FFFFh, specifies or indicates that the entire track is being described.
More than one logical block may be described by this address descriptor.
Table 165 — Extended physical sector format address descriptor (010b)
 Bit
Byte
(MSB)
CYLINDER NUMBER
•••
(LSB)
HEAD NUMBER
MADS
Reserved
(MSB)
•••
SECTOR NUMBER
(LSB)


Table 166 defines the order of the fields used for sorting extended physical sector format address descriptors
if the command using the address descriptors specifies sorting.
6.2.5 Long block format address descriptor
A format type of 011b specifies the long block format address descriptor (see table 167).
For the FORMAT UNIT parameter list, the LONG BLOCK ADDRESS field specifies an eight-byte LBA. If the
physical block containing the logical block referenced by the specified LBA contains additional logical blocks,
then the device server may consider the LBAs of those additional logical blocks to also have been specified.
For the READ DEFECT DATA parameter data, the LONG BLOCK ADDRESS field indicates a vendor specific
eight-byte value.
For the Translate Address diagnostic pages, the LONG BLOCK ADDRESS field contains:
a)
an eight-byte LBA, if the value is less than or equal to the capacity of the medium; or
b)
a vendor specific eight-byte, if the value is greater than the capacity of the medium.
6.2.6 Bytes from index format address descriptor
A format type of 100b specifies the bytes from index format address descriptor (see table 168). This address
descriptor contains the location of a track or an offset from the start of a track.
Table 166 — Sorting order for extended physical sector format address descriptors
Bit:
(MSB)
•••
•••
•••
(LSB)
CYLINDER NUMBER field
HEAD NUMBER field
SECTOR NUMBER field
Table 167 — Long block format address descriptor (011b)
Bit
Byte
(MSB)
LONG BLOCK ADDRESS
•••
(LSB)
Table 168 — Bytes from index format address descriptor (100b)
Bit
Byte
(MSB)
CYLINDER NUMBER
•••
(LSB)
HEAD NUMBER
(MSB)
BYTES FROM INDEX
•••
(LSB)


The CYLINDER NUMBER field contains the cylinder number (see 4.3.2).
The HEAD NUMBER field contains the head number (see 4.3.2).
The BYTES FROM INDEX field contains the number of bytes from the index (e.g., from the start of the track) to
the location being described. A BYTES FROM INDEX field set to FFFF_FFFFh specifies or indicates that the
entire track is being described.
More than one logical block may be described by this address descriptor.
Table 169 defines the order of the fields used for sorting bytes from index format address descriptors if the
command using the address descriptors specifies sorting.

6.2.7 Physical sector format address descriptor
A format type of 101b specifies the physical sector format address descriptor (see table 170). This address
descriptor contains the location of a track or a sector (see 4.3.2).
The CYLINDER NUMBER field contains the cylinder number (see 4.3.2).
The HEAD NUMBER field contains the head number (see 4.3.2).
The SECTOR NUMBER field contains the sector number (see 4.3.2). A SECTOR NUMBER field set to FFFF_FFFFh
specifies or indicates that the entire track is being described.
More than one logical block may be described by this address descriptor.
Table 171 defines the order of the fields used for sorting physical sector format address descriptors if the
command using the address descriptors specifies sorting.

Table 169 — Sorting order for bytes from index format address descriptors
Bit
(MSB)
•••
•••
•••
(LSB)
CYLINDER NUMBER field
HEAD NUMBER field
BYTES FROM INDEX field
Table 170 — Physical sector format address descriptor (101b)
Bit
Byte
(MSB)
CYLINDER NUMBER
•••
(LSB)
HEAD NUMBER
(MSB)
SECTOR NUMBER
•••
(LSB)
Table 171 — Sorting order for physical sector format address descriptors
Bit
(MSB)
•••
•••
•••
(LSB)
CYLINDER NUMBER field
HEAD NUMBER field
SECTOR NUMBER field
