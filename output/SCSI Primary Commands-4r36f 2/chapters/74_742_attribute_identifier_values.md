# 7.4.2 Attribute identifier values

7.4.2 Attribute identifier values
7.4.2.1 Attribute identifier values overview
The values in the ATTRIBUTE IDENTIFIER field (see 7.4.1) are assigned according to the attribute type (see 5.7)
and whether the attribute is standard or vendor specific (see table 440).
Device servers may accept and process a WRITE ATTRIBUTE command containing standardized host type
attribute identifier values (i.e., 0800h-0BFFh) or vendor specific host type attribute identifier values (i.e.,
1400h-17FFh). Standardized host type attribute identifier values may be checked as described in 7.4.2.4.
Table 440 — MAM attribute identifier range assignments
Attribute Identifiers
Attribute Type
Standardized
Reference
0000h to 03FFh
Device
Yes
7.4.2.2
0400h to 07FFh
Medium
Yes
7.4.2.3
0800h to 0BFFh
Host
Yes
7.4.2.4
0C00h to 0FFFh
Device
Vendor specific
1000h to 13FFh
Medium
Vendor specific
1400h to 17FFh
Host
Vendor specific
1800h to FFFFh
Reserved


7.4.2.2 Device type attributes
Device type attributes (see table 441) shall be maintained and updated by the device server while the medium
and associated medium auxiliary memory are present. All supported medium type attributes shall have a
status of read only (see 5.7).
7.4.2.2.1 REMAINING CAPACITY IN PARTITION and MAXIMUM CAPACITY IN PARTITION: Are native
capacities (i.e., assuming no data compression for the specified medium partition). These values are
Table 441 — Device type attributes
Attribute
Identifier
Name
Attribute
Length
(in bytes)
Format
Reference
0000h
REMAINING CAPACITY IN PARTITION
BINARY
7.4.2.2.1
0001h
MAXIMUM CAPACITY IN PARTITION
BINARY
7.4.2.2.1
0002h
Restricted (see SSC-3)
0003h
LOAD COUNT
BINARY
7.4.2.2.2
0004h
MAM SPACE REMAINING
BINARY
7.4.2.2.3
0005h to
0006h
Restricted (see SSC-3)
0007h
INITIALIZATION COUNT
BINARY
7.4.2.2.4
0008h
VOLUME IDENTIFIER
ASCII
7.4.2.2.5
0009h to
0209h
Reserved
020Ah
DEVICE VENDOR/SERIAL NUMBER AT LAST LOAD
ASCII
7.4.2.2.6
020Bh
DEVICE VENDOR/SERIAL NUMBER AT LOAD-1
ASCII
7.4.2.2.6
020Ch
DEVICE VENDOR/SERIAL NUMBER AT LOAD-2
ASCII
7.4.2.2.6
020Dh
DEVICE VENDOR/SERIAL NUMBER AT LOAD-3
ASCII
7.4.2.2.6
020Eh to
021Fh
Reserved
0220h
TOTAL MBYTES WRITTEN IN MEDIUM LIFE
BINARY
7.4.2.2.7
0221h
TOTAL MBYTES READ IN MEDIUM LIFE
BINARY
7.4.2.2.7
0222h
TOTAL MBYTES WRITTEN IN CURRENT/LAST LOAD
BINARY
7.4.2.2.8
0223h
TOTAL MBYTES READ IN CURRENT/LAST LOAD
BINARY
7.4.2.2.8
0224h
LOGICAL POSITION OF FIRST ENCRYPTED BLOCK
BINARY
7.4.2.2.9
0225h
LOGICAL POSITION OF FIRST UNENCRYPTED
BLOCK AFTER THE FIRST ENCRYPTED BLOCK
BINARY
7.4.2.2.10
0226h to
033Fh
Reserved
0340h
MEDIUM USAGE HISTORY
BINARY
7.4.2.2.11
0341h
PARTITION USAGE HISTORY
BINARY
7.4.2.2.12
0342h to
03FFh
Reserved


