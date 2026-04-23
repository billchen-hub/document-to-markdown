# 6.4 Log parameters

The PAGE CODE field and PAGE LENGTH field are defined in SPC-6 and shall be set to the values shown in
table 176 for the Translate Address Output diagnostic page.
The SUPPLIED FORMAT field specifies the format (see 6.2) of the ADDRESS TO TRANSLATE field. If the device
server does not support the requested format, then the device server shall terminate the SEND DIAGNOSTIC
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
The TRANSLATE FORMAT field specifies the format (see 6.2) the device server shall use for the result of the
address translation. If the device server does not support the specified format, then the device server shall
terminate the SEND DIAGNOSTIC command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The ADDRESS TO TRANSLATE field contains a single address descriptor that the application client is requesting
the device server to translate. The format of this field depends on the value in the SUPPLIED FORMAT field. The
formats are described in 6.2. If the short block format address descriptor is specified, then the first four bytes
of the ADDRESS TO TRANSLATE field shall contain the short block format address descriptor and the last four
bytes shall contain 0000_0000h.
6.4 Log parameters
6.4.1 Log parameters overview
6.4.1.1 Summary of log pages
See table 177 for references to the log pages and their corresponding page codes and subpage codes for
direct access block devices. See SPC-6 for a detailed description of logging operations.
Table 177 — Log page codes and subpage codes for direct access block devices  (part 1 of 2)
Log page name
Page code a
Subpage code a
Reference
Application Client
0Fh
00h
SPC-6
ATA PASS-THROUGH Results
16h
00h
SAT-4
Background Scan Results
15h
00h
6.4.2
Background Operation
15h
02h
6.4.3
Buffer Over-Run/Under-Run
01h
00h
SPC-6
Cache Memory Statistics
19h
20h
SPC-6
Command Duration Limits Statistics
19h
21h
SPC-6
Environmental Limits
0Dh
02h
SPC-6
Environmental Reporting
0Dh
01h
SPC-6
Format Status
08h
00h
6.4.4
General Statistics and Performance
19h
00h
SPC-6
Group Statistics and Performance (1 to 31)
19h
01h to 1Fh
SPC-6
Informational Exceptions
2Fh
00h
SPC-6
Last n Deferred Errors or Asynchronous Events
0Bh
00h
SPC-6
Last n Error Events
07h
00h
SPC-6
Logical Block Provisioning
0Ch
00h
6.4.5
a All page code and subpage code combinations not shown in this table are reserved.


6.4.1.2 Setting and resetting log parameters
In a LOG SELECT command (see SPC-6), an application client may specify that:
a)
all the parameters in a log page or pages are to be reset (i.e., the PCR bit set to one and the
PARAMETER LIST LENGTH field is set to zero); or
b)
individual parameters in log page are to be changed to specified new values (i.e., the PCR bit is set to
zero and the PARAMETER LIST LENGTH field is not set to zero).
LPS Misalignment
15h
03h
6.4.6
Non-Medium Error
06h
00h
SPC-6
Non-volatile Cache
17h
00h
6.4.7
Pending Defects
15h
01h
6.4.8
Power Condition Transitions
1Ah
00h
SPC-6
Protocol-Specific Ports
18h
00h to FEh
SPC-6
Read Error Counters
03h
00h
SPC-6
Self-Test Results
10h
00h
SPC-6
Solid State Media
11h
00h
6.4.9
Start-Stop Cycle Counter
0Eh
00h
SPC-6
Supported Log Pages
00h
00h
SPC-6
Supported Log Pages and Subpages
00h
FFh
SPC-6
Supported Subpages
01h to 3Fh
FFh
SPC-6
Temperature
0Dh
00h
SPC-6
Utilization
0Eh
01h
6.4.10
Verify Error Counters
05h
00h
SPC-6
Write Error Counters
02h
00h
SPC-6
Zoned Block Device Statistics
14h
01h
ZBC-2
Vendor specific
30h to 3Eh
00h to FEh
n/a
Table 177 — Log page codes and subpage codes for direct access block devices  (part 2 of 2)
Log page name
Page code a
Subpage code a
Reference
a All page code and subpage code combinations not shown in this table are reserved.


The device server processing of LOG SELECT commands (see SPC-6) that request changes to individual log
parameters or reset all log parameters depend on the log parameter that is being changed or reset, and is
specified in the table that defines the log parameter using the keywords shown in table 178 (also see SPC-6).
6.4.2 Background Scan log page
6.4.2.1 Background Scan log page overview
Using the format shown in table 180, the Background Scan log page reports information about:
a)
background pre-scan operations (see 4.23.2) and background medium scan operations (see 4.23.3);
and
b)
any logical blocks where an error was detected during a background scan operation.
The parameter codes for the Background Scan log page are listed in table 179.
Table 178 — Keywords for resetting or changing log parameters
Keyword
Device server processing when:
PCR bit is set to one a
PCR bit is set to zero b
Always
Reset the log parameter.
Change the log parameter.
Reset Only
Reset the log parameter.
If any changes are requested in the PARAMETER VALUE
field of the log parameter, then:
a)
terminate the command with CHECK CONDITION
status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST; and
b)
do not make any requested changes in any field in
any log parameter in any log page
Never
Do not reset the log parameter; see
the LOG SELECT command in
SPC-6 for description of possible
error conditions.
a If the PCR bit is set to one, and the PARAMETER LIST LENGTH field is not set to zero, then the device
server shall terminate the LOG SELECT command (see SPC-6).
b If the PCR bit is set to zero, and the PARAMETER LIST LENGTH field is set to zero. then no log parameters
are changed (see SPC-6).
Table 179 — Background Scan log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Background Scan Status
Never
6.4.2.2
Mandatory
0001h to 0800h
Background Scan Results
Reset Only
6.4.2.3
Optional b
8000h to AFFFh
Vendor specific
n/a
Optional
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
b If the Background Scan log page is supported, then at least one Background Scan Results log
parameter shall be supported.


