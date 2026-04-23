# 5.16.2 Asymmetric logical unit access

If referrals are supported (see SBC-3), then a logical unit accessed through a target port group may have
different target port group asymmetric access states based on the user data segments being accessed.
5.16.2 Asymmetric logical unit access
5.16.2.1 Introduction to asymmetric logical unit access
Asymmetric logical unit access occurs when the access characteristics of one port may differ from those of
another port. SCSI target devices with target ports implemented in separate physical units may need to
designate differing levels of access for the target ports associated with each logical unit. While commands and
task management functions (see SAM-5) may be routed to a logical unit through any target port, the perfor-
mance may not be optimal, and the allowable command set may be less complete than when the same
commands and task management functions are routed through a different target port. In addition, some target
ports may be in a state (e.g., offline) that is unique to that target port. If a failure on the path to one target port
is detected, the SCSI target device may perform automatic internal reconfiguration to make a logical unit
accessible from a different set of target ports or may be instructed by the application client to make a logical
unit accessible from a different set of target ports.
A target port characteristic called primary target port asymmetric access state (see 5.16.2.4) defines
properties of a target port and the allowable command set for a logical unit when commands and task
management functions are routed through the target port maintaining that state.
A primary target port group is defined as a set of target ports that are in the same primary target port
asymmetric access state at all times (i.e., a change in one target port’s primary target port asymmetric access
state implies an equivalent change in the primary target port asymmetric access state of all target ports in the
same primary target port group). A primary target port group asymmetric access state is defined as the
primary target port asymmetric access state common to the set of target ports in a primary target port group.
One target port is a member of at most one primary target port group for a logical unit group (see 7.8.6.9). The
grouping of target ports in a primary target port group is vendor specific.
A logical unit may have commands and task management functions routed through multiple primary target
port groups. Logical units support asymmetric logical unit access if different primary target port groups may be
in different primary target port group asymmetric access states.
An example of asymmetric logical unit access is a SCSI controller device with two separated controllers where
all target ports on one controller are in the same primary target port asymmetric access state with respect to a
logical unit and are members of the same primary target port group. Target ports on the other controller are
members of another primary target port group. The behavior of each primary target port group may be
different with respect to a logical unit, but all members of a single primary target port group are always in the
same primary target port group asymmetric access state with respect to a logical unit.


An example of primary target port groups is shown in figure 16.
Another target port characteristic called secondary target port asymmetric access state (see 5.16.2.4)
indicates a condition that affects the way in which an individual target port participates in its assigned primary
target port group. All target ports, if any, in one secondary target port asymmetric access state are grouped
into a secondary target port group. Secondary target port groups have the following properties:
a)
a target port in any secondary target port group also shall be in one primary target port group;
b)
a change of secondary target port asymmetric access state for one target port shall not cause
changes in the secondary target port asymmetric access state of other target ports, if any, in the same
secondary target port group; and
c)
a target port may be a member of zero or more secondary target port groups.
The term target port asymmetric access state represents both primary target port asymmetric access states
and secondary target port asymmetric access states. The term target port group represents both primary
target port groups and secondary target port groups.
5.16.2.2 Explicit and implicit asymmetric logical unit access
Asymmetric logical unit access may be managed explicitly by an application client using the REPORT
TARGET PORT GROUPS (see 6.37) and SET TARGET PORT GROUPS (see 6.45) commands.
Alternatively, asymmetric logical unit access may be managed implicitly by the SCSI target device based on
the type of transactions being routed through each target port and the internal configuration capabilities of the
primary target port group(s) through which the logical unit may be accessed. The logical units may attempt to
maintain full performance across the primary target port groups that are busiest and that show the most
reliable performance, allowing other primary target port groups to select a lower performance primary target
port asymmetric access state.
Implicit management of secondary target port asymmetric access states is based on the condition of an
individual target port and how such conditions affect that target port’s ability to participate in its assigned
primary target port group.
If both explicit and implicit asymmetric logical unit access management methods are implemented, the prece-
dence of one over the other is vendor specific.
Figure 16 — Primary target port group example
Primary
Target Port
Group 1
Target
Port 1
●   ●   ●
Target
Port 2
Target
Port n
Primary
Target Port
Group n
Logical Unit


