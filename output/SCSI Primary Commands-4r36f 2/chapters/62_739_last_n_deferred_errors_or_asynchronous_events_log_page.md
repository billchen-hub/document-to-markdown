# 7.3.9 Last n Deferred Errors or Asynchronous Events log page

The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 387 for the Informa-
tional Exceptions General log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Informational Excep-
tions General log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1. The parameter length shall be at least 04h.
If the INFORMATIONAL EXCEPTION ADDITIONAL SENSE CODE field is set to zero, no informational exception
condition exists and contents of the INFORMATIONAL EXCEPTION ADDITIONAL SENSE CODE QUALIFIER field are
unspecified. If the INFORMATIONAL EXCEPTION ADDITIONAL SENSE CODE field is set to a value other than zero, an
informational exception condition exists that has an additional sense code indicated by INFORMATIONAL
EXCEPTION ADDITIONAL SENSE CODE field and an ADDITIONAL SENSE CODE QUALIFIER indicated by the INFORMA-
TIONAL EXCEPTION ADDITIONAL SENSE CODE QUALIFIER field.
The MOST RECENT TEMPERATURE READING field indicates the temperature in degrees Celsius of the SCSI target
device at the time the LOG SENSE command is performed. Temperatures equal to or less than zero degrees
Celsius shall be indicated by a value of zero. If the device server is unable to detect a valid temperature
because of a sensor failure or other condition, the value returned shall be FFh. The temperature should be
reported with an accuracy of plus or minus three Celsius degrees while the device is operating at a steady
state within the environmental limits specified for the device.
7.3.9 Last n Deferred Errors or Asynchronous Events log page
7.3.9.1 Overview
Using the format shown in table 389, the Last n Deferred Errors or Asynchronous Events log page (page code
0Bh) provides one or more Deferred Error or Asynchronous Event log parameters (see 7.3.9.2). The number
of Deferred Error or Asynchronous Event log parameters supported (i.e., n) is vendor specific. The parameter
codes for the Last n Deferred Errors or Asynchronous Events log page are listed in table 388.
Table 388 — Last n Deferred Errors or Asynchronous Events log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Deferred Error or
Asynchronous Event
Reset Only
7.3.9.2
Mandatory
0001h to FFFFh
Optional
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


The Last n Deferred Errors or Asynchronous Events log page has the format shown in table 389.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 389 for the Last n Deferred Errors
or Asynchronous Events log page.
The contents of each deferred error or asynchronous event log parameter are described in 7.3.9.2. The
device server shall assign parameter codes to log parameters as follows:
a)
if the vendor specific number of supported deferred error or asynchronous event log parameters has
not been exceeded, then the parameter code in each log parameter shall indicate the relative time at
which the deferred error or asynchronous event occurred. A higher parameter code indicates that the
deferred error or asynchronous event occurred at a more recent time; or
b)
if the vendor specific number of supported deferred error or asynchronous event log parameters has
been exceeded, then:
A)
the log parameter with the oldest data shall be overwritten with the newest data (i.e., after the
highest supported parameter code is used, reporting wraps so that the next deferred error or
asynchronous event is reported in the log parameter with parameter code zero); and
B)
if the RLEC bit is set to one in the Control mode page (see 7.5.8) and a LOG SELECT command
that transfers the Last n Deferred Errors or Asynchronous Events log page completes without
error, except for the parameter code being at its maximum value, then the command shall be
terminated with CHECK CONDITION status, with the sense key set to RECOVERED ERROR,
and the additional sense code set to LOG LIST CODES EXHAUSTED.
Table 389 — Last n Deferred Errors or Asynchronous Events log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (0Bh)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Deferred error or asynchronous event log parameters
Deferred error or asynchronous event log
parameter (see 7.3.9.2) [first]
•••
•••
Deferred error or asynchronous event log
parameter (see 7.3.9.2) [last]
•••
n
