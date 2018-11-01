#include <stdio.h>
#include <math.h>

#define SIZE 3

float mean(float* data) {
	float sum = 0.0;
	for (int i = 0; i < SIZE; ++i) {
		sum += data[i];
	}
	return (sum / SIZE);
}

float std(float* data) {
	float std = 0.0;
	float m = mean(data);
	for (int i = 0; i < SIZE; ++i) {
		std += pow(data[i] - m, 2); 
	}
	std /= SIZE;
	std = sqrtf(std);
	return std;
}

void main(void) {
	float data[SIZE] = {2.0, 3.9, 4.0};

	printf("Mean: %f\n", mean(data));
	printf("STD: %f\n", std(data));
}
