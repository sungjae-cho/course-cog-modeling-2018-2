#include <stdio.h>

int main()
{
	int x = 4;
	int y = 5;
	int z = 10;

	float sum = x + y + z;
	float mean = ((float)(x + y + z))/3.0;

	printf("sum = %f\n", sum);
	printf("mean = %f\n", mean);

	return 0;
}
