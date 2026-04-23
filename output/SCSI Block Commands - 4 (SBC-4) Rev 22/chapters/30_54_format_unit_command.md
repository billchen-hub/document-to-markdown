# 5.4 FORMAT UNIT command

The CONTROL byte is defined in SAM-6.
5.4 FORMAT UNIT command
5.4.1 FORMAT UNIT command overview
The FORMAT UNIT command (see table 38) requests that the device server perform a format operation.
The device server shall handle any deferred microcode as specified in 4.24.
Table 38 defines the FORMAT UNIT command.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 38 for the FORMAT
UNIT command.
The combination (see table 44) of the format protection information (FMTPINFO) field and the PROTECTION FIELD
USAGE field (see 5.4.2.2) specifies whether or not the device server enables or disables the use of protection
information.
A LONGLIST bit set to zero specifies that the parameter list, if any, contains a short parameter list header as
shown in table 42. A LONGLIST bit set to one specifies that the parameter list, if any, contains a long parameter
list header as shown in table 43. If the FMTDATA bit is set to zero, then the LONGLIST bit shall be ignored.
A format data (FMTDATA) bit set to one specifies that the FORMAT UNIT parameter list (see 5.4.2) shall be
transferred from the Data-Out Buffer. A FMTDATA bit set to zero specifies that no parameter list be transferred
from the Data-Out Buffer. If the FMTDATA bit is set to zero and the FMTPINFO field is not set to zero, then the
device server shall terminate the command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
Following a successful format operation, the PROT_EN bit and the P_TYPE field (see 5.21.2) indicate the type of
protection currently in effect on the logical unit.
If protection information is written during a format operation (i.e., the FMTPINFO field is set to a value greater
than zero), then protection information shall be written to a default value of FFFF_FFFF_FFFF_FFFFh.
A complete list (CMPLST) bit set to zero specifies that the device server shall add the defect list included in the
FORMAT UNIT parameter list to the existing GLIST (see 4.13). A CMPLST bit set to one specifies that the
device server shall replace the existing GLIST with the defect list, if any, included in the FORMAT UNIT
parameter list.
If the FMTDATA bit is set to zero, then the CMPLST bit shall be ignored.
If the FMTDATA bit is set to one, then the DEFECT LIST FORMAT field specifies the format of the address
descriptors in the defect list in the FORMAT UNIT parameter list.
Table 38 — FORMAT UNIT command
Bit
Byte
OPERATION CODE (04h)
FMTPINFO
LONGLIST
FMTDATA
CMPLST
DEFECT LIST FORMAT
Vendor specific
Reserved
Reserved
FFMT
CONTROL


Table 39 defines support requirements for address descriptors based on the combinations of the FMTDATA bit,
the CMPLST bit, the DEFECT LIST FORMAT field, and the DEFECT LIST LENGTH field.
Table 39 — FORMAT UNIT command address descriptor support requirements
Field in the FORMAT UNIT CDB
DEFECT
LIST
LENGTH a
Support
Comments
FMTDATA
CMPLST
DEFECT LIST FORMAT
any
000b
Not
available
M
Vendor specific
defect information
Either:
a)
000b (i.e., short block address
descriptor)(see 6.2.2);
b)
001b (i.e., extended bytes from index
address descriptor)(see 6.2.3);
c)
010b (i.e., extended physical sector
address descriptor)(see 6.2.4);
d)
011b (i.e., long block address
descriptor)(see 6.2.5);
e)
100b (i.e., bytes from index address
descriptor)(see 6.2.6); or
f)
101b (i.e., physical sector address
descriptor)(see 6.2.7)
Zero
O
See b and d
O
See b and e
Non-zero
O
See c and d
O
See c and e
110b (i.e., vendor specific)
Zero
O
See b and d
Non-zero
O
See c and d
Zero
O
See b and e
Non-zero
O
See c and e
All other combinations
Reserved
a This field is in the parameter list header.
b No defect list is included in the parameter list.
c A defect list is included in the parameter list.
d The device server retains the existing GLIST.
e The device server discards the existing GLIST.


