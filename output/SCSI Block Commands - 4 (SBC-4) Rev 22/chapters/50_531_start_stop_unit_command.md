# 5.31 START STOP UNIT command

CHECK CONDITION status with the sense key set to ABORTED COMMAND and the appropriate
additional sense code for the condition (e.g., for READ commands, the additional sense code shown
in table 79);
b)
the device server should complete reads to unmapped LBAs without error (see 4.7.4.6.1 and
4.7.4.7.1);
c)
if the logical unit is a zoned block device and the ZNR bit in the CDB is set to zero then:
A) the device server shall perform the equivalent of a RESET WRITE POINTER command (see
ZBC-2) with the ALL bit set to one; and
B) for each write pointer zone, if the reset write pointer operation is not successful, then the Zone
Condition (see ZBC-2) shall be set to OFFLINE;
and
d)
if the logical unit is a zoned block device and the ZNR bit in the CDB is set to one then, for any write
pointer zone where the write pointer was not reset as part of the failed SANITIZE command, the
device server shall not modify the write pointer (see ZBC-2).
5.31 START STOP UNIT command
The START STOP UNIT command (see table 113) requests that the device server change the power
condition of the logical unit (see 4.20) or load or eject the medium. This includes specifying that the device
server enable or disable the direct access block device for medium access operations by controlling power
conditions and timers.
The device server shall handle any deferred microcode as specified in 4.24.
The OPERATION CODE field is defined in SPC-6 and shall be set to the value shown in table 113 for the START
STOP UNIT command.
If the immediate (IMMED) bit is set to zero, then the device server shall return status after the operation is
completed. If the IMMED bit is set to one, then the device server shall return status as soon as the CDB has
been validated.
Table 113 — START STOP UNIT command
Bit
Byte
OPERATION CODE (1Bh)
Reserved
IMMED
Reserved
Reserved
POWER CONDITION MODIFIER
POWER CONDITION
Reserved
NO_FLUSH
LOEJ
START
CONTROL


The combinations of values in the POWER CONDITION field and the POWER CONDITION MODIFIER field are shown
in table 114. If the POWER CONDITION field is supported and is set to a value other than 0h, then the device
server shall ignore the START bit and the LOEJ bit.
Table 114 — POWER CONDITION and POWER CONDITION MODIFIER field (part 1 of 2)
 POWER
CONDITION
value
POWER
CONDITION
name
POWER
CONDITION
MODIFIER
value
Device server action
0h
START_
VALID
0h
Process the START bit and the LOEJ bit.
1h
ACTIVE
0h
Cause the logical unit to transition to the active power condition. a
2h
IDLE
0h
Cause the logical unit to transition to the idle_a power condition. a b
1h
Cause the logical unit to transition to the idle_b power condition. a b c
2h
Cause the logical unit to transition to the idle_c power condition. a b d
3h
STANDBY
0h
Cause the logical unit to transition to the standby_z power
condition. a b
1h
Cause the logical unit to transition to the standby_y power
condition. a b
5h
Obsolete
0h to Fh
Obsolete
7h
LU_
CONTROL
0h
Initialize and start all of the idle condition timers that are enabled
(see SPC-6), and initialize and start all of the standby condition
timers that are enabled (see SPC-6).
a Process the following actions:
1)
the device server shall comply with any SCSI transport protocol specific power condition transition
restrictions (e.g., the NOTIFY (ENABLE SPINUP) requirement (see SPL-5));
2)
the logical unit shall transition to the specified power condition; and
3)
the device server shall disable all of the idle condition timers that are enabled (see SPC-6) and
disable all of the standby condition timers that are enabled (see SPC-6) until another START STOP
UNIT command is processed that returns control of the power condition to the logical unit or a logical
unit reset occurs.
b If a timer for a background scan operation expires, or a device specific event occurs, then the logical unit
shall not leave this power condition to perform the background function associated with the timer or
event.
c The device server shall cause the direct access block device to increase its tolerance of external physical
forces (e.g., causes a device that has movable read/write heads to move those heads to a safe position).
d The device server shall cause the direct access block device to increase its tolerance of external physical
forces and reduce its power consumption to use less power than when the logical unit is in the idle_b
power condition (e.g., cause a device that has rotating medium to rotate the medium at a lower
revolutions per minute).
e If the specified timer is supported and enabled, then the device server shall:
1)
force the specified timer to expire, which may cause the logical unit to transition to the specified
power condition;
2)
initialize and start all of the idle condition timers that are enabled (see SPC-6); and
3)
initialize and start all of the standby condition timers that are enabled (see SPC-6),
otherwise the device server shall terminate the START STOP UNIT command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN CDB.


