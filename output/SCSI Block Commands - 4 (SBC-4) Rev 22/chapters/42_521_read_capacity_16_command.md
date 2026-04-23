# 5.21 READ CAPACITY (16) command

5.21 READ CAPACITY (16) command
5.21.1 READ CAPACITY (16) command overview
The READ CAPACITY (16) command (see table 86) requests that the device server transfer parameter data
describing the capacity and medium format of the direct access block device to the Data-In Buffer. This
command is mandatory if the logical unit supports protection information (see 4.21) or logical block
provisioning management (see 4.7) and is optional otherwise. This command may be processed as if it has a
HEAD OF QUEUE task attribute (see 4.16).
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the values shown
in table 86 for the READ CAPACITY (16) command.
The ALLOCATION LENGTH field is defined in SPC-6.
The CONTROL byte is defined in SAM-6.
Table 86 — READ CAPACITY (16) command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (10h)
Obsolete
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB)
Reserved
Obsolete
CONTROL


5.21.2 READ CAPACITY (16) parameter data
The READ CAPACITY (16) parameter data is shown in table 87. Any time the READ CAPACITY (16)
parameter data changes, the device server should establish a unit attention condition as described in 4.10.
The RETURNED LOGICAL BLOCK ADDRESS field and LOGICAL BLOCK LENGTH IN BYTES field of the READ
CAPACITY (16) parameter data are defined in the READ CAPACITY (10) parameter data (see 5.20). The
maximum value that shall be returned in the RETURNED LOGICAL BLOCK ADDRESS field is
FFFF_FFFF_FFFF_FFFEh.
The protection type (P_TYPE) field and the protection enable (PROT_EN) bit (see table 88) indicate the logical
unit’s current type of protection.
The P_I_EXPONENT field may be used to determine the number of protection information intervals placed within
each logical block (see 5.4.2).
Table 87 — READ CAPACITY (16) parameter data
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
Reserved
Restricted for ZBC-2
P_TYPE
PROT_EN
P_I_EXPONENT
LOGICAL BLOCKS PER PHYSICAL BLOCK
EXPONENT
LBPME
LBPRZ
(MSB)
LOWEST ALIGNED LOGICAL BLOCK ADDRESS
(LSB)
Reserved
•••
Table 88 — P_TYPE field and PROT_EN bit
P_TYPE
PROT_EN
Description
n/a
The logical unit is formatted to type 0 protection (see 4.21.2.2).
000b
The logical unit is formatted to type 1 protection (see 4.21.2.3).
001b
The logical unit is formatted to type 2 protection (see 4.21.2.4).
010b
The logical unit is formatted to type 3 protection (see 4.21.2.5).
011b to 111b
Reserved
