# Direct access block devices with shared resources

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


requirement may result in a START STOP UNIT command that is processed by one logical unit affecting more
than one logical unit (e.g., in a SCSI target device that has only one rotating medium spindle).
Some SCSI target devices process the stopped power condition caused by a START STOP UNIT command
in the same way that the idle power condition and the standby power condition are processed in SPC-6 (i.e.,
requests to change a specific power condition are ignored until a vendor specific group of logical units have
changed their power condition in similar ways).
Application clients that are trying to stop the rotating medium spindle in a SCSI target device (e.g., to facilitate
removal of that SCSI target device from the configuration), should send appropriate START STOP UNIT
commands to each logical unit in that SCSI target device that indicates participation in a vendor specific group
of logical units. Information about participation in a vendor specific group of logical units may be available from
the MLU field in the descriptor associated with the START STOP UNIT command in the REPORT
SUPPORTED OPERATION CODES command parameter data (see K.7).
K.5 Mode page considerations
The MLUS bit in the Mode Page Policy VPD page (see SPC-6) indicates whether or not multiple logical units in
a SCSI target device share the mode page and subpage identified by each descriptor in the Mode Page Policy
VPD page. If any field in a mode page is shared by multiple logical units, then the Mode Page Policy VPD
page reports that mode page as being shared.
The Disconnect-Reconnect mode page and all protocol-specific modes pages are shared by all logical units in
a SCSI target device (see SPC-6).
A change that is made in a mode parameter that is shared by multiple logical units results in a unit attention
condition being established with the additional sense code set to MODE PARAMETERS CHANGED as
described in SPC-6.
EXAMPLE - The Power Conditions mode page is an example of a mode page where some fields are shared and some
fields are not. If a rotating medium spindle is shared by multiple logical units and multiple head assemblies are not shared
by those logical units, then:
a)
the Power Conditions mode page fields (see SPC-6) that affect whether the medium spindle is rotating are
shared by those logical units; and
b)
the Power Conditions mode page fields that affect whether a head assembly is retracted from the medium are not
shared by those logical units.
K.6 Log page considerations
The choice of whether a log page is maintained separately for each logical unit or aggregates information for
multiple logical units is vendor specific.
If a SCSI target device returns a log page that aggregates information for multiple logical units, then a LOG
SELECT command that resets that log page resets the log data for all of those logical units in that SCSI target
device.
The Power Condition Transitions log page (see SPC-6) has a high probability of being shared. Sharing for the
Cache Memory Statistics log page (see SPC-6) has a high probability of having the same sharing as the
Caching mode page (see K.3).
Separate log pages for each logical unit are recommended in cases where:
a)
the information is specific to the interactions between that logical unit and the application client (e.g.,
the Last n Deferred Error or Asynchronous Events log page (see SPC-6), and the Application Client
log page (see SPC-6)); and
b)
LBA values that are specific to one logical unit are returned (e.g., Background Scan Results log page
(see 6.4.2) and the Pending Defects log page (see 6.4.8)).


EXAMPLE - Some log pages may have a mix of log parameters where some parameter values are an aggregate of
multiple logical units and other parameters are specific to that logical unit. If a rotating medium spindle is shared by
multiple logical units and multiple head assemblies are not shared by those logical units, then:
a)
the Power Conditions Transitions log page (see SPC-6) log parameters that are affected by whether the medium
spindle is rotating may report the same value for each logical unit; and
b)
the Power Conditions Transitions log page log parameters that are affected by whether a head assembly is
retracted from the medium may report a different value for each logical unit.
K.7 Command considerations
The MLU field in the REPORT SUPPORTED OPERATION CODES command parameter data (see SPC-6)
indicates whether the command indicated by the command descriptor affects multiple logical units in a SCSI
target device.
Some commands (see K.8) are defined to produce adverse effects (e.g., data loss, degraded performance) on
the logical unit in which they are processed. If these commands affect logical units other than the one in which
they are processed, then application clients that are accessing those other logical units may observe
unexpected adverse effects.
If a SCSI target device supports any of the commands described in K.8 on LUN 0 only, then an application
client may detect this case by comparing the REPORT SUPPORTED OPERATION CODES parameter data
(see SPC-6) from different logical units.
K.8 Commands with a high probability of affecting more than one logical unit
K.8.1 The FORMAT UNIT command
The MLU field (see S.7) may indicate whether the processing of a FORMAT UNIT command (see 5.4) affects
more than one logical unit.
If the FORMAT UNIT command affects multiple logical units, then the processing of a FORMAT UNIT
command in any of those logical units causes all of those logical units:
a)
to process commands as described in 4.33; and
b)
to be initialized as required by the FORMAT UNIT command parameters (see 5.4).
K.8.2 The REMOVE ELEMENT AND TRUNCATE command
The MLU field (see K.7) may indicate whether the processing of a REMOVE ELEMENT AND TRUNCATE
command (see 5.26) affects more than one logical unit.
If one or more of the elements processed by a REMOVE ELEMENT AND TRUNCATE command is shared
between logical units, then processing the command in one logical unit affects all the logical units that share
that element.
If a REMOVE ELEMENT AND TRUNCATE command service action affects multiple logical units, then the
processing of that REMOVE ELEMENT AND TRUNCATE command service action in any of those logical
units causes all of those logical units:
a)
to process commands as described in 4.36; and
b)
to be affected as required by the REMOVE ELEMENT AND TRUNCATE command parameters (see
5.26).
K.8.3 The SANITIZE command
The MLU field (see K.7) may indicate whether the processing of a SANITIZE command (see 5.30) affects more
than one logical unit. Each sanitize service action is reported separately by the REPORT SUPPORTED


