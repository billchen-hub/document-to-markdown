# 5.28 REPORT REFERRALS command

The ELEMENT IDENTIFIER field specifies the element identifier associated with the storage element (see 4.36.1)
to be depopulated. If the ELEMENT IDENTIFIER field specifies a physical element that is not a storage element,
(i.e. the PHYSICAL ELEMENT TYPE field (see table 61) is not set to 01h in the corresponding physical element
status descriptor) or specifies a physical element not supported by the device (see 5.8.2.2), then the device
server shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If the ELEMENT IDENTIFIER field specifies an element identifier for which the device server does not support
depopulation, then the device server shall terminate this command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If the ELEMENT IDENTIFIER field specifies an element identifier that is associated with a storage element that is
depopulated, then the device server shall make no changes and not consider this an error.
The CONTROL byte is defined in SAM-6.
After successful command completion , further processing may occur as described in 4.36.3.
5.27 REPORT PROVISIONING INITIALIZATION PATTERN command
The REPORT PROVISIONING INITIALIZATION PATTERN command (see table 105) requests that the
device server transfer the provisioning initialization pattern to the Data-In Buffer.
The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the value shown
in table 105 for the REPORT PROVISIONING INITIALIZATION PATTERN command.
The ALLOCATION LENGTH field is defined in SPC-6.
The CONTROL byte in defined in SAM-6.
5.28 REPORT REFERRALS command
5.28.1 REPORT REFERRALS command overview
The REPORT REFERRALS command (see table 106) requests that the device server transfer parameter
data indicating the user data segment(s) on the logical unit and the SCSI target ports through which those
user data segments may be accessed (see 4.26) to the Data-In Buffer. This command shall be supported by a
Table 105 — REPORT PROVISIONING INITIALIZATION PATTERN command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (1Dh)
Reserved
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB)
Reserved
CONTROL


logical unit that reports in the Extended INQUIRY Data VPD page (see SPC-6) that it supports referrals (i.e.,
the R_SUP bit set to one).
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).
The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the values shown
in table 106 for the REPORT REFERRALS command.
The LOGICAL BLOCK ADDRESS field specifies an LBA in the first user data segment that the device server shall
report in the REPORT REFERRALS parameter data. If the specified LBA exceeds the capacity of the medium
(see 4.5), then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to LOGICAL BLOCK ADDRESS
OUT OF RANGE.
The ALLOCATION LENGTH field is defined in SPC-6.
A one segment (ONE_SEG) bit set to zero specifics that the device server shall return information on all user
data segments starting with the user data segment that contains the LBA specified in the LOGICAL BLOCK
ADDRESS field and ending with the user data segment that contains the last LBA of the logical unit. A ONE_SEG
bit set to one specifies the device server shall only return information on the user data segment that contains
the LBA specified in the LOGICAL BLOCK ADDRESS field.
The CONTROL byte is defined in SAM-6.
Table 106 — REPORT REFERRALS command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (13h)
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)
(MSB)
ALLOCATION LENGTH
•••
LSB)
Reserved
ONE_SEG
CONTROL
