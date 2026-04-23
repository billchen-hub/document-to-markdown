# 7.7.4 CbCS security protocol

7.7.4 CbCS security protocol
7.7.4.1 Overview
If the SECURITY PROTOCOL field in a SECURITY PROTOCOL IN command (see 6.40) is set to 07h, then the
command specifies one of the CbCS pages (see 7.7.4.2) to be returned by the device sever. The information
returned by a CbCS SECURITY PROTOCOL IN command indicates the CbCS operating parameters of:
a)
the logical unit to which the CbCS SECURITY PROTOCOL IN command is addressed; or
b)
the SCSI target device that contains the well-known logical unit to which the CbCS SECURITY
PROTOCOL IN command is addressed.
If the SECURITY PROTOCOL field in a SECURITY PROTOCOL OUT command (see 6.41) is set to 07h, then the
command specifies one of the CbCS pages (see 7.7.4.4) to be sent to the device sever. The instructions sent
in a CbCS SECURITY PROTOCOL OUT command specify the CbCS operating parameters of:
a)
the logical unit to which the CbCS SECURITY PROTOCOL OUT command is addressed; or
b)
the SCSI target device that contains the well-known logical unit to which the CbCS SECURITY
PROTOCOL OUT command is addressed.
7.7.4.2 CbCS SECURITY PROTOCOL IN CDB description
The CbCS SECURITY PROTOCOL IN CDB has the format defined in 6.40 with the additional requirements
described in this subclause.
If the SECURITY PROTOCOL field is set to CbCS (i.e., 07h) in a SECURITY PROTOCOL IN command, then the
SECURITY PROTOCOL SPECIFIC field (see table 559) specifies the CbCS page to be returned in the parameter
data (see 7.7.4.3). If the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see 7.8.7), the
CbCS SECURITY PROTOCOL IN command support requirements are shown in table 559.
Table 559 — SECURITY PROTOCOL SPECIFIC field for the CbCS SECURITY PROTOCOL IN command
Code a
CbCS page returned
Support
Reference
0000h
Supported CbCS SECURITY PROTOCOL IN Pages
Mandatory
7.7.4.3.1
0001h
Supported CbCS SECURITY PROTOCOL OUT Pages
Mandatory
7.7.4.3.2
0002h
Unchangeable CbCS Parameters
Mandatory
7.7.4.3.3
0003h to 003Eh
Reserved
003Fh
Security Token
Optional b
7.7.4.3.4
0040h
Current CbCS Parameters
Mandatory
7.7.4.3.5
0041h to D00Fh
Reserved
D010h
Set Master Key – Seed Exchange
Optional b
7.7.4.3.6
D011h to FFFFh
Reserved
a If the SECURITY PROTOCOL SPECIFIC field is set to a value that is less than D000h, then the working key
specified by the KEY VERSION field in the CbCS capability descriptor (see 6.27.2.3) shall be used to
compute the capability key (see 5.14.6.8.12). If the SECURITY PROTOCOL SPECIFIC field is set to a value
that is greater than or equal to D000h, then the authentication key component of the master key (see
5.14.6.8.11) shall be used to compute the capability key.
b Mandatory if the CAPKEY CbCS method (see 5.14.6.8.8.3) is supported.


