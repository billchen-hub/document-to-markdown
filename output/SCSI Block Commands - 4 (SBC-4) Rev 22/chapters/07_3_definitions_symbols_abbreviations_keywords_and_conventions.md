# 3 Definitions, symbols, abbreviations, keywords, and conventions Introduction

3 Definitions, symbols, abbreviations, keywords, and conventions Introduction
Table 1 shows the topics in clause 3 and a reference to the subclause where each topic is described.
3.1 Terms and Definitions
3.1.1 additional sense code
combination of the ADDITIONAL SENSE CODE field and the ADDITIONAL SENSE CODE QUALIFIER field in the sense
data
Note 1  to entry: See SPC-6.
3.1.2 advanced background operation
background operation that may impact device server response time to affected LBAs and may include
garbage collection operations
3.1.3 AND
Boolean arithmetic function (see 3.1.13) on two binary input values that results in an output value of one if
both of the input values are one or zero if either of the input values is zero
3.1.4 AND operation
performance of an AND (see 3.1.3) bitwise on two multiple-bit input values both having the same number of
bits
Note 1  to entry: An example of multiple-bit inputs is the current content of a logical block and the content
contained in the Data-Out Buffer having the same number of bytes.
3.1.5 anchored
logical block provisioning state of an LBA (see 4.7.1) in which physical capacity has been reserved for the
referenced logical block (see 4.7.4.7)
3.1.6 application client
object that is the source of SCSI commands
Note 1  to entry: See SAM-6.
3.1.7 automatic read reassignment
sequence after the device server detects a recovered read error during which the device server, without
intervention from an application client, performs a reassign operation on the LBA for which the error was
detected
Table 1 — Direct access block device type mode topics and references
Topic
Reference
Terms and Definitions
3.1
Symbols
3.2
Abbreviations
3.3
Keywords
3.4
Editorial conventions
3.5
Numeric conventions
3.6
State machine conventions
3.7


3.1.8 atomic write command
command that performs  one or more atomic write operations
Note 1  to entry: See 4.29.
3.1.9 atomic write operation
process by which a device server performs a write operation that is either completed in its entirety or has no
effects on stored logical block data
Note 1  to entry: See 4.29.
3.1.10 automatic write reassignment
sequence after the device server detects a recovered error or an unrecovered error during which the device
server, without intervention from an application client, performs a reassign operation on the LBA for which the
error was detected
3.1.11 background function
either a background scan operation (see 4.23) or a device specific background function (see 3.1.29)
3.1.12 bitmap buffer
temporary buffer within a device server (e.g., for one or more bytes of the result of an AND operation
(see 3.1.4) or an OR operation (see 3.1.61))
3.1.13 Boolean arithmetic function
function that produces an output from one or more inputs according to the rules of AND (see 3.1.3), XOR
(see 3.1.33), and OR (see 3.1.60)
3.1.14 byte
sequence of eight contiguous bits considered as a unit
3.1.15 cache
temporary data storage area that is capable of containing a subset of the logical block data stored by the
logical unit and is either volatile or non-volatile
3.1.16 check data
information contained within a redundancy group (see 3.1.83) that may allow lost or destroyed XOR-protected
data (see 3.1.120) to be recreated
3.1.17 command
request describing a unit of work to be performed by a device server
Note 1  to entry: See SAM-6.
3.1.18 command descriptor block (CDB)
structure used to communicate commands from an application client to a device server
Note 1  to entry: See SPC-6.
3.1.19 compare operation
process by which a device server compares two sets of data for equality
3.1.20 cyclic redundancy check (CRC)
error checking mechanism that checks data integrity by computing a polynomial algorithm based checksum
(see 4.21.4)


