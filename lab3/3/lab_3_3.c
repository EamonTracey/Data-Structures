#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void promptpi(int *);
void fprintia(int *, int);
int iinarray(int, int *, int);
void append(int **, int *, int);
void delete(int **, int *, int);
void reverse(int *, int);

int main() {
	// Read input filepath
	char filepath[100];
	fprintf(stdout, "Enter array filepath: ");
	fscanf(stdin, "%s", filepath);

	// Open input file for reading
	FILE *fp = fopen(filepath, "r");

	// Read array size
	int sz;
	fscanf(fp, "%d", &sz);

	// Allocate initial array
	int *arr = (int *)malloc(sz * sizeof(int));

	// Load initial array values
	int i;
	for (i = 0; i < sz; ++i) {
		fscanf(fp, "%d", arr + i);
	}
	fprintia(arr, sz);

	// Show options
	fprintf(stdout, "\nThis is a list of operations\n\t1. Append a number\n\t2. Delete a number\n\t3. Reverse the array\n");

	int op;
	char cont;
	int n;
	do {
		// Ask for option
		fprintf(stdout, "\nEnter your option: ");
		fscanf(stdin, "%d", &op);

		// Handle option
		switch (op) {
		case 1:
			fprintf(stdout, "Enter a number to append: ");
			fscanf(stdin, "%d", &n);
			if (n < 0) promptpi(&n);
			if (iinarray(n, arr, sz)) {
				fprintf(stdout, "%d is already in the array.\n", n);
				break;
			}
			append(&arr, &sz, n);
			fprintia(arr, sz);
			break;
		case 2:
			fprintf(stdout, "Enter a number to delete: ");
			fscanf(stdin, "%d", &n);
			if (n < 0) promptpi(&n);
			if (!iinarray(n, arr, sz)) {
				fprintf(stdout, "%d is not in the array.\n", n);
				break;
			}
			delete(&arr, &sz, n);
			fprintia(arr, sz);
			break;
		case 3:
			reverse(arr,sz);
			fprintia(arr, sz);
		default:
			break;
		}

		// Ask to continue
		fgetc(stdin);
		fprintf(stdout, "Continue? (Y/N): ");
		fscanf(stdin, "%c", &cont);
	} while (cont == 'Y');
}

void promptpi(int *n) {
	while (*n < 0) {
		fprintf(stdout, "Please enter a positive number: ");
		fscanf(stdin, "%d", n);
		fgetc(stdin);
	}
}

void fprintia(int *arr, int sz) {
	int i;
	fprintf(stdout, "Array values: ");
	for (i = 0; i < sz; ++i) {
		fprintf(stdout, "%d ", arr[i]);
	}
	fprintf(stdout, "\nArray size: %d\n", sz);
}

int iinarray(int n, int *arr, int sz) {
	int i;
	for (i = 0; i < sz; ++i) {
		if (arr[i] == n) {
			return 1;
		}
	}
	return 0;
}

void append(int **arr, int *sz, int n) {
	++(*sz);
	int *new = (int *)malloc(*sz * sizeof(int));

	memcpy(new, *arr, (*sz - 1) * sizeof(int));
	new[*sz - 1] = n;

	free(*arr);
	*arr = new;
}

void delete(int **arr, int *sz, int n) {
	--(*sz);
	int *new = (int *)malloc(*sz * sizeof(int));
	
	int i;
	int newi = 0;
	for (i = 0; i < (*sz + 1); ++i) {
		if ((*arr)[i] == n) {
			continue;
		} else {
			new[newi] = (*arr)[i];
			++newi;
		}
	}

	free(*arr);
	*arr = new;
}

void reverse(int *arr, int sz) {
	int *orig = malloc(sz * sizeof(int));
	memcpy(orig, arr, sz * sizeof(int));

	int i;
	for (i = sz - 1; i >= 0; --i) {
		arr[sz - 1 - i] = orig[i];
	}
}
