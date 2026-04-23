# 6.3 Diagnostic parameters

6.3 Diagnostic parameters
6.3.1 Diagnostic parameters overview
See table 172 for references to the pages and descriptors for diagnostic parameters used by direct access
block devices.
The diagnostic pages and their corresponding page codes for direct access block devices are shown in
table 172.
Table 172 — Diagnostic page codes for direct access block devices
Diagnostic page name
Page code
Reference
Diagnostic pages assigned by SPC-6
30h to 3Fh
SPC-6
Rebuild Assist Input diagnostic page
42h
6.3.2
Rebuild Assist Output diagnostic page
6.3.3
SCSI Enclosure Services diagnostic pages
01h to 2Fh
SES-3
Supported Diagnostic Page diagnostic page
00h
SPC-6
Translate Address Input diagnostic page
40h
6.3.4
Translate Address Output diagnostic page
6.3.5
Obsolete
41h
Vendor specific diagnostic pages
80h to FFh
Reserved for this standard
43h to 7Fh


6.3.2 Rebuild Assist Input diagnostic page
An application client sends a RECEIVE DIAGNOSTIC RESULTS command to retrieve a Rebuild Assist Input
diagnostic page (see table 173), which provides information about whether the rebuild assist mode (see 4.19)
is enabled or not and a device server’s rebuild assist mode capabilities.
The PAGE CODE field and the PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 173.
An ENABLED bit set to one indicates that the rebuild assist mode is enabled. An ENABLED bit set to zero
indicates that the rebuild assist mode is disabled.
The PHYSICAL ELEMENT LENGTH field indicates the length in bytes of the DISABLED PHYSICAL ELEMENT MASK field
and the length in bytes of the DISABLED PHYSICAL ELEMENT field.
The bits in the DISABLED PHYSICAL ELEMENT MASK field indicate the bits in the DISABLED PHYSICAL ELEMENT field
that are supported. Each bit set to one in the DISABLED PHYSICAL ELEMENT MASK field indicates that the
corresponding bit in the DISABLED PHYSICAL ELEMENT field is supported and may be set to one in a Rebuild
Assist Output diagnostic page sent with a SEND DIAGNOSTIC command.
The bits in the DISABLED PHYSICAL ELEMENT field indicate the physical elements that are disabled in this logical
unit. Each bit set to one indicates that a physical element is disabled, and the device server shall report
predicted read errors and predicted write errors for the associated group of LBAs.
Table 173 — Rebuild Assist Input diagnostic page
Bit
Byte
PAGE CODE (42h)
Reserved
(MSB)
PAGE LENGTH (4 + (2 × n))
(LSB)
Reserved
ENABLED
Reserved
PHYSICAL ELEMENT LENGTH (n)
DISABLED PHYSICAL ELEMENT MASK (if any)
•••
7 + n
8 + n
DISABLED PHYSICAL ELEMENT (if any)
•••
7 + (2 × n)


6.3.3 Rebuild Assist Output diagnostic page
The Rebuild Assist Output diagnostic page (see table 174) provides a method for an application client to
manage rebuild assist mode (see 4.19).
The PAGE CODE field and the PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 174.
An ENABLE bit set to one specifies that, after all fields in this diagnostic page have been validated:
a)
a self-test of the physical elements in the logical unit may be performed; and
b)
rebuild assist mode is enabled.
An ENABLE bit set to zero specifies that:
a)
rebuild assist mode shall be disabled;
b)
the other fields in this page shall be ignored; and
c)
all physical elements shall be enabled.
The PHYSICAL ELEMENT LENGTH field shall be set to the same value that is returned in the PHYSICAL ELEMENT
LENGTH field (see 6.3.2).
If the PHYSICAL ELEMENT LENGTH field is not set to the same value that is returned in the PHYSICAL ELEMENT
LENGTH field , then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
The device server shall ignore the DISABLED PHYSICAL ELEMENT MASK field.
Each bit in the DISABLE PHYSICAL ELEMENT field specifies a physical element that shall be disabled. A bit set to
one in the DISABLE PHYSICAL ELEMENT field specifies that the device server shall respond to read commands
and write commands specifying LBAs associated with that physical element as if the associated LBAs have
predicted errors. A bit set to zero in the DISABLE PHYSICAL ELEMENT field specifies that the device server shall
respond to read commands and write commands specifying LBAs associated with that physical element as if
Table 174 — Rebuild Assist Output diagnostic page
Bit
Byte
PAGE CODE (42h)
Reserved
(MSB)
PAGE LENGTH (4 + (2 × n))
(LSB)
Reserved
ENABLE
Reserved
PHYSICAL ELEMENT LENGTH (n)
DISABLED PHYSICAL ELEMENT MASK (if any)
•••
7 + n
8 + n
DISABLE PHYSICAL ELEMENT (if any)
•••
7 + (2 × n)