3.1.21 Data-In Buffer
buffer specified by the application client to receive data from the device server during the processing of a
command
Note 1  to entry: See SAM-6 and SPC-6.
3.1.22 Data-Out Buffer
buffer specified by the application client to supply data that is sent from the application client to the device
server during the processing of a command
Note 1  to entry: See SAM-6 and SPC-6.
3.1.23 deallocated
logical block provisioning state of an LBA (see 4.7.1) in which physical capacity has not been reserved for the
referenced logical block (see 4.7.4.6)
3.1.24 defect list
GLIST (see 4.13) or PLIST (see 4.13)
3.1.25 depopulate operation
process by which a SCSI device removes the capability of a storage element to store logical block data
Note 1  to entry: See 4.36.3.2.
3.1.26 depopulated
the condition of a physical element that has been affected by a depopulate operation
3.1.27 device managed zoned block device
device server that implements write pointer zones that are not sequential write required zones (see ZBC-2) in
ways that do not affect the inputs and outputs for any of the commands defined in this standard
3.1.28 device server
object within a logical unit (see 3.1.51) that processes SCSI commands according to the rules of command
management
Note 1  to entry: See SAM-6.
3.1.29 device specific background functions
SCSI target device specific functions that a SCSI target device may perform that have no specific association
with application client-initiated operations
Note 1  to entry: See SPC-6.
3.1.30 device type
device model implemented by the logical unit and indicated to the application client by the PERIPHERAL DEVICE
TYPE field of the standard INQUIRY data (see SPC-6)
3.1.31 direct access block device
device that is capable of containing data stored in logical blocks that each have a unique LBA (see 4.2)
3.1.32 error correcting code (ECC)
error checking mechanism that checks data integrity and enables some errors in the logical block data to be
corrected
3.1.33 exclusive-or (XOR)
boolean arithmetic function on two binary input values that results in an output value of one if one and only
one of the input values is one, or zero if both of the input values are either zero or one


3.1.34 extent
set of logical blocks occupying contiguous LBAs on a logical unit
3.1.35 field
group of one or more contiguous bits, a part of a larger structure (e.g., a CDB (see 3.1.18) or sense data (see
SPC-6))
3.1.36 format corrupt
vendor specific condition in which the device server may not be able to perform logical block access
commands
Note 1  to entry: See 4.10, 4.33, and 5.26.
3.1.37 format operation
process by which a device server initializes the medium in a logical unit
Note 1  to entry: See 4.10 and 4.33.
3.1.38 fully provisioned logical unit
logical unit that stores logical block data for every LBA and has assigned physical capacity for every LBA
Note 1  to entry: See 4.7.2.
3.1.39 garbage collection operation
process that prepares resources for future allocation to LBAs
3.1.40 grown defect list (GLIST)
list of physical blocks that the device server has detected as containing medium defects or that the application
client has specified as containing medium defects
Note 1  to entry: See 4.13.
3.1.41 hard reset
condition resulting from the events defined by SAM-6 during which the SCSI device performs the hard reset
operations described in SAM-6, this standard, and other applicable command standards (see table 34)
3.1.42 I_T nexus
relationship between a SCSI initiator port and a SCSI target port
Note 1  to entry: See SAM-6.
3.1.43 I_T nexus loss
condition resulting from the events defined by SAM-6 during which the SCSI device performs the I_T nexus
loss operations described in SAM-6, this standard, and other applicable command standards (see table 34)
3.1.44 LBA resource
resource used for storing logical block data
3.1.45 LBA mapping resource
resource used by a logical unit that supports logical block provisioning management
Note 1  to entry: An example of a mapping resource is a a physical block or a data structure associated with
tracking resource usage.
3.1.46 logical block
set of data bytes accessed and referenced as a unit
Note 1  to entry: See 4.5.


3.1.47 logical block access command
command that requests access to one or more logical blocks that may require access to the medium
Note 1  to entry: See 4.2.2.
3.1.48 logical block address (LBA)
value used to reference a logical block (see 4.5)
3.1.49 logical block data
user data and protection information, if any
3.1.50 logical block length
number of bytes of user data in a logical block (see 4.5)
3.1.51 logical unit
externally addressable entity within a SCSI target device (see 3.1.87) that implements a SCSI device model
Note 1  to entry: See SAM-6.
3.1.52 logical unit reset
condition resulting from the events defined by SAM-6 in which the logical unit performs the logical unit reset
operations described in SAM-6, this standard, and other applicable command standards (see table 34)
3.1.53 mapped
logical block provisioning state of an LBA (see 4.7.1) in which physical capacity has been assigned to the
referenced logical block (see 4.7.4.5)
3.1.54 medium
material that is not cache on which data is stored
Note 1  to entry: The plural of medium is media.
Note 2  to entry: An example of a medium in which data is stored is a magnetic disk.
3.1.55 medium defect
area of the medium that results in a recovered error or an unrecovered error when a read medium operation or
a write medium operation is performed
Note 1  to entry: See 4.13.
3.1.56 misaligned write command
write command with fields set as described in 4.6.2
3.1.57 non-advanced background operation
background operation that does not impact device server response time to affected LBAs and may include
garbage collection operations
3.1.58 non-volatile cache
cache that retains logical block data through any power cycle
3.1.59 non-volatile medium
medium that retains logical block data through any power cycle
3.1.60 OR
Boolean arithmetic function (see 3.1.13) on two binary input values that results in an output value of one if
either of the input values are one or zero if both of the input values are zero


