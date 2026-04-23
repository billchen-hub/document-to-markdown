# 4.18 Error reporting

4.18 Error reporting
4.18.1 Error reporting overview
If any of the conditions listed in table 14 occur during the processing of a command, then the device server
shall terminate the command with CHECK CONDITION status with the sense key set to the specified value
and the additional sense code set to the appropriate value for the condition. Some errors may occur after the
completion status has already been reported. For such errors, SPC-6 defines a deferred error reporting
mechanism. Table 14 lists some error conditions and the applicable sense keys. The list does not provide a
complete list of all conditions that may cause CHECK CONDITION status.
WRITE AND VERIFY
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE ATOMIC
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE LONG
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE SAME
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE SCATTERED
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE STREAM
Conflict
Conflict
Allowed
Conflict
Conflict
WRITE USING TOKEN
Conflict
Conflict
Allowed
Conflict
Conflict
Table 13 — SBC-4 commands that are allowed in the presence of various reservations (part 3 of 3)
Command
Addressed logical unit has this type of persistent
reservation held by another I_T nexus
From any I_T nexus
From
registered
I_T nexus
(RR all
types)
From I_T nexus not
registered
Write
Exclusive
Exclusive
Access
Write
Exclusive
- RR
Exclusive
Access
- RR
Key:
RR = Registrants Only or All Registrants
Allowed = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present should complete
normally.
Conflict = Commands received from I_T nexuses not holding the reservation or from I_T nexuses not
registered when a registrants only or all registrants type persistent reservation is present shall not be
performed, and the device server shall complete the command with RESERVATION CONFLICT status.
a The device server in logical units claiming compliance with SBC-2 may complete the command with
RESERVATION CONFLICT status. Device servers may report whether certain commands are allowed
in the PERSISTENT RESERVE IN command REPORT CAPABILITIES service action parameter data
ALLOW COMMANDS field (see SPC-6).


Direct access block devices compliant with this standard shall support both the fixed and descriptor formats of
sense data (see SPC-6).
Table 14 — Example error conditions
Condition
Sense key
Invalid LBA
ILLEGAL REQUEST
Unsupported option requested
ILLEGAL REQUEST
Logical unit reset, I_T nexus loss, or medium change
since last command from this application client
UNIT ATTENTION
Logical block provisioning threshold notification
UNIT ATTENTION
Self diagnostic failed
HARDWARE ERROR
Unrecovered error
MEDIUM ERROR or HARDWARE ERROR
Recovered read error
RECOVERED ERROR
Pseudo unrecovered error
MEDIUM ERROR
Over-run or other error that may be resolved by repeating
the command
ABORTED COMMAND
Attempt to write on write-protected medium
DATA PROTECT