If a CbCS SECURITY PROTOCOL IN command is received with the INC_512 bit set to one, the command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
7.7.4.3 CbCS SECURITY PROTOCOL IN parameter data
7.7.4.3.1 Supported CbCS SECURITY PROTOCOL IN Pages CbCS page
The Supported CbCS SECURITY PROTOCOL IN Pages CbCS page (see table 560) lists the CbCS pages
that are supported for the (i.e., the values that are allowed in the SECURITY PROTOCOL SPECIFIC field in a)
SECURITY PROTOCOL IN command (see 6.40).
The PAGE CODE field shall be set to 0000h to indicate that the Supported CbCS SECURITY PROTOCOL IN
Pages CbCS page is being returned.
The page length field indicates the number of bytes that follow in the Supported CbCS SECURITY
PROTOCOL IN Pages CbCS page.
Each SUPPORTED CBCS SECURITY PROTOCOL IN PAGE field indicates the page code (see table 559 in 7.7.4.2) of
one CbCS page that is supported by the SECURITY PROTOCOL IN command if the SECURITY PROTOCOL field
(see 6.40) is set to 07h (i.e., CbCS). The values in the SUPPORTED CBCS SECURITY PROTOCOL IN PAGE fields
shall be returned in ascending order beginning with 0000h (i.e., this CbCS page).
Table 560 — Supported CbCS SECURITY PROTOCOL IN Pages CbCS page format
Bit
Byte
(MSB)
PAGE CODE (0000h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported CbCS SECURITY PROTOCOL IN page list
(MSB)
SUPPORTED CBCS SECURITY PROTOCOL IN PAGE
[first]
(0000h)
(LSB)
•••
n-1
(MSB)
SUPPORTED CBCS SECURITY PROTOCOL IN PAGE
[last]
n
(LSB)


7.7.4.3.2 Supported CbCS SECURITY PROTOCOL OUT pages CbCS page
The Supported CbCS SECURITY PROTOCOL OUT Pages CbCS page (see table 561) lists the CbCS pages
that are supported for the (i.e., the values that are allowed in the SECURITY PROTOCOL SPECIFIC field in a)
SECURITY PROTOCOL OUT command (see 6.41).
The PAGE CODE field shall be set to 0001h to indicate that the Supported CbCS SECURITY PROTOCOL OUT
Pages CbCS page is being returned.
The page length field indicates the number of bytes that follow in the Supported CbCS SECURITY
PROTOCOL OUT Pages CbCS page.
Each SUPPORTED CBCS SECURITY PROTOCOL OUT PAGE field indicates the page code (see table 568 in 7.7.4.4)
of one CbCS page that is supported by the SECURITY PROTOCOL OUT command if the SECURITY PROTOCOL
field (see 6.41) is set to 07h (i.e., CbCS). The values in the SUPPORTED CBCS SECURITY PROTOCOL IN PAGE
fields shall be returned in ascending order.
Table 561 — Supported CbCS SECURITY PROTOCOL OUT Pages CbCS page format
Bit
Byte
(MSB)
PAGE CODE (0001h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Supported CbCS SECURITY PROTOCOL OUT page list
(MSB)
SUPPORTED CBCS SECURITY PROTOCOL OUT PAGE
[first]
(LSB)
•••
n-1
(MSB)
SUPPORTED CBCS SECURITY PROTOCOL OUT PAGE
[last]
n
(LSB)


7.7.4.3.3 Unchangeable CbCS Parameters CbCS page
The Unchangeable CbCS Parameters CbCS page (see table 562) indicates the supported CbCS features and
algorithms.
Table 562 — Unchangeable CbCS Parameters CbCS page format (part 1 of 2)
Bit
Byte
(MSB)
PAGE CODE (0002h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
KEYS SUPPORT
MIN CBCS METHOD SUP
Reserved
Reserved
(MSB)
SUPPORTED INTEGRITY CHECK VALUE ALGORITHM
LIST LENGTH (c-7)
(LSB)
Supported integrity check value algorithms list
(MSB)
SUPPORTED INTEGRITY CHECK VALUE ALGORITHM
[first]

•••
(LSB)
•••
c-3
(MSB)
SUPPORTED INTEGRITY CHECK VALUE ALGORITHM
[last]

•••
c
(LSB)
c+1
Reserved
c+2
c+3
(MSB)
SUPPORTED D-H ALGORITHM LIST LENGTH (d-c-4)
c+4
(LSB)
Supported Diffie-Hellman (D-H) algorithms list
c+5
(MSB)
SUPPORTED D-H ALGORITHM [first]

•••
c+8
(LSB)
•••
d-3
(MSB)
SUPPORTED D-H ALGORITHM [last]

•••
d
(LSB)


The PAGE CODE field shall be set to 0002h to indicate that the Unchangeable CbCS Parameters CbCS page is
being returned.
The page length field indicates the number of bytes that follow in the Unchangeable CbCS Parameters CbCS
page.
The KEYS SUPPORT field (see table 563) indicates the type of CbCS master keys and working keys supported.
The MIN CBCS METHOD SUP field (see table 564) indicates how the assignment of the minimum allowable CbCS
method is supported.
d+1
(MSB)
SUPPORTED CBCS METHODS LIST LENGTH (n-d-2)
d+2
(LSB)
Supported CbCS methods list
d+3
SUPPORTED CBCS METHOD [first]
•••
n
SUPPORTED CBCS METHOD [last]
Table 563 — KEYS SUPPORT field
Code
Description
00b
Reserved
01b
The SCSI target device supports single CbCS master key and a set of CbCS working
keys (see 5.14.6.8.11) for the SCSI target device, but the logical units in the SCSI target
device do not support CbCS master keys or working keys.
10b
The SCSI target device does not support CbCS master keys or working keys for the
SCSI target device, but each logical unit in the SCSI target device supports a single
CbCS master key and a set of CbCS working keys for that logical unit.
11b
The SCSI target device supports single CbCS master key and a set of CbCS working
keys for the SCSI target device, and each logical unit in the SCSI target device supports
a single CbCS master key and a set of CbCS working keys for that logical unit. Keys
stored in the logical unit take precedence over keys stored in the SCSI target device
(see 5.14.6.8.6).
Table 564 — MIN CBCS METHOD SUP field
Code
Description
00b
Reserved
01b
A single minimum allowed CbCS method (see 5.14.6.8.8) is assigned to all logical units in the
SCSI target device, and the SECURITY PROTOCOL well known logical unit is implemented to
control its value.
10b
Each logical unit in the SCSI target device is assigned its own minimum allowed CbCS method.
11b
Reserved
Table 562 — Unchangeable CbCS Parameters CbCS page format (part 2 of 2)
Bit
Byte


The SUPPORTED INTEGRITY CHECK VALUE ALGORITHM LIST LENGTH field indicates the number of bytes that follow
in the supported integrity check value algorithms list.
Each SUPPORTED INTEGRITY CHECK VALUE ALGORITHM field indicates one supported algorithm for computing
CbCS integrity check values. The values in the SUPPORTED INTEGRITY CHECK VALUE ALGORITHM fields are
selected from the codes that table 104 (see 5.14.8) lists as integrity checking (i.e., AUTH) algorithms, except
for AUTH_COMBINED.
The SUPPORTED D-H ALGORITHM LIST LENGTH field indicates the number of bytes that follow in the supported
Diffie-Hellman (D-H) algorithms list.
Each SUPPORTED D-H ALGORITHM field indicates one supported algorithm for constructing CbCS shared keys.
The values in the SUPPORTED D-H ALGORITHM fields are selected from the codes that table 104 (see 5.14.8)
lists as Diffie-Hellman algorithms with finite field D-H computations.
The SUPPORTED CBCS METHODS LIST LENGTH field indicates the number of bytes that follow in the supported
CbCS methods list.
Each SUPPORTED CBCS METHODS field indicates one supported CbCS method (see 6.27.2.3). The values in the
SUPPORTED CBCS METHODS fields are selected from the codes listed in table 267 (see 6.27.2.3).
7.7.4.3.4 Security Token CbCS page
The Security Token CbCS page (see table 565) indicates the value of the security token (see 5.14.6.8.10) for
the I_T nexus on which the SECURITY PROTOCOL IN command was received.
The PAGE CODE field shall be set to 003Fh to indicate that the Security Token CbCS page is being returned.
The page length field indicates the number of bytes that follow in the Security Token CbCS page.
The SECURITY TOKEN field shall contain the security token (see 5.14.6.8.10) for the I_T nexus on which the
command was received.
7.7.4.3.5 Current CbCS Parameters CbCS page
The Current CbCS Parameters CbCS page (see table 566) indicates the current values for the CbCS param-
eters (see 5.14.6.8.15) used by the SCSI target device or logical unit as follows:
Table 565 — Security Token CbCS page format
Bit
Byte
(MSB)
PAGE CODE (003Fh)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
(MSB)
SECURITY TOKEN
•••
n
(LSB)


a)
if the logical unit to which the SECURITY PROTOCOL IN command is addressed is the SECURITY
PROTOCOL well known logical unit (see 8.5), then the contents of the Current CbCS Parameters
CbCS page apply to the SCSI target device; or
b)
if the logical unit to which the SECURITY PROTOCOL IN command is addressed is not the
SECURITY PROTOCOL well known logical unit, then the contents of the Current CbCS Parameters
CbCS page apply to the addressed logical unit.
The PAGE CODE field shall be set to 0040h to indicate that the Current CbCS Parameters CbCS page is being
returned.
Table 566 — Current CbCS Parameters CbCS page format
Bit
Byte
(MSB)
PAGE CODE (0040h)
(LSB)
(MSB)
PAGE LENGTH (009Ah)
(LSB)

Reserved

MINIMUM ALLOWED CBCS METHOD
(MSB)
POLICY ACCESS TAG

•••
(LSB)

Reserved

•••

(MSB)
MASTER KEY IDENTIFIER

•••
(LSB)
(MSB)
WORKING KEY 0 IDENTIFIER

•••
(LSB)
(MSB)
WORKING KEY 1 IDENTIFIER

•••
(LSB)
•••
(MSB)
WORKING KEY 15 IDENTIFIER

•••
(LSB)
(MSB)
CLOCK

•••
(LSB)


The page length field indicates the number of bytes that follow in the Current CbCS Parameters CbCS page.
The contents of the MINIMUM ALLOWED CBCS METHOD field depend on the logical unit that returned the Current
CbCS Parameters CbCS page as follows:
a)
if the logical unit is not the SECURITY PROTOCOL well known logical unit, then the MINIMUM
ALLOWED CBCS METHOD field indicates the smallest value allowed in the CBCS METHOD field (see
6.27.2.3) of a capability descriptor processed by the enforcement manager (see 5.14.6.8.7) as
described in 5.14.6.8.13.2 (i.e., the value of the minimum CbCS method CbCS parameter for the
logical unit (see 5.14.6.8.15); or
b)
if the SECURITY PROTOCOL well known logical unit is returning the Current CbCS Parameters
CbCS page, then the MINIMUM ALLOWED CBCS METHOD field indicates the value that will be copied to
the minimum CbCS method CbCS parameter of any dynamically created logical units (i.e., the initial
minimum CbCS method CbCS parameter summarized in 5.14.6.8.15).
The value in the MINIMUM ALLOWED CBCS METHOD field is selected from those listed in table 267 (see 6.27.2.3).
The contents of the POLICY ACCESS TAG field depend on the logical unit that returned the Current CbCS Param-
eters CbCS page as follows:
a)
if the logical unit is not the SECURITY PROTOCOL well known logical unit, then the POLICY ACCESS
TAG field indicates the value required in the POLICY ACCESS TAG field (see 6.27.2.3) of a capability
descriptor processed by the enforcement manager (see 5.14.6.8.7) as described in 5.14.6.8.13.2 (i.e.,
the value of the policy access tag CbCS parameter for the logical unit (see 5.14.6.8.15); or
b)
if the SECURITY PROTOCOL well known logical unit is returning the Current CbCS Parameters
CbCS page, then the POLICY ACCESS TAG field indicates the value that will be copied to the policy
access tag CbCS parameter of any dynamically created logical units (i.e., the initial policy access tag
CbCS parameter summarized in 5.14.6.8.15).
The MASTER KEY IDENTIFIER field specifies the current CbCS shared key identifier (see 5.14.6.8.11.2) for the
master key (see 5.14.6.8.11).
The WORKING KEY 0 IDENTIFIER field, WORKING KEY 1 IDENTIFIER field, WORKING KEY 2 IDENTIFIER field, … and
WORKING KEY 15 IDENTIFIER field contain the current CbCS shared key identifier (see 5.14.6.8.11.2) for the
working keys (see 5.14.6.8.11).
The CLOCK field shall be set to the TIMESTAMP field format and value defined in 5.2.


