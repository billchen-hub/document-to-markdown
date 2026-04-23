# 5.12.8 Power condition state machine

D) STANDBY CONDITION ACTIVATED BY TIMER if the logical unit entered the standby_z power
condition due to the standby_z condition timer (see 5.12.8.5); or
E)
STANDBY_Z CONDITION ACTIVATED BY COMMAND if the logical unit entered the standby_y
power condition due to processing of a command;
or
c)
if the logical unit is in the stopped power condition (see SBC-3), then the sense key shall be set to
NOT READY and the additional sense code shall be set to LOGICAL UNIT NOT READY, INITIAL-
IZING COMMAND REQUIRED.
NOTE 12 - Device servers that conform to SBC-2 may not provide the pollable sense data described in c).
5.12.8 Power condition state machine
5.12.8.1 Power condition state machine overview
The power condition state machine describes the logical unit power states and transitions resulting from
command processing and Power Condition mode page values (see 7.5.13).
The power condition state machine states are shown in table 63.
While in the following power condition state machine states the logical unit may be increasing power usage to
enter a higher power condition:
a)
PC4:Active_Wait.
While in the following power condition state machine states the logical unit may be decreasing power usage to
enter a lower power condition:
a)
PC5:Wait_Idle; and
b)
PC6:Wait_Standby.
Table 63 — Power condition state machine states
State
Reference
PC0:Powered_On a
5.12.8.2
PC1:Active
5.12.8.3
PC2:Idle
5.12.8.4
PC3:Standby
5.12.8.5
PC4:Active_Wait
5.12.8.6
PC5:Wait_Idle
5.12.8.7
PC6:Wait_Standby
5.12.8.8
a PC0:Powered_On is the initial state.


The power condition state machine maintains the timers listed in table 64.
If more than one of the timers listed in table 64 expire at the same time, then only one timer is processed. The
processing priority order shall be as follows:
1)
standby_z condition timer;
2)
standby_y condition timer;
3)
idle_c condition timer;
4)
idle_b condition timer; and
5)
idle_a condition timer.
The power condition state machine shall start in the PC0:Powered_On state after power on.
Figure 8 describes the power condition state machine.
Table 64 — Power condition state machine timers
Timer
Initial value a
Enable bit  a, b
idle_a condition
IDLE_A CONDITION TIMER field
IDLE_A bit
idle_b condition
IDLE_B CONDITION TIMER field
IDLE_B bit
idle_c condition
IDLE_C CONDITION TIMER field
IDLE_C bit
standby_y condition
STANDBY_Y CONDITION TIMER field
STANDBY_Y bit
standby_z condition
STANDBY_Z CONDITION TIMER field
STANDBY_Z bit
a These fields and bits are in the Power Condition mode page (see 7.5.13).
b The enabled state of these bits may be overridden by a START STOP UNIT
command (see SBC-3).
Figure 8 — Power condition state machine
PC0:
Powered_On
PC4:
Active_Wait
PC1:
Active
PC5:
Wait_Idle
PC2:
Idle
PC6:
Wait_Standby
PC3:
Standby


5.12.8.2 PC0:Powered_On state
5.12.8.2.1 PC0:Powered_On state description
The logical unit shall enter this state upon power on.
5.12.8.2.2 Transition PC0:Powered_On to PC4:Active_Wait
This transition shall occur after:
a)
the logical unit is ready to begin power on initialization.
The transition shall include a Transitioning From Powered On argument.
5.12.8.3 PC1:Active state
5.12.8.3.1 PC1:Active state description
While in this state, if power on initialization is not complete, then the logical unit shall complete its power on
initialization.
While in this state, if power on initialization is complete, then:
a)
the logical unit is in the active power condition (see 5.12.4);
b)
each enabled idle condition timer is running; and
c)
each enabled standby condition timer is running.
5.12.8.3.2 Transition PC1:Active to PC5:Wait_Idle
This transition shall occur if:
a)
an idle condition timer is enabled; and
b)
that idle condition timer has expired.
The transition shall include a:
a)
Transitioning To Idle_a argument, if the highest priority timer (see 5.12.8.1) that expired is the idle_a
condition timer;
b)
Transitioning To Idle_b argument, if the highest priority timer that expired is the idle_b condition timer;
or
c)
Transitioning To Idle_c argument, if the highest priority timer that expired is the idle_c condition timer.
5.12.8.3.3 Transition PC1:Active to PC6:Wait_Standby
This transition shall occur if:
a)
a standby condition timer is enabled; and
b)
that standby condition timer has expired.
The transition shall include a:
a)
Transitioning To Standby_z argument, if the highest priority timer (see 5.12.8.1) that expired is the
standby_z condition timer; or


