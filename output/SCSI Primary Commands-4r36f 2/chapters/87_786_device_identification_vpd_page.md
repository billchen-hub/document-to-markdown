# 7.8.6 Device Identification VPD page

The DIRECT ACCESS BLOCK DEVICE SPECIFIC TYPE field (see table 590) indicates the type of direct access block
device specific data in this descriptor.
The ADDITIONAL LENGTH field indicates the number of bytes that follow in this descriptor.
The contents of the direct access block device specific data depend on the value in the DIRECT ACCESS BLOCK
DEVICE SPECIFIC TYPE field.
7.8.6 Device Identification VPD page
7.8.6.1 Device Identification VPD page overview
The Device Identification VPD page (see table 591) provides the means to retrieve designation descriptors
applying to the logical unit. Logical units may have more than one designation descriptor (e.g., if several types
or associations of designator are supported). Designators consist of one or more of the following:
a)
logical unit names;
b)
SCSI target port identifiers;
c)
SCSI target port names;
d)
SCSI device names;
e)
relative target port identifiers;
f)
primary target port group number; or
g)
logical unit group number.
Designation descriptors shall be assigned to the peripheral device (e.g., a disk drive) and not to the currently
mounted media, in the case of removable media devices. Operating systems are expected to use the desig-
Table 590 — DIRECT ACCESS BLOCK DEVICE SPECIFIC TYPE field
Code
Description
00h to FEh
Reserved
FFh
Vendor specific


