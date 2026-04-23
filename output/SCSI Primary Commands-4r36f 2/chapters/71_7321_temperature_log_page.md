# 7.3.21 Temperature log page

7.3.21 Temperature log page
7.3.21.1 Overview
Using the format shown in table 429, the Temperature log page (page code 0Dh) provides information about
the current operating temperature of the SCSI Target Device using the parameter codes listed in table 428.
The Temperature log page has the format shown in table 429.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 429 for the Temperature log page.
The contents of each temperature log parameter depends on the value in its PARAMETER CODE field (see table
428).
Table 428 — Temperature log page parameter codes
Parameter
code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h
Temperature
Never
7.3.21.2
Mandatory
0001h
Reference Temperature
Never
7.3.21.3
Optional
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
Table 429 — Temperature log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (0Dh)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Temperature log parameters
Temperature log parameter (see table 428) [first]
•••
•••
Temperature log parameter (see table 428) [last]
•••
n


7.3.21.2 Temperature log parameter
The Temperature log parameter has the format shown in table 430.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 430 for the Temper-
ature log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Temperature log
parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 430 for the
Temperature log parameter.
The TEMPERATURE field indicates the temperature of the SCSI target device in degrees Celsius at the time the
LOG SENSE command is performed. Temperatures equal to or less than zero degrees Celsius shall cause
the TEMPERATURE field to be set to zero. If the device server is unable to detect a valid temperature because of
a sensor failure or other condition, then the TEMPERATURE field shall be set to FFh. The temperature should be
reported with an accuracy of plus or minus three Celsius degrees while the SCSI target device is operating at
a steady state within its environmental limits.
No comparison is performed between the contents of the TEMPERATURE field and the contents of the optional
REFERENCE TEMPERATURE field (see 7.3.21.3).
Table 430 — Temperature log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0000h)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (02h)
Reserved
TEMPERATURE


7.3.21.3 Reference Temperature log parameter
The Reference Temperature log parameter has the format shown in table 431.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 431 for the Reference
Temperature log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Reference Temper-
ature log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 431 for the
Reference Temperature log parameter.
The REFERENCE TEMPERATURE field indicates the maximum reported sensor temperature in degrees Celsius at
which the SCSI target device is capable of operating continuously without degrading the SCSI target device's
operation or reliability beyond manufacturer accepted limits. If the device server is unable to return a
reference temperature and the optional Reference Temperature log parameter is included in the Temperature
log page being returned, then REFERENCE TEMPERATURE field is set to FFh.
The reference temperature may change for vendor specific reasons.
Table 431 — Reference Temperature log parameter
Bit
Byte
(MSB)
PARAMETER CODE (0001h)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (02h)
Reserved
REFERENCE TEMPERATURE
