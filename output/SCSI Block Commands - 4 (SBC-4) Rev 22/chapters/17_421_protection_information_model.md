# 4.21 Protection information model

If this state was entered with a Transitioning From Stopped argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero, that the device server is able to process and
complete while in the SSU_PC8:Stopped state; and
b)
if the CCF STOPPED field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server terminates any TEST UNIT READY command or logical block access
command, with CHECK CONDITION status, with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
4.20.5.11.2 Transition SSU_PC9:Standby_Wait to SSU_PC3:Standby
This transition shall occur when the logical unit meets the requirements for being in the:
a)
standby_y power condition, if this state was entered with a Transitioning To Standby_y argument; or
b)
standby_z power condition, if this state was entered with a Transitioning To Standby_z argument.
4.20.5.12 SSU_PC10:Wait_Stopped state
4.20.5.12.1 SSU_PC10:Wait_Stopped state description
While in this state:
a)
the device server shall provide power management pollable sense data (see SPC-6) with the sense
key set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION;
b)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero (see 5.31), that the device server is able to
process and complete in the SSU_PC8:Stopped state;
c)
the logical unit is performing the operations required for it to be in the SSU_PC8:Stopped state (e.g., a
disk drive spins down its medium); and
d)
the device server shall terminate any TEST UNIT READY command or logical block access
command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT NOT READY, INITIALIZING COMMAND REQUIRED.
4.20.5.12.2 Transition SSU_PC10:Wait_Stopped to SSU_PC8:Stopped
This transition shall occur when:
a)
the logical unit meets the requirements for being in the SSU_PC8:Stopped state.
4.21 Protection information model
4.21.1 Protection information overview
The protection information model provides for protection of user data while user data is being transferred
between a sender and a receiver. Protection information is generated at the application layer and may be
checked by any object associated with the I_T_L nexus (see SAM-6). Once received, protection information is
retained (e.g., written to the medium, stored in non-volatile memory, or recalculated on read back) by the
device server until overwritten. Power loss, hard reset, logical unit reset, and I_T nexus loss shall have no
effect on the retention of protection information.
Support for protection information shall be indicated in the PROTECT bit in the standard INQUIRY data (see
SPC-6).
If the logical unit is formatted with protection information, and the EMDP bit is set to one in the
Disconnect-Reconnect mode page (see SPC-6), then checking of the logical block reference tag within a


service delivery subsystem without accounting for modified data pointers and data alignments may cause
false errors when logical blocks are transmitted out of order.
Protection information is also referred to as the data integrity field (DIF).
4.21.2 Protection types
4.21.2.1 Protection types overview
The content of protection information is dependent on the type of protection to which a logical unit has been
formatted.
The type of protection supported by the logical unit shall be indicated in the SPT field in the Extended INQUIRY
Data VPD page (see SPC-6). The current protection type shall be indicated in the P_TYPE field (see 5.21.2).
An application client may format the logical unit to a specific type of protection using the FMTPINFO field and the
PROTECTION FIELD USAGE field (see 5.4).
An application client may format the logical unit to place protection information at intervals other than on
logical block boundaries using the PROTECTION INTERVAL EXPONENT field.
A medium access command is processed in a different manner by a device server depending on the type of
protection in effect. When used in relation to types of protection, the term “medium access command” is
defined as any one of the following commands:
a)
COMPARE AND WRITE;
b)
ORWRITE (16);
c)
ORWRITE (32);
d)
READ (10);
e)
READ (12);
f)
READ (16);
g)
READ (32);
h)
VERIFY (10);
i)
VERIFY (12);
j)
VERIFY (16);
k)
VERIFY (32);
l)
WRITE (10);
m) WRITE (12);
n)
WRITE (16);
o)
WRITE (32);
p)
WRITE AND VERIFY (10);
q)
WRITE AND VERIFY (12);
r)
WRITE AND VERIFY (16);
s)
WRITE AND VERIFY (32);
t)
WRITE ATOMIC (16);
u)
WRITE ATOMIC (32);
v)
WRITE SAME (10);
w) WRITE SAME (16);
x)
WRITE SAME (32);
y)
WRITE SCATTERED (16);
z)
WIRITE SCATTERED (32);
aa) WRITE STREAM (16); and
ab) WRITE STREAM (32).
4.21.2.2 Type 0 protection
Type 0 protection defines no protection over that which is defined within the transport protocol.


