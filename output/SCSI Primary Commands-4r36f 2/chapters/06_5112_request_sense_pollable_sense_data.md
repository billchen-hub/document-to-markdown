# 5.11.2 REQUEST SENSE pollable sense data

An application client or device server shall not assume that any length field contains the value defined in a
SCSI standard.
If a device server receives a parameter list containing a length field (e.g., a PAGE LENGTH field) and containing
more bytes than are defined in the standard to which it was designed (e.g., the device server complies with a
version of a SCSI standard defining that a parameter list has 24 bytes, but receives a parameter list containing
36 bytes), then the device server shall terminate the command with CHECK CONDITION status, with the
sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN PARAMETER
LIST.
For parameter lists containing a descriptor length field and a descriptor list, if a device server receives more
bytes in a descriptor than are defined in the standard to which it was designed (e.g., the device server
complies with a version of a SCSI standard defining that a descriptor is 12 bytes, but receives a parameter list
containing a 16 byte form of that descriptor), then the device server shall terminate the command with CHECK
CONDITION status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to
INVALID FIELD IN PARAMETER LIST.
An application client should ignore any bytes of parameter data beyond those defined in the standard to which
it was designed (e.g., if the application client complies with a version of a SCSI standard defining 24 bytes of
parameter data, but receives 36 bytes of parameter data, then the application client should ignore the last 12
bytes or the parameter data).
For additional response bytes containing a descriptor length field and a descriptor list, an application client
should ignore any bytes in each descriptor beyond those defined in the standard to which it was designed
(e.g., if the application client complies with a version of a SCSI standard defining that a descriptor has 24
bytes, but receives parameter data containing a descriptor list with a 36 byte form of that descriptor, then the
application client should ignore the last 12 bytes of the descriptor).
5.11 Pollable condition information
5.11.1 Overview
A device server may have information about a condition that does not represent an exception condition. This
information is not reported with a CHECK CONDITION status. Instead, this information is reported:
a)
as sense data format parameter data in response to a REQUEST SENSE command as described in
5.11.2; or
b)
as log parameter data as described in 5.11.3.
5.11.2 REQUEST SENSE pollable sense data
5.11.2.1 Overview
SCSI target devices are required to make specified information used to prepare the parameter data that is
returned by the REQUEST SENSE command (see 6.39) available whenever that information is applicable.
Which sense data is returned in a REQUEST SENSE parameter data is determined at the time the REQUEST
SENSE command is processed.


Application clients have no way to control which pollable sense data is returned by a REQUEST SENSE
command. Mechanisms that are specialized to a particular function (e.g., log pages, mode pages) should be
used to obtain information about that function.
5.11.2.2 Selecting pollable sense data to return
Conditions that are not related to the availability of pollable sense data (e.g., a pending unit attention
condition) may cause the device server to ignore all available pollable sense data.
If pollable sense data is available to be returned by a REQUEST SENSE command (see 6.39), the choice of
which sense key and additional sense code to return shall be made as follows:
1)
sense data with the sense key set to NOT READY and the additional sense code set to:
1)
LOGICAL UNIT NOT READY, INITIALIZING COMMAND REQUIRED (see 5.12.7); and
2)
any other additional sense code that is associated with pollable sense data when combined with a
sense key set to NOT READY;
and
2)
sense data with the sense key set to NO SENSE and the additional sense code set:
1)
as defined for the informational exceptions sense data described in the Informational Exceptions
Control mode page (see applicable command standard);
2)
to LOGICAL UNIT TRANSITIONING TO ANOTHER POWER CONDITION (see 5.12.8 and
SBC-3);
3)
as defined for any power condition related sense data described in 5.12.7; and
4)
any other additional sense code that is associated with pollable sense data when combined with a
sense key set to NO SENSE.
5.11.2.3 Returning one or more progress indications
If the sense key is set to NOT READY or NO SENSE in the header for the sense data being returned by the
REQUEST SENSE command (see 6.39) as parameter data, and progress indication information is being
provided as part of any pollable sense data available for return by the REQUEST SENSE command (see
5.11.2.1), then:
a)
if the DESC bit is set to zero in the REQUEST SENSE command, then the device server shall set the
SKSV bit in the fixed-format sense data to one only if progress indication information is available for the
additional sense code being returned in the ADDITIONAL SENSE CODE field and ADDITIONAL SENSE CODE
QUALIFIER field; or
b)
if the DESC bit is set to one in the REQUEST SENSE command, then the device server places
progress indications in the sense data being returned as follows:
A)
if progress indication information is available for the additional sense code being returned in the
ADDITIONAL SENSE CODE field and ADDITIONAL SENSE CODE QUALIFIER field in the sense data header,
then the device shall include one sense key specific sense data descriptor (see 4.5.2.4) in which
that progress indication is returned; and
B)
if progress indication information is available for one or more additional sense codes that are not
being returned in the ADDITIONAL SENSE CODE field and ADDITIONAL SENSE CODE QUALIFIER field in
the sense data header, then should include in the sense data one another progress indication
sense data descriptor (see 4.5.2.6) for each available instance of progress indication information.


