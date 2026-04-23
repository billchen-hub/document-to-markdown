# Logical block provisioning reporting examples

Annex E
(informative)
Logical block provisioning reporting examples
E.1 Overview
Logical block provisioning reporting may be implemented using different methods. Implementations may
include one or more of the following:
a)
use of dedicated LBA mapping resources (e.g., resources are associated with a specific logical unit);
b)
use of shared LBA mapping resources (e.g., resources are shared by multiple logical units);
c)
reporting based on dedicated LBA mapping resources (e.g., resources are reported specific to the
logical unit);
d)
reporting based on shared LBA mapping resources (e.g., resources are reported for the resource pool
as a whole);
e)
LBA mapping resource tracking based on logical blocks; and
f)
LBA mapping resource tracking based on threshold sets.
This annex describes examples of logical block provisioning reporting. Each example follows logical block
provisioning resource usage and reporting over time as a specified set of operations occur.
E.2 Interpreting log parameter counts
As a result of the variation of the threshold set size implementations, logical block usage and resource
reporting may not have a direct relationship. The second example (see clause E.4) demonstrates an
implementation where logical blocks are allocated on an individual LBA basis and reported using a larger
threshold set basis. The reporting is a direct calculation from a logical block based count to a threshold set
based count.
In implementations where a threshold set contains a set of contiguous logical blocks, the reporting may be
substantially different. LUN 1 in the first example (see clause E.3) demonstrates such an implementation. At
the initial conditions, two threshold sets are reported as being used. With a threshold set size of 1 024 blocks,
these two threshold sets may contain as little as one logical block of application client data in each threshold
set, or as many as 1 024 contiguous logical blocks in each threshold set. Which LBAs have been written by
the application client has a substantial impact on how the usage of those resources is reported.
The relationship of the physical blocks to the logical blocks (see figure 4 and figure 5) may have an impact on
the logical block provisioning log parameters. Which LBAs are written by the application may impact the
number of physical blocks required to be allocated and therefore impact the reporting of the LBA mapping
resource parameters.
The device server may not prioritize the maintenance of the values in the Logical Block Provisioning log page
(see 6.4.5) above the completion of other operations (e.g., read operations or write operations). This may
result in delays in updates to these values (e.g., after a request to unmap a large number of logical blocks).
The logical block provisioning log parameters may also appear inaccurate for logical units where unmap
operations cause LBA mapping resources to be released using a periodic background function.
Data de-duplication (see 4.8) and compression may impact the logical block provisioning log parameters. If
the device server is able to perform data de-duplication or compression, then the number of LBA mapping
resources:
a)
used for a successful write operation may not be the same as specified in the command that
requested that operation; or
b)
made available after one or more successful unmap operations may not be the same as specified in
the command that requested those operations.


EXAMPLE 1 - If a write command to LBAs that are all in the deallocated state (see 4.7.4.6) results in data that is all
de-duplicated, then there may be no additional LBA mapping resources used when those LBAs transition to the mapped
state (see 4.7.4.5). This may result in no change in the available LBA mapping resource count (see 6.4.5.2), or the used
LBA mapping resource count (see 6.4.5.3).
EXAMPLE 2 -If a write command to LBAs that are all in the mapped state results in data that is no longer de-duplicated,
then additional LBA mapping resources may be required even though all the LBAs addressed by the command remain in
the mapped state. This may result in a reduction in the available LBA mapping resource count, or an increase in the used
LBA mapping resource count. On a thin provisioned logical unit, such a write command may also be terminated as a result
of a resource exhaustion condition (see 4.7.3.6.1).
EXAMPLE 3 -If a write command to LBAs that are all in the mapped state results in data that is more compressible than
the previous data in those LBAs, then fewer LBA mapping resources may be required even though all the LBAs addressed
by that command remain in the mapped state. This may result in an increase in the available LBA mapping resource
count, or a decrease in the used LBA mapping resource count.
EXAMPLE 4 -If a write command to LBAs that are all in the mapped state results in data that is less compressible than the
previous data in those LBAs, then additional LBA mapping resources may be required even though all the LBAs
addressed by that command remain in the mapped state. This may result in a decrease in the available LBA mapping
resource count, or an increase in the used LBA mapping resource count. On a thin provisioned logical unit, such a write
command may also be terminated as a result of a resource exhaustion condition.
EXAMPLE 5 -If an unmap command addresses LBAs that are all in the mapped state and contain data that has been
de-duplicated (i.e., additional logical blocks still contain that same de-duplicated data), then on a thin provisioned logical
unit, there may be no change in the LBA mapping resources even though all of the LBAs addressed by that command
transition to the deallocated state. This may result in no change to the available LBA mapping resource count or the used
LBA mapping resource count.
As a result, application clients using logical block provisioning thresholds and examining logical block
provisioning log parameters should not expect application client determined usage values or application client
determined available space values to match log parameters or threshold events as reported by the logical
unit.


