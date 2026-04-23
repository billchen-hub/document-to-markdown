# 7.2.4 Supported Diagnostic Pages

7.2.3 Protocol Specific
The Protocol Specific diagnostic page (see table 345) provides access to SCSI transport protocol specific
diagnostic parameters.
The PAGE CODE field is described in 7.2.2, and shall be set to 3Fh to indicate a Protocol Specific diagnostic
page follows.
The PROTOCOL IDENTIFIER field contains one of the values shown in table 477 (see 7.6.1) to identify the SCSI
transport protocol standard that defines the SCSI transport protocol specific diagnostic parameters. The SCSI
transport protocol specific data is defined by the corresponding SCSI transport protocol standard.
The PAGE LENGTH field specifies the length in bytes of the following supported page list.
The SCSI transport protocol specific diagnostic parameters are defined by the SCSI transport protocol
standard that corresponds to the value in the PROTOCOL IDENTIFIER field.
7.2.4 Supported Diagnostic Pages
The Supported Diagnostic Pages diagnostic page (see table 346) returns the list of diagnostic pages imple-
mented by the device server. This diagnostic page shall be implemented if the device server implements the
diagnostic page format option of the SEND DIAGNOSTIC and RECEIVE DIAGNOSTIC RESULTS
commands.
Table 345 — Protocol Specific diagnostic page
Bit
Byte
PAGE CODE (3Fh)
Reserved
PROTOCOL IDENTIFIER
(MSB)
PAGE LENGTH (n-3)
(LSB)
SCSI transport protocol specific
diagnostic parameters
•••
n
Table 346 — Supported Diagnostic Pages diagnostic page
Bit
Byte
PAGE CODE (00h)
Reserved
(MSB)
PAGE LENGTH (n-3)
(LSB)
SUPPORTED PAGE LIST
•••
n


The definition of this diagnostic page for the SEND DIAGNOSTIC command includes only the first four bytes.
If the PAGE LENGTH field is not zero, the device server shall terminate the SEND DIAGNOSTIC command with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST. This diagnostic page instructs the device server to make available
the list of all supported diagnostic pages to be returned by a subsequent RECEIVE DIAGNOSTIC RESULTS
command.
The definition of this diagnostic page for the RECEIVE DIAGNOSTIC RESULTS command includes the list of
diagnostic pages supported by the device server.
The PAGE CODE field is described in 7.2.2, and shall be set to 00h to indicate a Supported Diagnostics Pages
diagnostic page follows.
The PAGE LENGTH field indicates the length in bytes of the following supported page list.
The SUPPORTED PAGE LIST field shall contain a list of all diagnostic page codes, one per byte, implemented by
the device server in ascending order beginning with page code 00h.


7.3 Log parameters
7.3.1 Summary of log page codes
The page code assignments for log pages are summarized in table 347.
Table 347 — Summary of log page codes
Log page name
Page code
Subpage code
Reference
Application Client
0Fh
00h
7.3.3
Buffer Over-Run/Under-Run
01h
00h
7.3.4
Cache Memory Statistics
19h
20h
7.3.5
General Statistics and Performance
19h
00h
7.3.6
Group Statistics and Performance (1 to 31)
19h
01h to 1Fh
7.3.6
Informational Exceptions
2Fh
00h
7.3.8
Last n Deferred Errors or Asynchronous Events
0Bh
00h
7.3.9
Last n Error Events
07h
00h
7.3.10
Non-Medium Error
06h
00h
7.3.11
Power Condition Transitions
1Ah
00h
7.3.12
Protocol Specific Port a
18h
00h to FEh
7.3.13
Read Error Counters
03h
00h
7.3.14
Read Reverse Error Counters
04h
00h
7.3.15
Self-Test Results
10h
00h
7.3.16
Start-Stop Cycle Counter
0Eh
00h
7.3.17
Supported Log Pages
00h
00h
7.3.18
Supported Log Pages and Subpages
00h
FFh
7.3.19
Supported Subpages
01h to 3Fh
FFh
7.3.20
Temperature
0Dh
00h
7.3.21
Verify Error Counters
05h
00h
7.3.22
Write Error Counters
02h
00h
7.3.23
Reserved (may be used by specific device types)
08h to 0Ah
00h to FEh
0Ch
00h to FEh
11h to 17h
00h to FEh
1Bh to 2Eh
00h to FEh
Vendor specific b
Reserved
All other codes
A numeric ordered listing of log pages codes and subpage codes is provided in E.5.
a Each SCSI transport protocol standard may define a different name for these log pages.
b The following combinations page codes and subpage codes are vendor specific: 30h to 3Eh/00h to FEh.
