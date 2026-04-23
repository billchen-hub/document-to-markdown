# 5.17.2 Copy manager model

5.16.3 Symmetric logical unit access
A device server that provides symmetrical access to a logical unit may use a subset of the asymmetrical
logical access features (see 5.16.2) to indicate this ability to an application client, providing an application
client a common set of commands to determine how to manage target port access to a logical unit.
Symmetrical logical unit access should be represented as follows:
a)
the TPGS field in the standard INQUIRY data (see 6.6.2) indicates that implicit asymmetric access is
supported;
b)
the REPORT TARGET PORT GROUPS command is supported; and
c)
the REPORT TARGET PORT GROUPS parameter data indicates that the same state (e.g.,
active/optimized state) is in effect for all primary target port groups.
5.17 Third-party copies
5.17.1 General considerations for third-party copies
Third-party copy commands (see 5.17.3) cause copy operations (see 5.17.4.3) to transfer data as follows:
a)
from specified areas of the medium within a logical unit to different areas within the same logical unit;
b)
from one logical unit to another within a SCSI target device; or
c)
from one SCSI target device to another SCSI target device.
The transfers requested by a third-party copy command are managed by a copy manager (see 5.17.2) that is
contained in a logical unit (see SAM-5). The copy manager is responsible for transferring data from copy
sources to copy destinations (i.e., reading from the copy sources, buffering as needed, and writing to the copy
destinations).
Application clients and other copy managers request third-party copy operations by sending commands (see
5.17.3) to a copy manager for processing by that copy manager. Copy managers provide information about
their capabilities to application clients in the Third-party Copy VPD page (see 7.8.17).
A copy manager need not support all the third-party copy features described in 5.17, but if a copy manager
supports copies from one SCSI target device to another SCSI target device, then the copy manager
shall support copies from one logical unit to another logical unit within the same SCSI target device.
If a logical unit contains a copy manager that supports any of the commands described in 5.17.3, then the 3PC
bit shall be set to one in the standard INQUIRY data (see 6.6.2).
5.17.2 Copy manager model
A copy manager is:
a)
a kind of device server that processes a limited set of commands (i.e., the commands described in
5.17.3) as foreground or background copy operations (see 5.17.4.3); and
b)
a kind of application client that sends commands to other device servers and copy managers,
possibly in other SCSI target devices, as necessary to perform the copy operation originated by a
third-party command (see 5.17.4.3).


If a copy manager interacts with a copy manger in another SCSI target device, these interactions may occur
over a SCSI transport protocol or over a non-SCSI transport.
Upon the successful completion of a copy operation (see 5.17.4.3), the copy manager shall have produced
the results specified by the command that originated the copy operation in accordance with this standard or
the applicable command standard (e.g., SBC-3 for the WRITE USING TOKEN command). To ensure interop-
erability, this standard or the applicable command standard may place requirements on the copy manager
using terminology based on specific commands and parameter data (e.g., specific instances of the
EXTENDED COPY(LID4) command). These are only functional descriptions of the required copy manager
behavior. Any copy manager implementation that produces the specified results and does not violate interop-
erability may be used.
A copy manager may be contained in:
a)
the same logical unit as the device server for a data storage device (e.g., a direct access block device
(see SBC-3) or sequential-access device (see SSC-4)); or
b)
a standalone SCSI target device whose sole purpose is to house one or more logical units that
contain copy managers.
If the copy manager is contained in the same logical unit as the device server for a data storage device, then
the following requirements shall apply:
a)
the PERIPHERAL DEVICE TYPE field in the standard INQUIRY data (see 6.6.2) shall indicate the device
type associated with the device server;
b)
the copy manager shall have the same access to the data storage media associated with the logical
unit that contains the copy manager as any other application client for the purposes of processing
third-party copy commands and operations (see 5.17.3);
c)
the copy manager shall be able to access all other device servers and copy managers located in the
same SCSI target device as the copy manager; and
d)
the copy manager may or may not be able to access device servers and copy managers located in
other SCSI target devices.
If the copy manager is contained in a standalone SCSI target device whose sole purpose is to house logical
units that contain copy managers, then the following requirements shall apply:
a)
the PERIPHERAL DEVICE TYPE field in the standard INQUIRY data (see 6.6.2) shall indicate that the
device is processor type device (see SPC-2);
b)
the device server may not implement any of the specialized processor device type commands (e.g.,
SEND); and
c)
the copy manager shall able to access device servers and copy managers in at least one other SCSI
target device for the purposes of processing third-party copy commands and operations.
Within a SCSI target device, a copy manager shall not have access to SCSI ports that are not accessible to
the device server in the same logical unit (e.g., due to restrictions imposed by asymmetric logical unit access
features (see 5.16.2)), but a copy manager may have access to non-SCSI data transports. As a result:
a)
if a copy manager has access to only one SCSI port, then the copy operations performed by the copy
manager are limited to a single SCSI domain;
b)
if a copy manager has access to multiple SCSI ports some of which are in different SCSI domains,
then the copy operations performed by the copy manager are limited to the accessible SCSI domains,
but may transfer data from one SCSI domain to another; or
c)
if a copy manager has access to non-SCSI data transports, then the copy operations performed by
the copy manager may transfer data from one SCSI domain to another SCSI domain that is not
accessible to the device server associated with the copy manager.


