# 4.20 START STOP UNIT and power conditions

Each bit in the DISABLED PHYSICAL ELEMENT field represents a physical element that is associated with a group
of LBAs that are treated as having predicted unrecovered read errors. The correlation of bits in the DISABLED
PHYSICAL ELEMENT field to LBAs in the logical unit is vendor specific.
An application client ends a test by disabling the rebuild assist mode (see 4.19.4).
4.20 START STOP UNIT and power conditions
4.20.1 START STOP UNIT and power conditions overview
The START STOP UNIT command (see 5.31) allows an application client to control the power condition of a
logical unit. This method includes specifying that the logical unit transition to a specific power condition.
In addition to the START STOP UNIT command, the power condition of a logical unit may be controlled by the
Power Condition mode page (see SPC-6). If both the START STOP UNIT command and the Power Condition
mode page methods are being used to control the power condition of the same logical unit, then the power
condition specified by any START STOP UNIT command shall override the Power Condition mode page's
power control.
4.20.2 Processing of concurrent START STOP UNIT commands
If a START STOP UNIT command is being processed by the device server, and a subsequent START STOP
UNIT command for which the CDB is validated requests that the logical unit change to a different power
condition than was specified by the START STOP UNIT command being processed, then the device server
shall terminate the subsequent START STOP UNIT command with CHECK CONDITION status with the
sense key set to NOT READY and the additional sense code set to LOGICAL UNIT NOT READY, START
STOP UNIT COMMAND IN PROGRESS.
The constraints on concurrent START STOP UNIT commands apply only to commands that have the IMMED
bit set to zero. The effects of concurrent power condition changes requested by START STOP UNIT
commands with the IMMED bit set to one are vendor specific.
4.20.3 Managing logical block access commands during a change to the active power condition
Application clients may minimize the return of BUSY status or TASK SET FULL status during a change to the
active power condition by:
a)
polling the power condition using the REQUEST SENSE command (see SPC-6); or
b)
sending a START STOP UNIT command with the IMMED bit set to zero and the START bit set to one
and waiting for GOOD status to be returned.
4.20.4 Stopped power condition
In addition to the active power condition, idle power conditions, and standby power conditions described in
SPC-6, this standard describes the stopped power condition.
While in the stopped power condition:
a)
the device server shall terminate TEST UNIT READY commands and logical block access commands
with CHECK CONDITION status with the sense key set to NOT READY and the additional sense
code set to LOGICAL UNIT NOT READY, INITIALIZING COMMAND REQUIRED;
b)
the power consumed by the SCSI target device while in the stopped power condition should be less
than the power consumed when the logical unit is in the active power condition or any of the idle
power conditions (e.g., for direct access block devices that have a rotating medium, the medium is
stopped in the stopped power condition);
c)
the peak power consumption during a change from the stopped power condition to the active power
condition or an idle power condition is not limited by this standard; and


d)
the peak power consumption during a change from the stopped power condition to a standby power
condition shall be no more than the typical peak power consumption in the active power condition.
No power condition defined in this standard shall affect the supply of any power required for proper operation
of a service delivery subsystem.
4.20.5 START STOP UNIT and power condition state machine
4.20.5.1 START STOP UNIT and power condition state machine overview
The SSU_PC (START STOP UNIT and power condition) state machine for logical units implementing the
START STOP UNIT command describes the:
a)
logical unit power states and transitions resulting from specifications in the START STOP UNIT
command;
b)
settings in the Power Condition mode page (see SPC-6); and
c)
the processing of commands.
NOTE 4 - The SSU_PC state machine is an enhanced version of the PC (power condition) state machine
described in SPC-6.
The SSU_PC state machine consists of the states shown in table 21.
While in the following SSU_PC states, the logical unit may be increasing power usage to enter a higher power
condition:
a)
SSU_PC4:Active_Wait;
b)
SSU_PC7:Idle_Wait; and
c)
SSU_PC9:Standby_Wait.
While in the following SSU_PC states, the logical unit may be decreasing power usage to enter a lower power
condition:
a)
SSU_PC5:Wait_Idle;
b)
SSU_PC6:Wait_Standby; and
Table 21 — Summary of states in the SSU_PC state machine
State
Reference
PC state machine state with additional
definition (see SPC-6)
SSU_PC0:Powered_On a
4.20.5.2
PC0:Powered_On
SSU_PC1:Active
4.20.5.3
PC1:Active
SSU_PC2:Idle
4.20.5.4
PC2:Idle
SSU_PC3:Standby
4.20.5.5
PC3:Standby
SSU_PC4:Active_Wait
4.20.5.6
PC4:Active_Wait
SSU_PC5:Wait_Idle
4.20.5.7
PC5:Wait_Idle
SSU_PC6:Wait_Standby
4.20.5.8
PC6:Wait_Standby
SSU_PC7:Idle_Wait
4.20.5.9
n/a
SSU_PC8:Stopped
4.20.5.10
n/a
SSU_PC9:Standby_Wait
4.20.5.11
n/a
SSU_PC10:Wait_Stopped
4.20.5.12
n/a
a SSU_PC0:Powered_On is the initial state.


