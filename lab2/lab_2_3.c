/* Title: lab_2_3.c
 * Abstract: This program left/right shifts an array based on user input.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 20 minutes
 * Date: 08/30/2022
 */

#include <stdio.h>
#include <stdlib.h>

void fprintia(FILE *, int *, unsigned int);
void right_shift(int *, unsigned int);
void left_shift(int *, unsigned int);

int main() {
	FILE *ifp;

	// Open file
	ifp = fopen("input.txt", "r");
	if (ifp == NULL) {
		fprintf(stderr, "File does not exist.");
		return 1;
	}

	int chunk_size = 100;
	int *array = (int *)malloc(chunk_size * sizeof(int));
	unsigned int a_size = 0;
	
	// Read integers
	fprintf(stdout, "Array values: ");
	while (fscanf(ifp, "%d", array + a_size) == 1) {
		fprintf(stdout, "%d ", *(array + a_size));
		++a_size;

		if (a_size == chunk_size) {
			chunk_size += 100;
			array = (int *)realloc(array, chunk_size * sizeof(int));
		}
	}
	fprintf(stdout, "\n");

	fprintf(stdout, "This is the list of options:\n\t1. Right shift\n\t2. Left shift\n");
	
	int option;
	char cont = 'Y';
	while (cont == 'Y') {
		fprintf(stdout, "\nEnter your option: ");
		fscanf(stdin, "%d", &option);

		switch (option) {
		case 1:
			right_shift(array, a_size);
			break;
		case 2:
			left_shift(array, a_size);
			break;
		default:
			continue;
		}

		fprintf(stdout, "New array values: ");
		fprintia(stdout, array, a_size);

		fprintf(stdout, "Continue? (Y/N): ");
		fgetc(stdin);
		fscanf(stdin, "%c", &cont);
	}

	fclose(ifp);
	free(array);

	return 0;
}

void fprintia(FILE *fp, int *ia, unsigned int size) {
	int i;
	for (i = 0; i < size; ++i) {
		fprintf(fp, "%d ", ia[i]);
	}
	fprintf(fp, "\n");
}

void right_shift(int *array, unsigned int size) {
	if (size == 0) return;

	int i;
	for (i = size - 1; i > 0; --i) {
		array[i] = array[i - 1];
	}
	array[0] = 0;
}

void left_shift(int *array, unsigned int size) {
	if (size == 0) return;

	int i;
	for (i = 0; i < size - 1; ++i) {
		array[i] = array[i + 1];
	}
	array[size - 1] = 0;
}