7.7.4.3.6 Set Master Key – Seed Exchange CbCS page
The Set Master Key – Seed Exchange CbCS page (see table 567) in a SECURITY PROTOCOL IN command
continues a CbCS master key update CCS (see 5.14.6.8.11.4) that was initiated by processing of a Set
Master Key – Seed Exchange CbCS page in a SECURITY PROTOCOL OUT command (see 7.7.4.5.5), and
completes a Diffie-Hellman key exchange protocol as part of that CCS.
The Diffie-Hellman (D-H) algorithm being used in the CbCS master key update CCS is determined by the
contents of the D-H ALGORITHM field in the Set Master Key – Seed Exchange CbCS page in the SECURITY
PROTOCOL OUT command (see 7.7.4.5.5) that initiated the CCS. This Diffie-Hellman algorithm specifies the
DH_generator value and DH_prime value to be used in the computation of the D-H DATA field as described in
this subclause.
The PAGE CODE field set to D010h specifies that the Set Master Key – Seed Exchange CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Master Key – Seed Exchange
CbCS page. If the PAGE LENGTH field is set to a value that is inconsistent with the Diffie-Hellman algorithm
specified for the CbCS master key update CCS, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
The contents of the D-H DATA field are computed as follows:
1)
a random number, y, is generated having a value between 0 and DH_prime minus one observing the
requirements in RFC 4086; and
2)
the D-H DATA field is set to DH_generatory modulo DH_prime, where the DH_generator and DH_prime
values are identified by the value in the D-H ALGORITHM field.
As part of the successful completion of processing for the SECURITY PROTOCOL IN command transfer of
the Set Master Key – Seed Exchange CbCS page the device server and application client store as part of the
state maintained for CbCS master key update CCS (see 5.14.6.8.11.4):
a)
the authentication key component of the next master key; and
b)
the generation key component of the next master key.
Table 567 — Set Master Key – Seed Exchange CbCS page format
Bit
Byte
(MSB)
PAGE CODE (D010h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
(MSB)
D-H DATA
•••
n
(LSB)


The new master key is computed as follows:
1)
an initial_seed value that is the value DH_generatorxy modulo DH_prime is computed as follows:
A)
the device server computes (DH_generatorx modulo DH_prime)y, where DH_generatorx is the
contents of the D-H DATA field in the SECURITY PROTOCOL OUT command and y is the random
number generated by the device server; and
B)
the application client computes (DH_generatory modulo DH_prime)x, where DH_generatory is the
contents of the D-H DATA field in the SECURITY PROTOCOL IN command and x is the random
number generated by the application client (see 7.7.4.5.5);
2)
the generation key component of the new master key is computed using the integrity check value
algorithm specified by the integrity check value algorithm field in the capability (see 6.27.2.3) in the
CbCS extension descriptor (see 5.14.6.8.16) associated with the SECURITY PROTOCOL IN
command that transferred the Set Master Key – Seed Exchange CbCS page. The following inputs are
used with the specified integrity check value algorithm:
A)
the concatenation of the initial_seed value computed in step 1) and all of the bytes in the Device
Identification VPD page (see 7.8.6) for the logical unit that is processing the CbCS master key
update CCS (see 5.14.6.8.11.4) as the string for which the integrity check value is to be
computed; and
B)
the generation key component of the current master key (see 5.14.6.8.11) for the logical unit that
is processing the CbCS master key update CCS as the cryptographic key;
3)
a modified_seed value is computed as follows:
A)
if the least significant bit of the initial_seed value is zero, then the modified_seed value is equal to
the initial_seed value with the least significant bit set to one; and
B)
if the least significant bit of the initial_seed value is one, then the modified_seed value is equal to
the initial_seed value with the least significant bit set to zero;
and
4)
the authentication key component of the new master key is computed using the integrity check value
algorithm specified by the integrity check value algorithm field in the capability (see 6.27.2.3) in the
CbCS extension descriptor (see 5.14.6.8.16) associated with the SECURITY PROTOCOL IN
command that transferred the Set Master Key – Seed Exchange CbCS page. The following inputs are
used with the specified integrity check value algorithm:
A)
the concatenation of the modified_seed value computed in step 3) and all of the bytes in the
Device Identification VPD page for the logical unit that is processing the CbCS master key update
CCS as the string for which the integrity check value is to be computed; and
B)
the generation key component of the current master key for the logical unit that is processing the
CbCS master key update CCS as the cryptographic key.


