# 5.30 SANITIZE command

5.30 SANITIZE command
5.30.1 SANITIZE command overview
The SANITIZE command (see table 109) requests that the device server perform a sanitize operation
(see 4.11). This device server shall process this command as if it has a HEAD OF QUEUE task attribute
(see 4.16).
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 109 for the
SANITIZE command.
If the immediate (IMMED) bit is set to zero, then the device server shall return status after the sanitize operation
is completed. If the IMMED bit set to one, then the device server shall return status as soon as the CDB and
parameter data, if any, have been validated. The REQUEST SENSE command may be used to poll for
progress of the sanitize operation regardless of the value of the IMMED bit.
For a zoned block device, the zoned no reset (ZNR) bit requests the device server to perform specific actions
upon successful completion of a sanitize operation (see 4.11). Conditions described in ZBC-2 (e.g., the Zone
Condition becoming OFFLINE for a write pointer zone) may result in the device server not performing the
actions requested by the ZNR bit. Unless otherwise defined, if the ZNR bit is set to:
a)
zero, then the device server shall perform the equivalent of a RESET WRITE POINTER command
(see ZBC-2) with the ALL bit set to one; and
b)
one, then the device server shall:
A) not modify the write pointer (see ZBC-2) for any write pointer zone that is sanitized by a sanitize
cryptographic erase operation; and
B) perform the equivalent of a FINISH ZONE command (see ZBC-2) with the ALL bit set to one for
any write pointer zone that is sanitized by a sanitize overwrite operation or a sanitize block erase
operation.
For a logical unit that is not a zoned block device the ZNR bit shall be ignored.
If the allow unrestricted sanitize exit (AUSE) bit is set to one, and the specified sanitize operation fails, then the
device server shall process a subsequent EXIT FAILURE MODE service action as if the previous sanitize
operation had completed without error (see 4.11.4).
If:
1)
the AUSE bit is set to zero in the SANITIZE command that requested a sanitize operation;
2)
that sanitize operation completes with an error (see 4.11.4); and
3)
a subsequent SANITIZE command is received with:
A) the EXIT FAILURE MODE service action; or
Table 109 — SANITIZE command
Bit
Byte
OPERATION CODE (48h)
IMMED
ZNR
AUSE
SERVICE ACTION
Reserved
•••
(MSB)
PARAMETER LIST LENGTH
LSB)
CONTROL


B) any service action with the AUSE bit set to one,
then the device server shall terminate that subsequent SANITIZE command with CHECK CONDITION status
with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
The SERVICE ACTION field is defined in 5.30.2.
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter data that is available to be
transferred from the Data-Out Buffer. A PARAMETER LIST LENGTH field set to zero specifies that no data shall be
transferred.
The CONTROL byte is defined in SAM-6.
5.30.2 SANITIZE command service actions
5.30.2.1 SANITIZE command service actions overview
The SANITIZE command service actions are shown in table 110. At least one service action shall be
supported if the SANITIZE command is supported. If the service action specified in the CDB is not supported,
then the device server shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
If deferred microcode has been saved and not activated (see SPC-6), then the device server shall terminate
this command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT NOT READY, MICROCODE ACTIVATION REQUIRED.
5.30.2.2 OVERWRITE service action
The OVERWRITE service action (see table 110) requests that the device server perform a sanitize overwrite
operation (see 4.11).
While performing a sanitize overwrite operation, the device server shall remove all Background Scan Results
log parameters (see 6.4.2.3) from the Background Scan Results log page, if supported, and remove all
Pending Defect log parameters (see 6.4.8.3) from the Pending Defects log page, if supported.
Table 110 — SANITIZE service action codes
Code
Name
Description
PARAMETER LIST LENGTH
requirement a
Reference
01h
OVERWRITE
Perform a sanitize
overwrite operation
Set to > 0004h and
< (logical block length + 5)
5.30.2.2
02h
BLOCK ERASE
Perform a sanitize block
erase operation
Set to 0000h
5.30.2.3
03h
CRYPTOGRAPHIC
ERASE
Perform a sanitize
cryptographic erase
operation
Set to 0000h
5.30.2.4
1Fh
EXIT FAILURE
MODE
Exit the sanitize failure
mode
Set to 0000h
5.30.2.5
all others
Reserved
a If the requirement is not met, then the SANITIZE command is terminated with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN CDB.