A logical unit that has been formatted with protection information disabled (see 5.3) or a logical unit that does
not support protection information (i.e., the PROTECT bit set to zero in the standard INQUIRY data (see
SPC-6)) has type 0 protection.
If type 0 protection is enabled and the RDPROTECT field, the WRPROTECT field, the VRPROTECT field, or the
ORPROTECT field is set to a non-zero value, then medium access commands are invalid and may be
terminated by the device server with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If type 0 protection is enabled, then the following medium access commands are invalid and shall be
terminated by the device server with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID COMMAND OPERATION CODE:
a)
READ (32);
b)
VERIFY (32);
c)
WRITE (32);
d)
WRITE AND VERIFY (32);
e)
WRITE ATOMIC (32);
f)
WRITE SAME (32);
g)
WRITE SCATTERED (32); and
h)
WRITE STREAM (32).
4.21.2.3 Type 1 protection
Type 1 protection:
a)
defines the content of each LOGICAL BLOCK GUARD field;
b)
does not define the content of any LOGICAL BLOCK APPLICATION TAG field; and
c)
defines the content of each LOGICAL BLOCK REFERENCE TAG field.
If type 1 protection is enabled, then the following medium access commands are invalid and shall be
terminated by the device server with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID COMMAND OPERATION CODE:
a)
READ (32);
b)
VERIFY (32);
c)
WRITE (32);
d)
WRITE AND VERIFY (32);
e)
WRITE ATOMIC (32);
f)
WRITE SAME (32);
g)
WRITE SCATTERED (32); and
h)
WRITE STREAM (32).
For valid medium access commands in which the RDPROTECT field, the WRPROTECT field, the VRPROTECT field,
or the ORPROTECT field is set to:
a)
zero, the Data-In Buffer and/or Data-Out Buffer associated with those commands shall consist of
logical block data containing only user data; or
b)
a non-zero value, the Data-In Buffer and/or Data-Out Buffer shall consist of logical block data
containing both user data and protection information.
4.21.2.4 Type 2 protection
Type 2 protection:
a)
defines the content of each LOGICAL BLOCK GUARD field;
b)
does not define the content of any LOGICAL BLOCK APPLICATION TAG field; and
c)
defines, except for the first logical block addressed by the command, the content of each LOGICAL
BLOCK REFERENCE TAG field.
If type 2 protection is enabled and the RDPROTECT field, the WRPROTECT field, the VRPROTECT field, or the
ORPROTECT field is set to a non-zero value, then the following medium access commands are invalid and shall