The Background Scan log page has the format shown in table 180.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
The DS bit, the SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in
table 180 for the Background Scan log page.
If the device server processes a LOG SELECT command with the PCR bit set to one (see SPC-6), then the
device server shall:
a)
not change the values in the Background Scan Status log parameter; and
b)
delete all Background Scan Results log parameters.
Table 180 — Background Scan log page
Bit
Byte
DS (1b)
SPF (0b)
PAGE CODE (15h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Background scan parameters
Background scan parameter [first] (if any)
•••
•••
Background scan parameter [last] (if any)
•••
n


6.4.2.2 Background Scan Status log parameter
The Background Scan Status log parameter for the Background Scan log page has the format shown in
table 181.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 181 for the
Background Scan Status log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Background Scan Status log parameter shall
be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 181 for the
Background Scan Status log parameter.
The ACCUMULATED POWER ON MINUTES field indicates the number of minutes the device server has been
powered on since manufacturing.
Table 181 — Background Scan Status log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (0Ch)
(MSB)
ACCUMULATED POWER ON MINUTES
•••
(LSB)
Reserved
BACKGROUND SCAN STATUS
(MSB)
NUMBER OF BACKGROUND SCANS PERFORMED
(LSB)
(MSB)
BACKGROUND SCAN PROGRESS
(LSB)
(MSB)
NUMBER OF BACKGROUND MEDIUM SCANS PERFORMED
(LSB)


Table 182 defines the BACKGROUND SCAN STATUS field.
The NUMBER OF BACKGROUND SCANS PERFORMED field indicates the number of background scan operations
(i.e., the total number of background pre-scan operations plus the number of background medium scan
operations) that have been performed since the SCSI target device was shipped by the manufacturer.
The BACKGROUND SCAN PROGRESS field indicates the percent complete of a background scan operation in
progress. The returned value is a numerator that has 65 536 (i.e., 1_0000h) as its denominator. If there is no
background scan operation in progress (i.e., no background scan operation has been initiated since power on
or the most recent background scan operation has completed), then the device server shall set the
BACKGROUND SCAN PROGRESS field to 0000h.
The NUMBER OF BACKGROUND MEDIUM SCANS PERFORMED field indicates the number of background medium
scan operations that have been performed since the SCSI target device was shipped by the manufacturer. If
the NUMBER OF BACKGROUND MEDIUM SCANS PERFORMED field contains 0000h, then the number of background
medium scan operations is unknown.
The total number of background pre-scan operations that have been performed is the value in the NUMBER OF
BACKGROUND SCANS PERFORMED field minus the value in the NUMBER OF BACKGROUND MEDIUM SCANS
PERFORMED field.
Table 182 — BACKGROUND SCAN STATUS field
Code
Description
00h
No background scan operation is active.
01h
A background medium scan operation is active.
02h
A background pre-scan operation is active.
03h
A background scan operation was halted as a result of a fatal error.
04h
A background scan operation was halted as a result of a vendor specific pattern of errors.
05h
A background scan operation was halted as a result of the medium being formatted without
the PLIST.
06h
A background scan operation was halted as a result of a vendor specific cause.
07h
A background scan operation was halted as a result of the temperature being out of the
allowed range.
08h
Background medium scan operations are enabled (i.e., the EN_BMS bit is set to one in the
Background Control mode page (see 6.5.4)), and no background medium scan operation is
active (i.e., the device server is waiting for Background Medium Scan Interval timer expiration
before starting the next background medium scan operation).
09h
A background scan operation was halted as a result of the S_L_FULL bit being set to one in
the Background Control mode page (see 6.5.4) and the background scan results list being
full.
0Ah
A background pre-scan operation was halted as a result of the Background Pre-scan Time
Limit timer expiring.
0Bh to FFh
Reserved


6.4.2.3 Background Scan Results log parameter
The Background Scan Results log parameter for the Background Scan log page has the format shown in
table 183. If the Background Scan log page is reset, then all Background Scan Results log parameters are
discarded. If no errors have occurred during any background scan since the most recent reset of the
Background Scan log page, then no Background Scan Results log parameters shall be present.
The PARAMETER CODE field is described in SPC-6 and shall be set to a value from 0001h through 0800h in
sequence as errors are discovered during a background scan operation. When all of the supported parameter
code values have been used, and a new error is discovered during a background scan operation, the oldest
Background Scan Results log parameter in the list (i.e., the Background Scan Results log parameter with the
smallest value in the ACCUMULATED POWER ON MINUTES field) shall be discarded, and the PARAMETER CODE field
(see 6.4.2.3) for the new defect shall be set to the parameter code value of the discarded Background Scan
Results log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for a Background Scan Results log parameter shall
be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is defined in SPC-6 and shall be set to the value shown in table 183 for the
Background Scan Results log parameter.
The ACCUMULATED POWER ON MINUTES field indicates the number of minutes that the device server has been
powered on since manufacturing at the time the background scan error reported in the Background Scan
Results log parameter occurred.
Table 183 — Background Scan Results log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h to 0800h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (14h)
(MSB)
ACCUMULATED POWER ON MINUTES
•••
(LSB)
REASSIGN STATUS
SENSE KEY
ADDITIONAL SENSE CODE
ADDITIONAL SENSE CODE QUALIFIER
Vendor specific
•••
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)


