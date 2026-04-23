# 6.6.2 Standard INQUIRY data

INQUIRY data (i.e., standard INQUIRY data (see 6.6.2) and all VPD pages (see 7.8)) should be returned even
though the device server is not ready for other commands. Standard INQUIRY data, the Extended INQUIRY
Data VPD page (see 7.8.7), and the Device Identification VPD page (see 7.8.6) should be available without
incurring any media access delays. If the device server does store some of the standard INQUIRY data or
VPD data on the media, it may return ASCII spaces (20h) in ASCII fields and zeros in other fields until the data
is available from the media.
INQUIRY data may change as the SCSI target device and its logical units perform their initialization sequence.
(E.g., logical units may provide a minimum command set from nonvolatile memory until they load the final
firmware from the media. After the firmware has been loaded, more options may be supported and therefore
different INQUIRY data may be returned.)
If INQUIRY data changes for any reason, the device server shall establish a unit attention condition for the
initiator port associated with every I_T nexus (see SAM-5), with the additional sense code set to INQUIRY
DATA HAS CHANGED.
NOTE 29 - The INQUIRY command may be used by an application client after a hard reset or power on
condition to determine the device types for system configuration.
6.6.2 Standard INQUIRY data
The standard INQUIRY data (see table 174) shall contain at least 36 bytes.
Table 174 — Standard INQUIRY data format (part 1 of 2)
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
RMB
Reserved
VERSION
Reserved
Reserved
NORMACA
HISUP
RESPONSE DATA FORMAT (2h)
ADDITIONAL LENGTH (n-4)
SCCS
ACC
TPGS
3PC
Reserved
PROTECT
Obsolete
ENCSERV
VS
MULTIP
Obsolete
Reserved
Reserved
ADDR16 a
Obsolete
Reserved
WBUS16 a
SYNC a
Obsolete
Reserved
CMDQUE
VS
(MSB)
T10 VENDOR IDENTIFICATION
•••
(LSB)
(MSB)
PRODUCT IDENTIFICATION
•••
(LSB)
(MSB)
PRODUCT REVISION LEVEL
•••
(LSB)
Vendor specific
•••


The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field identify the peripheral device connected to
the logical unit. If the SCSI target device is not capable of supporting a peripheral device connected to this
logical unit, the device server shall set these fields to 7Fh (i.e., PERIPHERAL QUALIFIER field set to 011b and
PERIPHERAL DEVICE TYPE field set to 1Fh).
The PERIPHERAL QUALIFIER field is defined in table 175.
Reserved
CLOCKING a
QAS a
IUS a
Reserved
(MSB)
VERSION DESCRIPTOR 1
(LSB)
•••
(MSB)
VERSION DESCRIPTOR 8
(LSB)
Reserved
•••
Vendor specific parameters
Vendor specific
•••
n
a The meanings of these fields are specific to SPI-5 (see 6.6.3). For SCSI transport protocols other than
the SCSI Parallel Interface, these fields are reserved.
Table 175 — PERIPHERAL QUALIFIER field
Qualifier
Description
000b
A peripheral device having the specified peripheral device type is connected to this
logical unit. If the device server is unable to determine whether or not a peripheral
device is connected, it also shall use this peripheral qualifier. This peripheral qualifier
does not mean that the peripheral device connected to the logical unit is ready for
access.
001b
A peripheral device having the specified peripheral device type is not connected to this
logical unit. However, the device server is capable of supporting the specified periph-
eral device type on this logical unit.
010b
Reserved
011b
The device server is not capable of supporting a peripheral device on this logical unit.
For this peripheral qualifier the peripheral device type shall be set to 1Fh. All other
peripheral device type values are reserved for this peripheral qualifier.
100b to 111b
Vendor specific
Table 174 — Standard INQUIRY data format (part 2 of 2)
Bit
Byte


