# 7.8.9 Mode Page Policy VPD page

7.8.9 Mode Page Policy VPD page
The Mode Page Policy VPD page (see table 625) indicates which mode page policy (see 7.5.2) is in effect for
each mode page supported by the logical unit.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 625 for the Mode Page Policy VPD
page.
Each mode page policy descriptor (see table 626) contains information describing the mode page policy for
one or more mode pages or subpages (see 7.5.7). The information in the mode page policy descriptors in this
VPD page shall describe the mode page policy for every mode page and subpage supported by the logical
unit.
The POLICY PAGE CODE field and POLICY SUBPAGE CODE field indicate the mode page and subpage to which the
descriptor applies. The POLICY PAGE CODE field contains the value that is used in a MODE SENSE command
(see table 198 in 6.13.1) to retrieve the mode page being described.
If the first mode page policy descriptor in the list contains a POLICY PAGE CODE field set to 3Fh and a POLICY
SUBPAGE CODE field set to FFh, then the descriptor applies to all mode pages and subpages not described by
Table 625 — Mode Page Policy VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (87h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Mode page policy descriptor list
Mode page policy descriptor [first]
•••
•••
n-3
Mode page policy descriptor [last]
•••
n
Table 626 — Mode page policy descriptor
Bit
Byte
Reserved
POLICY PAGE CODE
POLICY SUBPAGE CODE
MLUS
Reserved
MODE PAGE POLICY
Reserved


other mode page policy descriptors. The POLICY PAGE CODE field shall be set to 3Fh and the POLICY SUBPAGE
CODE field shall be set to FFh only in the first mode page policy descriptor in the list.
If the POLICY PAGE CODE field is set to a value other than 3Fh and a POLICY SUBPAGE CODE field is set to a value
other than FFh, then the POLICY PAGE CODE field and the POLICY SUBPAGE CODE field indicate a single mode
page and subpage to which the descriptor applies.
If the POLICY PAGE CODE field is set to a value other than 3Fh, then POLICY SUBPAGE CODE field shall contain a
value other than FFh. If the POLICY SUBPAGE CODE field is set to a value other than FFh, then POLICY PAGE
CODE field shall contain a value other than 3Fh.
If the SCSI target device has more than one logical unit, a multiple logical units share (MLUS) bit set to one
indicates the mode page and subpage identified by the POLICY PAGE CODE field and POLICY SUBPAGE CODE field
is shared by more than one logical unit. A MLUS bit set to zero indicates the logical unit maintains its own copy
of the mode page and subpage identified by the POLICY PAGE CODE field and POLICY SUBPAGE CODE field.
The MLUS bit is set to one in the mode page policy descriptors or descriptor that indicates the mode page
policy for the:
a)
Disconnect-Reconnect mode page (see 7.5.10); and
b)
Protocol Specific Port mode page (see 7.5.16).
The MODE PAGE POLICY field (see table 627) indicates the mode page policy for the mode page and subpage
identified by the POLICY PAGE CODE field and POLICY SUBPAGE CODE field. The mode page policies are
described in table 450 (see 7.5.2).
Table 627 — MODE PAGE POLICY field
Code
Description
00b
Shared
01b
Per target port
10b
Obsolete
11b
Per I_T nexus
