# 5.29 RESTORE ELEMENTS AND REBUILD command

5.28.2 REPORT REFERRALS parameter data
The REPORT REFERRALS parameter data (see table 107) contains information indicating the user data
segment(s) on the logical unit and the SCSI target port groups though which those user data segments may
be accessed (see 4.26).
The USER DATA SEGMENT REFERRAL DESCRIPTOR LENGTH field indicates the number of bytes that follow in the
REPORT REFERRALS parameter data.
The user data segment referral descriptor (see table 18) is defined in the user data segment referral sense
data descriptor (see 4.18.4).
5.29 RESTORE ELEMENTS AND REBUILD command
The RESTORE ELEMENTS AND REBUILD command (see table 108) requests that the device server
perform a storage element restoration (see 4.36.4).
If deferred microcode has been saved and not activated (see SPC-6), then the device server shall terminate
this command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT NOT READY, MICROCODE ACTIVATION REQUIRED.
Table 107 — REPORT REFERRALS parameter data
Bit
Byte
Reserved
(MSB)
USER DATA SEGMENT REFERRAL DESCRIPTOR LENGTH (y - 3)
(LSB)
User data segment referral descriptor list
User data segment referral descriptor [first] (if any)
•••
4 + n
•••
y - m
User data segment referral descriptor [last] (if any)
•••
y


The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 108 for the RESTORE ELEMENTS AND REBUILD command.
For a RESTORE ELEMENTS AND REBUILD command, the device server shall terminate the command with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST and the additional sense code set
to COMMAND SEQUENCE ERROR if:
a)
there is at least one depopulated storage element (e.g., the PHYSICAL ELEMENT HEALTH field is set to
FFh); and
b)
all depopulated storage elements have the RALWD bit (see 5.8.2.2) set to zero.
For a RESTORE ELEMENTS AND REBUILD command, the following shall not be considered an error:
a)
the device has no depopulated storage elements; or
b)
at least one depopulated storage element has the RALWD bit (see 5.8.2.2) set to one.
The CONTROL byte is defined in SAM-6.
After command completion without error, further processing may occur as described in 4.36.4.
Table 108 — RESTORE ELEMENTS AND REBUILD command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
SERVICE ACTION (19h)
Reserved
•••
CONTROL
