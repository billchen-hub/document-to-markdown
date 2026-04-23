# 5.59 WRITE USING TOKEN command

5.59 WRITE USING TOKEN command
5.59.1 WRITE USING TOKEN command overview
The WRITE USING TOKEN command (see table 158) requests that the copy manager (see SPC-6) write
logical block data represented by the specified ROD token to the specified LBAs.
The OPERATION CODE field and the SERVICE ACTION field are defined in SPC-6 and shall be set to the values
shown in table 158 for the WRITE USING TOKEN command.
The LIST IDENTIFIER field is defined in SPC-6. The list identifier shall be processed as if the LIST ID USAGE field
is set to 00b in the parameter data for an EXTENDED COPY(LID4) command (see SPC-6).
The PARAMETER LIST LENGTH field specifies the length in bytes of the parameter data that is available to be
transferred from the Data-Out Buffer. A PARAMETER LIST LENGTH set to zero specifies that no data shall be
transferred. This shall not be considered an error.
See the PRE-FETCH (10) command (see 5.13 and 4.22) for the definition of the GROUP NUMBER field.
The CONTROL byte is defined in SAM-6.
Table 158 — WRITE USING TOKEN command
Bit
Byte
OPERATION CODE (83h)
Reserved
SERVICE ACTION (11h)
Reserved
•••
(MSB)
LIST IDENTIFIER
•••
(LSB)
(MSB)
PARAMETER LIST LENGTH
•••
(LSB)
Reserved
GROUP NUMBER
CONTROL


5.59.2 WRITE USING TOKEN parameter list
The parameter list for the WRITE USING TOKEN command is shown in table 159.
The WRITE USING TOKEN DATA LENGTH field specifies the length in bytes of the data that is available to be
transferred from the Data-Out Buffer. The write using token data length does not include the number of bytes
in the WRITE USING TOKEN DATA LENGTH field.
If the WRITE USING TOKEN DATA LENGTH field is less than 0226h (i.e., 550), then the copy manager shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the contents of the WRITE USING TOKEN DATA LENGTH  field is not equal to the contents of the BLOCK DEVICE
RANGE DESCRIPTOR LENGTH field plus 534 then  the device server should terminate the command with CHECK
CONDITION status with the sense key set to ILLEGAL REQUEST and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
Table 159 — WRITE USING TOKEN parameter list
Bit
Byte
(MSB)
WRITE USING TOKEN DATA LENGTH (n - 1)
(LSB)
Reserved
DEL_TKN
IMMED
Reserved
•••
(MSB)
OFFSET INTO ROD
•••
(LSB)
ROD TOKEN
•••
Reserved
•••
BLOCK DEVICE RANGE DESCRIPTOR LENGTH (n - 535)
Block device range descriptor list (if any)
Block device range descriptor [first] (see 5.12.3)
•••
•••
n - 15
Block device range descriptor [last] (see 5.12.3)
•••
n