7.7.4.4 CbCS SECURITY PROTOCOL OUT CDB description
The CbCS SECURITY PROTOCOL OUT CDB has the format defined in 6.41 with the additional requirements
described in this subclause.
If the SECURITY PROTOCOL field is set to CbCS (i.e., 07h) in a SECURITY PROTOCOL OUT command, then
the SECURITY PROTOCOL SPECIFIC field (see table 568) specifies the CbCS page to be returned in the
parameter data (see 7.7.4.5). If the CBCS bit is set to one in the Extended INQUIRY Data VPD page (see
7.8.7), the CbCS SECURITY PROTOCOL IN command support requirements are shown in table 568.
If a CbCS SECURITY PROTOCOL OUT command is received with the INC_512 bit set to one, the command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
Table 568 — SECURITY PROTOCOL SPECIFIC field for the CbCS SECURITY PROTOCOL OUT command
Code a
CbCS page sent
Support
Reference
0000h to 0040h
Reserved
0041h
Set Policy Access Tag
Optional
7.7.4.5.1
0042h
Set Minimum CbCS Method
Optional
7.7.4.5.2
0043h to CFFFh
Reserved
D000h
Invalidate Key
Optional b
7.7.4.5.3
D001h
Set Key
Optional b
7.7.4.5.4
D003h to D00Fh
Reserved
D010h
Set Master Key – Seed Exchange
Optional b
7.7.4.5.5
D011h
Set Master Key – Change Master Key
Optional b
7.7.4.5.6
D012h to FFFFh
Reserved
a If the SECURITY PROTOCOL SPECIFIC field is set to a value that is less than D000h, then
the working key specified by the KEY VERSION field in the CbCS capability descriptor
(see 6.27.2.3) shall be used to compute the capability key (see 5.14.6.8.12). If the
SECURITY PROTOCOL SPECIFIC field is set to a value that is greater than or equal to
D000h, then the authentication key component of the master key (see 5.14.6.8.11)
shall be used to compute the capability key.
b Mandatory if the CAPKEY CbCS method (see 5.14.6.8.8.3) is supported.


