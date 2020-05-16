.data
.balign 4
tot:		.word 0
max:		.word 0
counter:	.word 0

.text
.arm
.global add_numbers_asm

add_numbers_asm:

  ldr r4, adr_counter
  ldr r5, adr_max
  ldr r6, adr_tot

  str r0, [r5] /* max */
  mov r1, #0  /* counter */
  mov r2, #0  /* tot */

loop:

  cmp r0, r1
  beq endloop
  add r2, r2, r1
  add r1, r1, #1
  bal loop

endloop:

  str r0, [r4]
  str r1, [r5]
  str r2, [r6]

  ldr r0, [r6]

  bx lr

adr_tot: .word tot
adr_max: .word max
adr_counter: .word counter

