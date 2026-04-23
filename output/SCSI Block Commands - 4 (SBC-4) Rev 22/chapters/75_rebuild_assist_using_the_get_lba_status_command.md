# Rebuild assist using the GET LBA STATUS command

Annex J
(informative)
Rebuild assist using the GET LBA STATUS command
J.1 Overview
This annex describes an example of an application client rebuilding data from a SCSI device with a physical
element failure. This examples uses the following commands:
a)
the GET PHYSICAL ELEMENT STATUS command (see 5.8);
b)
the GET LBA STATUS (32) command (see 5.7); and
c)
write commands.
J.2 Discovery process
This example show how an application client is able to discover what LBAs are affected on a block storage
device with a capacity of 2_147_483_648 bytes, a logical block length of 4_096 bytes, and the physical
element identified by identifier 7 with a health status of 65. The discovery process for the LBAs that are
affected by the failure of a this physical element consists of following sequence. The application client issues
a GET PHYSICAL ELEMENT STATUS command with:
a)
the STARTING ELEMENT field set to 0000h;
b)
the FILTER field set to 01b (i.e., physical elements with a health outside manufacturers specification
limit or depopulated); and
c)
the REPORT TYPE field set to 1h (i.e., storage elements).
In this example the GET PHYSICAL ELEMENT STATUS command returns one descriptor in the parameter
data. That descriptor contains:
a)
an element identifier of 0007h;
b)
a physical element type of 01h; and
c)
a physical element health of 65h.
The application client then issues a GET LBA STATUS (32) command with:
a)
the REPORT TYPE field set to 00h (i.e., return descriptors for all LBAs);
b)
the STARTING LOGICAL BLOCK ADDRESS field set to 0000_0000h;
c)
the SCAN LENGTH field set to FFFFh; and
d)
the ELEMENT IDENTIFIER field set to 0007h.
Any LBAs from 0000_0000h to 0000_FFFFh that are mapped to physical element 0007h are included in the
returned parameter data.
The application client then issues a GET LBA STATUS (32) command with:
a)
the REPORT TYPE field set to 00h;
b)
the STARTING LOGICAL BLOCK ADDRESS field set to 0001_0000h;
c)
the SCAN LENGTH field set to FFFFh; and
d)
the ELEMENT IDENTIFIER field set to 0007h.
Any LBAs from 0001_0000h to 0001_FFFFh that are mapped to physical element 0007h are included in the
returned parameter data.
The application client continues issuing GET LBA STATUS (32) commands incrementing the STARTING
LOGICAL BLOCK ADDRESS field by 1_0000h for each command until it issues a GET LBA STATUS (32)
command with a STARTING LOGICAL BLOCK ADDRESS field set to 0079_0000h.


After issuing all necessary GET LBA STATUS (32) commands, the application client has a complete list of the
LBAs affected by the physical element that is bad and can retrieve the user data from another source and
write it to the SCSI device causing it to be written to a different physical element.


Annex K
(informative)
Direct access block devices with shared resources
K.1 Overview
Traditionally, most disk drives have shipped with only one logical unit supported. SAM-6 allows for multiple
logical units to be contained in one SCSI target device, and many products (e.g., storage arrays) have
incorporated this feature. Within the boundaries defined in SAM-6, these logical units are completely
independent of each other. In practice, there may be resources shared between the logical units and such
sharing may be observable to SCSI initiator devices.
This annex reviews effects that SCSI initiator devices may be able to observe if a direct access block device
shares resources between logical units and describes methods by which a SCSI initiator device may be able
to discover that certain resources are shared.
Designs for direct access block devices balance component costs against effects that are observable to SCSI
initiator devices. Small numbers of components lower cost but increase the numbers and severity of the
effects that are observable to SCSI initiator devices. This annex discusses these tradeoffs.
K.2 Downloading and activating microcode
SPC-6 allows for either separate microcode per logical unit or one microcode that is used by multiple logical
units contained in a SCSI target device. An application client may detect if microcode is shared by multiple
logical units by observing that the MICROCODE HAS BEEN CHANGED unit attention condition, if any, or the
MICROCODE HAS BEEN CHANGED WITHOUT RESET unit attention condition, if any, occurs on logical
units other than the logical unit that performed the microcode download operation and activation.
K.3 Caching
The direct access block device caching model (see 4.15) allows, among other choices, a separate cache per
logical unit or a cache that is shared by the attached logical units. The advantages and disadvantages of these
approaches are vendor specific.
The sharing characteristics of the cache in a direct access block device are the same as the sharing
characteristics of the Caching mode page (see 6.5.6). The MLUS bit for the Caching mode page (i.e., mode
page 08h) in the Mode Page Policy VPD page (see SPC-6) indicates whether the affected logical units share
the cache or each logical unit has its own cache.
K.4 Power management
The SPC-6 requirements for the idle power condition and the standby power condition allow a logical unit to
ignore any request to change a specific power condition until a vendor specific group of logical units have
changed their power condition in similar ways. As a result, there is variability in the exact point at which the
power condition of a logical unit in a SCSI target device changes in a way that is observable to the device
server.
The START STOP UNIT command requirements for the START bit (see 5.31) define a case in which the logical
unit is required to transition to the stopped power condition (e.g., the rotating medium spindle is stopped). This
