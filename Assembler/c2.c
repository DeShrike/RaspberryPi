#include <stdio.h>
#include <stdlib.h>

int add_numbers_asm(int a, int b);

int x = 34;
int y = 99;

int main(int argc, char *argv[])
{
  printf("Answer should be %d\n", 22 + 42 + x + y);
  printf("Answer: %d\n", add_numbers_asm(x, y));

  return 0;
}