expressed in increments of 1 048 576 bytes (e.g., a value of one means 1 048 576 bytes and a value of two
means 2 097 152 bytes).
7.4.2.2.2 LOAD COUNT: Indicates how many times this medium has been fully loaded. This attribute should
not be reset to zero by any action of the device server. The load counter is a saturating counter.
7.4.2.2.3 MAM SPACE REMAINING: Indicates the space currently available in the medium auxiliary memory.
The total medium auxiliary memory capacity is reported in the MAM CAPACITY attribute (see 7.4.2.3.4).
NOTE 46 - It may not always be possible to utilize all of the available space in a given medium auxiliary
memory implementation. Depending on the internal organization of the memory and the software that controls
it, fragmentation issues may mean that certain attribute sizes may not be fully accommodated as the medium
auxiliary memory nears its maximum capacity.
7.4.2.2.4 INITIALIZATION COUNT: Indicates the number of times that a device server has logically formatted
the medium. This value is cumulative over the life of the medium and shall not be reset to zero. The initial-
ization counter is a saturating counter.
7.4.2.2.5  VOLUME IDENTIFIER: Indicates the volume identifier (see SMC-3) of the medium. If the device
server supports this attribute but does not have access to the volume identifier, it shall report this attribute with
an attribute length value of zero.
7.4.2.2.6 DEVICE VENDOR/SERIAL NUMBER AT LAST LOAD, DEVICE VENDOR/SERIAL NUMBER AT
LOAD –1, DEVICE VENDOR/SERIAL NUMBER AT LOAD –2 and DEVICE VENDOR/SERIAL NUMBER AT
LOAD –3: Give a history of the last four device servers in which the medium has been loaded. The format of
the attributes is shown in table 442.
The T10 VENDOR IDENTIFICATION field shall be the same value returned in the Standard INQUIRY data (see
6.6.2).
The PRODUCT SERIAL NUMBER field contains ASCII data (see 4.3.1) that is a vendor specific serial number. If
the product serial number is not available, the PRODUCT SERIAL NUMBER field shall contain ASCII spaces (20h).
7.4.2.2.7 TOTAL MBYTES WRITTEN IN MEDIUM LIFE and TOTAL MBYTES READ IN MEDIUM LIFE:
Indicate the total number of data bytes that are transferred to or from the medium, after any data compression
has been applied, over the entire medium life. These values are cumulative and shall not be reset to zero.
These values are expressed in increments of 1 048 576 bytes (e.g., a value of one means 1 048 576 bytes
and a value of two means 2 097 152 bytes).
Table 442 — DEVICE VENDOR/SERIAL NUMBER attribute format
Bit
Byte
(MSB)
T10 VENDOR IDENTIFICATION
•••
(LSB)
(MSB)
PRODUCT SERIAL NUMBER
•••
(LSB)


7.4.2.2.8 TOTAL MBYTES WRITTEN IN CURRENT/LAST LOAD and TOTAL MBYTES READ IN CUR-
RENT/LAST LOAD:  Indicate the total number of data bytes that are transferred to or from the medium, after
any data compression has been applied, during the current load if the medium is currently loaded, or the last
load if the medium is currently unloaded. The device server should reset these attributes to zero when the
medium is loaded. These values are expressed in increments of 1 048 576 bytes (e.g., a value of one means
1 048 576 bytes and a value of two means 2 097 152 bytes).
7.4.2.2.9 LOGICAL POSITION OF FIRST ENCRYPTED BLOCK: Indicates the address of the first logical
block on the medium that contains encrypted data. If no logical block in the partition contains encrypted data,
then the attribute value shall be set to FFFF FFFF FFFF FFFFh. If it is unknown whether any logical block in
the partition contains encrypted data, then the attribute value shall be set to FFFF FFFF FFFF FFFEh.
7.4.2.2.10 LOGICAL POSITION OF FIRST UNENCRYPTED BLOCK AFTER THE FIRST ENCRYPTED
BLOCK: Indicates the address of the first logical block in the partition that contains unencrypted data and
follows the first logical block in the partition that contains encrypted data. If this attribute is supported, then the
LOGICAL POSITION OF FIRST ENCRYPTED BLOCK (see 7.4.2.2.9) attribute shall be supported.
The attribute value shall be set to FFFF FFFF FFFF FFFFh if the attribute value for the LOGICAL POSITION
OF FIRST ENCRYPTED BLOCK is set to:
a)
FFFF FFFF FFFF FFFFh; or
b)
any value other than FFFF FFFF FFFF FFFFh or FFFF FFFF FFFF FFFEh and no logical block in the
partition after the first encrypted logical block contains unencrypted data.
The attribute value shall be set to FFFF FFFF FFFF FFFEh if the attribute value for the LOGICAL POSITION
OF FIRST ENCRYPTED BLOCK is set to:
a)
FFFF FFFF FFFF FFFEh; or
b)
any value other than FFFF FFFF FFFF FFFFh or FFFF FFFF FFFF FFFEh and it is unknown
whether any logical block in the partition after the first encrypted logical block contains unencrypted
data.
7.4.2.2.11 MEDIUM USAGE HISTORY: Provides saturating counters (see table 443) for the entire medium.
The value in each field is the sum for all partitions. If a field is not used, it should be set to zero.
Table 443 — MEDIUM USAGE HISTORY attribute format (part 1 of 2)
Bit
Byte
(MSB)
CURRENT AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
CURRENT WRITE RETRIES COUNT
•••
(LSB)
(MSB)
CURRENT AMOUNT OF DATA READ
•••
(LSB)
(MSB)
CURRENT READ RETRIES COUNT
•••
(LSB)