The peripheral device type is defined in table 176.
A removable medium (RMB) bit set to zero indicates that the medium is not removable. A RMB bit set to one
indicates that the medium is removable.
Table 176 — Peripheral device type
Code
Reference a
Description
00h
SBC-3
Direct access block device (e.g., magnetic disk)
01h
SSC-3
Sequential-access device (e.g., magnetic tape)
02h
SSC
Printer device
03h
SPC-2
Processor device
04h
SBC
Write-once device (e.g., some optical disks)
05h
MMC-6
CD/DVD device
06h
Scanner device (obsolete)
07h
SBC
Optical memory device (e.g., some optical disks)
08h
SMC-3
Media changer device (e.g., jukeboxes)
09h
Communications device (obsolete)
0Ah to 0Bh
Obsolete
0Ch
SCC-2
Storage array controller device (e.g., RAID)
0Dh
SES-2
Enclosure services device
0Eh
RBC
Simplified direct-access device (e.g., magnetic disk)
0Fh
OCRW
Optical card reader/writer device
10h
BCC
Bridge Controller Commands
11h
OSD-2
Object-based Storage Device
12h
ADC-3
Automation/Drive Interface
13h
clause 9
Security manager device
14h to 1Dh
Reserved
1Eh
clause 8
Well known logical unit b
1Fh
Unknown or no device type
a All standards are subject to revision, and parties to agreements based on this standard are
encouraged to investigate the possibility of applying the most recent editions of the listed
standards.
b All well known logical units use the same peripheral device type code.


The VERSION field indicates the implemented version of this standard and is defined in table 177.
The Normal ACA Supported (NORMACA) bit set to one indicates that the device server supports a NACA bit set
to one in the CDB CONTROL byte and supports the ACA task attribute (see SAM-5). A NORMACA bit set to zero
indicates that the device server does not support a NACA bit set to one and does not support the ACA task
attribute.
A hierarchical support (HISUP) bit set to zero indicates the SCSI target device does not use the hierarchical
addressing model to assign LUNs to logical units. A HISUP bit set to one indicates the SCSI target device uses
the hierarchical addressing model to assign LUNs to logical units.
The RESPONSE DATA FORMAT field indicates the format of the standard INQUIRY data and shall be set as
shown in table 174. A RESPONSE DATA FORMAT field set to 2h indicates that the standard INQUIRY data is in
the format defined in this standard. Response data format values less than 2h are obsolete. Response data
format values greater than 2h are reserved.
The ADDITIONAL LENGTH field indicates the length in bytes of the remaining standard INQUIRY data. The
contents of the ADDITIONAL LENGTH field are not altered based on the allocation length (see 4.2.5.6).
An SCC Supported (SCCS) bit set to one indicates that the SCSI target device contains an embedded storage
array controller component that is addressable through this logical unit. See SCC-2 for details about storage
array controller devices. An SCCS bit set to zero indicates that no embedded storage array controller
component is addressable through this logical unit.
An Access Controls Coordinator (ACC) bit set to one indicates that the SCSI target device contains an access
controls coordinator that is addressable through this logical unit. An ACC bit set to zero indicates that no
access controls coordinator is addressable through this logical unit. If the SCSI target device contains an
access controls coordinator that is addressable through any logical unit other than the ACCESS CONTROLS
well known logical unit (see 8.3), then the ACC bit shall be set to one for LUN 0.
Table 177 — VERSION field
Code
Description
00h
The device server does not claim conformance to any standard.
01h to 02h
Obsolete
03h
The device server complies to ANSI INCITS 301-1997 (a withdrawn standard).
04h
The device server complies to ANSI INCITS 351-2001 (SPC-2).
05h
The device server complies to ANSI INCITS 408-2005 (SPC-3).
06h
The device server complies to this standard.
07h
Reserved
08h to 0Ch
Obsolete
0Dh to 3Fh
Reserved
40h to 44h
Obsolete
45h to 47h
Reserved
48h to 4Ch
Obsolete
4Dh to 7Fh
Reserved
80h to 84h
Obsolete
85h to 87h
Reserved
88h to 8Ch
Obsolete
8Dh to FFh
Reserved


