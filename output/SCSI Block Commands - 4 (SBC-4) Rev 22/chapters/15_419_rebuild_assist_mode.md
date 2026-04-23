# 4.19 Rebuild assist mode

The DESCRIPTOR TYPE field is described in SPC-6, and shall be set as shown in table 20 for the direct access
block device sense data descriptor.
A VALID bit set to zero indicates that the INFORMATION field is not defined in this standard or any other
command standard. A VALID bit set to one indicates the INFORMATION field contains valid information as defined
in this standard or a command standard.
A sense-key specific valid (SKSV) bit set to one indicates the sense key specific information contains valid
information as defined in SPC-6. An SKSV bit set to zero indicates that the sense key specific information is not
as defined by SPC-6.
The sense key specific information is described in the sense key specific sense data descriptor (see SPC-6).
The FIELD REPLACEABLE UNIT CODE field is described in the field replaceable unit sense data descriptor (see
SPC-6).
The INFORMATION field is described in the information sense data descriptor (see SPC-6).
The COMMAND-SPECIFIC INFORMATION field is described in the command-specific information sense data
descriptor (see SPC-6). The COMMAND-SPECIFIC INFORMATION field should be ignored in sense data for a
command or operation for which the COMMAND-SPECIFIC INFORMATION field is not defined and in sense data
that is not related to a command or operation (e.g., pollable sense data).
4.19 Rebuild assist mode
4.19.1 Rebuild assist mode overview
The rebuild assist mode provides a method for a SCSI storage array device (see SCC-2) to read recovered
logical blocks from a failed logical unit in a storage array instead of rebuilding the logical blocks from other
logical units in the storage array. This mode allows the failed logical unit to report logical blocks that are
unreadable without requiring the SCSI storage array device to read every LBA in the failed logical unit to
determine the unrecovered logical blocks. The SCSI storage array device then copies the logical blocks
recovered from the failed logical unit to a replacement logical unit and only rebuilds the failed logical blocks.
Enabling the rebuild assist mode:
a)
may cause the device server to initiate a self test to identify the scope of failures, if any;
b)
modifies READ command recovery behavior by the device server based on the setting of the RARC bit
(see 4.19.3 and 5.16); and
c)
may cause sense data to be returned by the device server that indicates the location of multiple failing
logical blocks on read commands and write commands.
The self-test operations performed by the device server while rebuild assist mode is enabled may result in
detection of failed physical elements. A predicted unrecovered error is an unrecovered error that is the result
of an attempt by the device server to access an LBA associated with a failed physical element. An unpredicted
unrecovered error is an unrecovered error that is the result of a device server accessing an LBA that is not
associated with a failed physical element.
4.19.2 Enabling rebuild assist mode
An application client should enable rebuild assist mode after the application client determines that a rebuild is
required. The application client enables the rebuild assist mode by setting the ENABLED bit to one and setting
the DISABLED PHYSICAL ELEMENT field to all zeros in the Rebuild Assist Output diagnostic page (see 6.3.3).
If a SEND DIAGNOSTIC command requests the enabling of the rebuild assist mode, then the device server:
1)
shall enable the rebuild assist mode;
2)
may perform a diagnostic test of the physical elements contained within the logical unit; and
3)
should disable any physical elements that are not functional if a diagnostic test of the physical
elements is performed.


