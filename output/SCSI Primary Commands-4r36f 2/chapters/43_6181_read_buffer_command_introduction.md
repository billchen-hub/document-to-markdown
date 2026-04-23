# 6.18.1 READ BUFFER command introduction

6.17.6 SUPPORTED ATTRIBUTES service action
The READ ATTRIBUTE command with SUPPORTED ATTRIBUTES service action returns parameter data
containing the attribute identifiers for the attributes that are supported by the device server in the specified
partition and volume number. The contents of FIRST ATTRIBUTE IDENTIFIER field in the CDB shall be ignored.
The returned parameter data shall contain the requested attribute identifiers in ascending numerical order by
attribute identifier value and in the format shown in table 224.
The AVAILABLE DATA field shall contain the number of bytes of attribute identifiers in the parameter list. The
contents of the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
For each attribute that is in the read only state, in the read/write state, or in the nonexistent state (see 5.7) in
the specified partition and volume number:
a)
an attribute identifier (see 7.4.2) is returned for device type attributes (see 7.4.2.2), medium type
attributes (see 7.4.2.3), and host type attributes defined in this standard (see 7.4.2.4); and
b)
if vendor specific host type attributes (see 7.4.2.1) are supported, then an attribute identifier is
returned for the first supported vendor specific host type attribute and attribute identifiers may be
returned for other supported vendor specific host type attributes.
6.18 READ BUFFER command
6.18.1 READ BUFFER command introduction
The READ BUFFER command (see table 225) is used in conjunction with the WRITE BUFFER command for:
a)
testing logical unit buffer memory;
b)
testing the integrity of the service delivery subsystem;
c)
downloading microcode (see 5.4); and
Table 224 — READ ATTRIBUTE with SUPPORTED ATTRIBUTES service action parameter list format
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)
•••
 (LSB)
Attribute identifiers
(MSB)
ATTRIBUTE IDENTIFIER 0
 (LSB)
•••
n-1
(MSB)
ATTRIBUTE IDENTIFIER x
n
 (LSB)


d)
retrieving error history.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 225 for the READ BUFFER
command.
The function of this command and the meaning of fields within the CDB depend on the contents of the MODE
field. The MODE field is defined in table 226.
The MODE field may be processed as specifying a service action by the REPORT SUPPORTED OPERATION
CODES command (see 6.35).
If the MODE field is not set to one, the ALLOCATION LENGTH field is defined in 4.2.5.6.
Table 225 — READ BUFFER command
Bit
Byte
OPERATION CODE (3Ch)
Reserved
MODE
BUFFER ID
(MSB)
BUFFER OFFSET
(LSB)
(MSB)
ALLOCATION LENGTH
(LSB)
CONTROL
Table 226 — READ BUFFER MODE field
Code
Description
References
00h
Combined header and data a
6.18.2
01h
Vendor specific a
6.18.3
02h
Data
6.18.4
03h
Descriptor
6.18.5
04h to 09h
Reserved
0Ah
Read data from echo buffer
6.18.6
0Bh
Echo buffer descriptor
6.18.7
0Ch to 19h
Reserved
1Ah
Enable expander communications protocol and Echo buffer
6.18.8
1Bh
Reserved
1Ch
Error history
5.5 and 6.18.9
1Dh to 1Fh
Reserved
a Modes 00h and 01h are not recommended.


The CONTROL byte is defined in SAM-5.
6.18.2 Combined header and data mode (00h)
In this mode, a four-byte header followed by data bytes is returned to the application client in the Data-In
Buffer. The allocation length should be set to four or greater. The BUFFER ID and the BUFFER OFFSET fields are
reserved.
The four-byte READ BUFFER header (see table 227) is followed by data bytes from the buffer.
The BUFFER CAPACITY field specifies the total number of data bytes that follow in the buffer. The buffer capacity
is not reduced to reflect the actual number of bytes written using the WRITE BUFFER command with
combined header and data mode (see 6.49.2). The contents of the BUFFER CAPACITY field are not altered
based on the allocation length (see 4.2.5.6). Following the READ BUFFER header, the device server shall
transfer data from the buffer.
NOTE 35 - The buffer is shared by all application clients and I_T nexuses. If one application client writes the
buffer, a second application client writes the buffer, and then the first application client reads the buffer, the
read may or may not retrieve the data from the second application client.
6.18.3 Vendor specific mode (01h)
In this mode, the meanings of the BUFFER ID, BUFFER OFFSET, and ALLOCATION LENGTH fields are not specified
by this standard.
6.18.4 Data mode (02h)
In this mode, the Data-In Buffer is filled only with logical unit buffer data. The BUFFER ID field specifies a buffer
within the logical unit from which data shall be transferred. The vendor assigns buffer ID codes to buffers
within the logical unit. Buffer ID zero shall be supported. If more than one buffer is supported, then additional
buffer ID codes shall be assigned contiguously, beginning with one. Buffer ID code assignments for the READ
BUFFER command with data mode shall be the same as for the WRITE BUFFER command with data mode
(see 6.49.4). If an unsupported buffer ID code is selected, then the command shall be terminated with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN CDB.
Table 227 — READ BUFFER header
Bit
Byte
Reserved
(MSB)
BUFFER CAPACITY
(LSB)
Data
•••
n


