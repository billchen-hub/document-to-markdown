# 4.28 Block device ROD token operations

4.28 Block device ROD token operations
4.28.1 Block device ROD token operations overview
Application clients request that block device ROD token operations (see SPC-6) be performed using the
commands summarized in this subclause or the commands specified in SPC-6.
Copy managers (see SPC-6) that implement the POPULATE TOKEN command (see 5.12) or the WRITE
USING TOKEN command (see 5.59) shall support the following:
a)
the POPULATE TOKEN command;
b)
the WRITE USING TOKEN command;
c)
the RECEIVE COPY STATUS (LID4) command (see SPC-6);
d)
the RECEIVE ROD TOKEN INFORMATION command (see SPC-6 and 5.25); and
e)
the Third-party Copy VPD page (see 6.6.9) containing at least one Block Device ROD token limits
descriptor (see 6.6.9.3).
The POPULATE TOKEN command may cause the copy manager to create zero or one point in time ROD
tokens. If the POPULATE TOKEN command causes one point in time ROD token to be created, then this
point in time ROD token may be retrieved by an application client using the RECEIVE ROD TOKEN
INFORMATION command.
The WRITE USING TOKEN command causes the copy manager to transfer the data represented by the
specified ROD token (i.e., the data represented by the ROD token retrieved using the RECEIVE ROD TOKEN
INFORMATION command or the data represented by the block device zero ROD token).
The copy manager manages the point in time ROD token.
After the copy manager begins processing a POPULATE TOKEN command or a WRITE USING TOKEN
command, the copy manager shall preserve information for return in response to a RECEIVE ROD TOKEN
INFORMATION command as defined in SPC-6.
Block device range descriptor lists (see 5.12.3) contain non-overlapping block device range descriptors and
are used by the application client to specify:
a)
the logical blocks to include in the data represented by the ROD token;
b)
the sequence of the logical blocks in the data represented by the ROD token (e.g., the first logical
block represented by the LBA described in the first block device range descriptor is placed at the
beginning of the data represented by the ROD token, and the first logical block represented by the
LBA described in the second block device range descriptor is placed in the data represented by the
ROD token immediately following the last logical block represented by the LBA described in the first
block device range descriptor);
c)
the logical blocks to be written from the data represented by the ROD token; and
d)
the sequence of the logical blocks written from the data represented by the ROD token (e.g., the first
logical block represented by the LBA described in the first block device range descriptor is written
from the beginning of the data represented by the ROD token, and the first logical block represented
by the LBA described in the second block device range descriptor is written from data represented by
the ROD token immediately following the data written to the last logical block represented by the LBA
described in the first block device range descriptor).
If the copy manager uses out of order transfers to create the representation of data for the ROD token, then
the TRANSFER COUNT field in the parameter data returned in the response to a RECEIVE ROD TOKEN
INFORMATION command with a list identifier that specifies a POPULATE TOKEN command (see 5.25.2)
shall be based only on the contiguous transfers that complete without error starting at the first LBA specified
by the first block device range descriptor (i.e., any transfers completed without error beyond the first
incomplete or unsuccessful transfer shall not contribute to the computation of the value in the TRANSFER
COUNT field).
If the copy manager uses out of order transfers to write from the data represented by the ROD token, then the
TRANSFER COUNT field in the parameter data returned in response to a RECEIVE ROD TOKEN
INFORMATION command with a list identifier that specifies a WRITE USING TOKEN command (see 5.25.3)