The CURRENT AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium during this
load of the medium. This value is expressed in mebibytes (see 3.5.2).
The CURRENT WRITE RETRIES COUNT field indicates the total number of times a write retry occurred during this
load of the medium.1)
(MSB)
PREVIOUS AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
PREVIOUS WRITE RETRIES COUNT
•••
(LSB)
(MSB)
PREVIOUS AMOUNT OF DATA READ
•••
(LSB)
(MSB)
PREVIOUS READ RETRIES COUNT
•••
(LSB)
(MSB)
TOTAL AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
TOTAL WRITE RETRIES COUNT
•••
(LSB)
(MSB)
TOTAL AMOUNT OF DATA READ
•••
(LSB)
(MSB)
TOTAL READ RETRIES COUNT
•••
(LSB)
(MSB)
LOAD COUNT
•••
(LSB)
(MSB)
TOTAL CHANGE PARTITION COUNT
•••
(LSB)
(MSB)
TOTAL PARTITION INITIALIZE COUNT
•••
(LSB)
1) The definition of one retry as counted by this attribute field is not part of this standard. This count
should not be used to compare products because the products may define errors differently.
Table 443 — MEDIUM USAGE HISTORY attribute format (part 2 of 2)
Bit
Byte


The CURRENT AMOUNT OF DATA READ field indicates the amount of data read from the medium during this load
of the medium. This value is expressed in mebibytes (see 3.5.2).
The CURRENT READ RETRIES COUNT field indicates the number of times a read retry occurred during this load of
the medium.2)
The PREVIOUS AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium during the
previous load of the medium. This value is expressed in mebibytes (see 3.5.2).
The PREVIOUS WRITE RETRIES COUNT field indicates the total number of times a write retry occurred during the
previous load of the medium.2)
The PREVIOUS AMOUNT OF DATA READ field indicates the amount of data read from the medium during the
previous load of the medium. This value is expressed in mebibytes (see 3.5.2).
The PREVIOUS READ RETRIES COUNT field indicates the number of times a read retry occurred during the
previous load of the medium.2)
The TOTAL AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium since the last
medium format. This value is expressed in mebibytes (see 3.5.2).
The TOTAL WRITE RETRIES COUNT field indicates the total number of times a write retry occurred since the last
medium format.2)
The TOTAL AMOUNT OF DATA READ field indicates the amount of data read from the medium since the last
medium format. This value is expressed in mebibytes (see 3.5.2).
The TOTAL READ RETRIES COUNT field indicates the number of times a read retry occurred since the last
medium format.2)
The LOAD COUNT field indicates the number of loads since the last medium format. This count accumulates
over the life of the medium but it is reset to zero after a medium format.
The TOTAL CHANGE PARTITION COUNT field indicates the number of times that switches between partitions have
been performed on the medium. This count accumulates over the life of the medium but it is reset to zero after
a medium format.
The TOTAL PARTITION INITIALIZE COUNT field indicates number of times that any of the partitions on the medium
have been erased. This count accumulates over the life of the medium but it is reset to zero after a medium
format.
2) The definition of one retry as counted by this attribute field is not part of this standard. This count
should not be used to compare products because the products may define errors differently.


