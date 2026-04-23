# 7.7.2 SA creation capabilities

The HARDWARE VERSION field is null terminated, null padded data (see 4.3.2) that indicates the version number
of the hardware in the module, as reported by NIST.
The VERSION field is null terminated, null padded data (see 4.3.2) that indicates the version number of the
firmware or software in the module, as reported by NIST. The value in the VERSION field is not related to the
PRODUCT REVISION LEVEL field of standard INQUIRY data (see 6.6.2).
The MODULE NAME field is null terminated, null padded data (see 4.3.2) that indicates the name or identifier of
the cryptographic module, as reported by NIST.
7.7.2 SA creation capabilities
7.7.2.1 Overview
If the SECURITY PROTOCOL field in a SECURITY PROTOCOL IN command (see 6.40) is set to 40h, then the
command returns information related to the SA creation (see 5.14.2.3) capabilities provided by the device
server.
The SA creation capabilities protocol is independent of any other SA creation protocols. The device server
shall not refuse to process an SA creation capabilities SECURITY PROTOCOL IN command, and this
processing shall not affect the state maintained for any SA creation CCS (e.g., an IKEv2-SCSI CCS) on any
I_T_L nexus. Except for those cases where an SA creation capabilities SECURITY PROTOCOL IN command
reports changed SA creation capabilities, processing of the command shall not affect the concurrent
processing of any commands that are part of an SA creation CCS.
If any SA creation protocols are supported, the SA creation capabilities protocol shall be supported as
described in 7.7.2.
The SA creation capabilities SECURITY PROTOCOL IN CDB format is described in 7.7.2.2.
As shown in table 517 (see 7.7.2.2), the format of the parameter data returned by a SA creation capabilities
SECURITY PROTOCOL IN command depends on the value in the SECURITY PROTOCOL SPECIFIC field in the
CDB.
7.7.2.2 SA creation capabilities CDB description
The SA creation capabilities SECURITY PROTOCOL IN CDB has the format defined in 6.40 with the
additional requirements described in this subclause.


If the SECURITY PROTOCOL field is set to SA creation capabilities (i.e., 40h) in a SECURITY PROTOCOL IN
command, the SECURITY PROTOCOL SPECIFIC field (see table 517) identifies the SA creation protocol (see
5.14.2.3) for which the device server shall return capability information.
If an SA creation capabilities SECURITY PROTOCOL IN command is received with the INC_512 bit is set to
one, then the SECURITY PROTOCOL IN command shall be terminated with CHECK CONDITION status,
with the sense key set to ILLEGAL REQUEST, and the additional sense code set to INVALID FIELD IN CDB.
7.7.2.3 SA creation capabilities parameter data formats
7.7.2.3.1 Supported device server capabilities formats parameter data format
The supported device server capabilities formats parameter data (see table 518) indicates which device
server capabilities parameter data formats are supported by the device server.
The PARAMETER DATA LENGTH field indicates the number of bytes that follow in the parameter data.
Each CAPABILITIES PARAMETER DATA FORMAT field in the supported capabilities parameter data formats list shall
contain one of the SECURITY PROTOCOL SPECIFIC field values (see table 517) supported by the device server.
The values shall be listed in ascending order starting with 0000h.
Table 517 — SECURITY PROTOCOL SPECIFIC field for the SA creation capabilities
Code
Description
Parameter
data format
0000h
Supported device server capabilities formats
7.7.2.3.1
0001h to 0100h
Reserved
0101h
IKEv2-SCSI device server capabilities
7.7.2.3.2
0102h to EFFFh
Reserved
F000h to FFFFh
Vendor Specific
Table 518 — Supported device server capabilities formats parameter data
Bit
Byte
(MSB)
PARAMETER DATA LENGTH (n-3)

•••
(LSB)
Supported capabilities parameter data formats
CAPABILITIES PARAMETER DATA FORMAT [first]
(0000h)
•••
n-1
CAPABILITIES PARAMETER DATA FORMAT [last]

n