nation descriptors during system configuration activities to determine whether alternate paths exist for the
same peripheral device.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 591 for the Device Identification
VPD page.
Each designation descriptor (see table 592) contains information identifying the logical unit, SCSI target
device containing the logical unit, or access path (i.e., target port) used by the command and returned
parameter data. The Device Identification VPD page shall contain the designation descriptors enumerated in
7.8.6.2.
The PROTOCOL IDENTIFIER field may indicate the SCSI transport protocol to which the designation descriptor
applies. If the ASSOCIATION field is set to a value other than 01b (i.e., target port) or 10b (i.e., SCSI target
device) or the PIV bit is set to zero, then the PROTOCOL IDENTIFIER field contents are reserved. If the ASSOCI-
ATION field is set to a value of 01b or 10b and the PIV bit is set to one, then the PROTOCOL IDENTIFIER field shall
Table 591 — Device Identification VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (83h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Designation descriptor list
Designation descriptor [first]
•••
•••
Designation descriptor [last]
•••
n
Table 592 — Designation descriptor
Bit
Byte
PROTOCOL IDENTIFIER
CODE SET
PIV
Reserved
ASSOCIATION
DESIGNATOR TYPE
Reserved
DESIGNATOR LENGTH (n-3)
DESIGNATOR
•••
n


contain one of the values shown in table 477 (see 7.6.1) to indicate the SCSI transport protocol to which the
designation descriptor applies.
The CODE SET field contains a code set enumeration (see 4.3.3) that indicates the format of the DESIGNATOR
field.
A protocol identifier valid (PIV) bit set to zero indicates the PROTOCOL IDENTIFIER field contents are reserved. If
the ASSOCIATION field is set to a value of 01b or 10b, then a PIV bit set to one indicates the PROTOCOL
IDENTIFIER field contains a valid protocol identifier selected from the values shown in table 477 (see 7.6.1). If
the ASSOCIATION field is set to a value other than 01b or 10b, then the PIV bit contents are reserved.
The ASSOCIATION field indicates the entity with which the DESIGNATOR field is associated, as described in table
593. If a logical unit returns a designation descriptor with the ASSOCIATION field set to 00b or 10b, it shall return
the same descriptor when it is accessed through any other I_T nexus.
The DESIGNATOR TYPE field (see table 594) indicates the format and assignment authority for the designator.
The DESIGNATOR LENGTH field indicates the length in bytes of the DESIGNATOR field. The contents of the DESIG-
NATOR LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The DESIGNATOR field contains the designator as described by the ASSOCIATION, DESIGNATOR TYPE, CODE SET,
and DESIGNATOR LENGTH fields.
Table 593 — ASSOCIATION field
Code
Description
00b
The DESIGNATOR field is associated with the addressed logical unit.
01b
The DESIGNATOR field is associated with the target port that received the request.
10b
The DESIGNATOR field is associated with the SCSI target device that contains the
addressed logical unit.
11b
Reserved
Table 594 — DESIGNATOR TYPE field
Code
Description
Reference
0h
Vendor specific
7.8.6.3
1h
T10 vendor ID based
7.8.6.4
2h
EUI-64 based
7.8.6.5
3h
NAA
7.8.6.6
4h
Relative target port identifier
7.8.6.7
5h
Target port group
7.8.6.8
6h
Logical unit group
7.8.6.9
7h
MD5 logical unit identifier
7.8.6.10
8h
SCSI name string
7.8.6.11
9h
Protocol specific port identifier
7.8.6.12
Ah to Fh
Reserved


7.8.6.2 Device designation descriptor requirements
7.8.6.2.1 Designation descriptors for logical units other than well known logical units
For each logical unit that is not a well known logical unit, the Device Identification VPD page shall include at
least one designation descriptor in which a logical unit name (see SAM-5) is indicated. The designation
descriptor shall have the ASSOCIATION field set to 00b (i.e., logical unit) and the DESIGNATOR TYPE field set to:
a)
1h (i.e., T10 vendor ID based);
b)
2h (i.e., EUI-64-based);
c)
3h (i.e., NAA); or
d)
8h (i.e., SCSI name string).
At least one designation descriptor should have the DESIGNATOR TYPE field set to:
a)
2h (i.e., EUI-64-based);
b)
3h (i.e., NAA); or
c)
8h (i.e., SCSI name string).
In the case of virtual logical units (e.g., volume sets as defined by SCC-2), designation descriptors should
contain a DESIGNATOR TYPE field set to:
a)
2h (i.e., EUI-64-based);
b)
3h (i.e., NAA); or
c)
8h (i.e., SCSI name string).
In the case of virtual logical units that have an EUI-64 based designation descriptor (see 7.8.6.5) the DESIG-
NATOR LENGTH field should be set to:
a)
0Ch (i.e., EUI-64-based 12-byte); or
b)
10h (i.e., EUI-64-based 16-byte).
In the case of virtual logical units that have an NAA designation descriptor (see 7.8.6.6) the NAA field should
be set to 6h (i.e., IEEE Registered Extended).
The Device Identification VPD page shall contain the same set of designation descriptors with the ASSOCI-
ATION field set to 00b (i.e., logical unit) regardless of the I_T nexus being used to retrieve the designation
descriptors.
For logical units that are not well known logical units, the requirements for SCSI target device designation
descriptors are defined in 7.8.6.2.4 and the requirements for SCSI target port designation descriptors are
defined in 7.8.6.2.3.
7.8.6.2.2 Designation descriptors for well known logical units
Well known logical units shall not return any designation descriptors with the ASSOCIATION field set to 00b (i.e.,
logical unit).
The Device Identification VPD page shall contain the same set of designation descriptors with the ASSOCI-
ATION field set to 10b (i.e., SCSI target device) regardless of the I_T nexus being used to retrieve the desig-
nation descriptors.