Table 184 defines the REASSIGN STATUS field.
Table 184 — REASSIGN STATUS field
Code
Reason
LOWIR bit a
Original
error b
Additional conditions
1h
Yes
Yes
Recovered or
unrecovered
The LBA has not yet been reassigned. c
2h
Yes
No
Recovered
The device server performed automatic read reassignment for the
LBA (i.e., performed a reassign operation for the LBA and a write
operation with recovered logical block data). d
4h
Yes
Yes
Recovered
The device server’s attempt to perform automatic read reassignment
failed. The logical block may or may not now have an uncorrectable
error. c
5h
Yes
No
Recovered
The error was corrected by the device server rewriting the logical
block without performing a reassign operation.
6h
Yes
Yes
Recovered or
unrecovered
Either:
a)
an application client caused automatic write reassignment for the
LBA with a command performing a write operation; or
b)
the LBPRZ field is set to xx1b (see 6.6.7), and an application client
caused an unmap operation for the LBA. c
7h
Yes
Yes
Recovered or
unrecovered
Either:
a)
an application client caused a reassign operation for the LBA with
a REASSIGN BLOCKS command; or
b)
the LBPRZ field is set to 000b or is set to 010b (see 6.6.7), and an
application client caused an unmap operation for the LBA. c
8h
Yes
Yes
Recovered or
unrecovered
An application client’s request for a reassign operation for the LBA
with a REASSIGN BLOCKS command failed. The logical block
referenced by the LBA may or may not still have an uncorrectable
error.
All
others
Reserved
Key:
Yes = specifies that a Background Scan Results log parameter shall be generated for the error.
No
= specifies that a Background Scan Results log parameter shall not be generated for the error
a The LOWIR bit (see 6.5.4).
b Type of error detected while reading the logical block referenced by the LBA specified by the LOGICAL
BLOCK ADDRESS field(see 6.4.2.3) during a background scan operation.
c The REASSIGN STATUS field in a given log parameter changes from 1h or 4h to 6h, 7h, or 8h when a
reassign operation, write operation, or unmap operation on the LBA succeeds or when a reassign
operation on the LBA fails. After the LBA is reassigned, any subsequent medium error occurring for the
LBA is reported in a new log parameter with the same value in the LOGICAL BLOCK ADDRESS field as the
value in the LOGICAL BLOCK ADDRESS field in the log parameter for the previous medium error for the
LBA.
d The ARRE bit (see 6.5.10) controls automatic read reassignment based on errors detected during all
read medium operations, including those that are part of background scan operations.