The fast format (FFMT) field is described in table 40
The CONTROL byte is defined in SAM-6.
5.4.2 FORMAT UNIT parameter list
5.4.2.1 FORMAT UNIT parameter list overview
Table 41 defines the FORMAT UNIT parameter list.
The parameter list header is defined in 5.4.2.2.
Table 40 — FFMT field description
Code
Description
Support
00b
The device server initializes the medium (see 4.10) as specified in the CDB
and parameter list before completing the format operation. After successful
completion of the format operation, read commands and verify commands
are processed as described in 4.33.3.2.1 and 4.33.3.2.2.
Mandatory
01b
The device server initializes the medium (see 4.10) without overwriting the
medium (i.e., resources for managing medium access are initialized and the
medium is not written) before completing the format operation. After
successful completion of the format operation, read commands and verify
commands are processed as described in 4.33.3.2.1 and 4.33.3.2.3.
If the device server determines that the options specified in this FORMAT
UNIT command are incompatible with the read command and verify
command requirements described in 4.33.3.2.3, then the device server shall
not perform the format operation and shall terminate the FORMAT UNIT
command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID FAST
FORMAT.
Optional
10b
The device server initializes the medium (see 4.10) without overwriting the
medium (i.e., resources for managing medium access are initialized and the
medium is not written) before completing the format operation. After
successful completion of the format operation, read commands and verify
commands are processed as described in 4.33.3.2.1 and 4.33.3.2.4.
Optional
11b
Reserved
Table 41 — FORMAT UNIT parameter list
Bit
Byte
Parameter list header (see table 42 or table 43 in 5.4.2.2)
Initialization pattern descriptor (if any) (see table 45 in 5.4.2.3)
Defect list (if any)


The initialization pattern descriptor, if any, is defined in 5.4.2.3.
The defect list, if any, contains address descriptors (see 6.2) each specifying a location on the medium to
which the device server shall not assign LBAs. The device server shall maintain the current logical block to
physical block alignment (see 4.6) for logical blocks not specified in the defect list.
Short block format address descriptors and long block format address descriptors should be in ascending
order. Bytes from index format address descriptors and physical sector format address descriptors shall be in
ascending order. If the address descriptors are not in the required order, then the device server may terminate
the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
5.4.2.2 Parameter list header
The parameter list headers (see table 42 and table 43) provide several optional format control parameters. If
the application client requests a function that is not implemented by the device server, then the device server
shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the LONGLIST bit is set to zero in the FORMAT UNIT CDB, then the short parameter list header (see table 42)
is used.
If the LONGLIST bit is set to one in the FORMAT UNIT CDB, then the long parameter list header (see table 43)
is used.
Table 42 — Short parameter list header
Bit
Byte
Reserved
PROTECTION FIELD USAGE
FOV
Format options bits
Obsolete
IMMED
Vendor
specific
DPRY
DCRT
STPF
IP
(MSB)
DEFECT LIST LENGTH
(LSB)
Table 43 — Long parameter list header
Bit
Byte
Reserved
PROTECTION FIELD USAGE
FOV
Format options bits
Obsolete
IMMED
Vendor
specific
DPRY
DCRT
STPF
IP
Reserved
P_I_INFORMATION
PROTECTION INTERVAL EXPONENT
(MSB)
DEFECT LIST LENGTH
•••
(LSB)


The combination (see table 44) of the PROTECTION FIELD USAGE field and the FMTPINFO field (see 5.4.1)
specifies the requested protection type (see 4.21.2).
Table 44 — FMTPINFO field and PROTECTION FIELD USAGE field (part 1 of 2)
Fields indicated by
the device server
Fields specified by the
application client
Description
SPT a
PROTECT b
FMTPINFO
PROTECTION
FIELD USAGE
xxxb
00b
000b
The logical unit shall be formatted to type 0
protection  c (see 4.21.2.2) resulting in the PROT_EN
bit d being set to zero and the P_TYPE field d being set
to 000b.
>000b
Illegal e
01b
xxxb
Illegal f
1xb
xxxb
Illegal f
xxxb
00b
000b
The logical unit shall be formatted to type 0
protection  c (see 4.21.2.2) resulting in the PROT_EN
bit d being set to zero and the P_TYPE field d being set
to 000b.
>000b
Illegal e
xxxb
01b
xxxb
Illegal f
000b
001b
011b
111b
10b
000b
The logical unit shall be formatted to type 1
protection  g (see 4.21.2.3) resulting in the PROT_EN
bit d being set to one and the P_TYPE field d being set
to 000b.
>000b
Illegal e
010b
100b
101b
10b
xxxb
Illegal f
000b
11b
xxxb
Illegal f
a See the Extended INQUIRY Data VPD page (see SPC-6) for the definition of the SPT field.
b See the standard INQUIRY data (see SPC-6) for the definition of the PROTECT bit.
c The device server shall format the medium to the logical block length specified in the mode parameter
block descriptor of the mode parameter header (see SPC-6).
d See the READ CAPACITY (16) parameter data (see 5.21.2) for the definition of the PROT_EN bit and
P_TYPE field.
e The device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
f
The device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
g The device server shall format the medium to the logical block length specified in the mode parameter
block descriptor of the mode parameter header plus eight bytes for each protection information interval
(e.g., if the logical block length is 2 048 and the PROTECTION INTERVAL EXPONENT field set to two, then
there are four 512 byte protection information intervals each followed by eight bytes of protection
information resulting in a formatted logical block length of 2 080 bytes). Following a successful format
operation, the PROT_EN  (see 5.21.2) indicates whether protection information (see 4.21) is enabled.