b)
Transitioning To Standby_y argument, if the highest priority timer that expired is the standby_y
condition timer.
5.12.8.4 PC2:Idle state
5.12.8.4.1 PC2:Idle state description
While in this state:
a)
the logical unit is in an idle power condition (see 5.12.5);
b)
the device server shall provide power condition pollable sense data (see 5.12.7);
c)
each enabled idle condition timer that has not expired is running; and
d)
each enabled standby condition timer that has not expired is running.
If a lower priority (see 5.12.8.1) idle condition timer is enabled and expires, then that timer is ignored.
5.12.8.4.2 Transition PC2:Idle to PC4:Active_Wait
This transition shall occur if:
a)
the device server processes a command that requires the logical unit to be in the PC1:Active state to
continue processing that command.
The transition shall include a:
a)
Transitioning From Idle argument; and
b)
Transitioning From Idle_c argument, if the current power condition is the idle_c power condition.
5.12.8.4.3 Transition PC2:Idle to PC5:Wait_Idle
This transition shall occur if:
a)
an idle condition timer is enabled;
b)
that idle condition timer has expired; and
c)
the priority (see 5.12.8.1) of that idle condition timer is greater than the priority of the idle condition
timer associated with the current idle power condition.
The transition shall include a:
a)
Transitioning To Idle_b argument, if the highest priority timer that expired is the idle_b condition timer;
or
b)
Transitioning To Idle_c argument, if the highest priority timer that expired is the idle_c condition timer.
5.12.8.4.4 Transition PC2:Idle to PC6:Wait_Standby
This transition shall occur if:
a)
a standby condition timer is enabled; and
b)
that standby condition timer has expired.
The transition shall include a:
a)
Transitioning To Standby_z argument, if the highest priority timer (see 5.12.8.1) that expired is the
standby_z condition timer; or


b)
Transitioning To Standby_y argument, if the highest priority timer that expired is the standby_y
condition timer.
5.12.8.5 PC3:Standby state
5.12.8.5.1 PC3:Standby state description
While in this state:
a)
the logical unit is in a standby power condition (see 5.12.6);
b)
the device server shall provide power condition pollable sense data (see 5.12.7);
c)
each enabled idle condition timer that has not expired is running; and
d)
each enabled standby condition timer that has not expired is running.
If an idle condition timer or a lower priority (see 5.12.8.1) standby condition timer is enabled and expires, then
that timer is ignored.
5.12.8.5.2 Transition PC3:Standby to PC4:Active_Wait
This transition shall occur if:
a)
the device server processes a command that requires the logical unit to be in the PC1:Active state to
continue processing that command.
The transition shall include a Transitioning From Standby argument.
5.12.8.5.3 Transition PC3:Standby to PC6:Wait_Standby
This transition shall occur if:
a)
the standby_z condition timer is enabled;
b)
the standby_z condition timer expires; and
c)
the current power condition is the standby_y power condition.
The transition shall include a Transitioning To Standby_z argument.
5.12.8.6 PC4:Active_Wait state
5.12.8.6.1 PC4:Active_Wait state description
While in this state:
a)
each idle condition timer that is enabled and not expired is running;
b)
each standby condition timer that is enabled and not expired is running;
c)
the device server shall provide power condition pollable sense data (see 5.12.7) with the sense key
set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION; and
d)
the logical unit is performing the operations required for it to be in the PC1:Active state (e.g., a disk
drive spins up its media).
If this state was entered with a Transitioning From Idle argument, then:
a)
the device server is capable of processing and completing the same commands that the device server
is able to process and complete while in the PC2:Idle state;