7.8.6.2.3 Designation descriptors for SCSI target ports
7.8.6.2.3.1 Relative target port identifiers
For the target port through which the Device Identification VPD page is accessed, the Device Identification
VPD page should include one designation descriptor with the ASSOCIATION field set to 01b (i.e., target port)
and the DESIGNATOR TYPE field set to 4h (i.e., relative target port identifier) identifying the target port being
used to retrieve the designation descriptors.
7.8.6.2.3.2 Target port names or identifiers
For the SCSI target port through which the Device Identification VPD page is accessed, the Device Identifi-
cation VPD page should include one designation descriptor in which the target port name or identifier (see
SAM-5) is indicated. The designation descriptor, if any, shall have the ASSOCIATION field set to 01b (i.e., target
port) and the DESIGNATOR TYPE field set to:
a)
2h (i.e., EUI-64-based);
b)
3h (i.e., NAA); or
c)
8h (i.e., SCSI name string).
If the SCSI transport protocol standard for the target port defines target port names, the designation
descriptor, if any, shall contain the target port name. If the SCSI transport protocol for the target port does not
define target port names, the designation descriptor, if any, shall contain the target port identifier.
7.8.6.2.4 Designation descriptors for SCSI target devices
If the SCSI target device contains a well known logical unit, the Device Identification VPD page shall have one
or more designation descriptors for the SCSI target device. If the SCSI target device does not contain a well
known logical unit, the Device Identification VPD page should have one or more designation descriptors for
the SCSI target device.
Each SCSI target device designation descriptor, if any, shall have the ASSOCIATION field set to 10b (i.e., SCSI
target device) and the DESIGNATOR TYPE field set to:
a)
2h (i.e., EUI-64-based);
b)
3h (i.e., NAA); or
c)
8h (i.e., SCSI name string).
The Device Identification VPD page shall contain designation descriptors, if any, for all the SCSI device
names for all the SCSI transport protocols supported by the SCSI target device.