If the START STOP UNIT command specifies a power condition that conflicts with an operation in progress
then, after the START STOP UNIT command completes with GOOD status, the logical unit may not be in the
power condition that was requested by the command.
It is not an error to specify that the logical unit transition to its current power condition.
If no START STOP UNIT command is being processed by the device server, then the device server shall
process any received START STOP UNIT command.
If a START STOP UNIT command is being processed by the device server and a subsequent START STOP
UNIT command for which the CDB is validated requests that the logical unit change to the same power
condition that was specified by the START STOP UNIT command being processed, then the device server
shall process the subsequent command.
If the NO_FLUSH bit is set to zero, then the device server shall write all logical block data in cache that is newer
than logical block data on the medium to the medium (e.g., as if in response to a SYNCHRONIZE CACHE
command (see 5.33 and 5.34) with  the LOGICAL BLOCK ADDRESS field set to zero and the NUMBER OF LOGICAL
Ah
FORCE_
IDLE_0
0h
Force the idle_a condition timer to be initialized to zero. e
1h
Force the idle_b condition timer to be initialized to zero. e
2h
Force the idle_c condition timer to be initialized to zero. e
Bh
FORCE_
STANDBY_0
0h
Force the standby_z condition timer to be initialized to zero. e
1h
Force the standby_y condition timer to be initialized to zero. e
All other combinations
Reserved
Table 114 — POWER CONDITION and POWER CONDITION MODIFIER field (part 2 of 2)
 POWER
CONDITION
value
POWER
CONDITION
name
POWER
CONDITION
MODIFIER
value
Device server action
a Process the following actions:
1)
the device server shall comply with any SCSI transport protocol specific power condition transition
restrictions (e.g., the NOTIFY (ENABLE SPINUP) requirement (see SPL-5));
2)
the logical unit shall transition to the specified power condition; and
3)
the device server shall disable all of the idle condition timers that are enabled (see SPC-6) and
disable all of the standby condition timers that are enabled (see SPC-6) until another START STOP
UNIT command is processed that returns control of the power condition to the logical unit or a logical
unit reset occurs.
b If a timer for a background scan operation expires, or a device specific event occurs, then the logical unit
shall not leave this power condition to perform the background function associated with the timer or
event.
c The device server shall cause the direct access block device to increase its tolerance of external physical
forces (e.g., causes a device that has movable read/write heads to move those heads to a safe position).
d The device server shall cause the direct access block device to increase its tolerance of external physical
forces and reduce its power consumption to use less power than when the logical unit is in the idle_b
power condition (e.g., cause a device that has rotating medium to rotate the medium at a lower
revolutions per minute).
e If the specified timer is supported and enabled, then the device server shall:
1)
force the specified timer to expire, which may cause the logical unit to transition to the specified
power condition;
2)
initialize and start all of the idle condition timers that are enabled (see SPC-6); and
3)
initialize and start all of the standby condition timers that are enabled (see SPC-6),
otherwise the device server shall terminate the START STOP UNIT command with CHECK CONDITION
status with the sense key set to ILLEGAL REQUEST and the additional sense code set to INVALID
FIELD IN CDB.
