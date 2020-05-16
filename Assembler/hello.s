.global main
main:
    mov   r0,#1
    adr   r1,message
    mov   r2,#12
    mov   r7,#4
    svc   0      // write
    mov   r7,#1
    svc   0      // exit
message:
    .ascii  "Hello world\n"

