#include <stdio.h>

int * getnumber( ) {

   static int r[10];

   int i;


   //random initialization later 
   for ( i = 0; i < 10; ++i) {
      r[i] = rand();
   }

   return r;
}

/* main function to call above defined function */
void main (void) {

   /* a pointer to an int */
   int *p;
   int i;

   p = getnumber();

   for ( i = 0; i < 10; i++ ) {
      printf( "p[%d] : %d\n", i, p[i]);
   }
}
