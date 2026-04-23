# Optimizing block access characteristics

Annex D
(informative)
Optimizing block access characteristics
D.1 Overview
This annex describes example methods that application clients may use to achieve optimal performance for
logical block access. These examples use the following information:
a)
the LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2);
b)
the LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field (see 5.21.2);
c)
the OPTIMAL TRANSFER LENGTH GRANULARITY field(see 6.6.4);
d)
the OPTIMAL TRANSFER LENGTH field (see 6.6.4);
e)
the MAXIMUM TRANSFER LENGTH field (see 6.6.4);
f)
the OPTIMAL STREAM WRITE SIZE field (see 6.6.5); and
g)
the STREAM GRANULARITY SIZE field (see 6.6.5).
D.2 Starting logical block offset
The READ CAPACITY (16) command transfers parameter data which includes a value in the LOWEST ALIGNED
LOGICAL BLOCK ADDRESS field. As shown in figure 4, the value in this field indicates the starting alignment of
logical block addresses where optimal performance for logical block access begins.
D.3 Optimal granularity sizes
The READ CAPACITY (16) command transfers parameter data that includes a value in the LOGICAL BLOCKS
PER PHYSICAL BLOCK EXPONENT field. As shown in figure 2 and in figure 4, the value in this field enables the
application client to determine the number of logical blocks per physical block.
The Block Limits VPD page may include values in the OPTIMAL TRANSFER LENGTH GRANULARITY field, the
OPTIMAL TRANSFER LENGTH field, and the MAXIMUM TRANSFER LENGTH field. These values may be used to
determine optimum transfer sizes.
If the OPTIMAL TRANSFER LENGTH GRANULARITY field is valid (i.e., contains a value greater than zero), then the
value in the OPTIMAL TRANSFER LENGTH GRANULARITY field is the optimal granularity size. If:
a)
the Block Limits VPD page is not supported; or
b)
the Block Limits VPD page is supported and the OPTIMAL TRANSFER LENGTH GRANULARITY field is set to
zero,
then the value 2(logical blocks per physical block exponent) is the optimal granularity size.
D.4 Optimal stream granularity sizes
The Block Limits Extension VPD page may include values in the OPTIMAL STREAM WRITE SIZE field and the
STREAM GRANULARITY SIZE field. These values may be used to determine optimum transfer sizes and optimum
transfer alignment to use with the WRITE STREAM commands (see 5.57 and 5.58).
If the OPTIMAL STREAM WRITE SIZE field is valid (i.e., contains a value greater than zero), then the value in the
OPTIMAL STREAM WRITE SIZE field indicates the optimum transfer size and the optimum transfer alignment.


If:
a)
the Block Limits Extension VPD page is not supported; or
b)
the Block Limits Extension VPD page is supported and the OPTIMAL STREAM WRITE SIZE field is
set to zero,
then the optimum transfer size and optimum transfer alignment is not reported for WRITE STREAM
commands.
D.5 Optimizing transfers
D.5.1 Overview
Non-stream write commands may be optimized using the method described in D.5.2. WRITE STREAM
commands may be optimized using the method described in D.5.3.
D.5.2 Optimizing non-stream transfers
If:
a)
the Block Limits Extension VPD page is not supported;
b)
the OPTIMAL STREAM WRITE SIZE field (see 6.6.5) is zero; or
c)
a write command other than a WRITE STREAM command is sent to the device server,
then to obtain optimal performance, the application client requests transfers with a starting LBA of the form
calculated by the following formula:
starting LBA = lowest aligned LBA + (optimal transfer length granularity × n)
where:
starting LBA
is the LBA of the first logical block accessed;
lowest aligned LBA
is the value in the LOWEST ALIGNED LOGICAL BLOCK ADDRESS field; and
n
is zero or a positive integer.
and using transfer lengths of the form:
transfer length = (optimal granularity size × k)
where:
transfer length
is the number of contiguous logical blocks of data being accessed;
optimal granularity size
is the value described in D.3; and
k
is a positive integer.
To obtain optimal performance, the application client requests a transfer length, in logical blocks, that is no
larger than the value in the MAXIMUM TRANSFER LENGTH field, and is:
a)
no larger than the optimal transfer length for logical units where the delay in processing transfers
larger than the optimal transfer length is large; or
b)
not limited by the value in the OPTIMAL TRANSFER LENGTH field for logical units where the delay in
processing transfers larger than the optimal transfer length is small (i.e., most direct access block
devices exhibit this type of operation).
NOTE 24 - There is no method available to determine if the delay in processing for various transfer lengths is
large or small.
It is more important that the application client meet the logical unit’s starting and ending alignment boundary
conditions than the maximum transfer length conditions. These considerations have larger impacts on write
performance than read performance.