E.3 Dedicated resource, threshold set tracked example
E.3.1 Dedicated resource, threshold set tracked example overview
This example describes a method that reports dedicated logical block provisioning resources based on
threshold sets. In this example, the values reported by the logical unit in the Logical Block Provisioning log
page (see 6.4.5) reflect the usage for each logical unit and the available resources dedicated to each logical
unit. Each threshold set is allocated to contain a set of contiguous logical blocks (e.g., LBAs 1 024 to 2 047 are
contained in the same threshold set).
E.3.2 Dedicated resource, threshold set tracked example configuration
The configuration used for this example consists of two thin provisioned logical units, each with dedicated
logical block provisioning resources. Table E.1 shows logical block provisioning related capacity values used
in this example.
Table E.2 shows LUN 1 with four enabled threshold descriptors and LUN 2 with two enabled threshold
descriptors. The threshold descriptors in the Logical Block Provisioning mode page (see 6.5.9) for LUN 1 are
configured to report a logical block provisioning threshold crossing (see 4.7.3.7) when:
a)
the percentage of available LBA mapping resources reaches 30 % of reported capacity;
b)
the percentage of available LBA mapping resources reaches 20 % of reported capacity;
c)
the percentage of available LBA mapping resources reaches 10 % of reported capacity; or
d)
the percentage of used LBA mapping resources reaches 75 % of reported capacity.
Table E.1 — Dedicated resource, threshold set tracked example capacity information
LUN
Capacity
THRESHOLD EXPONENT field  c
Number of threshold sets  d
LBA  a
Logical
blocks  b
3FFF_FFFFh
1 Gi
0Ah (i.e., 512 KiB, 1 024 logical blocks)
0010_0000h (i.e., 1 Mi)
BFFF_FFFFh
3 Gi
0Ch (i.e., 2 MiB, 4 096 logical blocks)
000C_0000h (i.e., 768 Ki)
a RETURNED LOGICAL BLOCK ADDRESS field in READ CAPACITY parameter data (see 5.20.2 and 5.21.2).
b The value returned in the RETURNED LOGICAL BLOCK ADDRESS field plus one.
c In the Logical Block Provisioning VPD page (see 6.6.7).
d Number of threshold sets = capacity ÷ 2(threshold exponent).


The threshold descriptors in the Logical Block Provisioning mode page for LUN 2 are configured to report a
logical block provisioning threshold crossing when:
a)
the percentage of available LBA mapping resources reaches 50 % of reported capacity; or
b)
the percentage of available LBA mapping resources reaches 10 % of reported capacity.
E.3.3 Dedicated resource, threshold set tracked example sequence
The sequence of events for this example are:
1)
initial conditions (see E.3.4);
2)
operations that occur (see E.3.5); and
3)
final values in the logical block provisioning log page (see E.3.6).
Table E.2 — Dedicated resource, threshold set tracked example capacity information
LUN
Threshold
resource  a
Threshold
count  b
Description
0001h
0004_CCCCh
An available LBA mapping resource threshold set to 30 % of the
reported capacity (i.e., number of threshold sets from table F.1 ×
0.30 = 0004_CCCCh threshold sets)
0001h
0003_3333h
An available LBA mapping resource threshold set to 20 % of the
reported capacity
0001h
0001_9999h
An available LBA mapping resource threshold set to 10 % of
the reported capacity
0002h
000C_0000h
A used LBA mapping resource threshold set to 75 % of the reported
capacity (i.e., number of threshold sets from table F.1 (i.e.,
0010_0000h) × 0.75 = 000C_0000h threshold sets)
0001h
0006_0000h
An available LBA mapping resource threshold set to 50 % of the
reported capacity (i.e., number of threshold sets from table F.1 (i.e.,
000C_0000h) × 0.50 = 0006_0000h threshold sets)
0001h
0001_3333h
An available LBA mapping resource threshold set to 10 % of the
reported capacity
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b THRESHOLD COUNT field (see 6.5.9.2).


