# 4.26 Referrals

4.25 Model for uninterrupted sequences on LBA ranges
Direct access block devices may perform commands that require an uninterrupted sequence of actions to be
performed on a specified range of LBAs. The uninterrupted sequence requirements are described in table 28.
The uninterrupted sequences do not impact the processing of commands that access logical blocks other than
those specified in the command requiring an uninterrupted sequence. The task attribute (see SAM-6) controls
interactions between multiple commands. Commands with uninterrupted sequences on LBA ranges are
shown in table 28.
4.26 Referrals
4.26.1 Referrals overview
Referrals allow a logical unit to inform an application client that one or more user data segments (i.e., ranges
of logical blocks) are accessible through target port group(s).
Support for referrals is indicated by the device server setting the R_SUP bit to one in the Extended INQUIRY
Data VPD page (see SPC-6).
An application client may determine information on referrals by:
a)
issuing commands; or
b)
monitoring sense data returned as part of a completed command or a terminated command.
Figure 12 shows an example of how a logical unit informs an application client that one or more user data
segments are accessible through target port groups.
Table 28 — Commands that require uninterrupted sequences
Command
Consistency enforcement
Reference
ORWRITE (16)
ORWRITE (32)
The device server shall not perform any operations requested
by any other command in the task set on logical blocks in the
range specified by the command that requires an
uninterrupted sequence of actions while performing the
specified uninterrupted sequence of actions.
4.27
COMPARE AND WRITE
The device server shall not perform:
a)
any operations requested by any COMPARE AND
WRITE command in the task set on logical blocks in the
range specified by the command that requires an
uninterrupted sequence of actions while performing the
specified uninterrupted sequence of actions;
b)
any write operations to or unmap operations on logical
blocks in the range specified by the command that
requires an uninterrupted sequence of actions while
performing the read operations specified in the
uninterrupted sequence of actions; and
c)
any read operations or verify operations from logical
blocks in the range specified by the command that
requires an uninterrupted sequence of actions while
performing the write operations specified in the
uninterrupted sequence of actions.
5.3


Figure 12 — Referrals
4.26.2 Discovering referrals
An application client may determine referrals information on a logical unit by:
1)
determining if the R_SUP bit is set to one (i.e., the logical unit supports referrals) in the Extended
INQUIRY Data VPD page (see SPC-6);
2)
requesting the user data segment information from the Referrals VPD page (see 6.6.8);
3)
requesting a list of target port groups by issuing a REPORT TARGET PORT GROUPS command (see
SPC-6); and
4)
either:
A) requesting referrals information by issuing a REPORT REFERRALS command (see 5.28); or
B) monitoring for referral information in sense data returned by the device server (see 4.26.3).
The following calculation is used to determine the first LBA for each user data segment within the range of
LBAs indicated by the user data segment referral descriptors (see table 18) returned in:
a)
the REPORT REFERRALS parameter data (see table 107); or
b)
the user data segment referrals sense data descriptor (see 4.18.4):
first LBA of the current user data segment = first LBA + (segment size × segment multiplier)
where:
first LBA
the initial value is the first user data segment LBA specified in the user data
segment referral descriptor (see table 18). Subsequent values, if any, are the
first LBA of the previous user data segment;
segment size
the content of the USER DATA SEGMENT SIZE field (see 6.6.8); and
segment multiplier
the content of the USER DATA SEGMENT MULTIPLIER field (see 6.6.8).
SCSI device
SCSI target device
Target port group
SCSI target port
Logical unit
User data segment
SCSI target port
Target port group
SCSI target port
SCSI target port
User data segment
Active/optimized target port asymmetric access (see SPC-4) to user data segment
Active/non-optimized target port asymmetric access (see SPC-4) to user data segment


If the content of the USER DATA SEGMENT SIZE field is greater than zero, and the content of the USER DATA
SEGMENT MULTIPLIER field is greater than zero, then the following calculation may be used to determine the last
LBA for each user data segment within the range of LBAs indicated by the user data segment referral
descriptors (see table 18) returned in:
a)
the REPORT REFERRALS parameter data (see table 107); or
b)
the user data segment referrals sense data descriptor (see 4.18.4):
last LBA of the current user data segment = first LBA + (segment size – 1)
where:
first LBA
the first LBA of the current user data segment;
segment size
the content of the USER DATA SEGMENT SIZE field (see 6.6.8).
If the content of the USER DATA SEGMENT SIZE field is zero, then there is only one user data segment, and the
last LBA of that user data segment is equal to the last LBA specified in the last USER DATA SEGMENT LBA field
(see table 18).
See annex F for examples for discovering referrals.
4.26.3 Referrals in sense data
Returning referral information in sense data is enabled if the:
a)
R_SUP bit in the Extended INQUIRY Data VPD page is set to one (i.e., the logical unit supports
referrals) (see SPC-6); and
b)
D_SENSE bit in the Control mode page is set to one (i.e., returning descriptor formatted sense data is
enabled) (see SPC-6).
If reporting of referrals in sense data is enabled, a command completes without error, no other sense data is
available within the logical unit, and the device server has an alternate I_T_L nexus that an application client
should use to access at least one of the specified logical blocks, then the device server shall complete the
command with GOOD status with the sense key set to COMPLETED, the additional sense code set to
INSPECT REFERRALS SENSE DESCRIPTORS, and a user data segment referrals sense data descriptor
(see 4.18.4).
The user data segment referral sense data descriptor (see 4.18.4) shall define the description of as many
complete user data segments (i.e., one user data segment referral descriptor contains one complete user data
segment) that fit in the maximum number of bytes allowed for sense data (i.e., 244 bytes or the maximum
supported sense data length indicated in the Extended INQUIRY Data VPD page (see SPC-6)). If all the user
data segments do not fit within the maximum number of bytes allowed for sense data, then:
a)
the device server shall set the NOT_ALL_R bit to one in the user data segment referral sense data
descriptor (see 4.18.4); and
b)
the selection of which user data segments to include in the user data segment referral sense data
descriptor is vendor specific.
Each user data segment referral sense data descriptor (see 4.18.4) contains information on alternate I_T_L
nexuses to user data segments that the application client should use to access LBAs within the LBA range(s)
indicated by the user data segments.
If reporting of referrals in sense data is enabled, the device server receives a command for which the device
server is not able to access user data associated with the requested command, and the inaccessible user
data is accessible through another target port group, then the device server shall terminate the command with
CHECK CONDITION status with the sense key set to ABORTED COMMAND, the additional sense code set
to INSPECT REFERRALS SENSE DESCRIPTORS, and a user data segment referral sense data descriptor.
The user data segment referral sense data descriptor shall, at a minimum, indicate the user data segment that
contains the LBA of the first inaccessible logical block. Any other type of error that occurs while processing the
command shall take precedence and be reported as described in this standard. If any other type of error
occurs while the device server is processing the command, then processing that error shall take precedence
over processing the command, and the device server shall report the error as described in this standard.