D.5.3 Optimizing stream transfers
If the Block Limits Extension VPD page is supported, the OPTIMAL STREAM WRITE SIZE field (see 6.6.5) is
non-zero, and WRITE STREAM commands are sent to the device server with a given stream identifier, then to
obtain optimal performance, the application client requests transfers using transfer lengths of the form:
transfer length = (optimal stream granularity × k)
where:
transfer length
is the number of contiguous logical blocks of data being accessed;
optimal stream granularity
is the optimal stream write size (see 6.6.5); and
k
is a positive integer,
and a stream length of the form:
stream length = (optimal stream granularity × stream granularity size × k)
where:
stream length
is the sum of the transfer length of all transfers for that stream (i.e., from
when the stream is opened to when the stream is closed);
optimal granularity size
is the optimal stream write size;
stream granularity size
is the value in the STREAM GRANULARITY SIZE field; and
k
is a positive integer.
D.6 Examples
In this first example, a logical unit reports the following information:
a)
the LOWEST ALIGNED LOGICAL BLOCK ADDRESS field set to 0003h in the READ CAPACITY (16)
parameter data (see 5.21.2);
b)
the OPTIMAL TRANSFER LENGTH GRANULARITY field set to 0008h in the Block Limits VPD page (see
6.6.4);
c)
the MAXIMUM TRANSFER LENGTH field set to 0000_0000h in the Block Limits VPD page; and
d)
the OPTIMAL TRANSFER LENGTH field set to 0000_0080h (i.e., 128) in the Block Limits VPD page.
The starting LBA for optimal transfers on this logical unit should be of the form ((8 × n) + 3) where n is any
integer greater than or equal to zero (e.g., starting LBAs of 3, 11, 19, 27, and 35). The transfer length for
optimal transfers should be a multiple of eight logical blocks (e.g., transfer lengths of 8 blocks, 32 blocks, or
128 blocks).
A write command with the LOGICAL BLOCK ADDRESS field set to 19 and the TRANSFER LENGTH field set to 32
should exhibit improved performance over a write command with the LOGICAL BLOCK ADDRESS field set to 18
and the TRANSFER LENGTH field set to 32.
If the device has a delay in processing transfers larger than the optimal transfer length, some operations may
exhibit improved performance if a single large request is broken into multiple smaller requests (e.g., rather
than performing a single read of 248 logical blocks, the transfer may be optimized by setting the transfer
length of one read command to 128 logical blocks and setting the transfer length of a second read command
to 120 logical blocks).
In this second example, a logical unit reports the following information:
a)
the OPTIMAL STREAM WRITE SIZE field set to 0010h (i.e., 16) in the Block Limits Extension VPD page
(see 6.6.5); and
b)
the STREAM GRANULARITY SIZE field set to 0040h (i.e., 64) in the Block Limits Extension VPD page.


The LOGICAL BLOCK ADDRESS field in a WRITE STREAM command for optimal transfers should be of the form
(16 × j) where j is any integer greater than or equal to zero (e.g., logical block addresses of 16, 32, or 48). The
transfer length in a WRITE STREAM command for optimal transfers should be of the form (16 × k) where k is
any integer greater than or equal to zero (e.g., transfer lengths of 16 blocks, 32 blocks, or 48 blocks). The
stream length for optimal transfers should be of the form (16 × 64 × m) where m is any integer greater than or
equal to zero (e.g., stream lengths of 1 024 blocks, 2 048 blocks, or 3 072 blocks).
The stream length is the total of all write transactions using the specified stream identifier (i.e., from the receipt
of a STREAM CONTROL command with the STR_CTL field set to 01b (i.e., open) to the receipt of a STREAM
CONTROL command with the STR_CTL field set to 10b (i.e., close) and the STR_ID field set to the specified
stream identifier).
A WRITE STREAM command with the LOGICAL BLOCK ADDRESS field set to 32 (i.e., an integer multiple of 16)
and the TRANSFER LENGTH field set to 64 (i.e., an integer multiple of 16) should exhibit improved performance
over a WRITE STREAM command with the LOGICAL BLOCK ADDRESS field set to 16 (i.e., an integer multiple of
16) and the TRANSFER LENGTH field set to 20 (i.e., not an integer multiple of 16).
A sequence of WRITE STREAM commands to the stream that specify a total of 2 048 logical blocks (i.e., an
integer multiple of 1 024) should exhibit improved performance over a sequence of WRITE STREAM
commands to the stream that specify a total of 1 536 logical blocks (i.e., not an integer multiple of 1 024).


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