7.4.2.2.12 PARTITION USAGE HISTORY: Provides saturating counters (see table 444) for the partition
specified by the PARTITION NUMBER field in the CDB. If a field is not used, it should be set to zero.
Table 444 — PARTITION USAGE HISTORY attribute format (part 1 of 2)
Bit
Byte
(MSB)
CURRENT AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
CURRENT WRITE RETRIES COUNT
•••
(LSB)
(MSB)
CURRENT AMOUNT OF DATA READ
•••
(LSB)
(MSB)
CURRENT READ RETRIES COUNT
•••
(LSB)
(MSB)
PREVIOUS AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
PREVIOUS WRITE RETRIES COUNT
•••
(LSB)
(MSB)
PREVIOUS AMOUNT OF DATA READ
•••
(LSB)
(MSB)
PREVIOUS READ RETRIES COUNT
•••
(LSB)
(MSB)
TOTAL AMOUNT OF DATA WRITTEN
•••
(LSB)
(MSB)
TOTAL WRITE RETRIES COUNT
•••
(LSB)
(MSB)
TOTAL AMOUNT OF DATA READ
•••
(LSB)
(MSB)
TOTAL READ RETRIES COUNT
•••
(LSB)


The CURRENT AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium in the partition
specified by the PARTITION NUMBER field in the CDB during this load of the medium. This value is expressed in
mebibytes (see 3.5.2).
The CURRENT WRITE RETRIES COUNT field indicates the total number of times a write retry occurred in the
partition specified by the PARTITION NUMBER field in the CDB during this load of the medium.3)
The CURRENT AMOUNT OF DATA READ field indicates the amount of data read from the medium in the partition
specified by the PARTITION NUMBER field in the CDB during this load of the medium. This value is expressed
mebibytes (see 3.5.2).
The CURRENT READ RETRIES COUNT field indicates the number of times a read retry occurred in the partition
specified by the PARTITION NUMBER field in the CDB during this load of the medium.3)
The PREVIOUS AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium in the
partition specified by the PARTITION NUMBER field in the CDB during the previous load of the medium. This
value is expressed in mebibytes (see 3.5.2).
The PREVIOUS WRITE RETRIES COUNT field indicates the total number of times a write retry occurred in the
partition specified by the PARTITION NUMBER field in the CDB during the previous load of the medium.3)
The PREVIOUS AMOUNT OF DATA READ field indicates the amount of data read from the medium in the partition
specified by the PARTITION NUMBER field in the CDB during the previous load of the medium. This value is
expressed in mebibytes (see 3.5.2).
The PREVIOUS READ RETRIES COUNT field indicates the number of times a read retry occurred in the partition
specified by the PARTITION NUMBER field in the CDB during the previous load of the medium.3)
The TOTAL AMOUNT OF DATA WRITTEN field indicates the amount of data written to the medium in the partition
specified by the PARTITION NUMBER field in the CDB since the last medium format. This value is expressed in
mebibytes (see 3.5.2).
The TOTAL WRITE RETRIES COUNT field indicates the total number of times a write retry occurred in the partition
specified by the PARTITION NUMBER field in the CDB since the last medium format.3)
(MSB)
LOAD COUNT
•••
(LSB)
(MSB)
CHANGE PARTITION COUNT
•••
(LSB)
(MSB)
PARTITION INITIALIZE COUNT
•••
(LSB)
3) The definition of one retry as counted by this attribute field is not part of this standard. This count
should not be used to compare products because the products may define errors differently.
Table 444 — PARTITION USAGE HISTORY attribute format (part 2 of 2)
Bit
Byte


