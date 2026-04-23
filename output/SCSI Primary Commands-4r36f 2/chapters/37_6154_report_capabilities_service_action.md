# 6.15.4 REPORT CAPABILITIES service action

6.15.4 REPORT CAPABILITIES service action
The REPORT CAPABILITIES service action requests that the device server return information on persistent
reservation features.
The format for the parameter data provided in response to a PERSISTENT RESERVE IN command with the
REPORT CAPABILITIES service action is shown in table 207.
The LENGTH field indicates the length in bytes of the parameter data. The contents of the LENGTH field are not
altered based on the allocation length (see 4.2.5.6).
A replace lost reservation capable (RLR_C) bit set to one indicates that the device server supports the
REPLACE LOST RESERVATION service action in the PERSISTENT RESERVE OUT command. An RLR_C
bit set to zero indicates that the device server does not support the REPLACE LOST RESERVATION service
action in the PERSISTENT RESERVE OUT command. If the RLR_C bit is set to zero then the device server
shall not terminate any commands with CHECK CONDITION status with the sense key set to DATA
PROTECT and the additional sense code set to PERSISTENT RESERVATION INFORMATION LOST (see
5.13.5.3).
A compatible reservation handling (CRH) bit set to one indicates that the device server supports the exceptions
to the SPC-2 RESERVE and RELEASE commands described in 5.13.3. A CRH bit set to zero indicates that
RESERVE(6) command, RESERVE(10) command, RELEASE(6) command, and RELEASE(10) command
are processed as defined in SPC-2.
A specify initiator ports capable (SIP_C) bit set to one indicates that the device server supports the SPEC_I_PT
bit in the PERSISTENT RESERVE OUT command parameter data (see 6.16.3). An SIP_C bit set to zero
indicates that the device server does not support the SPEC_I_PT bit in the PERSISTENT RESERVE OUT
command parameter data.
An all target ports capable (ATP_C) bit set to one indicates that the device server supports the ALL_TG_PT bit in
the PERSISTENT RESERVE OUT command parameter data. An ATP_C bit set to zero indicates that the
device server does not support the ALL_TG_PT bit in the PERSISTENT RESERVE OUT command parameter
data.
A persist through power loss capable (PTPL_C) bit set to one indicates that the device server supports the
persist through power loss capability (see 5.13.5) for persistent reservations and the APTPL bit in the
Table 207 — PERSISTENT RESERVE IN parameter data for REPORT CAPABILITIES
Bit
Byte
(MSB)
LENGTH (0008h)
(LSB)
RLR_C
Reserved
CRH
SIP_C
ATP_C
Reserved
PTPL_C
TMV
ALLOW COMMANDS
Reserved
PTPL_A
PERSISTENT RESERVATION TYPE MASK
Reserved


PERSISTENT RESERVE OUT command parameter data. An PTPL_C bit set to zero indicates that the device
server does not support the persist through power loss capability.
A type mask valid (TMV) bit set to one indicates that the PERSISTENT RESERVATION TYPE MASK field contains a
bit map indicating which persistent reservation types are supported by the device server. A TMV bit set to zero
indicates that the PERSISTENT RESERVATION TYPE MASK field shall be ignored.