7.8.6.3 Vendor specific designator format
If the designator type is 0h (i.e., vendor specific), no assignment authority was used and there is no guarantee
that the designator is globally unique (i.e., the identifier is vendor specific). Table 595 defines the DESIGNATOR
field format.
7.8.6.4 T10 vendor ID based designator format
If the designator type is 1h (i.e., T10 vendor ID based), the DESIGNATOR field has the format shown in table
596.
The T10 VENDOR IDENTIFICATION field contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying the
vendor of the product. The data shall be left aligned within this field.The T10 vendor identification shall be one
assigned by INCITS. A list of assigned T10 vendor identifications is in Annex F and on the T10 web site
(http://www.T10.org).
NOTE 68 - The T10 web site (http://www.t10.org) provides a convenient means to request an identification
code.
The organization associated with the T10 vendor identification is responsible for ensuring that the VENDOR
SPECIFIC DESIGNATOR field is unique in a way that makes the entire DESIGNATOR field unique. A recommended
method of constructing a unique DESIGNATOR field is to concatenate the PRODUCT IDENTIFICATION field from the
standard INQUIRY data (see 6.6.2) and the PRODUCT SERIAL NUMBER field from the Unit Serial Number VPD
page (see 7.8.18).
Table 595 — Vendor specific DESIGNATOR field format
Bit
Byte
VENDOR SPECIFIC IDENTIFIER
•••
n
Table 596 — T10 vendor ID based DESIGNATOR field format
Bit
Byte
(MSB)
T10 VENDOR IDENTIFICATION
•••
(LSB)
VENDOR SPECIFIC IDENTIFIER
•••
n


7.8.6.5 EUI-64 based designator format
7.8.6.5.1 EUI-64 based designator format overview
If the designator type is 2h (i.e., EUI-64 based identifier), the DESIGNATOR LENGTH field (see table 597)
indicates the format of the designation descriptor.
7.8.6.5.2 EUI-64 designator format
If the designator type is 2h (i.e., EUI-64 based identifier) and the DESIGNATOR LENGTH field is set to 08h, the
DESIGNATOR field has the format shown in table 598. The CODE SET field shall be set to 1h (i.e., binary).
The IEEE COMPANY_ID field contains a 24-bit OUI assigned by the IEEE.
The VENDOR SPECIFIC EXTENSION IDENTIFIER field contains a 40-bit numeric value that is uniquely assigned by
the organization associated with the IEEE company_id as required by the IEEE definition of EUI-64.
Table 597 — EUI-64 based designator lengths
Designator Length
Description
Reference
08h
EUI-64 identifier
7.8.6.5.2
0Ch
EUI-64 based 12-byte identifier
7.8.6.5.3
10h
EUI-64 based 16-byte identifier
7.8.6.5.4
All other values
Reserved
Table 598 — EUI-64 DESIGNATOR field format
Bit
Byte
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC EXTENSION IDENTIFIER
•••
(LSB)


7.8.6.5.3 EUI-64 based 12-byte designator format
If the designator type is 2h (i.e., EUI-64 based identifier) and the DESIGNATOR LENGTH field is set to 0Ch, the
DESIGNATOR field has the format shown in table 599. The CODE SET field shall be set to 1h (i.e., binary).
The IEEE COMPANY_ID field and VENDOR SPECIFIC EXTENSION IDENTIFIER field are defined in 7.8.6.5.2.
The DIRECTORY ID field contains a directory identifier, as specified by ISO/IEC 13213:1994.
NOTE 69 - The EUI-64 based 12 byte format may be used to report IEEE 1394 target port identifiers (see
SBP-3).
7.8.6.5.4 EUI-64 based 16-byte designator format
If the designator type is 2h (i.e., EUI-64 based identifier) and the DESIGNATOR LENGTH field is set to 10h, the
DESIGNATOR field has the format shown in table 600. The CODE SET field shall be set to 1h (i.e., binary).
The IDENTIFIER EXTENSION field contains a 64 bit numeric value.
The IEEE COMPANY_ID field and VENDOR SPECIFIC EXTENSION IDENTIFIER field are defined in 7.8.6.5.2.
Table 599 — EUI-64 based 12-byte DESIGNATOR field format
Bit
Byte
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC EXTENSION IDENTIFIER
•••
(LSB)
(MSB)
DIRECTORY ID
•••
(LSB)
Table 600 — EUI-64 based 16-byte DESIGNATOR field format
Bit
Byte
(MSB)
IDENTIFIER EXTENSION
•••
(LSB)
(MSB)
IEEE COMPANY_ID
•••
(LSB)
(MSB)
VENDOR SPECIFIC EXTENSION IDENTIFIER
•••
(LSB)


NOTE 70 - The EUI-64 based 16-byte format may be used to report SCSI over RDMA target port identifiers (see
SRP).
7.8.6.6 NAA designator format
7.8.6.6.1 NAA identifier basic format
If the designator type is 3h (i.e., NAA identifier), the DESIGNATOR field has the format shown in table 601. This
format is compatible with the Name_Identifier format defined in FC-FS-3.
The Name Address Authority (NAA) field (see table 602) defines the format of the NAA specific data in the
designator.
Table 601 — NAA DESIGNATOR field format
Bit
Byte
NAA
NAA specific data
•••
n
Table 602 — Name Address Authority (NAA) field
Code
Description
Reference
2h
IEEE Extended
7.8.6.6.2
3h
Locally Assigned
7.8.6.6.3
5h
IEEE Registered
7.8.6.6.4
6h
IEEE Registered Extended
7.8.6.6.5
All others
Reserved


7.8.6.6.2 NAA IEEE Extended designator format
If NAA is 2h (i.e., IEEE Extended), the eight byte fixed length DESIGNATOR field shall have the format shown in
table 603. The CODE SET field shall be set to 1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to
08h.
The IEEE COMPANY_ID field contains a 24 bit canonical form OUI assigned by the IEEE.
The VENDOR SPECIFIC IDENTIFIER A contains a 12 bit numeric value that is uniquely assigned by the organi-
zation associated with the IEEE company_id.
The VENDOR SPECIFIC IDENTIFIER B contains a 24 bit numeric value that is uniquely assigned by the organi-
zation associated with the IEEE company_id.
NOTE 71 - The EUI-64 format includes a 40 bit vendor specific identifier. The IEEE Extended format includes
36 bits vendor specific identifier in two fields.
7.8.6.6.3 NAA Locally Assigned designator format
If NAA is 3h (i.e., Locally Assigned), the eight byte fixed length DESIGNATOR field shall have the format shown
in table 604. The CODE SET field shall be set to 1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to
08h.
The LOCALLY ADMINISTERED VALUE field contains a 60 bit value that is assigned by an administrator to be
unique within the set of SCSI domains that are accessible by a common instance of an administrative tool or
tools.
Table 603 — NAA IEEE Extended DESIGNATOR field format
Bit
Byte
NAA (2h)
(MSB)
VENDOR SPECIFIC IDENTIFIER A
(LSB)
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC IDENTIFIER B
(LSB)
Table 604 — NAA Locally Assigned DESIGNATOR field format
Bit
Byte
NAA (3h)
LOCALLY ADMINISTERED VALUE

•••


7.8.6.6.4 NAA IEEE Registered designator format
If NAA is 5h (i.e., IEEE Registered), the eight byte fixed length DESIGNATOR field shall have the format shown
in table 605. The CODE SET field shall be set to 1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to
08h.
The IEEE COMPANY_ID field contains a 24 bit canonical form OUI assigned by the IEEE.
The VENDOR SPECIFIC IDENTIFIER a 36 bit numeric value that is uniquely assigned by the organization
associated with the IEEE company_id.
NOTE 72 - The EUI-64 identifier includes a 40 bit vendor specific identifier. The IEEE Registered format
includes a 36 bit vendor specific identifier.
7.8.6.6.5 NAA IEEE Registered Extended designator format
If NAA is 6h (i.e., IEEE Registered Extended), the sixteen byte fixed length DESIGNATOR field shall have the
format shown in table 606. The CODE SET field shall be set to 1h (i.e., binary) and the DESIGNATOR LENGTH field
shall be set to 10h.
The IEEE COMPANY_ID field contains a 24 bit canonical form OUI assigned by the IEEE.
Table 605 — NAA IEEE Registered DESIGNATOR field format
Bit
Byte
NAA (5h)
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC IDENTIFIER
•••
(LSB)
Table 606 — NAA IEEE Registered Extended DESIGNATOR field format
Bit
Byte
NAA (6h)
(MSB)
IEEE COMPANY_ID
(LSB)
(MSB)
VENDOR SPECIFIC IDENTIFIER
•••
(LSB)
(MSB)
VENDOR SPECIFIC IDENTIFIER EXTENSION
•••
(LSB)


The VENDOR SPECIFIC IDENTIFIER field contains a 36 bit numeric value that is uniquely assigned by the organi-
zation associated with the IEEE company_id.
NOTE 73 - The EUI-64 format includes a 40 bit vendor specific identifier. The IEEE Registered Extended
format includes a 36 bit vendor specific identifier.
The VENDOR SPECIFIC IDENTIFIER EXTENSION a 64 bit numeric value that is assigned to make the DESIGNATOR
field unique.
7.8.6.7 Relative target port designator format
If the designator type is 4h (i.e., relative target port identifier) and the ASSOCIATION field is set to 01b (i.e.,
target port), then the DESIGNATOR field shall have the format shown in table 607. The CODE SET field shall be
set to 1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to 04h. If the ASSOCIATION field does not
contain 01b, use of this designator type is reserved.
The RELATIVE TARGET PORT IDENTIFIER field (see table 608) contains the relative port identifier of the target port
on which the INQUIRY command was received.
Table 607 — Relative target port DESIGNATOR field format
Bit
Byte
Reserved
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
Table 608 — RELATIVE TARGET PORT IDENTIFIER field
Code
Description
0h
Reserved
1h
Relative port 1, historically known as port A
2h
Relative port 2, historically known as port B
3h to FFFFh
Relative port 3 through 65 535


7.8.6.8 Target port group designator format
If the designator type is 5h (i.e., target port group) and the ASSOCIATION value is 01b (i.e., target port), the four
byte fixed length DESIGNATOR field shall have the format shown in table 609. The CODE SET field shall be set to
1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to 04h. If the ASSOCIATION field does not contain
01b, use of this designator type is reserved.
The TARGET PORT GROUP field indicates the primary target port group to which the target port is a member (see
5.16).
7.8.6.9 Logical unit group designator format
A logical unit group is a group of logical units that share the same primary target port group (see 5.16) defini-
tions. The primary target port groups maintain the same primary target port group asymmetric access states
for all logical units in the same logical unit group. A logical unit shall be in no more than one logical unit group.
If the designator type is 6h (i.e., logical unit group) and the ASSOCIATION value is 00b (i.e., logical unit), the four
byte fixed length DESIGNATOR field shall have the format shown in table 610. The CODE SET field shall be set to
1h (i.e., binary) and the DESIGNATOR LENGTH field shall be set to 04h. If the ASSOCIATION field does not contain
00b, use of this designator type is reserved.
The LOGICAL UNIT GROUP field indicates the logical unit group to which the logical unit is a member.
7.8.6.10 MD5 logical unit designator format
If the designator type is 7h (i.e., MD5 logical unit identifier) and the ASSOCIATION value is 00b (i.e., logical unit),
the DESIGNATOR field has the format shown in table 611. The CODE SET field shall be set to 1h (i.e., binary). The
MD5 logical unit designator shall not be used if a logical unit provides unique identification using designator
types 2h (i.e., EUI-64 based identifier), 3h (i.e., NAA identifier), or 8h (i.e., SCSI name string). A bridge device
may return a MD5 logical unit designator type for that logical unit that does not support the Device Identifi-
cation VPD page (see 7.8.6).
Table 609 — Target port group DESIGNATOR field format
Bit
Byte
Reserved
(MSB)
TARGET PORT GROUP
(LSB)
Table 610 — Logical unit group DESIGNATOR field format
Bit
Byte
Reserved
(MSB)
LOGICAL UNIT GROUP
(LSB)


If the ASSOCIATION field does not contain 00b, use of this designator type is reserved.
The MD5 LOGICAL UNIT IDENTIFIER field contains the message digest of the supplied message input. The
message digest shall be generated using the MD5 message-digest algorithm as defined in RFC 1321 (see
2.5) with the following information as message input:
1)
the contents of the T10 VENDOR IDENTIFICATION field in the standard INQUIRY data (see 6.6.2);
2)
the contents of the PRODUCT IDENTIFICATION field in the standard INQUIRY data;
3)
the contents of the PRODUCT SERIAL NUMBER field in the Unit Serial Number VPD page (see 7.8.18);
4)
the contents of a vendor specific DESIGNATOR field (designator type 0h) from the Device Identification
VPD page; and
5)
the contents of a T10 vendor ID based DESIGNATOR field (designator type 1h) from the Device Identifi-
cation VPD page.
If a field or page is not available, the message input for that field or page shall be 8 bytes of ASCII space
characters (i.e., 20h).
The uniqueness of the MD5 logical unit identifier is dependent upon the relative degree of randomness (i.e.,
the entropy) of the message input. If it is found that two or more logical units have the same MD5 logical unit
identifier, the application client should determine in a vendor specific manner whether the logical units are the
same entities.
The MD5 logical unit identifier example described in this paragraph and shown in table 612 and table 613 is
not a normative part of this standard. The data available for input to the MD5 algorithm for this example is
shown in table 612.
Table 611 — MD5 logical unit DESIGNATOR field format
Bit
Byte
(MSB)
MD5 LOGICAL UNIT IDENTIFIER
•••
(LSB)
Table 612 — MD5 logical unit identifier example available data
MD5 message input
Available
Contents
T10 VENDOR IDENTIFICATION field
Yes
T10
PRODUCT IDENTIFICATION field
Yes
MD5 Logical Unit
PRODUCT SERIAL NUMBER field
Yes
01234567
vendor specific DESIGNATOR field
No
T10 vendor ID based DESIGNATOR field
No