In response to interactions with other copy managers, a copy manager may process requests for copy opera-
tions even if the copy manager does not implement an equivalent third-party copy command (see 5.17.3).
EXAMPLE – Suppose a copy manager has access to a non-SCSI transport that transfers data in message IUs instead of
SCSI reads and writes. Even though no commands of the kind are performed, the copy manager is allowed to process a
write command as an EXTENDED COPY(LID4) command (see 6.4) with the data to be written contained in the inline data
portion of the parameter data. The copy manager is also allowed to process a read command as an EXTENDED
COPY(LID4) command that generates held data (see 5.17.4.5) followed by a RECEIVE COPY DATA(LID4) command
(see 6.20) to retrieve the held data. The same copy manager may indicate that it supports only the POPULATE TOKEN
command (see SBC-3), WRITE USING TOKEN command (see SBC-3), and RECEIVE ROD TOKEN INFORMATION
command (see 6.26 and SBC-3).
Figure 17 shows examples copy manager configurations and third-party copies they may perform.
Figure 17 — Examples of copy manager configurations
Key:
SCSI transport
data storage media
non-SCSI transport
example third-party copy
SCSI domain
Note - These elements are shown only
when needed for clarity.
Copy
Manager
Applica-
tion Client
Copy
Manager
Copy manager
in logical unit
Applica-
tion Client
Copy
Manager
Copy
Manager
Copy managers
in SCSI target
Copy
Manager
Applica-
tion Client
Copy
Manager
Copy managers in
one SCSI domain
Applica-
tion Client
Copy
Manager
Standalone Copy Manager
Applica-
tion Client
Two copy managers in two SCSI domains
connected by a non-SCSI transport
Copy
Manager
Device
Server
Device
Server


5.17.3 Third-party copy commands
The commands processed by copy managers (i.e., third-party copy commands) are shown in table 107.
Table 107 — Third-party copy commands
Command
Operation
code a
Command
type b
Reference
COPY OPERATION ABORT
83h/1Ch
abort
6.3
EXTENDED COPY(LID4)
83h/01h
originate
6.4
EXTENDED COPY(LID1)
83h/00h
originate
6.5
POPULATE TOKEN
83h/10h
originate
SBC-3
RECEIVE COPY DATA(LID4)
84h/06h
retrieve
6.20
RECEIVE COPY DATA(LID1)
84h/01h
retrieve
6.21
RECEIVE COPY OPERATING PARAMETERS c
84h/03h
retrieve
6.22
RECEIVE COPY FAILURE DETAILS(LID1)
84h/04h
retrieve
6.23
RECEIVE COPY STATUS(LID4)
84h/05h
retrieve
6.24
RECEIVE COPY STATUS(LID1)
84h/00h
retrieve
6.25
RECEIVE ROD TOKEN INFORMATION
84h/07h
retrieve
6.26
REPORT ALL ROD TOKENS
84h/08h
retrieve
6.31
WRITE USING TOKEN
83h/11h
originate
SBC-3
Reserved
all others d
a All copy manager commands are defined by a combination of operation code and service action.
The operation code value is shown preceding the slash and the service action value is shown
after the slash.
b Key:
abort
means a third-party copy command that aborts a specified copy operation
originate
means a third-party copy command that requests the processing of a copy operation
retrieve
means a third-party copy command that retrieves the results (e.g., status or held data)
for a previously originated copy operation
c New operating parameters are no longer being added to the parameter data returned by the
RECEIVE COPY OPERATING PARAMETERS command. The Third-party Copy VPD page (see
7.8.17) provides the most complete information about how a copy manager operates and the
functions that it supports.
d All service actions of operation code 83h and operation code 84h not shown in this table are
reserved.
