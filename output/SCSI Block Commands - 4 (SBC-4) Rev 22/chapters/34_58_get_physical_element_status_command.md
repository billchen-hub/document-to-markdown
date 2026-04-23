# 5.8 GET PHYSICAL ELEMENT STATUS command

5.8 GET PHYSICAL ELEMENT STATUS command
5.8.1 GET PHYSICAL ELEMENT STATUS command overview
The GET PHYSICAL ELEMENT STATUS command (see table 56) requests that the device server return
status information for physical elements within the logical unit.
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 56 for the GET PHYSICAL ELEMENT STATUS command.
The STARTING ELEMENT field specifies the element identifier of the first physical element addressed by this
command.
The ALLOCATION LENGTH field is defined in SPC-6. In response to a GET PHYSICAL ELEMENT STATUS
command, the device server may send less data to the Data-In Buffer than is specified by the allocation
length. If, in response to a GET PHYSICAL ELEMENT STATUS command, the device server does not send
sufficient data to the Data-In Buffer to satisfy the requirement of the application client, then, to retrieve
additional information, the application client may send additional GET PHYSICAL ELEMENT STATUS
commands with different starting element values.
Table 56 — GET PHYSICAL ELEMENT STATUS command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (17h)
Reserved
•••
(MSB)
STARTING ELEMENT
•••
(LSB)
(MSB)
ALLOCATION LENGTH
•••
(LSB)
FILTER
Reserved
REPORT TYPE
CONTROL


The FILTER field restricts the physical element status descriptors to return, as shown in table 57.
The REPORT TYPE field specifies the type of physical element status descriptors to return as shown in table 58.
The CONTROL byte is defined in SAM-6.
Table 57 — FILTER field
Code
Description
00b
All physical status descriptors as specified by the other fields in the CDB.
01b
Only physical element status descriptors for which the value of the PHYSICAL
ELEMENT HEALTH field (see 5.8.2.2) is:
a)
greater than or equal to 65h and less than or equal to CFh (i.e., outside
manufacturer’s specification limit);
b)
equal to FDh (i.e., all operations associated with storage element
depopulation have completed and one or more completed with error);
c)
equal to FEh (i.e., an operation associated with storage element
depopulation is in progress); or
d)
equal to FFh (i.e., all operations associated with storage element
depopulation have completed without error).
all others
Reserved
Table 58 — REPORT TYPE field
Code
Description
0h
Return descriptors for physical elements, based on the FILTER field
1h
Return descriptors for storage elements, based on the FILTER field
all others
Reserved


5.8.2 GET PHYSICAL ELEMENT STATUS parameter data
5.8.2.1 GET PHYSICAL ELEMENT STATUS parameter data overview
The GET PHYSICAL ELEMENT STATUS parameter data (see table 59) contains a 32-byte header followed
by zero or more physical element status descriptors.
The NUMBER OF DESCRIPTORS field shall contain the number of descriptors in the element descriptors list. The
element descriptors list is a list of physical elements that:
a)
meet the requirements of the REPORTING OPTIONS field;
b)
meet the requirements of the FILTER field; and
c)
have an element identifier that is greater than or equal to the element identifier specified by the
STARTING ELEMENT field in the CDB.
The contents of the NUMBER OF DESCRIPTORS field are not altered based on the allocation length.
The NUMBER OF DESCRIPTORS RETURNED field contains the number of valid physical element status descriptors
returned in the parameter data.
The IDENTIFIER OF ELEMENT BEING DEPOPULATED field contains the element identifier of the element that has a
physical element health set to FEh (i.e., an operation associated with storage element depopulation is in
progress). If the value of this field is set to zero, then no operation associated with storage element
depopulation is in progress.
Table 59 — GET PHYSICAL ELEMENT STATUS parameter data
Bit
Byte
(MSB)
NUMBER OF DESCRIPTORS
•••
(LSB)
(MSB)
NUMBER OF DESCRIPTORS RETURNED
•••
(LSB)
(MSB)
IDENTIFIER OF ELEMENT BEING DEPOPULATED
•••
(LSB)
Reserved
•••
Physical element status descriptor list
Physical element status descriptor [first] (see 5.8.2.2)
•••
•••
n - 32
Physical element status descriptor [last] (see 5.8.2.2)
•••
n


As a result of processing considerations not defined by this standard, two GET PHYSICAL ELEMENT
STATUS commands with identical values in all CDB fields may result in two different values in the NUMBER OF
DESCRIPTORS field.
The physical element status descriptors shall be sorted in ascending order of the element identifier.
5.8.2.2 Physical element status descriptor
The physical element status descriptor (see table 60) contains status information for a physical element.
The ELEMENT IDENTIFIER field contains the non-zero identifier of the physical element (e.g., storage element)
associated with this physical element status descriptor.
A restoration allowed (RALWD) bit set to one indicates that this storage element has been depopulated and is a
candidate for being restored. A RALWD bit set to zero indicates that this storage element:
a)
has not been depopulated; or
b)
has been depopulated and is not a candidate for being restored.
The PHYSICAL ELEMENT TYPE field indicates the type of the physical element associated with this physical
element status descriptor, as described in table 61.
Table 60 — Physical element status descriptor format
Bit
Byte
Reserved
•••
(MSB)
ELEMENT IDENTIFIER
•••
(LSB)
Reserved
•••
Reserved
RALWD
PHYSICAL ELEMENT TYPE
PHYSICAL ELEMENT HEALTH
(MSB)
ASSOCIATED CAPACITY
•••
(LSB
Reserved
•••
Table 61 — PHYSICAL ELEMENT TYPE field
Code
Description
01h
Storage element
all others
Reserved