5.16.2.3 Discovery of asymmetric logical unit access behavior
SCSI logical units with asymmetric logical unit access may be identified using the INQUIRY command. The
value in the target port group support (TPGS) field (see 6.6.2) indicates whether or not the logical unit supports
asymmetric logical unit access and if so whether implicit or explicit management is supported. The target port
asymmetric access states supported by a logical unit may be determined by the REPORT TARGET PORT
GROUPS command parameter data (see 6.37).
5.16.2.4 Target port asymmetric access states
5.16.2.4.1 Target port asymmetric access states overview
For all SCSI target devices that report in the INQUIRY data that they support asymmetric logical unit access,
all of the target ports in a primary target port group (see 5.16.2.1) shall be in the same primary target port
asymmetric access state with respect to the ability to route information to a logical unit. The primary target port
asymmetric access states are:
a)
active/optimized;
b)
active/non-optimized;
c)
standby;
d)
unavailable; and
e)
logical block dependent.
Individual target ports may be in secondary target port groups (see 5.16.2.1) that have the following
secondary target port asymmetric access states:
a)
offline.
5.16.2.4.2 Active/optimized state
The active/optimized state is a primary target port asymmetric access state. While commands and task
management functions are being routed through a target port in the active/optimized primary target port
asymmetric access state, the device server shall function (e.g., respond to commands) as specified in the
appropriate command standards. All target ports within a primary target port group should be capable of
immediately accessing the logical unit.
The SCSI target device shall participate in all task management functions as defined in SAM-5 and modified
by the applicable SCSI transport protocol standards.
5.16.2.4.3 Active/non-optimized state
The active/non-optimized state is a primary target port asymmetric access state. While commands and task
management functions are being routed through a target port in the active/non-optimized primary target port
asymmetric access state, the device server shall function as specified in the appropriate command standards.
The processing of some task management functions and commands, especially those involving data transfer
or caching, may operate with lower performance than they would if the target port were in the active/optimized
primary target port asymmetric access state.
The SCSI target device shall participate in all task management functions as defined in SAM-5 and modified
by the applicable SCSI transport protocol standards.


5.16.2.4.4 Standby state
The standby state is a primary target port asymmetric access state. While being accessed through a target
port in the standby primary target port asymmetric access state, the device server shall support those of the
following commands that it supports while in the active/optimized primary target port asymmetric access state:
a)
INQUIRY;
b)
LOG SELECT;
c)
LOG SENSE;
d)
MODE SELECT;
e)
MODE SENSE;
f)
REPORT LUNS;
g)
RECEIVE DIAGNOSTIC RESULTS;
h)
SEND DIAGNOSTIC;
i)
REPORT TARGET PORT GROUPS;
j)
SET TARGET PORT GROUPS;
k)
REQUEST SENSE;
l)
PERSISTENT RESERVE IN;
m) PERSISTENT RESERVE OUT;
n)
echo buffer modes of READ BUFFER; and
o)
echo buffer modes of WRITE BUFFER.
The device server may support other commands.
For those commands that are not supported, the device server shall terminate the command with CHECK
CONDITION status, with the sense key set to NOT READY, and the additional sense code set to LOGICAL
UNIT NOT ACCESSIBLE, TARGET PORT IN STANDBY STATE.
The SCSI target device shall participate in all task management functions as defined in SAM-5 and modified
by the applicable SCSI transport protocol standards.
5.16.2.4.5 Unavailable state
The unavailable state is a primary target port asymmetric access state. While being accessed through a target
port in the unavailable primary target port asymmetric access state, the device server shall accept only a
limited set of commands. The unavailable primary target port asymmetric access state is intended for situa-
tions where the target port accessibility to a logical unit may be severely constrained due to SCSI target
device limitations (e.g., hardware errors). Therefore it may not be possible to transition from this state to either
the active/optimized, active/non-optimized or standby states. The unavailable primary target port asymmetric
access state is also intended for minimizing any disruption where using the downloading microcode mode of
the WRITE BUFFER command.
While in the unavailable primary target port asymmetric access state, the device server shall support those of
the following commands that it supports while in the active/optimized state:
a)
INQUIRY (the peripheral qualifier (see 6.6.2) shall be set to 001b);
b)
REPORT LUNS;
c)
REPORT TARGET PORT GROUPS;
d)
SET TARGET PORT GROUPS;
e)
REQUEST SENSE;
f)
echo buffer modes of READ BUFFER;
g)
echo buffer modes of WRITE BUFFER; and
h)
download microcode mode of WRITE BUFFER.