5.11.3 Log parameter pollable device condition information
The following background testing functions report their condition information using log page parameters:
a)
self-test operations report whether a test is in progress, but not how far it has progressed using the
Self-Test Results log page (see 7.3.16); and
b)
direct-access block devices report progress for background pre-scan operations and background
medium scan operations using the Background Scan Results log page (see SBC-3).
5.12 Power management
5.12.1 Power management overview
The Power Condition mode page (see 7.5.13) and Power Consumption mode page (see 7.5.14) allow an
application client to manage the power utilization of a logical unit in a manner that may reduce power
consumption of the SCSI target device.
Power consumption management is described in 5.12.2, including its interactions with power condition
management. Power condition management is described in 5.12.3.
A change in the power consumption setting or power condition of any logical unit in a SCSI target device may
result in a change in the SCSI target device's power utilization. If a SCSI target device contains multiple logical
units, then the SCSI target device’s power utilization may not change until a group of the logical units have
changed their power consumption in the active power condition (see 5.12.2) or changed to a lower power
condition (see 5.12.3). Any grouping or groupings of logical units for power management is outside the scope
of this standard.
5.12.2 Power consumption management
Power consumption management allows control of the maximum power consumption (e.g., see USB-3) of a
logical unit that is in the active power condition (see 5.12.4).
If power consumption management is supported, then the device server shall support the:
a)
Power Consumption mode page (see 7.5.14); and
b)
Power Consumption VPD page (see 7.8.11).
The Power Consumption VPD page contains one or more power consumption descriptors that indicate the
maximum power consumption levels supported by the device server using:
a)
a power consumption identifier; and
b)
information about the maximum power consumption associated with that power consumption
identifier.
An application client may specify use of one of the maximum power consumption levels indicated by the
Power Consumption VPD page by setting the POWER CONSUMPTION IDENTIFIER field in the Power Consumption
mode page to the contents of that POWER CONSUMPTION IDENTIFIER field in the Power Consumption VPD page.
The SCSI target device shall limit the maximum power consumption while the logical unit is in the active
power condition to the value indicated in the power consumption descriptor in the Power Consumption VPD
page that is associated with the POWER CONSUMPTION IDENTIFIER field in the Power Consumption mode page.


Power consumption management shall:
a)
be used to limit the maximum power consumption while in the active power condition;
b)
not affect the power consumed during a change between power conditions; and
c)
not affect the power consumed while in a power condition other than active.
5.12.3 Power conditions management
This control is invoked by enabling and initializing one or more idle condition timers and/or standby condition
timers based on Power Condition mode page values.
Command standards may define the following additional power management features:
a)
power conditions (e.g., the stopped power condition in SBC-3);
b)
changes to the power condition state machine (e.g., the SSU_PC8:Stopped state in SBC-3);
c)
commands that manage power conditions (e.g., a START STOP UNIT command in SBC-3 or
MMC-6);
d)
changes to commands defined in this standard; or
e)
mode pages, log pages, or VPD pages that are associated with managing power conditions.
Transport protocol standards (e.g., SPL) may define additional requirements on the states in the power
condition state machine defined in this standard or a command standard.
There shall be no notification to the application client that a logical unit has changed from one power condition
to another. The response to a REQUEST SENSE command (see 6.39) may indicate whether a logical unit is
in a low power condition and which low power condition.
The current power condition of a logical unit may be decreased by:
a)
the expiration of a power condition timer;
b)
the completion of background functions; or
c)
power condition activities described in a command standard.
The current power condition of a logical unit is increased by:
a)
the processing of a command that the device server is unable to continue processing while in the
current power condition;
b)
the processing of a background function that the device server is unable to process while in the
current power condition; or
c)
power condition activities described in a command standard.
If a device server processes a command that the device server is capable of completing while the logical unit
is in a low power condition, then the device server shall not stop any enabled power condition timers,
regardless of which power condition the logical unit was in when the device server began processing the
command.
If a device server processes a command that the device server is not capable of completing while the logical
unit is in a low power condition, then the device server shall stop any running power condition timers. On
completion of the command, the device server shall reinitialize all enabled power condition timers based on
their values in the Power Condition mode page (see 7.5.13) and start the timers, regardless of which power
condition the logical unit was in when the device server began processing the command.


