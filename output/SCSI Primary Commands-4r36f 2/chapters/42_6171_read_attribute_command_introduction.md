# 6.17.1 READ ATTRIBUTE command introduction

6.17 READ ATTRIBUTE command
6.17.1 READ ATTRIBUTE command introduction
The READ ATTRIBUTE command (see table 218) allows an application client to read attribute information
from medium auxiliary memory.
The OPERATION CODE field is defined in 4.2.5.1 and shall be set as shown in table 218 for the READ
ATTRIBUTE command.
If the medium is present but the medium auxiliary memory is not accessible, the READ ATTRIBUTE
command shall be terminated with CHECK CONDITION status, with the sense key set to MEDIUM ERROR,
and the additional sense code set to LOGICAL UNIT NOT READY, AUXILIARY MEMORY NOT ACCES-
SIBLE.
If the medium auxiliary memory is not operational, the READ ATTRIBUTE command shall be terminated with
CHECK CONDITION status, with the sense key set to MEDIUM ERROR, and the additional sense code set to
AUXILIARY MEMORY READ ERROR.
Table 218 — READ ATTRIBUTE command
Bit
Byte
OPERATION CODE (8Ch)
Reserved
SERVICE ACTION
Restricted (see SMC-3)

•••
LOGICAL VOLUME NUMBER
Reserved
PARTITION NUMBER
(MSB)
FIRST ATTRIBUTE IDENTIFIER
(LSB)
(MSB)
ALLOCATION LENGTH

•••
(LSB)
Reserved
CACHE
CONTROL


The SERVICE ACTION field is defined in 4.2.5.2. The service action codes defined for the READ ATTRIBUTE
command are shown in table 219.
The LOGICAL VOLUME NUMBER field specifies a logical volume (e.g., the medium auxiliary memory storage for
one side of a double sided medium) within the medium auxiliary memory. The number of logical volumes of
the medium auxiliary memory shall equal that of the attached medium. If the medium only has a single logical
volume, then its logical volume number shall be zero.
The PARTITION NUMBER field specifies a partition (see SSC-3) within a logical volume. The number of partitions
of the medium auxiliary memory shall equal that of the attached medium. If the medium only has a single
partition, then its partition number shall be zero.
If the combination of logical volume number and partition number is not valid, the command shall be termi-
nated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN CDB.
The FIRST ATTRIBUTE IDENTIFIER field specifies the attribute identifier of the first attribute to be returned. If the
specified attribute is in the unsupported state or nonexistent state (see 5.7), the READ ATTRIBUTE command
shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the
additional sense code set to INVALID FIELD IN CDB.
The ALLOCATION LENGTH field is defined in 4.2.5.6.
A CACHE bit set to one specifies that, if medium is not present, then the device server may report attribute
information cached from the most recently mounted medium. A CACHE bit set to zero specifies that the device
server shall not report attribute information cached from the most recently mounted medium. The READ
ATTRIBUTE command shall be terminated with CHECK CONDITION status, with the sense key set to NOT
READY, and the additional sense code set to MEDIUM NOT PRESENT if the CACHE bit set to:
a)
zero, and medium auxiliary memory is not accessible because there is no medium present; or
b)
one, and the device server does not have a cache of attribute information read from the most recently
mounted medium.
If medium is mounted and the CACHE bit is supported, then attribute information shall be reported for the
mounted medium and the CACHE bit shall be ignored.
Table 219 — READ ATTRIBUTE service action codes
Code
Name
Description
Reference
00h
ATTRIBUTE VALUES
Return attribute values.
6.17.2
01h
ATTRIBUTE LIST
Return a list of available attribute identifiers, identifi-
ers that are in the read only state or in the
read/write state (see 5.7).
6.17.3
02h
LOGICAL VOLUME LIST
Return a list of known logical volume numbers.
6.17.4
03h
PARTITION LIST
Return a list of known partition numbers.
6.17.5
04h
Restricted
SMC-3
05h
SUPPORTED ATTRIBUTES
Return a list of supported attribute identifiers, identi-
fiers that are in the read only state, in the read/write
state, or in the nonexistent state (see 5.7).
6.17.6
06h to
1Fh
Reserved


