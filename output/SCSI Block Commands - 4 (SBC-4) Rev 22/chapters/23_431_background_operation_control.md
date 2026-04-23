# 4.31 Background operation control

4.29.4 Processing ACA conditions during atomic write commands
If another command causes an ACA condition while an atomic write command is being processed, then the
device server:
a)
shall ensure that none of the LBAs specified by the atomic write operation have been altered by any
logical block data from the atomic write operation (i.e., the specified LBAs return logical block data, as
if the atomic write operation had not occurred); and
b)
after the ACA condition is cleared:
A) may terminate the atomic write command with CHECK CONDITION status with a sense key of
ABORTED COMMAND and an additional sense code set to ATOMIC COMMAND ABORTED
DUE TO ACA; or
B) may process the atomic write operation.
4.30 IO advice hints
4.30.1 IO advice hints overview
IO advice hints allow application clients to provide device servers with information about anticipated LBA
usage patterns. A device server uses IO advice hints to provide access to logical blocks that is appropriate to
the specified usage patterns and optimize other aspects of the direct access block device (e.g., power
consumption and performance). The degree to which the device server optimizes the direct access block
device based on anticipated LBA usage patterns may not be measurable by the application client.
EXAMPLE - A device server that implements the IO advice hints features described in this subclause may provide
improved performance for cases where the access pattern matches what was specified by the applicable IO advice hints
(e.g., LBAs that are read in a sequential manner may exhibit better performance when the IO advice hints indicates
sequential access).
IO advice hints are associated with individual commands that contain a GROUP NUMBER field (see 4.30.2). The
device server is not required to retain this association in a way that produces repeatable results (e.g.,
recorded metadata associated with each LBA specified by the command). Device servers may provide the
features described in this subclause by other means (e.g., a device server may direct the transferred data and
the associated LBAs to an area of the media that has properties that match the specified IO advice hints).
4.30.2 Specifying IO advice hints
An application client may specify an IO advice hints by applying the IO advice hints extension of the grouping
function using the GROUP NUMBER field in the CDB of certain commands. The GROUP NUMBER field in each
command determines the IO advice hints used during the processing of that command. At the time a
command that specifies an IO advice hints is received, the device server should process that command in a
manner that produces the effects described in 4.30.1. This standard does not define a method for the device
server to save or return IO advice hints after a command that specifies an IO advice hints has been
processed.
IO advice hints are provided in most data transfer commands. If a device server supports IO advice hints, then
the device server shall implement the:
a)
IO Advice Hints Grouping mode page (see 6.5.7); and
b)
grouping function (see 4.22.1) and grouping function extensions for IO advice hints (see 4.22.2).
4.31 Background operation control
Background operation control is managed by information in the Background Control Mode page (see 6.5.4). A
device server may have requirements to perform advanced background operations if the percentage of device


resources available for allocation reaches the minimum percentage indicated in the MINIMUM PERCENTAGE field
(see 6.6.7). The device server may provide an indication that these resources have reached a value (e.g.,
minimum percentage plus 10%) that is specified by an armed decreasing threshold percentage
(see 4.7.3.7.3). If the device server does not process a BACKGROUND CONTROL command that requests
advanced background operations and the percentage of device resources available for allocation reach the
minimum percentage indicated in the MINIMUM PERCENTAGE field (see 6.6.7), then the device server may
perform advanced background operations without a request from the application client.
EXAMPLE - Advanced background operation may include NAND block erase operations, media read operations, and
media write operations (e.g., garbage collection), which may impact response time for normal read requests or write
requests from the application client.
If the application client is able to predict idle time when there are few read requests and few write requests to
the device server, then the application client may notify the device server about this idle time so that the
device server may perform advanced background operations. As a result, advanced background operations
are minimally overlapped with normal read commands and normal write commands from the application
client. The BACKGROUND CONTROL command (see 5.2) provides the mechanism for the application client
to communicate this information to a logical unit.
The logical block provisioning thresholds (see 4.7.3.7) provides a mechanism for the device server to
establish a unit attention condition to notify application clients when a related logical block provisioning
threshold is crossed.
A device server that supports background operation control as described in this subclause:
a)
shall be a resource provisioned device as described in 4.7.3.2 or a thin provisioned device as
described in 4.7.3.3;
b)
shall set the BOCS bit to one in the Block Device Characteristics VPD page (see 6.6.2);
c)
shall support the Logical Block Provisioning VPD page (see 6.6.7);
d)
should support logical block provisioning thresholds with the THRESHOLD TYPE field set to 001b and
threshold resource value set to 01h (see 4.7.3.7.3);
e)
shall support the Background Operation log page (see 6.4.3);
f)
shall support the Background Control mode page (see 6.5.4); and
g)
shall support the BACKGROUND CONTROL command (see 5.2).
The device server performs notification to the application client of decreasing provisioning resource
percentage using logical block provisioning thresholds (see 4.7.3.7.3). Performing this notification informs the
application client that the application client should determine a time to perform advanced background
operations and then request the device server to perform these advanced background operations using the
BACKGROUND CONTROL command.
If the device server reaches the minimum percentage of resources available as indicated in the MINIMUM
PERCENTAGE field (see 6.6.7), then the device server may begin performing device server initiated advanced
background operations. As a result, the application client should set the threshold percentage sufficiently high
to allow the application client to receive a notification and specify to the device server to perform host initiated
advanced background operations before the device reaches the minimum percentage.
If the device server processes a BACKGROUND CONTROL command with the BO_CTL field set to 01b (i.e.,
start host initiated background control operations), then the device server shall:
1)
initialize the bo_time timer to the value specified in the BO_TIME field (see 5.2) and start the bo_time
timer; and
2)
perform host initiated advanced background operations until:
A) the bo_time timer expires;
B) the device server determines that all necessary advanced background operations are completed;
or
C) the device server processes a BACKGROUND CONTROL command with the BO_CTL field set to
10b (i.e., stop host initiated background control operations).