The immediate (IMMED) bit specifies when the copy manager shall return status for the WRITE USING TOKEN
command. If the IMMED bit is set to zero, then the copy manager shall process the WRITE USING TOKEN
command until all specified operations are complete or an error is detected. If the IMMED bit is set to one, then
the copy manager:
1)
shall validate the CDB (i.e., detect and report all errors in the CDB);
2)
shall transfer all the parameter data to the copy manager;
3)
may validate the parameter data;
4)
shall complete the WRITE USING TOKEN command with GOOD status; and
5)
shall complete processing of all specified operations as a background operation (see SPC-6).
If the operations specified by a WRITE USING TOKEN command are processed as a background operation
(i.e., the IMMED bit is set to one) (see SPC-6), then the copy manager shall not generate deferred errors (see
SAM-6) to report the errors encountered, if any, during this processing. The copy manager shall make error
information available to an application client using a RECEIVE ROD TOKEN INFORMATION command
(see 5.25).
A delete token (DEL_TKN) bit set to one specifies that the ROD token specified in the ROD TOKEN field should be
deleted when processing of the WRITE USING TOKEN command is complete. A DEL_TKN bit set to zero
specifies that the ROD token lifetime for the ROD token specified in the ROD TOKEN field shall be as described
in SPC-6.
The OFFSET INTO ROD field specifies the offset into the data represented by the ROD token from the first byte
represented by the ROD token to the first byte to be transferred. The offset is specified in number of blocks
based on the logical block length of the logical unit to which the WRITE USING TOKEN command is to write
data. The copy manager that processes the WRITE USING TOKEN command shall compute the byte offset
into the ROD by multiplying the contents of the OFFSET INTO ROD field by the logical block length of the logical
unit to which the WRITE USING TOKEN command is to write data.
EXAMPLE - To calculate an offset, a ROD token is created from LBAs 15 to 20 followed by LBAs 40 to 100 by a copy
manager associated with a logical unit with a logical block length of 512 bytes per logical block. That ROD token is
specified in a WRITE USING TOKEN command that transfers one logical block to a logical unit with a logical block length
of 4 096 bytes per logical block. The subsequent RECEIVE ROD TOKEN INFORMATION command indicates the
successful transfer of 4 096 bytes by setting the TRANSFER COUNT field to one. To create a WRITE USING TOKEN
command that transfers bytes from the ROD token starting at the point where the previous WRITE USING TOKEN
command stopped, the OFFSET INTO ROD field is set to one (i.e., the contents of the TRANSFER COUNT field) plus the value in
the OFFSET INTO ROD field in the previous WRITE USING TOKEN command (i.e., zero). The copy manager multiplies one
(i.e., the value in the OFFSET INTO ROD field) by 4 096 (i.e., the logical block length for the logical unit to which the data is
being written) and the result is 4 096. As a result, the ROD token logical block that is the start of the transfer is LBA 8 (i.e.,
LBA 42 from the logical unit whose logical block length is 512 bytes per logical block that was used to create the ROD
token).
If the computed byte offset into the ROD is greater than or equal to the number of bytes represented by the
ROD token, then the copy manager shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
If the ROD TOKEN LENGTH field (see SPC-6) in the ROD TOKEN field is not set to 01F8h, then the copy manager
shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST
and the additional sense key set to INVALID TOKEN OPERATION, INVALID TOKEN LENGTH.
The ROD TOKEN field specifies the ROD token that represents the data from which logical block data is written.
The ROD token is defined as follows:
a)
a ROD token returned by a RECEIVE ROD TOKEN INFORMATION command; or
b)
a block device zero ROD token (see 4.28.4).
If the ROD token does not match any known to the copy manager, then the copy manager shall terminate the
command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and the additional
sense code set to INVALID TOKEN OPERATION, TOKEN UNKNOWN.


The BLOCK DEVICE RANGE DESCRIPTOR LENGTH field specifies the length in bytes of the block device range
descriptor list. The block device range descriptor list length should be a multiple of 16. If the block device
range descriptor list length is not a multiple of 16, then the last block device range (see 5.12.3) descriptor is
incomplete and shall be ignored. If the block device range descriptor list length is less than 16, then the copy
manager shall terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL
REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the number of complete block device range descriptors is larger than the MAXIMUM RANGE DESCRIPTORS field
(see 6.6.9.3), then the copy manager shall terminate the command with CHECK CONDITION status with the
sense key set to ILLEGAL REQUEST and the additional sense code set to TOO MANY SEGMENT
DESCRIPTORS.
If the same LBA is included in more than one block device range descriptor, then the copy manager shall
terminate the command with CHECK CONDITION status with the sense key set to ILLEGAL REQUEST and
the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the number of bytes of user data represented by the sum of the contents of the NUMBER OF LOGICAL BLOCKS
fields in all of the complete block device range descriptors is larger than:
a)
the MAXIMUM BYTES IN BLOCK ROD field in the block ROD device type specific features descriptor in the
ROD token features third-party copy descriptor in the Third-party Copy VPD page (see SPC-6) and
that field is set to a non-zero value; or
b)
the MAXIMUM TOKEN TRANSFER SIZE field (see 6.6.9.3) and that field is set to a non-zero value,
then the copy manager shall terminate the command with CHECK CONDITION status with the sense key set
to ILLEGAL REQUEST and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
If the number of bytes of user data represented by the sum of the contents of the NUMBER OF LOGICAL BLOCKS
fields in all of the complete block device range descriptors is larger than the number of bytes in the data
represented by the ROD token minus the computed byte offset into the ROD (i.e., the total requested length of
the transfer exceeds the length of the data available in the data represented by the ROD token), then the copy
manager shall:
a)
transfer as many whole logical blocks as possible; and
b)
if any portion of a logical block that is written by the copy manager corresponds to offsets into the
ROD at or beyond the length of the data represented by the ROD token, then write that portion of the
logical block with user data with all bits set to zero.
The copy manager may perform this check during the processing of each block device range descriptor.
