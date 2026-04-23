# Revision History

v
Revision History
This revision history is not part of American National Standard INCITS 1799:200x.
R.1 Revision 0 (27 February 2014)
Revision 0 of SBC-4 is substantially equal to revision 36 of SBC-3. The only differences arise from changes
made in SBC-3 discovered during the ISO process and modification of the format of the definitions to use the
new ISO style of “Note to Entry” for definitions that are longer than a single sentence.
R.2 Revision 1 (14 March 2014)
Incorporated the following proposals:
a)
Fixed “LENGTH OF SENSE DATA” to “LENGTH OF THE SENSE DATA FIELD” in 5.22.2;
b)
14-003r1 - Add reporting of unrecoverable errors that aren't reassigned
c)
14-019r2 - Discussion of WCE intent
d)
14-061r0 - 'Not defined' is not defined sufficiently;
e)
14-018r3 - Update Block Device Characteristics VPD page for ZBC; and
f)
13-094r4 - Supported Block lengths and protection types VPD page.
R.3 Revision 2 (20 May 2014)
Incorporated the following proposals:
a)
Corrected editorial errors on incorporation 14-003r1;
b)
14-112r0 - Clarifying token timeout;
c)
14-103r1 - Obsolete EER, DCR bits in Read-Write Recovery mode page;
d)
14-075r1 - Designed Utilization VPD data; and
e)
14-043r4 - Atomic writes and reads.
R.4 Revision 3 (27 August 2014)
Incorporated the following proposals:
a)
Corrected errors on incorporation of 13-094r5;
b)
14-148r3 - Redefinition of Peripheral device type;
c)
14-143r0 - Enhancing SBC-4 to allow ZBC to share its VPD page definitions;
d)
14-163r1 - Make the WRITE SAME no Data-Out Buffer bit broadly useful; and
e)
14-178r1 - Disable PI checking on write if PI is all Fs.
R.5 Revision 4(4 December 2014)
Incorporated the following proposals:
a)
Corrected errors on incorporation of 14-178r1;
b)
14-210r1 Minimal Workload Utilization logging
c)
14-064r5 Granular Boundaries for ATOMIC commands
d)
14-128r4 Unmap methods and text clarifications
e)
14-262r1 Thin Provisioning and De-Dupe interactions
f)
14-238r0 Remove Unused MMC Restrictions
g)
14-188r3 Resolve error cases with supporting Application Tag mode page
h)
14-107r8 Command Deadlines
i)
14-281r1 Zone Control command
j)
14-233r3 READ CAPACITY (16)
k)
14-194r2 Update Block Device Characteristics VPD page for Self Managed Devices


vi
R.6 Revision 5 (22 January 2015)
Incorporated the following proposals:
a)
Corrected errors on incorporation of 14-107r8
b)
15-024r1 Clarify SANITIZE command error case when AUSE=1;
c)
14-264r3 Logical Block Markup descriptors;
d)
15-019r0 Adding NO_PI_CHK to Supported Block Lengths And Protection Types VPD;
e)
14-249r2 Obsolete TMC and ETC bits;
f)
bring all of clause 2 into conformance with the currently approved T10 Style Guide T10/14-006r7
R.7 Revision 6 (28 April 2015)
Incorporated the following proposals:
a)
15-062r2 Revise Logical Block Model to support block device extension technologies
b)
15-060r0 Change obsolete fields in FORMAT UNIT command to reserved
c)
14-065r3 Per IO Advice (hints)
d)
Various editorial corrections for previously incorporated proposals including fixing cross references
R.8 Revision 7(20 May 2015)
Incorporated the following proposals:
a)
15-007r5 Additional provisioning reporting
b)
15-147r0 Remove ignored keyword
c)
15-075r2 Obsolete READ LONG and WRITE LONG except for write uncorrectable
d)
15-141r0 Storage Intelligence
e)
15-072r3 Result of SANITIZE for ZBC devices
f)
modifications for officer changes in T10
g)
Various editorial corrections for previously incorporated proposals including fixing cross references
R.9 Revision 7a(22 May 2015)
Incorporated the following:
a)
Changed Background Operation Control mode page from 0Ah/05h to 0Ah/06h.
R.10 Revision 7b (26 May 2015)
Incorporated the following:
a)
Changed Background Operation log page from 15h/01h to 15h/02h.
R.11 Revision 7c (26 May 2015)
Incorporated the following:
a)
Changed SPC-5 to SPC-6 except:
A) CBCS references;
B) ACCESS CONTROL IN command;
C) ACCESS CONTROL OUT command.