Table 15 summarizes use of the sense data fields.
If a command attempts to access or reference an invalid LBA, then the device server shall report the first
invalid LBA (e.g., lowest numbered LBA) in the INFORMATION field of the sense data (see SPC-6).
If a recovered read error is reported, then the device server shall report the last LBA (e.g., highest numbered
LBA) on which a recovered read error occurred for the command in the INFORMATION field of the sense data.
If an unrecovered error is reported, then the device server shall report the LBA of the logical block on which an
unrecovered error occurred in the INFORMATION field of the sense data.
4.18.2 Processing pseudo unrecovered errors
If a pseudo unrecovered error with correction disabled is encountered on a logical block (e.g., by a command,
a background scan(see 4.23.1), or a background self-test (see SPC-6)), then the device server shall:
a)
perform no error recovery on the affected logical blocks, including any read error recovery enabled by
the Read-Write Error Recovery mode page (see 6.5.10) or the Verify Error Recovery mode page
(see 6.5.11);
b)
perform no automatic read reassignment or automatic write reassignment for the affected logical
blocks, regardless of the settings of the AWRE bit and the ARRE bit in the Read-Write Error Recovery
mode page;
c)
not consider errors on the affected logical blocks to be informational exception conditions as defined
in the Information Exceptions Control mode page (see 6.5.8);
Table 15 — Sense data field usage for direct access block devices
Field
Usage
Reference
INFORMATION field a
REASSIGN BLOCKS command
5.24
Any command that accesses the medium, based on the
Read-Write Error Recovery mode page
4.19.3 and 6.5.10
Any command that accesses the medium, based on the
Verify Error Recovery mode page
6.5.11
Any command that is terminated with a logical block
provisioning threshold notification
4.7.3.7.6
COMPARE AND WRITE command
5.3
COMMAND-SPECIFIC
INFORMATION field
EXTENDED COPY command
SPC-6
REASSIGN BLOCKS command
5.24
WRITE SCATTERED (16) command
4.35.3 and 5.55
WRITE SCATTERED (32) command
4.35.3 and 5.56
If rebuild assist mode is enabled (see 4.19), then any
command that accesses the medium, based on the
Read-Write Error Recovery mode page b
4.19.3
a See SPC-6 for a description of how the VALID bit interacts with the INFORMATION field.
b If fixed format sense data is used but the value to be placed in the COMMAND-SPECIFIC INFORMATION
field is greater than FFFF_FFFFh (e.g., an 8-byte LBA), then the device server shall report no value in
the INFORMATION field (see SPC-6) and shall report no value in the COMMAND-SPECIFIC INFORMATION
field (see SPC-6).


d)
not log errors on the affected logical blocks in any log page that contain error counters (see SPC-6);
and
e)
in any information returned for the error (e.g., in sense data or in the Background Scan Results log
page (see 6.4.2)), set the sense key to MEDIUM ERROR and either:
A) should set the additional sense code to READ ERROR – LBA MARKED BAD BY APPLICATION
CLIENT; or
B) may set the additional sense code to UNRECOVERABLE READ ERROR.
The logical unit shall clear a pseudo unrecovered error if it processes or performs one of the following for that
LBA:
a)
a format operation;
b)
a reassign operation;
c)
a sanitize overwrite operation;
d)
a sanitize block erase operation; or
e)
a write command that is not a WRITE LONG command specifying a pseudo unrecovered error.
The logical unit may clear a pseudo unrecovered error if it processes or performs one of the following for that
LBA:
a)
a sanitize cryptographic erase operation;
b)
an unmap operation;
c)
a MODE SELECT command that uses the mode parameter block descriptor (see 6.5.2) to change the
capacity to be lower than that LBA;
d)
a depopulate operation; or
e)
a depopulation revocation operation.
The logical unit shall not clear a pseudo unrecovered error if it processes one of the following for that LBA:
a)
a read command.
4.18.3 Block commands sense data descriptor
Table 16 defines the block commands sense data descriptor used in descriptor format sense data (see
SPC-6) for direct access block devices.
The DESCRIPTOR TYPE field and the ADDITIONAL LENGTH field are defined in SPC-6 and shall be set to the
values shown in table 16 for the block commands sense data descriptor.
4.18.4 User data segment referral sense data descriptor
Table 17 defines the user data segment referral sense data descriptor used in descriptor format sense data for
direct access block devices. The user data segment referral sense data descriptor contains descriptors
indicating the user data segment(s) on the logical unit and the SCSI target port groups through which those
user data segments may be accessed (see 4.26).
Table 16 — Block commands sense data descriptor format
Bit
Byte
DESCRIPTOR TYPE (05h)
ADDITIONAL LENGTH (02h)
Reserved
Reserved
Obsolete
Reserved