c)
SSU_PC10:Wait_Stopped.
Any command causing a state machine transition (e.g., a START STOP UNIT command with the IMMED bit set
to zero) shall not complete with GOOD status until this state machine reaches the state (i.e., power condition)
required or specified by the command.
The SSU_PC state machine shall start in the SSU_PC0:Powered_On state after power on. The SSU_PC
state machine shall be configured to transition to the SSU_PC4:Active_Wait state or the SSU_PC8:Stopped
state after power on by a mechanism not defined by this standard.
This state machine references timers controlled by the Power Condition mode page (see SPC-6) and refers to
the START STOP UNIT command (see 5.31).


Figure 11 describes the SSU_PC state machine.
Figure 11 — SSU_PC state machine
SSU_PC4:
Active_Wait a
SSU_PC0:
Powered_On a
SSU_PC8:
Stopped b
SSU_PC1:
Active a
SSU_PC3:
Standby a
SSU_PC7:
Idle_Wait b
SSU_PC2:
Idle a
SSU_PC10:
Wait_Stopped b
SSU_PC9:
Standby_Wait b
SSU_PC5:
Wait_Idle a
SSU_PC6:
Wait_Standby
a This state or transition is also described in SPC-6, but may have additional characteristics
  unique to this standard (e.g., a transition to or from a state described in this standard).
b This state or transition is described in this standard.


4.20.5.2 SSU_PC0:Powered_On state
4.20.5.2.1 SSU_PC0:Powered_On state description
See the PC0:Powered_On state in SPC-6 for details about this state.
4.20.5.2.2 Transition SSU_PC0:Powered_On to SSU_PC4:Active_Wait
This transition shall occur if:
a)
the logical unit is ready to begin power on initialization; and
b)
the logical unit has been configured to transition to the SSU_PC4:Active_Wait state.
The transition shall include a Transitioning From Powered On argument.
4.20.5.2.3 Transition SSU_PC0:Powered_On to SSU_PC8:Stopped
This transition shall occur if:
a)
the logical unit has been configured to transition to the SSU_PC8:Stopped state.
The transition shall include a Transitioning From Powered On argument.
4.20.5.3 SSU_PC1:Active state
4.20.5.3.1 SSU_PC1:Active state description
See the PC1:Active state in SPC-6 for details about this state.
4.20.5.3.2 Transition SSU_PC1:Active to SSU_PC5:Wait_Idle
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 2h (i.e., IDLE); or
b)
an idle condition timer (see SPC-6) is enabled, and that timer has expired.
The transition shall include a:
a)
Transitioning To Idle_a argument, if:
A) the highest priority timer that expired is the idle_a condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 0h (i.e., idle_a power condition);
b)
Transitioning To Idle_b argument, if:
A) the highest priority timer that expired is the idle_b condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 1h (i.e., idle_b power condition);
or
c)
Transitioning To Idle_c argument, if:
A) the highest priority timer that expired is the idle_c condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 2h (i.e., idle_c power condition).
4.20.5.3.3 Transition SSU_PC1:Active to SSU_PC6:Wait_Standby
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 3h (i.e., STANDBY); or
b)
a standby condition timer (see SPC-6) is enabled and that timer has expired.