A format options valid (FOV) bit set to zero specifies that the device server shall use its default settings for the
functionality represented by the DPRY bit, the DCRT bit, the STPF bit, and IP bit (i.e., the format options bits). If
the FOV bit is set to zero, then the application client should set each of the format options bits to zero. If the
FOV bit is set to zero, and any of the format options bits are not set to zero, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
A FOV bit set to one specifies that the device server shall process the format options bits as follows:
a)
a disable primary (DPRY) bit:
A) set to zero specifies that the device server shall not assign LBAs to parts of the medium identified
as defective in the PLIST; or
B) set to one specifies that the device server shall not use the PLIST to identify defective areas of
the medium, and the PLIST shall not be deleted;
b)
a disable certification (DCRT) bit:
001b
010b
101b
111b
11b
000b
The logical unit shall be formatted to type 2
protection  g (see 4.21.2.4) resulting in the PROT_EN
bit d being set to one and the P_TYPE field d being set
to 001b.
001b
010b
11b
>000b
Illegal e
011b
100b
11b
000b
Illegal e
011b
100b
101b
111b
11b
001b
The logical unit shall be formatted to type 3
protection. g (see 4.21.2.5) resulting in the PROT_EN
bit d being set to one and the P_TYPE field d being set
to 010b.
>001b
Illegal e
110b
10b
11b
xxxb
Reserved
Table 44 — FMTPINFO field and PROTECTION FIELD USAGE field (part 2 of 2)
Fields indicated by
the device server
Fields specified by the
application client
Description
SPT a
PROTECT b
FMTPINFO
PROTECTION
FIELD USAGE
a See the Extended INQUIRY Data VPD page (see SPC-6) for the definition of the SPT field.
b See the standard INQUIRY data (see SPC-6) for the definition of the PROTECT bit.
c The device server shall format the medium to the logical block length specified in the mode parameter
block descriptor of the mode parameter header (see SPC-6).
d See the READ CAPACITY (16) parameter data (see 5.21.2) for the definition of the PROT_EN bit and
P_TYPE field.
e The device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
f
The device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
g The device server shall format the medium to the logical block length specified in the mode parameter
block descriptor of the mode parameter header plus eight bytes for each protection information interval
(e.g., if the logical block length is 2 048 and the PROTECTION INTERVAL EXPONENT field set to two, then
there are four 512 byte protection information intervals each followed by eight bytes of protection
information resulting in a formatted logical block length of 2 080 bytes). Following a successful format
operation, the PROT_EN  (see 5.21.2) indicates whether protection information (see 4.21) is enabled.