3.1.61 OR operation
performance of an OR (see 3.1.60) bitwise on two multiple-bit input values both having the same number of
bits
Note 1  to entry: An example of multiple-bit input is the current content of a logical block and the content
contained in the Data-Out Buffer having the same number of bytes.
3.1.62 point in time ROD token
ROD token with a ROD type that is a point in time copy ROD
Note 1  to entry: See SPC-6.
3.1.63 physical block
set of data bytes accessed as a unit by the device server (see 4.6)
3.1.64 physical block length
number of bytes of logical block data in a physical block (see 4.6)
3.1.65 physical element
subcomponent of a SCSI device
3.1.66 power cycle
sequence of power being removed followed by power being applied to a SCSI device
3.1.67 power on
condition resulting from the events defined by SAM-6 during which a SCSI device performs the power on
operations described in SAM-6, this standard, and other applicable command standards (see table 34)
3.1.68 primary defect list (PLIST)
list of physical blocks containing medium defects that are considered permanent
Note 1  to entry: See 4.13.
3.1.69 protection information
group of fields at the end of each logical block or at specified intervals within each logical block that contain a
logical block guard, an application tag, and a reference tag
Note 1  to entry: See 4.21.
3.1.70 protection information interval
length of user data that occurs within a logical block before each protection information
3.1.71 provisioning initialization pattern
non-zero pattern that is the length of one logical block
3.1.72 pseudo read data
indeterminate logical block data
3.1.73 pseudo unrecovered error
simulated error (e.g., created by a WRITE LONG command (see 5.50 and 5.51)) for which a device server
reports that it is unable to read or write a logical block, regardless of whether the data on the medium is valid,
recoverable, or unrecoverable
3.1.74 pseudo unrecovered error with correction disabled
pseudo unrecovered error for which a device server performs no error recovery
Note 1  to entry: See 4.18.2.


3.1.75 read cache operation
process by which a device server reads logical blocks for one or more LBAs from cache as described in 4.15
3.1.76 read command
command that requests read operations
Note 1  to entry: See 4.2.2.
3.1.77 read medium operation
process by which a device server reads logical blocks for one or more LBAs from the medium using the
parameters specified in the Read-Write Error Recovery mode page (see 6.5.10)
3.1.78 read operation
process by which a device server performs operations as described in this standard
Note 1  to entry: Examples of read operations are read cache operations and read medium operations.
Note 2  to entry: See 4.2.3.
3.1.79 reassign
perform a reassign operation
3.1.80 reassign operation
operation during which the device server changes the assignment of an LBA from a specified physical block to
another physical block and adds the specified physical block to the GLIST
3.1.81 recovered error
error for which a device server is able to read or write a logical block within the recovery limits specified in the
Read-Write Error Recovery mode page (see 6.5.10) or the Verify Error Recovery mode page (see 6.5.11)
3.1.82 recovered read error
recovered error that occurs during a read medium operation
3.1.83 redundancy group
grouping of XOR-protected data (see 3.1.120) and associated check data (see 3.1.16) into a single type of
data redundancy (see SCC-2)
3.1.84 resource provisioned logical unit
logical unit that may or may not store logical block data for every LBA and that provides enough LBA mapping
resources (see 3.1.45) to map every LBA
Note 1  to entry: See 4.7.3.2.
3.1.85 sanitize operation
process by which a device server alters information on a logical unit such that recovery of previous logical
block data from the cache and the medium is not possible
Note 1  to entry: See 4.11.
3.1.86 scattered write command
command that requests write operations to LBA ranges that may not be contiguous
3.1.87 SCSI target device
SCSI device containing logical units and SCSI target ports that receives device service requests and task
management requests for processing and sends device service responses and task management responses
to SCSI initiator devices
Note 1  to entry: See SAM-6.