vii
R.12 Revision 8 (1 September 2015)
Incorporate the following:
a)
14-265r3 Allow device discovery through sanitize;
b)
15-162r1 Clarify FUA bit wording;
c)
15-186r0 Stream Corrections;
d)
VPD page code for the Block Limits Extension VPD page overlapped the Supported Block Lengths
And Protection Types VPD page. The VPD page code for the Block Limits Extension VPD page was
changed to B7h
R.13 Revision 9 (9 November 2015)
Incorporate the following:
a)
15-193r1 Expunge I_T_L_Q nexus transaction;
b)
15-203r1 More Stream Correction;
c)
15-218r2 Definition of Stream Identifier zero;
d)
15-219r1 Reset of stream identifiers; and
e)
Modified occurrences of “field in ...” and “bit in ...”.
R.14 Revision 10 (21 January 2016)
Incorporate the following:
a)
15-264r1 Allow REPORT ZONES command during sanitize operation;
b)
15-117r6 Add fast format feature to FORMAT UNIT command;
c)
15-081r4 IO Access Hint Data Class;
d)
15-037r6 Detection handling and reporting of unaligned writes;
e)
16-044r0 Correction for commands allowed during sanitize;
f)
15-288r2 Sanitize fix for ZBC;
g)
15-293r0 Revise NDOB bit wording;
h)
15-163r4 Organization of 'things supported' tables; and
i)
16-005r1 UUID descriptor usage.
R.15 Revision 11 (2 June 2016)
Incorporate the following:
a)
15-087r9 Scattered writes;
b)
16-098r1 Cleanup of Transfer limits for commands table;
c)
16-086r1 WRITE SCATTERED (32);
d)
16-118r1 Supported Block Lengths and Protection Type enhancement;
e)
fixed the Supported Loge Pages and Supported Log Pages And Subpages rows in table Log page
codes and subpage codes for direct access block devices table;
f)
Removed FCP-3 from bibliography and fixed FCP-4 reference;
R.16 Revision 12 (11 October 2016)
Incorporate the following:
a)
16-197r0 FORMAT UNIT SI and FMTDATA interaction
b)
16-201r1 Clarification of data transfer for DTE set to one
c)
16-187r1 Reassign blocks zero fill
d)
16-168r0 WSNZ bit clarification, old school style
e)
15-040r4 Simplified SCSI - Basic Provisioning feature set
f)
16-029r4 SCSI Feature Sets base requirements


viii
g)
16-158r1 SBC-3: Response to ISO editor general comments on ISO/IEC 14776-323
h)
16-155r1 SBC-3 ISO - SBC-4: ISO changes
i)
16-159r1 isoiec14776-323 DIS comments and T10 responses
j)
16-171r3 Disabled logical block protection information
k)
15-211r4 Simplified SCSI - Drive Maintenance feature set
l)
16-198r3 Rebuild Assist for SSDs
R.17 Revision 12a (19 October 2016)
Incorporate the following:
a)
Editorial corrections on the incorporation of proposals in r12 of improper small caps and cross
references
R.18 Revision 13 (26 January 2017)
Incorporate the following:
a)
16-239r0 Clarification of Verify (32) app tag mask
b)
16-255r0 Cleanup of SSU_PC state machine figure 11
c)
16-203r2 New Access Patterns LBM Descriptor Bit for SBC
d)
16-273r1 Repurposing Depopulation
e)
17-023r1 Background Scan Log ambiguity
f)
17-024r1 Write and unmap failures clarification
R.19 Revision 14 (17 August 2017)
Incorporate the following:
a)
17-014r3 Repurposing Depopulation cleanup
b)
17-054r0 Various corrections
c)
17-057r2 Get LBA Status Fixes
d)
17-067r2 Repurposing Depopulation errata - STARTING ELEMENT
e)
17-075r1 Unraveling medium access commands
f)
17-077r1 Open stream when format corrupt
g)
17-074r1 Rebuild Assist for SSDs Enhancements
h)
17-076r1 Verify compare operation clarification
i)
17-078r2 Rebuild Assist for SSDs Annex
R.20 Revision 15 (9 November 2017)
Incorporate the following:
a)
17-131r2 Obsolete XOR
R.21 Revision 16 (9 January 2019)
Incorporate the following:
a)
Fixed error introduced in WRITE SAME (10) in SBC-3r35i;
b)
added GET PHYSICAL ELEMENT STATUS and REMOVE ELEMENT AND TRUNCATE to table A.2;
c)
16-264r4 ZBC-2 SPC-6 SBC-4 Add zoned parameters log page;
d)
18-031r0 Update the table of VPD pages for direct access devices; and
e)
18-074r2 Dual Actuator Informative Annex.


ix
R.22 Revision 17 (2 April 2019)
Incorporate the following:
a)
18-089r5 SPC-6, SBC-4, SAM-6: More Specific Command Duration Limits
b)
19-020r1 SBC-4 Allow READ CAPACITY (10) during depopulation
c)
19-022r1 SBC-4 Logical Block Provisioning cleanup
d)
19-027r1 Utilization Rate Based on Date and Time log parameter format issues
R.23 Revision 18 (10 January 2019)
Incorporated the following:
a)
19-029r7 FORMAT WITH PRESET command;
b)
19-087r1 Add new ZBC-2 commands;
c)
19-100r0 Eviscerate CbCS in RFC processing;
d)
19-101r0 Quickie ZBC to ZBC-2 changes;
e)
19-103r0 Funky ZBC to ZBC-2 Tweaks;
f)
19-121r0 RFC comment resolution (Grouping function);
g)
19-063r6 SBC4r17 RFC comment resolution.
R.24 Revision 19
Incorporated:
a)
removed change tracking from revision 18;
b)
19-088R2 Modernize the ZONED field;
c)
19-067r3 Create Restore Elements and Rebuild feature;
d)
20-002R1 Rebalance ZNR requirements with ZBC-2 (and SATA);
e)
20-004R1 Revise depopulation and restoration rule for interruptions; and
f)
20-026R0 Add command duration limits feature to 32 byte commands.
R.25 Revision 19a
a)
Updates 19-067r3 to 19-067r4
R.26 Revision 19b
a)
Editorial changes from Ralph Weber and Brad Besmer
R.27 Revision 20
a)
Removed all change tracking for public review
R.28 Revision 20a
a)
Fixed naming issue of RES_ALL which should have been RALWD
R.29 Revision 21
a)
Resolved letter ballot comments in T10/20-062
R.30 Revision 22
a)
Incorporated 20-091r0 (public review comment)


x
b)
Incorporated 20-092r1 (public review comment)
c)
Modified reference in glossary entry of storage element
d)
Fixed two field references that were not in small caps