The transition shall include a:
a)
Transitioning To Standby_z argument, if:
A) the highest priority timer that expired is the standby_z condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 0h (i.e., standby_z power condition);
or
b)
Transitioning To Standby_y argument, if:
A) the highest priority timer that expired is the standby_y condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 1h (i.e., standby_y power condition).
4.20.5.3.4 Transition SSU_PC1:Active to SSU_PC10:Wait_Stopped
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to zero
and the POWER CONDITION field set to 0h (i.e., START_VALID).
4.20.5.4 SSU_PC2:Idle state
4.20.5.4.1 SSU_PC2:Idle state description
See the PC2:Idle state in SPC-6 for details about this state.
4.20.5.4.2 Transition SSU_PC2:Idle to SSU_PC4:Active_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to one
and the POWER CONDITION field set to 0h (i.e., START_VALID);
b)
the device server processes a START STOP UNIT command with the POWER CONDITION field set to 1h
(i.e., ACTIVE); or
c)
the device server processes a command that requires the logical unit to be in the SSU_PC1:Active
state to continue processing that command.
The transition shall include a:
a)
Transitioning From Idle argument; and
b)
Transitioning From Idle_c argument if the current power condition is the idle_c power condition.
4.20.5.4.3 Transition SSU_PC2:Idle to SSU_PC5:Wait_Idle
This transition shall occur if:
a)
the following occur:
A) an idle condition timer is enabled and that idle condition timer has expired; and
B) the priority of that idle condition timer is greater than the priority of the idle condition timer
associated with the current idle power condition (see SPC-6);
or
b)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 2h (i.e., IDLE) and the POWER CONDITION MODIFIER field set to a value that specifies that the
logical unit transition to a lower idle power condition.
The transition shall include a:
a)
Transitioning To Idle_b argument, if:
A) the highest priority timer that expired is the idle_b condition timer; or


B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 1h (i.e., idle_b power condition);
or
b)
Transitioning To Idle_c argument, if:
A) the highest priority timer that expired is the idle_c condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 2h (i.e., idle_c power condition).
4.20.5.4.4 Transition SSU_PC2:Idle to SSU_PC6:Wait_Standby
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 3h (i.e., STANDBY); or
b)
a standby condition timer is enabled and that timer has expired.
The transition shall include a:
a)
Transitioning To Standby_z argument, if:
A) the highest priority timer that expired is the standby_z condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 0h (i.e., standby_z power condition);
or
b)
Transitioning To Standby_y argument, if:
A) the highest priority timer that expired is the standby_y condition timer; or
B) the START STOP UNIT command being processed has the POWER CONDITION MODIFIER field set
to 1h (i.e., standby_y power condition).
4.20.5.4.5 Transition SSU_PC2:Idle to SSU_PC7:Idle_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 2h (i.e., IDLE) and the POWER CONDITION MODIFIER field set to a value that specifies that the
logical unit transition to a higher idle power condition.
The transition shall include Transitioning From Idle argument and a:
a)
Transitioning To Idle_a argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 0h (i.e., idle_a power condition); or
b)
Transitioning To Idle_b argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 1h (i.e., idle_b power condition).
4.20.5.4.6 Transition SSU_PC2:Idle to SSU_PC10:Wait_Stopped
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to zero
and the POWER CONDITION field set to 0h (i.e., START_VALID).
4.20.5.5 SSU_PC3:Standby state
4.20.5.5.1 SSU_PC3:Standby state description
See the PC3:Standby state in SPC-6 for details about this state.


4.20.5.5.2 Transition SSU_PC3:Standby to SSU_PC4:Active_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to one
and the POWER CONDITION field set to 0h (i.e., START_VALID);
b)
the device server processes a START STOP UNIT command with the POWER CONDITION field set to 1h
(i.e., ACTIVE); or
c)
the device server processes a command that requires the logical unit to be in the SSU_PC1:Active
state to continue processing that command.
The transition shall include a Transitioning From Standby argument.
4.20.5.5.3 Transition SSU_PC3:Standby to SSU_PC6:Wait_Standby
This transition shall occur if:
a)
the following occur:
A) the standby_z condition timer is enabled and that timer expires; and
B) the priority of that standby condition timer is greater than the priority of the standby condition timer
associated with the current standby power condition (see SPC-6);
or
b)
the device server processes a START STOP UNIT command with the POWER CONDITION field set to 3h
(i.e., STANDBY) and the POWER CONDITION MODIFIER field set to a value that specifies that the logical
unit transition to a lower standby power condition.
The transition shall include Transitioning To Standby_z argument.
4.20.5.5.4 Transition SSU_PC3:Standby to SSU_PC7:Idle_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 2h (i.e., IDLE); or
b)
the device server processes a command and determines that the device server is capable of
continuing the processing of that command, when the logical unit is in the SSU_PC2:Idle state.
The transition shall include a Transitioning From Standby argument and a:
a)
Transitioning To Idle_a argument, if:
A) the device server processes a command and determines that the device server is capable of
continuing the processing of that command, when the logical unit is in the idle_a power condition;
or
B) the device server processes a START STOP UNIT command with the POWER CONDITION MODIFIER
field set to 0h (i.e., idle_a power condition);
b)
Transitioning To Idle_b argument, if:
A) the device server processes a command and determines that the device server is capable of
continuing the processing of that command, when the logical unit is in the idle_b power condition;
or
B) the device server processes a START STOP UNIT command with the POWER CONDITION MODIFIER
field set to 1h (i.e., idle_b power condition);
or
c)
Transitioning To_Idle_c argument, if:
A) the device server processes a command and determines that the device server is capable of
continuing the processing of that command, when the logical unit is in the idle_c power condition;
or
B) the device server processes a START STOP UNIT command with the POWER CONDITION MODIFIER
field set to 2h (i.e., idle_c power condition).