3.1.88 sense data
data describing an error, exceptional condition, or completion information
Note 1  to entry: See SPC-6.
3.1.89 sense key
contents of the SENSE KEY field in the sense data
Note 1  to entry: See SAM-6.
3.1.90 status
one byte of response information that contains a coded value defined in SAM-6, transferred from a device
server to an application client upon completion of each command
Note 1  to entry: See SAM-6.
3.1.91 stopped power condition
power condition in which a device server terminates TEST UNIT READY commands and logical block access
commands
Note 1  to entry: See 4.20.4.
3.1.92 storage element
physical element that provides non-volatile storage for an associated group of logical blocks
Note 1  to entry: See 4.36.
3.1.93 stream block
stream granularity size (see 6.6.5) area of physical media that is able to contain logical block data
3.1.94 stream identifier
identifier supplied by the device server and used by the application client to identify a stream
Note 1  to entry: See 4.32.
3.1.95 synchronize cache operation
process by which a device server synchronizes logical blocks within the volatile cache with the non-volatile
cache or the medium
3.1.96 thin provisioned logical unit
logical unit that may or may not store logical block data for every LBA and that may or may not provide enough
LBA mapping resources (see 3.1.45) to map every LBA
Note 1  to entry: See 4.7.3.3.
3.1.97 threshold set
set of two or more logical blocks used for tracking logical block provisioning thresholds
Note 1  to entry: See 4.7.3.7.
3.1.98 threshold set size
number of LBAs in a threshold set
Note 1  to entry: See 4.7.3.7.
3.1.99 token
representation of a collection of data
Note 1  to entry: See SPC-6.


3.1.100 truncate operation
process by which a device server reduces the logical unit’s capacity
Note 1  to entry: See 4.36.3.3.
3.1.101 unit attention condition
asynchronous status information that a logical unit establishes to report to the initiator ports associated with
one or more I_T nexuses
Note 1  to entry: See SAM-6.
3.1.102 unmap command
command that requests an unmap operation
Note 1  to entry: See 4.2.2.
3.1.103 unmap operation
process by which a device server either deallocates or anchors a single LBA
Note 1  to entry: See 4.2.3 and 4.7.3.4.
3.1.104 unmapped
logical block provisioning state of an LBA (see 4.7.1) in which the LBA is either anchored or deallocated
3.1.105 unrecovered error
error for which a device server is unable to read a logical block or write a logical block within the recovery
limits specified in the Read-Write Error Recovery mode page (see 6.5.10) and/or the Verify Error Recovery
mode page (see 6.5.11)
3.1.106 unrecovered read error
unrecovered error that occurs during a read medium operation
3.1.107 unrecovered write error
unrecovered error that occurs during a write medium operation
3.1.108 user data
data contained in logical blocks that is accessible by an application client and is neither protection information
nor other information that may not be accessible to the application client
3.1.109 user data segment
contiguous sequence of logical blocks
Note 1  to entry: See 4.26.
3.1.110 verify command
command that requests verify operations
Note 1  to entry: See 4.2.2.
3.1.111 verify medium operation
process by which a device server reads logical blocks for one or more LBAs from the medium using the
parameters specified in the Verify Error Recovery mode page (see 6.5.11)
3.1.112 verify operation
process by which the device server performs operations as described in this standard
Note 1  to entry: An example of a verify operation is a verify medium operation.
Note 2  to entry: See 4.2.3.


3.1.113 volatile cache
cache that does not retain logical block data between power cycles
3.1.114 volatile medium
medium that does not retain logical block data between power cycles
Note 1  to entry: An example of volatile medium is a silicon memory device that loses data written to it if device
power is lost.
3.1.115 write cache operation
process by which a device server writes logical blocks for one or more LBAs to the cache (see 4.7.1)
3.1.116 write command
command that requests write operations
Note 1  to entry: See 4.2.2.
3.1.117 write medium operation
process by which a device server writes logical blocks for one or more LBAs to the medium using the
parameters specified in the Read-Write Error Recovery mode page (see 6.5.10)
3.1.118 write operation
process by which a device server performs operations as described in this standard
Note 1  to entry: See 4.2.3.
3.1.119 XOR operation
processing of an XOR bitwise on two identical-sized multiple-bit input values
Note 1  to entry: An example of multiple-bit inputs is the current value of a logical block and the new value for
that logical block.
3.1.120 XOR-protected data
logical blocks (i.e., including logical block data) that are part of a redundancy group
3.1.121 zoned block device
block device based on this standard that implements one or more of the models defined in ZBC-2