The concatenation of the fields in table 612 to form input to the MD5 algorithm is shown in table 613.
Based on the example inputs shown in table 612 and the concatenation of the inputs shown in table 613,
the MD5 base 16 algorithm described in RFC 1321 produces the value 8FAC A22A 0AC0 3839
255 25F2 0EFE 2E7Eh.
7.8.6.11 SCSI name string designator format
If the designator type is 8h (i.e., SCSI name string), the DESIGNATOR field has the format shown in table 614.
The CODE SET field shall be set to 3h (i.e., UTF-8).
The null-terminated, null-padded (see 4.3.2) SCSI NAME STRING field contains a UTF-8 format string. The
number of bytes in the SCSI NAME STRING field (i.e., the value in the DESIGNATOR LENGTH field) shall be no larger
than 256 and shall be a multiple of four.
The SCSI NAME STRING field starts with either:
a)
the four UTF-8 characters 'eui.' concatenated with 16, 24, or 32 hexadecimal digits (i.e., the UTF-8
characters 0 through 9 and A through F) for an EUI-64 based identifier (see 7.8.6.5). The first
hexadecimal digit shall be the most significant four bits of the first byte (i.e., most significant byte) of
the EUI-64 based identifier;
b)
the four UTF-8 characters 'naa.' concatenated with 16 or 32 hexadecimal digits for an NAA identifier
(see 7.8.6.6). The first hexadecimal digit shall be the most significant four bits of the first byte (i.e.,
most significant byte) of the NAA identifier; or
c)
the four UTF-8 characters 'iqn.' concatenated with an iSCSI Name for an iSCSI-name based identifier
(see iSCSI).
If the ASSOCIATION field is set to 00b (i.e., logical unit) and the SCSI NAME STRING field starts with the four UTF-8
characters 'iqn.', the SCSI NAME STRING field ends with the five UTF-8 characters ',L,0x' concatenated with 16
hexadecimal digits for the logical unit name extension. The logical unit name extension is a UTF-8 string
containing no more than 16 hexadecimal digits. The logical unit name extension is assigned by the SCSI
target device vendor and shall be assigned so the logical unit name is worldwide unique.
If the ASSOCIATION field is set to 01b (i.e., target port), the SCSI NAME STRING field ends with the five UTF-8
characters ',t,0x' concatenated with two or more hexadecimal digits as defined in the applicable SCSI
transport protocol standard.
Table 613 — Example MD5 input for computation of a logical unit identifier
Bytes
Hexadecimal values
ASCII values
00 to 15
54 31 30 20
20 20 20 20
4D 44 35 20
4C 6F 67 69
T10     MD5 Logi
16 to 31
63 61 6C 20
55 6E 69 74
30 31 32 33
34 35 36 37
cal Unit01234567
32 to 47
20 20 20 20
20 20 20 20
20 20 20 20
20 20 20 20
NOTE 1 Non-printing ASCII characters are shown as '.'.
Table 614 — SCSI name string DESIGNATOR field format
Bit
Byte
SCSI NAME STRING
•••
n