7.7.4.5 CbCS SECURITY PROTOCOL OUT parameter data
7.7.4.5.1 Set Policy Access Tag CbCS page
The Set Policy Access Tag CbCS page (see table 569) specifies a new policy access tag CbCS parameter
value or a new initial policy access tag CbCS parameter value.
The PAGE CODE field set to 0041h specifies that the Set Policy Access Tag CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Policy Access Tag CbCS page. If
the PAGE LENGTH field is set to a value that is smaller than four, then the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
The CbCS parameter (see 5.14.6.8.15) that is set to the contents of the POLICY ACCESS TAG field depends on
the logical unit that is processing the Set Policy Access Tag CbCS page as follows:
a)
if the logical unit is not the SECURITY PROTOCOL well known logical unit, then the contents of the
POLICY ACCESS TAG field shall be placed in the policy access tag CbCS parameter for the logical unit;
or
b)
if the SECURITY PROTOCOL well known logical unit is processing the Set Policy Access Tag CbCS
page, then the contents of the POLICY ACCESS TAG field shall be placed in the initial policy access tag
CbCS parameter.
Table 569 — Set Policy Access Tag CbCS page format
Bit
Byte
(MSB)
PAGE CODE (0041h)
(LSB)
(MSB)
PAGE LENGTH (0004h)
(LSB)
(MSB)
POLICY ACCESS TAG

•••
(LSB)


7.7.4.5.2 Set Minimum CbCS Method CbCS page
The Set Minimum CbCS Method CbCS page (see table 570) specifies a new minimum CbCS method CbCS
parameter value or a new initial minimum CbCS method CbCS parameter value.
The PAGE CODE field set to 0042h specifies that the Set Minimum CbCS Method CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Minimum CbCS Method CbCS
page. If the PAGE LENGTH field is set to a value that is smaller than two, then the command shall be terminated
with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense
code set to INVALID FIELD IN PARAMETER LIST.
The CbCS parameter or CbCS parameters (see 5.14.6.8.15) that are set to the contents of the MINIMUM
ALLOWED CBCS METHOD field depends on the logical unit that is processing the Set Minimum CbCS Method
CbCS page and the contents of the MIN CBCS METHOD SUP field in the Unchangeable CbCS Parameters CbCS
page (see 7.7.4.3.3) as shown in table 571.
If the MINIMUM ALLOWED CBCS METHOD field specifies a value that does not appear in the supported CbCS
methods list in the Unchangeable CbCS Parameters CbCS page (see 7.7.4.3.3), then the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
Table 570 — Set Minimum CbCS Method CbCS page format
Bit
Byte
(MSB)
PAGE CODE (0042h)
(LSB)
(MSB)
PAGE LENGTH (0002h)
(LSB)
Reserved
MINIMUM ALLOWED CBCS METHOD
Table 571 — Minimum CbCS Method CbCS Parameter set
MIN CBCS
METHOD
SUP field
CbCS Parameter set based on the logical unit that processes the Set Minimum CbCS
Method CbCS page
Not the SECURITY PROTOCOL
well known logical unit
SECURITY PROTOCOL
well known logical unit
00b
Reserved (see table 564)
01b
The command is terminated with CHECK
CONDITION status with the sense key set to
ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN
PARAMETER LIST
All minimum CbCS method CbCS parame-
ters for all logical units in the SCSI target
device, and the initial minimum CbCS
method, if any
10b
The minimum CbCS method CbCS parame-
ter for the logical unit that processes the Set
Minimum CbCS Method CbCS page
The initial minimum CbCS method CbCS
parameter
11b
Reserved (see table 564)