3.2 Symbols
Symbols used in this standard include:
3.3 Abbreviations
Abbreviations used in this standard include:
Symbol
Meaning
+
plus
–
minus
×
multiplied by
÷
divided by
=
equals

not equal
<
less than
>
greater than
Abbreviation
Meaning
CDB
command descriptor block (see 3.1.18)
CRC
cyclic redundancy check (see 3.1.20)
ECC
error correcting code (see 3.1.32)
GLIST
grown defect list (see 3.1.40)
LBA
logical block address (see 3.1.48)
LBM
Logical Block Markup (see 6.8)
LBP
logical block provisioning (see 4.7.4)
LSB
least significant bit
LUN
logical unit number
M
implementation is mandatory
MMC-6
SCSI Multimedia Commands - 6 (see clause 2)
MSB
most significant bit
O
implementation is optional
PLIST
primary defect list (see 3.1.68)
n/a
not applicable
ROD
representation of data (see SPC-6)
SAM-6
SCSI Architecture Model - 6 (see clause 2)
SCSI
Small Computer System Interface family of standards
SCC-2
SCSI-3 Controller Commands - 2 (see clause 2)
SES-3
SCSI Enclosure Services - 3 (see clause 2)
SPC-6
SCSI Primary Commands - 6 (see clause 2)
SPL-5
SAS Protocol Layer-5 (see clause 2)
VPD
Vital product data (see 6.6)
XOR
exclusive-or (see 3.1.33)
ZBC-2
Zoned Block Commands - 2 (see clause 2)


3.4 Keywords
3.4.1 invalid
keyword used to describe an illegal or unsupported bit, byte, word, field or code value
Note 1  to entry: Receipt of an invalid bit, byte, word, field or code value shall be reported as an error.
3.4.2 mandatory
keyword indicating an item that is required to be implemented as defined in this standard
3.4.3 may
keyword that indicates flexibility of choice with no implied preference
Note 1  to entry: “May” is equivalent to “may or may not”.
3.4.4 may not
keywords that indicate flexibility of choice with no implied preference
Note 1  to entry: “May not” is equivalent to “may or may not”.
3.4.5 obsolete
keyword indicating that an item was defined in prior SCSI standards but has been removed from this standard
3.4.6 optional
keyword that describes features that are not required to be implemented by this standard; however, if any
optional feature defined in this standard is implemented, then it shall be implemented as defined in this
standard
3.4.7 prohibited
keyword used to describe a feature, function, or coded value that is defined in a non-SCSI standard (i.e., a
standard that is not a member of the SCSI family of standards) to which this standard makes a normative
reference where the use of said feature, function, or coded value is not allowed for implementations of this
standard
3.4.8 reserved
keyword referring to bits, bytes, words, fields and code values that are set aside for future standardization
Note 1  to entry: A reserved bit, byte, word or field shall be set to zero, or in accordance with a future
extension to this standard.
Note 2  to entry: Recipients are not required to check reserved bits, bytes, words or fields for zero values.
Note 3  to entry: Receipt of reserved code values in defined fields shall be reported as an error.
3.4.9 restricted
keyword referring to bits, bytes, words, and fields that are set aside for other identified standardization
purposes
Note 1  to entry: A restricted bit, byte, word, or field shall be treated as a reserved bit, byte, word or field in the
context where the restricted designation appears.
3.4.10 shall
keyword indicating a mandatory requirement
Note 1  to entry: Designers are required to implement all such mandatory requirements to ensure
interoperability with other products that conform to this standard.
3.4.11 should
keyword indicating flexibility of choice with a strongly preferred alternative
Note 1  to entry: “Should” is equivalent to the phrase “it is strongly recommended”.


