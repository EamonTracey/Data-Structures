/* Title: lab_2_2.c
 * Abstract: This program right shifts an array.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 20 minutes
 * Date: 08/30/2022
 */

#include <stdio.h>
#include <stdlib.h>

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

	// Perform right shift
	int i;
	for (i = a_size - 1; i >= 1; --i) {
		array[i] = array[i - 1];
	}
	array[0] = 0;

	// Print values
	fprintf(stdout, "Array values after the right shift: ");
	for (i = 0; i < a_size; ++i) {
		fprintf(stdout, "%d ", array[i]);
	}
	fprintf(stdout, "\n");


	fclose(ifp);
	free(array);

	return 0;
}
