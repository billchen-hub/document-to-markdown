# 4.32 Stream control

If the device server processes a BACKGROUND CONTROL command with the BO_CTL field set to 10b (i.e.,
stop host initiated background control operations) and the device server is not performing host initiated
advanced background operations, then the device server shall not considered this an error.
If the device server processes a BACKGROUND CONTROL command with the BO_CTL field set to 10b (i.e.,
stop host initiated background control operations) and the device server is performing host initiated advanced
background operations, then the device server shall stop performing host initiated advanced background
operations.
If the device server processes a BACKGROUND CONTROL command with the BO_CTL field set to 00b, then
the device server shall:
a)
not change any host initiated advanced background operations;
b)
ignore the value in the BO_TIME field; and
c)
not considered this an error.
4.32 Stream control
Stream control is limited by the MAXIMUM NUMBER OF STREAMS field, the OPTIMAL STREAM WRITE SIZE field, and
the STREAM GRANULARITY SIZE field (see 6.6.5). Logical units that support stream control shall be resource
provisioned logical units as described in 4.7.3.2 or thin provisioned logical units as described in 4.7.3.3.
Logical units that implement the stream control model are comprised of physical blocks that are arranged in a
manner such that background operations to prepare resources for future allocations to LBAs are performed on
those physical blocks. STREAM WRITE commands with a transfer length that matches the value specified in
the OPTIMAL STREAM WRITE SIZE field (see 6.6.5), and with an initial LBA that is either zero or a multiple of the
value specified in the OPTIMAL STREAM WRITE SIZE field provide optimal performance from the device.
See annex D for an example method in which application clients may use alignment information to determine
optimal performance for stream writes.
A device server that supports stream control as described in this subclause shall:
a)
support the STREAM CONTROL command (see 5.32);
b)
Support the WRITE STREAM (16) command (see 5.57) or the WRITE STREAM (32) command
(see 5.58);
c)
support the GET STREAM STATUS command (see 5.9); and
d)
support the Block Limits Extension VPD page (see 6.6.5).
The number of optimal stream write size blocks that are prepared as a unit for future allocation to LBAs is
indicated in the STREAM GRANULARITY SIZE field (see 6.6.5). The application client should write an integer
multiple of stream blocks to the logical unit before closing a stream.
Stream control provides control of streams, each of which is comprised of user data associated with a single
data structure (e.g., a single file or a complete database) or data that has the same lifetime. An application
client opens a stream using the STREAM CONTROL command and then uses the stream identifier provided
by the device server for all subsequent writes associated with that stream. Each stream is associated with a
stream identifier that is associated with the stream from when the stream is opened until the stream is closed.
Valid stream identifiers are 0001h to FFFFh. A stream allows the device server to place the data associated
with a stream identifier into locations that:
a)
are part of one or more stream blocks; and
b)
do not contain any data not associated with that stream identifier.
For optimal performance, writes to the stream should be aligned to and a multiple of the length specified by
the OPTIMAL STREAM WRITE SIZE field indicated in the Block Limits Extension VPD page (see 6.6.5). Figure 13


shows the relationship of data blocks of optimal stream write size within a stream block, and multiple stream
blocks within a complete stream.
Figure 13 — Stream Block Relationships
Figure 14 shows an example assignment of data blocks received for four different streams to associated
device server resources where:
a)
Stream 1 LBA m - n is one optimal stream write size in length;
b)
Stream 2 LBA x - y is one optimal stream write size in length;
c)
Stream 1 LBA a - b is two optimal stream write sizes in length;
d)
Stream 2 LBA t - u is one optimal stream write size in length;
e)
Stream m LBA k - l is one optimal stream write size in length;
f)
Stream m LBA v - w is one optimal stream write size in length; and
g)
Stream n mapping is not shown.
Figure 14 — Multiple streams example
The application client opens and closes streams using the STREAM CONTROL command (see 5.32) and
requests write operations to a stream using the WRITE STREAM (16) command (see 5.57) or the WRITE
STREAM (32) command (see 5.58). To use a stream for data the application client:
1)
sends a STREAM CONTROL command with the STR_CTL field set to 01b (i.e., open);
2)
waits for the stream identifier value returned in the ASSIGNED_STR_ID field (see 5.32);
3)
sends one or more WRITE STREAM commands with the STR_ID field set to the associated stream
identifier;
Stream Block (first)
Stream Block (last)
...
Complete Stream (stream identifier)
Stream Block
first
opt_sw_size
last
opt_sw_size
...
Key:
    opt_sw_size is the optimal stream write size
Stream 1 resources
LBA m-n
LBA a-b
time
Stream 1
LBA m - n
Stream 1
LBA a - b
Stream m
LBA k - l
Stream 2
LBA t - u
Stream n
LBA e - f
Stream m
LBA v - w
Stream 2
LBA x - y
LBA x-y
LBA t-u
Key:
    opt_sw_size is the optimal stream write size
Stream 2 resources
Stream m resources
LBA k - l
LBA v - w