A) set to zero specifies that the device server shall perform a vendor specific medium certification
operation and add address descriptors for defects that it detects during the certification operation
to the GLIST; or
B) set to one specifies that the device server shall not perform any vendor specific medium certifi-
cation process or format verification operation;
c)
the stop format (STPF) bit controls the behavior of the device server if the device server has been
requested to use the PLIST (i.e., the DPRY bit is set to zero) or the GLIST (i.e., the CMPLST bit is set to
zero) and one or more of the following occurs:
A) list locate error: the device server is not able to locate a specified defect list or determine
whether a specified defect list exists; or
B) list access error: the device server encounters an error while accessing a specified defect list;
d)
a STPF bit set to zero specifies that:
A) if a list locate error or a list access error occurs, then the device server shall continue to process
the FORMAT UNIT command; and
B) after the format operation is complete, if:
a)
a list locate error and a list access error both occurred, then the device server shall terminate
the FORMAT UNIT command with CHECK CONDITION status at the completion of the
command with the sense key set to RECOVERED ERROR and the additional sense code set
to DEFECT LIST NOT FOUND or DEFECT LIST ERROR;
b)
a list locate error occurred and a list access error did not occur, then the device server shall
terminate the FORMAT UNIT command with CHECK CONDITION status with the sense key
set to RECOVERED ERROR with the additional sense code set to DEFECT LIST NOT
FOUND; and
c)
a list access error occurred and a list locate error did not occur, then the device server shall
terminate the FORMAT UNIT command with CHECK CONDITION status with the sense key
set to RECOVERED ERROR with the additional sense code set to DEFECT LIST ERROR;
e)
a STPF bit set to one specifies that:
A) if a list locate error occurs, then the device server shall terminate the FORMAT UNIT command
with CHECK CONDITION status with the sense key set to MEDIUM ERROR and the additional
sense code set to either DEFECT LIST NOT FOUND; or
B) if a list access error occurs, then the device server shall terminate the FORMAT UNIT command
with CHECK CONDITION status with the sense key set to MEDIUM ERROR with the additional
sense code set to DEFECT LIST ERROR;
and
f)
an initialization pattern (IP) bit:
A) set to zero specifies that an initialization pattern descriptor (see 5.4.2.3) is not included and that
the device server shall use its default initialization pattern; or
B) set to one specifies that:
a)
an initialization pattern descriptor is included in the FORMAT UNIT parameter list following
the parameter list header; and
b)
if the device server does not support initialization pattern descriptors, then the device server
shall terminate the FORMAT UNIT command with CHECK CONDITION status with the sense
key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
An immediate (IMMED) bit set to zero specifies that the device server shall return status after the format
operation has completed. An IMMED bit set to one specifies that the device server shall return status after the
entire parameter list has been transferred.
The P_I_INFORMATION field, if any (i.e., if the long parameter list header is used), should be set to 0h. If the
P_I_INFORMATION field is not set to zero, then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
For a type 0 or a type 1 protection information request, if the PROTECTION INTERVAL EXPONENT field, if any, is
not set to 0h, then the device server shall terminate the command with CHECK CONDITION status with the


sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
For a type 2 protection or a type 3 protection format request, the protection interval exponent determines the
length of user data to be transferred before protection information is transferred (i.e., the protection
information interval).
The protection information interval is calculated as follows:
protection information interval = logical block length ÷ 2(protection interval exponent)
where:
logical block length
is the number of bytes of user data in a logical block (see 4.5)
protection interval exponent
is zero if the short parameter list header (see table 42) is used or the
contents of the PROTECTION INTERVAL EXPONENT field if the long parameter list
header (see table 43) is used
If the protection information interval calculates to a value that is not an even number (e.g., 520 ÷ 23 = 65) or
not a whole number (e.g., 520 ÷ 24 = 32.5 and 520 ÷ 210 = 0.508), then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
The DEFECT LIST LENGTH field specifies the total length in bytes of the defect list (i.e., the address descriptors)
that follow and does not include the length of the initialization pattern descriptor, if any. The formats for the
address descriptor(s) are shown in 6.2.
5.4.2.3 Initialization pattern descriptor
The initialization pattern descriptor specifies that the device server initialize logical blocks to a specified
pattern. The initialization pattern descriptor (see table 45) is transferred to the device server as part of the
FORMAT UNIT parameter list.
A security initialize (SI) bit set to one specifies that the device server shall attempt to write the initialization
pattern to all areas of the medium including those that may have been reassigned (i.e., are in a defect list). An
SI bit set to one specifies that the device server shall ignore:
a)
the FMTPINFO field;
b)
the CMPLIST bit;
c)
the DEFECT LIST FORMAT field;
d)
all the bits and fields in the parameter list header, except the IMMED bit; and
e)
any defect list data.
Table 45 — Initialization pattern descriptor
Bit
Byte
Obsolete
SI
Reserved
INITIALIZATION PATTERN TYPE
(MSB)
INITIALIZATION PATTERN LENGTH (n - 3)
(LSB)
INITIALIZATION PATTERN
•••
n