If sense data is available, then the device server shall set the SENSE KEY field, the ADDITIONAL SENSE CODE
field, and the ADDITIONAL SENSE CODE QUALIFIER field to a hierarchy of additional information relating to error
conditions that occurred during the background scan operation. The content of these fields is represented in
the same format used by the sense data (see SPC-6).
The LOGICAL BLOCK ADDRESS field indicates the LBA associated with the medium error.
6.4.3 Background Operation log page
6.4.3.1 Background Operation log page overview
Using the format shown in table 185, the Background Operation log page reports parameters that are specific
to background operations.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
The SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in table 185 for
the Background Operation log page.
The parameter codes for the Background Operation log page are listed in table 186.
Table 185 — Background Operation log page
Bit
Byte
DS
SPF (1b)
PAGE CODE (15h)
SUBPAGE CODE (02h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Background operation parameters
Background operation parameter [first] (if any)
•••
•••
Background operation parameter [last] (if any)
•••
n
Table 186 — Background Operation log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Background Operation
Never
6.4.3.2
Mandatory
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.


6.4.3.2 Background Operation log parameter
The Background Operation log parameter of the Background Operation log page has the format shown in
table 187.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 187 for the
Background Operation log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Background Operation log parameter shall be
set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 187 for the
Background Operation log parameter.
The background operation status (BO_STATUS) field indicates the type of background operation, if any, that is
being performed by the device server as shown in table 188.
Table 187 — Background Operation log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Reserved
TSD
Reserved
FORMAT AND LINKING
PARAMETER LENGTH (4h)
BO_STATUS
Reserved
•••
n
TABLE 188 — BO_STATUS DEFINITIONS
Code
Description
00h
No indication
01h
No advanced background operation being performed
02h
Host initiated advanced background operation being performed
03h
Device initiated advanced background operation being performed
All others
Reserved


6.4.4 Format Status log page
6.4.4.1 Format Status log page overview
Using the format shown table 190, the Format Status log page reports information about the most recent
successful format operation and the state of the direct access block device since that operation was
performed. The parameter codes for the Format Status log page are listed in table 189.
The Format Status log page has the format shown in table 190.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
Table 189 — Format Status log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Format Data Out
Never
6.4.4.2
Mandatory
0001h
Grown Defects During Certification
Never
6.4.4.3
Mandatory
0002h
Total Blocks Reassigned During
Format
Never
6.4.4.4
Mandatory
0003h
Total New Blocks Reassigned
Never
6.4.4.5
Mandatory
0004h
Power On Minutes Since Format
Never
6.4.4.6
Mandatory
0005h to 7FFFh
Reserved
8000h to FFFFh
Vendor specific
Optional
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
Table 190 — Format Status log page
Bit
Byte
DS (1b)
SPF (0b)
PAGE CODE (08h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Format status log parameters
Format status log parameter [first]
•••
•••
Format status log parameter [last]
•••
n


The DS bit, the SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in
table 190 for the Format Status log page.
If a format operation has never been performed by the logical unit, then the log parameter  for each Format
Status log parameter listed in table 189 is not defined by this standard. If a device server begins a format
operation, then the device server shall set each byte of the log parameter data (i.e., bytes four to n of the log
parameter), if any, to FFh for each Format Status log parameter (e.g., if the PARAMETER LENGTH field is set to
02h, then the log parameter data is set to FFFFh).
If the most recent format operation failed or the information for a Format Status log parameter is not available,
then the device server shall return FFh in each byte of the log parameter data (i.e., bytes four to n of the log
parameter), if any, for the Format Status log parameter (e.g., if the PARAMETER LENGTH field is set to 04h, then
the log parameter data shall be set to FFFF_FFFFh). The device server shall set each Format Status log
parameter to be a multiple of four bytes.
6.4.4.2 Format Data Out log parameter
The Format Data Out log parameter of the Format Status log page has the format shown in table 191.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 191 for the
Format Data Out log parameter.
The DU bit, and the FORMAT AND LINKING field for the Format Data Out log parameter shall be set for a binary
format list log parameter as described in SPC-6.
The target save disable (TSD) bit (see SPC-6) shall be set to zero for the Format Data Out log parameter,
indicating that the logical unit saves the Format Data Out log parameter at vendor specific intervals without
any request from an application client.
The PARAMETER LENGTH field is described in SPC-6.
After a successful format operation, the FORMAT DATA OUT field contains the FORMAT UNIT parameter list
(see 5.4.2).
Table 191 — Format Data Out log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (n - 3)
(MSB)
FORMAT DATA OUT
•••
n
(LSB)


6.4.4.3 Grown Defects During Certification log parameter
The Grown Defects During Certification log parameter for the Format Status log page has the format shown in
table 192.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 192 for the
Grown Defects During Certification log parameter.
The DU bit, and the FORMAT AND LINKING field for the Grown Defects During Certification log parameter shall be
set for a binary format list log parameters as described in SPC-6.
The target save disable (TSD) bit (see SPC-6) shall be set to zero for the Grown Defects During Certification
log parameter, indicating that the logical unit saves the Grown Defects During Certification log parameter at
vendor specific intervals without any request from an application client.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 192 for the
Grown Defects During Certification log parameter.
After a successful format operation during which certification was performed, the GROWN DEFECTS DURING
CERTIFICATION field shall indicate the number of defects detected as a result of performing the certification. The
value in the GROWN DEFECTS DURING CERTIFICATION field count reflects only those defects detected and
replaced during the successful format operation that were not already part of the PLIST or GLIST.
After a successful format operation during which certification was not performed, the GROWN DEFECTS DURING
CERTIFICATION field shall be set to zero.
Table 192 — Grown Defects During Certification log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
GROWN DEFECTS DURING CERTIFICATION
•••
(LSB)


6.4.4.4 Total Blocks Reassigned During Format log parameter
The Total Blocks Reassigned During Format log parameter for the Format Status log page has the format
shown in table 193.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 193 for the Total
Blocks Reassigned During Format log parameter.
The DU bit, and the FORMAT AND LINKING field for the Total Blocks Reassigned During Format log parameter
shall be set for a binary format list log parameters described in SPC-6.
The target save disable (TSD) bit (see SPC-6) shall be set to zero for the Total Blocks Reassigned During
Format log parameter, indicating that the logical unit saves the Total Blocks Reassigned During Format log
parameter at vendor specific intervals without any request from an application client.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 193 for the
Total Blocks Reassigned During Format log parameter.
The TOTAL BLOCKS REASSIGNED DURING FORMAT field contains the count of the total number of logical blocks
that were reassigned during the most recent successful format operation.
Table 193 — Total Blocks Reassigned During Format log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0002h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
TOTAL BLOCKS REASSIGNED DURING FORMAT
•••
(LSB)


6.4.4.5 Total New Blocks Reassigned log parameter
The Total New Blocks Reassigned log parameter for the Format Status log page has the format shown in
table 194.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 194 for the Total
New Blocks Reassigned log parameter.
The DU bit, and the FORMAT AND LINKING field for the Total New Blocks Reassigned log parameter shall be set
for a binary format list log parameters described in SPC-6.
The target save disable (TSD) bit (see SPC-6) shall be set to zero for the Total New Blocks Reassigned log
parameter, indicating that the logical unit saves the Total New Blocks Reassigned log parameter at vendor
specific intervals without any request from an application client.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 194 for the
Total New Blocks Reassigned log parameter.
The TOTAL NEW BLOCKS REASSIGNED field contains a count of the total number of logical blocks that have been
reassigned since the completion of the most recent successful format operation.
Table 194 — Total New Blocks Reassigned log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0003h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
TOTAL NEW BLOCKS REASSIGNED
•••
(LSB)


6.4.4.6 Power On Minutes Since Format log parameter
The Power On Minutes Since Format log parameter for the Format Status log page has the format shown in
table 195.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 195 for the
Power On Minutes Since Format log parameter.
The DU bit, and the FORMAT AND LINKING field for the Power On Minutes Since Format log parameter shall be
set for a binary format list log parameter as described in SPC-6.
The target save disable (TSD) bit (see SPC-6) shall be set to zero for the Power On Minutes Since Format log
parameter, indicating that the logical unit saves the Power On Minutes Since Format log parameter at vendor
specific intervals without any request from an application client.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 195 for the
Power On Minutes Since Format log parameter.
The POWER ON MINUTES SINCE FORMAT field contains the unsigned number of usage minutes (i.e., minutes with
power applied regardless of power state) that have elapsed since the most recent successful format
operation.
Table 195 — Power On Minutes Since Format log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0004h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
(MSB)
POWER ON MINUTES SINCE FORMAT
•••
(LSB)


6.4.5 Logical Block Provisioning log page
6.4.5.1 Logical Block Provisioning log page overview
Using the format shown in table 197, the Logical Block Provisioning log page reports the logical block
provisioning status of the logical unit. The parameter codes for the Logical Block Provisioning log page are
listed in table 196.
Table 196 — Logical Block Provisioning log parameters
Parameter
code a
Description
Resettable or
Changeable b
Reference
Support
Resources that are associated with thresholds (0000h to 00FFh)
0000h
Reserved
0001h
Available LBA Mapping Resource Count
Never
6.4.5.2
Optional c
0002h
Used LBA Mapping Resource Count
Never
6.4.5.3
0003h
Available Provisioning Resource
Percentage
Never
6.4.5.4
0004h to 00FFh
Reserved
Resources that are not associated with thresholds (0000h to 00FFh)
0100h
De-duplicated LBA Resource Count
Never
6.4.5.5
Optional
0101h
Compressed LBA Resource Count
Never
6.4.5.6
0102h
Total Efficiency LBA Resource Count
Never
6.4.5.7
0103h to FFEFh
Reserved
FFF0h to FFFFh
Vendor specific
a Parameter codes 0000h to 00FFh are coordinated with the THRESHOLD RESOURCE field (see 6.5.9).
b The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
c If this log page is supported, then at least one Logical Block Provisioning log parameter shall be
supported. A Logical Block Provisioning log parameter in the range 0001h to 00FFh should be provided
to report resource usage for each threshold resource for which a threshold descriptor in the Logical
Block Provisioning mode page (see 6.5.9) is available.


The Logical Block Provisioning log page has the format shown in table 197.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
The DS bit, the SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in
table 197 for the Logical Block Provisioning log page.
Table 197 — Logical Block Provisioning log page
Bit
Byte
DS (1b)
SPF (0b)
PAGE CODE (0Ch)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Logical block provisioning parameter list
Logical block provisioning log parameter [first]
•••
•••
Logical block provisioning log parameter [last]
•••
n


6.4.5.2 Available LBA Mapping Resource Count log parameter
6.4.5.2.1 Available LBA Mapping Resource Count log parameter overview
The Available LBA Mapping Resource Count log parameter of the Logical Block Provisioning log page has the
format shown in table 198.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 198 for the
Available LBA Mapping Resource Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Available LBA Mapping Resource Count shall
be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 198 for the
Available LBA Mapping Resource Count.
The RESOURCE COUNT field indicates an estimate of the number of available LBA mapping resources and is
defined in 6.4.5.2.2.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
Table 198 — Available LBA Mapping Resource Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
•••
(LSB)
Reserved
SCOPE
Reserved
•••
Table 199 — SCOPE field
Code
Description
00b
The scope of the resource count is not reported.
01b
The RESOURCE COUNT field indicates a resource that is dedicated to the logical unit. Usage of
resources on other logical units does not impact the resource count.
10b
The RESOURCE COUNT field indicates resources that  may or may not be dedicated to any logical
unit including the addressed logical unit. Usage of resources on other logical units may impact the
resource count.
11b
Reserved


6.4.5.2.2 RESOURCE COUNT field
The RESOURCE COUNT field indicates an estimate of the number of LBA resources expressed as a number of
threshold sets for the threshold resource indicated by the parameter code value. The nominal number of LBA
resources is calculated as follows:
LBA resources = resource count × threshold set size
where:
resource count
is the value in the RESOURCE COUNT field; and
threshold set size
is the number of LBAs in each threshold set (i.e., 2 (threshold exponent) LBAs,
where the threshold exponent is indicated in the Logical Block Provisioning
VPD page (see 6.6.7)).
6.4.5.3 Used LBA Mapping Resource Count log parameter
The Used LBA Mapping Resource Count log parameter of the Logical Block Provisioning log page has the
format shown in table 200.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 200 for the Used
LBA Mapping Resource Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Used LBA Mapping Resource Count log
parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 200 for the
Used LBA Mapping Resource Count log parameter.
The RESOURCE COUNT field indicates an estimate of the number of used LBA mapping resources and is
defined in 6.4.5.2.2.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
Table 200 — Used LBA Mapping Resource Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0002h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
•••
(LSB)
Reserved
SCOPE
Reserved
•••


6.4.5.4 Available Provisioning Resource Percentage log parameter
6.4.5.4.1 Available Provisioning Resource Percentage log parameter overview
The Available Provisioning Resource Percentage log parameter of the Logical Block Provisioning log page
has the format shown in table 201
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 201 for the
Available Provisioning Resource Percentage log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Available Provisioning Resource Percentage
log parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 201 for the
Available Provisioning Resource Percentage.
The RESOURCE COUNT field indicates an estimate of the percentage of available provisioning resources used
for this logical block provisioning threshold and is defined in 6.4.5.4.2.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
6.4.5.4.2 RESOURCE COUNT field
The RESOURCE COUNT field (see table 202) contains an estimate of the percentage of resources available for
allocation to LBAs as a percentage of the manufacturer's total resources available for allocation. The units for
the reported values are percent and range from 0% to 100%.
Table 201 — Available Provisioning Resource Percentage log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0003h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
(LSB)
Reserved
Reserved
SCOPE
Reserved
•••
Table 202 — RESOURCE COUNT field
Code
Description
0 to 100
0% to 100% of the provisioning resources of the logical unit are available
All others
Reserved


6.4.5.5 De-duplicated LBA Resource Count log parameter
The De-duplicated LBA Resource Count log parameter of the Logical Block Provisioning log page
(see table 203) contains information about de-duplicated LBA resources.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 203 for the
De-duplicated LBA Resource Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the De-duplicated LBA Resource Count log
parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 203 for the
De-duplicated LBA Resource Count log parameter.
The RESOURCE COUNT field indicates an estimate of the number of LBA resources made available as a result
of de-duplication and is defined in 6.4.5.2.2.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
Table 203 — De-duplicated LBA Resource Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0100h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
•••
(LSB)
Reserved
SCOPE
Reserved
•••


6.4.5.6 Compressed LBA Resource Count log parameter
The Compressed LBA Resource Count log parameter of the Logical Block Provisioning log page
(see table 204) contains information about compressed LBA resources.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 204 for the
Compressed LBA Resource Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Compressed LBA Resource Count log
parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 204 for the
Compressed LBA Resource Count log parameter.
The RESOURCE COUNT field indicates an estimate of the number of LBA resources made available as a result
of compression and is defined in 6.4.5.2.2.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
Table 204 — Compressed LBA Resource Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0101h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
•••
(LSB)
Reserved
SCOPE
Reserved
•••


6.4.5.7 Total Efficiency LBA Resource Count log parameter
The Total Efficiency LBA Resource Count log parameter of the Logical Block Provisioning log page
(see table 205) contains information about the combined effects of all LBA resource efficiencies (e.g., the
result of the combination of de-duplicated LBA resources and compressed LBA resources).
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 205 for the Total
Efficiency LBA Resource Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Total Efficiency LBA Resource Count log
parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 205 for the
Total Efficiency LBA Resource Count log parameter.
The RESOURCE COUNT field indicates an estimate of the number of LBA resources made available by the
combined effects of all LBA resource efficiency methods (e.g., de-duplication and compression) and is defined
in 6.4.5.2.2. The algorithm used to calculate this value is not defined by this standard.
The SCOPE field indicates the scope to which the RESOURCE COUNT field applies and is shown in table 199.
Table 205 — Total Efficiency LBA Resource Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0102h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
RESOURCE COUNT
•••
(LSB)
Reserved
SCOPE
Reserved
•••


6.4.6 LPS Misalignment log page
6.4.6.1 Overview
Using the format shown in table 207, the LPS Misalignment log page reports misaligned write command
information (see 4.6.2). The parameter codes for the LPS Misalignment log page are listed in table 206.
The LPS Misalignment log page has the format shown in table 207
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, and the SUBPAGE CODE field are
described in SPC-6 and shall be set to the values shown in table 207 for the LPS Misalignment log page.
The PAGE LENGTH field is defined in SPC-6.
The contents of each LPS misalignment log parameter depends on the value in the PARAMETER CODE field
(see table 206).
Table 206 — LPS Misalignment log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
LPS Misalignment Count
Reset Only
6.4.6.2
Mandatory
0001h to F000h
LPS Misalignment
Reset Only
6.4.6.3
Optional b
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
b If the LPS Misalignment log page is supported, then at least one LPS Misalignment log parameter shall
be supported.
Table 207 — LPS Misalignment log page
Bit
Byte
DS
SPF (1b)
PAGE CODE (15h)
SUBPAGE CODE (03h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
LPS misalignment log parameters
LPS misalignment log parameter [first] (see table 208 and table 209)
•••
•••
LPS misalignment log parameter [last] (see table 208 and table 209)
•••
n


6.4.6.2 LPS Misalignment Count log parameter
The LPS Misalignment Count log parameter has the format shown in table 208 and indicates the number of
LPS Misalignment log parameters that are available.
The PARAMETER CODE field is described in SPC-6 and shall be set as shown in table 208 for the LPS
Misalignment Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the LPS Misalignment Count log parameter shall
be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 208 for the
LPS Misalignment Count log parameter.
The MAX_LPSM field indicates the maximum number of LPS Misalignment log parameters (see 6.4.6.3)
supported by the device server. The device server may support any number of LPS Misalignment log
parameters from 0001h to F000h inclusive.
The LPS MISALIGNMENT COUNT field indicates the number of LPS Misalignment log parameters that are
available.
6.4.6.3 LPS Misalignment log parameter
An LPS Misalignment log parameter has the format shown in table 209. If no misaligned write commands
have been processed since the most recent reset of the LPS Misalignment log page then no LPS
Table 208 — LPS Misalignment Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
(MSB)
MAX_LPSM
(LSB)
(MSB)
LPS MISALIGNMENT COUNT
(LSB)


Misalignment log parameters shall be present. LPS Misalignment log parameters are added as described in
4.6.2.
The PARAMETER CODE field is described in SPC-6. A PARAMETER CODE field set to 0001h indicates the oldest
misaligned write command reported by the log, and successive values indicate successive misaligned writes.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for a LPS Misalignment log parameter shall be set for
a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is defined in SPC-6 and shall be set to the value shown in table 209 for a LPS
Misalignment log parameter.
The LBA OF MISALIGNED BLOCK field indicates the starting LBA associated with the misaligned write command.
6.4.7 Non-volatile Cache log page
6.4.7.1 Non-volatile Cache log page overview
Using the format shown in table 211, the Nonvolatile Cache log page reports the status of battery backup for a
nonvolatile cache. The parameter codes for the Nonvolatile Cache log page are listed in table 210.
Table 209 — LPS Misalignment log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h to F000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (08h)
(MSB)
LBA OF MISALIGNED BLOCK
•••
(LSB)
Table 210 — Nonvolatile Cache log parameters
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Remaining Nonvolatile Time
Never
6.4.7.2
Mandatory
0001h
Maximum Nonvolatile Time
Never
6.4.7.3
Mandatory
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.


The Nonvolatile Cache log page has the format shown in table 211.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
The SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in table 211 for
the Nonvolatile Cache log page.
6.4.7.2 Remaining Nonvolatile Time log parameter
The Remaining Nonvolatile Time log parameter of the Nonvolatile Cache log page has the format shown in
table 212.
Table 211 — Nonvolatile Cache log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (17h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Nonvolatile cache log parameters
Non-volatile cache log parameter [first] (see table 210)
•••
•••
Nonvolatile cache log parameter [last] (see table 210)
•••
n
Table 212 — Remaining Nonvolatile Time log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
Obsolete
(MSB)
REMAINING NONVOLATILE TIME
•••
(LSB)


The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 212 for the
Remaining Nonvolatile Time log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Remaining Nonvolatile Time log parameter
shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 212 for the
Remaining Nonvolatile Time log parameter.
The REMAINING NONVOLATILE TIME field is shown in table 213.
6.4.7.3 Maximum Nonvolatile Time log parameter
The Maximum Nonvolatile Time log parameter of the Nonvolatile Cache log page has the format shown in
table 214.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 214 for the
Maximum Nonvolatile Time log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Maximum Nonvolatile Time log parameter
shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 214 for the
Maximum Nonvolatile Time log parameter.
Table 213 — REMAINING NONVOLATILE TIME field
Code
Description
00_0000h
Nonvolatile cache is volatile, either permanently or temporarily (e.g., if batteries require
recharging).
00_0001h
Nonvolatile cache is expected to remain nonvolatile for an unknown amount of time (e.g., if
battery status is unknown)
00_0002h to
FF_FFFEh
Nonvolatile cache is expected to remain nonvolatile for the number of minutes indicated
(e.g., for the life of the battery supplying power to random access memory).
FF_FFFFh
Nonvolatile cache is indefinitely nonvolatile.
Table 214 — Maximum Nonvolatile Time log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
Obsolete
(MSB)
MAXIMUM NONVOLATILE TIME
•••
(LSB)


The MAXIMUM NONVOLATILE TIME field is shown in table 215.
6.4.8 Pending Defects log page
6.4.8.1 Overview
Using the format shown in table 217, the Pending Defects log page reports an unsorted list of logical blocks
for which the device server has detected an unrecovered medium error. The parameter codes for the Pending
Defects log page are listed in table 216.
Table 215 — MAXIMUM NONVOLATILE TIME field
Code
Description
00_0000h
Nonvolatile cache is volatile
00_0001h
Reserved
00_0002h to
FF_FFFEh
Nonvolatile cache is capable of being nonvolatile for the estimated number of minutes
indicated. If the time is based on batteries, then the time shall be based on the last full
charge capacity rather than the design capacity of the batteries.
FF_FFFFh
Nonvolatile cache is indefinitely nonvolatile.
Table 216 — Pending Defects log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Pending Defect
Count
Never
6.4.8.2
Mandatory
0001h to F000h
Pending Defect
Never
6.4.8.3
Optional b
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
b If the Pending Defects log page is supported, then at least one Pending Defect log parameter shall be
supported.


The Pending Defects log page has the format shown in table 217
The subpage format (SPF) bit, the PAGE CODE field, and the SUBPAGE CODE field are described in SPC-6 and
shall be set to the values shown in table 217 for the Pending Defects log page.
The disable save (DS) bit, and the PAGE LENGTH field are described in SPC-6.
The contents of each pending defect parameter depends on the value in its PARAMETER CODE field
(see table 216).
6.4.8.2 Pending Defect Count log parameter
The Pending Defect Count log parameter has the format shown in table 218 and indicates the number of
Pending Defect log parameters that are available.
Table 217 — Pending Defects log page
Bit
Byte
DS
SPF (1b)
PAGE CODE (15h)
SUBPAGE CODE (01h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Pending defect parameters
Pending defect parameter [first]
•••
•••
Pending defect parameter [last]
•••
n
Table 218 — Pending Defect Count log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
(MSB)
PENDING DEFECT COUNT
•••
(LSB)


The PARAMETER CODE field is described in SPC-6 and shall be set as shown in table 218 for the Pending
Defect Count log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Pending Defect Count log parameter shall be
set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 218 for the
Pending Defect Count log parameter.
The PENDING DEFECT COUNT field indicates the number of Pending Defect log parameters that are available.
6.4.8.3 Pending Defect log parameter
A Pending Defect log parameter has the format shown in table 219. If no unrecovered medium errors have
occurred then no Pending Defect log parameters shall be present. A Pending Defect log parameter shall be
added for each LBA for which the device server has detected an unrecovered medium error that is not:
a)
a pseudo unrecovered read error (see 4.18.2);
b)
a predicted unrecovered read error (see 4.19.3.3); or
c)
a predicted unrecovered write error (see 4.19.3.5).
If all of the supported parameter code values have been used and a new defect is discovered, then the device
server shall not add more Pending Defect log parameters and the PENDING ERROR COUNT field shall not be
changed.
Pending Defect log parameters may duplicate information that is in Background Scan Results log parameters
in the Background Scan log page (see 6.4.2).
A Pending Defect log parameter shall be removed if the indicated LBA:
a)
is reassigned without error;
b)
is written without error; or
c)
is read without error.
A Pending Defect log parameter may be removed if the indicated LBA is unmapped without error.
A sanitize overwrite operation (see 5.30.2.2) and a format operation (see 5.4.1) shall cause all Pending Defect
log parameters to be removed..
Table 219 — Pending Defect log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h to F000h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (0Ch)
(MSB)
ACCUMULATED POWER ON HOURS
•••
(LSB)
(MSB)
LOGICAL BLOCK ADDRESS
•••
(LSB)


