# 5.23 READ DEFECT DATA (12) command

5.22.2 READ DEFECT DATA (10) parameter data
The READ DEFECT DATA (10) parameter data (see table 92) contains a four-byte header, followed by zero or
more address descriptors.
A PLIST valid (PLISTV) bit set to zero indicates that the defect list does not contain the PLIST. A PLISTV bit set
to one indicates that the defect list contains the PLIST.
A GLIST valid (GLISTV) bit set to zero indicates that the defect list does not contain the GLIST. A GLISTV bit set
to one indicates that the defect list contains the GLIST.
The DEFECT LIST FORMAT field indicates the format of the address descriptors returned in the defect list. This
field is defined in 6.2.
If the device server returns short block format address descriptors (see 6.2.2) or long block format address
descriptors (see 6.2.5), then the address descriptors contain vendor-specific values.
The DEFECT LIST LENGTH field indicates the length in bytes of the defect list. The DEFECT LIST LENGTH is equal to
four or eight times the number of the address descriptors, depending on the format of the returned address
descriptors (see 6.2).
The defect list contains address descriptors (see 6.2).
5.23 READ DEFECT DATA (12) command
5.23.1 READ DEFECT DATA (12) command overview
The READ DEFECT DATA (12) command (see table 93) requests that the device server transfer parameter
data (see 5.23.2) containing a four-byte header, the PLIST, and/or the GLIST to the Data-In Buffer.
Table 92 — READ DEFECT DATA (10) parameter data
Bit
Byte
Parameter data header
Reserved
Reserved
PLISTV
GLISTV
DEFECT LIST FORMAT
(MSB)
DEFECT LIST LENGTH (n - 3)
(LSB)
Defect list (if any)
Address descriptor(s) (if any)
•••
n


An application client determines the length of the defect list by sending a READ DEFECT DATA (12)
command with an ALLOCATION LENGTH field set to eight and the ADDRESS DESCRIPTOR INDEX field set to
0000_0000h. The device server returns the defect list header that contains the length of the defect list.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 93 for the READ
DEFECT DATA (12) command.
See the READ DEFECT DATA (10) command (see 5.22) for the definitions of the REQ_PLIST bit, the
REQ_GLIST bit, and the DEFECT LIST FORMAT field.
The ADDRESS DESCRIPTOR INDEX field specifies the index of the first address descriptor (see 6.2) in the defect
list that the device server shall return. If the ADDRESS DESCRIPTOR INDEX field is set to:
a)
a value less than the number of available address descriptors, then the device server shall transfer a
defect list beginning with the address descriptor that is at the ADDRESS DESCRIPTOR INDEX field value
multiplied by the size of the address descriptor; or
b)
a value greater than or equal to the number of available address descriptors, then the device server
shall return a zero length defect list.
The ALLOCATION LENGTH field is defined in SPC-6, however if the length of all the address descriptors that are
available is greater than FFFF_FFFFh, then the device server shall transfer the length of address descriptors
specified by the allocation length or the DEFECT LIST LENGTH field value plus eight, whichever is less, and
complete the command with GOOD status.
The CONTROL byte is defined in SAM-6.
Table 93 — READ DEFECT DATA (12) command
Bit
Byte
OPERATION CODE (B7h)
Reserved
REQ_PLIST
REQ_GLIST
DEFECT LIST FORMAT
(MSB)
ADDRESS DESCRIPTOR INDEX
•••
(LSB)
(MSB)
ALLOCATION LENGTH
•••
(LSB)
Reserved
CONTROL


5.23.2 READ DEFECT DATA (12) parameter data
The READ DEFECT DATA (12) parameter data (see table 94) contains an eight-byte header, followed by zero
or more address descriptors.
The GENERATION CODE field is a two-byte counter that shall be incremented by one by the device server every
time the defect list is changed. A GENERATION CODE field set to 0000h indicates the generation code is not
supported. If the GENERATION CODE field is supported, then the GENERATION CODE field shall be initialized to at
least 0001h at power on and the device server shall wrap this field to 0001h as the next increment after
reaching its maximum value (i.e., FFFFh).
Application clients that use the GENERATION CODE field should read this field often enough to ensure that the
contents of this field do not increment a multiple of 65 535 times between readings.
The DEFECT LIST LENGTH field indicates the length in bytes of address descriptors from the beginning address
descriptor specified by the ADDRESS DESCRIPTOR INDEX field to the last address descriptor available to be
returned. A value of FFFF_FFFFh in the DEFECT LIST LENGTH field indicates that more than FFFF_FFFEh
bytes are available.
See the READ DEFECT DATA (10) command (see 5.22) for the definitions of the other fields in the READ
DEFECT DATA (12) parameter data.
Table 94 — READ DEFECT DATA (12) parameter data
Bit
Byte
Parameter data header
Reserved
Reserved
PLISTV
GLISTV
DEFECT LIST FORMAT
(MSB)
GENERATION CODE
(LSB)
(MSB)
DEFECT LIST LENGTH (n - 7)
•••
(LSB)
Defect list (if any)
Address descriptor(s) (if any)
•••
n