E.3.4 Dedicated resource, threshold set tracked example initial conditions
Initially, LUN 1 has two threshold sets used and has 69 108 736 logical blocks available (i.e. 0001_07A1h
threshold sets). The application client has written at least one logical block into each of the two logical block
ranges that correspond to those two threshold sets, therefore the application client may have written from two
logical blocks to 2 048 logical blocks. LUN 2 has 1 073 741 824 logical blocks available (i.e., 0004_0000h
threshold sets). LUN 2 does not report a used LBA mapping resource parameter. Table E.3 shows the values
in the Logical Block Provisioning log page for the initial conditions in this example.
E.3.5 Operations that occur
Write operations occur to LUN 1 that require one additional threshold set to be allocated when the application
client writes 50 additional contiguous logical blocks. Used LBA mapping resources on LUN 1 are now 3 072
logical blocks (i.e., three threshold sets), and available LBA mapping resources are 69 107 712 logical blocks.
Write operations also occur to LUN 2 that require no additional threshold sets when the application client
writes an additional 100 logical blocks into a threshold set that was already allocated.
Table E.3 — Dedicated resource, threshold set tracked example initial conditions
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description  d
0001h
0001_07A1h
01b
The available LBA mapping resource parameter
indicates that 69 108 736 logical blocks (i.e., 1_07A1h
threshold sets × 1 024 logical blocks per threshold set)
are available for LUN 1.
0002h
0000_0002h
01b
The used LBA mapping resource parameter indicates
that 2 048 logical blocks (i.e., 2h threshold sets × 1 024
logical blocks per threshold set) have been used (i.e.,
allocated) by LUN 1.
0001h
0004_0000h
01b
The available LBA mapping resource parameter
indicates that 1 073 741 824 logical blocks (i.e.,
4_0000h threshold sets × 4 096 logical blocks per
threshold set) are available for LUN 2.
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.4.5.2).
d LBA count = capacity × 2(threshold exponent).


E.3.6 Dedicated resource, threshold set tracked example final log page values
Table E.4 shows the values in the Logical Block Provisioning log page after the operations described in E.3.5
have occurred.
E.4 Shared resource, logical block tracked example
E.4.1 Shared resource, logical block tracked example overview
This example describes a method that tracks shared logical block provisioning resources based on logical
blocks. The logical block provisioning resources are shared by multiple logical units. In this example, the
values reported by each logical unit in its Logical Block Provisioning log page (see 6.4.5) reflect the combined
usage of all logical units that share the logical block provisioning resources and the resources available for
use by any of the logical units that share the logical block provisioning resources. Resources are allocated
one logical block at a time but reported with a larger threshold set size.
Table E.4 — Dedicated resource, threshold set tracked example final log page values
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description  d
0001h
0001_07A0h
01b
The available LBA mapping resource parameter
indicates that 69 107 712 logical blocks (i.e., 1_07A0h
threshold sets × 1 024 logical blocks per threshold set)
are available for LUN 1.
0002h
0000_0003h
01b
The used LBA mapping resource parameter indicates
that 3 072 logical blocks (i.e., 3h threshold sets × 1 024
logical blocks per threshold set) have been used (i.e.,
allocated) by LUN 1.
0001h
0004_0000h
01b
The available LBA mapping resource parameter
indicates that 1 073 741 824 (i.e., 4_0000h threshold
sets × 4 096 logical blocks per threshold set) are
available for LUN 2.
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.4.5.2).
d LBA count = capacity × 2(threshold exponent).


E.4.2 Shared resource, logical block tracked example configuration
The configuration used for this example consists of two thin provisioned logical units, where the logical block
provisioning resources are shared between both logical units. Table E.5 shows logical block provisioning
related capacity values used in this example.
E.4.3 Shared resource, logical block tracked example time line
The sequence of events for this example are:
1)
initial conditions (see E.4.4);
2)
operations that occur (see E.4.5); and
3)
final values in the logical block provisioning log page (see E.4.6).
Table E.5 — Shared resource, logical block tracked example capacity information
LUN
Capacity
THRESHOLD EXPONENT field  c
Number of threshold sets  d
LBA  a
Logical
blocks  b
3FFF_FFFFh
1 Gi
0Bh (i.e., 1 MiB, 2 048 logical blocks)
0008_0000h (i.e., 512 Ki)
BFFF_FFFFh
3 Gi
0Bh (i.e., 1 MiB, 2 048 logical blocks)
0018_0000h (i.e., 1 536 Ki)
a RETURNED LOGICAL BLOCK ADDRESS field in READ CAPACITY parameter data (see 5.20.2 and 5.21.2).
b The value returned in the RETURNED LOGICAL BLOCK ADDRESS field plus one.
c In the Logical Block Provisioning VPD page (see 6.6.7).
d Number of threshold sets = capacity ÷ 2(threshold exponent).