be terminated by the device server with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID COMMAND OPERATION CODE:
a)
COMPARE AND WRITE;
b)
ORWRITE (16);
c)
ORWRITE (32);
d)
READ (10);
e)
READ (12);
f)
READ (16);
g)
VERIFY (10);
h)
VERIFY (12);
i)
VERIFY (16);
j)
WRITE (10);
k)
WRITE (12);
l)
WRITE (16);
m) WRITE AND VERIFY (10);
n)
WRITE AND VERIFY (12);
o)
WRITE AND VERIFY (16);
p)
WRITE ATOMIC (16);
q)
WRITE SAME (10);
r)
WRITE SAME (16);
s)
WRITE SCATTERED (16); and
t)
WRITE STREAM (16).
For valid medium access commands in which the RDPROTECT field, the WRPROTECT field, the VRPROTECT field,
or the ORPROTECT field is set to:
a)
zero, the Data-In Buffer and/or Data-Out Buffer associated with those commands shall consist of
logical block data containing only user data; or
b)
a non-zero value, the Data-In Buffer and/or Data-Out Buffer shall consist of logical block data
containing both user data and protection information.
4.21.2.5 Type 3 protection
Type 3 protection:
a)
defines the content of each LOGICAL BLOCK GUARD field;
b)
does not define the content of any LOGICAL BLOCK APPLICATION TAG field; and
c)
does not define the content of any LOGICAL BLOCK REFERENCE TAG field.
If type 3 protection is enabled, then the following medium access commands are invalid and shall be
terminated by the device server with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID COMMAND OPERATION CODE:
a)
READ (32);
b)
VERIFY (32);
c)
WRITE (32);
d)
WRITE AND VERIFY (32);
e)
WRITE ATOMIC (32);
f)
WRITE SAME (32);
g)
WRITE SCATTERED (32); and
h)
WRITE STREAM (32).
For valid medium access commands in which the RDPROTECT field, the WRPROTECT field, the VRPROTECT field,
or the ORPROTECT field is set to:
a)
zero, the Data-In Buffer and/or Data-Out Buffer associated with those commands shall consist of
logical block data containing only user data; or
b)
a non-zero value, the Data-In Buffer and/or Data-Out Buffer shall consist of logical block data
containing both user data and protection information.


4.21.3 Protection information format
Table 22 defines the placement of protection information in a logical block with a single protection information
interval (i.e., the PROTECTION INTERVAL EXPONENT field is set to zero in the parameter list header for a FORMAT
UNIT command (see 5.4.2.2))
.
Table 22 — Logical block data format with a single protection information interval
Bit
Byte
USER DATA
•••
n - 1
n
(MSB)
LOGICAL BLOCK GUARD
n + 1
(LSB)
n + 2
(MSB)
LOGICAL BLOCK APPLICATION TAG
n + 3
(LSB)
n + 4
(MSB)
 LOGICAL BLOCK REFERENCE TAG
•••
n + 7
(LSB)


Table 23 shows an example of the placement of protection information in a logical block with more than one
protection information interval (i.e., the PROTECTION INTERVAL EXPONENT field is set to a non-zero value in the
parameter list header for a FORMAT UNIT command (see 5.4.2.2)).
Each USER DATA field shall contain user data.
Table 23 — An example of the logical block data for a logical block with more than one protection
information interval
Bit
Byte
USER DATA [first]
•••
n - 1
n
(MSB)
LOGICAL BLOCK GUARD [first]
n + 1
(LSB)
n + 2
(MSB)
LOGICAL BLOCK APPLICATION TAG [first]
n + 3
(LSB)
n + 4
(MSB)
 LOGICAL BLOCK REFERENCE TAG [first]
•••
n + 7
(LSB)
n + 8
USER DATA [second]
•••
m - 1
m
(MSB)
LOGICAL BLOCK GUARD [second]
m + 1
(LSB)
m + 2
(MSB)
LOGICAL BLOCK APPLICATION TAG [second]
m + 3
(LSB)
m + 4
(MSB)
 LOGICAL BLOCK REFERENCE TAG [second]
•••
m + 7
(LSB)
•••
USER DATA [last]
•••
z - 1
z
(MSB)
LOGICAL BLOCK GUARD [last]
z + 1
(LSB)
z + 2
(MSB)
LOGICAL BLOCK APPLICATION TAG [last]
z + 3
(LSB)
z + 4
(MSB)
 LOGICAL BLOCK REFERENCE TAG [last]
•••
z + 7
(LSB)


