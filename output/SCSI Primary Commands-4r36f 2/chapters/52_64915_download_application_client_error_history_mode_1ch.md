# 6.49.15 Download application client error history mode (1Ch)

The MODE SPECIFIC field is reserved.
Device servers in SCSI target devices that receive a WRITE BUFFER command with this mode shall
terminate the command with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and
the additional sense code set to INVALID FIELD IN CDB.
6.49.15 Download application client error history mode (1Ch)
In this mode the device server transfers application client error history from the application client and stores it
in the error history (see 5.5). The format of the application client error history parameter list is defined in table
340.
The MODE SPECIFIC field is reserved.
The BUFFER ID field and BUFFER OFFSET field shall be ignored in this mode.
Upon successful completion of a WRITE BUFFER command, the information contained in the application
client error history parameter list shall be appended to the application client error history in a format deter-
mined by the logical unit.
The PARAMETER LIST LENGTH field specifies the length in bytes of the application client error history parameter
list that shall be transferred from the application client to the device server. If the PARAMETER LIST LENGTH field
specifies a transfer that exceeds the error history capacity, the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB.
The device server shall not return an error based on the contents of any of the field values defined in table 340
except:
a)
the CLR bit;
b)
the ERROR LOCATION LENGTH field; and


c)
the APPLICATION CLIENT ERROR HISTORY LENGTH field.
The T10 VENDOR IDENTIFICATION field contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying the
vendor providing the application client error history. The T10 vendor identification shall be one assigned by
INCITS. A list of assigned T10 vendor identifications is in Annex F and on the T10 web site
(http://www.t10.org).
Table 340 — Application client error history parameter list format
Bit
Byte
(MSB)
T10 VENDOR IDENTIFICATION
•••
(LSB)
(MSB)
ERROR TYPE
(LSB)
Reserved
CLR
Reserved
(MSB)
TIMESTAMP
•••
(LSB)
Reserved
Reserved
CODE SET
ERROR LOCATION FORMAT
(MSB)
ERROR LOCATION LENGTH (m-25)
(LSB)
(MSB)
APPLICATION CLIENT ERROR HISTORY LENGTH (n-m)
(LSB)
(MSB)
ERROR LOCATION
•••
m
(LSB)
m+1
APPLICATION CLIENT ERROR HISTORY
•••
n


The ERROR TYPE field (see table 341) specifies the error detected by the application client.
If the CLR_SUP bit is set to one in the error history directory parameter data (see 6.18.9.2), a CLR bit set to one
specifies that the device server shall:
a)
clear the portions of the error history that the device server allows to be cleared; and
b)
ignore any application client error history specified in the parameter list.
If the CLR_SUP bit is set to one in the error history directory parameter data, a CLR bit set to zero specifies that
the device server shall:
a)
not clear the error history; and
b)
process all application client error history specified in the parameter list.
If the CLR_SUP bit is set to zero in the error history directory parameter data, the device server shall ignore the
CLR bit.
The TIMESTAMP field shall contain:
a)
a time based on the timestamp reported by the REPORT TIMESTAMP command, if the device server
supports a device clock (see 5.2);
b)
the number of milliseconds that have elapsed since midnight, 1 January 1970 UT; or
c)
zero, if the application client is not able to determine the UT of the log entry.
The CODE SET field contains a code set enumeration (see 4.3.3) that indicates the format of the APPLICATION
CLIENT ERROR HISTORY field.
The ERROR LOCATION FORMAT field (see table 342) specifies the format of the ERROR LOCATION field.
Table 341 — ERROR TYPE field
Code
Description
0000h
No error specified by the application client
0001h
An unknown error was detected by the application client
0002h
The application client detected corrupted data
0003h
The application client detected a permanent error
0004h
The application client detected a service response of
SERVICE DELIVERY OR TARGET FAILURE (see SAM-5).
0005h to 7FFFh
Reserved
8000h to FFFFh
Vendor specific
Table 342 — ERROR LOCATION FORMAT field
Code
Description
00h
No error history location specified by the application client
01h
For direct-access block devices (see SBC-3 and RBC), the ERROR LOCATION
field specifies the logical block address associated the specified application
client error history. For other peripheral device types, this code is reserved.
02h to 7Fh
Reserved
80h to FFh
Vendor specific


The ERROR LOCATION LENGTH field specifies the length of the ERROR LOCATION field. The ERROR LOCATION
LENGTH field value shall be a multiple of four. An ERROR LOCATION LENGTH field set to zero specifies that there
is no error location information.
The APPLICATION CLIENT ERROR HISTORY LENGTH field specifies the length of the APPLICATION CLIENT ERROR
HISTORY field. The APPLICATION CLIENT ERROR HISTORY LENGTH field value shall be a multiple of four. An APPLI-
CATION CLIENT ERROR HISTORY field set to zero specifies that there is no vendor specific information.
The ERROR LOCATION field specifies the location at which the application client detected the error, in the format
specified by the ERROR LOCATION FORMAT field.
The APPLICATION CLIENT ERROR HISTORY field specifies vendor specific application client error history (see
5.5.1).