shall be based only on the contiguous transfers that complete without error starting at the first LBA specified
by the first block device range descriptor (i.e., any transfers completed without error beyond the first
incomplete or unsuccessful transfer shall not contribute to the computation of the value in the TRANSFER
COUNT field).
4.28.2 POPULATE TOKEN command and WRITE USING TOKEN command completion
As part of completing a block device token operation originated by a POPULATE TOKEN command
(see 5.12) or a WRITE USING TOKEN command (see 5.59), the copy manager shall compute the residual by
subtracting the sum of the contents of the NUMBER OF LOGICAL BLOCK fields in all of the complete block device
range descriptors of the parameter list (see 5.12.3) from the TRANSFER COUNT field in the parameter data
returned in response to a RECEIVE ROD TOKEN INFORMATION command (see 5.25.2 and 5.25.3).
If the POPULATE TOKEN command was received with the IMMED bit set to zero, and the residual is negative,
then the copy manager shall:
a)
terminate the command with CHECK CONDITION status, with the additional sense code set to COPY
TARGET DEVICE DATA UNDERRUN, the sense key set to:
A) COPY ABORTED, if the transfer count is not zero; or
B) ILLEGAL REQUEST, if the transfer count is zero,
and report the transfer count in the INFORMATION field (see SPC-6); or
b)
complete the command with GOOD status and return parameter data for the RECEIVE ROD TOKEN
INFORMATION command received on the same I_T nexus with a matching LIST IDENTIFIER field with:
A) the COPY OPERATION STATUS field set to 03h or set to 60h (see SPC-6);
B) the EXTENDED COPY COMPLETION STATUS field set to CHECK CONDITION (see SAM-6); and
C) the SENSE DATA field with the additional sense code set to COPY TARGET DEVICE DATA
UNDERRUN, the sense key set to:
a)
COPY ABORTED, if the transfer count is not zero; or
b)
ILLEGAL REQUEST, if the transfer count is zero,
and report the transfer count in the INFORMATION field (see SPC-6).
If the WRITE USING TOKEN command was received with the IMMED bit set to zero, and the residual is
negative, then the copy manager shall terminate the command with CHECK CONDITION status, the
additional sense code set to COPY TARGET DEVICE DATA UNDERRUN, the sense key set to:
a)
COPY ABORTED, if the transfer count is not zero; or
b)
ILLEGAL REQUEST, if the transfer count is zero,
and report the transfer count in the INFORMATION field (see SPC-6).
If the POPULATE TOKEN command or WRITE USING TOKEN command was received with the IMMED bit set
to one, and the residual is negative, then the copy manager shall return parameter data for the RECEIVE
ROD TOKEN INFORMATION command received on the same I_T nexus with a matching LIST IDENTIFIER field
with:
a)
the COPY OPERATION STATUS field set to 03h or 60h (see SPC-6);
b)
the EXTENDED COPY COMPLETION STATUS field set to CHECK CONDITION status (see SAM-6); and
c)
the SENSE DATA field with the additional sense code set to COPY TARGET DEVICE DATA
UNDERRUN, the sense key set to:
A) COPY ABORTED, if the transfer count is not zero; or
B) ILLEGAL REQUEST, if the transfer count is zero,
and report the transfer count in the INFORMATION field (see SPC-6).
4.28.3 Block device specific ROD tokens
Block device specific ROD token types (see SPC-6) are shown in table 30.


4.28.4 Block device zero ROD token
The block device zero ROD token represents user data in which all bits are set to zero and protection
information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h (i.e., the valid CRC for user data in which all
bits are set to zero);
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh.
If user data with all bits set to zero and protection information, if any, with the:
a)
LOGICAL BLOCK GUARD field set to FFFFh or set to 0000h;
b)
LOGICAL BLOCK APPLICATION TAG field set to FFFFh; and
c)
LOGICAL BLOCK REFERENCE TAG field set to FFFF_FFFFh,
is represented by a ROD token, then, in response to a RECEIVE ROD TOKEN INFORMATION command in
which the LIST IDENTIFIER field specifies a POPULATE TOKEN command, the copy manager may or may not
return a ROD token that is the block device zero ROD token. The block device zero ROD token format is
shown in table 31.
Table 30 — ROD token type values
ROD token type
Description
Reference
FF00_0000h to FFFF_0000h
Reserved
FFFF_0001h
Block device zero ROD token
4.28.4
FFFF_0002h to FFFF_FFEFh
Reserved
Table 31 — Block device zero ROD token format
Bit
Byte
(MSB)
ROD TOKEN TYPE (FFFF_0001h)
•••
(LSB)
Reserved
(MSB)
ROD TOKEN LENGTH (01F8h)
(LSB)
Reserved
•••
Reserved
CRC VALID
Reserved
•••
