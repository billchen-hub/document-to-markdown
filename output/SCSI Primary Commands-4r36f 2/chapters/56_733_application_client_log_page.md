# 7.3.3 Application Client log page

7.3.2.2.2.6 Resetting and setting log parameters
In a LOG SELECT command, an application client may specify that:
a)
all the parameters in a log page or pages are to be reset (i.e., the PCR bit set to one); or
b)
individual parameters in log page are to be changed to specified new values (i.e., the PCR bit set to
zero and the PARAMETER LIST LENGTH field not set to zero).
The device server handling of these requests depends on the log parameter that is being reset or changed,
and is defined in the table that defines the log parameter using the keywords defined in table 357.
7.3.3 Application Client log page
7.3.3.1 Overview
Using the format shown in table 359, the Application Client log page (page code 0Fh) provides a place for
application clients to store information. The parameter codes for the Application Client log page are listed in
table 358.
Table 357 — Keywords for resetting or changing log parameters
Keyword
Device server handling when
PCR bit is set to one a
PCR bit is set to zero b
Always
Reset the log parameter
Change the log parameter
Reset Only
Reset the log parameter
If any changes are requested in the parameter value
field of the log parameter, then
a)
terminate the command with CHECK
CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER
LIST; and
b)
do not make any requested changes in any
field in any log parameter in any log page
Never
Do not reset the log parameter;
table 186 (see 6.7.1) describes
error conditions that may apply
a If the PCR bit is set to one and the PARAMETER LIST LENGTH field is not set to zero. then the LOG SELECT
command shall be terminated (see table 349 in 7.3.2.1).
b If the PCR bit is set to zero and the PARAMETER LIST LENGTH field is set to zero. then no log parameters are
changed (see 6.7.2).
Table 358 — Application Client log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0000h to 003Fh
General Usage Application Client
Always
7.3.3.2
Mandatory
0040h to 0FFFh
Optional
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.


The Application Client log page has the format shown in table 359.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, and SUBPAGE CODE field shall be set as shown in table 359 for the Application Client log
page.
Each application client log parameter contains the information described in 7.3.3.2.
7.3.3.2 General Usage Application Client log parameter
The General Usage Application Client log parameter has the format shown in table 360. This information may
be used to describe the system configuration and system problems, but the specific definition of the data is
application client specific.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 358 for the General
Usage Application Client log parameter.
Table 359 — Application Client log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (0Fh)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Application client log parameters
Application client log parameter (see 7.3.3.2)
[first]
•••
•••
Application client log parameter (see 7.3.3.2)
[last]
•••
n
Table 360 — General Usage Application Client log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 358)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (FCh)
GENERAL USAGE PARAMETER BYTES
•••
