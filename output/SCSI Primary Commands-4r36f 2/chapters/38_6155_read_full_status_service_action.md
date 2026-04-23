# 6.15.5 READ FULL STATUS service action

6.15.5 READ FULL STATUS service action
The READ FULL STATUS service action requests that the device server return a parameter list describing the
registration and persistent reservation status of each currently registered I_T nexus for the logical unit.
For more information on READ FULL STATUS see 5.13.6.4.
The format for the parameter data provided in response to a PERSISTENT RESERVE IN command with the
READ FULL STATUS service action is shown in table 210.
The PRGENERATION field shall be as defined for the PERSISTENT RESERVE IN command with READ KEYS
service action parameter data (see 6.15.2).
The ADDITIONAL LENGTH field indicates the number of bytes that follow in the full status descriptors. The
contents of the ADDITIONAL LENGTH field are not altered based on the allocation length (see 4.2.5.6).
Table 210 — PERSISTENT RESERVE IN parameter data for READ FULL STATUS
Bit
Byte
(MSB)
PRGENERATION
•••
(LSB)
(MSB)
ADDITIONAL LENGTH (n-7)
•••
(LSB)
Full status descriptors
Full status descriptor [first] (see table 211)
•••
•••
Full status descriptor [last] (see table 211)
•••
n


The format of the full status descriptors is shown in table 211. Each full status descriptor describes one or
more registered I_T nexuses. The device server shall return persistent reservations status information for
every registered I_T nexus.
The RESERVATION KEY field contains the reservation key.
A Reservation Holder (R_HOLDER) bit set to one indicates that all I_T nexuses described by this full status
descriptor are registered and are persistent reservation holders (see 5.13.10). A R_HOLDER bit set to zero
indicates that all I_T nexuses described by this full status descriptor are registered but are not persistent
reservation holders.
An All Target Ports (ALL_TG_PT) bit set to zero indicates that this full status descriptor represents a single I_T
nexus. An ALL_TG_PT bit set to one indicates that:
a)
this full status descriptor represents all the I_T nexuses that are associated with both:
A)
the initiator port specified by the TransportID; and
B)
every target port in the SCSI target device;
b)
all the I_T nexuses are registered with the same reservation key; and
c)
all the I_T nexuses are either reservation holders or not reservation holders as indicated by the
R_HOLDER bit.
The device server is not required to return an ALL_TG_PT bit set to one. Instead, it may return separate full
status descriptors for each I_T nexus.
Table 211 — PERSISTENT RESERVE IN full status descriptor format
Bit
Byte
(MSB)
RESERVATION KEY
•••
(LSB)
Reserved
•••
Reserved
ALL_TG_PT
R_HOLDER
SCOPE
TYPE
Reserved
•••
(MSB)
RELATIVE TARGET PORT IDENTIFIER
(LSB)
(MSB)
ADDITIONAL DESCRIPTOR LENGTH (n-23)
•••
(LSB)
TransportID
•••
n