4.20.5.5.5 Transition SSU_PC3:Standby to SSU_PC9:Standby_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 3h (i.e., STANDBY) and the POWER CONDITION MODIFIER field set to a value that specifies
that the logical unit transition to a higher standby power condition.
The transition shall include a Transitioning To Standby_y argument.
4.20.5.5.6 Transition SSU_PC3:Standby to SSU_PC10:Wait_Stopped
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to zero
and the POWER CONDITION field set to 0h (i.e., START_VALID).
4.20.5.6 SSU_PC4:Active_Wait state
4.20.5.6.1 SSU_PC4:Active_Wait state description
While in this state:
a)
each idle condition timer that is enabled and not expired is running;
b)
each standby condition timer that is enabled and not expired is running;
c)
the device server shall provide power management pollable sense data (see SPC-6) with the sense
key set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION; and
d)
the logical unit is performing the operations required for it to be in the SSU_PC1:Active state (e.g., a
disk drive spins up its medium).
If this state was entered with a Transitioning From Idle argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero (see 5.31), that the device server is able to
process and complete while in the SSU_PC2:Idle state;
b)
the peak power consumed in this state shall be no more than the typical peak power consumed in the
SSU_PC1:Active state; and
c)
if:
A) this state was entered with a Transitioning From Idle_c argument; and
B) the CCF IDLE field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server shall terminate any command, except a START STOP UNIT command, that
requires the logical unit be in the SSU_PC1:Active state to continue processing, with CHECK
CONDITION status, with the sense key set to NOT READY and the additional sense code set to
LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
If this state was entered with a Transitioning From Standby argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero, that the device server is able to process and
complete while in the SSU_PC3:Standby state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
if the CCF STANDBY field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server shall terminate any command, except a START STOP UNIT command, that
requires the logical unit be in the SSU_PC1:Active state or SSU_PC2:Idle state to continue
processing, with CHECK CONDITION status, with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.


If this state was entered with a Transitioning From Stopped argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero, that the device server is able to process and
complete while in the SSU_PC8:Stopped state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
if the CCF STOPPED field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server shall terminate any TEST UNIT READY command or logical block access
command, with CHECK CONDITION status, with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
If this state was entered with a Transitioning From Powered On argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero or TEST UNIT READY command, that the
device server is able to process and complete while in the SSU_PC8:Stopped state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
the device server shall terminate any TEST UNIT READY command or logical block access
command with CHECK CONDITION status with the sense key set to NOT READY and the additional
sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
If an idle condition timer or a standby condition timer is enabled and expires, then that timer is ignored in this
state.
4.20.5.6.2 Transition SSU_PC4:Active_Wait to SSU_PC1:Active
See the PC4:Active_Wait to PC1:Active transition in SPC-6 for details about this transition.
4.20.5.7 SSU_PC5:Wait_Idle state
4.20.5.7.1 SSU_PC5:Wait_Idle state description
See the PC5:Wait_Idle state in SPC-6 for details about this state.
4.20.5.7.2 Transition SSU_PC5:Wait_Idle to SSU_PC2:Idle
See the PC5:Wait_Idle to PC2:Idle transition in SPC-6 for details about this transition.
4.20.5.8 SSU_PC6:Wait_Standby state
4.20.5.8.1 SSU_PC6:Wait_Standby state description
See the PC6:Wait_Standby state in SPC-6 for details about this state.
4.20.5.8.2 Transition SSU_PC6:Wait_Standby to SSU_PC3:Standby
See the PC6:Wait_Standby to PC3:Standby transition in SPC-6 for details about this transition.
4.20.5.9 SSU_PC7:Idle_Wait state
4.20.5.9.1 SSU_PC7:Idle_Wait state description
While in this state:
a)
each idle condition timer that is enabled and not expired is running;
b)
each standby condition timer that is enabled and not expired is running;
c)
the device server shall provide power management pollable sense data (see SPC-6) with the sense
key set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION; and


