#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define MAXCHAR 1000

double mean(double* data, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; ++i) {
        sum += data[i];
    }
    return (sum / size);
}

double std(double* data, int size) {
    double std = 0.0;
    double m = mean(data, size);
    for (int i = 0; i < size; ++i) {
        std += pow(data[i] - m, 2);
    }
    std /= size;
    std = sqrtf(std);
    return std;
}

int read_file(char *file_name, double *data) {
	FILE *ptr_file = fopen(file_name, "r");
	char tmp_str[MAXCHAR];
	int size = 0;

	while(fgets(tmp_str, MAXCHAR, ptr_file) != NULL) {
		data[size++] = (double)atoi(tmp_str);
	}
		
	fclose(ptr_file);

	return size;
}

void write_file(char *file_name, double mean_val, double std_val) {
	FILE *ptr_file = fopen(file_name, "w");
	fprintf(ptr_file, "mean: %f\n", mean_val);
	fprintf(ptr_file, "std: %f\n", std_val);
	fclose(ptr_file);
}


void main(void) {
	char *r_file_name = "data/data_asmt_6-3.txt";
	char *w_file_name = "asmt_6-3.txt";
	
	double data[MAXCHAR];
	int size = 0;
	double mean_val;
	double std_val;

	size = read_file(r_file_name, data);
	
	mean_val = mean(data, size);
	std_val = std(data, size);

	write_file(w_file_name, mean_val, std_val);
}
