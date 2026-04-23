# 4.33 Format operations

4)
waits for responses to all WRITE STREAM commands for the stream associated with the stream
identifier; and
5)
sends a STREAM CONTROL command with the STR_CTL field set to 10b (i.e., close) and the STR_ID
field set to the associated stream identifier.
If the device server processes a WRITE STREAM command with the STR_ID field set to a stream identifier of
a stream that is not open, then the device server shall terminate the WRITE STREAM command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
STREAM NOT OPEN.
If the device server processes a STREAM CONTROL command with the STR_CTL field set to 10b (i.e., close)
and the STR_ID field set to the stream identifier of a stream that is not open, then the device server shall
terminate the STREAM CONTROL command with CHECK CONDITION status with the sense key set to
ILLEGAL REQUEST and the additional sense code set to STREAM NOT OPEN.
If the device server processes a STREAM CONTROL command with the STR_CTL field set to 01b (i.e., open)
and the maximum number of streams as defined by the MAXIMUM NUMBER OF STREAMS field (see 6.6.5) are
already open, then the device server shall terminate the STREAM CONTROL command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
MAXIMUM NUMBER OF STREAMS OPEN.
The application client may discover the state of open streams using the GET STREAM STATUS command
(see 5.9).
Resources (e.g., stream identifier) allocated to maintaining a specific stream are released if:
a)
the device server processes a STREAM CONTROL command (see 5.32) with the stream identifier of
the specified stream and the STR_CTL field set to 10b (i.e., close);
b)
a hard reset occurs;
c)
a logical unit reset occurs;
d)
a power on occurs;
e)
a FORMAT UNIT command is processed;
f)
a FORMAT WITH PRESETS command is processed; or
g)
a sanitize operation is processed.
If physical blocks that are part of a stream block do not contain logical block data when the associated stream
is closed, then logical block data should not be written to those physical blocks until all LBAs in that stream
block are unmapped.
4.33 Format operations
4.33.1 Format operations overview
A format operation results in the device server:
a)
configuring the logical block length and number of logical blocks of the logical unit as specified by the
block descriptor (see 6.5.2); and
b)
performing the following as specified by:
A) a FORMAT UNIT command (see 5.4):
a)
configure protection information;
b)
perform defect management;
c)
initialize LBAs; and
d)
vendor specific medium certification;
or
B) a FORMAT WITH PRESET command (see 5.5):
a)
change LBA configuration for a new device type;
b)
update peripheral device type;
c)
update VPD pages;
d)
perform medium defect management; and


e)
initialize LBAs as described in 4.33.3.
The degree that the medium is altered by a format operation is vendor specific. A format operation is
requested by a FORMAT UNIT command.
4.33.2 Performing a format operation
Before performing a format operation, the device server shall stop all:
a)
enabled power condition timers (see SPC-6);
b)
timers for enabled background scan operations (see 4.23); and
c)
timers or counters enabled for device-specific background functions.
As the result of completing a format operation, the device server shall reinitialize and restart all enabled timers
and counters for power conditions and background functions.
While performing a format operation, the device server shall:
a)
process commands already in a task set when a FORMAT UNIT command or a FORMAT WITH
PRESET command is received in a vendor specific manner;
b)
process an INQUIRY command by returning parameter data based on the condition of the logical unit
before beginning the FORMAT UNIT command or the FORMAT WITH PRESET command (i.e.,
INQUIRY data does not change until successful completion of a format operation):
c)
process a REQUEST SENSE command by returning parameter data containing sense data with the
sense key set to NOT READY, the additional sense code set to LOGICAL UNIT NOT READY,
FORMAT IN PROGRESS, and the PROGRESS INDICATION field in the sense data (see SPC-6) set to
indicate the progress of the format operation;
d)
process REPORT LUNS commands;
e)
terminate all commands, except INQUIRY commands, REPORT LUNS commands, and REQUEST
SENSE commands, with CHECK CONDITION status with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT NOT READY, FORMAT IN PROGRESS;
f)
remove all Background Scan Results log parameters (see 6.4.2.3) from the Background Scan Results
log page, if supported; and
g)
remove all Pending Defect log parameters (see 6.4.8.3) from the Pending Defects log page, if
supported.
For a FORMAT UNIT command, the application client may specify:
a)
that the device server clear the existing GLIST;
b)
a list of address descriptors that the device server adds to the GLIST;
c)
that the device server enable a certification operation that adds address descriptors for physical
blocks with medium defects discovered during the certification operation to the GLIST; and
d)
the behavior of the device server if it is not able to:
A) access the PLIST or GLIST; or
B) determine whether the PLIST or GLIST exists.
For a FORMAT WITH PRESET command, the device server manages all defect information. No information is
specified by the application client (e.g., GLIST and PLIST).
4.33.3 Completing a format operation
4.33.3.1 Completing a format operation overview
If a format operation completes without error, then:
a)
stream resources, if any, shall be released;
b)
if the logical unit is a zoned block device, then all LBAs in the logical unit are as defined in ZBC-2;
c)
if the logical unit is fully provisioned (i.e., the LBPME bit (see 5.21.2) is set to zero), then all LBAs in the
logical unit are mapped (see 4.7.2); or
d)
if the logical unit supports logical block provisioning management (i.e., the LBPME bit is set to one),
then if the LBPRZ field (see 6.6.7) is set to:


