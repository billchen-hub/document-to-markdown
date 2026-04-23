# 4.36 Storage element depopulation and restoration

The COMMAND-SPECIFIC INFORMATION field should be set:
a)
as specified in 4.19.3.5, if rebuild assist mode is enabled and one or more predicted unrecovered
write errors occurs;
b)
to the count of LBA range descriptors for which the associated write operations completed without
error; or
c)
to zero if the device server does not support reporting a count of completed write operations.
4.36 Storage element depopulation and restoration
4.36.1 Overview
Storage element depopulation provides a REMOVE ELEMENT AND TRUNCATE command (see 5.26) for an
application client to depopulate a storage element from a SCSI target device (i.e., making a specified storage
element inaccessible for LBA resources and LBA mapping resources). After a storage element has been
depopulated, it may be restored to normal operation using a RESTORE ELEMENTS AND REBUILD
command (see 5.29).
A storage element that has been depopulated provides:
a)
no LBA mapping resources; and
b)
no LBA resources.
The media in a SCSI device may consist of a number of storage elements. Each of these storage elements:
a)
is associated with a number of physical blocks; and
b)
has a health status (see 5.8.2.2).
A storage element is a type of physical element. Physical elements are associated with a unique element
identifier that is assigned by the device server. The element identifier shall be non-zero. The association of
element identifiers to physical elements shall persist through all events (e.g., across all resets) except
microcode change (see SAM-6). The association of element identifiers to physical elements may persist
through microcode change events.
The health status of a given physical element may become degraded (i.e., outside manufacturer’s
specification limit). Such degradation may affect the overall performance of the SCSI device as seen by the
application client.
4.36.2 Physical element status change notification
The device server may monitor the status of storage elements as a background operation. The device server
may notify application clients that the status of one or more storage elements is not within expected
manufacturer’s specification limit (see 5.8.2.2). The specific mechanism for detection of this condition is not
defined by this standard. If the reporting of informational exceptions control warnings is enabled (i.e., the
EWASC bit is set to one (see 6.5.8)), then the device server shall report the change in condition as specified in
the Informational Exceptions Control mode page with the additional sense code set to WARNING -
PHYSICAL ELEMENT STATUS CHANGE.
Upon receipt of this notification the application client should examine physical element health (see 5.8).
4.36.3 Storage element depopulation
4.36.3.1 Overview
An application client may specify that a storage element be depopulated as described in 4.36.3. A device
server that supports storage element depopulation shall support:
a)
the REPORT SUPPORTED OPERATION CODES command (see SPC-6);
b)
the GET PHYSICAL ELEMENT STATUS command (see 5.8); and
c)
the REMOVE ELEMENT AND TRUNCATE command (see 5.26).


