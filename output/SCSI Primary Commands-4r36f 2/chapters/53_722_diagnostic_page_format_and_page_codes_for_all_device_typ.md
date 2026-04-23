# 7.2.2 Diagnostic page format and page codes for all device types

7 Parameters for all device types
7.1 Overview
Parameters for all device types are defined in this clause as follows:
a)
diagnostic parameters are defined in 7.2;
b)
log parameters are defined in 7.3;
c)
medium auxiliary attributes are defined in 7.4;
d)
mode parameters are defined in 7.5;
e)
protocol specific parameters are defined in 7.6;
f)
security parameters are defined in 7.7; and
g)
vital product data are defined in 7.8.
7.2 Diagnostic parameters
7.2.1 Summary of diagnostic page codes
The page code assignments for diagnostic pages are summarized in table 343.
7.2.2 Diagnostic page format and page codes for all device types
This subclause describes the diagnostic page structure and the diagnostic pages that are applicable to all
SCSI devices. Diagnostic pages specific to each device type are described in the command standard that
applies to that device type.
A SEND DIAGNOSTIC command with a PF bit set to one specifies that the SEND DIAGNOSTIC parameter
list consists of a single diagnostic page and that the data returned by the subsequent RECEIVE DIAGNOSTIC
Table 343 — Summary of diagnostic page codes
Diagnostic page description
Page code
Reference
Defined by SES-3 for:
a)
standalone enclosure services devices (i.e., logical
units with the PERIPHERAL DEVICE TYPE field set to
0Dh in standard INQUIRY data (see 6.6.2)); and
b)
attached enclosure services devices (i.e., logical
units with the ENCSERV bit set to one in standard
INQUIRY data).
01h to 2Fh
SES-3
Protocol Specific
3Fh
7.2.3
Supported Diagnostic Pages
00h
7.2.4
Restricted (see applicable command standard)
40h to 7Fh
Vendor specific a
Reserved
All other codes
A numeric ordered listing of diagnostic page codes is provided in E.4.
a The following page codes are vendor specific: 80h to FFh.


RESULTS command that has the PCV bit set to zero shall use the diagnostic page format defined in table 344.
A RECEIVE DIAGNOSTIC RESULTS command with a PCV bit set to one specifies that the device server
return a diagnostic page using the format defined in table 344.
Each diagnostic page defines a function or operation that the device server shall perform as a result of a
SEND DIAGNOSTIC command or the information being returned as a result of a RECEIVE DIAGNOSTIC
RESULTS command with the PCV bit equal to one. The diagnostic parameters contain data that is formatted
according to the page code specified.
The PAGE CODE field (see 7.2.1) identifies the diagnostic page.
The PAGE LENGTH field indicates the number of bytes that follow in the diagnostic parameters. If the application
client sends a SEND DIAGNOSTIC command with a parameter list containing a PAGE LENGTH field that results
in the truncation of any parameter, then the command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
The diagnostic parameters are defined for each diagnostic page code. The diagnostic parameters within a
diagnostic page may be defined differently in a SEND DIAGNOSTIC command than in a RECEIVE
DIAGNOSTIC RESULTS command.
Table 344 — Diagnostic page format
Bit
Byte
PAGE CODE
Page code specific
(MSB)
PAGE LENGTH (n-3)
(LSB)
Diagnostic parameters
•••
n
