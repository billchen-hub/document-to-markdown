# SCSI standards family

xxxi
SCSI standards family
Figure 0 shows the relationship of this standard to the other standards and related projects in the SCSI family
of standards as of the publication of this standard.
Figure 0 — SCSI document relationships
The SCSI document structure in figure 0 is intended to show the general applicability of the documents to one
another. Figure 0 is not intended to imply any hierarchy, protocol stack, or system architecture relationship.
The functional areas identified in figure 0 characterize the scope of standards within a group as follows:
SCSI Architecture Model: Defines the SCSI systems model, the functional partitioning of the SCSI standard
set and requirements applicable to all SCSI implementations and implementation standards.
Device-Type Specific Command Sets: Implementation standards that define specific device types including
a device model for each device type. These standards specify the required commands and behaviors that are
specific to a given device type and prescribe the requirements to be followed by a SCSI initiator device when
sending commands to a SCSI target device having the specific device type. The commands and behaviors for
a specific device type may include by reference commands and behaviors that are defined by other command
sets.
Shared Command Set: An implementation standard that defines a model for all SCSI device types. This
standard specifies the required commands and behavior that is common to all SCSI devices, regardless of
device type, and prescribes the requirements to be followed by a SCSI initiator device when sending
commands to any SCSI target device.
SCSI Transport Protocols: Implementation standards that define the requirements for exchanging
information so that different SCSI devices are capable of communicating.
Interconnects: Implementation standards that define the communications mechanism employed by the SCSI
transport protocols. These standards may describe the electrical and signaling requirements essential for
SCSI devices to interoperate over a given interconnect. Interconnect standards may allow the interconnection
of devices other than SCSI devices in ways that are not defined by this standard.
The term SCSI is used to refer to the family of standards described in this subclause.
Device-type specific command sets
(e.g., MMC-6, this standard)
Primary command set
(shared for all device types)
(SPC-6)
SCSI transport protocols
(e.g.,  SPL-5, FCP-4)
Interconnects
(e.g., SAS-4, Fibre Channel)
SCSI Architecture Model
(SAM-6)


xxxii


AMERICAN NATIONAL STANDARD
BSR INCITS 506:201x
American National Standard
for Information Technology -
SCSI Block Commands – 4 (SBC-4)
1 Scope
This standard defines the command set extensions to facilitate operation of SCSI direct access block devices.
The clauses in this standard, implemented in conjunction with the applicable clauses of SPC-6, specify the
standard command set for SCSI direct access block devices.
The objectives of this standard are to:
a)
permit an application client to communicate over a SCSI service delivery subsystem (see SAM-6) with
a logical unit that declares itself to be a direct access block device in the PERIPHERAL DEVICE TYPE field
of the standard INQUIRY data (see SPC-6); and
b)
define commands and parameters unique to the direct access block device type.
This standard makes obsolete the following concepts from SBC-3:
a)
the EER bit and DCR bit (see 6.5.10);
b)
the TMC field and ETC bit in various log parameters;
c)
the READ LONG command and WRITE LONG command except for write uncorrectable; and
d)
the XOR command.
2 Normative references
The following documents, in whole or in part, are normatively referenced in this document and are
indispensable for its application. For dated references, only the edition cited applies. For undated references,
the latest edition of the referenced document (including any amendments) applies.
ISO/IEC 14776-342, Information technology – Small Computer System Interface (SCSI) – Part 342: SCSI-3
Controller Commands - 2 (SCC-2)
T10/BSR INCITS 491-2018, SCSI / ATA Translation - 4 (SAT-4)
INCITS 497-2012, Automation/Drive Interface Commands - 3 (ADC-3)
T10/BSR INCITS 518, SCSI Enclosure Services - 3 (SES-3) (planned as ISO/IEC 14776-373)
T10/BSR INCITS 536, Zoned Block Commands (ZBC) (planned as ISO/IEC 14776-345)
T10/BSR INCITS 546, SCSI Architecture Model - 6 (SAM-6) (under consideration)
T10/BSR INCITS 550, Zoned Block Commands - 2 (ZBC-2) (under consideration)
T10/BSR INCITS 554, SAS Protocol Layer - 5 (SPL-5) (under consideration)
T10/BSR INCITS 566, SCSI Primary Commands - 6 (SPC-6) (under consideration)
INCITS 468-2010, Multi-Media Commands - 6 (MMC-6)
INCITS 468-2010/AM 1 MultiMedia Command Set - 6 - Amendment 1 (MMC-6/AM 1)