The contents of the target port group support (TPGS) field (see table 178) indicate the support for asymmetric
logical unit access (see 5.16).
A third-party copy (3PC) bit set to one indicates that the logical unit supports third-party copy commands (see
5.17.3). A 3PC bit set to zero indicates that the logical unit does not support third-party copy commands.
A PROTECT bit set to zero indicates that the logical unit does not support protection information. A PROTECT bit
set to one indicates that the logical unit supports:
a)
type 1 protection, type 2 protection, or type 3 protection (see SBC-3); or
b)
logical block protection (see SSC-4).
More information about the type of protection the logical unit supports is available in the SPT field (see 7.8.7).
An Enclosure Services (ENCSERV) bit set to one indicates that the SCSI target device contains an embedded
enclosure services component that is addressable through this logical unit. See SES-3 for details about
enclosure services. An ENCSERV bit set to zero indicates that no embedded enclosure services component is
addressable through this logical unit.
A Multi Port (MULTIP) bit set to one indicates that this is a multi-port (two or more ports) SCSI target device
and conforms to the SCSI multi-port device requirements found in the applicable standards (e.g., SAM-5, a
SCSI transport protocol standard and possibly provisions of a command standard). A MULTIP bit set to zero
indicates that this SCSI target device has a single port and does not implement the multi-port requirements.
The CMDQUE bit shall be set to one indicating that the logical unit supports the command management model
defined in SAM-5.
The T10 VENDOR IDENTIFICATION field contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying the
vendor of the logical unit. The T10 vendor identification shall be one assigned by INCITS. A list of assigned
T10 vendor identifications is in Annex F and on the T10 web site (http://www.t10.org).
NOTE 30 - The T10 web site (http://www.t10.org) provides a convenient means to request an identification
code.
Table 178 — TPGS field
Code
Description
00b
The logical unit does not support asymmetric logical unit access or supports a form of asymmet-
ric access that is vendor specific. Neither the REPORT TARGET GROUPS nor the SET TAR-
GET PORT GROUPS commands is supported.
01b
The logical unit supports only implicit asymmetric logical unit access (see 5.16.2.7). The logical
unit is capable of changing target port asymmetric access states without a SET TARGET PORT
GROUPS command. The REPORT TARGET PORT GROUPS command is supported and the
SET TARGET PORT GROUPS command is not supported.
10b
The logical unit supports only explicit asymmetric logical unit access (see 5.16.2.8). The logical
unit only changes target port asymmetric access states as requested with the SET TARGET
PORT GROUPS command. Both the REPORT TARGET PORT GROUPS command and the
SET TARGET PORT GROUPS command are supported.
11b
The logical unit supports both explicit and implicit asymmetric logical unit access. Both the
REPORT TARGET PORT GROUPS command and the SET TARGET PORT GROUPS
commands are supported.


The PRODUCT IDENTIFICATION field contains sixteen bytes of left-aligned ASCII data (see 4.3.1) defined by the
vendor.
The PRODUCT REVISION LEVEL field contains four bytes of left-aligned ASCII data defined by the vendor.
The VERSION DESCRIPTOR fields provide for identifying up to eight standards to which the SCSI target device
and/or logical unit claim conformance. The value in each VERSION DESCRIPTOR field shall be selected from
table 179. All version descriptor values not listed in table 179 are reserved. Technical Committee T10 of
INCITS maintains an electronic copy of the information in table 179 on its world wide web site
(http://www.t10.org/). In the event that the T10 world wide web site is no longer active, access may be
possible via the INCITS world wide web site (http://www.incits.org), the ANSI world wide web site
(http://www.ansi.org), the IEC site (http://www.iec.ch/), the ISO site (http://www.iso.ch/), or the ISO/IEC JTC 1
web site (http://www.jtc1.org/). It is recommended that the first version descriptor be used for the SCSI archi-
tecture standard, followed by the physical transport standard if any, followed by the SCSI transport protocol
standard, followed by the appropriate SPC-x version, followed by the device type command set, followed by a
secondary command set if any.
Table 179 — Version descriptor values (part 1 of 12)
Standard
Version
Descriptor
Value
ACS-2 (no version claimed)
1761h
ADC (no version claimed)
03C0h
ADC ANSI INCITS 403-2005
03D7h
ADC T10/1558-D revision 7
03D6h
ADC T10/1558-D revision 6
03D5h
ADC-2 (no version claimed)
04A0h
ADC-2 ANSI INCITS 441-2008
04ACh
ADC-2 T10/1741-D revision 7
04A7h
ADC-2 T10/1741-D revision 8
04AAh
ADC-3 (no version claimed)
0500h
ADC-3 T10/1895-D revision 04
0502h
ADC-3 T10/1895-D revision 05
0504h
ADC-3 T10/1895-D revision 05a
0506h
ADP (no version claimed)
09C0h
ADT (no version claimed)
09E0h
ADT ANSI INCITS 406-2005
09FDh
ADT T10/1557-D revision 14
09FAh
ADT T10/1557-D revision 11
09F9h
ADT-2 (no version claimed)
0A20h
ADT-2 ANSI INCITS 472-2011
0A2Bh
ADT-2 T10/1742-D revision 06
0A22h
ADT-2 T10/1742-D revision 08
0A27h
ADT-2 T10/1742-D revision 09
0A28h
ATA/ATAPI-6 (no version claimed)
15E0h
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


ATA/ATAPI-6 ANSI INCITS 361-2002
15FDh
ATA/ATAPI-7 (no version claimed)
1600h
ATA/ATAPI-7 ISO/IEC 24739
161Eh
ATA/ATAPI-7 ANSI INCITS 397-2005
161Ch
ATA/ATAPI-7 T13/1532-D revision 3
1602h
ATA/ATAPI-8 ATA8-AAM (no version claimed)
1620h
ATA/ATAPI-8 ATA8-AAM ANSI INCITS 451-2008
1628h
ATA/ATAPI-8 ATA8-APT Parallel Transport (no version claimed)
1621h
ATA/ATAPI-8 ATA8-AST Serial Transport (no version claimed)
1622h
ATA/ATAPI-8 ATA8-ACS ATA/ATAPI Command Set (no version claimed)
1623h
ATA/ATAPI-8 ATA8-ACS ANSI INCITS 452-2009 w/ Amendment 1
162Ah
BCC (no version claimed)
0380h
EPI (no version claimed)
0B20h
EPI ANSI INCITS TR-23 1999
0B3Ch
EPI T10/1134 revision 16
0B3Bh
Fast-20 (no version claimed)
0AC0h
Fast-20 ANSI INCITS 277-1996
0ADCh
Fast-20 T10/1071 revision 06
0ADBh
FC 10GFC (no version claimed)
0EA0h
FC 10GFC ISO/IEC 14165-116
0EA3h
FC 10GFC ANSI INCITS 364-2003
0EA2h
FC 10GFC ISO/IEC 14165-116 with AM1
0EA5h
FC 10GFC ANSI INCITS 364-2003 with AM1 ANSI INCITS 364/AM1-2007
0EA6h
FC-AL (no version claimed)
0D40h
FC-AL ANSI INCITS 272-1996
0D5Ch
FC-AL-2 (no version claimed)
0D60h
FC-AL-2 ISO/IEC 14165-122 with AM1 & AM2
0D65h
FC-AL-2 ANSI INCITS 332-1999 with AM1-2003 & AM2-2006
0D63h
FC-AL-2 ANSI INCITS 332-1999 with Amnd 2 AM2-2006
0D64h
FC-AL-2 ANSI INCITS 332-1999 with Amnd 1 AM1-2003
0D7Dh
FC-AL-2 ANSI INCITS 332-1999
0D7Ch
FC-AL-2 T11/1133-D revision 7.0
0D61h
FC-DA (no version claimed)
12E0h
FC-DA ISO/IEC 14165-341
12E9h
FC-DA ANSI INCITS TR-36 2004
12E8h
FC-DA T11/1513-DT revision 3.1
12E2h
FC-DA-2 (no version claimed)
12C0h
FC-DA-2 INCITS TR-49 2012
12C9h
Table 179 — Version descriptor values (part 2 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


FC-DA-2 T11/1870DT revision 1.04
12C3h
FC-DA-2 T11/1870DT revision 1.06
12C5h
FC-FLA (no version claimed)
1320h
FC-FLA ANSI INCITS TR-20 1998
133Ch
FC-FLA T11/1235 revision 7
133Bh
FC-FS (no version claimed)
0DA0h
FC-FS ISO/IEC 14165-251
0DBDh
FC-FS ANSI INCITS 373-2003
0DBCh
FC-FS T11/1331-D revision 1.2
0DB7h
FC-FS T11/1331-D revision 1.7
0DB8h
FC-FS-2 (no version claimed)
0E00h
FC-FS-2 ANSI INCITS 242-2007 with AM1 ANSI INCITS 242/AM1-2007
0E03h
FC-FS-2 ANSI INCITS 242-2007
0E02h
FC-FS-3 (no version claimed)
0EE0h
FC-FS-3 ANSI INCITS 470-2011
0EEBh
FC-FS-3 T11/1861-D revision 0.9
0EE2h
FC-FS-3 T11/1861-D revision 1.0
0EE7h
FC-FS-3 T11/1861-D revision 1.10
0EE9h
FC-FS-4 (no version claimed)
0F60h
FC-LS (no version claimed)
0E20h
FC-LS ANSI INCITS 433-2007
0E29h
FC-LS T11/1620-D revision 1.62
0E21h
FC-LS-2 (no version claimed)
0F00h
FC-LS-2 ANSI INCITS 477-2011
0F07h
FC-LS-2 T11/2103-D revision 2.11
0F03h
FC-LS-2 T11/2103-D revision 2.21
0F05h
FC-LS-3 (no version claimed)
0F80h
FCP (no version claimed)
08C0h
FCP ANSI INCITS 269-1996
08DCh
FCP T10/0993-D revision 12
08DBh
FC-PH (no version claimed)
0D20h
FC-PH ANSI INCITS 230-1994
0D3Bh
FC-PH ANSI INCITS 230-1994 with Amnd 1 ANSI INCITS 230/AM1-1996
0D3Ch
FC-PH-3 (no version claimed)
0D80h
FC-PH-3 ANSI INCITS 303-1998
0D9Ch
FC-PI (no version claimed)
0DC0h
FC-PI ANSI INCITS 352-2002
0DDCh
FC-PI-2 (no version claimed)
0DE0h
Table 179 — Version descriptor values (part 3 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


FC-PI-2 ANSI INCITS 404-2006
0DE4h
FC-PI-2 T11/1506-D revision 5.0
0DE2h
FC-PI-3 (no version claimed)
0E60h
FC-PI-3 ANSI INCITS 460-2011
0E6Eh
FC-PI-3 T11/1625-D revision 2.0
0E62h
FC-PI-3 T11/1625-D revision 2.1
0E68h
FC-PI-3 T11/1625-D revision 4.0
0E6Ah
FC-PI-4 (no version claimed)
0E80h
FC-PI-4 ANSI INCITS 450-2009
0E88h
FC-PI-4 T11/1647-D revision 8.0
0E82h
FC-PI-5 (no version claimed)
0F20h
FC-PI-5 ANSI INCITS 479-2011
0F2Eh
FC-PI-5 T11/2118-D revision 2.00
0F27h
FC-PI-5 T11/2118-D revision 3.00
0F28h
FC-PI-5 T11/2118-D revision 6.00
0F2Ah
FC-PI-5 T11/2118-D revision 6.10
0F2Bh
FC-PI-6 (no version claimed)
0F40h
FC-PLDA (no version claimed)
1340h
FC-PLDA ANSI INCITS TR-19 1998
135Ch
FC-PLDA T11/1162 revision 2.1
135Bh
FCP-2 (no version claimed)
0900h
FCP-2 ANSI INCITS 350-2003
0917h
FCP-2 T10/1144-D revision 8
0918h
FCP-2 T10/1144-D revision 4
0901h
FCP-2 T10/1144-D revision 7
0915h
FCP-2 T10/1144-D revision 7a
0916h
FCP-3 (no version claimed)
0A00h
FCP-3 ISO/IEC 14776-223
0A1Ch
FCP-3 ANSI INCITS 416-2006
0A11h
FCP-3 T10/1560-D revision 4
0A0Fh
FCP-3 T10/1560-D revision 3f
0A07h
FCP-4 (no version claimed)
0A40h
FCP-4 ANSI INCITS 481-2012
0A46h
FCP-4 T10/1828-D revision 01
0A42h
FCP-4 T10/1828-D revision 02
0A44h
FCP-4 T10/1828-D revision 02b
0A45h
FC-SCM (no version claimed)
12A0h
FC-SCM INCITS TR-47 2012
12AAh
Table 179 — Version descriptor values (part 4 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


FC-SCM T11/1824DT revision 1.0
12A3h
FC-SCM T11/1824DT revision 1.1
12A5h
FC-SCM T11/1824DT revision 1.4
12A7h
FC-SP (no version claimed)
0E40h
FC-SP ANSI INCITS 426-2007
0E45h
FC-SP T11/1570-D revision 1.6
0E42h
FC-SP-2 (no version claimed)
0EC0h
FC-Tape (no version claimed)
1300h
FC-Tape ANSI INCITS TR-24 1999
131Ch
FC-Tape T11/1315 revision 1.17
131Bh
FC-Tape T11/1315 revision 1.16
1301h
IEEE 1394 (no version claimed)
14A0h
ANSI IEEE 1394-1995
14BDh
IEEE 1394a (no version claimed)
14C0h
IEEE 1394b (no version claimed)
14E0h
IEEE 1667 (no version claimed)
FFC0h
IEEE 1667-2006
FFC1h
IEEE 1667-2009
FFC2h
iSCSI (no version claimed)
0960h
MMC (no version claimed)
0140h
MMC ANSI INCITS 304-1997
015Ch
MMC T10/1048-D revision 10a
015Bh
MMC-2 (no version claimed)
0240h
MMC-2 ANSI INCITS 333-2000
025Ch
MMC-2 T10/1228-D revision 11a
025Bh
MMC-2 T10/1228-D revision 11
0255h
MMC-3 (no version claimed)
02A0h
MMC-3 ANSI INCITS 360-2002
02B8h
MMC-3 T10/1363-D revision 10g
02B6h
MMC-3 T10/1363-D revision 9
02B5h
MMC-4 (no version claimed)
03A0h
MMC-4 ANSI INCITS 401-2005
03BFh
MMC-4 T10/1545-D revision 3
03BDh
MMC-4 T10/1545-D revision 3d
03BEh
MMC-4 T10/1545-D revision 5
03B0h
MMC-4 T10/1545-D revision 5a
03B1h
MMC-5 (no version claimed)
0420h
MMC-5 T10/1675-D revision 04
0432h
Table 179 — Version descriptor values (part 5 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


MMC-5 ANSI INCITS 430-2007
0434h
MMC-5 T10/1675-D revision 03
042Fh
MMC-5 T10/1675-D revision 03b
0431h
MMC-6 (no version claimed)
04E0h
MMC-6 T10/1836-D revision 02b
04E3h
MMC-6 T10/1836-D revision 02g
04E5h
MMC-6 ANSI INCITS 468-2010
04E6h
OCRW (no version claimed)
0280h
OCRW ISO/IEC 14776-381
029Eh
OSD (no version claimed)
0340h
OSD ANSI INCITS 400-2004
0356h
OSD T10/1355-D revision 10
0355h
OSD T10/1355-D revision 0
0341h
OSD T10/1355-D revision 7a
0342h
OSD T10/1355-D revision 8
0343h
OSD T10/1355-D revision 9
0344h
OSD-2 (no version claimed)
0440h
OSD-2 ANSI INCITS 458-2011
0448h
OSD-2 T10/1729-D revision 4
0444h
OSD-2 T10/1729-D revision 5
0446h
OSD-3 (no version claimed)
0560h
PQI (no version claimed)
2200h
RBC (no version claimed)
0220h
RBC ANSI INCITS 330-2000
023Ch
RBC T10/1240-D revision 10a
0238h
SAM (no version claimed)
0020h
SAM ANSI INCITS 270-1996
003Ch
SAM T10/0994-D revision 18
003Bh
SAM-2 (no version claimed)
0040h
SAM-2 ISO/IEC 14776-412
005Eh
SAM-2 ANSI INCITS 366-2003
005Ch
SAM-2 T10/1157-D revision 24
0055h
SAM-2 T10/1157-D revision 23
0054h
SAM-3 (no version claimed)
0060h
SAM-3 ANSI INCITS 402-2005
0077h
SAM-3 T10/1561-D revision 14
0076h
SAM-3 T10/1561-D revision 7
0062h
SAM-3 T10/1561-D revision 13
0075h
Table 179 — Version descriptor values (part 6 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


SAM-4 (no version claimed)
0080h
SAM-4 ISO/IEC 14776-414
0092h
SAM-4 ANSI INCITS 447-2008
0090h
SAM-4 T10/1683-D revision 13
0087h
SAM-4 T10/1683-D revision 14
008Bh
SAM-5 (no version claimed)
00A0h
SAM-5 T10/2104-D revision 4
00A2h
SAS (no version claimed)
0BE0h
SAS ANSI INCITS 376-2003
0BFDh
SAS T10/1562-D revision 05
0BFCh
SAS T10/1562-D revision 01
0BE1h
SAS T10/1562-D revision 03
0BF5h
SAS T10/1562-D revision 04
0BFAh
SAS T10/1562-D revision 04
0BFBh
SAS-1.1 (no version claimed)
0C00h
SAS-1.1 ISO/IEC 14776-151
0C12h
SAS-1.1 ANSI INCITS 417-2006
0C11h
SAS-1.1 T10/1601-D revision 9
0C07h
SAS-1.1 T10/1601-D revision 10
0C0Fh
SAS-2 (no version claimed)
0C20h
SAS-2 ANSI INCITS 457-2010
0C2Ah
SAS-2 T10/1760-D revision 14
0C23h
SAS-2 T10/1760-D revision 15
0C27h
SAS-2 T10/1760-D revision 16
0C28h
SAS-2.1 (no version claimed)
0C40h
SAS-2.1 ANSI INCITS 478-2011
0C4Eh
SAS-2.1 T10/2125-D revision 04
0C48h
SAS-2.1 T10/2125-D revision 06
0C4Ah
SAS-2.1 T10/2125-D revision 07
0C4Bh
SAS-3 (no version claimed)
0C60h
SAT (no version claimed)
1EA0h
SAT ANSI INCITS 431-2007
1EADh
SAT T10/1711-D revision 9
1EABh
SAT T10/1711-D revision 8
1EA7h
SAT-2 (no version claimed)
1EC0h
SAT-2 ANSI INCITS 465-2010
1ECAh
SAT-2 T10/1826-D revision 06
1EC4h
SAT-2 T10/1826-D revision 09
1EC8h
Table 179 — Version descriptor values (part 7 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


SAT-3 (no version claimed)
1EE0h
SAT-3 T10/2126-D revision 4
1EE2h
SAT-4 (no version claimed)
1F00h
SBC (no version claimed)
0180h
SBC ANSI INCITS 306-1998
019Ch
SBC T10/0996-D revision 08c
019Bh
SBC-2 (no version claimed)
0320h
SBC-2 ISO/IEC 14776-322
033Eh
SBC-2 ANSI INCITS 405-2005
033Dh
SBC-2 T10/1417-D revision 16
033Bh
SBC-2 T10/1417-D revision 5a
0322h
SBC-2 T10/1417-D revision 15
0324h
SBC-3 (no version claimed)
04C0h
SBP-2 (no version claimed)
08E0h
SBP-2 ANSI INCITS 325-1998
08FCh
SBP-2 T10/1155-D revision 04
08FBh
SBP-3 (no version claimed)
0980h
SBP-3 ANSI INCITS 375-2004
099Ch
SBP-3 T10/1467-D revision 5
099Bh
SBP-3 T10/1467-D revision 1f
0982h
SBP-3 T10/1467-D revision 3
0994h
SBP-3 T10/1467-D revision 4
099Ah
SCC (no version claimed)
0160h
SCC ANSI INCITS 276-1997
017Ch
SCC T10/1047-D revision 06c
017Bh
SCC-2 (no version claimed)
01E0h
SCC-2 ANSI INCITS 318-1998
01FCh
SCC-2 T10/1125-D revision 04
01FBh
SES (no version claimed)
01C0h
SES ANSI INCITS 305-1998
01DCh
SES T10/1212-D revision 08b
01DBh
SES ANSI INCITS 305-1998 w/ Amendment ANSI INCITS.305/AM1-2000
01DEh
SES T10/1212 revision 08b w/ Amendment ANSI INCITS.305/AM1-2000
01DDh
SES-2 (no version claimed)
03E0h
SES-2 ISO/IEC 14776-372
03F2h
SES-2 ANSI INCITS 448-2008
03F0h
SES-2 T10/1559-D revision 16
03E1h
SES-2 T10/1559-D revision 19
03E7h
Table 179 — Version descriptor values (part 8 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


SES-2 T10/1559-D revision 20
03EBh
SES-3 (no version claimed)
0580h
SFSC (no version claimed)
05E0h
SIP (no version claimed)
08A0h
SIP ANSI INCITS 292-1997
08BCh
SIP T10/0856-D revision 10
08BBh
SMC (no version claimed)
01A0h
SMC ISO/IEC 14776-351
01BEh
SMC ANSI INCITS 314-1998
01BCh
SMC T10/0999-D revision 10a
01BBh
SMC-2 (no version claimed)
02E0h
SMC-2 ANSI INCITS 382-2004
02FEh
SMC-2 T10/1383-D revision 7
02FDh
SMC-2 T10/1383-D revision 5
02F5h
SMC-2 T10/1383-D revision 6
02FCh
SMC-3 (no version claimed)
0480h
SMC-3 T10/1730-D revision 15
0482h
SMC-3 T10/1730-D revision 16
0484h
SOP (no version claimed)
21E0h
SPC (no version claimed)
0120h
SPC ANSI INCITS 301-1997
013Ch
SPC T10/0995-D revision 11a
013Bh
SPC-2 (no version claimed)
0260h
SPC-2 ISO/IEC 14776-452
0278h
SPC-2 ANSI INCITS 351-2001
0277h
SPC-2 T10/1236-D revision 20
0276h
SPC-2 T10/1236-D revision 12
0267h
SPC-2 T10/1236-D revision 18
0269h
SPC-2 T10/1236-D revision 19
0275h
SPC-3 (no version claimed)
0300h
SPC-3 ISO/IEC 14776-453
0316h
SPC-3 ANSI INCITS 408-2005
0314h
SPC-3 T10/1416-D revision 7
0301h
SPC-3 T10/1416-D revision 21
0307h
SPC-3 T10/1416-D revision 22
030Fh
SPC-3 T10/1416-D revision 23
0312h
SPC-4 (no version claimed)
0460h
SPC-4 T10/1731-D revision 16
0461h
Table 179 — Version descriptor values (part 9 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


SPC-4 T10/1731-D revision 18
0462h
SPC-4 T10/1731-D revision 23
0463h
SPC-4 T10/1731-D revision 36
0466h
SPC-5 (no version claimed)
05C0h
SPI (no version claimed)
0AA0h
SPI ANSI INCITS 253-1995
0ABAh
SPI T10/0855-D revision 15a
0AB9h
SPI ANSI INCITS 253-1995 with SPI Amnd ANSI INCITS 253/AM1-1998
0ABCh
SPI T10/0855-D revision 15a with SPI Amnd revision 3a
0ABBh
SPI-2 (no version claimed)
0AE0h
SPI-2 ANSI INCITS 302-1999
0AFCh
SPI-2 T10/1142-D revision 20b
0AFBh
SPI-3 (no version claimed)
0B00h
SPI-3 ANSI INCITS 336-2000
0B1Ch
SPI-3 T10/1302-D revision 14
0B1Ah
SPI-3 T10/1302-D revision 10
0B18h
SPI-3 T10/1302-D revision 13a
0B19h
SPI-4 (no version claimed)
0B40h
SPI-4 ANSI INCITS 362-2002
0B56h
SPI-4 T10/1365-D revision 7
0B54h
SPI-4 T10/1365-D revision 9
0B55h
SPI-4 T10/1365-D revision 10
0B59h
SPI-5 (no version claimed)
0B60h
SPI-5 ANSI INCITS 367-2003
0B7Ch
SPI-5 T10/1525-D revision 6
0B7Bh
SPI-5 T10/1525-D revision 3
0B79h
SPI-5 T10/1525-D revision 5
0B7Ah
SPL (no version claimed)
20A0h
SPL ANSI INCITS 476-2011
20A7h
SPL ANSI INCITS 476-2011 + SPL AM1 INCITS 476/AM1 2012
20A8h
SPL T10/2124-D revision 6a
20A3h
SPL T10/2124-D revision 7
20A5h
SPL-2 (no version claimed)
20C0h
SPL-2 T10/2228-D revision 4
20C2h
SPL-2 T10/2228-D revision 5
20C4h
SPL-3 (no version claimed)
20E0h
SRP (no version claimed)
0940h
SRP ANSI INCITS 365-2002
095Ch
Table 179 — Version descriptor values (part 10 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.


SRP T10/1415-D revision 16a
0955h
SRP T10/1415-D revision 10
0954h
SSA-PH2 (no version claimed)
1360h
SSA-PH2 ANSI INCITS 293-1996
137Ch
SSA-PH2 T10.1/1145-D revision 09c
137Bh
SSA-PH3 (no version claimed)
1380h
SSA-PH3 ANSI INCITS 307-1998
139Ch
SSA-PH3 T10.1/1146-D revision 05b
139Bh
SSA-S2P (no version claimed)
0880h
SSA-S2P ANSI INCITS 294-1996
089Ch
SSA-S2P T10.1/1121-D revision 07b
089Bh
SSA-S3P (no version claimed)
0860h
SSA-S3P ANSI INCITS 309-1998
087Ch
SSA-S3P T10.1/1051-D revision 05b
087Bh
SSA-TL1 (no version claimed)
0840h
SSA-TL1 ANSI INCITS 295-1996
085Ch
SSA-TL1 T10.1/0989-D revision 10b
085Bh
SSA-TL2 (no version claimed)
0820h
SSA-TL2 ANSI INCITS 308-1998
083Ch
SSA-TL2 T10.1/1147-D revision 05b
083Bh
SSC (no version claimed)
0200h
SSC ANSI INCITS 335-2000
021Ch
SSC T10/0997-D revision 22
0207h
SSC T10/0997-D revision 17
0201h
SSC-2 (no version claimed)
0360h
SSC-2 ANSI INCITS 380-2003
037Dh
SSC-2 T10/1434-D revision 9
0375h
SSC-2 T10/1434-D revision 7
0374h
SSC-3 (no version claimed)
0400h
SSC-3 ANSI INCITS 467-2011
0409h
SSC-3 T10/1611-D revision 04a
0403h
SSC-3 T10/1611-D revision 05
0407h
SSC-4 (no version claimed)
0520h
SSC-4 T10/2123-D revision 2
0523h
SSC-5 (no version claimed)
05A0h
SST (no version claimed)
0920h
SST T10/1380-D revision 8b
0935h
UAS (no version claimed)
1740h
Table 179 — Version descriptor values (part 11 of 12)
Standard
Version
Descriptor
Value
A numeric ordered listing of the version descriptor value assignments is provided in E.9.