7.7.4.5.3 Invalidate Key CbCS page
The Invalidate Key CbCS page (see table 572) causes a working key (see 5.14.6.8.11) to be invalidated. After
the successful processing of an Invalidate Key CbCS page, the working key with the specified key version
shall not be valid for the purposes of enforcement manager (see 5.14.6.8.7) CbCS extension descriptor
validation (see 5.14.6.8.13.2).
The PAGE CODE field set to D000h specifies that the Invalidate Key CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Invalidate Key CbCS page. If the PAGE
LENGTH field is set to a value that is smaller than four, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
The KEY VERSION field specifies which working key (e.g., a KEY VERSION field set to four specifies that the
working key whose Current CbCS Parameters CbCS page (see 7.7.4.3.5) key identifier is returned in the
WORKING KEY 4 IDENTIFIER field) is to be invalidated as follows:
a)
if the Invalidate Key CbCS page is processed by a logical unit that is not the SECURITY PROTOCOL
well known logical unit, then the specified working key for that logical unit shall be invalidated; or
b)
if the Invalidate Key CbCS page is processed by the SECURITY PROTOCOL well known logical unit,
then the specified target-wide working key (see 5.14.6.8.11) shall be invalidated.
The CbCS shared key identifier (see 5.14.6.8.11.2) for the invalidated working key shall be set to
FFFF FFFF FFFF FFFEh.
It shall not be an error to invalidate a working key that is already invalid.
Table 572 — Invalidate Key CbCS page format
Bit
Byte
(MSB)
PAGE CODE (D000h)
(LSB)
(MSB)
PAGE LENGTH (0004h)
(LSB)

Reserved

Reserved
KEY VERSION


7.7.4.5.4 Set Key CbCS page
The Set Key CbCS page (see table 573) causes a working key (see 5.14.6.8.11) to be set to a new value.
After the successful processing of a Set Key CbCS page, the working key with the specified key version shall
be valid for the purposes of enforcement manager (see 5.14.6.8.7) CbCS extension descriptor validation (see
5.14.6.8.13.2).
The PAGE CODE field set to D001h specifies that the Set Key CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Key CbCS page. If the PAGE LENGTH
field is set to a value that is other than 32, then the command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
The KEY VERSION field specifies which working key (e.g., a KEY VERSION field set to six specifies that the
working key whose Current CbCS Parameters CbCS page (see 7.7.4.3.5) key identifier is returned in the
WORKING KEY 6 IDENTIFIER field) is to be set as follows:
a)
if the Set Key CbCS page is processed by a logical unit that is not the SECURITY PROTOCOL well
known logical unit, then the specified working key for that logical unit shall be set; or
b)
if the Set Key CbCS page is processed by the SECURITY PROTOCOL well known logical unit, then
the specified target-wide working key (see 5.14.6.8.11) shall be set.
The KEY IDENTIFIER field specifies the value to which the CbCS shared key identifier (see 5.14.6.8.11.2) shall
be set for the working key affected by the Set Key CbCS page. If the KEY IDENTIFIER field is set to a value that
table 88 (see 5.14.6.8.11.2) describes as reserved in the CbCS pages that change CbCS shared key values,
then the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The SEED field specifies a random number that is an input to the computation of the new working key value.
Table 573 — Set Key CbCS page format
Bit
Byte
(MSB)
PAGE CODE (D001h)
(LSB)
(MSB)
PAGE LENGTH (0020h)
(LSB)

Reserved

Reserved
KEY VERSION
(MSB)
KEY IDENTIFIER

•••
(LSB)
(MSB)
SEED

•••
(LSB)


The value to which the specified working key is set shall be computed using the integrity check value
algorithm specified by the INTEGRITY CHECK VALUE ALGORITHM field in the capability (see 6.27.2.3) in the CbCS
extension descriptor (see 5.14.6.8.16) associated with the SECURITY PROTOCOL OUT command that sent
the Set Key CbCS page. The following inputs shall be used with the specified integrity check value algorithm:
a)
the contents of the SEED field in the Set Key CbCS page as the string for which the integrity check
value is to be computed; and
b)
the generation key component of the master key (see 5.14.6.8.11) for the logical unit that is
processing the Set Key CbCS page as the cryptographic key.
7.7.4.5.5 Set Master Key – Seed Exchange CbCS page
The Set Master Key – Seed Exchange CbCS page (see table 574) in a SECURITY PROTOCOL OUT
command initiates a CbCS master key update CCS (see 5.14.6.8.11.4) and begins a Diffie-Hellman key
exchange protocol as part of that CCS.
The PAGE CODE field set to D010h specifies that the Set Master Key – Seed Exchange CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Master Key – Seed Exchange
CbCS page. If the PAGE LENGTH field is set to a value that is smaller than ten, then the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
The D-H ALGORITHM field specifies the Diffie-Hellman (D-H) algorithm to be used in the seed exchange
protocol. The value in the D-H ALGORITHM field is selected from the codes that table 104 (see 5.14.8) lists as
Diffie-Hellman algorithms with finite field D-H computations. The Diffie-Hellman algorithm selected specifies
the DH_generator value and DH_prime value to be used in the computation of the D-H DATA field as described
in this subclause.
If the value in the D-H ALGORITHM field does not appear in the Supported Diffie-Hellman algorithms list in the
Unchangeable CbCS Parameters CbCS page (see 7.7.4.3.3), then the command shall be terminated with
Table 574 — Set Master Key – Seed Exchange CbCS page format
Bit
Byte
(MSB)
PAGE CODE (D010h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)
(MSB)
D-H ALGORITHM