The PARAMETER CODE field is described in SPC-6 and shall be set as shown in table 219 for a Pending Defect
log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for a Pending Defect log parameter shall be set for a
binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is defined in SPC-6 and shall be set to the value shown in table 219 for a
Pending Defect log parameter.
The ACCUMULATED POWER ON HOURS field indicates the number of hours that the device server has been
powered on since manufacturing at the time the Pending Defect log parameter was created. A value of
FFFF_FFFFh indicates that the accumulated power on hours value is unknown.
The LOGICAL BLOCK ADDRESS field indicates the LBA associated with the unrecovered medium error.
6.4.9 Solid State Media log page
6.4.9.1 Solid State Media log page overview
Using the format shown in table 220, the Solid State media log page reports parameters that are specific to
SCSI target devices that contain solid state media.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, the SUBPAGE CODE field, and the
PAGE LENGTH field are described in SPC-6.
The SPF bit, the PAGE CODE field, and the SUBPAGE CODE field shall be set to the values shown in table 220 for
the Solid State Media log page.
Table 220 — Solid State Media log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (11h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Solid state media log parameters
Solid state media parameter [first]
•••
•••
Solid state media parameter [last]
•••
n


The parameter codes for the Solid State Media log page are listed in table 221.
6.4.9.2 Percentage Used Endurance Indicator log parameter
The Percentage Used Endurance Indicator log parameter of the Solid Sate Media log page has the format
shown in table 222.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 222 for the
Percentage Used Endurance Indicator log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Percentage Used Endurance Indicator log
parameter shall be set for a binary format list log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 222 for the
Percentage Used Endurance Indicator log parameter.
The PERCENTAGE USED ENDURANCE INDICATOR field indicates an estimate of the percentage of a SCSI target
device that contains solid state media life that has been used. The value in the field shall be set to zero at the
time of manufacture. A value of 100 indicates that the estimated endurance of the SCSI target device that
contains solid state media has been consumed, but may not indicate the presence of a solid state media
failure in that SCSI target device (e.g., the minimum power-off data retention capability has been reached for
a SCSI target devices that contains solid state media while the media is still functional). The value is allowed
to exceed 100. Values greater than 254 shall be reported as 255. The device server shall update the value at
least once per power on hour.
Table 221 — Solid State Media log parameters
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0001h
Percentage Used Endurance
Indicator
Never
6.4.9.2
Mandatory
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.
Table 222 — Percentage Used Endurance Indicator log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – binary format list log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (04h)
Reserved
•••
PERCENTAGE USED ENDURANCE INDICATOR


6.4.10 Utilization log page
6.4.10.1 Utilization log page overview
Using the format shown in table 223, the Utilization log page reports estimates of the rate at which device
wear factors (e.g., damage to the recording medium) are being used.
The disable save (DS) bit, the subpage format (SPF) bit, the PAGE CODE field, and the SUBPAGE CODE field are
described in SPC-6 and shall be set to the values shown in table 223 for the Utilization log page.
The PAGE LENGTH field is described in SPC-6.
The parameter codes for the Utilization log page are shown in table 224.
Table 223 — Utilization log page
Bit
Byte
DS (1b)
SPF (1b)
PAGE CODE (0Eh)
SUBPAGE CODE (01h)
(MSB)
PAGE LENGTH (n - 3)
(LSB)
Utilization log parameters
Utilization log parameter [first]
•••
•••
Utilization log parameter [last]
•••
n
Table 224 — Utilization log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
0000h
Workload Utilization
Never
6.4.10.2
Mandatory
0001h
Utilization Usage Rate Based on
Date and Time
Never
6.4.10.3
Optional
All others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 6.4.1.2.


6.4.10.2 Workload Utilization log parameter
The Workload Utilization log parameter for the Utilization log page has the format shown in table 225.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 225 for the
Workload Utilization log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Workload Utilization log parameter shall be set
for a bounded data counter log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 225 for the
Workload Utilization log parameter.
The WORKLOAD UTILIZATION field (see table 226) contains an estimate of the utilization associated with the
logical unit as a percentage of the manufacturer's designs for various wear factors (e.g., wear of the medium,
head load events), if any. The units for the reported values are percent times 100 and range from 0.00% to
655.35%.
Table 225 — Workload Utilization log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – bounded data counter log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (02h)
(MSB)
WORKLOAD UTILIZATION
(LSB)
Table 226 — WORKLOAD UTILIZATION field
Code
Description
0 to 9 999
Less than (i.e., 0.00% to 99.99% of) the designed workload has been utilized.
10 000
Exactly the designed workload for the device has been utilized.
10 001 to 65 534
Greater than (i.e., 100.01% to 655.34% of) the designed workload has been
utilized.
65 535
Greater than 655.34% of the designed workload has been utilized.


