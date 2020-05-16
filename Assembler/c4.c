#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int add_numbers_asm(int max, int aantal);

int x = 6666;
int aantal = 100000;

clock_t start, end;
double cpu_time_used;

int add_numbers(int max)
{
   int tot = 0;
   int counter = 0;
   while (counter < max)
   {
      tot = tot + counter;
      counter++;
   }

   return tot;
}

int add_numbers_c(int max, int aantal)
{
  int tot = 0;
  for (int i = 0; i < aantal; i++)
  {
    tot = tot + add_numbers(x);
  }

  return tot;
}

int main(int argc, char *argv[])
{
  int tot;
  
  printf("C\n");
  start = clock();
  tot = add_numbers_c(x, aantal);
  end = clock();
  cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
  printf("Time taken in C: %f seconds\n", cpu_time_used);
  printf("Result: %d\n", tot);

  //////////////////////////////////////////

  printf("ASM\n");
  start = clock();
  tot = add_numbers_asm(x, aantal);
  end = clock();
  cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
  printf("Time taken in ASM: %f seconds\n", cpu_time_used);
  printf("Result: %d\n", tot);
  return 0;
}
