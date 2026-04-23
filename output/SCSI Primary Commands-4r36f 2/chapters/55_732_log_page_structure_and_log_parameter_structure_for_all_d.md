# 7.3.2 Log page structure and log parameter structure for all device types

7.3.2 Log page structure and log parameter structure for all device types
7.3.2.1 Log page structure
This subclause describes the log page structure that is applicable to all SCSI devices. Log pages specific to
each device type are described in the command standard that applies to that device type. The LOG SELECT
command (see 6.7) supports the ability to send zero or more log pages. The LOG SENSE command (see 6.8)
returns the log page or log pages specified by the combination of the PAGE CODE field and SUBPAGE CODE field
in the CDB.
Each log page begins with a four-byte page header followed by zero or more variable-length log parameters
defined for that log page. The log page format is shown in table 348.
For the LOG SENSE command (see 6.8), the DS bit indicates whether log parameters in this log page are
saved if the SP bit is set to one in the CDB. If the DS bit is set to zero, the log parameters are saved if the SP bit
is set to one. If the DS bit is set to one, the log parameters are not saved. For the LOG SELECT command
(see 6.7), the disable save (DS) bit operates in conjunction with the PCR bit, the SP bit, the PC field, and the
PARAMETER LIST LENGTH field in the CDB.
If the subpage format (SPF) bit is set to zero, then the SUBPAGE CODE field shall contain 00h. If the SPF bit is set
to one, then the SUBPAGE CODE field shall contain a value between 01h and FFh.
The PAGE CODE field indicates the number of the log page (see 7.3.1) that is being transferred.
The SUBPAGE CODE field indicates the subpage number of the log page (see 7.3.1) that is being transferred.
If an application client specifies values in the PAGE CODE field and SUBPAGE CODE field for a log page that is
reserved or not implemented by the logical unit, then the device server shall terminate the LOG SELECT
command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
Table 348 — Log page format
Bit
Byte
DS
SPF
PAGE CODE
SUBPAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
Log parameter(s)
Log parameter [first] (see 7.3.2.2)
(Length x)
•••
x+3
•••
n-y+1
Log parameter [last] (see 7.3.2.2)
(Length y)
•••
n


If the PARAMETER LIST LENGTH field in a LOG SELECT CDB contains zero, the meanings for the PCR bit, SP bit,
and PC field are defined in 6.7.2.
If the PARAMETER LIST LENGTH field in a LOG SELECT CDB contains a non-zero value (i.e., if a parameter list
is being sent with the LOG SELECT command), then table 349 defines the meaning for the combinations of
values for:
a)
the PCR bit, the SP bit, and the PC field in the LOG SELECT CDB; and
b)
the PARAMETER CODE field, the FORMAT AND LINKING field, and the DS bit in each log parameter trans-
ferred.
The PAGE LENGTH field indicates the length in bytes of the log parameters that follow. If the application client
sends a log page length that results in the truncation of any parameter, the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
Table 349 — LOG SELECT PCR bit, SP bit, and DS bit meanings when parameter list length is not zero
PCR
bit
SP
bit
DS
bit
Description
0b
0b
xb
The device server shall set the specified valuesa to the values in the parameter list and
shall not save any values to non-volatile media.
0b
1b
0b
The device server shall set the specified valuesa to the values in the parameter list and
shall process the optional saving of log parameter values as follows:
a)
If default data counter values are specified (see table 184 in 6.7.1), no values
shall be saved;
b)
If values other than default data counter values are specified and the device
server implements saving of the specified valuesa, then the device server shall
save the specified valuesa in the parameter list to non-volatile media; or
c)
If values other than default values are specified and the device server does not
implement saving of one or more of the specified valuesa, then the device server
shall terminate the command with CHECK CONDITION status, with the sense
key set to ILLEGAL REQUEST, and the additional sense code set to INVALID
FIELD IN PARAMETER LIST.
0b
1b
1b
The device server shall set the specified valuesa to the values in the parameter list and
shall not save any values in the specified log page to non-volatile media.
1b
xb
xb
The device server terminate the command with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID
FIELD IN CDB.
a The specified parameters are determined by the PARAMETER CODE field contents (see 7.3.2.2.1) in the
LOG SELECT parameter data as well as by the PC field contents (see table 184 in 6.7.1) in the LOG
SELECT CDB.