d)
the logical unit is performing the operations required for it to be in the SSU_PC2:Idle state (e.g., a disk
drive spins up its medium).
If this state was entered with a Transitioning From Idle argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero (see 5.31), that the device server is able to
process and complete while in the SSU_PC2:Idle state; and
b)
the peak power consumed in this state shall be no more than the typical peak power consumed in the
SSU_PC1:Active state.
If this state was entered with a Transitioning From Standby argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero, that the device server is able to process and
complete while in the SSU_PC3:Standby state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
the CCF STANDBY field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server shall terminate any command, except a START STOP UNIT command, that
requires the logical unit be in the SSU_PC1:Active state or SSU_PC2:Idle state to continue
processing, with CHECK CONDITION status, with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
If this state was entered with a Transitioning From Stopped argument, then:
a)
the device server is capable of processing and completing the same commands, except START
STOP UNIT commands with the IMMED bit set to zero, that the device server is able to process and
complete while in the SSU_PC8:Stopped state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
if the CCF STOPPED field in the Power Condition mode page (see SPC-6) is set to 10b (i.e., enabled),
then the device server shall terminate any TEST UNIT READY command or logical block access
command, with CHECK CONDITION status, with the sense key set to NOT READY and the
additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY.
If an idle condition timer or a standby condition timer is enabled and expires, then that timer is ignored in this
state.
4.20.5.9.2 Transition SSU_PC7:Idle_Wait to SSU_PC2:Idle
This transition shall occur when the logical unit meets the requirements for being in the:
a)
idle_a power condition, if this state was entered with a Transitioning To Idle_a argument;
b)
idle_b power condition, if this state was entered with a Transitioning To Idle_b argument; or
c)
idle_c power condition, if this state was entered with a Transitioning To Idle_c argument.
4.20.5.10 SSU_PC8:Stopped state
4.20.5.10.1 SSU_PC8:Stopped state description
While in this state:
a)
the logical unit is in the stopped power condition (see 4.20.4);
b)
the idle condition timers and the standby condition timers are disabled;
c)
the device server shall provide power management pollable sense data (see SPC-6); and
d)
the device server terminates each logical block access command or TEST UNIT READY command
(see SPC-6) as described in 4.20.4.


4.20.5.10.2 Transition SSU_PC8:Stopped to SSU_PC4:Active_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the START bit set to one
and the POWER CONDITION field set to 0h (i.e., START_VALID); or
b)
the device server processes a START STOP UNIT command with the POWER CONDITION field set to 1h
(i.e., ACTIVE).
The transition shall include a Transitioning From Stopped argument.
4.20.5.10.3 Transition SSU_PC8:Stopped to SSU_PC7:Idle_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 2h (i.e., IDLE).
The transition shall include a Transitioning From Stopped argument and a:
a)
Transitioning To Idle_a argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 0h (i.e., idle_a power condition);
b)
Transitioning To Idle_b argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 1h (i.e., idle_b power condition); or
c)
Transitioning To Idle_c argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 2h (i.e., idle_c power condition).
4.20.5.10.4 Transition SSU_PC8:Stopped to SSU_PC9:Standby_Wait
This transition shall occur if:
a)
the device server processes a START STOP UNIT command (see 5.31) with the POWER CONDITION
field set to 3h (i.e., STANDBY).
The transition shall include a Transitioning From Stopped argument and a:
a)
Transitioning To Standby_z argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 0h (i.e., standby_z power condition); or
b)
Transitioning To Standby_y argument, if the START STOP UNIT command being processed has the
POWER CONDITION MODIFIER field set to 1h (i.e., standby_y power condition).
4.20.5.11 SSU_PC9:Standby_Wait state
4.20.5.11.1 SSU_PC9:Standby_Wait state description
While in this state:
a)
the device server shall provide power management pollable sense data (see SPC-6) with the sense
key set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION;
b)
the peak power consumed in this state shall be no more than the typical peak power consumed in the
SSU_PC1:Active state; and
c)
the logical unit is performing the operations required for it to be in the SSU_PC3:Standby state ((e.g.,
a direct access block device is activating circuitry).
If this state was entered with a Transitioning From Standby argument, then the device server is capable of
processing and completing the same commands, except START STOP UNIT commands with the IMMED bit
set to zero (see 5.31), that the device server is able to process and complete in the SSU_PC3:Standby state.
