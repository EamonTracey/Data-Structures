/* Title: array-rotation.c
 * Abstract: Left/right circular shift an array r times given a txt file with n integers.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 45 minutes
 * Date 08/30/22
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define filename "input.txt"

void fprinta(FILE *, int *, int);
void left_shift(int *, int, int);
void right_shift(int *, int, int);

int main() {
	// Open file
	FILE *fp;
	fp = fopen(filename, "r");
	if (fp == NULL) {
		fprintf(stderr, "File %s does not exist.\n", filename);
		return 1;
	}
	
	// Load n, r, and d
	int n, r;
	char d;
	fscanf(fp, "%d %d %c", &n, &r, &d);

	// Allocate memory for array
	int *iarr = (int *)malloc(n * sizeof(int));

	// Read integers into array from file
	int i;
	for (i = 0; i < n; ++i) {
		fscanf(fp, "%d", iarr + i);
	}

	// Shift array
	if (d == 'L') {
		left_shift(iarr, n, r);
	} else if (d == 'R') {
		right_shift(iarr, n, r);
	}

	fprinta(stdout, iarr, n);
	fprintf(stdout, "\n");

	free(iarr);
}

void fprinta(FILE *outfp, int *arr, int sz) {
	int i;
	for (i = 0; i < sz; ++i) {
		fprintf(outfp, "%d ", arr[i]);
	}
}

void left_shift(int *arr, int sz, int r) {
	r %= sz;
	if (sz < 1 || sz == r) return;

	int *first_r = malloc(r * sizeof(int));
	memcpy(first_r, arr, r * sizeof(int));

	int i;
	for (i = 0; i < sz - r; ++i) {
		arr[i] = arr[i + r];
	}

	memcpy(arr + sz - r, first_r, r * sizeof(int));
	free(first_r);
}

void right_shift(int *arr, int sz, int r) {
	r %= sz;
	if (sz < 1 || sz == r) return;

	int *last_r = malloc(r * sizeof(int));
	memcpy(last_r, arr + sz - r, r * sizeof(int));

	int i;
	for (i = sz - 1; i > r - 1; --i) {
		arr[i] = arr[i - r];
	}
	
	memcpy(arr, last_r, r * sizeof(int));
	free(last_r);
}