•••
(LSB)
(MSB)
D-H DATA LENGTH (n-11)

•••
(LSB)
(MSB)
D-H DATA
•••
n
(LSB)


CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
The D-H DATA LENGTH field specifies the number of bytes that follow in D-H DATA field. If the D-H DATA LENGTH
field is set to a value that is inconsistent with the Diffie-Hellman algorithm specified by the D-H ALGORITHM field,
then the command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The contents of the D-H DATA field are computed as follows:
1)
a random number, x, is generated having a value between 0 and DH_prime minus one observing the
requirements in RFC 4086; and
2)
the D-H DATA field is set to DH_generatorx modulo DH_prime, where the DH_generator and DH_prime
values are identified by the value in the D-H ALGORITHM field.
7.7.4.5.6 Set Master Key – Change Master Key CbCS page
The Set Master Key – Change Master Key CbCS page (see table 575) concludes a CbCS master key update
CCS (see 5.14.6.8.11.4) and changes the master key components to the values computed as part of
processing completion (see 7.7.4.3.6) for the SECURITY PROTOCOL IN command that transferred the Set
Master Key – Seed Exchange CbCS page.
Table 575 — Set Master Key – Change Master Key CbCS page format
Bit
Byte
(MSB)
PAGE CODE (D011h)
(LSB)
(MSB)
PAGE LENGTH (n-3)
(LSB)

Reserved

•••

(MSB)
KEY IDENTIFIER

•••
(LSB)
(MSB)
APPLICATION CLIENT D-H DATA LENGTH (k-19)

•••
(LSB)
(MSB)
APPLICATION CLIENT D-H DATA
•••
k
(LSB)
k+1
(MSB)
DEVICE SERVER D-H DATA LENGTH (n-(k-4))

•••
k+4
(LSB)
k+5
(MSB)
DEVICE SERVER D-H DATA
•••
n
(LSB)


The PAGE CODE field set to D011h specifies that the Set Master Key – Change Master Key CbCS page follows.
The PAGE LENGTH field specifies the number of bytes that follow in the Set Master Key – Change Master Key
CbCS page. If the PAGE LENGTH field is set to a value that is smaller than 24, then the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
The KEY IDENTIFIER field specifies the value to which the master key CbCS shared key identifier (see
5.14.6.8.11.2) shall be set. If the KEY IDENTIFIER field is set to a value that table 88 (see 5.14.6.8.11.2)
describes as reserved in the CbCS pages that change CbCS shared key values, then the command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN PARAMETER LIST.
The APPLICATION CLIENT D-H DATA LENGTH field specifies the number of bytes that follow in the APPLICATION
CLIENT D-H DATA field. If the contents of the APPLICATION CLIENT D-H DATA LENGTH field do not match the number
of Diffie-Hellman (D-H) data bytes that the device server received in the SECURITY PROTOCOL OUT
command that sent the Set Master Key – Seed Exchange CbCS page (see 7.7.4.5.5) and initiated the current
CbCS master key update CCS (see 5.14.6.8.11.4), then the master key shall not be modified and the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The APPLICATION CLIENT D-H DATA field contains Diffie-Hellman data field that was sent in the Set Master Key –
Seed Exchange CbCS page that initiated the current CbCS master key update CCS. If the contents of the
APPLICATION CLIENT D-H DATA field do not match Diffie-Hellman data that the device server received in the
SECURITY PROTOCOL OUT command that sent the Set Master Key – Seed Exchange CbCS page that
initiated the current CbCS master key update CCS (see 5.14.6.8.11.4), then the master key shall not be
modified and the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
The DEVICE SERVER D-H DATA LENGTH field specifies the number of bytes that follow in the DEVICE SERVER D-H
DATA field. If the contents of the DEVICE SERVER D-H DATA LENGTH field do not match the number of
Diffie-Hellman data bytes that the device server returned in the SECURITY PROTOCOL IN command that
returned the Set Master Key – Seed Exchange CbCS page (see 7.7.4.3.6) in the current CbCS master key
update CCS, then the master key shall not be modified and the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
The DEVICE SERVER D-H DATA field contains Diffie-Hellman data field that was returned in the Set Master Key –
Seed Exchange CbCS page that the device server returned in response to a SECURITY PROTOCOL IN
COMMAND as part of the current CbCS master key update CCS. If the contents of the DEVICE SERVER D-H
DATA field do not match Diffie-Hellman data that the device server sent in the SECURITY PROTOCOL IN
command that send the Set Master Key – Seed Exchange CbCS page, then the master key shall not be
modified and the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.


