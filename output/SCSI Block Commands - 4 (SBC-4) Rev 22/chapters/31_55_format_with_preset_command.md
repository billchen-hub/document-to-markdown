# 5.5 FORMAT WITH PRESET command

The device server shall write the initialization pattern using a security erasure write technique. The security
erasure write technique requirement and procedure is not defined by this standard. The device server is not
required to write the initialization pattern over the header and other parts of the medium not previously
accessible to the application client. If the device server is unable to write over any part of the medium that is
currently accessible to the application client or may be made accessible to the application client in the future
(e.g., by clearing the defect list), then the device server shall terminate the command with CHECK
CONDITION status with the sense key set to MEDIUM ERROR and the additional sense code set to the
appropriate value for the condition. The device server shall attempt to rewrite all remaining parts of the
medium even if some parts are not able to be rewritten.
NOTE 5 - The intent of the security erasure write is to render any previous user data unrecoverable by any
analog or digital technique.
NOTE 6 - Migration from the SI bit to the SANITIZE command (see 5.30) is recommended for all
implementations.
An SI bit set to zero specifies that the device server shall initialize the application client accessible part of the
medium. The device server is not required to initialize other areas of the medium. The device server shall
format the medium as defined in the FORMAT UNIT command.
The INITIALIZATION PATTERN TYPE field (see table 46) specifies the type of pattern the device server shall use to
initialize each logical block within the application client accessible part of the medium. All bytes within a logical
block shall be written with the initialization pattern.
The INITIALIZATION PATTERN LENGTH field specifies the number of bytes contained in the INITIALIZATION PATTERN
field. If the initialization pattern length exceeds the current logical block length, then the device server shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The INITIALIZATION PATTERN field specifies the initialization pattern.
5.5 FORMAT WITH PRESET command
The FORMAT WITH PRESET command (see table 47) requests that the device server perform a format
operation (see 4.33) using the parameters specified by the PRESET IDENTIFIER field.
Table 46 — INITIALIZATION PATTERN TYPE field
Code
Description
00h
Use a default initialization pattern a
01h
Repeat the pattern specified in the INITIALIZATION PATTERN field as required to fill the logical
block b
02h to 7Fh
Reserved
80h to FFh
Vendor specific
a If the INITIALIZATION PATTERN LENGTH field is not set to zero, then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
b If the INITIALIZATION PATTERN LENGTH field is set to zero, then the device server shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.


If deferred microcode has been saved and not activated (see SPC-6), then the device server shall terminate
this command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT NOT READY, MICROCODE ACTIVATION REQUIRED.
If the FORMAT WITH PRESET command is supported, the Format Presets VPD page (see 6.6.6) shall be
supported.
The processing of a FORMAT WITH PRESET command may result in the device server providing a different
logical unit (e.g., the peripheral device type may change). As a result, the successful completion of the format
operation (see 4.33.3.1) requires a power cycle before most commands return a status other than CHECK
CONDITION.
.
The OPERATION CODE field is defined in SPC-6 and shall be set as shown in table 47 for the FORMAT WITH
PRESET command.
An immediate (IMMED) bit set to zero specifies that the device server shall return status upon completion of the
format operation. An IMMED bit set to one specifies that the device server shall return status after the PRESET
IDENTIFIER field has been validated.
A format to maximum last logical block address (FMTMAXLBA) bit set to zero specifies that the format operation
should result in the RETURNED LOGICAL BLOCK ADDRESS field returned by a subsequent READ CAPACITY (16)
command (see 5.20) being equal to the value in the DESIGNED LAST LOGICAL BLOCK ADDRESS field in the
specified format preset descriptor (see 6.6.6). A FMTMAXLBA bit set to one specifies that the format operation
shall result in the RETURNED LOGICAL BLOCK ADDRESS field being set to the largest possible value based on the
condition of the media being formatted.
The PRESET IDENTIFIER field specifies which format preset descriptor (see 6.6.6) is used. If the specified preset
identifier is not equal to the contents of any PRESET IDENTIFIER field in the Format Presets VPD page
(see 6.6.6), then the device server shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN CDB.
The CONTROL byte is defined in SAM-6.
Table 47 — FORMAT WITH PRESET command
Bit
Byte
OPERATION CODE (38h)
IMMED
FMTMAXLBA
Reserved
(MSB)
•••
PRESET IDENTIFIER
(LSB)
•••
Reserved
CONTROL
