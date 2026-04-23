# 7.8.18 Unit Serial Number VPD page

7.8.18 Unit Serial Number VPD page
The Unit Serial Number VPD page (see table 661) provides a product serial number for the SCSI target device
or logical unit.
The PERIPHERAL QUALIFIER field, PERIPHERAL DEVICE TYPE field, and PAGE LENGTH field are defined in 7.8.2.
The PAGE CODE field is defined in 7.8.2 and shall be set as shown in table 661 for the Unit Serial Number VPD
page.
The PRODUCT SERIAL NUMBER field contains right-aligned ASCII data (see 4.3.1) that is vendor-assigned serial
number. If the product serial number is not available, the device server shall return ASCII spaces (20h) in this
field.
Table 661 — Unit Serial Number VPD page
Bit
Byte
PERIPHERAL QUALIFIER
PERIPHERAL DEVICE TYPE
PAGE CODE (80h)
(MSB)
PAGE LENGTH (n-3)
(LSB)
(MSB)
PRODUCT SERIAL NUMBER
•••
n
(LSB)


8 Well known logical units
8.1 Model for well known logical units
Well known logical units are addressed using the well known logical unit addressing method of extended
logical unit addressing (see SAM-5). Each well known logical unit has a well known logical unit number
(W-LUN) as shown in table 662.
If a well known logical unit is supported within a SCSI target device, then that logical unit shall support all the
commands defined for it.
Access to well known logical units shall not be affected by access controls.
The SCSI device name of the well known logical unit may be determined by issuing an INQUIRY command
(see 6.6) requesting the Device Identification VPD page (see 7.8.6).
All well known logical units shall support the INQUIRY command’s Device Identification VPD page as defined
in 7.8.6.2.2.
8.2 REPORT LUNS well known logical unit
The REPORT LUNS well known logical unit shall only process the commands listed in table 663. If a
command is received by the REPORT LUNS well known logical unit that is not listed in table 663, then the
command shall be terminated with CHECK CONDITION status, with the sense key set to ILLEGAL
REQUEST, and the additional sense code set to INVALID COMMAND OPERATION CODE.
Table 662 — Well known logical unit numbers
W-LUN
Description
Reference
00h
Reserved
01h
REPORT LUNS well known logical unit
8.2
02h
ACCESS CONTROLS well known logical unit
8.3
03h
TARGET LOG PAGES well known logical unit
8.4
04h
SECURITY PROTOCOL well known logical unit
8.5
05h
MANAGEMENT PROTOCOL well known logical unit
8.6
06h-FFh
Reserved
Table 663 — Commands for the REPORT LUNS well known logical unit
Command
Operation
code
Type
Reference
INQUIRY
12h
M
6.6
REPORT LUNS
A0h
M
6.33
REQUEST SENSE
03h
M
6.39
TEST UNIT READY
00h
M
6.47
Key: M = Command implementation is mandatory.