7.8 Vital product data parameters
7.8.1 Vital product data parameters overview and page codes
This subclause describes the vital product data (VPD) page structure and the VPD pages (see table 576) that
are applicable to all SCSI devices. These VPD pages are returned by an INQUIRY command with the EVPD bit
set to one (see 6.6) and contain vendor specific product information about a logical unit and SCSI target
device. The vital product data may include vendor identification, product identification, unit serial numbers,
device operating definitions, manufacturing data, field replaceable unit information, and other vendor specific
information. This standard defines the structure of the vital product data, but not the contents.
Table 576 — Vital product data page codes
VPD Page Name
Page code
Reference
Support
requirements
ASCII Information
01h to 7Fh
7.8.3
Optional
ATA Information
89h
SAT-3
See SAT-3
CFA Profile Information
8Ch
7.8.4
Optional
Device Constituents
8Bh
7.8.5
Optional
Device Identification
83h
7.8.6
Mandatory
Extended INQUIRY Data
86h
7.8.7
Optional
Management Network Addresses
85h
7.8.8
Optional
Mode Page Policy
87h
7.8.9
Optional
Power Condition
8Ah
7.8.10
Optional
Power Consumption
8Dh
7.8.11
Optional
Protocol Specific Logical Unit Information
90h
7.8.12
Protocol specific a
Protocol Specific Port Information
91h
7.8.13
Protocol specific a
SCSI Ports
88h
7.8.14
Optional
Software Interface Identification
84h
7.8.15
Optional
Supported VPD Pages
00h
7.8.16
Mandatory
Third-party Copy
8Fh
7.8.17
Optional
Unit Serial Number
80h
7.8.18
Optional
Restricted (see applicable command standard)
B0h to BFh
Obsolete b
Vendor specific c
Reserved
All other codes
A numeric ordered listing of VPD page codes is provided in E.7.
a See applicable SCSI transport protocol standard for support requirements.
b The following page codes are obsolete: 81h and 82h.
c The following page codes are vendor specific: C0h to FFh.


This standard does not define the location or method of storing the vital product data. The retrieval of the vital
product data may require completion of initialization operations within the device, that may result in delays
before the vital product data is available to the application client. Time-critical requirements are an implemen-
tation consideration and are not defined in this standard.
7.8.2 VPD page format and page codes for all device types
This subclause describes the VPD page structure and the VPD pages that are applicable to all SCSI devices.
VPD pages specific to each device type are described in the command standard that applies to that device
type.
An INQUIRY command with the EVPD bit set to one (see 6.6) specifies that the device server return a VPD
page using the format defined in table 577.
The PERIPHERAL QUALIFIER field and the PERIPHERAL DEVICE TYPE field are the same as defined for standard
INQUIRY data (see 6.6.2).
The PAGE CODE field (see 7.8.1) identifies the VPD page and contains the same value as in the PAGE CODE
field in the INQUIRY CDB (see 6.6).
The PAGE LENGTH field indicates the length in bytes of the VPD parameters that follow this field. The contents
of the PAGE LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The VPD parameters are defined for each VPD page code.
Table 577 — VPD page format
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
VPD parameters
•••
n


7.8.3 ASCII Information VPD page
The ASCII Information VPD page (see table 578) contains information for the field replaceable unit code
returned in the sense data (see 4.5).
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, PAGE CODE field, and PAGE LENGTH field are
defined in 7.8.2.
The value in the PAGE CODE field is associated with the FIELD REPLACEABLE UNIT CODE field returned in the
sense data.
NOTE 67 - The FIELD REPLACEABLE UNIT CODE field in the sense data provides for 255 possible codes, while
the PAGE CODE field provides for only 127 possible codes. For that reason it is not possible to return ASCII
Information VPD pages for the upper code values.
The PAGE LENGTH field is defined in 7.8.2.
The ASCII LENGTH field indicates the length in bytes of the ASCII INFORMATION field that follows. A value of zero
in this field indicates that no ASCII information is available for the indicated page code. The contents of the
ASCII LENGTH field are not altered based on the allocation length (see 4.2.5.6).
The ASCII INFORMATION field contains ASCII information concerning the field replaceable unit identified by the
page code. The data in this field shall be formatted in one or more character string lines. Each line shall
contain only ASCII printable characters (i.e., code values 20h through 7Eh) and shall be terminated with a
NULL (00h) character.
The contents of the vendor specific information field is not defined in this standard.
Table 578 — ASCII Information VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (01h to 7Fh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
ASCII LENGTH (m-4)
(MSB)
ASCII INFORMATION
•••
m
(LSB)
m+1
Vendor specific information
•••
n


7.8.4 CFA Profile Information VPD page
The CFA Profile Information VPD page (see table 579) provides information on the CFA profiles, if any, that
are supported by the device server.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 579 for the CFA Profile Information
VPD page.
Each CFA profile descriptor (see table 580) contains identifying information for one CFA profile supported by
the device server described in the standard INQUIRY data (see 6.6.2).
The CFA PROFILE SUPPORTED field indicates a CFA profile number (see VPG1) that the device server supports.
The SEQUENTIAL WRITE DATA SIZE field indicates the preferred number of logical blocks in a stream field write
operation (see VPG1) for the CFA profile indicated by the CFA PROFILE SUPPORTED field. If the SEQUENTIAL
WRITE DATA SIZE field is set to zero, then no preferred number of logical blocks is indicated for stream field
write operations by this CFA profile descriptor.
Table 579 — CFA Profile Information VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (8Ch)
(MSB)
PAGE LENGTH (n-3)
(LSB)
CFA profile descriptor list
CFA profile descriptor (see table 580) [first]

•••
•••
n-3
CFA profile descriptor (see table 580) [last]
•••
n
Table 580 — CFA profile descriptor
Bit
Byte
CFA PROFILE SUPPORTED
Reserved
(MSB)
SEQUENTIAL WRITE DATA SIZE
(LSB)
