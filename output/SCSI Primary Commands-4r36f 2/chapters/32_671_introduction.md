# 6.7.1 Introduction

6.7 LOG SELECT command
6.7.1 Introduction
The LOG SELECT command (see table 183) provides a means for an application client to manage statistical
information maintained by the SCSI target device about the SCSI target device or its logical units. Device
servers that implement the LOG SELECT command shall also implement the LOG SENSE command. Struc-
tures in the form of log parameters within log pages are defined as a way to manage the log data. The LOG
SELECT command provides a method for sending zero or more log pages via the Data-Out Buffer. This
standard defines the format of the log pages (see 7.3) and defines some of the conditions and events that are
logged.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 183 for the LOG SELECT
command.
The parameter code reset (PCR) bit instructs a device server whether or not to set parameters to their vendor
specific default values (e.g., zero) as described in table 186.
The save parameters (SP) bit instructs a device server whether or not to save parameters to non-volatile
memory as described in table 186.
Table 183 — LOG SELECT command
Bit
Byte
OPERATION CODE (4Ch)
Reserved
PCR
SP
PC
PAGE CODE
SUBPAGE CODE
Reserved

•••

(MSB)
PARAMETER LIST LENGTH
(LSB)
CONTROL


The page control (PC) field specifies which values the device server shall process for bounded data counter
log parameters (see 7.3.2.2.2.2) and unbounded data counter log parameters (see 7.3.2.2.2.3) in response to
a LOG SELECT command as described in table 184. The PC field shall be ignored for ASCII format list log
parameters (see 7.3.2.2.2.4) and binary format list log parameters (see 7.3.2.2.2.5).
When evaluated together, the combination of the values in the PCR bit, the SP bit, and the PC field specify the
actions that a SCSI target device performs while processing a LOG SELECT command.
If the PARAMETER LIST LENGTH field is set to zero, the PAGE CODE field and SUBPAGE CODE field specify the log
page or log pages to which the other CDB fields apply (see 6.7.2).
Since each log page in the parameter list contains a PAGE CODE field and SUBPAGE CODE field (see 7.3.2.1), the
device server shall terminate the command with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB, if:
a)
the PARAMETER LIST LENGTH field is set to a value other than zero, and:
A)
the PAGE CODE field is set to a value other than zero; or
B)
the SUBPAGE CODE field is set to a value other than zero.
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter list that shall be located in the
Data-Out Buffer.
If the PARAMETER LIST LENGTH field is set to a value other than zero, the actions that a SCSI target device
performs after receiving a LOG SELECT command are determined by the values in the PCR bit, the SP bit, and
the PC field as described in table 349 (see 7.3.2.1).
If the PARAMETER LIST LENGTH field is set to zero, no log pages shall be transferred. This condition shall not be
considered an error. The LOG SELECT command shall be processed as described in 6.7.2.
The CONTROL byte is defined in SAM-5.
Table 184 — Page control (PC) field
Value
Description
00b
Threshold values a
01b
Cumulative values a
10b
Default threshold values
11b
Default cumulative values
a The threshold values and cumulative values for data counter parameters are:
1)
the current values if there has been an update to a cumulative parameter value (e.g., by a LOG
SELECT command or by a device specific event) in the specified page or pages since the last
logical unit reset occurred;
2)
the saved values, if saved parameters are implemented, current values have been saved, and
an update has not occurred since the last logical unit reset; or
3)
the vendor specific default values, if saved values are not available or not implemented.
