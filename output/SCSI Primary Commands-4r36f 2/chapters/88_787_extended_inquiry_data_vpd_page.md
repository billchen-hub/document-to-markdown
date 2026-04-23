# 7.8.7 Extended INQUIRY Data VPD page

b)
the DESIGNATOR field has the format shown in table 617.
The ROUTING ID field contains a PCI Express routing ID (see SOP).
7.8.7 Extended INQUIRY Data VPD page
The Extended INQUIRY Data VPD page (see table 618) provides the application client with a means to obtain
information about the logical unit.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in 7.8.2.
Table 617 — PCI Express routing ID DESIGNATOR field format
Bit
Byte
ROUTING ID
Reserved

•••
Table 618 — Extended INQUIRY Data VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (86h)
(MSB)
PAGE LENGTH (003Ch)
(LSB)
ACTIVATE MICROCODE
SPT
GRD_CHK
APP_CHK
REF_CHK
Reserved
UASK_SUP
GROUP_SUP PRIOR_SUP
HEADSUP
ORDSUP
SIMPSUP
Reserved
WU_SUP
CRD_SUP
NV_SUP
V_SUP
Reserved
P_I_I_SUP
Reserved
LUICLR
Reserved
R_SUP
Reserved
CBCS
Reserved
MULTI I_T NEXUS MICROCODE DOWNLOAD
(MSB)
EXTENDED SELF-TEST COMPLETION MINUTES
(LSB)
POA_SUP
HRA_SUP
VSA_SUP
Reserved
MAXIMUM SUPPORTED SENSE DATA LENGTH

Reserved
•••


The PAGE CODE field and PAGE LENGTH field are defined in 7.8.2, and shall be set to the value shown in table
618 for the Extended INQUIRY Data VPD page.
The ACTIVATE MICROCODE field (see table 619) indicates how a device server activates microcode and estab-
lishes a unit attention condition when a WRITE BUFFER command (see 6.49) with the download microcode
mode set to 05h or 07h is processed (see 5.4).
A supported protection type (SPT) field indicates the type of protection the logical unit supports based on the
contents of the PERIPHERAL DEVICE TYPE field. If the PROTECT bit (see 6.6.2) is set to zero, the SPT field is
reserved.
If the PERIPHERAL DEVICE TYPE field is set to 00h (i.e., direct access block device) and the PROTECT bit is set to
one, then table 620 defines the contents of the SPT field.
Table 619 — ACTIVATE MICROCODE field
Value
Meaning
00b
The actions of the device server may or may not be as defined for values 01b or 10b.
01b
The device server:
1)
activates the microcode before completion of the final command in the WRITE BUFFER
sequence; and
2)
establishes a unit attention condition for the initiator port associated with every I_T nexus,
except the I_T nexus on which the WRITE BUFFER command was received, with the
additional sense code set to MICROCODE HAS BEEN CHANGED.
10b
The device server:
1)
activates the microcode after:
A)
a vendor specific event;
B)
a power on event; or
C) a hard reset event;
and
2)
establishes a unit attention condition for the initiator port associated with every I_T nexus
with the additional sense code set to MICROCODE HAS BEEN CHANGED.
11b
Reserved
Table 620 — SPT field for peripheral device type 00h
Code
Protection type supported
Type 1
Type 2
Type 3
000b
yes
no
no
001b
yes
yes
no
010b
no
yes
no
011b
yes
no
yes
100b
no
no
yes
101b
no
yes
yes
110b
Reserved
111b
yes
yes
yes


If the PERIPHERAL DEVICE TYPE field is set to 01h (i.e., sequential-access device) and the PROTECT bit is set to
one, then table 621 defines the contents of the SPT field.
If the PROTECT bit is set to one and the PERIPHERAL DEVICE TYPE field is set to a value other than 00h or 01h,
the SPT field is reserved.
A guard check (GRD_CHK) bit set to zero indicates that the device server does not check the LOGICAL BLOCK
GUARD field in the protection information (see SBC-2), if any. A GRD_CHK bit set to one indicates that the
device server checks the LOGICAL BLOCK GUARD field in the protection information, if any.
An application tag check (APP_CHK) bit set to zero indicates that the device server does not check the LOGICAL
BLOCK APPLICATION TAG field in the protection information (see SBC-2), if any. An APP_CHK bit set to one
indicates that the device server checks the LOGICAL BLOCK APPLICATION TAG field in the protection information,
if any.
A reference tag check (REF_CHK) bit set to zero indicates that the device server does not check the LOGICAL
BLOCK REFERENCE TAG field in the protection information (see SBC-2), if any. A REF_CHK bit set to one
indicates that the device server checks the LOGICAL BLOCK REFERENCE TAG field in the protection information, if
any.
A unit attention condition sense key specific data supported (UASK_SUP) bit set to one indicates that the device
server returns sense-key specific data for the UNIT ATTENTION sense key (see 4.5.2.4.6). A UASK_SUP bit
set to zero indicates that the device server does not return sense-key specific data for the UNIT ATTENTION
sense key.
A grouping function supported (GROUP_SUP) bit set to one indicates that the grouping function (see SBC-2) is
supported by the device server. A GROUP_SUP bit set to zero indicates that the grouping function is not
supported.
A priority supported (PRIOR_SUP) bit set to one indicates that command priority (see SAM-5) is supported by
the logical unit. A PRIOR_SUP bit set to zero indicates that command priority is not supported.
A head of queue supported (HEADSUP) bit set to one indicates that the HEAD OF QUEUE task attribute (see
SAM-5) is supported by the logical unit. A HEADSUP bit set to zero indicates that the HEAD OF QUEUE task
attribute is not supported. If the HEADSUP bit is set to zero, application clients should not specify the HEAD OF
QUEUE task attribute as an Execute Command (see SAM-5) procedure call argument.
An ordered supported (ORDSUP) bit set to one indicates that the ORDERED task attribute (see SAM-5) is
supported by the logical unit. An ORDSUP bit set to zero indicates that the ORDERED task attribute is not
supported. If the ORDSUP bit is set to zero, application clients should not specify the ORDERED task attribute as
an Execute Command procedure call argument.
The simple supported (SIMPSUP) bit shall be set to one indicating that the SIMPLE task attribute (see SAM-5) is
supported by the logical unit.
SAM-5 defines how unsupported task attributes are processed.
Table 621 — SPT field for peripheral device type 01h
Code
Protection type supported
001b
Logical block protection
all others
Reserved


