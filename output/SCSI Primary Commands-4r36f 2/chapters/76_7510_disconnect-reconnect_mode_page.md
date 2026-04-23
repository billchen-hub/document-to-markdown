# 7.5.10 Disconnect-Reconnect mode page

The MAXIMUM SENSE DATA LENGTH field specifies the maximum number of bytes of sense data the device
server shall return in the same I_T_L_Q nexus transaction as the status. A MAXIMUM SENSE DATA LENGTH field
set to zero specifies that there is no limit. The device server shall not return more sense data bytes in the
same I_T_L_Q nexus transaction as the status than the smaller of the length indicated by the:
a)
MAXIMUM SENSE DATA LENGTH field; and
b)
MAXIMUM SUPPORTED SENSE DATA LENGTH field in the Extended INQUIRY VPD page (see 7.8.7).
7.5.10 Disconnect-Reconnect mode page
The Disconnect-Reconnect mode page (see table 464) provides the application client the means to tune the
performance of a service delivery subsystem. The name for this mode page, disconnect-reconnect, comes
from the SCSI parallel interface. The mode page policy (see 7.5.2) for this mode page shall be shared or per
target port. If the SCSI target device contains more than one target port, the mode page policy should be per
target port.
The Disconnect-Reconnect mode page controls parameters that affect one or more target ports. The param-
eters that may be implemented are defined in the SCSI transport protocol standard for the target port. The
MLUS bit (see 7.8.9) shall be set to one in the mode page policy descriptor for this mode page.
The parameters for a target port affect its behavior regardless of which initiator port is forming an I_T nexus
with the target port. The parameters may be accessed by MODE SENSE (see 6.13) and MODE SELECT (see
6.11) commands directed to any logical unit accessible through the target port. If a parameter value is
changed, all the device servers for all logical units accessible through the target port shall establish a unit
attention condition for the initiator port associated with every I_T nexus that includes the target port except the
Table 464 — Disconnect-Reconnect mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (02h)
PAGE LENGTH (0Eh)
BUFFER FULL RATIO
BUFFER EMPTY RATIO
(MSB)
BUS INACTIVITY LIMIT
(LSB)
(MSB)
DISCONNECT TIME LIMIT
(LSB)
(MSB)
CONNECT TIME LIMIT
(LSB)
(MSB)
MAXIMUM BURST SIZE
(LSB)
EMDP
FAIR ARBITRATION
DIMM
DTDC
Reserved
(MSB)
FIRST BURST SIZE
(LSB)


I_T nexus on which the MODE SELECT command was received, with the additional sense code set to MODE
PARAMETERS CHANGED.
If a parameter that is not appropriate for the specific SCSI transport protocol implemented by the target port is
non-zero, the command shall be terminated with CHECK CONDITION status, with the sense key set to
ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER LIST.
An interconnect tenancy is a period of time during which a given pair of SCSI ports (i.e., an initiator port and a
target port) are accessing the interconnect layer to communicate with each other (e.g., on arbitrated intercon-
nects, a tenancy typically begins when a SCSI port successfully arbitrates for the interconnect and ends when
the SCSI port releases the interconnect for use by other devices). Data and other information transfers take
place during interconnect tenancies.
The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit, PAGE CODE field, and PAGE LENGTH field shall be set as shown in table 464 for the
Disconnect-Reconnect mode page.
The BUFFER FULL RATIO field specifies to the target port how full the buffer should be during read operations
prior to requesting an interconnect tenancy. Target ports that do not implement the requested ratio should
round down to the nearest implemented ratio as defined in 5.9.
The BUFFER EMPTY RATIO field specifies to the target port how empty the buffer should be during write opera-
tions prior to requesting an interconnect tenancy. Target ports that do not implement the requested ratio
should round down to the nearest implemented ratio as defined in 5.9.
The buffer full and buffer empty ratios are numerators of a fractional multiplier that has 256 as its denominator.
A value of zero indicates that the target port determines when to request an interconnect tenancy consistent
with the disconnect time limit parameter. These parameters are advisory to the target port.
NOTE 52 - As an example, consider a target port with ten 512-byte buffers and a specified buffer full ratio of
3Fh. The formula is: INTEGER((ratio256)number of buffers). Therefore in this example
INTEGER((3Fh256)10) = 2. During the read operations described in this example, the target port should
request an interconnect tenancy whenever two or more buffers are full.
The BUS INACTIVITY LIMIT field specifies the maximum time that the target port is permitted to maintain an inter-
connect tenancy without data or information transfer. If the bus inactivity limit is exceeded, then the target port
shall conclude the interconnect tenancy, within the restrictions placed on it by the applicable SCSI transport
protocol. The contents of the DTDC field in this mode page also shall affect the duration of an interconnect
tenancy. This value may be rounded as defined in 5.9. A value of zero specifies that there is no bus inactivity
limit. Different SCSI transport protocols define different units of measure for the bus inactivity limit.
The DISCONNECT TIME LIMIT field specifies the minimum time that the target port shall wait between inter-
connect tenancies. This value may be rounded as defined in 5.9. A value of zero specifies that there is no
disconnect time limit. Different SCSI transport protocols define different units of measure for the disconnect
time limit.
The CONNECT TIME LIMIT field specifies the maximum duration of a single interconnect tenancy. If the connect
time limit is exceeded, then the target port shall conclude the interconnect tenancy, within the restrictions
placed on it by the applicable SCSI transport protocol. The contents of the DTDC field in this mode page also
shall affect the duration of an interconnect tenancy. This value may be rounded as defined in 5.9. A value of
zero specifies that there is no connect time limit. Different SCSI transport protocols define different units of
measure for the connect time limit.