The device server may support other commands.
For those commands that are not supported, the device server shall terminate the command with CHECK
CONDITION status, with the sense key set to NOT READY, and the additional sense code set to LOGICAL
UNIT NOT ACCESSIBLE, TARGET PORT IN UNAVAILABLE STATE.
The SCSI target device is not required to participate in all task management functions (see SAM-5 and the
applicable SCSI transport protocol standards).
5.16.2.4.6 Offline state
The offline state is a secondary target port asymmetric access state. Target ports in the offline secondary
target port asymmetric access state are not accessible via the service delivery subsystem (e.g. during mainte-
nance, port replacement, port disabled, hot swap, or power failures impacting only some target port). While in
the offline secondary target port asymmetric state, the target port is not capable of receiving or responding to
any commands or task management functions.
The offline secondary target port asymmetric access state allows a device server to report that some target
ports are not capable of being accessed.
After access to the service delivery subsystem is enabled, the target port shall transition out of the offline
secondary target port asymmetric access state.
5.16.2.4.7 Logical block dependent state
The logical block dependent state only occurs if the device server supports referrals (see 7.8.7).
The target port asymmetric access state for a user data segment shall be one of the following target port
asymmetric access states:
a)
active/optimized;
b)
active/non-optimized;
c)
transitioning; or
d)
unavailable.
An application client may determine the target port asymmetric access state for user data segments by issuing
a REPORT REFERRALS command (see SBC-3).
5.16.2.5 Transitions between target port asymmetric access states
The movement from one target port asymmetric access state to another is called a transition.
During a transition between target port asymmetric access states the device server shall respond to a
command in one of the following ways:
a)
if during the transition the logical unit is inaccessible, then the transition is performed as a single
indivisible event and the device server shall respond by either returning BUSY status, or returning
CHECK CONDITION status, with the sense key set to NOT READY, and the sense code set to
LOGICAL UNIT NOT ACCESSIBLE, ASYMMETRIC ACCESS STATE TRANSITION; or
b)
if during the transition the target ports in a primary target port group are able to access the requested
logical unit, then the device server shall support those of the following commands that it supports
while in the active/optimized primary target port asymmetric access state:
A)
INQUIRY;
B)
REPORT LUNS;


C) REPORT TARGET PORT GROUPS;
D) REQUEST SENSE;
E)
echo buffer modes of READ BUFFER; and
F)
echo buffer modes of WRITE BUFFER.
The device server may support other commands when those commands are routed though a target
port that is transitioning between primary target port asymmetric access states.
For those commands that are not supported during a transition, the device server shall terminate the
command with CHECK CONDITION status, with the sense key set to NOT READY, and the additional
sense code set to LOGICAL UNIT NOT ACCESSIBLE, ASYMMETRIC ACCESS STATE
TRANSITION.
The SCSI target device is not required to participate in all task management functions.
If the transition was explicit to a supported target port asymmetric access state and it failed, then the device
server shall terminate the command with CHECK CONDITION status, with the sense key set to HARDWARE
ERROR, and the additional sense code set to SET TARGET PORT GROUPS COMMAND FAILED. If the
transition was to a primary target port asymmetric access stated, the primary target port group that encoun-
tered the error should complete a transition to the unavailable primary target port asymmetric access state.
If a target port asymmetric access state change occurred as a result of the failed transition, then the device
server shall establish a unit attention condition for the initiator port associated with every I_T nexus other than
the I_T nexus on which the SET TARGET PORT GROUPS command was received with the additional sense
code set to ASYMMETRIC ACCESS STATE CHANGED.
If the transition was implicit and it failed, then the device server shall establish a unit attention condition for the
initiator port associated with every I_T nexus with the additional sense code set to IMPLICIT ASYMMETRIC
ACCESS STATE TRANSITION FAILED.
An implicit CLEAR TASK SET task management function may be performed following a transition failure.
Once a transition is completed, the new target port asymmetric access state may apply to some or all
commands entered into the task set before the completion of the transition. The new target port asymmetric
access state shall apply to all commands received by the device server after completion of a transition.
If a transition is to the offline secondary target port asymmetric access state, communication with the service
delivery subsystem shall be terminated. This may result in commands being terminated and may cause
command timeouts to occur on the initiator.
After an implicit target port asymmetric access state change, a device server shall establish a unit attention
condition for the initiator port associated with every I_T nexus with the additional sense code set to
ASYMMETRIC ACCESS STATE CHANGED.
After an explicit target port asymmetric access state change, a device server shall establish a unit attention
condition with the additional sense code set to ASYMMETRIC ACCESS STATE CHANGED for the initiator
port associated with every I_T nexus other than the I_T nexus on which the SET TARGET PORT GROUPS
command was received.
5.16.2.6 Preference Indicator
A device server may indicate one or more primary target port groups is a preferred primary target port group
for accessing a logical unit by setting the PREF bit to one in the target port group descriptor (see 6.37). The
preference indication is independent of the primary target port asymmetric access state.