Attribute information from cache may or may not be the complete set of attribute information from the most
recently mounted medium. The device server shall clear cached attribute information at the start of a medium
load.
The CONTROL byte is defined in SAM-5.
The format of parameter data returned by the READ ATTRIBUTE command depends on the service action
specified.
6.17.2 ATTRIBUTE VALUES service action
The READ ATTRIBUTE command with ATTRIBUTE VALUES service action returns parameter data
containing the attributes that are in the read state or read/write state (see 5.7) specified by the PARTITION
NUMBER, LOGICAL VOLUME NUMBER, and FIRST ATTRIBUTE IDENTIFIER fields in the CDB. The returned parameter
data shall contain the requested attributes in ascending numerical order by attribute identifier value and in the
format shown in table 220.
The AVAILABLE DATA field shall contain the number of bytes of attribute information in the parameter list. The
contents of the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
The format of the attributes is described in 7.4.1.
Table 220 — READ ATTRIBUTE with ATTRIBUTE VALUES service action parameter list format
Bit
Byte
(MSB)
AVAILABLE DATA (n-3)
•••
 (LSB)
Attribute(s)
Attribute 0 (see 7.4.1)
•••
•••
Attribute x (see 7.4.1)
•••
n


6.17.3 ATTRIBUTE LIST service action
The READ ATTRIBUTE command with ATTRIBUTE LIST service action returns parameter data containing
the attribute identifiers for the attributes that are in the read only state or in the read/write state (see 5.7) in the
specified partition and volume number. The contents of FIRST ATTRIBUTE IDENTIFIER field in the CDB shall be
ignored. The returned parameter data shall contain the requested attribute identifiers in ascending numerical
order by attribute identifier value and in the format shown in table 221.
The AVAILABLE DATA field shall contain the number of bytes of attribute identifiers in the parameter list. The
contents of the AVAILABLE DATA field are not altered based on the allocation length (see 4.2.5.6).
An ATTRIBUTE IDENTIFIER field is returned for each attribute that is in the read only state or in the read/write
state (see 5.7) in the specified partition and volume number. See 7.4.2 for a description of the attribute
identifier values.
6.17.4 LOGICAL VOLUME LIST service action
The READ ATTRIBUTE command with LOGICAL VOLUME LIST service action returns parameter data (see
table 222) identifying the supported number of logical volumes. The contents of LOGICAL VOLUME NUMBER,
PARTITION NUMBER, and FIRST ATTRIBUTE IDENTIFIER fields in the CDB shall be ignored.
The AVAILABLE DATA field shall contain two. The contents of the AVAILABLE DATA field are not altered based on
the allocation length (see 4.2.5.6).
Table 221 — READ ATTRIBUTE with ATTRIBUTE LIST service action parameter list format
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
Table 222 — READ ATTRIBUTE with LOGICAL VOLUME LIST service action parameter list format
Bit
Byte
(MSB)
AVAILABLE DATA (0002h)
 (LSB)
FIRST LOGICAL VOLUME NUMBER
NUMBER OF LOGICAL VOLUMES AVAILABLE


The FIRST LOGICAL VOLUME NUMBER field indicates the first volume available. Logical volume numbering should
start at zero.
The NUMBER OF LOGICAL VOLUMES AVAILABLE field indicates the number of volumes available.
6.17.5 PARTITION LIST service action
The READ ATTRIBUTE command with PARTITION LIST service action returns parameter data (see table
223) identifying the number of partitions supported in the specified logical volume number. The contents of
PARTITION NUMBER and FIRST ATTRIBUTE IDENTIFIER fields in the CDB shall be ignored.
The AVAILABLE DATA field shall contain two. The contents of the AVAILABLE DATA field are not altered based on
the allocation length (see 4.2.5.6).
The FIRST PARTITION NUMBER field indicates the first partition available on the specified logical volume number.
Partition numbering should start at zero.
The NUMBER OF PARTITIONS AVAILABLE field indicates the number of partitions available on the specified logical
volume number.
Table 223 — READ ATTRIBUTE with PARTITION LIST service action parameter list format
Bit
Byte
(MSB)
AVAILABLE DATA (0002h)
 (LSB)
FIRST PARTITION NUMBER
NUMBER OF PARTITIONS AVAILABLE
