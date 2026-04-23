# 5.32 STREAM CONTROL command

BLOCKS field set to zero) prior to entering into any power condition that prevents accessing the medium (e.g.,
before the rotating medium spindle motor is stopped during transition to the stopped power condition). If the
NO_FLUSH bit is set to one, then the device server should not write any cached logical blocks to the medium
prior to entering into any power condition that prevents accessing the medium.
If the load eject (LOEJ) bit is set to zero and the POWER CONDITION field is set to zero, then the logical unit shall
take no action regarding loading or ejecting the medium. If the LOEJ bit is set to one and the POWER CONDITION
field is set to zero, then the logical unit shall unload the medium if the START bit is set to zero. If the LOEJ bit is
set to one, the POWER CONDITION field is set to zero, and the START bit is set to one, then the logical unit shall
load the medium.
If the START bit is set to zero and the POWER CONDITION field is set to zero, then the device server shall:
a)
cause the logical unit to transition to the stopped power condition;
b)
stop any idle condition timer that is enabled (see SPC-6); and
c)
stop any standby condition timer that is enabled (see SPC-6).
If the START bit set to one and the POWER CONDITION field is set to zero, then the device server shall:
1)
comply with requirements defined in SCSI transport protocol standards (e.g., the NOTIFY (ENABLE
SPINUP) requirement (see SPL-5));
2)
cause the logical unit to transition to the active power condition;
3)
initialize and start any idle condition timer that is enabled; and
4)
initialize and start any standby condition timer that is enabled.
The CONTROL byte is defined in SAM-6.
5.32 STREAM CONTROL command
5.32.1 STREAM CONTROL command overview
The STREAM CONTROL command (see table 115) requests the device server to open a stream and return
the stream identifier in the return parameter data or close the stream specified in the STR_ID field in the CDB.
This command uses the SERVICE ACTION IN (16) CDB format (see clause A.2).


The OPERATION CODE field and SERVICE ACTION field are defined in SPC-6 and shall be set to the values shown
in table 115 for the STREAM CONTROL command.
The stream control (STR_CTL) field specifies the operation to be performed as described in table 116.
If the STR_CTL field is set to 10b, then the stream identifier (STR_ID) field specifies the stream identifier
associated with the requested operation. If the STR_CTL field is not set to 10b, then the device server shall
ignore the STR_ID field.
The ALLOCATION LENGTH field is defined in SPC-6.
The CONTROL byte is defined in SAM-6.
Table 115 — STREAM CONTROL command
Bit
Byte
OPERATION CODE (9Eh)
Reserved
STR_CTL
SERVICE ACTION (14h)
Reserved
(MSB)
STR_ID
(LSB)
Reserved
•••
(MSB)
ALLOCATION LENGTH
•••
(LSB)
Reserved
CONTROL
Table 116 — STR_CTL field
Code
Description
01b
Open a stream and return the stream identifier in the
ASSIGNED_STR_ID field in the returned parameter data.
10b
Close the stream associated with the STR_ID field.
all others
Reserved