A) 000b, then each LBA in the logical unit shall be either:
a)
mapped, if an initialization pattern was specified that does not match the vendor-specific data
returned by a read command for an unmapped LBA (see 4.7.4.4); or
b)
unmapped, if no initialization pattern was specified or an initialization pattern was specified
that matches the vendor-specific data returned by a read command for an unmapped LBA
(see 4.7.4.4);
B) xx1b, then each LBA in the logical unit:
a)
shall be mapped, if the format operation did not initialize the user data to all zeroes for the
logical block referenced by that LBA;
b)
shall be unmapped, if the format operation initialized the user data to all zeroes for the logical
blocks referenced by all valid LBAs in the logical unit; or
c)
may be unmapped, if the format operation initialized the user data to all zeroes for the logical
block referenced by that LBA, and the format operation did not initialize the user data to all
zeroes for the logical blocks referenced by all valid LBAs in the logical unit;
and
C) 010b, then each LBA in the logical unit:
a)
shall be mapped, if an initialization pattern was specified that does not match the provisioning
initialization pattern; or
b)
shall be unmapped, if no initialization pattern was specified or an initialization pattern was
specified that matches the provisioning initialization pattern;
and
e)
if the format operation was performed for a FORMAT WITH PRESET command, then until Power On
condition (see SAM-6) is detected, the device server shall:
A) terminate all commands except REQUEST SENSE with CHECK CONDITION status, with the
sense key set to NOT READY and the additional sense code set to LOGICAL UNIT NOT READY,
POWER CYCLE REQUIRED; and
B) for the REQUEST SENSE command, return sense data with the sense key set to NOT READY
and the additional sense code set to LOGICAL UNIT NOT READY, POWER CYCLE REQUIRED.
If a format operation is aborted (e.g., by a power on condition or a hard reset condition (see SAM-6)) or
completes with an error, then the logical unit may become format corrupt. Format corrupt may be cleared by a
format operation that completes without error. If the logical unit is format corrupt, then the device server shall
terminate any:
a)
logical block access command other than commands that may correct the format corrupt condition
(e.g., FORMAT UNIT command); and
b)
any STREAM CONTROL command with the STR_CTRL field set to 01b (i.e., open stream),
with CHECK CONDITION status, with the sense key set to MEDIUM ERROR and the additional sense code
set to MEDIUM FORMAT CORRUPTED.
4.33.3.2 Completing read commands after a successful format operation
4.33.3.2.1 Completing read commands overview
Following a successful format operation and before a write operation to an LBA, a read command or verify
command that specifies that LBA shall be processed by the device server as described in:
a)
4.33.3.2.2, 4.33.3.2.3, and 4.33.3.2.4 for a mapped LBA; and
b)
4.7.4.4 for an unmapped LBA.
4.33.3.2.2 With FFMT field set to 00b
If the FFMT field (see table 40) was set to 00b in the most recent successful FORMAT UNIT command, then
subsequent read commands or verify commands that complete without error are processed using:
a)
the user data set as specified by:
A) the initialization pattern, if any;
B) the provisioning initialization pattern, if applicable; or


C) the manufacturer’s default initialization pattern;
and
b)
the protection information, if any, set to FFFF_FFFF_FFFF_FFFFh.
4.33.3.2.3 With FFMT field set to 01b
If the FFMT field (see table 40) was set to 01b in the most recent successful FORMAT UNIT command, then
subsequent read commands or verify commands:
a)
with unrecovered medium errors are processed as described in 4.18.1;
b)
with pseudo unrecovered errors are processed as described in 4.18.2;
c)
should be processed using unspecified logical block data and complete without error, if protection
information is disabled; or
d)
if protection information is enabled, then:
A) may be processed using unspecified logical block data and complete without error; or
B) may terminate with CHECK CONDITION status with sense data that indicates that the protection
information check fails as defined in 5.16 or 5.36.
4.33.3.2.4 With FFMT field set to 10b
If the FFMT field (see table 40) was set to 10b in the most recent successful FORMAT UNIT command, then
the device server may:
a)
return unspecified logical block data and complete subsequent read commands  without error;
b)
complete subsequent verify commands without error; or
c)
terminate subsequent read commands or verify commands with CHECK CONDITION status with the
sense key set to HARDWARE ERROR, MEDIUM ERROR, or ABORTED COMMAND.
