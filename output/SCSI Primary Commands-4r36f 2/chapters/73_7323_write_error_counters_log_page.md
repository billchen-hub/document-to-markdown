# 7.3.23 Write Error Counters log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Verify Error
Counter log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The VERIFY ERROR COUNTER field contains the value for the counter described by the contents of the
PARAMETER CODE field.
7.3.23 Write Error Counters log page
7.3.23.1 Overview
Using the format shown in table 436, the Write Error Counters log page (page code 02h) contains log param-
eters that report bounded data counters for detected events (e.g., total bytes processed) identified by the
parameter codes listed in table 435.
Table 435 — Write Error Counters log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Errors corrected without substantial
delay c
Reset Only
7.3.23.2
At least one b
0001h
Errors corrected with possible delays c
0002h
Total (e.g., rewrites or rereads) c
0003h
Total errors corrected c
0004h
Total times correction algorithm
processed c
0005h
Total bytes processed c
0006h
Total uncorrected errors c
8000h to
FFFFh
Vendor specific
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
b If the Write Error Counters log page is supported, at least one of the parameter codes listed in this table
shall be supported.
c The exact definition of this error counter is not part of this standard. This counter should not be used to
compare products because the products may define errors differently.


The Write Error Counters log page has the format shown in table 436.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 436 for the Write Error Counters
log page.
Each Write Error Counter log parameter contains the information described in 7.3.23.2.
7.3.23.2 Write Error Counter log parameter
The Write Error Counter log parameter has the format shown in table 437.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 435 for the Write Error
Counter log parameter.
Table 436 — Write Error Counters log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (02h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Write error counter log parameters
Write Error Counter log parameter (see 7.3.23.2)
[first]
•••
•••
Write Error Counter log parameter (see 7.3.23.2)
[last]
•••
n
Table 437 — Write Error Counter log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 435)
(LSB)
Parameter control byte – bounded data counter log parameter (see 7.3.2.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
(MSB)
WRITE ERROR COUNTER
•••
n
(LSB)


The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Write Error
Counter log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The WRITE ERROR COUNTER field contains the value for the counter described by the contents of the
PARAMETER CODE field.


7.4 Medium auxiliary memory attributes
7.4.1 Attribute format
Each medium auxiliary memory attribute shall be communicated between the application client and device
server in the format shown in table 438. This format shall be used in the parameter data for the WRITE
ATTRIBUTE command (see 6.48) and the READ ATTRIBUTE command (see 6.17). The attribute format in
this standard implies nothing about the physical representation of an attribute in the medium auxiliary memory.
The ATTRIBUTE IDENTIFIER field contains a code value identifying the attribute (see 7.4.2).
The READ ONLY bit indicates whether the attribute is in the read only state (see 5.7). If the READ ONLY bit is set
to one, the attribute is in the read only state. If the READ ONLY bit is set to zero, the attribute is in the read/write
state.
The FORMAT field (see table 439) specifies the format of the data in the ATTRIBUTE VALUE field.
The ATTRIBUTE LENGTH field specifies the length in bytes of the ATTRIBUTE VALUE field.
The ATTRIBUTE VALUE field contains the current value, for the READ ATTRIBUTE command (see 6.17), or
intended value, for the WRITE ATTRIBUTE command (see 6.48), of the attribute.
Table 438 — MAM ATTRIBUTE format
Bit
Byte
(MSB)
ATTRIBUTE IDENTIFIER
(LSB)
READ ONLY
Reserved
FORMAT
(MSB)
ATTRIBUTE LENGTH (n-4)
(LSB)
ATTRIBUTE VALUE
•••
n
Table 439 — MAM attribute FORMAT field
Format
Name
Description
00b
BINARY
The ATTRIBUTE VALUE field contains binary data.
01b
ASCII
The ATTRIBUTE VALUE field contains left-aligned ASCII data (see 4.3.1).
10b
TEXT
The attribute contains textual data. The character set is as described in
the TEXT LOCALIZATION IDENTIFIER attribute (see 7.4.2.4.6).
11b
Reserved
