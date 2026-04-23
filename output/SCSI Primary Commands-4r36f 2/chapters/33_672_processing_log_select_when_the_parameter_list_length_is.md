# 6.7.2 Processing LOG SELECT when the parameter list length is zero

6.7.2 Processing LOG SELECT when the parameter list length is zero
If the PARAMETER LIST LENGTH field is set to zero (i.e., when there is no parameter data being sent with a LOG
SELECT command), the SCSI target device responds by processing the log parameter values as described in
this subclause.
The PAGE CODE field and SUBPAGE CODE field (see table 185) specify the log page or log pages to which the
other CDB fields apply (see table 186).
Table 186 defines the meaning of the combinations of values for the PCR bit, the SP bit, and the PC field.
Table 185 — PAGE CODE field and SUBPAGE CODE field
PAGE CODE
field
SUBPAGE CODE
field
Description
00h
00h
All log parameters in all log pages a
00h to 3Fh
01h to FEh
All log parameters in the log page specified by the page code and
subpage code
00h to 3Fh
FFh
All log parameters in the log pages specified by page code and all
subpage codes
01h to 3Fh
00h
All log parameters in the log page specified by the page code
a This is equivalent to the LOG SELECT command operation specified by SPC-3.
Table 186 — PCR bit, SP bit, and PC field meanings when parameter list length is zero (part 1 of 3)
PCR
bit
SP
bit
PC
field
Description
0b
0b
0xb
This is not an error. The device server shall make no changes to any log parameter
values and shall not save any values to non-volatile media.
0b
1b
00b
The device server shall make no changes to any log parameter values and shall
process the optional saving of current parameter values as follows:
a)
if the values are current threshold data counter parameters, then:
A)
if the device server implements saving of the current threshold values, the
device server shall save all current threshold values to non-volatile media;
or
B)
if the device server does not implement saving of the current threshold
values, the device server shall terminate the commanda.
or
b)
if the values are current list parameters, then:
A)
if the device server implements saving of the current list parameters, the
device server shall save all current list parameters to non-volatile media; or
B)
if the device server does not implement saving of the current list param-
eters, the device server shall terminate the commanda.
a The device server shall terminate the command with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
b Vendor specific default threshold values and vendor specific default cumulative values may be zero.


0b
1b
01b
The device server shall make no change to any log parameter values and shall
process the optional saving of current parameter values as follows:
a)
if the values are current cumulative data counter parameters, then:
A)
if the device server implements saving of the current cumulative values, the
device server shall save all current cumulative values to non-volatile media;
or
B)
if the device server does not implement saving of the current cumulative
values, the device server shall terminate the commanda.
or
b)
if the values are current list parameters, then:
A)
if the device server implements saving of the current list parameters, the
device server shall save all current list parameters to non-volatile media; or
B)
if the device server does not implement saving of the current list param-
eters, the device server shall terminate the commanda.
0b
xb
10b
The device server shall set all current threshold values to the vendor specific default
threshold valuesb and shall not save any values to non-volatile media.
0b
xb
11b
The device server shall set all current cumulative values to the vendor specific default
cumulative valuesb and shall not save any values to non-volatile media.
1b
0b
xxb
The device server shall:
1)
set all current threshold values to the vendor specific default threshold valuesb;
2)
set all current cumulative values to the vendor specific default cumulative
valuesb;
3)
set all list parameters to their vendor specific default values; and
4)
not save any values to non-volatile media.
1b
1b
00b
The device server shall process the optional saving of current threshold values as
follows:
a)
if the device server implements saving of the current threshold values, the
device server shall:
1)
save all current threshold values to non-volatile media;
Note: Device servers compliant with SPC-3 may save the log parameter values to
non-volatile media after setting the log parameter values instead of before setting
the log parameter values.
2)
set all current threshold values to the vendor specific default threshold
valuesb;
3)
set all current cumulative values to the vendor specific default cumulative
valuesb, and
4)
set all list parameters to their vendor specific default values.
or
b)
if the device server does not implement saving of the current threshold values,
the device server shall terminate the commanda.
Table 186 — PCR bit, SP bit, and PC field meanings when parameter list length is zero (part 2 of 3)
PCR
bit
SP
bit
PC
field
Description
a The device server shall terminate the command with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
b Vendor specific default threshold values and vendor specific default cumulative values may be zero.


The current cumulative values may be updated by the device server as defined for the specific log page or by
the application client using the LOG SELECT command. The current threshold values may only be modified
by the application client via the LOG SELECT command.
NOTE 31 - Log pages or log parameters that are not available may become available at some later time (e.g.,
after the logical unit has become ready).
1b
1b
01b
The device server shall process the optional saving of current cumulative values as
follows:
a)
if the device server implements saving of the current cumulative values, the
device server shall:
1)
save all current cumulative values to non-volatile media;
Note: Device servers compliant with SPC-3 may save the log parameter values to
non-volatile media after setting the log parameter values instead of before setting
the log parameter values.
2)
set all current threshold values to the vendor specific default threshold
valuesb;
3)
set all current cumulative values to the vendor specific default cumulative
valuesb, and
4)
set all list parameters to their vendor specific default values.
or
b)
if the device server does not implement saving of the current cumulative values,
the device server shall terminate the commanda.
1b
1b
1xb
The device server shall:
1)
set all current threshold values to the vendor specific default threshold valuesb;
2)
set all current cumulative values to the vendor specific default cumulative
valuesb;
3)
set all list parameters to their vendor specific default values; and
4)
not save any values to non-volatile media.
Table 186 — PCR bit, SP bit, and PC field meanings when parameter list length is zero (part 3 of 3)
PCR
bit
SP
bit
PC
field
Description
a The device server shall terminate the command with CHECK CONDITION status, with the sense key set
to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
b Vendor specific default threshold values and vendor specific default cumulative values may be zero.