7.3.2.2 Log parameter structure
7.3.2.2.1 Introduction
Most log pages contain one or more data structures called log parameters (see table 350). Log parameters
may be data counters of a particular event(s), the conditions under which certain operations were performed,
or list parameters that contain a character string or binary description related to a particular event.
Each log parameter begins with a four-byte parameter header followed by one or more bytes of parameter
value data.
The PARAMETER CODE field identifies the log parameter being transferred. The device server shall return the
log parameters in a log page in ascending order based on the value in their PARAMETER CODE field.
If an application client specifies a value in the PARAMETER CODE field in the LOG SELECT command parameter
data that is reserved or not implemented by the logical unit, then the device server shall terminate the
command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are collectively referred to as the
parameter control byte. The bits and fields in the parameter control byte are described in 7.3.2.2.2.
The PARAMETER LENGTH field specifies the length in bytes of the PARAMETER VALUE field that follows. If the
application client specifies a parameter length that results in the truncation of the PARAMETER VALUE field, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the application client sends a value in a PARAMETER VALUE field that is outside the range supported by the
logical unit, and rounding is implemented for that parameter, the device server may:
a)
round to an acceptable value and terminate the command as described in 5.9; or
b)
terminate the command with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the parameter data for one LOG SELECT command contains more than one log page and the log pages are
not in ascending order by page code value then subpage code value, then the device server shall terminate
the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
Table 350 — Log parameter
Bit
Byte
(MSB)
PARAMETER CODE
(LSB)
Parameter control byte (see 7.3.2.2.2)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (n-3)
(MSB)
PARAMETER VALUE
•••
n
(LSB)


If the parameter data for one LOG SELECT command contains more than one log parameter in any one log
page and the log parameters are not in ascending order by parameter code value, then the device server shall
terminate the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
Application clients should send LOG SENSE commands prior to sending LOG SELECT commands to
determine supported log pages and page lengths.
The SCSI target device may provide independent sets of log parameters for each logical unit or for each
combination of logical units and I_T nexuses. If the SCSI target device does not support independent sets of
log parameters and any log parameters are changed that affect other I_T nexuses, then the device server
shall establish a unit attention condition (see SAM-5) for the initiator port associated with every I_T nexus
except the I_T nexus on which the LOG SELECT command was received, with the additional sense code set
to LOG PARAMETERS CHANGED.
7.3.2.2.2 Parameter control byte
7.3.2.2.2.1 Introduction
The bits and fields in the parameter control byte are described in 7.3.2.2.2.
For cumulative log parameter values, indicated by the PC field (see table 184 in 6.7.1) of the LOG SELECT
command and LOG SENSE command, the disable update (DU) bit is defined as follows:
a)
DU set to zero indicates that the device server shall update the log parameter value to reflect all
events that should be noted by that parameter; or
b)
DU set to one indicates that the device server shall not update the log parameter value except in
response to a LOG SELECT command that specifies a new value for the parameter.
NOTE 44 - While updating cumulative log parameter values, a device server may use volatile memory to hold
these values until a LOG SELECT or LOG SENSE command is received with an SP bit set to one or a vendor
specific event occurs. As a result the updated cumulative log parameter values may be lost if a power cycle
occurs.
If the PC field (see table 184 in 6.7.1) indicates that threshold values or default values are being processed,
the device server shall:
a)
set the DU bit to zero, if a LOG SENSE command is being processed; and
b)
ignore the DU bit, if a LOG SELECT command is being processed.
Regardless of the value in the PC field, the device server shall process ASCII format list log parameters (see
7.3.2.2.2.4) and binary format list log parameters (see 7.3.2.2.2.5) by:
a)
setting the DU bit to zero, if a LOG SENSE command is being processed; and
b)
ignoring the DU bit, if a LOG SELECT command is being processed.
A target save disable (TSD) bit set to zero indicates that the logical unit implicitly saves the log parameter at
vendor specific intervals. This implicit saving operation shall be done frequently enough to ensure that the
cumulative parameter values retain statistical significance (i.e., across power cycles). A TSD bit set to one
indicates that either the logical unit does not implicitly save the log parameter or implicit saving of the log
parameter has been disabled individually by an application client setting the TSD bit to one. An application
client may disable the implicit saving for all log parameters without changing any TSD bits using the GLTSD bit
in the Control mode page (see 7.5.8).