A REMOVE ELEMENT AND TRUNCATE command specifies that the device server:
a)
shall perform a depopulate operation (see 4.36.3.2);
b)
shall perform a truncate operation (see 4.36.3.3); and
c)
may perform an initialization.
The depopulate operation, truncate operation, and initialization operation, if any, may continue after the
successful completion of the REMOVE ELEMENT AND TRUNCATE command.
If an initialization is not performed, then user data written before the depopulate operation may be readable in
any accessible logical block.
The processing of a REMOVE ELEMENT AND TRUNCATE command shall not change:
a)
the logical block length (see 4.5);
b)
the lowest aligned logical block address (see 4.6.1); and
c)
the protection type (see 4.21.2).
A REMOVE ELEMENT AND TRUNCATE command may be issued for each storage element that is to be
removed from the current operating configuration.The effect of the processing of multiple REMOVE
ELEMENT AND TRUNCATE commands shall be cumulative (see 5.26).
A device server may have a limit on the number of storage elements that may be depopulated. If the device
server is requested to depopulate a storage element in excess of this limit, the device server may terminate
that command with a sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN CDB.
Upon successful completion of the REMOVE ELEMENT AND TRUNCATE command; the depopulate
operation, the truncate operation, and the initialization, if any, continue as background operations. While those
operations are in progress, the device server shall:
a)
provide pollable sense data (see SPC-6) with the sense key set to NOT READY, the additional sense
code set to DEPOPULATION IN PROGRESS and the PROGRESS INDICATION field in the sense data
set to indicate the progress of those operations; and
b)
process other commands as described in 4.36.5.
Upon the completion of the depopulate operation, the truncate operation, and the initialization, if any, the
contents of the user data area may have no relation to the contents of the user data area before the
processing of the REMOVE ELEMENT AND TRUNCATE command.
Any depopulate operation, truncate operation, and initialization initiated by a REMOVE ELEMENT AND
TRUNCATE command shall resume after any hard reset or logical unit reset. If any depopulate operation,
truncate operation, and initialization requested by a REMOVE ELEMENT AND TRUNCATE command is
interrupted by a power cycle then that operation shall be terminated and the logical unit may become format
corrupt.
If a depopulate operation, a truncate operation, or an initialization initiated by the REMOVE ELEMENT AND
TRUNCATE command does not complete successfully, then the logical unit may become format corrupt.
If the logical unit is format corrupt as a result of a depopulate operation, a truncate operation, or an
initialization requested by a REMOVE ELEMENT AND TRUNCATE command, then the device server shall
terminate any medium access command with CHECK CONDITION status, with the sense key set to MEDIUM
ERROR and the additional sense code set to DEPOPULATION FAILED.
4.36.3.2 Depopulate operations
A depopulate operation reduces the number of storage elements that are accessible to the logical unit’s
device server. To request a depopulate operation an application client issues a REMOVE ELEMENT AND
TRUNCATE command.
Automatic reassignment of defects may occur during depopulate operations. Following a successful
depopulate operation and before a write operation to an LBA, a read command or verify command that
specifies that LBA that completes without error may return indeterminate results.


4.36.3.3 Truncate operations
A truncate operation reduces the capacity of the media. The REMOVE ELEMENT AND TRUNCATE
command specifies the capacity to which the media is truncated, and should be no larger than the capacity at
the time the command begins processing minus the capacity associated with the storage element being
depopulated (see 5.8.2.2).
As a result of successful completion of a truncate operation, the device server shall:
a)
respond to successful READ CAPACITY commands (See 5.20 and 5.21) with parameter data
reporting the resulting capacity;
b)
respond to successful MODE SENSE commands (see SPC-6) with the mode parameter block
descriptor (see 6.5.2) reporting the resulting capacity; and
c)
establish a unit attention condition with the additional sense code set to CAPACITY DATA HAS
CHANGED as described in 4.10.
4.36.4 Storage element restoration
4.36.4.1 Overview
An application client may specify that a previously depopulated storage element be restored as described in
4.36.4. A device server that supports storage element restoration shall support:
a)
the REPORT SUPPORTED OPERATION CODES command (see SPC-6);
b)
the GET PHYSICAL ELEMENT STATUS command (see 5.8);
c)
the REMOVE ELEMENT AND TRUNCATE command (see 5.26); and
d)
the RESTORE ELEMENTS AND REBUILD command (see 5.29).
A RESTORE ELEMENTS AND REBUILD command specifies that the device server:
1)
shall perform a depopulation revocation operation (see 4.36.4.2);
2)
shall perform a rebuild operation (see 4.36.4.3); and
3)
may perform an initialization.
If an initialization is not performed, user data written before the depopulation revocation operation may be
readable in any accessible logical block.
The depopulation revocation operation, rebuild operation, and initialization operation, if any, may continue
after the successful completion of the RESTORE ELEMENTS AND REBUILD command.
The processing of a RESTORE ELEMENTS AND REBUILD command shall not change:
a)
the logical block length (see 4.5);
b)
the lowest aligned logical block address (see 4.6.1); or
c)
the protection type (see 4.21.2).
Upon successful completion of the RESTORE ELEMENTS AND REBUILD command; the depopulation
revocation operation, rebuild operation, and the initialization, if any, shall continue as background operations.
While those operations are in progress, the device server shall:
a)
provide pollable sense data (see SPC-6) with the sense key set to NOT READY, the additional sense
code set to DEPOPULATION RESTORATION IN PROGRESS and the PROGRESS INDICATION field in
the sense data set to indicate the progress of those operations; and
b)
process other commands as described in 4.36.5.
Upon the completion of the depopulation revocation operation, rebuild operation, and initialization, if any, the
contents of the user data area may have no relation to the contents of the user data area before the
processing of the RESTORE ELEMENTS AND REBUILD command.
Any depopulation revocation operation, rebuild operation, and initialization requested by a RESTORE
ELEMENTS AND REBUILD command shall resume after any interruption hard reset or logical unit reset. If
any depopulate operation, truncate operation, and initialization requested by a RESTORE ELEMENTS AND


