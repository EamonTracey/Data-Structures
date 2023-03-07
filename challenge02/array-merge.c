/* Title: array-merge.c
 * Abstract: This program reads 2 arrays from an input file and merges them.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 20 minutes 
 * Date: 09/06/2022 
 */

#include <stdio.h>
#include <stdlib.h>

void disp_arr(int *, int);
int *merge(int *, int, int *, int, int *);

int main() {
	// Prompt the user for a filename.
	char filename[100];

	fprintf(stdout, "Enter filename: ");
	fscanf(stdin, "%s", filename);

	// Open file.
	FILE *fp = fopen(filename, "r");
	if (fp == NULL) {
		fprintf(stderr, "Fail. The file %s does not exist.\n", filename);
		return 1;
        }

	// Read and allocate arrays.
	// Use fscanf to read the first value, denoting the size.
	// Then, iterate using fscanf to copy the array values into memory.
	int sz1, sz2;
	int *arr1, *arr2;
	int i;

	fscanf(fp, "%d", &sz1);
	arr1 = (int *)malloc(sz1 * sizeof(int));
	for (i = 0; i < sz1; ++i) {
		fscanf(fp, "%d", arr1 + i);
	}

	fscanf(fp, "%d", &sz2);
	arr2 = (int *)malloc(sz2 * sizeof(int));
	for (i = 0; i < sz2; ++i) {
		fscanf(fp, "%d", arr2 + i);
	}

	fclose(fp);

	fprintf(stdout, "Array 1: ");
	disp_arr(arr1, sz1);
	fprintf(stdout, "\nArray 1 size: %d\n", sz1);
	fprintf(stdout, "Array 2: ");
	disp_arr(arr2, sz2);
	fprintf(stdout, "\nArray 2 size: %d\n", sz2);

	// Merge arrays.
	int szm;
	int *arrm = merge(arr1, sz1, arr2, sz2, &szm);

	fprintf(stdout, "Combined array: ");
	disp_arr(arrm, szm);
	fprintf(stdout, "\nCombined array size: %d\n", szm);

	// Free memory.
	free(arr1);
	free(arr2);
	free(arrm);

	return 0;

}

// This function prints the values of an array to stdout, space-separated.
void disp_arr(int *arr, int sz) {
	int i;
	for (i = 0; i < sz; ++i) {
		fprintf(stdout, "%d ", arr[i]);
	}
}

// This function merges 2 arrays, returning a pointer to the new array.
int *merge(int *arr1, int sz1, int *arr2, int sz2, int *szm) {
	// Assign size of the merged array.
	// The size is equal to the sum of the two arrays.
	*szm = sz1 + sz2;

	// Dynamically allocate memory for the merged arrays.
	int *arrm = (int *)malloc(*szm * sizeof(int));

	// Iterate through the two arrays, copying values.
	int i;
	for (i = 0; i < sz1; ++i) {
		arrm[i] = arr1[i];
	}
	for (i = sz1; i < *szm; ++i) {
		arrm[i] = arr2[i - sz1];
	}

	// Finally, return a pointer to the merged array.
	return arrm;
}