An enable threshold comparison (ETC) bit set to one indicates that a comparison to the threshold value is
performed whenever the cumulative value is updated. An ETC bit set to zero indicates that a comparison is not
performed. The value of the ETC bit is the same for cumulative and threshold parameters.
The threshold met criteria (TMC) field (see table 351) defines the basis for comparison of the cumulative and
threshold values. The TMC field is valid only if the ETC bit is set to one. The value of the TMC field is the same
for cumulative and threshold parameters.
If the ETC bit is set to one and the result of the comparison is true, the device server shall establish a unit
attention condition (see SAM-5) for the initiator port associated with every I_T nexus, with the additional sense
code set to THRESHOLD CONDITION MET.
The FORMAT AND LINKING field (see table 352) indicates the type of log parameter.
Table 351 — Threshold met criteria (TMC) field
Code
Basis for comparison
00b
Every update of the cumulative value
01b
Cumulative value
equal to
threshold value
10b
Cumulative value
not equal to
threshold value
11b
Cumulative value
greater than
threshold value
Table 352 — FORMAT AND LINKING field
Code
Log parameter type
Reference
00b
Bounded data counter
7.3.2.2.2.2
01b
ASCII format list
7.3.2.2.2.4
10b
Bounded data counter or
unbounded data counter
7.3.2.2.2.2 or
7.3.2.2.2.3
11b
Binary format list
7.3.2.2.2.5


7.3.2.2.2.2 Parameter control byte values for bounded data counter parameters
The device server shall return LOG SENSE parameter control byte values and process LOG SELECT
parameter control byte values as shown in table 353 for any log parameter that is defined to be a bounded
data counter log parameter.
If a LOG SELECT command contains a bounded data counter log parameter in which the parameter control
byte values differ from those shown in table 353, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
Each bounded data counter log parameter contains one saturating counter that is:
a)
associated with one or more events; and
b)
incremented whenever one of these events occurs.
If the counter in a bounded data counter log parameter has associated with it a vendor specific maximum
value, then upon reaching this maximum value, the data counter shall not be incremented (i.e., its value does
not wrap).
If the counter in a bounded data counter log parameter reaches its maximum value (i.e., saturates), the device
server shall:
a)
set the DU bit to one;
b)
handle other bounded data counter log parameters in the log page based on the contents of the
FORMAT AND LINKING field in each other log parameter as follows:
A)
if the FORMAT AND LINKING field is set to 00b, then that other log parameter shall stop incrementing
until reinitialized by a LOG SELECT command; or
Table 353 — Parameter control byte values for bounded data counter parameters
Field
or bit
Value for
LOG
SENSE
Value for
LOG
SELECT
Description
DU
0 or 1
0 or 1
If the DU bit is set to zero, the device server shall update the log
parameter value to reflect all events that should be noted by that
parameter. If the DU bit is set to one, the device server shall not
update the log parameter value except in response to a LOG
SELECT command that specifies a new value for the parameter.
TSD
0 or 1
0 or 1
If the TSD bit is set to zero, the device server shall save the log
parameter to its medium at vendor specific intervals. If the TSD bit is
set to one, implicit saving of the log parameter is disabled by an
application client.
ETC
0 or 1
0 or 1
If the ETC bit is set to one, a comparison to the threshold value is
performed whenever the cumulative value is updated. If the ETC bit
is set to zero, a comparison is not performed.
TMC
any
any
The TMC field (see table 351 in 7.3.2.2.2.1) defines the basis for
comparison of the cumulative and threshold values. The TMC field is
valid only if the ETC bit is set to one.
FORMAT
AND
LINKING
00b or 10b
00b or 10b
The log parameter is a data counter (see table 352 in 7.3.2.2.2.1)
and the handling of a parameter that reaches its maximum value is
described in this subclause


