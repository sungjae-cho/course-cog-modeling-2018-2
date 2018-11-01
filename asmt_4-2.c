/*
2018.9.27
c practice 2
*/

#include <stdio.h>

#define LAST 10

void main(void) {
    int i, total;

    total = 0;
    i = 0;

    while(i < LAST){
		// If i is odd, ...
		if (i % 2 == 1) {
        	total=total+i;
		}
        i=i+1;
    }

    printf("Total is %d.\n", total);
}