The application client may verify that rebuild assist mode is enabled by verifying that the ENABLED bit is set to
one in the Rebuild Assist Input diagnostic page (see 6.3.2).
4.19.3 Using the rebuild assist mode
4.19.3.1 Using rebuild assist mode overview
After rebuild assist mode is enabled, the application client should issue read commands to read the available
logical block data from the failed logical unit. If the device server does not detect an unrecovered error while
processing a read command, then the device server should continue processing the read command.
The rebuild assist mode allows the device server to report unrecovered read errors or unrecovered write
errors that are either predicted (i.e., predicted unrecovered errors) or unpredicted (i.e., unpredicted
unrecovered errors).
4.19.3.2 Unpredicted unrecovered read error
If a device server receives a read command with the RARC bit set to one, then rebuild assist mode shall not
affect processing of the read command.
If rebuild assist mode is enabled and a device server receives a read command with the RARC bit set to zero
and the device server detects an unpredicted unrecovered error that is not a pseudo unrecovered read error
(see 4.18.2), then the device server:
1)
shall perform limited read recovery that is vendor specific;
2)
shall transfer the data for all recovered logical blocks, if any, from the logical block referenced by the
starting LBA of the failed read command up to the first unrecovered logical block (i.e., the lowest
numbered LBA) to the Data-in Buffer;
3)
shall terminate the command with CHECK CONDITION status with the sense key set to MEDIUM
ERROR, the additional sense code set to UNRECOVERED READ ERROR, and report the LBA
referencing the unrecovered logical block in the INFORMATION field (see SPC-6); and
4)
may use this failure in a vendor specific manner to predict other logical blocks that may be
unrecovered.
If the application client receives sense data with the sense key set to MEDIUM ERROR,  the additional sense
code set to UNRECOVERED READ ERROR, and the INFORMATION field indicating a valid LBA (see SPC-6),
then the application client should issue the next read command with the starting LBA set to the contents of the
INFORMATION field plus one.
4.19.3.3 Predicted unrecovered read error
If the device server receives a read command with the RARC bit set to one, then rebuild assist mode shall not
affect the processing of the read command.
If rebuild assist mode is enabled and the device server receives a read command with the RARC bit set to zero,
and the device server detects a predicted unrecovered error, then the device server:
1)
shall perform limited read recovery that is vendor specific;
2)
shall transfer the data for all recovered logical blocks, if any, from the logical block referenced by the
starting LBA of the failed read command up to the first predicted unrecovered LBA (i.e., the lowest
numbered LBA) to the Data-in Buffer; and
3)
shall terminate the read command with CHECK CONDITION status with the sense key set to
ABORTED COMMAND, the additional sense code set to MULTIPLE READ ERRORS, and:
A) report the following value in the INFORMATION field (see SPC-6):
a)
the LBA referencing the first unrecovered logical block (i.e., the lowest numbered LBA);
and
B) report the following value in the COMMAND-SPECIFIC INFORMATION field (see SPC-6):


a)
the LBA referencing the last unrecovered logical block (i.e., the highest numbered LBA) in a
sequence of contiguous unrecovered logical blocks that started with the LBA indicated in the
INFORMATION field.
If the application client receives sense data with the sense key set to ABORTED COMMAND, the additional
sense code set to MULTIPLE READ ERRORS, and the INFORMATION field indicating a valid LBA (see SPC-6),
then the application client should issue the next read command with the starting LBA set to the contents of the
COMMAND-SPECIFIC INFORMATION field plus one to continue recovering data from the logical unit. This process
should be repeated until all of the LBAs have been scanned.
4.19.3.4 Unpredicted unrecovered write error
If rebuild assist mode is enabled and the device server detects an unpredicted unrecovered error while
processing a write command, then the device server shall terminate the command with CHECK CONDITION
status with the sense key set to MEDIUM ERROR, the additional sense code set to WRITE ERROR, and
report the LBA referencing the first logical block (i.e., the lowest numbered LBA) in error in the INFORMATION
field (see SPC-6).
4.19.3.5 Predicted unrecovered write error
If rebuild assist mode is enabled and the device server detects a predicted unrecovered error while
processing a write command, then the device server:
1)
transfers the write data from the Data-Out Buffer;
2)
writes the transferred data up to the logical block referenced by the failing LBA; and
3)
shall terminate the write command with CHECK CONDITION status with the sense key set to
ABORTED COMMAND, the additional sense code set to MULTIPLE WRITE ERRORS, and:
A) report the following value in the INFORMATION field (see SPC-6):
a)
the LBA referencing the first logical block (i.e., the lowest numbered LBA) in error;
and
B) report the following value in the COMMAND-SPECIFIC INFORMATION field (see SPC-6):
a)
the LBA referencing the last logical block (i.e., the highest numbered LBA) in error in a
sequence of contiguous logical blocks that started with the LBA indicated in the INFORMATION
field.
If the application client receives sense data with the sense key set to ABORTED COMMAND, the additional
sense code set to MULTIPLE WRITE ERRORS, and the INFORMATION field indicating a valid LBA (see
SPC-6), then the application client should issue the next write command with the starting LBA set to the
contents of the COMMAND-SPECIFIC INFORMATION field plus one to continue writing to the logical unit.
4.19.4 Disabling the rebuild assist mode
Rebuild assist mode shall be disabled after a power on.
Rebuild assist mode shall not be affected by a hard reset, an I_T nexus loss, or any task management
functions (see SAM-6).
The application client disables rebuild assist mode by setting the ENABLED bit to zero in the Rebuild Assist
Output diagnostic page (see 6.3.3).
4.19.5 Testing rebuild assist mode
The Rebuild Assist Output diagnostic page (see 6.3.3) provides a method to test the application client’s
rebuild process.
An application client places a logical unit into a simulated failing condition by setting the ENABLED bit to one
and setting one or more bits in the DISABLED PHYSICAL ELEMENT field to one in the Rebuild Assist Output
diagnostic page.