The DESCRIPTOR TYPE field is defined in SPC-6 and shall be set to the value shown in table 17 for the user
data segment referral sense data descriptor.
The ADDITIONAL LENGTH field indicates the number of bytes that follow in the logical block referrals sense data
descriptor.
A not all referrals (NOT_ALL_R) bit set to zero indicates that the list of user data segment referral descriptors is
a complete list of user data segments. A NOT_ALL_R bit set to one indicates that there are more user data
segments than are able to be indicated by the user data segment referral sense data.
Each user data segment referral descriptor (see table 18) indicates information identifying:
a)
a user data segment that is accessible through the SCSI target port groups indicated by this
descriptor; and
b)
one or more SCSI target port groups through which the user data segment indicated by this descriptor
is able to be accessed.
User data segment referral descriptors shall be listed in ascending LBA order. If a user data segment referral
descriptor describes the last user data segment (i.e., points to the largest LBA) and the preceding user data
segment descriptors do not represent the complete list of user data segments, then the next user data
segment referral descriptor, if any, shall describe the first user data segment (i.e., the user data segments may
wrap).
Table 17 — User data segment referral sense data descriptor format
Bit
Byte
DESCRIPTOR TYPE (0Bh)
ADDITIONAL LENGTH (y -1)
Reserved
NOT_ALL_R
Reserved
User data segment referral descriptor list
 User data segment referral descriptor [first]
•••
4 + n
•••
y - m
User data segment referral descriptor [last]
•••
y


Table 18 defines the user data segment referral descriptor.
The NUMBER OF TARGET PORT GROUP DESCRIPTORS field indicates the number of target port group descriptors
that follow.
The FIRST USER DATA SEGMENT LBA field indicates the first LBA of the first user data segment (see 4.26)
indicated by this descriptor.
The LAST USER DATA SEGMENT LBA field indicates the last LBA of the last user data segment (see 4.26)
indicated by this descriptor.
The target port group descriptor (see table 19) specifies the target port group and the asymmetric access
state of the target port group (see SPC-6). The device server shall return one target port group descriptor for
each target port group in a target port asymmetric access state of active/optimized, active/non-optimized, or
transitioning. The device server may return one target port group descriptor for each target port group in a
target port asymmetric access state of unavailable.
Table 18 — User data segment referral descriptor format
Bit
Byte
Reserved
•••
NUMBER OF TARGET PORT GROUP DESCRIPTORS
(MSB)
FIRST USER DATA SEGMENT LBA
•••
(LSB)
(MSB)
LAST USER DATA SEGMENT LBA
•••
(LSB)
Target port group descriptor list
 Target port group descriptor [first]
•••
•••
m-3
Target port group descriptor [last]
•••
m


The ASYMMETRIC ACCESS STATE field (see SPC-6) contains the asymmetric access state of the user data
segment(s) specified by this descriptor that may be accessed through this target port group.
The TARGET PORT GROUP field specifies a target port group (see SPC-6) that the application client uses when
issuing commands associated with the user data segments specified by this descriptor.
4.18.5 Direct access block device sense data descriptor
Table 20 defines the direct access block device sense data descriptor, which may be used in descriptor format
sense data (see SPC-6) instead of any of the following sense data descriptors:
a)
information (see SPC-6);
b)
command-specific information (see SPC-6);
c)
sense key specific (see SPC-6);
d)
field replaceable unit (see SPC-6); and
e)
block commands (see 4.18.3).
If the device server includes the direct access block device sense data descriptor in a sense data descriptor
list, then it shall not include any of those sense data descriptors in the same sense data descriptor list.
Table 19 — Target port group descriptor
Bit
Byte
Reserved
ASYMMETRIC ACCESS STATE
Reserved
(MSB)
TARGET PORT GROUP
(LSB)
Table 20 — Direct access block device sense data descriptor format
Bit
Byte
DESCRIPTOR TYPE (0Dh)
ADDITIONAL LENGTH (16h)
VALID
Reserved
Obsolete
Reserved
Reserved
SKSV
Sense key specific information
•••
FIELD REPLACEABLE UNIT CODE
(MSB)
 INFORMATION
•••
(LSB)
(MSB)
COMMAND-SPECIFIC INFORMATION
•••
(LSB)