6.4.10.3 Utilization Usage Rate Based on Date and Time
The Utilization Rate Based on Date and Time log parameter for the Utilization log page has the format shown
in table 227. If the interval that begins at the date and time of manufacture and ends at the timestamp that is
reported by a REPORT TIMESTAMP command is not able to be determined (e.g.,the current date and time
has not been initialized by a SET TIMESTAMP command (see SPC-6) or the current date and time is prior to
the date and time of manufacture), then the Utilization Rate Based on Date and Time log parameter shall not
be returned in the Utilization log page.
The PARAMETER CODE field is described in SPC-6 and shall be set to the value shown in table 227 for the
Utilization Rate Based on Date and Time log parameter.
The DU bit, the TSD bit, and the FORMAT AND LINKING field for the Utilization Rate Based on Date and Time log
parameter shall be set for a bounded data counter log parameter as described in SPC-6.
The PARAMETER LENGTH field is described in SPC-6 and shall be set to the value shown in table 227 for the
Utilization Rate Based on Date and Time log parameter.
The DATE AND TIME BASED UTILIZATION RATE field (see table 228) contains an estimate of the rate at which
device wear factors (e.g., damage to the recording medium) associated with the logical unit have been used
during the interval that begins at the date and time of manufacture and ends at the timestamp that is reported
by a REPORT TIMESTAMP command (i.e., the current value of a device clock) (see SPC-6).
Table 227 — Utilization Rate Based on Date and Time log parameter format
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – bounded data counter log parameter (see SPC-6)
DU
Obsolete
TSD
Obsolete
FORMAT AND LINKING
PARAMETER LENGTH (02h)
DATE AND TIME BASED UTILIZATION RATE
Reserved
Table 228 — DATE AND TIME BASED UTILIZATION RATE field
Code
Description
0 to 99
The Workload Utilization usage rate has been less than (i.e., 0% to 99% of) the
designed usage rate during the interval that begins at the date and time of
manufacture and ends at the timestamp.
The Workload Utilization usage rate has been the exact designed usage rate during
the interval that begins at the date and time of manufacture and ends at the
timestamp.
101 to 254
The Workload Utilization usage rate has been greater than (i.e., 101% to 254% of)
the designed usage rate during the interval that begins at the date and time of
manufacture and ends at the timestamp.
The Workload Utilization usage rate has been greater than 254% of designed
usage rate during the interval that begins at the date and time of manufacture and
ends at the timestamp.
