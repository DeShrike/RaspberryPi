.data
.balign 4
a:	.word 22
b:	.word 42
c:	.word 0

.text
.arm
.global add_numbers_asm

add_numbers_asm:
  add r0, r0, r1

  ldr r6, adr_c
  ldr r5, adr_b
  ldr r4, adr_a

  ldr r1, [r4]
  ldr r2, [r5]
  ldr r3, [r6]

  str r0, [r6]
  add r0, r0, r1
  add r0, r0, r2

  bx lr

adr_a: .word a
adr_b: .word b
adr_c: .word c

