# 7.8.10 Power Condition VPD page

7.8.10 Power Condition VPD page
The Power Condition VPD page (see table 628) indicates which power conditions (see 5.12) are supported by
the logical unit and provides information about how those power conditions operate.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in 7.8.2.
The PAGE CODE field and PAGE LENGTH field are defined in 7.8.2, and shall be set to the value shown in table
628 for the Power Condition VPD page.
If set to one, a power condition support bit (i.e., the STANDBY_Y bit, the STANDBY_Z bit, the IDLE_C bit, the
IDLE_B bit, and the IDLE_A bit) indicates that:
a)
the associated power condition may be entered with the START STOP UNIT command (see SBC-3) if
that command is implemented; and
b)
the associated power condition may be entered with a power condition timer if the associated timer is
supported and enabled (see 7.5.13).
A STANDBY_Y power conditions support bit set to one indicates that the logical unit supports the standby_y
power condition as described in this subclause. A STANDBY_Y bit set to zero indicates that the logical unit does
not support the standby_y power condition.
Table 628 — Power Condition VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (8Ah)
(MSB)
PAGE LENGTH (000Eh)
(LSB)
Reserved
STANDBY_Y STANDBY_Z
Reserved
IDLE_C
IDLE_B
IDLE_A
(MSB)
STOPPED CONDITION RECOVERY TIME
(LSB)
(MSB)
STANDBY_Z CONDITION RECOVERY TIME
(LSB)
(MSB)
STANDBY_Y CONDITION RECOVERY TIME
(LSB)
(MSB)
IDLE_A CONDITION RECOVERY TIME
(LSB)
(MSB)
IDLE_B CONDITION RECOVERY TIME
(LSB)
(MSB)
IDLE_C CONDITION RECOVERY TIME
(LSB)


A STANDBY_Z power conditions support bit set to one indicates that the logical unit supports the standby_z
power condition as described in this subclause. A STANDBY_Z bit set to zero indicates that the logical unit does
not support the standby_z power condition.
A IDLE_C power conditions support bit set to one indicates that the logical unit supports the idle_c power
condition as described in this subclause. A IDLE_C bit set to zero indicates that the logical unit does not
support the idle_c power condition.
A IDLE_B power conditions support bit set to one indicates that the logical unit supports the idle_b power
condition as described in this subclause. A IDLE_B bit set to zero indicates that the logical unit does not
support the idle_b power condition.
A IDLE_A power conditions support bit set to one indicates that the logical unit supports the idle_a power
condition as described in this subclause. A IDLE_A bit set to zero indicates that the logical unit does not
support the idle_a power condition.
The STOPPED CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the logical
unit takes to transition from the stopped power condition to the active power condition. This field is only appli-
cable to SCSI target devices that implement the START STOP UNIT command (see SBC-3). This time does
not include the processing time for the command that caused this transition to occur or any SCSI transport
protocol specific waiting time (e.g., the NOTIFY (ENABLE SPINUP) requirement described in SPL). A value of
zero indicates that the recovery time is not specified. A value of FFFFh indicates that the recovery time is
more than 65.534 seconds.
The STANDBY_Z CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the
logical unit takes to transition from the standby_z power condition to the active power condition. This time
does not include the processing time for the command that caused this transition to occur or any SCSI
transport protocol specific waiting time (e.g., the NOTIFY (ENABLE SPINUP) requirement described in SPL).
A value of zero indicates that the recovery time is not specified. A value of FFFFh indicates that the recovery
time is more than 65.534 seconds.
The STANDBY_Y CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the
logical unit takes to transition from the standby_y power condition to the active power condition. This time
does not include the processing time for the command that caused this transition to occur or any SCSI
transport protocol specific waiting time (e.g., the NOTIFY (ENABLE SPINUP) requirement described in SPL).
A value of zero indicates that the recovery time is not specified. A value of FFFFh indicates that the recovery
time is more than 65.534 seconds.
The IDLE_A CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the logical
unit takes to transition from the idle_a power condition to the active power condition. This time does not
include the processing time for the command that caused this transition to occur. A value of zero indicates that
the recovery time is not specified. A value of FFFFh indicates that the recovery time is more than 65.534
seconds.
The IDLE_B CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the logical
unit takes to transition from the idle_b power condition to the active power condition. This time does not
include the processing time for the command that caused this transition to occur. A value of zero indicates that
the recovery time is not specified. A value of FFFFh indicates that the recovery time is more than 65.534
seconds.
The IDLE_C CONDITION RECOVERY TIME field indicates the time, in one millisecond increments, that the logical
unit takes to transition from the idle_c power condition to the active power condition. This time does not
include the processing time for the command that caused this transition to occur. A value of zero indicates that


the recovery time is not specified. A value of FFFFh indicates that the recovery time is more than 65.534
seconds.
7.8.11 Power Consumption VPD page
The Power Consumption VPD page (see table 629) provides an application client with a list of the available
settings to limit the maximum power consumption (e.g., see USB-3) of the logical unit while in the active
power condition (see 5.12.4) as described in 5.12.2.
The PERIPHERAL QUALIFIER field and PERIPHERAL DEVICE TYPE field are defined in 7.8.2.
The PAGE CODE field and PAGE LENGTH field are defined in 7.8.2, and shall be set to the value shown in table
629 for the Power Consumption VPD page.
Each power consumption descriptor (see table 630) describes one maximum power consumption level that
the application client may establish for use by the active power condition (see 5.12.4) using the Power
Consumption mode page (see 7.5.14) as described in 5.12.2.
The POWER CONSUMPTION IDENTIFIER field provides a reference handle to specify which descriptor is selected
by the Power Consumption mode page as described in 5.12.2.
Table 629 — Power Consumption VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (8Dh)
(MSB)
PAGE LENGTH (n-3)
(LSB)
Power consumption descriptor list
Power consumption descriptor [first]
•••
•••
n-3
Power consumption descriptor [last]
•••
n
Table 630 — Power consumption descriptor format
Bit
Byte
POWER CONSUMPTION IDENTIFIER
Reserved
POWER CONSUMPTION UNITS
(MSB)
POWER CONSUMPTION VALUE
(LSB)
