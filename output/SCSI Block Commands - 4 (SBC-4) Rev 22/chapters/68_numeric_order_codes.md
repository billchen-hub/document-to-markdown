# Numeric order codes

Annex A
(informative)
Numeric order codes
A.1 Variable length CDBs
 Commands that use operation code 7Fh in table 34 use the variable length command format defined in
SPC-6 and are differentiated by service action codes as described in table A.1.
Table A.1 — Variable length command service action code assignments
Operation code/service
action code
Description
7Fh/0000h
Reserved
7Fh/0001h
Reserved
7Fh/0002h
Reserved
7Fh/0003h
Obsolete (XDREAD (32))
7Fh/0004h
Obsolete (XDWRITE (32))
7Fh/0005h
Reserved
7Fh/0006h
Obsolete (XPWRITE (32))
7Fh/0007h
Obsolete (XDWRITEREAD (32))
7Fh/0008h
Reserved
7Fh/0009h
READ (32)
7Fh/000Ah
VERIFY (32)
7Fh/000Bh
WRITE (32)
7Fh/000Ch
WRITE AND VERIFY (32)
7Fh/000Dh
WRITE SAME (32)
7Fh/000Eh
ORWRITE (32)
7Fh/000Fh
WRITE ATOMIC (32)
7Fh/0010h
WRITE STREAM (32)
7Fh/0011h
WRITE SCATTERED (32)
7F/0012h
GET LBA STATUS (32)
7Fh/0013h to 07FFh
Reserved
7Fh/0800h to FFFFh
See SPC-6


A.2 SERVICE ACTION IN commands and SERVICE ACTION OUT commands
Commands that use operation code 9Eh (i.e., SERVICE ACTION IN (16)) (see SPC-6) in table 34 are
differentiated by service action codes as described in table A.2.
Commands that use operation code 9Fh (i.e., SERVICE ACTION OUT (16)) (see SPC-6) in table 34 are
differentiated by service action codes as described in table A.3.
Table A.2 — SERVICE ACTION IN (16) service actions
Operation code/service
action code
Description
9Eh/00h to 0Fh
Reserved for commands applicable to all device types (see SPC-6)
9Eh/10h
READ CAPACITY (16)
9Eh/11h
Obsolete READ LONG (16)
9Eh/12h
GET LBA STATUS (16)
9Eh/13h
REPORT REFERRALS
9Eh/14h
STREAM CONTROL
9Eh/15h
BACKGROUND CONTROL
9Eh/16h
GET STREAM STATUS
9Eh/17h
GET PHYSICAL ELEMENT STATUS
9Eh/18h
REMOVE ELEMENT AND TRUNCATE
9Eh/19h
RESTORE ELEMENTS AND REBUILD
9Eh/1Ah to 1Fh
Reserved
Table A.3 — SERVICE ACTION OUT (16) service actions
Operation code/service
action code
Description
9Fh/00h to 0Fh
Reserved for commands applicable to all device types (see SPC-6)
9Fh/10h
Reserved
9Fh/11h
WRITE LONG (16)
9Fh/12h
WRITE SCATTERED (16)
9Fh/13h to 1Fh
Reserved


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