3.4.12 vendor specific
something (e.g., a bit, field, code value) that is not defined by this standard
Note 1  to entry: Specification of the referenced item is determined by the SCSI device vendor and may be
used differently in various implementations.
3.5 Editorial conventions
Certain words and terms used in this standard have a specific meaning beyond the normal English meaning.
These words and terms are defined either in 3.5 or in the text where they first appear.
Normal case is used for words having the normal English meaning.
Upper case is used when referring to names of commands, status codes, sense keys, and additional sense
codes (e.g., REQUEST SENSE command).
If there is more than one CDB length for a particular command (e.g., ORWRITE (16) and ORWRITE (32)), and
the name of the command is used in a sentence without any CDB length descriptor (e.g., ORWRITE), then the
condition described in the sentence applies to all CDB lengths for that command.
Names of fields and state variables are in small uppercase (e.g. NAME). When a field or state variable name
contains acronyms, uppercase letters may also be used for readability (e.g., the LOGERR bit). Normal case is
used when the contents of a field or state variable are being discussed. Fields or state variables containing
only one bit are usually referred to as the NAME bit instead of the NAME field.
Lists sequenced by lowercase or uppercase letters show no ordering relationship between the listed items.
EXAMPLE 1 - The following list shows no relationship between the listed items:
a)
red (i.e., one of the following colors):
A)
crimson: or
B)
amber;
b)
blue; or
c)
green.
Lists sequenced by numbers show an ordering relationship between the listed items.
EXAMPLE 2 -The following list shows an ordered relationship between the named items:
1)
top;
2)
middle; and
3)
bottom.
Lists are associated with an introductory paragraph or phrase, and are numbered relative to that paragraph or
phrase (i.e., all lists begin with an a) or 1) entry).
In the event of conflicting information the precedence for requirements defined in this standard is:
1)
text;
2)
tables; then
3)
figures.
Tables show data format and values. Not all tables or figures are fully described in the text.
Notes and examples do not constitute any requirements for implementers, and notes are numbered
consecutively throughout this standard.
3.6 Numeric and character conventions
3.6.1 Numeric conventions
A binary number is represented in this standard by any sequence of digits comprised of only the Arabic
numerals 0 and 1 immediately followed by a lower-case b (e.g., 0101b). Underscores are included between
characters in binary number representations to increase readability or delineate field boundaries (e.g.,
0_0101_1010b).


A hexadecimal number is represented in this standard by any sequence of digits comprised of only the Arabic
numerals 0 to 9 and/or the upper-case English letters A to F immediately followed by a lower-case h (e.g.,
FA23h). Underscores are included in hexadecimal number representations to increase readability or delineate
field boundaries (e.g., B_FD8C_FA23h).
A decimal number is represented in this standard by any sequence of digits comprised of only the Arabic
numerals 0 to 9 not immediately followed by a lower-case b or lower-case h (e.g., 25).
A range of numeric values is represented in this standard in the form “a to z”, where a is the first value
included in the range, all values between a and z are included in the range, and z is the last value included in
the range (e.g., the representation “0h to 3h” includes the values 0h, 1h, 2h, and 3h).
This standard uses the following conventions for representing decimal numbers:
a)
the decimal separator (i.e., separating the integer and fractional portions of the number) is a period;
b)
the thousands separator (i.e., separating groups of three digits in a portion of the number) is a space;
and
c)
the thousands separator is used in both the integer portion and the fraction portion of a number.
Table 2 shows some examples of decimal numbers represented using various conventions.
A decimal number represented in this standard with an overline over one or more digits following the decimal
point is a number where the overlined digits are infinitely repeating (e.g., 666.6 means 666.666 666... or
666 2/3, and 12.142 857 means 12.142 857 142 857... or 12 1/7).
3.6.2 Units of measure
This standard represents values using both decimal units of measure and binary units of measure. Values are
represented by the following formats:
a)
for values based on decimal units of measure:
1)
numerical value (e.g., 100);
2)
space;
3)
prefix symbol and unit:
1)
decimal prefix symbol (e.g., M) (see table 3); and
2)
unit abbreviation;
and
b)
for values based on binary units of measure:
1)
numerical value (e.g., 1 024);
2)
space;
3)
prefix symbol and unit:
1)
binary prefix symbol (e.g., Gi) (see table 3); and
2)
unit abbreviation.
Table 3 compares the prefix, symbols, and power of the binary and decimal units.
Table 2 — Numbering convention examples
ISO/IEC
United States
This standard
0,6
0.6
0.6
3,141 592 65
3.14159265
3.141 592 65
1 000
1,000
1 000
1 323 462,95
1,323,462.95
1 323 462.95