OPERATION CODES command (see SPC-6). Some service actions may affect multiple logical units and
some may affect only one logical unit.
If a SANITIZE command service action affects multiple logical units, then the processing of that SANITIZE
command service action in any of those logical units causes all of those logical units:
a)
to process commands as described in 4.11; and
b)
to be sanitized as required by the SANITIZE command parameters (see 5.30).
K.8.4 The START STOP UNIT command
The MLU field (see K.7) may indicate whether the processing of a START STOP UNIT command (see 5.31)
affects more than one logical unit.
The START STOP UNIT command is able to cause a shared rotating medium spindle to stop rotating, a
condition that affects all the logical units that share that rotating medium spindle (see K.4).
K.8.5 The SEND DIAGNOSTIC command and RECEIVE DIAGNOSTIC RESULTS command
The MLU field (see K.7) for the SEND DIAGNOSTIC command may indicate whether the default self test and
the SELF-TEST CODE field diagnostics affects more than one logical unit. If the default self test and the
SELF-TEST CODE field diagnostics affect multiple logical units, then all affected logical units return a
SELF-TEST IN PROGRESS additional sense code while the test is in progress.
The RECEIVE DIAGNOSTIC RESULTS command only affects a single logical unit, but may return results that
apply to multiple logical units.
The Translate Address diagnostic page (see 6.3.4 and 6.3.5) only applies to one logical unit, regardless of the
value in the MLU field for the SEND DIAGNOSTIC command.
The choice of whether other diagnostic pages affect one logical unit or more than one logical unit is vendor
specific.
K.8.6 The WRITE BUFFER command and READ BUFFER command
The MLU field (see K.7) may indicate whether the processing of a WRITE BUFFER command (see SPC-6)
affects more than one logical unit. The MLU field (see K.7) indicates whether the processing of a READ
BUFFER command (see SPC-6) may affect more than one logical unit.
The considerations associated with microcode download and activation (see K.2) may affect the value
returned in the MLU field for the WRITE BUFFER command.
K.9 Common Mandatory SCSI Commands
The REQUEST SENSE command (see SPC-6) and the TEST UNIT READY command return information that
depends on the current operating conditions in one logical unit. Although some current operating conditions
affect multiple logical units in a SCSI target device, sense data is interpreted as applying only to the
addressed logical unit.
Although some of the information returned by the INQUIRY command (see SPC-6) is common to multiple
logical units in a SCSI target device, separate processing should be provided for an INQUIRY command
received by a specific logical unit.
For each of the multiple logical units in a SCSI target device, the REPORT LUNS command (see SPC-6)
reports all the accessible logical units in the SCSI target device, limited only by the contents of the SELECT
REPORT field in the CDB and the size of the Data-In Buffer.


Annex L
(informative)
Bibliography
ISO/IEC 14776-321, Information technology – Small Computer System Interface (SCSI-3) –
Part 321: SCSI Block Commands (SBC)
ISO/IEC 14776-322, Information technology – Small Computer System Interface (SCSI) –
Part 322: SCSI Block Commands-2 (SBC-2)
ISO/IEC 14776-154, Information technology – Small Computer System Interface (SCSI) –
Part 154: Serial Attached SCSI-3 (SAS-3)
ANSI INCITS 481-2011, Fibre Channel Protocol for SCSI - 4 (FCP-4)
ANSI INCITS 534-2019, Serial Attached SCSI-4 (SAS-3)
CFast (CFast)™, CompactFlash Association (see http://www.compactflash.org)
CompactFlash (CF), CompactFlash Association (see http://www.compactflash.org)
Memory Stick™ (MS). One Stop Site for Formats (see https://www.oss-formats.org)
MultiMediaCard (e•MMC), JEDEC® (see http://www.jedec.org)
NOTE 25  JEDEC® is a registered trademark of JEDEC Solid State Technology Association. This information
is given for the convenience of users of this standard and does not constitute an endorsement by ISO, IEC, or
ANSI.
Secure Digital Card (SD Card), SD Association (see http://www.sdcard.org)
XQD™ (XQD), CompactFlash Association (see http://www.compactflash.org)
Universal Flash Storage (UFS), JEDEC® (see http://www.jedec.org)
Differentiated Storage Services, ACM Special Interest Group on Operating Systems (see http://sigops.org/
sosp/sosp11/current/2011-Cascais/printable/05-mesnier.pdf)