The MAXIMUM BURST SIZE field indicates the maximum amount of data that the target port shall transfer during
a single data transfer operation. This value is expressed in increments of 512 bytes (i.e., a value of one means
512 bytes, two means 1 024 bytes, etc.). The relationship, if any, between data transfer operations and inter-
connect tenancies is defined in the individual SCSI transport protocol standards. A value of zero specifies
there is no limit on the amount of data transferred per data transfer operation.
In terms of the SCSI transport protocol services (see SAM-5), the device server shall limit the Request Byte
Count argument to the Receive Data-Out protocol service and the Send Data-In protocol service to the
amount specified in the MAXIMUM BURST SIZE field.
The enable modify data pointers (EMDP) bit specifies whether or not the target port may transfer data out of
order. If the EMDP bit is set to zero, the target port shall not transfer data out of order. If the EMDP bit is set to
one, the target port is allowed to transfer data out of order.
The FAIR ARBITRATION field specifies whether the target port should use fair or unfair arbitration when
requesting an interconnect tenancy. The field may be used to specify different fairness methods as defined in
the individual SCSI transport protocol standards.
A disconnect immediate (DIMM) bit set to zero specifies that the target port may transfer data for a command
during the same interconnect tenancy in which it receives the command. Whether or not the target port does
so may depend upon the target port’s internal algorithms, the rules of the applicable SCSI transport protocol,
and settings of the other parameters in this mode page. A disconnect immediate (DIMM) bit set to one
specifies that the target port shall not transfer data for a command during the same interconnect tenancy in
which it receives the command.
The data transfer disconnect control (DTDC) field (see table 465) defines other restrictions on when multiple
interconnect tenancies are permitted. A non-zero value in the DTDC field shall take precedence over other
interconnect tenancy controls represented by other fields in this mode page.
The FIRST BURST SIZE field specifies the maximum amount of data that may be transferred to the target port for
a command along with the command (i.e., the first burst). This value is expressed in increments of 512 bytes
(i.e., a value of one means 512 bytes, two means 1 024 bytes, etc.). The meaning of a value of zero is SCSI
transport protocol specific. SCSI transport protocols supporting this field shall provide an additional
mechanism to enable and disable the first burst function.
In terms of the SCSI transport protocol services (see SAM-5), the Receive Data-Out protocol service shall
retrieve the first FIRST BURST SIZE amount of data from the first burst.
Table 465 — Data transfer disconnect control (DTDC) field
Code
Description
000b
Data transfer disconnect control is not used. Interconnect tenancies are
controlled by other fields in this mode page.
001b
All data for a command shall be transferred within a single interconnect tenancy.
010b
Reserved
011b
All data and the response for a command shall be transferred within a single
interconnect tenancy.
100b to 111b
Reserved


7.5.11 Extended mode page
The Extended mode page (see table 466) provides a means to specify subpages that are defined for all
device types. Subpage code 00h is reserved. All Extended mode pages use the sub_page format.
The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit and PAGE CODE field shall be set as shown in table 466 for the Extended mode page.
7.5.12 Extended Device-Type Specific mode page
The Extended Device-Type Specific mode page (see table 467) provides a means to specify subpages that
are defined differently for each device type. Subpage code 00h is reserved in the MODE SENSE command
(see 6.13.1). All Extended Device-Type Specific mode pages use the sub_page format.
The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit and PAGE CODE field shall be set as shown in table 467 for the Extended Device-Type Specific
mode page.
Table 466 — Extended mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (15h)
SUBPAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
Subpage specific mode parameters
•••
n
Table 467 — Extended Device-Type Specific mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (16h)
SUBPAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
Subpage specific mode parameters
•••
n