E.4.4 Shared resource, logical block tracked example initial conditions
Initially, LUN 1 and LUN 2 have used a combined total of 57 000 logical blocks. LUN1 and LUN 2 have
1 073 741 900 logical blocks available for use by either LUN 1 or LUN 2. Table E.6 shows the values in the
Logical Block Provisioning log page for the initial conditions in this example.
E.4.5 Operations that occur
Write operations occur to LUN 1 that require 2 000 additional logical blocks to be used and write operations
occur to LUN 2 that require 3 000 additional logical blocks to be used. Used LBA mapping resources on LUN
1 and LUN 2 are now 62 000 logical blocks, and the combined LBA mapping resources available to both LUN
1 and LUN 2 are 1 073 736 900 logical blocks (i.e., 1 073 741 900 minus 5 000).
Table E.6 — Shared resource, logical block tracked example initial conditions
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description
0001h
0008_0000h
10b
The available LBA mapping resource parameter
indicates that from 1 073 741 824 logical blocks (i.e.
8_0000h threshold sets × 2 048 logical block per
threshold set) to 1 073 743 871 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_001Ch
10b
The used LBA mapping resource parameter indicates
that from 55 297 logical blocks to 57 344 logical blocks
(i.e., 1Ch threshold sets × 2 048 logical blocks per
threshold set) have been used (i.e., allocated) by
LUN 1 and LUN 2.  e
0001h
0008_0000h
10b
The available LBA mapping resource parameter
indicates that 1 073 741 824 logical blocks (i.e.,
8_0000h threshold sets × 2 048 logical blocks per
threshold set) are available for LUN 1 or LUN 2.  d
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.4.5.2).
d Minimum available LBA count = resource count × 2(threshold exponent).
e Maximum used LBA count = resource count × 2(threshold exponent).


E.4.6 Shared resource, logical block tracked example final log page values
Table E.7 shows the values in the Logical Block Provisioning log page after the operations described in E.4.5
have occurred.
Table E.7 — Shared resource, logical block tracked example final log page values
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description
0001h
0007_FFFDh
10b
The available LBA mapping resource parameter
indicates that from 1 073 735 680 logical blocks (i.e.
7_FFFDh threshold sets × 2 048 logical blocks per
threshold set) to 1 073 737 727 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_001Fh
10b
The used LBA mapping resource parameter indicates
that from 61 441 logical blocks to 63 488 logical blocks
(i.e., 1Fh threshold sets × 2 048 logical blocks per
threshold set) have been used (i.e., allocated) by LUN
1 and LUN 2.  e
0001h
0007_FFFDh
10b
The available LBA mapping resource parameter
indicates that from 1 073 735 680 logical blocks (i.e.
7_FFFDh threshold sets × 2 048 logical blocks per
threshold set) to 1 073 737 727 logical blocks are
available for LUN 1 or LUN 2.  d
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.4.5.2).
d Minimum available LBA count = resource count × 2(threshold exponent).
e Maximum used LBA count = resource count × 2(threshold exponent).


E.5 Shared available, dedicated used, logical block tracked example
E.5.1 Shared available, dedicated used, logical block tracked example overview
This example describes a method that tracks available shared logical block provisioning resources based on
logical blocks and dedicated used logical block provisioning resources based on logical blocks. The available
logical block provisioning resources are shared by multiple logical units. In this example, the values reported
by the logical unit in the available LBA mapping resource parameter of the Logical Block Provisioning log page
(see 6.4.5) reflect the resources available for use by any of the logical units that share the logical block
provisioning resources. The values reported by the logical unit in the used LBA mapping resource parameter
of the Logical Block Provisioning log page reflect the usage for the individual logical unit.
E.5.2 Shared available, dedicated used, logical block tracked example configuration
The configuration used for this example consists of two thin provisioned logical units, where the available
logical block provisioning resources are shared between both logical units and used logical block provisioning
resources are reported independently for each logical unit. Table E.8 shows logical block provisioning related
capacity values used in this example.
E.5.3 Shared available, dedicated used, logical block tracked example time line
The sequence of events for this example are:
1)
initial conditions (see E.5.4);
2)
operations that occur (see E.5.5); and
3)
final values in the logical block provisioning log page (see E.5.6).
Table E.8 — Shared available, dedicated used example capacity information
LUN
Capacity
THRESHOLD EXPONENT field  c
Number of threshold sets  d
LBA  a
Logical
blocks  b
3FFF_FFFFh
1 Gi
0Bh (i.e., 1 MiB, 2 048 logical blocks)
0008_0000h (i.e., 512 Ki)
BFFF_FFFFh
3 Gi
0Bh (i.e., 1 MiB, 2 048 logical blocks)
0018_0000h (i.e., 1 536 Ki)
a RETURNED LOGICAL BLOCK ADDRESS field in READ CAPACITY parameter data (see 5.20.2 and 5.21.2).
b The value returned in the RETURNED LOGICAL BLOCK ADDRESS field plus one.
c In the Logical Block Provisioning VPD page (see 6.6.7).
d Number of threshold sets = capacity ÷ 2(threshold exponent).