A write uncorrectable supported (WU_SUP) bit set to zero indicates that the device server does not support
application clients setting the WR_UNCOR bit to one in the WRITE LONG command (see SBC-3). A WU_SUP bit
set to one indicates that the device server supports application clients setting the WR_UNCOR bit to one in the
WRITE LONG command.
A correction disable supported (CRD_SUP) bit set to zero indicates that the device server does not support
application clients setting the COR_DIS bit to one in the WRITE LONG command (see SBC-3). A CRD_SUP bit
set to one indicates that the device server supports application clients setting the COR_DIS bit to one in the
WRITE LONG command.
A non-volatile cache supported (NV_SUP) bit set to one indicates that the device server supports a non-volatile
cache and that the applicable command standard defines features using this cache (e.g., the FUA_NV bit in
SBC-2). An NV_SUP bit set to zero indicates that the device server may or may not support a non-volatile
cache.
A volatile cache supported (V_SUP) bit set to one indicates that the device server supports a volatile cache and
that the applicable command standard defines features using this cache (e.g., the FUA bit in SBC-2). An V_SUP
bit set to zero indicates that the device server may or may not support a volatile cache.
A protection information interval supported (P_I_I_SUP) bit set to one indicates that the logical unit supports
protection information intervals (see SBC-3). A P_I_I_SUP bit set to zero indicates that the logical unit does not
support protection information intervals.
A logical unit I_T nexus clear (LUICLR) bit set to one indicates the SCSI target device clears any unit attention
condition with an additional sense code of REPORTED LUNS DATA HAS CHANGED in each logical unit
accessible to an I_T nexus after reporting the unit attention condition for any logical unit over that I_T nexus
(see SAM-5). An LUICLR bit set to zero indicates the SCSI target device clears unit attention conditions
according to a previous version of this standard. The LUICLR bit shall be set to one.
A referrals supported (R_SUP) bit set to zero indicates that the device server does not support referrals (see
SBC-3). An R_SUP bit set to one indicates that the device server supports referrals.
A capability-based command security (CBCS) bit set to one indicates that the logical unit supports the
capability- based command security technique (see 5.14.6.8). A CBCS bit set to zero indicates that the logical
unit does not support the capability-based command security technique.
The MULTI I_T NEXUS MICROCODE DOWNLOAD field (see table 59 in 5.4) indicates how the device server handles
concurrent attempts to download microcode using the WRITE BUFFER command (see 5.4) from multiple I_T
nexuses.
The EXTENDED SELF-TEST COMPLETION MINUTES field contains advisory data that is the time in minutes that the
device server requires to complete an extended self-test provided the device server is not interrupted by
subsequent commands and no errors occur during processing of the self-test. The application client should
expect the self-test completion time to exceed the value in this field if other commands are sent to the logical
unit while a self-test is in progress or if errors occur during the processing of the self-test. If a device server
supports SELF-TEST CODE field values other than 000b for the SEND DIAGNOSTIC command (see 6.42) and
the self-test completion time is greater than 18 hours, then the device server shall support the EXTENDED
SELF-TEST COMPLETION MINUTES field. A value of 0000h indicates that the EXTENDED SELF-TEST COMPLETION
MINUTES field is not supported. A value of FFFFh indicates that the extended self-test takes 65 535 minutes or
longer.
A power on activation supported (POA_SUP) bit set to one indicates that the device server supports a WRITE
BUFFER command with the MODE field set to 0Dh (see 6.49.10) and the PO_ACT bit set to one. A POA_SUP bit