The TOTAL AMOUNT OF DATA READ field indicates the amount of data read from the medium in the partition
specified by the PARTITION NUMBER field in the CDB since the last medium format. This value is expressed in
mebibytes (see 3.5.2).
The TOTAL READ RETRIES COUNT field indicates the number of times a read retry occurred in the partition
specified by the PARTITION NUMBER field in the CDB since the last medium format.4)
The LOAD COUNT field indicates the number of loads in the partition specified by the PARTITION NUMBER field in
the CDB since the last medium format. This count accumulates over the life of the medium but it is reset to
zero after a medium format.
The TOTAL CHANGE PARTITION COUNT field indicates the number of times that switches to the partition specified
by the PARTITION NUMBER field in the CDB have been performed on the medium. This count accumulates over
the life of the medium but it is reset to zero after a medium format.
The TOTAL PARTITION INITIALIZE COUNT field indicates number of times that the partition specified by the
PARTITION NUMBER field in the CDB has been initialized. This count accumulates over the life of the medium
but it is reset to zero after a medium format.
7.4.2.3 Medium type attributes
Medium type attributes (see table 445) are stored in the medium auxiliary memory by the manufacturer. The
device server shall not alter medium type attributes. All supported medium type attributes shall have a status
of read only (see 5.7).
7.4.2.3.1 MEDIUM MANUFACTURER: Contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying
the vendor of the media. The medium manufacturer shall be a T10 vendor identification assigned by INCITS.
A list of assigned T10 vendor identifications is in Annex F and on the T10 web site (http://www.T10.org).
NOTE 47 - The T10 web site (http://www.t10.org) provides a convenient means to request an identification
code.
4) The definition of one retry as counted by this attribute field is not part of this standard. This count
should not be used to compare products because the products may define errors differently.
Table 445 — Medium type attributes
Attribute
Identifier
Name
Attribute
Length
(in bytes)
Format
Reference
0400h
MEDIUM MANUFACTURER
ASCII
7.4.2.3.1
0401h
MEDIUM SERIAL NUMBER
ASCII
7.4.2.3.2
0402h to 0405h
Restricted (see SSC-3)
0406h
MEDIUM MANUFACTURE DATE
ASCII
7.4.2.3.3
0407h
MAM CAPACITY
BINARY
7.4.2.3.4
0408h
MEDIUM TYPE
BINARY
7.4.2.3.5
0409h
MEDIUM TYPE INFORMATION
BINARY
7.4.2.3.5
040Ah
NUMERIC MEDIUM SERIAL NUMBER
unspecified
unspecified
7.4.2.3.6
040Bh to 07FFh
Reserved


7.4.2.3.2 MEDIUM SERIAL NUMBER: Contains the manufacturer’s serial number for the medium.
7.4.2.3.3 MEDIUM MANUFACTURE DATE: Contains the date of manufacture of the medium. The format is
YYYYMMDD (i.e., four numeric ASCII characters for the year followed by two numeric ASCII characters for
the month followed by two numeric ASCII characters for the day with no intervening spaces).
7.4.2.3.4 MAM CAPACITY: Is the total capacity of the medium auxiliary memory, in bytes, at manufacture
time. It does not indicate the available space of an unused medium auxiliary memory because some of the
medium auxiliary memory space may be reserved for device-specific use making it inaccessible to the appli-
cation client.
7.4.2.3.5 MEDIUM TYPE and MEDIUM TYPE INFORMATION: Give information about non-data media and
other types of media. The MEDIUM TYPE INFORMATION attribute is interpreted according to the type of
medium indicated by the MEDIUM TYPE (see table 446).
7.4.2.3.6 NUMERIC MEDIUM SERIAL NUMBER: Contains the manufacturer’s serial number for the medium
in a vendor specific format.
Table 446 — MEDIUM TYPE and MEDIUM TYPE INFORMATION attributes
MEDIUM TYPE
Description
MEDIUM TYPE INFORMATION
00h
Data medium
Reserved
01h
Cleaning medium
Maximum number of cleaning cycles permitted
02h to 7Fh
Reserved
Reserved
80h
Write-once medium
Reserved
81h to FFh
Reserved
Reserved


7.4.2.4 Host type attributes
Application clients may use the WRITE ATTRIBUTE and READ ATTRIBUTE commands to maintain the
attributes shown in table 447. All existent host type attributes shall have a status of read/write (see 5.7).
7.4.2.4.1 APPLICATION VENDOR: Contains eight bytes of left-aligned ASCII data (see 4.3.1) identifying the
manufacturer of the application client (e.g., class driver or backup program) that last sent a WRITE
ATTRIBUTE command to the device server while this medium auxiliary memory was accessible. The appli-
cation vendor shall be a T10 vendor identification assigned by INCITS. A list of assigned T10 vendor identifi-
cations is in Annex F and on the T10 web site (http://www.T10.org).
NOTE 48 - The T10 web site (http://www.t10.org) provides a convenient means to request an identification
code.
7.4.2.4.2 APPLICATION NAME: Contains the name of the application client.
7.4.2.4.3 APPLICATION VERSION: Contains the version of the application client.
7.4.2.4.4 USER MEDIUM TEXT LABEL: Is the user level identifier for the medium.
7.4.2.4.5 DATE & TIME LAST WRITTEN: Contains the time at which the application client last wrote to the
medium auxiliary memory. The format is YYYYMMDDHHMM (i.e., four numeric ASCII characters for the year
followed by two numeric ASCII characters for the month followed by two numeric ASCII characters for the day
followed by two numeric ASCII characters between 00 and 24 for the hour followed by two numeric ASCII
characters for the minute with no intervening spaces).
Table 447 — Host type attributes
Attribute
Identifier
Name
Attribute
Length
(in bytes)
Format
Reference
0800h
APPLICATION VENDOR
ASCII
7.4.2.4.1
0801h
APPLICATION NAME
ASCII
7.4.2.4.2
0802h
APPLICATION VERSION
ASCII
7.4.2.4.3
0803h
USER MEDIUM TEXT LABEL
TEXT
7.4.2.4.4
0804h
DATE AND TIME LAST WRITTEN
ASCII
7.4.2.4.5
0805h
TEXT LOCALIZATION IDENTIFIER
BINARY
7.4.2.4.6
0806h
BARCODE
ASCII
7.4.2.4.7
0807h
OWNING HOST TEXTUAL NAME
TEXT
7.4.2.4.8
0808h
MEDIA POOL
TEXT
7.4.2.4.9
0809h
PARTITION USER TEXT LABEL
ASCII
7.4.2.4.10
080Ah
LOAD/UNLOAD AT PARTITION
BINARY
7.4.2.4.11
080Bh
APPLICATION FORMAT VERSION
ASCII
7.4.2.4.12
080Ch
Restricted (see SSC-4)
080Dh to BFFh
Reserved


7.4.2.4.6 TEXT LOCALIZATION IDENTIFIER: Defines the character set (see table 448) used for attributes
with a TEXT format (see 7.4.1).
7.4.2.4.7 BARCODE: Is contents of a barcode associated with the medium in the medium auxiliary memory.
7.4.2.4.8 OWNING HOST TEXTUAL NAME: Indicates the host from which that USER MEDIUM TEXT
LABEL (see 7.4.2.4.4) originates.
7.4.2.4.9 MEDIA POOL: Indicates the media pool to which this medium belongs.
7.4.2.4.10 PARTITION USER TEXT LABEL: Is a user level identifier for the partition specified by the
PARTITION NUMBER field in the CDB.
7.4.2.4.11 LOAD/UNLOAD AT PARTITION: Indicates whether the media is capable of being loaded or
unloaded at the partition specified by the PARTITION NUMBER field in the CDB. If loads and unloads are enabled
for the specified partition, the value of this attribute shall be one. If loads and unloads are not enabled for the
specified partition, the value of this attribute shall be zero. All attribute values other than zero and one are
reserved. If LOAD/UNLOAD AT PARTITION is disabled, then loads and unloads are performed at the
beginning of the media instead of at the specified partition. If this attribute is in the nonexistent state (see 5.7),
then the default action shall be to load and unload at the beginning of media.
7.4.2.4.12 APPLICATION FORMAT VERSION: Indicates the version of the format being used by the appli-
cation that set this attribute.
Table 448 — TEXT LOCALIZATION IDENTIFIER attribute values
Value
Meaning
00h
No code specified (ASCII)
01h
ISO/IEC 8859-1 (Europe, Latin America)
02h
ISO/IEC 8859-2 (Eastern Europe)
03h
ISO/IEC 8859-3 (SE Europe/miscellaneous)
04h
ISO/IEC 8859-4 (Scandinavia/Baltic)
05h
ISO/IEC 8859-5 (Cyrillic)
06h
ISO/IEC 8859-6 (Arabic)
07h
ISO/IEC 8859-7 (Greek)
08h
ISO/IEC 8859-8 (Hebrew)
09h
ISO/IEC 8859-9 (Latin 5)
0Ah
ISO/IEC 8859-10 (Latin 6)
0Bh to 7Fh
Reserved
80h
ISO/IEC 10646-1 (UCS-2BE)
81h
ISO/IEC 10646-1 (UTF-8)
82h to FFh
Reserved


7.5 Mode parameters
7.5.1 Summary of mode page codes
The page code assignments for mode pages are summarized in table 449.
Table 449 — Summary of mode page codes
Mode page name
Page code
Subpage code
Reference
Control
0Ah
n/a a
7.5.8
Control Extension
0Ah
01h
7.5.9
Disconnect-Reconnect
02h
n/a a
7.5.10
Extended
15h
01h to FEh
7.5.11
Extended Device-Type Specific
16h
01h to FEh
7.5.12
Power Condition
1Ah
n/a a
7.5.13
Power Consumption
1Ah
01h
7.5.14
Protocol Specific Logical Unit
18h
n/a a
7.5.15
Protocol Specific Port
19h
n/a a
7.5.16
Restricted (see applicable protocol standard)
18h
01h to FEh
19h
01h to FEh
Restricted (see applicable command standard)
01h
00h to FEh
03h to 08h
00h to FEh
0Ah
F0h to FEh
0Bh to 14h
00h to FEh
1Ah
F0h to FEh
1Bh to 1Fh
00h to FEh
20h to 3Eh
00h to FEh
Return all pages
3Fh b
00h b
6.13 and 6.14
Return all pages and subpages
3Fh b
FFh b
6.13 and 6.14
Return all subpages
00h to 3Eh b
FFh b
6.13 and 6.14
Obsolete c
Vendor specific d
Reserved
All other codes
A numeric ordered listing of mode page and subpage codes is provided in E.6.
a Applicable only in the MODE SENSE command (see 6.13 and 6.14).
b The use of these page codes and subpage codes is described in table 198 (see 6.13).
c The following page codes are obsolete: 09h.
d Page code 00h is vendor specific and does not require a page format or a subpage code.


7.5.2 Mode page policies
Logical units shall share mode parameter header and block descriptor values across all I_T nexuses. I_T
nexus loss shall not affect mode parameter header, block descriptor, and mode page values.
Each logical unit shall maintain current values and saved values of each mode page based on any of the
policies listed in table 450. The mode page policy used for each mode page may be reported in the Mode
Page Policy VPD page (see 7.8.9).
After a logical unit reset, each mode parameter header, block descriptor, and mode page shall revert to saved
values if supported or default values if saved values are not supported.
7.5.3 Mode parameters overview
This subclause describes the mode parameter headers, block descriptors, and mode pages used with MODE
SELECT command (see 6.11 and 6.12) and MODE SENSE command (see 6.13 and 6.14) that are applicable
to all SCSI devices. Subpages are identical to mode pages except that they include a SUBPAGE CODE field that
further differentiates the mode page contents. Mode pages specific to each device type are described in the
command standard that applies to that device type.
7.5.4 Mode parameter list format
The mode parameter list shown in table 451 contains a header, followed by zero or more block descriptors,
followed by zero or more variable length mode pages. Parameter lists are defined for each device type.
Table 450 — Mode page policies
Mode page policy
Number of mode page copies
Shared
One copy of the mode page that is shared by all I_T nexuses.
Per target port
A separate copy of the mode page for each target port with
each copy shared by all initiator ports.
Per I_T nexus
A separate copy of the mode page for each I_T nexus
Table 451 — Mode parameter list
Bit
Byte
Mode parameter header
Block descriptor(s)
Mode page(s) or vendor specific (e.g., page code set to zero)


7.5.5 Mode parameter header formats
The mode parameter header that is used by the MODE SELECT(6) command (see 6.11) and the MODE
SENSE(6) command (see 6.13) is defined in table 452.
The mode parameter header that is used by the MODE SELECT(10) command (see 6.12) and the MODE
SENSE(10) command (see 6.14) is defined in table 453.
When using the MODE SENSE command, the MODE DATA LENGTH field indicates the length in bytes of the
following data that is available to be transferred. The mode data length does not include the number of bytes
in the MODE DATA LENGTH field. When using the MODE SELECT command, this field is reserved.
NOTE 49 - Logical units that support more than 256 bytes of block descriptors and mode pages should
implement ten-byte mode commands. The MODE DATA LENGTH field in the six-byte CDB header limits the
transferred data to 256 bytes.
The contents of the MEDIUM TYPE field are unique for each device type. Refer to the mode parameters
subclause of the specific device type command standard for definition of these values. Some device types
reserve this field.
The DEVICE-SPECIFIC PARAMETER field is unique for each device type. Refer to the mode parameters subclause
of the specific device type command standard for definition of this field.
If the Long LBA (LONGLBA) bit is set to zero, the mode parameter block descriptor(s), if any, are each eight
bytes long and have the format described in 7.5.6.1. If the LONGLBA bit is set to one, the mode parameter block
descriptor(s), if any, are each 16 bytes long and have a format described in a command standard.
Table 452 — Mode parameter header(6)
Bit
Byte
MODE DATA LENGTH
MEDIUM TYPE
DEVICE-SPECIFIC PARAMETER
BLOCK DESCRIPTOR LENGTH
Table 453 — Mode parameter header(10)
Bit
Byte
(MSB)
MODE DATA LENGTH
(LSB)
MEDIUM TYPE
DEVICE-SPECIFIC PARAMETER
Reserved
LONGLBA
Reserved
(MSB)
BLOCK DESCRIPTOR LENGTH
(LSB)


The BLOCK DESCRIPTOR LENGTH field indicates the length in bytes of all the block descriptors. It is equal to the
number of block descriptors times eight if the LONGLBA bit is set to zero or times sixteen if the LONGLBA bit is
set to one, and does not include the length of mode pages or vendor specific parameters (e.g., page code set
to zero), if any, that may follow the last block descriptor. A block descriptor length of zero indicates that no
block descriptors are included in the mode parameter list. This condition shall not be considered an error.
7.5.6 Mode parameter block descriptor formats
7.5.6.1 General block descriptor format
If the LONGLBA bit is set to zero (see 7.5.5), the mode parameter block descriptor format for all device types
except direct access block devices (see SBC-2) is shown in table 454.
Block descriptors specify some of the medium characteristics for all or part of a logical unit. Support for block
descriptors is optional. Each block descriptor contains a DENSITY CODE field, a NUMBER OF BLOCKS field, and a
BLOCK LENGTH field. Block descriptor values are always current (i.e., saving is not supported). Whenever any
block descriptor values are changed, the device server shall establish a unit attention condition (see SAM-5)
for the initiator port associated with every I_T nexus except the I_T nexus on which the MODE SELECT
command (see 6.11) was received, with the additional sense code set to MODE PARAMETERS CHANGED.
Command standards may place additional requirements on the general mode parameter block descriptor.
Requirements in the command standards that conflict with requirements defined in this subclause shall take
precedence over the requirements defined in this subclause.
The DENSITY CODE field is unique for each device type. Refer to the mode parameters subclause of the specific
device type command standard for definition of this field. Some device types reserve all or part of this field.
The NUMBER OF BLOCKS field specifies the number of logical blocks on the medium to which the DENSITY CODE
field and BLOCK LENGTH field apply. A value of zero indicates that all of the remaining logical blocks of the
logical unit shall have the medium characteristics specified.
If the number of logical blocks on the medium exceeds the maximum value that may be specified in the
NUMBER OF BLOCKS field, a value of FFFFFFh indicates that all of the remaining logical blocks of the logical unit
shall have the medium characteristics specified.
NOTES
Table 454 — General mode parameter block descriptor
Bit
Byte
DENSITY CODE
(MSB)
NUMBER OF BLOCKS
(LSB)
Reserved
(MSB)
BLOCK LENGTH
(LSB)


There may be implicit association between parameters defined in the mode pages and block descriptors.
In this case, the device server may change parameters not explicitly sent with the MODE SELECT
command. A subsequent MODE SENSE command may be used to detect these changes.
The number of remaining logical blocks may be unknown for some device types.
The BLOCK LENGTH field specifies the length in bytes of each logical block described by the block descriptor.
For sequential-access devices, a block length of zero indicates that the logical block size written to the
medium is specified by the TRANSFER LENGTH field in the CDB (see SSC-3).
7.5.7 Mode page and subpage formats and page codes
The page_0 mode page format is defined in table 455.
The sub_page mode page format is defined in table 456.
Each mode page contains a PS bit, an SPF bit, a PAGE CODE field, a PAGE LENGTH field, and a set of mode
parameters. The page codes are defined in this subclause and in the mode parameter subclauses in the
command standard for the specific device type. Each mode page with a SPF bit set to one contains a SUBPAGE
CODE field.
A SubPage Format (SPF) bit set to zero indicates that the page_0 mode page format is being used. A SPF bit
set to one indicates that the sub_page mode page format is being used.
When using the MODE SENSE command, a parameters saveable (PS) bit set to one indicates that the mode
page may be saved by the logical unit in a nonvolatile, vendor specific location. A PS bit set to zero indicates
that the device server is not able to save the supported parameters. When using the MODE SELECT
command, the PS bit is reserved.
Table 455 — Page_0 mode page format
Bit
Byte
PS
SPF (0b)
PAGE CODE
PAGE LENGTH (n-1)
Mode parameters
•••
n
Table 456 — Sub_page mode page format
Bit
Byte
PS
SPF (1b)
PAGE CODE
SUBPAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
Mode parameters
•••
n
