# 5.5.2 Retrieving error history with the READ BUFFER command

5.5.2 Retrieving error history with the READ BUFFER command
Device servers may allow the error history to be retrieved using a sequence of READ BUFFER commands on
one I_T nexus.
Error history is returned using error history snapshots. An error history snapshot is the contents of the error
history at a specific point in time, created by the device server at vendor specific times or requested by the
application client using the READ BUFFER command with certain buffer IDs.
The I_T nexus being used to retrieve error history snapshot is called the error history I_T nexus. Only one I_T
nexus is allowed to retrieve an error history snapshot at a time.
To retrieve the complete error history, an application client uses one I_T nexus to:
1)
create an error history snapshot if one does not already exist, establish the I_T nexus as the error
history I_T nexus, and retrieve the error history directory by sending a READ BUFFER command (see
6.18.9.2) with:
A)
the MODE field set to 1Ch (i.e., error history);
B)
the BUFFER ID field set to one of the following:
a)
If the error history I_T nexus is expected to be valid:
A)
00h (i.e., return error history directory);
B)
01h (i.e., return error history directory and create new snapshot);
b)
if the application client has knowledge obtained by means outside the scope of this standard
that the error history I_T nexus is no longer valid:
A)
02h (i.e., return error history directory and establish new error history I_T nexus); or
B)
03h (i.e., return error history directory, establish new error history I_T nexus, and create
new snapshot);
C) the BUFFER OFFSET field set to 000000h; and
D) the ALLOCATION LENGTH field set to at least 2 088 (i.e., large enough to transfer the complete error
history directory);
2)
retrieve the error history. The application client uses a Data-In Buffer size that is a multiple of the
offset boundary indicated in the READ BUFFER descriptor (see 6.18.5). For each buffer ID indicated
in the error history directory in the range of 10h to EFh, the application client sends one or more
READ BUFFER commands (see 6.18.9.3) as follows:
1)
send the first READ BUFFER command with:
a)
the MODE field set to 1Ch (i.e., error history);
b)
the BUFFER ID field set to the buffer ID (i.e., an error history data buffer);
c)
the BUFFER OFFSET field set to 000000h; and
d)
the ALLOCATION LENGTH field set to the size of the Data-In Buffer;
2)
until the number of bytes returned by the previous READ BUFFER command does not equal the
specified allocation length and/or the total number of bytes returned from the buffer ID equals the
maximum available length indicated in the error history directory, send zero or more additional
READ BUFFER commands with:
a)
the MODE field set to 1Ch (i.e., error history);
b)
the BUFFER ID field set to the buffer ID (i.e., an error history data buffer);
c)
the BUFFER OFFSET field set to the previous buffer offset plus the previous allocation length;
and
d)
the ALLOCATION LENGTH field set to the size of the Data-In Buffer;
and
3)
clear the error history I_T nexus and, depending on the buffer ID, release the error history snapshot
by sending a READ BUFFER command with:
A)
the MODE field set to 1Ch (i.e., error history);
B)
the BUFFER ID field set to:
a)
FEh (i.e., clear error history I_T nexus) (see 6.18.9.4); or


b)
FFh (i.e., clear error history I_T nexus and release snapshot) (see 6.18.9.5);
C) the BUFFER OFFSET field set to any value allowed by table 231 (see 6.18.9.1) (e.g., 000000h); and
D) the ALLOCATION LENGTH field set to any value allowed for the chosen BUFFER ID field value (see
6.18.9.4 or 6.18.9.5) (e.g., 000000h).
While an error history snapshot exists, the device server:
a)
shall not modify the error history snapshot to reflect any changes to the error history;
b)
may or may not record events that it detects into the error history; and
c)
if it supports the WRITE BUFFER command download application client error history mode (see
6.49.15), shall record any application client error history received into the error history.
The device server shall clear the established error history I_T nexus and not release the error history
snapshot:
a)
upon processing of a READ BUFFER command on the error history I_T nexus with:
A)
the MODE field set to 1Ch (i.e., error history); and
B)
the BUFFER ID field set to FEh (i.e., clear error history I_T nexus) (see 6.18.9.4);
or
b)
if an I_T nexus loss occurs on the error history I_T nexus.
The device server shall clear the established error history I_T nexus and release the error history snapshot:
a)
upon processing of a READ BUFFER command using the same I_T nexus that was used to establish
the snapshot with:
A)
the MODE field set to 1Ch (i.e., error history); and
B)
the BUFFER ID field set to FFh (i.e., clear error history I_T nexus and release snapshot) (see
6.18.9.5);
b)
if a power on occurs;
c)
if a hard reset occurs; or
d)
if a logical unit reset occurs.
The device server shall not replace or release the error history snapshot while the error history I_T nexus is
established.
The device server shall implement a vendor specific timer for error history snapshot retrieval. If the vendor
specific timer expires, then:
a)
the device server shall:
A)
clear the error history I_T nexus; and
B)
establish a unit attention condition for the error history I_T nexus with the additional sense code
set to ERROR HISTORY I_T NEXUS CLEARED;
or
b)
the device server shall:
A)
clear the error history I_T nexus;
B)
release the error history snapshot; and
C) establish a unit attention condition for the error history I_T nexus with the additional sense code
set to ERROR HISTORY SNAPSHOT RELEASED.
After an error history snapshot is released, the device server shall resume recording error history for events
that it detects.
Error history may also be retrieved by vendor specific methods or other READ BUFFER command sequences
that are outside the scope of this standard.
