# 7.5.16 Protocol Specific Port mode page

7.5.16 Protocol Specific Port mode page
The Protocol Specific Port mode page provides protocol specific controls that are associated with a SCSI port.
The page_0 format (see table 475) is used if a MODE SENSE command (see 6.13.1) contains zero in the
SUBPAGE CODE field, and sub_page format (see table 476) is used for subpages 01h through FEh. See the
SCSI transport protocol standard for definition of the protocol specific mode parameters.
The Protocol Specific Port mode page controls parameters that affect one or more target ports. The param-
eters that may be implemented are defined in the SCSI transport protocol standard for the target port. The
mode page policy (see 7.5.2) for this mode page shall be shared or per target port. If the SCSI target device
contains more than one target port, the mode page policy should be per target port.
The parameters for a target port affect its behavior regardless of which initiator port is forming an I_T nexus
with the target port. The MLUS bit (see 7.8.9) shall be set to one in the mode page policy descriptor for this
mode page.
The parameters may be accessed by MODE SENSE (see 6.13) and MODE SELECT (see 6.11) commands
directed to any logical unit accessible through the target port. If a parameter value is changed, the device
servers for all logical units accessible through the target port shall establish a unit attention condition for the
initiator port associated with every I_T nexus except the I_T nexus on which the MODE SELECT command
was received, with the additional sense code set to MODE PARAMETERS CHANGED.
The PS bit, SPF bit, PAGE CODE field, SUBPAGE CODE field, and PAGE LENGTH field are described in 7.5.7.
Table 475 — Page_0 format Protocol Specific Port mode page
Bit
Byte
PS
SPF (0b)
PAGE CODE (19h)
PAGE LENGTH (n-1)
Protocol specific mode parameters
PROTOCOL IDENTIFIER
Protocol specific mode parameters
•••
n
Table 476 — Sub_page format Protocol Specific Port mode page
Bit
Byte
PS
SPF (1b)
PAGE CODE (19h)
SUBPAGE CODE
(MSB)
PAGE LENGTH (n-3)
(LSB)
Reserved
Protocol specific mode parameters
PROTOCOL IDENTIFIER
Protocol specific mode parameters
•••
n


The SPF bit and PAGE CODE field shall be set as shown in table 475 or table 476 for the Protocol Specific Port
mode page.
The value in the PROTOCOL IDENTIFIER field (see 7.6.1) defines the SCSI transport protocol to which the mode
page applies. For a MODE SENSE command, the device server shall set the PROTOCOL IDENTIFIER field to one
of the values shown in table 477 (see 7.6.1) to indicate the SCSI transport protocol used by the target port
through which the MODE SENSE command is being processed. For a MODE SELECT command, the appli-
cation client shall set the PROTOCOL IDENTIFIER field to one of the values shown in table 477 indicating the
SCSI transport protocol to which the protocol specific mode parameters apply. If a device server receives a
mode page containing a transport protocol identifier value other than the one used by the target port on which
the MODE SELECT command was received, then command shall be terminated with CHECK CONDITION
status, with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN
PARAMETER LIST.
