# 4.27 ORWRITE commands

If reporting of referrals in sense data is disabled (see 4.26.1), the device server receives a command for which
the device server is not able to access user data associated with the requested command, and the
inaccessible user data is accessible through another target port group, then the device server shall terminate
the command with CHECK CONDITION status with the sense key set to HARDWARE ERROR and the
additional sense code set to INTERNAL TARGET FAILURE.
4.27 ORWRITE commands
4.27.1 ORWRITE commands overview
The ORWRITE commands (see 5.10 and 5.11) provide a mechanism for an application client to manipulate
bitmap structures on direct access block devices.
An ORWRITE command shall be processed by the device server performing the following as an uninterrupted
sequence of actions (see 4.25):
1)
perform read operations from the LBAs specified by this command;
2)
transfer the specified number of logical blocks from the Data-Out Buffer;
3)
perform the specified Boolean arithmetic function on:
A) the user data contained in the logical blocks from read operations; and
B) the user data contained in the logical blocks transferred from the Data-Out Buffer;
4)
store the results of the Boolean arithmetic function in a bitmap buffer;
5)
generate new protection information, if any, from the stored results;
6)
store the generated protection information, if any, into the bitmap buffer; and
7)
perform write operations using the updated logical block data from the bitmap buffer.
If the check of the protection information from the read operations is successful (see table 67), and the check
of the protection information transferred from the Data-Out Buffer is successful (see table 68), then the device
server shall generate the new protection information (see 4.21) as follows:
a)
set the LOGICAL BLOCK GUARD field to the CRC (see 4.21.4) generated from the bitmap buffer by the
device server;
b)
set the LOGICAL BLOCK REFERENCE TAG field to the LOGICAL BLOCK REFERENCE TAG field received from
the Data-Out Buffer; and
c)
set the LOGICAL BLOCK APPLICATION TAG field to the LOGICAL BLOCK APPLICATION TAG field received from
the Data-Out Buffer.
In order to support the manipulation of bitmap structures:
a)
the ORWRITE (16) command supports the set operation (see 4.27.4); and
b)
the ORWRITE (32) command supports:
A) the set operation; and
B) the change generation and clear operation (see 4.27.3).
4.27.2 ORWgeneration code
4.27.2.1 ORWgeneration code overview
The ORWRITE commands use a generation code for synchronization. The device server shall establish and
maintain the following generation codes:
a)
a current ORWgeneration code; and
b)
a previous ORWgeneration code.
Subsequent ORWRITE command processing by the device server is dependent on comparisons involving the
ORWgeneration codes. Changes in these ORWgeneration codes define a synchronization point in the
management of the bitmap.


4.27.2.2 ORWgeneration code processing
The device server shall maintain at least one current ORWRITE processing policy. The device server may
support more than one ORWRITE processing policy (see table 29 in 4.27.4).
When processing an ORWRITE (32) command (see 5.11), the device server compares the value in the
EXPECTED ORWGENERATION field in the CDB to the current ORWgeneration code (see 4.27.2.1), and:
a)
if the two values are equal, then the device server continues processing the ORWRITE (32)
command as described in table 29 for the set operation and as described in 4.27.3 for the change
generation and clear operation; or
b)
if the two values are not equal, then:
A) for a set operation, the current ORWRITE processing policy (see table 29) determines how the
device server continues processing the ORWRITE (32) command; and
B) for a change generation and clear operation, the device server terminates the ORWRITE (32)
command (see 4.27.3).
If the device server supports both the ORWRITE (16) command (see 5.10) and the ORWRITE (32) command,
then the device server shall process all ORWRITE (16) commands as if they contained an EXPECTED
ORWGENERATION field set to zero.
4.27.3 Change generation and clear operation
The change generation portion of the change generation and clear operation is used to establish a point of
synchronization. The clear portion of the change generation and clear operation is used to set zero or more
bits in the bitmap structure to zero.
The device server performs a change generation and clear operation if:
a)
the BMOP field (see 5.11) is set to 001b; and
b)
the value in the EXPECTED ORWGENERATION field is equal to the current ORWgeneration code in the
device server.
If the device server performs a change generation and clear operation, then the device server shall perform
the following as an uninterrupted sequence:
1)
perform read operations from the LBAs specified by this command;
2)
transfer the specified logical blocks from the Data-Out Buffer;
3)
perform an AND operation (see 3.1.4) on the user data contained in the logical blocks from the read
operations and the user data contained in the logical blocks transferred from the Data-Out Buffer;
4)
store the results of the AND operation in a bitmap buffer;
5)
generate new protection information, if any, from the stored results;
6)
store the generated protection information, if any, into the bitmap buffer;
7)
perform write operations using the updated logical block data from the bitmap buffer;
8)
set the current ORWRITE processing policy to the value in the PREVIOUS GENERATION PROCESSING
field (see 5.11);
9)
set the previous ORWgeneration code (see 4.27.2) to the current ORWgeneration code in the device
server; and
10) set the current ORWgeneration code (see 4.27.2) to the value in the NEW ORWGENERATION
field(see 5.11).
If the value in the EXPECTED ORWGENERATION field is not equal to the current ORWgeneration code, then the
device server shall terminate the ORWRITE (32) command with CHECK CONDITION status with the sense
key set to ILLEGAL REQUEST and the additional sense code set to ORWRITE GENERATION DOES NOT
MATCH.
If a power on or hard reset condition occurs, then the device server shall set:
a)
the current ORWgeneration code to zero;
b)
the previous ORWgeneration code to zero; and
c)
the current ORWRITE processing policy to 7h.


The device server shall preserve the following across a logical unit reset:
a)
the current ORWgeneration code;
b)
the previous ORWgeneration code; and
c)
the current ORWRITE processing policy.
4.27.4 Set operation
The set operation is used to set zero or more bits in the bitmap structure to one.
The device server performs a set operation for an ORWRITE command (see 5.10 and 5.11) if the BMOP field in
the CDB is set to 000b.
The device server shall perform a set operation by performing the actions specified in table 29, which shows
the current ORWgeneration code, the previous ORWgeneration code, and the device server’s current
ORWRITE processing policy (see 4.27.3).
Table 29 — Performing an ORWRITE set operation
Current ORWRITE
processing policy
The value in the EXPECTED ORWGENERATION field matches
 Current
ORWgeneration code
 Previous
ORWgeneration code
Any other value
0h
PA
PA
CCG
1h
Reserved
2h
PA
DN
CCG
3h
PA
PA
PA
4h
Reserved
5h
PA
DN
DN
6h
Reserved
7h
PA
CCG
CCG
8h to Fh
Reserved
Key:
PA = the device server shall perform the following as an uninterrupted sequence:
1)
perform read operations from the LBAs specified by the command;
2)
transfer the specified logical blocks from the Data-Out Buffer;
3)
perform an OR operation on the logical blocks from the read operations and the user data contained
in the logical blocks transferred from the Data-Out Buffer;
4)
store the results of the OR operation in a bitmap buffer;
5)
generate new protection information, if any, from the stored results;
6)
store the generated protection information, if any, into the bitmap buffer; and
7)
perform write operations using the updated logical block data (i.e., those containing the user data
resulting from the OR operation and the generated protection information, if any) from the bitmap
buffer.
DN = the device server shall discard the contents of the Data-Out Buffer and shall complete the command
with GOOD status.
CCG = the device server shall terminate the command with CHECK CONDITION status with the sense key
set to ILLEGAL REQUEST and the additional sense code set to ORWRITE GENERATION DOES NOT
MATCH