Each LOGICAL BLOCK GUARD field contains a CRC (see 4.21.4). Only the contents of the USER DATA field
immediately preceding THE LOGICAL BLOCK GUARD field (i.e., the user data between the preceding logical block
reference tag, if any, and the current logical block guard) shall be used to generate and check the CRC
contained in the LOGICAL BLOCK GUARD field.
Each LOGICAL BLOCK APPLICATION TAG field is set by the application client. If the device server detects a:
a)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 1 protection (see 4.21.2.3) is enabled;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh and type 2 protection (see 4.21.2.4) is enabled; or
c)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh, LOGICAL BLOCK REFERENCE TAG field set to
FFFF_FFFFh, and type 3 protection (see 4.21.2.5) is enabled,
then the device server disables checking of all protection information for the associated protection information
interval when performing:
a)
a read operation; and
b)
a write operation if the NO_PI_CHK bit is set to one in the Extended INQUIRY Data VPD page (see
SPC-6).
Otherwise, if the ATMPE bit in the Control mode page (see SPC-6) is:
a)
set to one, then the logical block application tags are defined by the Application Tag mode page
(see 6.5.3); or
b)
set to zero, then the logical block application tags are not defined by this standard.
The LOGICAL BLOCK APPLICATION TAG field may be modified by a device server if the ATO bit is set to zero in the
Control mode page (see SPC-6). If the ATO bit is set to one in the Control mode page, then the device server
shall not modify the LOGICAL BLOCK APPLICATION TAG field.
The contents of a LOGICAL BLOCK APPLICATION TAG field shall not be used to generate or check the CRC
contained in the LOGICAL BLOCK GUARD field.
Table 24 indicates the value that shall be contained in the first LOGICAL BLOCK REFERENCE TAG field of the first
logical block:
a)
in the Data-In Buffer and/or Data-Out Buffer for commands other than WRITE SCATTERED
commands;
b)
in the Data-Out buffer for each LBA range (see 4.35) for WRITE SCATTERED (16) commands
(see 5.55); or
c)
in the Data-Out buffer for each LBA range (see 4.35) for WRITE SCATTERED (32) commands
(see 5.56).


.
Subsequent LOGICAL BLOCK REFERENCE TAG fields for a logical block in the Data-In Buffer and/or Data-Out
Buffer shall be set as specified in table 25.
The contents of a LOGICAL BLOCK REFERENCE TAG field shall not be used to generate or check the CRC
contained in the LOGICAL BLOCK GUARD field.
Table 24 — Content of the first LOGICAL BLOCK REFERENCE TAG field
Protection Type
Content of the first LOGICAL BLOCK REFERENCE TAG field a
Type 1 b
protection
(see 4.21.2.3)
The least significant four bytes of the LBA contained in the LOGICAL BLOCK ADDRESS
field of the CDB for medium access commands (see 4.21.2.1) other than WRITE
SCATTERED (16) commands (see 5.55).
The least significant four bytes of the LBA contained in the LOGICAL BLOCK ADDRESS
field of the associated LBA range descriptor for WRITE SCATTERED (16) commands..
Type 2 protection
(see 4.21.2.4)
The value in the EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG field of the CDB for
medium access commands other than WRITE SCATTERED (32) commands
(see 5.56).
The value in the EXPECTED INITIAL LOGICAL BLOCK REFERENCE TAG field of the
associated LBA range descriptor for WRITE SCATTERED (32) commands.
Type 3 protection
(see 4.21.2.5)
Not defined in this standard. If the ATO bit is set to zero in the Control mode page (see
SPC-6), then this field may be modified by the device server. If the ATO bit is set to one
in the Control mode page, then the device server shall not modify this field.
a The first logical block in the Data-In buffer and/or Data-Out Buffer for media access commands other
than WRITE SCATTERED commands or the first logical block in each LBA range in the Data-Out buffer
for WRITE SCATTERED commands
b The length of the protection information interval is equal to the logical block length (see 5.4.2).
Table 25 — Content of subsequent LOGICAL BLOCK REFERENCE TAG fields for a logical block in the
Data-In Buffer and/or Data-Out Buffer
Protection Type
The content of subsequent LOGICAL BLOCK REFERENCE TAG fields in the Data-In
Buffer and/or Data-Out Buffer
Type 1 protection
(see 4.21.2.3) and
Type 2 protection
(see 4.21.2.4)
The previous logical block reference tag plus one. If the contents of the previous
LOGICAL BLOCK REFERENCE TAG field is FFFF_FFFFh, then the contents of the
subsequent LOGICAL BLOCK REFERENCE TAG field is 0000_0000h.
Type 3 protection
(see 4.21.2.5)
Not defined in this standard. If the ATO bit is set to zero in the Control mode page (see
SPC-6), then this field may be modified by the device server. If the ATO bit is set to
one in the Control mode page, then the device server shall not modify this field.


