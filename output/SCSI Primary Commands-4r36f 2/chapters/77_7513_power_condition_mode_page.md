# 7.5.13 Power Condition mode page

7.5.13 Power Condition mode page
The Power Condition mode page provides an application client with a method to control the power condition of
a logical unit (see 5.12).
The mode page policy (see 7.5.2) for this mode page shall be shared.
The logical unit shall use the values in the Power Condition mode page to control its power condition after a
power on or a hard reset until a START STOP UNIT command (see SBC-3) setting a power condition is
received.
Table 468 defines the Power Condition mode page.
The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit, PAGE CODE field, and PAGE LENGTH field shall be set as shown in table 468 for the Power Condition
mode page.
Table 468 — Power Condition mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (1Ah)
PAGE LENGTH (26h)
PM_BG_PRECEDENCE
Reserved
STANDBY_Y
Reserved
IDLE_C
IDLE_B
IDLE_A
STANDBY_Z
(MSB)
IDLE_A CONDITION TIMER

•••
(LSB)
(MSB)
STANDBY_Z CONDITION TIMER

•••
(LSB)
(MSB)
IDLE_B CONDITION TIMER

•••
(LSB)
(MSB)
IDLE_C CONDITION TIMER

•••
(LSB)
(MSB)
STANDBY_Y CONDITION TIMER

•••
(LSB)

Reserved

•••

CCF IDLE
CCF STANDBY
CCF STOPPED
Reserved


The PM_BG_PRECEDENCE field (see table 469) specifies the interactions between background functions and
power management.
Table 469 — PM_BG_PRECEDENCE field
Code
Description
00b
Vendor specific
01b
Performing background functions take precedence over maintaining low power conditions as
follows:
a)
if the logical unit is in a low power condition as the result of a power condition timer
associated with that condition expiring, then:
1)
the logical unit shall change from that power condition, if necessary, to the power
condition required to perform the background function, if:
a)
a timer associated with a background scan operation expires, and that function is
enabled (see SBC-3); or
b)
an event occurs to initiate a device specific background function, and that function
is enabled (see 5.3);
2)
the logical unit shall perform the background function(s) based on the definitions in this
standard and other command standards (e.g., if the device server receives a command
while performing a background function, then the logical unit shall suspend the function
to process the command);
3)
if more than one condition is met to initiate a background function, then:
a)
all initiated background functions shall be performed; and
b)
the order of performing the functions is vendor specific;
and
4)
after all initiated background functions have been completed, the device server shall
check to see if any power condition timers have expired. If any power condition timer
has expired, then the logical unit shall change to the power condition associated with
the highest priority timer that has expired;
or
b)
if the logical unit is performing a background function, and a power condition timer expires,
then the logical unit shall perform all initiated background functions before the logical unit
changes to a power condition associated with a timer that has expired.
10b
Maintaining low power conditions take precedence over performing background functions as
follows:
a)
if the logical unit is in a low power condition, then the logical unit shall not change from that
power condition to perform a background function;
b)
the device server may perform any initiated and enabled background function based on the
definitions in this standard or other command standards, if all of the following are true:
A)
a condition is met to initiate a background function;
B)
that background function is enabled;
C) the logical unit changes to a power condition in which the background function may be
performed (e.g., the device server processes a medium access command causing the
logical unit to change its power condition to continue processing that command); and
D) all outstanding application client requests have been completed;
or
c)
if the logical unit is performing a background function, and a power condition timer expires
that causes a change to a power condition in which the logical unit is unable to continue
performing the background function, then the logical unit shall:
A)
suspend the background function; and
B)
change to the power condition associated with the timer that expired.
11b
Reserved


The behavior of the idle condition timer and standby condition timer controlled by this mode page is defined in
the power condition overview (see 5.12.1) and the power condition state machine (see 5.12.8).
If the STANDBY_Y bit is set to one, then the standby_y condition timer is enabled. If the STANDBY_Y bit is set to
zero, then the device server shall ignore the standby_y condition timer.
If the IDLE_C bit is set to one, then the idle_c condition timer is enabled. If the IDLE_C bit is set to zero, then the
device server shall ignore the idle_c condition timer.
If the IDLE_B bit is set to one, then the idle_b condition timer is enabled. If the IDLE_B bit is set to zero, then the
device server shall ignore the idle_b condition timer.
If the IDLE_A bit is set to one, then the idle_a condition timer is enabled. If the IDLE_A bit is set to zero, then the
device server shall ignore the idle_a condition timer.
If the STANDBY_Z bit is set to one, then the standby_z condition timer is enabled. If the STANDBY_Z bit is set to
zero, then the device server shall ignore the standby_z condition timer.
If any of the power condition enable bits (e.g., the IDLE_C bit or the STANDBY_Y bit) are set to zero and are not
changeable (see 6.13.3), then the device server does not implement the power condition timer associated
with that enable bit (see table 64 in 5.12.8.1).
The IDLE_A CONDITION TIMER field specifies the initial value, in 100 millisecond increments, for the idle_a power
condition timer (see 5.12.8.1). This value may be rounded up or down to the nearest implemented time as
described in 5.9.
The STANDBY_Z CONDITION TIMER field specifies the initial value, in 100 millisecond increments, for the
standby_z power condition timer (see 5.12.8.1). This value may be rounded up or down to the nearest imple-
mented time as described in 5.9.
The IDLE_B CONDITION TIMER field specifies the initial value, in 100 millisecond increments, for the idle_b power
condition timer (see 5.12.8.1). This value may be rounded up or down to the nearest implemented time as
described in 5.9.
The IDLE_C CONDITION TIMER field specifies the initial value, in 100 millisecond increments, for the idle_c power
condition timer (see 5.12.8.1). This value may be rounded up or down to the nearest implemented time as
described in 5.9.
The STANDBY_Y CONDITION TIMER field specifies the initial value, in 100 millisecond increments, for the
standby_y power condition timer (see 5.12.8.1). This value may be rounded up or down to the nearest imple-
mented time as described in 5.9.


