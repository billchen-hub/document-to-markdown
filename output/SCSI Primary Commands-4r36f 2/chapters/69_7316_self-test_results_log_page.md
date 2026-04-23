# 7.3.16 Self-Test Results log page

The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a bounded data counter log parameter (see 7.3.2.2.2.2) for the Read Reverse
Error Counter log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1.
The READ REVERSE ERROR COUNTER field contains the value for the counter described by the contents of the
PARAMETER CODE field.
7.3.16 Self-Test Results log page
7.3.16.1 Overview
Using the format shown in table 410, the Self-Test Results log page (page code 10h) reports the results from
the 20 most recent self-tests (see 5.15). The parameter codes for the Self-Test Results log page are listed in
table 409.
The Self-Test Results log page has the format shown in table 410.
The DS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.3.2. The SPF
bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field shall be set as shown in table 410 for the
Self-Test Results log page.
Table 409 — Self-Test Results log page parameter codes
Parameter code
Description
Resettable or
Changeable a
Reference
Support
requirements
0001h to 0014h
Self-Test Results
Reset Only
7.3.16.2
Mandatory
all others
Reserved
a The keywords in this column – Always, Reset Only, and Never – are defined in 7.3.2.2.2.6.
Table 410 — Self-Test Results log page
Bit
Byte
DS
SPF (0b)
PAGE CODE (10h)
SUBPAGE CODE (00h)
(MSB)
PAGE LENGTH (0190h)
(LSB)
Self-test results log parameters
Self-test results log parameter [first]
•••
•••
Self-test results log parameter [twentieth]
•••


The results of the most recent self-test shall be contained in the log parameter with the PARAMETER CODE field
set to 0001h; the results for the second most recent self-test shall be contained in the log parameter with the
PARAMETER CODE field set to 0002h; etc. If fewer than 20 self-tests have been performed, then:
a)
unused self-test log parameters shall have parameter code values higher than those of any used
self-test log parameter; and
b)
each unused self-test log parameter entry shall have the format shown in table 411.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 409 for each Unused
Self-Test Results log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for each Unused Self-Test
Results log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 411 for each
Unused Self-Test Results log parameter.
The ZERO field is set to zero.
Table 411 — Unused Self-Test Results log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 409)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (10h)
ZERO
•••


7.3.16.2 Self-Test Results log parameters
Each Self-Test Results log parameter has the format shown in table 412.
The PARAMETER CODE field is described in 7.3.2.2.1, and shall be set as shown in table 409 for the Self-Test
Results log parameter.
The DU bit, TSD bit, ETC bit, TMC field, and FORMAT AND LINKING field are described in 7.3.2.2.2.1. These fields
shall be set as described for a binary format list log parameter (see 7.3.2.2.2.5) for the Unused Self-Test
Results log parameter.
The PARAMETER LENGTH field is described in 7.3.2.2.2.1, and shall be set as shown in table 412 for the
Self-Test Results log parameter.
The SELF-TEST CODE field indicates the value in the SELF-TEST CODE field of the SEND DIAGNOSTIC
command (see 6.42) that initiated this self-test.
Table 412 — Self-Test Results log parameter
Bit
Byte
(MSB)
PARAMETER CODE (see table 409)
(LSB)
Parameter control byte – binary format list log parameter (see 7.3.2.2.2.5)
DU
Obsolete
TSD
ETC
TMC
FORMAT AND LINKING
PARAMETER LENGTH (10h)
SELF-TEST CODE
Reserved
SELF-TEST RESULTS
SELF-TEST NUMBER
(MSB)
ACCUMULATED POWER ON HOURS
(LSB)
(MSB)
ADDRESS OF FIRST FAILURE
•••
(LSB)
Reserved
SENSE KEY
ADDITIONAL SENSE CODE
ADDITIONAL SENSE CODE QUALIFIER
Vendor specific


Table 413 defines the content of the SELF-TEST RESULTS field.
The SELF-TEST NUMBER field identifies the self-test that failed and consists of either:
a)
the number of the segment that failed during the self-test; or
b)
the number of the test that failed and the number of the segment in which the test was run, using a
vendor specific method for placing the two values in the one field.
If the segment in which the failure occurred is not able to be identified or need not be identified, the SELF-TEST
NUMBER field shall contain 00h.
The ACCUMULATED POWER ON HOURS field indicates the total hours the device server has been powered on
since manufacturing at the time the self-test is completed. If the self-test is still in progress, the ACCUMULATED
POWER ON HOURS field shall be set to zero. If the number of hours is greater than FFFFh, the ACCUMULATED
POWER ON HOURS field shall be set to FFFFh.
The ADDRESS OF FIRST FAILURE field indicates information that locates the failure on the media. If the logical
unit implements logical blocks, the content of the ADDRESS OF FIRST FAILURE field is the first logical block
address where a self-test error occurred. This implies nothing about the quality of any other logical block on
the logical unit, since the testing during which the error occurred may not have been performed in a sequential
manner. This value shall not change (e.g., as the result of block reassignment). The content of the ADDRESS
OF FIRST FAILURE field shall be FFFF FFFF FFFF FFFFh if no errors occurred during the self-test or if the error
that occurred is not related to an identifiable media address.
The SENSE KEY field, ADDITIONAL SENSE CODE field, and ADDITIONAL SENSE CODE QUALIFIER field may contain a
hierarchy of additional information relating to error or exception conditions that occurred during the self-test
represented in the same format used by the sense data (see 4.5).
Table 413 — SELF-TEST RESULTS field
Code
Description
0h
The self-test completed without error.
1h
The background self-test was aborted by the application client using a SEND DIAGNOSTIC
command (see 6.42) with the SELF-TEST CODE field set to 100b (i.e., abort background
self-test).
2h
The self-test routine was aborted by an application client using a method other than a SEND
DIAGNOSTIC command with the SELF-TEST CODE field set to 100b (e.g., by a task manage-
ment function, or by issuing an exception command as defined in 5.15.4).
3h
An unknown error occurred while the device server was processing the self-test and the device
server was unable to complete the self-test.
4h
The self-test completed with a failure in a test segment, and the test segment that failed is not
known.
5h
The first segment of the self-test failed.
6h
The second segment of the self-test failed.
7h
Another segment of the self-test failed and which test is indicated by the contents of the
SELF-TEST NUMBER field.
8h to Eh
Reserved
Fh
The self-test is in progress.
