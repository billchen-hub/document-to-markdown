# 5.20 READ CAPACITY (10) command

See the READ (10) command (see 5.16) for the definitions of the GROUP NUMBER field, the RDPROTECT field,
the DPO bit, the FUA bit, the RARC bit, the LOGICAL BLOCK ADDRESS field, and the TRANSFER LENGTH field.
See the READ (16) command (see 5.18) for the definitions of the DLD2 bit, DLD1 bit, and DLD0 bit.
If checking of the LOGICAL BLOCK REFERENCE TAG field is enabled (see table 79 in 5.16), then the EXPECTED
INITIAL LOGICAL BLOCK REFERENCE TAG field contains the value of the LOGICAL BLOCK REFERENCE TAG field
expected in the protection information of the first logical block accessed by the command instead of a value
based on the LBA (see 4.21.3).
If the ATO bit is set to one in the Control mode page (see SPC-6), and checking of the LOGICAL BLOCK
APPLICATION TAG field is enabled (see table 79 in 5.16), then the LOGICAL BLOCK APPLICATION TAG MASK field
contains a value that is a bit mask for enabling the checking of the LOGICAL BLOCK APPLICATION TAG field in
every instance of protection information for each logical block accessed by the command. A LOGICAL BLOCK
APPLICATION TAG MASK field bit set to one enables the checking of the corresponding bit of the EXPECTED
LOGICAL BLOCK APPLICATION TAG field with the corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in
every instance of protection information. A LOGICAL BLOCK APPLICATION TAG MASK field bit set to zero disables
the checking of the corresponding bit of the EXPECTED LOGICAL BLOCK APPLICATION TAG field with the
corresponding bit of the LOGICAL BLOCK APPLICATION TAG field in every instance of protection information.
If the ATO bit is set:
a)
to zero; or
b)
to one in the Control mode page (see SPC-6), and checking of the LOGICAL BLOCK APPLICATION TAG
field is disabled (see table 79),
then the LOGICAL BLOCK APPLICATION TAG MASK field and the EXPECTED LOGICAL BLOCK APPLICATION TAG field
shall be ignored
5.20 READ CAPACITY (10) command
5.20.1 READ CAPACITY (10) overview
The READ CAPACITY (10) command (see table 84) requests that the device server transfer eight bytes of
parameter data describing the capacity and medium format of the direct access block device to the Data-In
Buffer. This command may be processed as if it has a HEAD OF QUEUE task attribute (see 4.16). If the
logical unit supports protection information (see 4.21) or logical block provisioning management (see 4.7),
then the application client should use the READ CAPACITY (16) command (see 5.21) instead of the READ
CAPACITY (10) command.
NOTE 11 - Migration from the READ CAPACITY (10) command to the READ CAPACITY (16) command is
recommended for all implementations.


The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 84 for the READ
CAPACITY (10) command.
The CONTROL byte is defined in SAM-6.
5.20.2 READ CAPACITY (10) parameter data
The READ CAPACITY (10) parameter data is shown in table 85. Any time the READ CAPACITY (10)
parameter data changes, the device server should establish a unit attention condition as described in 4.10.
The device server shall set the RETURNED LOGICAL BLOCK ADDRESS field to the lower of:
a)
the LBA of the last logical block on the direct access block device; or
b)
FFFF_FFFFh, if the LBA of the last logical block on the direct access block device is greater than the
maximum value that is able to be specified in the RETURNED LOGICAL BLOCK ADDRESS field.
If the RETURNED LOGICAL BLOCK ADDRESS field is set to FFFF_FFFFh, then the application client should issue a
READ CAPACITY (16) command (see 5.21) to request that the device server transfer the READ
CAPACITY (16) parameter data to the Data-In Buffer.
The LOGICAL BLOCK LENGTH IN BYTES field contains the number of bytes of user data in a logical block.
Table 84 — READ CAPACITY (10) command
Bit
Byte
OPERATION CODE (25h)
Reserved
Obsolete
Obsolete
•••
Reserved
Reserved
Obsolete
CONTROL
Table 85 — READ CAPACITY (10) parameter data
Bit
Byte
(MSB)
RETURNED LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
LOGICAL BLOCK LENGTH IN BYTES
•••
(LSB)