An application client may use the PREF bit value in the target port group descriptor to influence the path
selected to a logical unit (e.g., a primary target port group in the standby primary target port asymmetric
access state with the PREF bit set to one may be chosen over a primary target port group in the
active/optimized primary target port asymmetric access state with the PREF bit set to zero).
The value of the PREF bit for a primary target port group may change whenever an primary target port
asymmetric access state changes.
5.16.2.7 Implicit asymmetric logical units access management
SCSI target devices with implicit asymmetric logical units access management are capable using mecha-
nisms other than the SET TARGET PORT GROUPS command to set the:
a)
primary target port asymmetric access state of a primary target port group; or
b)
secondary target port asymmetric access state of a target port that is a member of a primary target
port group.
All logical units that report in the standard INQUIRY data (see 6.6.2) that they support asymmetric logical units
access and support implicit asymmetric logical unit access (i.e., the TPGS field is set to 01b or 11b):
a)
shall implement the INQUIRY command Device Identification VPD page designator types 4h (see
7.8.6.7) and 5h (see 7.8.6.8);
b)
shall support the REPORT TARGET PORT GROUPS command as described in 6.37; and
c)
may implement the INQUIRY command Device Identification VPD page designator type 6h (see
7.8.6.9).
Implicit logical unit access state changes between primary target port asymmetric access states may be
disabled with the IALUAE bit in the Control Extension mode page (see 7.5.9).
5.16.2.8 Explicit asymmetric logical units access management
All logical units that report in the standard INQUIRY data (see 6.6.2) that they support asymmetric logical units
access and support explicit asymmetric logical unit access (i.e., the TPGS field is set to 10b or 11b):
a)
shall implement the INQUIRY command Device Identification VPD page (see 7.8.6) designator types
4h and 5h;
b)
shall support the REPORT TARGET PORT GROUPS command as described in 6.37;
c)
shall support the SET TARGET PORT GROUPS command as described in 6.45; and
d)
may implement the INQUIRY command Device Identification VPD page designator type 6h (see
7.8.6.9).
5.16.2.9 Behavior after power on, hard reset, logical unit reset, and I_T nexus loss
For all SCSI target devices that report in the standard INQUIRY data (see 6.6.2) that they support only explicit
asymmetric logical unit access (i.e., the TPGS field is set to 10b), the target port shall preserve the primary
target port asymmetric access state during any power on, hard reset, logical unit reset, and I_T nexus loss.
5.16.2.10 Behavior of target ports that are not accessible from the service delivery subsystem
If the offline secondary target port asymmetric access state is supported and a subset of the target ports in a
primary target port group are not accessible via the service delivery subsystem (e.g. power failure), then those
ports may be reported in a primary target port group consistent with their primary target port asymmetric
access state and in the secondary target port group with the offline secondary target port asymmetric access
state.