The BUFFER OFFSET field specifies the byte offset within the specified buffer from which data shall be trans-
ferred. The application client should conform to the offset boundary requirements returned in the READ
BUFFER descriptor (see 6.18.5). If the device server is unable to accept the specified buffer offset, the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
NOTE 36 - The buffer is shared by all application clients and I_T nexuses. If one application client writes the
buffer, a second application client writes the buffer, and then the first application client reads the buffer, the
read may or may not retrieve the data from the second application client.
6.18.5 Descriptor mode (03h)
In this mode, a maximum of four bytes of READ BUFFER descriptor information is returned. The BUFFER
OFFSET field is reserved in this mode. The allocation length should be set to four or greater. The READ
BUFFER descriptor is defined as shown in table 228.
For READ BUFFER commands, the OFFSET BOUNDARY field (see table 229) applies to the following modes:
a)
data (i.e., 02h) (see 6.18.4); and
b)
error history (i.e., 1Ch) (see 6.18.9).
For WRITE BUFFER commands, the OFFSET BOUNDARY field (see table 229) applies to the following modes:
a)
data (i.e., 02h) (see 6.49.4);
b)
download microcode with offsets and activate (i.e., 06h) (see 6.49.7);
c)
download microcode with offsets, save, and activate (i.e., 07h) (see 6.49.8);
d)
download microcode with offsets, select activation events, save, and defer activate (i.e., 0Dh) (see
6.49.10); and
e)
download microcode with offsets, save, and defer activate (i.e., 0Eh) (see 6.49.11).
For data mode (i.e., 02h), the boundary alignment indicated by the OFFSET BOUNDARY field applies only to the
buffer specified by the BUFFER ID field. For modes other than data to which the OFFSET BOUNDARY field applies,
the boundary alignment applies regardless of the buffer specified by the BUFFER ID field.
Table 228 — READ BUFFER descriptor
Bit
Byte
OFFSET BOUNDARY
(MSB)
BUFFER CAPACITY
(LSB)
Table 229 — OFFSET BOUNDARY field
Code
Description
00h to FEh
Multiples of 2code (e.g., 00h means multiples of 1 byte or no offset restrictions,
01h means multiples of 2 bytes or even offsets, 02h means multiples of 4 bytes)
FFh
000000h is the only supported buffer offset


The BUFFER CAPACITY field indicates the maximum size in bytes of the buffer specified by the BUFFER ID field for
the:
a)
READ BUFFER command with data mode (i.e., 02h); and
b)
WRITE BUFFER command with data mode (i.e., 02h).
6.18.6 Read data from echo buffer mode (0Ah)
In this mode the device server transfers data to the application client from the echo buffer that was written by
the most recent WRITE BUFFER command with the MODE field set to write data to echo buffer (see 6.49.9)
received on the same I_T nexus. The READ BUFFER command shall return the same number of bytes of
data as received in the prior WRITE BUFFER command with the mode field set to write data to echo buffer,
limited by the allocation length as described in 4.2.5.6.
The BUFFER ID and BUFFER OFFSET fields are ignored in this mode.
If no WRITE BUFFER command with the mode set to write data to echo buffer received on this I_T nexus has
completed without an error, then the READ BUFFER command shall terminate with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to COMMAND
SEQUENCE ERROR. If the data in the echo buffer has been overwritten by another I_T nexus and the device
server supports error reporting on echo buffer overwrites (i.e., the EBOS bit is set to one in the echo buffer
descriptor (see 6.18.7)), then the READ BUFFER command shall be terminated with CHECK CONDITION
status, with the sense key set to ABORTED COMMAND, and the additional sense code set to ECHO
BUFFER OVERWRITTEN.
After a WRITE BUFFER command with the mode set to write data to echo buffer has completed without an
error, the application client may send multiple READ BUFFER commands with the mode set to read data from
echo buffer in order to read the echo buffer data multiple times.
6.18.7 Echo buffer descriptor mode (0Bh)
In this mode, a maximum of four bytes of READ BUFFER descriptor information is returned. The device
server shall return the descriptor information for the echo buffer. If there is no echo buffer implemented, the
device server shall return all zeros in the READ BUFFER descriptor. The BUFFER ID field and BUFFER OFFSET
field are reserved in this mode. The allocation length should be set to four or greater. The READ BUFFER
descriptor is defined as shown in table 230.
The BUFFER CAPACITY field shall return the size of the echo buffer in bytes aligned to a four-byte boundary. The
maximum echo buffer size is 4 096 bytes.
If the echo buffer is implemented, the echo buffer descriptor shall be implemented.
Table 230 — Echo buffer descriptor
Bit
Byte
Reserved
EBOS
Reserved
Reserved
(MSB)
BUFFER CAPACITY
(LSB)