6.8 LOG SENSE command
The LOG SENSE command (see table 187) provides a means for the application client to retrieve statistical or
other operational information maintained by the SCSI target device about the SCSI target device or its logical
units. It is a complementary command to the LOG SELECT command.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 187 for the LOG SENSE
command.
Saving parameters is an optional function of the LOG SENSE command. If the logical unit does not implement
saving log parameters and if the save parameters (SP) bit is set to one, the device server shall terminate the
command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
An SP bit set to zero specifies the device server shall perform the specified LOG SENSE command and shall
not save any log parameters. If saving log parameters is implemented, an SP bit set to one specifies that the
device server shall perform the specified LOG SENSE command and shall save all log parameters identified
as saveable by the DS bit (see 7.3) to a nonvolatile, vendor specific location.
The PC field shall be ignored for ASCII format list log parameters (see 7.3.2.2.2.4) and binary format list log
parameters (see 7.3.2.2.2.5).
For bounded data counter log parameters (see 7.3.2.2.2.2) and unbounded data counter log parameters (see
7.3.2.2.2.3), the page control (PC) field (see table 184 in 6.7.1) specifies which log parameter values are to be
returned by a device server in response to a LOG SENSE command.
For ASCII format list log parameters (see 7.3.2.2.2.4) and binary format list log parameters (see 7.3.2.2.2.5),
the PC field shall be ignored. If the parameters specified by the PAGE CODE field and SUBPAGE CODE field in the
CDB are list parameters, then the parameter values returned by a device server in response to a LOG SENSE
command are determined as follows:
1)
the current list log parameter values, if there has been an update to a list log parameter value (e.g., by
a LOG SELECT command or by a device specific event) in the specified page or pages since the last
logical unit reset occurred;
Table 187 — LOG SENSE command
Bit
Byte
OPERATION CODE (4Dh)
Reserved
Obsolete
SP
PC
PAGE CODE
SUBPAGE CODE
Reserved
(MSB)
PARAMETER POINTER
(LSB)
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL


2)
the saved list log parameter values, if saved log parameters are implemented and an update has not
occurred since the last logical unit reset; or
3)
the vendor specific default list log parameter values, if saved values are not available or not imple-
mented and an update has not occurred since the last logical unit reset.
The PAGE CODE field and SUBPAGE CODE field specify which log page of data is being requested (see 7.3). If the
log page specified by the page code and subpage code combination is reserved or not implemented, the
device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
The PARAMETER POINTER field allows the application client to request parameter data beginning from a specific
parameter code to the maximum allocation length or the maximum parameter code supported by the logical
unit, whichever is less. If the PARAMETER POINTER field is set to:
a)
0000h, then the device server shall begin the transfer of the parameter data with the log parameter
having the lowest parameter code that is implemented by the device server for the specified log page;
b)
a value specifying the parameter code of a log parameter implemented by the device server for the
specified log page, then the device server shall begin the transfer of the parameter data with the log
parameter having the specified code;
c)
a value that does not specify a parameter code implemented by the device server for the specified log
page but is less than the largest parameter code implemented by the device server, then the device
server shall begin the transfer of the parameter data with the log parameter implemented by the
device server that has the next largest parameter code after the specified value; or
d)
a value greater than the largest parameter code implemented by the device server for the specified
log page, then the device server shall terminate the command with CHECK CONDITION status, with
the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
CDB.
Log parameters within the specified log page shall be transferred in ascending order according to parameter
code.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.


6.9 MANAGEMENT PROTOCOL IN command
6.9.1 MANAGEMENT PROTOCOL IN command description
The MANAGEMENT PROTOCOL IN command (see table 188) is used to retrieve management protocol infor-
mation (see 6.9.2) or the results of one or more MANAGEMENT PROTOCOL OUT commands (see 6.10).
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 188 for the MANAGEMENT
PROTOCOL IN command.
The MANAGEMENT PROTOCOL field (see table 189) specifies which management protocol is being used.
The contents of the MANAGEMENT PROTOCOL SPECIFIC1 field and MANAGEMENT PROTOCOL SPECIFIC2 field depend
on the protocol specified by the MANAGEMENT PROTOCOL field (see table 189).
The ALLOCATION LENGTH field is defined in 4.2.5.6.
The CONTROL byte is defined in SAM-5.
Indications of data overrun or underrun and the mechanism, if any, for processing retries depend on the
protocol specified by the MANAGEMENT PROTOCOL field (see table 189).
Table 188 — MANAGEMENT PROTOCOL IN command
Bit
Byte
OPERATION CODE (A3h)
Reserved
SERVICE ACTION (10h)
MANAGEMENT PROTOCOL
MANAGEMENT PROTOCOL SPECIFIC1

•••
(MSB)
ALLOCATION LENGTH

•••
(LSB)
MANAGEMENT PROTOCOL SPECIFIC2
CONTROL
Table 189 — MANAGEMENT PROTOCOL field in MANAGEMENT PROTOCOL IN command
Code
Description
Reference
00h
Management protocol information
6.9.2
01h to 2Fh
Reserved
30h to 35h
Defined by the SNIA
3.1.171
36h to EFh
Reserved
F0h to FFh
Vendor Specific