The CHECK CONDITION if from idle_c (CCF IDLE) field is defined in table 470.
The CHECK CONDITION if from standby (CCF STANDBY) field is defined in table 471.
Table 470 — CCF IDLE field
Code
Description
00b
Restricted a
01b
If the transition was from an idle_c power condition, returning CHECK CONDITION status is
disabled. b
10b
If the transition was from an idle_c power condition, returning CHECK CONDITION status is
enabled. b
11b
Reserved
a See SAS-2 for command processing in the Active_Wait state and Idle_Wait state.
b For direct-access block devices see the Active_Wait state in SBC-3 for the definition of command
processing in that state. For devices that are not direct-access block devices, see the Active_Wait
state in this standard (i.e., see 5.12.8.6) for the definition of command processing in that state.
Table 471 — CCF STANDBY field
Code
Description
00b
Restricted a
01b
If the transition was from a standby power condition, returning CHECK CONDITION status is
disabled. b
10b
If the transition was from a standby power condition, returning CHECK CONDITION status is
enabled. b
11b
Reserved
a See SAS-2 for command processing in the Active_Wait state and Idle_Wait state.
b For direct-access block devices see the Active_Wait state and the Idle_Wait state in SBC-3 for the
definition of command processing in those states. For devices that are not direct-access block devices,
see the Active_Wait state in this standard (i.e., see 5.12.8.6) for the definition of command processing
in that state.


The CHECK CONDITION if from stopped (CCF STOPPED) field is defined in table 472.
7.5.14 Power Consumption mode page
The Power Consumption mode page (see table 473) is a subpage of the Power Conditions mode page (see
7.5.13) that provides a method to select a maximum power consumption level while in the active power
condition (see 5.12.4) based on the contents of the power consumption descriptors in the Power Consumption
VPD page (see 7.8.11) as described in 5.12.2. The mode page policy (see 7.5.2) for this mode page shall be
shared.
The PS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field shall be set as shown in table 473 for
the Power Consumption mode page.
The POWER CONSUMPTION IDENTIFIER field specifies the power consumption identifier from one of the power
consumption descriptors in the Power Consumption VPD page (see 7.8.11) that the device server is to use as
described in 5.12.2. If none of the power consumption descriptors in the Power Consumption VPD page
Table 472 — CCF STOPPED field
Code
Description
00b
Restricted a
01b
If the transition was from a stopped power condition, returning CHECK CONDITION status is
disabled. b
10b
If the transition was from a stopped power condition, returning CHECK CONDITION status is
enabled. b
11b
Reserved
a See SAS-2 for command processing in the Active_Wait state and Idle_Wait state.
b For direct-access block devices see the Active_Wait state, the Idle_Wait state description and the
Standby_Wait state in SBC-3 for the definition of command processing in those states.
Table 473 — Power Consumption mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (1Ah)
SUBPAGE CODE (01h)
 (MSB)
PAGE LENGTH (000Ch)
 (LSB)
Reserved

•••
POWER CONSUMPTION IDENTIFIER
Reserved

•••


contain the value in the POWER CONSUMPTION IDENTIFIER field, then the MODE SELECT command shall be
terminated with CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional
sense code set to INVALID FIELD IN PARAMETER LIST.
7.5.15 Protocol Specific Logical Unit mode page
The Protocol Specific Logical Unit mode page (see table 474) provides protocol specific controls that are
associated with a logical unit.
During an I_T_L nexus, the Protocol Specific Logical Unit mode page controls parameters that affect both:
a)
one or more target ports; and
b)
the logical unit.
The parameters that may be implemented are defined in the SCSI transport protocol standard for the target
port. The mode page policy (see 7.5.2) for this mode page shall be shared or per target port and should be per
target port.
The parameters for a target port and logical unit affect their behavior regardless of which initiator port is
forming an I_T_L nexus with the target port and logical unit. If a parameter value is changed, the device server
shall establish a unit attention condition for the initiator port associated with every I_T nexus except the I_T
nexus on which the MODE SELECT command was received, with the additional sense code set to MODE
PARAMETERS CHANGED.
The PS bit, SPF bit, PAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
The SPF bit and PAGE CODE field shall be set as shown in table 474 for the Protocol Specific Logical Unit mode
page.
The value in the PROTOCOL IDENTIFIER field (see 7.6.1) defines the SCSI transport protocol to which the mode
page applies. For a MODE SENSE command (see 6.13), the device server shall set the PROTOCOL IDENTIFIER
field to one of the values shown in table 477 (see 7.6.1) to indicate the SCSI transport protocol used by the
target port through which the MODE SENSE command is being processed. For a MODE SELECT command
(see 6.11), the application client shall set the PROTOCOL IDENTIFIER field to one of the values shown in table
477 indicating the SCSI transport protocol to which the protocol specific mode parameters apply. If a device
server receives a mode page containing a transport protocol identifier value other than the one used by the
target port on which the MODE SELECT command was received, then the command shall be terminated with
CHECK CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set
to INVALID FIELD IN PARAMETER LIST.
Table 474 — Protocol Specific Logical Unit mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (18h)
PAGE LENGTH (n-1)
Protocol specific mode parameters
PROTOCOL IDENTIFIER
Protocol specific mode parameters
•••
n
