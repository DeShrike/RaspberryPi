#include <stdio.h>
#include <stdlib.h>

int add_numbers_asm(int a, int b);

int main(int argc, char *argv[])
{
  printf("%d\n", add_numbers_asm(7,8));

  return 0;
}