b)
the peak power consumed in this state shall be no more than the typical peak power consumed in the
PC1: Active state; and
c)
the device server shall terminate any command that requires the logical unit be in the PC1:Active
state to continue processing, with CHECK CONDITION status, with the sense key set to NOT READY
and the additional sense code set to LOGICAL UNIT IS IN PROCESS OF BECOMING READY if all
of the following are true:
A)
this state was entered with a Transitioning From Idle_c argument; and
B)
the CCF IDLE field in the Power Condition mode page (see 7.5.13) is set to 10b (i.e., enabled).
If this state was entered with a Transitioning From Standby argument, then:
a)
the device server is capable of processing and completing the same commands that the device server
is able to process and complete while in the PC3:Standby state;
b)
the peak power consumption in this state is not limited by this standard; and
c)
if the CCF STANDBY field in the Power Condition mode page (see 7.5.13) is set to 10b (i.e. enabled),
then the device server shall terminate any command that requires the logical unit be in the PC1:Active
state or PC2:Idle state to continue processing, with CHECK CONDITION status, with the sense key
set to NOT READY and the additional sense code set to LOGICAL UNIT IN THE PROCESS OF
BECOMING READY.
If this state was entered with a Transitioning From Powered On argument, then:
a)
the device server is capable of processing and completing the same commands (except a TEST UNIT
READY command) that the device server is able to process and complete while in the PC3:Standby
state; and
b)
the device server shall terminate with CHECK CONDITION status, with the sense key set to NOT
READY and the additional sense code set to LOGICAL UNIT IN THE PROCESS OF BECOMING
READY any of the following commands:
A)
any command that requires the logical unit be in the PC1:Active state or PC2:Idle state to
continue processing; and
B)
all TEST UNIT READY commands (see 6.47).
If an idle condition timer or a standby condition timer is enabled and expires, then that timer is ignored in this
state.
5.12.8.6.2 Transition PC4:Active_Wait to PC1:Active
This transition shall occur if:
a)
the logical unit meets the requirements for being in the PC1:Active state.
5.12.8.7 PC5:Wait_Idle state
5.12.8.7.1 PC5:Wait_Idle state description
While in this state:
a)
each idle condition timer that is enabled and not expired is running;
b)
each standby condition timer that is enabled and not expired is running;
c)
the device server shall provide power condition pollable sense data (see 5.12.7) with the sense key
set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION;
d)
the logical unit is performing the operations required for it to be in the PC2:Idle state (e.g., reducing
power usage); and


e)
the device server is capable of processing and completing the same commands, except a START
STOP UNIT command with the IMMED bit set to zero (see SBC-3), that the device server is able to
process and complete in the PC2:Idle state.
If an idle condition timer or a standby condition timer is enabled and expires, then that timer is ignored in this
state.
5.12.8.7.2 Transition PC5:Wait_Idle to PC2:Idle
This transition shall occur if:
a)
the logical unit meets the requirements for being in the:
A)
idle_a power condition, if this state was entered with a Transitioning To Idle_a argument;
B)
idle_b power condition, if this state was entered with a Transitioning To Idle_b argument; or
C) idle_c power condition, if this state was entered with a Transitioning To Idle_c argument.
5.12.8.8 PC6:Wait_Standby state
5.12.8.8.1 PC6:Wait_Standby state description
While in this state:
a)
each idle condition timer that is enabled and not expired is running;
b)
each standby condition timer that is enabled and not expired is running;
c)
the device server shall provide power condition pollable sense data (see 5.12.7) with the sense key
set to NO SENSE and the additional sense code set to LOGICAL UNIT TRANSITIONING TO
ANOTHER POWER CONDITION;
d)
the logical unit is performing the operations required for it to be in the PC3:Standby state (e.g.,
reducing power usage); and
e)
the device server is capable of processing and completing the same commands, except a START
STOP UNIT command with the IMMED bit set to zero (see SBC-3), that the device server is able to
process and complete in the PC3:Standby state.
If an idle condition timer or a standby condition timer is enabled and expires, then that timer is ignored in the
state.
5.12.8.8.2 Transition PC6:Wait_Standby to PC3:Standby
This transition shall occur if:
a)
the logical unit meets the requirements for being in the:
A)
standby_y power condition, if this state was entered with a Transitioning To Standby_y argument;
or
B)
standby_z power condition, if this state was entered with a Transitioning To Standby_z argument.