3.7 State machine conventions
Figure 1 shows how state machines are described in this standard.
Figure 1 — Example state machine figure
The state machine figure is followed by subclauses describing the states and state transitions.
Each state and state transition is described in the list with particular attention to the conditions that cause the
transition to occur and special conditions related to the transition.
A system specified in this manner has the following properties:
a)
time elapses only within discrete states; and
b)
state transitions are logically instantaneous.
Table 3 — Comparison of decimal prefixes and binary prefixes
Decimal
Binary
Prefix name
Prefix symbol
Power
(base-10)
Prefix name
Prefix symbol
Power
(base-2)
kilo
k
kibi
Ki
mega
M
mebi
Mi
giga
G
gibi
Gi
tera
T
tebi
Ti
peta
P
pebi
Pi
exa
E
exbi
Ei
zetta
Z
zebi
Zi
yotta
Y
yobi
Yi
State 0
S1: State 1
S0: State 0
State1
State 0
Transition destination labels


4 Direct access block device type model
4.1 Direct access block device type model introduction
Table 4 shows the topics in clause 4 and a reference to the subclause where each topic is described.
Table 4 — Direct access block device type model topics  (part 1 of 2)
Topic
Reference
Direct access block device type model overview
4.2
Media examples
4.3
Removable media
4.4
Logical blocks
4.5
Physical blocks
4.6
Logical block provisioning
4.7
Data de-duplication
4.8
Ready state
4.9
Initialization
4.10
Sanitize operations
4.11
Write protection
4.12
Medium defects
4.13
Write and unmap failures
4.14
Caches
4.15
Implicit HEAD OF QUEUE command processing
4.16
Reservations
4.17
Error reporting
4.18
Rebuild assist mode
4.19
START STOP UNIT and power conditions
4.20
Protection information model
4.21
Grouping function
4.22
Background scan operations
4.23
Deferred microcode activation
4.24
Model for uninterrupted sequences on LBA ranges
4.25
Referrals
4.26


4.2 Direct access block device type model
4.2.1 Direct access block device type model overview
SCSI devices that conform to this standard are referred to as direct access block devices (e.g., hard disk
drives, removable rigid disks, and solid state drives).
This standard is intended to be used in conjunction with SAM-6, SPC-6, SCC-2, and SES-3.
Direct access block devices store data in logical blocks for later retrieval.
Logical blocks are stored by a process that causes localized changes or transitions within a medium. The
changes made to the medium to store the logical blocks may be volatile (i.e., not retained through power
cycles) or non-volatile (i.e., retained through power cycles).
4.2.2 Logical block access command types
The following are logical block access command types:
a)
read commands;
b)
unmap commands;
c)
verify commands;
d)
write commands; and
e)
other commands (e.g., a FORMAT UNIT command or a SANITIZE command).
See table 34 for a list of commands for direct access block devices, including the logical block access
command type. Some commands may be more than one type of logical block access command (e.g., a
COMPARE AND WRITE command is both a read command and a write command).
4.2.3 Logical block access operation types
Each named command type (see 4.2.2) is processed by performing one or more of the following:
a)
read operations;
b)
unmap operations;
c)
verify operations; and
d)
write operations.
ORWRITE commands
4.27
Block device ROD token operations
4.28
Atomic Writes
4.29
IO Advice Hints
4.30
Background operation control
4.31
Stream control
4.32
Format operations
4.33
Transfer limits
4.34
Scattered writes
4.35
Storage element depopulation and restoration
4.36
Table 4 — Direct access block device type model topics  (part 2 of 2)
Topic
Reference