If the ASSOCIATION field is set to 10b (i.e., SCSI target device), the SCSI NAME STRING field has no additional
characters.
7.8.6.12 Protocol specific port identifier designator format
7.8.6.12.1 Protocol specific port identifier designator format overview
If the designator type is 9h (i.e., protocol specific port identifier), then:
a)
the ASSOCIATION field shall be set to 01b (i.e., target port);
b)
the PIV bit shall set to one; and
c)
the contents of the PROTOCOL IDENTIFIER field (see table 615) indicate the format of the DESIGNATOR
field.
7.8.6.12.2 USB target port identifier designator format
If the DESIGNATOR TYPE field is set to 9h (i.e., protocol specific port identifier) and the PROTOCOL IDENTIFIER field
is set to 9h (i.e., USB Attached SCSI), then:
a)
the DESCRIPTOR LENGTH field shall be set to four; and
b)
the DESIGNATOR field has the format is shown in table 616.
The DEVICE ADDRESS field contains a USB device address (see USB-3).
The INTERFACE NUMBER field contains a USB interface number within a USB configuration (see USB-3).
7.8.6.12.3 PCI Express routing ID designator format
If the DESIGNATOR TYPE field is set to 9h (i.e., protocol specific port identifier) and the PROTOCOL IDENTIFIER field
is set to Ah (i.e., SCSI over PCI Express architecture), then:
a)
the DESCRIPTOR LENGTH field shall be set to eight; and
Table 615 — Protocol specific port designator formats
PROTOCOL
IDENTIFIER
field
Description
Reference
9h
USB target port identifier
7.8.6.12.2
Ah
PCI Express routing ID
7.8.6.12.3
all others
Reserved
Table 616 — USB target port identifier DESIGNATOR field format
Bit
Byte
Reserved
DEVICE ADDRESS
Reserved
INTERFACE NUMBER
Reserved