E.5.4 Shared available, dedicated used, logical block tracked example initial conditions
Initially, LUN 1 has used 57 000 logical blocks and, LUN 2 has used 103 000 logical blocks. LUN 1 and LUN 2
have 1 073 741 900 logical blocks available for use by either LUN 1 or LUN 2. Table E.9 shows the values in
the Logical Block Provisioning log page for the initial conditions in this example.
E.5.5 Operations that occur
Write operations occur to LUN 1 that require 2 000 additional logical blocks to be used and write operations
occur to LUN 2 that require 3 000 additional logical blocks to be used. Used LBA mapping resources on LUN
1 are now 59 000 logical blocks, used LBA mapping resources on LUN 2 are now 106 000 logical blocks, and
the combined LBA mapping resources available to both LUN 1 and LUN 2 are 1 073 736 900 logical blocks.
Table E.9 — Shared resource, logical block tracked example initial conditions
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description
0001h
0008_0000h
10b
The available LBA mapping resource parameter
indicates that from 1 073 741 824 logical blocks (i.e.
8_0000h threshold sets × 2 048 logical blocks per
threshold set) to 1 073 743 871 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_001Ch
01b
The used LBA mapping resource parameter indicates
that from 55 297 logical blocks to 57 344 logical blocks
(i.e., 1Ch threshold sets × 2 048 logical blocks per
threshold set) have been used (i.e., allocated) by
LUN 1.  e
0001h
0008_0000h
10b
The available LBA mapping resource parameter
indicates that from 1 073 741 824 logical blocks (i.e.,
8_0000h threshold sets × 2 048 logical blocks per
threshold set) to 1 073 743 871 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_0033h
01b
The used LBA mapping resource parameter indicates
that from 102 401 logical blocks to 104 448 (i.e., 33h
threshold sets × 2 048 logical blocks per threshold set)
have been used (i.e., allocated) by LUN 2.  e
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.5.9.2).
d Minimum available LBA count = resource count × 2(threshold exponent).
e Maximum used LBA count = resource count × 2(threshold exponent).


E.5.6 Shared available, dedicated used, example final log page values
Table E.10 shows the values in the Logical Block Provisioning log page after the operations described in E.5.5
have occurred.
Table E.10 — Shared available, dedicated used example final log page values
LUN
Log page
parameter  a
Resource
count  b
Scope  c
Description
0001h
0007_FFFDh
10b
The available LBA mapping resource parameter
indicates that from 1 073 735 680 logical blocks (i.e.
7_FFFDh threshold sets × 2 048 logical blocks per
threshold set) to 1 073 737 727 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_001Dh
01b
The used LBA mapping resource parameter indicates
that from 57 345 logical blocks to 59 392 logical blocks
(i.e., 1Dh threshold sets × 2 048 logical blocks per
threshold set) have been used (i.e., allocated) by
LUN 1.  e
0001h
0007_FFFDh
10b
The available LBA mapping resource parameter
indicates that from 1 073 735 680 logical blocks (i.e.
7_FFFDh threshold sets × 2 048 logical blocks per
threshold set) to 1 073 737 727 logical blocks are
available for LUN 1 or LUN 2.  d
0002h
0000_0034h
01b
The used LBA mapping resource parameter indicates
that from 104 449 logical blocks to 106 496 logical
blocks (i.e., 34h threshold sets × 2_048 logical blocks
per threshold set) have been used (i.e., allocated) by
LUN 2.  e
a THRESHOLD RESOURCE field (see 6.5.9.2) and the PARAMETER CODE field (see 6.4.5.2).
b RESOURCE COUNT field (see 6.5.9.2).
c
SCOPE field (see 6.4.5.2).
d Minimum available LBA count = resource count × 2(threshold exponent).
e Maximum used LBA count = resource count × 2(threshold exponent).


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
