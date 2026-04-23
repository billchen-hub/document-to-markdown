# Discovering referrals examples

Annex F
(informative)
Discovering referrals examples
F.1 Referrals example with no user data segment multiplier
This annex demonstrates a method an application client may use to determine the optimal target port group
from which to access logical blocks using information sent from the device server when the user data segment
multiplier is set to zero.
Figure F.1 shows an example of a SCSI device in which referrals have been implemented with a user data
segment multiplier of zero.
Figure F.1 — Referrals example with no user data segment multiplier
SCSI device
SCSI target device
Target port group (1)
SCSI target port
(1)
Logical unit
SCSI target port
(2)
Target port group (2)
SCSI target port
(4)
SCSI target port
(3)
Active/optimized target port asymmetric access (see SPC-6) to user data segment
Active/non-optimized target port asymmetric access (see SPC-6) to user data segment
User data segment
LBA: 0 to 1 999
User data segment
LBA: 2 000 to 2 999
User data segment
LBA: 3 000 to 5 999


In the example shown in figure F.1, the application client acquires the information from the logical unit as
shown in table F.1.
The application may determine the user data segments that are optimally accessed through the two target
port groups as shown in table F.2.
Table F.1 — Referrals application client information with no user data segment multiplier
Referrals VPD page
User data segment size
User data segment multiplier
ignored
REPORT TARGET PORT GROUPS command
Asymmetric access state
Target port
group
Relative target port identifier
4h (i.e., logical block
dependent)
REPORT REFERRALS command or user data segment referral sense data descriptors
First user data segment
LBA
Last user data
segment LBA
Asymmetric access state
Target port group
1 999
0 (i.e., active/optimized)
1 (i.e., active/non-optimized)
2 000
2 999
0 (i.e., active/optimized)
1 (i.e., active/non-optimized)
3 000
5 999
0 (i.e., active/optimized)
1 (i.e., active/non-optimized)
Table F.2 — User data segment calculations with no user data segment multiplier
First LBA of user
data segment
Calculation
(see 4.26.2)
Last LBA of user
data segment
Calculation
(see 4.26.2)
Target port group 1 user data segments in active/optimized asymmetric access state
0  a
1 999
1 999  b
3 000
3 000  a
5 999
5 999  b
Target port group 2 user data segments in active/optimized asymmetric access state
2 000
2 000  a
2 999
2 999  b
a The first user data segment LBA
b The last user data segment LBA


F.2 Referrals example with non-zero user data segment multiplier
This subclause demonstrates a method that an application client may use to determine the optimal target port
group from which to access logical blocks using information sent from the device server when the user data
segment multiplier is set to a non-zero value.
Figure F.2 shows an example of a SCSI device in which referrals have been implemented with a user data
segment multiplier of two and a user data segment size of 1 000.
Figure F.2 — Referrals example with non-zero user data segment multiplier
SCSI device
SCSI target device
Target port group (1)
SCSI target port  (1)
Logical unit
Target port group (3)
SCSI target port  (4)
Active/optimized target port asymmetric access (see SPC-6) to user data segment
Active/non-optimized target port asymmetric access (see SPC-6) to user data segment
User Data Segment
LBA: 0 to 999
User Data Segment
LBA: 2 000 to 2 999
User data segment
LBA: 4 000 to 4 999
User Data Segment
LBA: 1 000 to 1 999
User Data Segment
LBA: 3 000 to 3 999
User data segment
LBA: 5 000 to 5 999
Target port group (2)
SCSI target port  (2)
SCSI target port  (3)


In the example shown in figure F.2, the application client acquires the information from the logical unit as
shown in table F.3.
The application may determine the user data segments that are optimally accessed through the two target
port groups as shown in table F.4.
Table F.3 — Referrals application client information with non-zero user data segment multiplier
Referrals VPD page
User data segment size
User data segment multiplier
1 000
REPORT TARGET PORT GROUPS command
Asymmetric access state
Target port
group
Relative target port identifier
4h (i.e., logical block
dependent)
REPORT REFERRALS command or user data segment referral sense data descriptors
First user data segment
LBA
Last user data
segment LBA
Asymmetric access state
Target port group
4 999
0 (i.e., active/optimized)
1 (i.e., active/non-optimized)
1 (i.e., active/non-optimized)
1 000
5 999
0 (i.e., active/optimized)
1 (i.e., active/non-optimized)
1 (i.e., active/non-optimized)
Table F.4 — User data segment calculations with non-zero user data segment multiplier
First LBA of user
data segment
Calculation
(see 4.26.2)
Last LBA of user
data segment
Calculation
(see 4.26.2)
Target port group 2 user data segments in active/optimized asymmetric access state
0  a
0  a + (1 000 – 1)
2 000
0 + (1 000 × 2)
2 999
2 000 + (1 000 – 1)
4 000
2 000 + (1 000 × 2)
4 999
4 000 + (1 000 – 1)
Target port group 3 user data segments in active/optimized asymmetric access state
1 000
1 000  a
1 999
1 000  a + (1 000 – 1)
3 000
1 000 + (1 000 × 2)
3 999
3 000 + (1 000 – 1)
5 000
3 000 + (1 000 × 2)
5 999
5 000 + (1 000 – 1)
a The first user data segment LBA.


Annex G
(informative)
IO advice hints usage
G.1 Overview
This annex describes how application clients and device servers may use IO advice hints and their associated
logical block markup descriptors to provide information to a storage device to enhance access to data.
G.2 IO Advice Hints Grouping mode page
The IO Advice Hints Grouping mode page (see 6.5.7) contains the definitions of the IO advice hints (see
4.22.2) that are associated with each group number.
A device server may implement pre-defined IO advice hints that are not changeable and indicate this by
making one or more IO advice hints group descriptors in the mode page not changeable.
The application client may use the MODE SENSE command to retrieve IO advice hints group descriptors to
determine the IO advice hints that are available, and determine which IO advice hints are associated with
each group number.
If any IO advice hints group descriptors in the mode page are changeable, the application client may use a
MODE SELECT command to associate IO group numbers with IO advice hints that meet the application client
needs.
A device server may implement any combination of changeable IO advice hints group descriptors or
predefined IO advice hints group descriptors.
G.3 Issuing I/O commands with IO advice hints
G.3.1 Group numbers and I/O commands
An application client:
1)
determines the IO advice hints group descriptor appropriate for each particular type of command
using the process described in clause G.2;
2)
determines the value to specify in the GROUP NUMBER field of each command as described in
4.22.2; and
places that value into the GROUP NUMBER field of the CDB.If cache segmentation (see 4.15.2) is enabled (see
6.5.7), then the use of different group numbers by components within the application client (e.g., file system,
virtual memory swapping/paging, payroll application) allows the device server to associate an IO command
and the associated cached data with other IO commands and other cached data from that same component.
G.3.2 Possible constraints on IO advice hints
There is no method to report how an IO advice hints has been processed by the device server. The
implications of this model include the ability of the device server to ignore any, or even all, IO advice hints it
receives.
A device server may constrain the complexity of its IO advice hints implementation by ignoring one or more of
the values in the logical block markup descriptor (see 6.8) (e.g., to ignore the READ SEQUENTIALITY field, and
the READ/WRITE FREQUENCY field).