B)
if the FORMAT AND LINKING field is set to 10b, then that other log parameter shall not stop incre-
menting, but may be reinitialized by a LOG SELECT command.
and
c)
not alter the handling of other log parameters in the log page that are:
A)
unbounded data counter log parameters (see 7.3.2.2.2.3);
B)
ASCII format list log parameters (see 7.3.2.2.2.4); and
C) binary format list log parameters (see 7.3.2.2.2.5).
The processing of a command shall not be altered because the counter in a bounded data counter log
parameter reaches its maximum value (i.e., saturates). If the RLEC bit is set to one in the Control mode page
(see 7.5.8) and the processing of a command encounters no exception conditions other than the counter in a
bounded data counter log parameter reaching its maximum value, then the command shall be terminated with
CHECK CONDITION status, with the sense key set to RECOVERED ERROR, and the additional sense code
set to LOG COUNTER AT MAXIMUM.
7.3.2.2.2.3 Parameter control byte values for unbounded data counter parameters
The device server shall return LOG SENSE parameter control byte values and process LOG SELECT
parameter control byte values as shown in table 354 for any log parameter that is defined to be an unbounded
data counter log parameter.
If a LOG SELECT command contains an unbounded data counter log parameter in which the parameter
control byte values differ from those shown in table 354, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
Each unbounded data counter log parameter contains one or more saturating counters or wrapping counters.
The description of each counter field in the log parameter defines when the device server modifies the
contents of the counter that is transferred in that field.
Table 354 — Parameter control byte values for unbounded data counter parameters
Field
or bit
Value for
LOG
SENSE
Value for
LOG
SELECT
Description
DU
0 or 1
0 or 1
If the DU bit is set to zero, the device server shall update the log
parameter value or values to reflect all events that should be noted
by that parameter. If the DU bit is set to one, the device server shall
not update the log parameter value or values except in response to
a LOG SELECT command that specifies a new value for the
parameter.
TSD
0 or 1
0 or 1
If the TSD bit is set to zero, the device server shall save the log
parameter to its medium at vendor specific intervals. If the TSD bit is
set to one, implicit saving of the log parameter is disabled by an
application client.
ETC
Threshold comparisons are not performed for unbounded data
counter parameters
TMC
00b
ignored
Threshold comparisons are not performed for unbounded data
counter parameters
FORMAT
AND
LINKING
10b
10b
The log parameter is a data counter for which saturation of another
log parameter does not affect the incrementing of this log parameter
(see table 352 in 7.3.2.2.2.1).


Changes in an unbounded data counter (e.g., a counter reaching saturation or another maximum value) shall
not affect the handling of other log parameters in the log page. The processing of a command and the status
returned by that command shall not be altered because a counter in an unbounded data counter log
parameter saturates or reaches its maximum value.
The device server shall not change the value in the DU bit in an unbounded data counter log parameter unless
requested to do so by a LOG SELECT command.
7.3.2.2.2.4 Parameter control byte values for ASCII format list log parameters
The device server shall return LOG SENSE parameter control byte values and process LOG SELECT
parameter control byte values as shown in table 355 for any log parameter that is defined to be an ASCII
format (see 4.3.1) list log parameter.
If a LOG SELECT command contains an ASCII format list log parameter in which the parameter control byte
values differ from those shown in table 355, then the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
Table 355 — Parameter control byte values for ASCII format list log parameters
Field
or bit
Value for
LOG
SENSE
Value for
LOG
SELECT
Description
DU
ignored
The DU bit is not defined for list parameters.
TSD
0 or 1
0 or 1
If the TSD bit is set to zero, the device server shall save the log
parameter to its medium at vendor specific intervals. If the TSD bit is
set to one, implicit saving of the log parameter is disabled by an
application client.
ETC
Threshold comparisons are not performed for list parameters.
TMC
00b
ignored
Threshold comparisons are not performed for list parameters.
FORMAT
AND
LINKING
01b
01b
The log parameter is an ASCII format list parameter (see table 352
in 7.3.2.2.2.1).


7.3.2.2.2.5 Parameter control byte values for binary format list log parameters
The device server shall return LOG SENSE parameter control byte values and process LOG SELECT
parameter control byte values as shown in table 356 for any log parameter that is defined to be a binary format
list log parameter.
If a LOG SELECT command contains a binary format list log parameter in which the parameter control byte
values differ from those shown in table 356, then the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
Table 356 — Parameter control byte values for binary format list log parameters
Field
or bit
Value for
LOG
SENSE
Value for
LOG
SELECT
Description
DU
ignored
The DU bit is not defined for list parameters.
TSD
0 or 1
0 or 1
If the TSD bit is set to zero, the device server shall save the log
parameter to its medium at vendor specific intervals. If the TSD bit is
set to one, implicit saving of the log parameter is disabled by an
application client.
ETC
Threshold comparisons are not performed for list parameters.
TMC
00b
ignored
Threshold comparisons are not performed for list parameters.
FORMAT
AND
LINKING
11b
11b
The log parameter is an binary format list parameter (see table 352
in 7.3.2.2.2.1).
