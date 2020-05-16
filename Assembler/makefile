clean:
	rm *.o

sum3:
	as -o sum3.o sum3.s
	gcc -o sum3 sum3.o

hello:
	as -o hello.o hello.s
	gcc -o hello hello.o

asm1:
	as -o asm1.o asm1.s
	gcc -o c1 c1.c asm1.o -Wall

asm2:
	as -o asm2.o asm2.s
	gcc -o c2 c2.c asm2.o -Wall

asm3:
	as -o asm3.o asm3.s
	gcc -o c3 c3.c asm3.o -Wall

asm4:
	as -o asm4.o asm4.s
	gcc -o c4 c4.c asm4.o -Wall