The device server shall process any task management function (see SAM-5), except LOGICAL UNIT RESET,
regardless of current power condition, without changing to a different power condition. The power condition
timers shall not be affected by task management functions, except LOGICAL UNIT RESET.
The device server may change power conditions or power condition timers while processing a LOGICAL UNIT
RESET.
No power condition defined in this standard shall affect the supply of any power required for proper operation
of a service delivery subsystem.
Logical units that contain cache memory shall write all cached data to the medium for the logical unit (e.g., as
a logical unit would do in response to a SYNCHRONIZE CACHE command as described in SBC-3) prior to
entering into any power condition that prevents accessing the media (e.g., before a hard drive stops its spindle
motor during a change to the standby power condition).
5.12.4 Active power condition
While in the active power condition:
a)
the device server is capable of completing the processing of its supported commands, including those
that require media access, without the logical unit changing power condition;
b)
the device server completes processing of a command in the shortest time when compared to the
time required for completion of that command if command processing began while the logical unit was
in any of the idle power conditions or standby power conditions; and
c)
the SCSI target device may consume more power than while the logical unit is in any of the idle power
conditions or standby power conditions (e.g., a disk drive's spindle motor may be active).
A logical unit that is in the active power condition may be affected by power consumption management (see
5.12.2).
5.12.5 Idle power conditions
A device server may support more than one idle power condition (i.e., idle_a, idle_b, and idle_c) to provide
progressively lower power consumption (i.e., the following power consumption relationship: idle_a  idle_b 
idle_c).
NOTE 10 - The idle_a power condition was referenced as the idle power condition in SPC-3.
While in one of the idle power conditions:
a)
the device server is capable of completing the processing of its supported commands, except those
that require the logical unit to be in the active power condition to be capable of completing the
command with GOOD status (e.g., commands that require media access to complete processing);
b)
the device server may take longer to complete processing a command than while the logical unit is in
the active power condition (e.g., the device may have to activate some circuitry before completing
processing of a command);
c)
the power consumed by the SCSI target device while in an idle power condition should be less than
the power consumed while the logical unit is in the active power condition and may be greater than
the power consumed while the logical unit is in a standby power condition; and
d)
the peak power consumption during a change from an idle power condition to the active power
condition shall be no more than the typical peak power consumption in the active power condition.


5.12.6 Standby power conditions
A device server may support more than one standby power condition (i.e., standby_y and standby_z) to
provide progressively lower power consumption (i.e., the following power consumption relationship: standby_y
 standby_z).
NOTE 11 - The standby_z power condition was referenced as the standby power condition in SPC-3.
While in one of the standby power conditions:
a)
the device server is not capable of completing the processing of commands that require media access
without the logical unit changing to the active power condition. SCSI transport protocol standards may
impose additional requirements on command processing while changing to a higher power condition
(e.g., the response may be CHECK CONDITION status with sense key set to NOT READY and
additional sense bytes set to LOGICAL UNIT NOT READY, NOTIFY (ENABLE SPINUP) REQUIRED
instead of GOOD status described in SPL);
b)
the device server may take longer to complete processing a command than while the logical unit is in
the active power condition or one of the idle power conditions (e.g., a disk drive's spindle motor may
need to be started);
c)
the power consumed by the SCSI target device while in one of the standby power conditions should
be less than the power consumed while the logical unit is in the active power condition or any of the
idle power conditions; and
d)
the peak power consumption during a change from a standby power condition to the active power
condition or an idle power condition is not limited by this standard.
5.12.7 Power condition pollable sense data
If the logical unit is in any power condition other than active, the following data shall be available for use by the
REQUEST SENSE command while returning pollable sense data (see 5.11.2) and:
a)
if the logical unit is in an idle power condition (see 5.12.5), then the sense key shall be set to NO
SENSE and the additional sense code set to one of the following:
A)
LOW POWER CONDITION ON if the reason for entry into the idle power condition is unknown;
B)
IDLE CONDITION ACTIVATED BY TIMER if the logical unit entered the idle_a power condition
due to the idle_a condition timer (see 5.12.8.4);
C) IDLE CONDITION ACTIVATED BY COMMAND if the logical unit entered the idle_a power
condition due to processing of a command;
D) IDLE_B CONDITION ACTIVATED BY TIMER if the logical unit entered the idle_b power condition
due to the idle_b condition timer (see 5.12.8.4);
E)
IDLE_B CONDITION ACTIVATED BY COMMAND if the logical unit entered the idle_b power
condition due to processing of a command;
F)
IDLE_C CONDITION ACTIVATED BY TIMER if the logical unit entered the idle_c power condition
due to the idle_c condition timer (see 5.12.8.4); or
G) IDLE_C CONDITION ACTIVATED BY COMMAND if the logical unit entered the idle_c power
condition due to processing of a command;
b)
if the logical unit is in a standby power condition (see 5.12.6), then the sense key shall be set to NO
SENSE and the additional sense code set to one of the following:
A)
LOW POWER CONDITION ON if the reason for entry into the standby power condition is
unknown;
B)
STANDBY_Y CONDITION ACTIVATED BY TIMER if the logical unit entered the standby_y power
condition due to the standby_y condition timer (see 5.12.8.5);
C) STANDBY_Y CONDITION ACTIVATED BY COMMAND if the logical unit entered the standby_y
power condition due to processing of a command;