A device server that supports optional features (e.g., caches (see 4.15)) may be required to support additional
requirements (e.g., cache coherency, LBA mapping resource allocations) that are related to those features for
specific operations (e.g., read operations, write operations).
In a device server that does not support any optional features:
a)
any read operation causes only read medium operations to be performed;
b)
any verify operation causes only verify medium operations to be performed; and
c)
any write operation causes only write medium operations to be performed.
The requirements for any optional feature (e.g., caches) may include additional requirements for the
operations described in this subclause.
If an optional feature (e.g., caches) defines requirements for read operations, then the device server shall
support those requirements for both verify operations and read operations.
4.3 Media examples
4.3.1 Media examples overview
Examples of types of media used by the direct access block device are:
a)
a rotating medium (see 4.3.2); and
b)
a memory medium (see 4.3.3).
Other types of media are possible.
4.3.2 Rotating media
A rotating medium is one or more spinning disks, each coated with a magnetic material that allows flux
changes to be induced and recorded. An actuator positions a read-write head radially across the spinning
disk, allowing the device to randomly read or write the information at any radial position. Data is stored by
using the write portion of the head to record flux changes and the recorded data is read by using the read
portion of the head.
The circular path followed by the read-write head at a particular radius is called a track. A track is divided into
sectors each containing blocks of stored data. If there is more than one disk spinning on a single axis and the
actuator has a read-write head to access each of the disk surfaces, then the collection of tracks at a particular
radius is called a cylinder.
A logical block is stored in one or more sectors, or a sector may store more than one logical block. Sectors
may also contain information for accessing, synchronizing, and protecting the integrity of the logical blocks.
A rotating medium direct access block device is ready if:
a)
the disks are rotating at the correct speed; and
b)
the read-write circuitry is powered and ready to access the data.
A START STOP UNIT command (see 5.31) may be required to bring the logical unit to the ready state.
The rotating medium in a direct access block device is non-volatile.
4.3.3 Memory media
A memory medium is solid state, random access memory (RAM) (e.g., static RAM (SRAM), dynamic RAM
(DRAM), magnetoresistive RAM (MRAM), ferroelectric RAM (FeRAM), or flash memory).
A memory medium direct access block device may be ready after power on and may not require a START
STOP UNIT command (see 5.31) to bring the logical unit to a ready state.


These logical units may be nonmechanical, and logical blocks may be accessed with similar access times
regardless of their location on the medium. Memory medium direct access block devices may store less data
than disks or tapes and may be volatile.
A memory medium may be volatile (e.g., SRAM or DRAM) or non-volatile (e.g., SRAM or DRAM with battery
backup, MRAM, FeRAM, or flash memory).
4.4 Removable media
The medium may be removable or non-removable. A removable medium may be contained within a cartridge
or jacket to prevent damage to the recording surfaces.
A removable medium has an attribute of being mounted or demounted on a suitable transport mechanism in a
direct access block device. A removable medium is mounted when the direct access block device is capable
of accessing its medium (e.g., performing read medium operations and write medium operations). A
removable medium is demounted at any other time (e.g., during loading, unloading, or storage).
An application client may check whether a removable medium is mounted by sending a TEST UNIT READY
command (see SPC-6). A direct access block device containing a removable medium may not be accessible
for read operations, unmap operations, and write operations until it receives a START STOP UNIT command
with the START bit set to one (see 5.31).
If a direct access block device implements cache, either volatile or non-volatile, then the device server
ensures that all logical blocks on the medium contain the most recent logical block data prior to permitting
demounting of the removable medium.
If the medium in a direct access block device is removable, and the medium is removed, then the device
server shall establish a unit attention condition with the additional sense code set to the appropriate value
(e.g., MEDIUM NOT PRESENT). The PREVENT ALLOW MEDIUM REMOVAL command (see 5.15) allows
an application client to restrict the demounting of the removable medium.
If an application client sends a START STOP UNIT command to request that the removable medium to be
ejected and the direct access block device is prevented from demounting the medium by a previous
PREVENT ALLOW MEDIUM REMOVAL command, then the START STOP UNIT command is terminated by
the device server.
4.5 Logical blocks
Logical blocks are stored on the medium. Logical blocks:
a)
contain logical block data that contains:
A) user data; and
B) protection information, if any;
and
b)
may contain additional information (e.g., an ECC which may be used for medium defect management
(see 4.13)), which may not be accessible to the application client.
The number of bytes of user data contained in each logical block is the logical block length. The logical block
length is greater than or equal to one byte and should be an even number of bytes (e.g., 512 bytes, 520 bytes,
4 096 bytes, or 4 104 bytes). The logical block length does not include the length of protection information, if
any, and additional information, if any, that are contained in the logical block. The logical block length is the
same for all logical blocks in the logical unit. The LOGICAL BLOCK LENGTH IN BYTES field (see 5.20.2) and the
READ CAPACITY (16) parameter data (see 5.21.2) indicates the logical block length. The FORMAT UNIT
command (see 5.4) and the mode parameter block descriptor (see 6.5.2) are used together by an application
client to change the logical block length in direct access block devices that support changeable logical block
lengths.