The parameter list format for the OVERWRITE service action is shown in table 111.
If the INVERT bit is set to zero, then on each overwrite pass:
a)
the user data shall be written as specified in the INITIALIZATION PATTERN field; and
b)
the protection information, if any, shall be set to FFFF_FFFF_FFFF_FFFFh.
If the INVERT bit is set to one, then the user data and protection information bytes, if any, shall be inverted (i.e.,
each bit XORed with one) between consecutive overwrite passes.
The TEST field is shown in table 112.
The OVERWRITE COUNT field specifies the number of overwrite passes to be performed. The value of 00h is
reserved.
The INITIALIZATION PATTERN LENGTH field specifies the length in bytes of the INITIALIZATION PATTERN field. If the
INITIALIZATION PATTERN LENGTH field is set to zero or a value greater than the logical block length, then the
device server shall terminate the command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The INITIALIZATION PATTERN field specifies the data pattern to be used to write the user data. This data pattern
is repeated as necessary to fill each logical block. For each logical block, the first byte of the user data shall
begin with the first byte of the initialization pattern.
If the INVERT bit is set to one and:
a)
the OVERWRITE COUNT field is set to an even number, then the pattern used for the first write pass shall
consist of:
A) the user data set to the inversion of the INITIALIZATION PATTERN data; and
B) the protection information, if any, set to 0000_0000_0000_0000h;
or
Table 111 — OVERWRITE service action parameter list
Bit
Byte
INVERT
TEST
OVERWRITE COUNT
Reserved
(MSB)
INITIALIZATION PATTERN LENGTH (n - 3)
LSB)
INITIALIZATION PATTERN
•••
n
Table 112 — TEST field
Code
Description
00b
Shall not cause any changes in the defined behavior of the SANITIZE command.
01b to 11b
Vendor specific a
a Setting the TEST field to one of these values may adversely affect security properties of the
OVERWRITE service action.


b)
the OVERWRITE COUNT field is set to an odd number, then the pattern used for the first write pass shall
consist of:
A) the user data set to the INITIALIZATION PATTERN data; and
B) the protection information, if any, set to FFFF_FFFF_FFFF_FFFFh.
After a sanitize overwrite operation completes without error:
a)
the  device server completes read commands for which no other error occurs during processing with
GOOD status and read medium operations return the data written by the sanitize overwrite operation;
and
b)
protection information, if any, shall be set to FFFF_FFFF_FFFF_FFFFh in all logical blocks on the
medium.
5.30.2.3 BLOCK ERASE service action
The BLOCK ERASE service action (see table 110) requests that the device server perform a sanitize block
erase operation (see 4.11).
After a sanitize block erase operation completes without error:
a)
the device server may terminate commands that request read operations specifying mapped LBAs
(see 4.7.1) based on the setting of the WABEREQ field (see 6.6.2); and
b)
if the logical unit is formatted with protection information, then:
A) the protection information for each mapped LBA may be indeterminate; and
B) if the device server terminates a command that requests read operations specifying mapped
LBAs as a result of a protection information error, then the device server shall terminate that
command with CHECK CONDITION status with the sense key set to ABORTED COMMAND and
the appropriate additional sense code for the condition (e.g., for READ commands, the additional
sense code shown in table 79).
5.30.2.4 CRYPTOGRAPHIC ERASE service action
The CRYPTOGRAPHIC ERASE service action (see table 110) requests that the device server perform a
sanitize cryptographic erase operation (see 4.11).
After a sanitize cryptographic erase operation completes without error:
a)
the device server may terminate commands that request read operations specifying mapped LBAs
(see 4.7.1) based on the setting of the WACEREQ field (see 6.6.2); and
b)
if the logical unit is formatted with protection information, then:
A) the protection information for each mapped LBA may be indeterminate; and
B) if the device server terminates a command that requests read operations specifying mapped
LBAs as a result of a protection information error, then the device server shall terminate that
command with CHECK CONDITION status with the sense key set to ABORTED COMMAND and
the appropriate additional sense code for the condition (e.g., for READ commands, the additional
sense code shown in table 79).
5.30.2.5 EXIT FAILURE MODE service action
The EXIT FAILURE MODE service action (see table 110) requests that the device server complete a sanitize
operation which completed with an error as if the sanitize operation completed without an error (see 4.11). If
the most recent sanitize operation, if any, has completed without error, then the EXIT FAILURE MODE service
action completes without error.
After successful completion of a SANITIZE command with the EXIT FAILURE MODE service action:
a)
if any LBA is mapped (see 4.7.1), and the logical unit is formatted with protection information, then:
A) the protection information for each mapped LBA may be indeterminate; and
if the device server terminates a command that requests read operations specifying mapped LBAs as
a result of a protection information error, then the device server shall terminate that command with
