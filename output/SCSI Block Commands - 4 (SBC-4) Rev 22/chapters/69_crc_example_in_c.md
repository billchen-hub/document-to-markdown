# CRC example in C

Annex B
(informative)
CRC example in C
The following is an example C program that generates the value for the LOGICAL BLOCK GUARD field in
protection information (see 4.21).
// picrc.cpp : SCSI SBC-4 Protection Information CRC generator
#include “stdafx.h”
#include <stdio.h>
#include <malloc.h>
/* return crc value */
unsigned short calculate_crc(unsigned char *frame, unsigned long length) {
unsigned short const poly = 0x8BB7L;  /* Polynomial */
unsigned const int poly_length = 16;
unsigned short crc_gen;
unsigned short x;
unsigned int i, j, fb;
unsigned const int invert = 0;/* 1=seed with 1s and invert the CRC */

crc_gen = 0x0000;
crc_gen ^= invert? 0xFFFF: 0x0000;   /* seed generator */
for (i = 0; i < length; i += 2) {
/* assume little endian */
x = (frame[i] << 8) | frame[i+1];
/* serial shift register implementation */
        for (j = 0; j < poly_length; j++) {
fb = ((x & 0x8000L) == 0x8000L) ^ ((crc_gen & 0x8000L) ==
0x8000L);
x <<= 1;
crc_gen <<= 1;
if (fb)
crc_gen ^= poly;
}
}

return crc_gen ^ (invert? 0xFFFF: 0x0000); /* invert output */
} /* calculate_crc */
/* function prototype */
unsigned short calculate_crc(unsigned char *, unsigned long);
void main (void) {
unsigned char *buffer;
unsigned long buffer_size = 32;
unsigned short crc;
unsigned int i;

/* 32 0x00 */
buffer = (unsigned char *) malloc (buffer_size);
for (i = 0; i < buffer_size; i++) {
buffer[i] = 0x00;


}
crc = calculate_crc(buffer, buffer_size);
printf (“Example CRC all-zeros is %04x\n”, crc);
free (buffer);
/* 32 0xFF */
buffer = (unsigned char *) malloc (buffer_size);
for (i = 0; i < buffer_size; i++) {
buffer[i] = 0xFF;
}
crc = calculate_crc(buffer, buffer_size);
printf (“Example CRC all-ones is %04x\n”, crc);
free (buffer);
/* 0x00 incrementing to 0x1F */
buffer = (unsigned char *) malloc (buffer_size);
for (i = 0; i < buffer_size; i++) {
buffer[i] = i;
}
crc = calculate_crc(buffer, buffer_size);
printf (“Example CRC incrementing is %04x\n”, crc);
free (buffer);
/* 0xFF 0xFF then 30 zeros */
buffer = (unsigned char *) malloc (buffer_size);
buffer[0] = 0xff;
buffer[1] = 0xff;
for (i = 2; i < buffer_size; i++) {
buffer[i] = 0x00;
}
crc = calculate_crc(buffer, buffer_size);
printf (“Example CRC FF FF then 30 zeros is %04x\n”, crc);
free (buffer);
/* 0xFF decrementing to 0xE0 */
buffer = (unsigned char *) malloc (buffer_size);
for (i = 0; i < buffer_size; i++) {
buffer[i] = 0xff - i;
}
crc = calculate_crc(buffer, buffer_size);
printf (“Example CRC FF decrementing to E0 is %04x\n”, crc);
free (buffer);
} /* main */


Annex C
(informative)
Sense information for locked or encrypted logical units
A device server may complete some commands with CHECK CONDITION status under certain conditions
while the logical unit is locked or encrypted. Table C.1 describes the conditions relative to the sense key and
the additional sense code returned by the device server with the CHECK CONDITION status.
Table C.1 — Sense information for locked or encrypted logical units
Sense key
Additional sense code
Description
DATA
PROTECT
ACCESS DENIED –
NO ACCESS RIGHTS
The logical unit is locked. This condition may occur for read
commands or write commands. This condition may occur for
the entire logical unit or for a range of LBAs contained in the
logical unit. To clear this condition, an application client
performs a security protocol specific procedure to unlock
access to the logical unit.
ABORTED
COMMAND
LOGICAL BLOCK
REFERENCE TAG
CHECK FAILED
These conditions may occur for a read command. The
additional sense codes may indicate that an encrypting logical
unit has changed the encryption/decryption key, and the LBAs
requested by the command have not yet been rewritten.
Disabling protection information checking in a CDB may allow
the command to complete successfully, but the data returned
for the command may be invalid (i.e., not decrypted). To clear
this condition, an application client writes the LBAs for which
the condition occurred with new data.
ABORTED
COMMAND
LOGICAL BLOCK
APPLICATION TAG
CHECK FAILED
ABORTED
COMMAND
LOGICAL BLOCK
GUARD CHECK
FAILED


Annex D
(informative)
Optimizing block access characteristics
D.1 Overview
This annex describes example methods that application clients may use to achieve optimal performance for
logical block access. These examples use the following information:
a)
the LOWEST ALIGNED LOGICAL BLOCK ADDRESS field (see 5.21.2);
b)
the LOGICAL BLOCKS PER PHYSICAL BLOCK EXPONENT field (see 5.21.2);
c)
the OPTIMAL TRANSFER LENGTH GRANULARITY field(see 6.6.4);
d)
the OPTIMAL TRANSFER LENGTH field (see 6.6.4);
e)
the MAXIMUM TRANSFER LENGTH field (see 6.6.4);
f)
the OPTIMAL STREAM WRITE SIZE field (see 6.6.5); and
g)
the STREAM GRANULARITY SIZE field (see 6.6.5).
D.2 Starting logical block offset
The READ CAPACITY (16) command transfers parameter data which includes a value in the LOWEST ALIGNED
LOGICAL BLOCK ADDRESS field. As shown in figure 4, the value in this field indicates the starting alignment of
logical block addresses where optimal performance for logical block access begins.
D.3 Optimal granularity sizes
The READ CAPACITY (16) command transfers parameter data that includes a value in the LOGICAL BLOCKS
PER PHYSICAL BLOCK EXPONENT field. As shown in figure 2 and in figure 4, the value in this field enables the
application client to determine the number of logical blocks per physical block.
The Block Limits VPD page may include values in the OPTIMAL TRANSFER LENGTH GRANULARITY field, the
OPTIMAL TRANSFER LENGTH field, and the MAXIMUM TRANSFER LENGTH field. These values may be used to
determine optimum transfer sizes.
If the OPTIMAL TRANSFER LENGTH GRANULARITY field is valid (i.e., contains a value greater than zero), then the
value in the OPTIMAL TRANSFER LENGTH GRANULARITY field is the optimal granularity size. If:
a)
the Block Limits VPD page is not supported; or
b)
the Block Limits VPD page is supported and the OPTIMAL TRANSFER LENGTH GRANULARITY field is set to
zero,
then the value 2(logical blocks per physical block exponent) is the optimal granularity size.
D.4 Optimal stream granularity sizes
The Block Limits Extension VPD page may include values in the OPTIMAL STREAM WRITE SIZE field and the
STREAM GRANULARITY SIZE field. These values may be used to determine optimum transfer sizes and optimum
transfer alignment to use with the WRITE STREAM commands (see 5.57 and 5.58).
If the OPTIMAL STREAM WRITE SIZE field is valid (i.e., contains a value greater than zero), then the value in the
OPTIMAL STREAM WRITE SIZE field indicates the optimum transfer size and the optimum transfer alignment.