the associated LBAs do not have predicted errors. If the ENABLE bit is set to one, and the DISABLE PHYSICAL
ELEMENT field specifies:
a)
any bits set to one that are not supported by the logical unit;
b)
all bits that are supported by the logical unit are set to one; or
c)
setting to zero any bits that are set to one,
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
6.3.4 Translate Address Input diagnostic page
Table 175 defines the Translate Address Input diagnostic page sent by a device server in response to a
RECEIVE DIAGNOSTIC RESULTS command after a Translate Address Output diagnostic page (see 6.3.4)
has been sent by an application client with the SEND DIAGNOSTIC command. If a Translate Address Output
diagnostic page has not yet been processed by the device server, the results of a RECEIVE DIAGNOSTIC
RESULTS command requesting this diagnostic page are vendor specific.
The PAGE CODE field is defined in SPC-6 and shall be set to the value shown in table 175 for the Translate
Address Input diagnostic page.
The PAGE LENGTH field is defined in SPC-6.
The SUPPLIED FORMAT field contains the value from the SUPPLIED FORMAT field in the previous Translate
Address Output diagnostic page (see 6.3.5).
A reserved area (RAREA) bit set to zero indicates that no part of the translated address falls within a reserved
area of the medium (e.g., speed tolerance gap, alternate sector, or vendor reserved area). A RAREA bit set to
one indicates that all or part of the translated address falls within a reserved area of the medium. If the entire
translated address falls within a reserved area, then the device server may not return a translated address.
An alternate sector (ALTSEC) bit set to zero indicates that no part of the translated address is located in an
alternate sector of the medium or that the device server is unable to determine this information. An ALTSEC bit
Table 175 — Translate Address Input diagnostic page
Bit
Byte
PAGE CODE (40h)
Reserved
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Reserved
SUPPLIED FORMAT
RAREA
ALTSEC
ALTTRK
Reserved
TRANSLATED FORMAT
Translated address list
(MSB)
TRANSLATED ADDRESS 1 (if any)
•••
(LSB)
•••
n - 7
(MSB)
TRANSLATED ADDRESS x (if any)
•••
n
(LSB)


set to one indicates that the translated address is located in an alternate sector of the medium. If the device
server is unable to determine if all or part of the translated address is located in an alternate sector, then the
device server shall set this bit to zero.
An alternate track (ALTTRK) bit set to zero indicates that no part of the translated address is located on an
alternate track of the medium. An ALTTRK bit set to one indicates that part or all of the translated address is
located on an alternate track of the medium or the device server is unable to determine if all or part of the
translated address is located on an alternate track.
The TRANSLATED FORMAT field contains the value from the TRANSLATE FORMAT field in the previous Translate
Address Output diagnostic page (see 6.3.4).
Each TRANSLATED ADDRESS field contains an address descriptor (see 6.2) that the device server translated
from the address descriptor supplied by the application client in the previous Translate Address Output
diagnostic page (see 6.3.5). Each field shall be in the format (see 6.2) specified in the TRANSLATED FORMAT
field. If the short block format address descriptor (see 6.2.2) is specified, then the first four bytes of the
TRANSLATED ADDRESS field shall contain the short block format address descriptor and the last four bytes shall
contain 0000_0000h.
If the returned data is in short block format (see 6.2.2), long block format (see 6.2.5), or physical sector format
(see 6.2.7) and the ADDRESS TO TRANSLATE field in the previous Translate Address Output diagnostic page
covers more than one address after it has been translated (e.g., because of multiple physical sectors within a
single logical block or multiple logical blocks within a single physical sector), then the device server shall
return all possible addresses that are contained in the area specified by the address to be translated. If the
returned data is in bytes from index format (see 6.2.6), the device server shall return a pair of translated
values for each of the possible addresses that are contained in the area specified by the ADDRESS TO
TRANSLATE field in the previous Translate Address Output diagnostic page. Of the pair of translated values
returned, the first indicates the starting location and the second the ending location of the area.
6.3.5 Translate Address Output diagnostic page
The Translate Address diagnostic pages provides a method for an application client to have a device server
translate an address descriptor (see 6.2) from one format to another. The address descriptor to be translated
is sent to the device server in the Translate Address Output diagnostic page with a SEND DIAGNOSTIC
command and the results are returned by the device server in the Translate Address Input diagnostic page
sent in response to a RECEIVE DIAGNOSTIC RESULTS command.
Table 176 defines the format of the Translate Address Output diagnostic page sent with the SEND
DIAGNOSTIC command. The translated address returned in the Translate Address Input diagnostic page is
defined in 6.3.4.
Table 176 — Translate Address Output diagnostic page
Bit
Byte
PAGE CODE (40h)
Reserved
(MSB)
PAGE LENGTH (000Ah)
(LSB)
Reserved
SUPPLIED FORMAT
Reserved
TRANSLATE FORMAT
(MSB)
ADDRESS TO TRANSLATE
•••
(LSB)