4.21.4 Logical block guard
4.21.4.1 Logical block guard overview
A LOGICAL BLOCK GUARD field shall contain a CRC that is generated from the contents of only the USER DATA
field immediately preceding the LOGICAL BLOCK GUARD field.
Table 26 defines the CRC polynomials used to generate the logical block guard from the contents of the USER
DATA field.
4.21.4.2 CRC generation
The equations that are used to generate the CRC from F(x) are as follows. All arithmetic is modulo 2.
The transmitter shall calculate the CRC by appending 16 zeros to F(x) and dividing by G(x) to obtain the
remainder R(x):
R(x) is the CRC value, and is transmitted in the LOGICAL BLOCK GUARD field.
Table 26 — CRC polynomials
Function
Definition
F(x)
A polynomial representing the transmitted USER DATA field, which is covered by the CRC. For
the purposes of the CRC, the coefficient of the highest order term shall be byte zero bit seven
of the USER DATA field and the coefficient of the lowest order term shall be bit zero of the last
byte of the USER DATA field.
F’(x)
A polynomial representing the received USER DATA field.
G(x)
The generator polynomial:
G(x) = x16 + x15 + x11 + x9 + x8 + x7 + x5 + x4 + x2 + x + 1
(i.e., in finite field notation G(x) = 1_8BB7h)
R(x)
The remainder polynomial calculated during CRC generation by the transmitter, representing
the transmitted LOGICAL BLOCK GUARD field.
R’(x)
A polynomial representing the received LOGICAL BLOCK GUARD field.
RB(x)
The remainder polynomial calculated during CRC checking by the receiver.
RB(x) = 0 indicates no error was detected.
RC(x)
The remainder polynomial calculated during CRC checking by the receiver.
RC(x) = 0 indicates no error was detected.
QA(x)
The quotient polynomial calculated during CRC generation by the transmitter. The value of
QA(x) is not used.
QB(x)
The quotient polynomial calculated during CRC checking by the receiver. The value of QB(x)
is not used.
QC(x)
The quotient polynomial calculated during CRC checking by the receiver. The value of QC(x)
is not used.
M(x)
A polynomial representing the transmitted USER DATA field followed by the transmitted
LOGICAL BLOCK GUARD field.
M’(x)
A polynomial representing the received USER DATA field followed by the received LOGICAL
BLOCK GUARD field.
x16
F x




G x

------------------------------
QA x

R x

G x

------------
+
=


M(x) is the polynomial representing the USER DATA field followed by the LOGICAL BLOCK GUARD field (i.e., F(x)
followed by R(x)):
M(x) = (x16 × F(x)) + R(x)
4.21.4.3 CRC checking
M’(x) (i.e., the polynomial representing the received USER DATA field followed by the received LOGICAL BLOCK
GUARD field) may differ from M(x) (i.e., the polynomial representing the transmitted USER DATA field followed by
the transmitted LOGICAL BLOCK GUARD field) if there are transmission errors.
The receiver may check M’(x) validity by appending 16 zeros to F’(x) and dividing by G(x) and comparing the
calculated remainder RB(x) to the received CRC value R’(x):