REBUILD command is interrupted by a power cycle then that operation shall be terminated and the logical
unit may become format corrupt.
If a depopulation revocation operation, a rebuild operation, or an initialization initiated by the RESTORE
ELEMENTS AND REBUILD command does not complete successfully, then the logical unit may become
format corrupt.
If the logical unit is format corrupt as a result of a depopulation revocation operation, rebuild operation, or
initialization requested by a RESTORE ELEMENTS AND REBUILD command, then the device server shall
terminate any medium access command with CHECK CONDITION status, with the sense key set to MEDIUM
ERROR and the additional sense code set to DEPOPULATION RESTORATION FAILED.
4.36.4.2 Depopulation revocation operation
A depopulation revocation operation attempts to restore to operation every storage element that has the
RALWD bit (see 5.8.2.2) set to one.
A depopulation revocation operation is requested by a RESTORE ELEMENTS AND REBUILD command
(see 5.29).
Automatic reassignment of defects may occur during depopulation revocation operations. Following a
successful depopulation revocation operation and before a write operation to an LBA, a read command or
verify command that specifies that LBA that completes without error may return indeterminate logical block
data.
4.36.4.3 Rebuild operation
A rebuild operation assigns LBA mapping resources for the storage elements that are being restored.
As a result of successful completion of a rebuild operation, the device server shall:
a)
respond to successful READ CAPACITY commands (See 5.20 and 5.21) with parameter data
reporting the resulting capacity;
b)
respond to successful MODE SENSE commands (see SPC-6) with the mode parameter block
descriptor (see 6.5.2) reporting the resulting capacity; and
c)
establish a unit attention condition with the additional sense code set to CAPACITY DATA HAS
CHANGED as described in 4.10.
4.36.5 Command processing during storage element depopulation and restoration
After a device server has started processing the operations associated with a REMOVE ELEMENT AND
TRUNCATE command or a RESTORE ELEMENTS AND REBUILD command, and until the device server
completes those operations, the device server shall  terminate all commands other than:
a)
GET PHYSICAL ELEMENT STATUS commands (see 5.8);
b)
INQUIRY commands (see SPC-6);
c)
LOG SENSE commands that specify the Temperature log page (see SPC-6);
d)
MODE SENSE commands (see SPC-6) that specify:
A) the Informational Exceptions Control mode page (see 6.5.8);
B) the Caching mode page (see 6.5.6);
C) the Control mode page (see SPC-6);
D) the Protocol Specific Port mode page (see SPC-6); or
E) the Protocol Specific Logical Unit mode page (see SPC-6);
e)
READ CAPACITY (10) commands (see 5.20);
f)
READ CAPACITY (16) commands (see 5.21);
g)
REPORT LUNS commands (see SPC-6);
h)
REPORT SUPPORTED OPERATION CODES commands (see SPC-6);
i)
REPORT SUPPORTED TASK MANAGEMENT FUNCTIONS commands (see SPC-6);
j)
REPORT ZONES commands (see ZBC-2) with:
A) the ZONE START LBA field set to zero;


B) the REPORTING OPTIONS field set to 3Fh;
C) the PARTIAL bit set to one; and
D) the ALLOCATION LENGTH field set to a value less than or equal to 64;
and
k)
REQUEST SENSE commands (see SPC-6) (e.g., to retrieve pollable sense data),
with CHECK CONDITION status, with the sense key set to NOT READY, the additional sense code set to:
a)
DEPOPULATION IN PROGRESS, and the PROGRESS INDICATION field (see SPC-6) in the sense data
set to indicate the progress of the operations associated with the REMOVE ELEMENT AND
TRUNCATE command; or
b)
DEPOPULATION RESTORATION IN PROGRESS and the PROGRESS INDICATION field in the sense
data set to indicate the progress of the operations associated with the RESTORE ELEMENTS AND
REBUILD command.
