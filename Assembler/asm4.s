.data
.balign 4
tot:		.word 0
max:		.word 0
counter:	.word 0
aantal:		.word 0
returnadr1:	.word 0
returnadr2:     .word 0

.text
.arm
.global add_numbers_asm

add_numbers_asm:

  ldr r2, adr_returnadr1
  str lr, [r2]

  ldr r5, adr_max
  ldr r6, adr_aantal

  str r0, [r5]
  str r1, [r6]

  ldr r9, [r6]
  mov r8, #0

loop0:

  cmp r8, r9
  beq done

  add r8, #1
  ldr r0, [r5]
  bl add_numbers
//  bl dummy
//  bl dummy2

  bal loop0

done:

  ldr r6, adr_tot
  ldr r0, [r6]

  ldr lr, adr_returnadr1
  ldr lr, [lr]
  bx lr

/************************************/

dummy2:
  ldr r2, adr_returnadr2
  str lr, [r2]

  /* do stuff */

  ldr lr, adr_returnadr2
  ldr lr, [lr]
  bx lr

dummy:

  push {r11}
  add r11, sp, #0
  sub sp, sp, #16

  add sp, r11, #0
  pop {r11}
  bx lr

add_numbers:

  push {r11}		/* prologue */
  add r11, sp, #0
  sub sp, sp, #16

  ldr r4, adr_counter
  ldr r6, adr_tot

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
  ldr r3, [r6]
  add r2, r2, r3
  str r2, [r6]

  add sp, r11, #0	/* epilogue */
  pop {r11}
  bx lr

adr_tot:       .word tot
adr_max:        .word max
adr_counter:    .word counter
adr_aantal:     .word aantal
adr_returnadr1: .word returnadr1
adr_returnadr2: .word returnadr2