The ALLOW COMMANDS field (see table 208) indicates whether certain commands are allowed through certain
types of persistent reservations.
Table 208 — ALLOW COMMANDS field
Code
Description
000b
No information is provided about whether certain commands are allowed through certain types
of persistent reservations.
001b
The device server allows the TEST UNIT READY command (see table 65 in 5.13.1) through
Write Exclusive and Exclusive Access persistent reservations and does not provide informa-
tion about whether the following commands are allowed through Write Exclusive persistent
reservations:
a)
the MODE SENSE command, READ ATTRIBUTE command, READ BUFFER
command, RECEIVE COPY RESULTS command, RECEIVE DIAGNOSTIC RESULTS
command, REPORT SUPPORTED OPERATION CODES command, and REPORT
SUPPORTED TASK MANAGEMENT FUNCTION command (see table 65 in 5.13.1);
and
b)
the READ DEFECT DATA command (see SBC-3).
010b
The device server allows the TEST UNIT READY command through Write Exclusive and
Exclusive Access persistent reservations and does not allow the following commands through
Write Exclusive persistent reservations:
a)
the MODE SENSE command, READ ATTRIBUTE command, READ BUFFER
command, RECEIVE DIAGNOSTIC RESULTS command, REPORT SUPPORTED
OPERATION CODES command, and REPORT SUPPORTED TASK MANAGEMENT
FUNCTION command; and
b)
the READ DEFECT DATA command.
The device server does not allow the RECEIVE COPY RESULTS command through Write
Exclusive or Exclusive Access persistent reservations.
011b
The device server allows the TEST UNIT READY command through Write Exclusive and
Exclusive Access persistent reservations and allows the following commands through Write
Exclusive persistent reservations:
a)
the MODE SENSE command, READ ATTRIBUTE command, READ BUFFER
command, RECEIVE DIAGNOSTIC RESULTS command, REPORT SUPPORTED
OPERATION CODES command, and REPORT SUPPORTED TASK MANAGEMENT
FUNCTION command; and
b)
the READ DEFECT DATA command.
The device server does not allow the RECEIVE COPY RESULTS command through Write
Exclusive or Exclusive Access persistent reservations.
100b
The device server allows the TEST UNIT READY command and the RECEIVE COPY
RESULTS command through Write Exclusive and Exclusive Access persistent reservations
and allows the following commands through Write Exclusive persistent reservations:
a)
the MODE SENSE command, READ ATTRIBUTE command, READ BUFFER
command, RECEIVE DIAGNOSTIC RESULTS command, REPORT SUPPORTED
OPERATION CODES command, and REPORT SUPPORTED TASK MANAGEMENT
FUNCTION command; and
b)
the READ DEFECT DATA command.
101b to
111b
Reserved


A Persist Through Power Loss Activated (PTPL_A) bit set to one indicates that the persist through power loss
capability is activated (see 5.13.5). A PTPL_A bit set to zero indicates that the persist through power loss
capability is not activated.
The PERSISTENT RESERVATION TYPE MASK field (see table 209) contains a bit map that indicates the persistent
reservation types that are supported by the device server.
A Write Exclusive – All Registrants (WR_EX_AR) bit set to one indicates that the device server supports the
Write Exclusive – All Registrants persistent reservation type. An WR_EX_AR bit set to zero indicates that the
device server does not support the Write Exclusive – All Registrants persistent reservation type.
An Exclusive Access – Registrants Only (EX_AC_RO) bit set to one indicates that the device server supports
the Exclusive Access – Registrants Only persistent reservation type. An EX_AC_RO bit set to zero indicates
that the device server does not support the Exclusive Access – Registrants Only persistent reservation type.
A Write Exclusive – Registrants Only (WR_EX_RO) bit set to one indicates that the device server supports the
Write Exclusive – Registrants Only persistent reservation type. An WR_EX_RO bit set to zero indicates that the
device server does not support the Write Exclusive – Registrants Only persistent reservation type.
An Exclusive Access (EX_AC) bit set to one indicates that the device server supports the Exclusive Access
persistent reservation type. An EX_AC bit set to zero indicates that the device server does not support the
Exclusive Access persistent reservation type.
A Write Exclusive (WR_EX) bit set to one indicates that the device server supports the Write Exclusive
persistent reservation type. An WR_EX bit set to zero indicates that the device server does not support the
Write Exclusive persistent reservation type.
An Exclusive Access – All Registrants (EX_AC_AR) bit set to one indicates that the device server supports the
Exclusive Access – All Registrants persistent reservation type. An EX_AC_AR bit set to zero indicates that the
device server does not support the Exclusive Access – All Registrants persistent reservation type.
Table 209 — Persistent Reservation Type Mask format
Bit
Byte
WR_EX_AR
EX_AC_RO
WR_EX_RO
Reserved
EX_AC
Reserved
WR_EX
Reserved
Reserved
EX_AC_AR