In the absence of errors in F’(x) and R’(x), the remainder RB(x) is equal to R’(x).
The receiver may check M’(x) validity by dividing M’(x) by G(x) and comparing the calculated remainder RC(x)
to zero:
In the absence of errors in F’(x) and R’(x), the remainder RC(x) is equal to zero.
Both methods of checking M’(x) validity are mathematically equivalent.
4.21.4.4 CRC test cases
Several CRC test cases are shown in table 27.
4.21.5 Application of protection information
Before an application client transmits or receives logical block data with protection information, the application
client:
1)
determines if a logical unit supports protection information using the INQUIRY command (see the
PROTECT bit in the standard INQUIRY data in SPC-6);
2)
if protection information is supported, then determines if the logical unit is formatted to accept
protection information using the READ CAPACITY (16) command (e.g., see the PROT_EN bit and the
P_TYPE field (see 5.21.2)); and
3)
if the logical unit supports protection information and is not formatted to accept protection information,
then formats the logical unit (see 5.4) with protection information enabled.
Table 27 — CRC test cases
Pattern
CRC
32 bytes each set to 00h
0000h
32 bytes each set to FFh
A293h
32 bytes of an incrementing pattern from 00h to 1Fh
0224h
2 bytes each set to FFh followed by 30 bytes set to 00h
21B8h
32 bytes of a decrementing pattern from FFh to E0h
A0B7h
x16
F

x



G x

--------------------------------
QB x

RB x

G x

----------------
+
=
M' x

G x

-------------
QC x

RC x

G x

----------------
+
=


If the logical unit supports protection information and is formatted to accept protection information, then the
application client may use read commands that support protection information and should use verify
commands and write commands that support protection information.
4.21.6 Protection information and commands
The enabling of protection information enables fields in medium access commands that instruct the device
server on the handling of protection information. The detailed definitions of each command’s protection
information fields are in the individual command descriptions.
The commands that are affected while protection information is enabled are listed in table 34.
Commands that cause a device server to return the length in bytes of each logical block (e.g., the MODE
SENSE (10) command and the READ CAPACITY (16) command) shall cause the device server to return the
combined length of the USER DATA field(s) contained in the logical block, not including the length of any
protection information (i.e., the LOGICAL BLOCK GUARD field(s), the LOGICAL BLOCK APPLICATION TAG field(s), and
the LOGICAL BLOCK REFERENCE TAG field(s)) (e.g., if the user data plus the protection information is equal to 520
bytes and there is one protection information interval, then 512 is returned).
4.22 Grouping function
4.22.1 Grouping function overview
A grouping function is a function that collects information about attributes associated with commands (i.e.,
information about commands with the same group value are collected into the specified group). The definition
of the attributes and the groups is not defined by this standard. Groups are identified with the GROUP NUMBER
field in the CDBs of certain commands (e.g., the PRE-FETCH (10) command (see 5.13)).
Support for the grouping function is indicated in the GROUP_SUP bit in the Extended INQUIRY Data VPD page
(see SPC-6).
The collection of this information is not defined by this standard (e.g., the information may not be transmitted
using any SCSI protocols).
EXAMPLE - In a SCSI domain in which two applications are using a subsystem where one application streams data and
another accesses data randomly, if:
a)the streaming application groups all of its commands with one group number (e.g., x); and
b)the random application groups all of its commands with another group number (e.g., y),
then the applications use those group numbers (e.g., x and y) to collect separate performance metrics for each
application.
A management application then reads the performance metrics and determines if the performance of a specific
group is acceptable.
Device servers that support the grouping function shall support at least group 0 to group 31.
4.22.2 Grouping function extensions for IO advice hints
The IO Advice Hints Grouping mode page (see 6.5.7) may be used to enable or disable the collection of
information, and define the IO advice hints associated with each group. The IO Advice Hints Grouping mode
page contains 64 IO advice hints group descriptors (i.e., one descriptor for each possible group number) (see
table 243) that are in ascending order of group number. The IO advice hints group number associated with
each IO advice hints group descriptor is calculated as follows:
IO advice hints group number = ( offset /16 ) -1
where:
