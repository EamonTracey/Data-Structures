/* Title: lab_2_1.c
 * Abstract This program reads and writes to a file.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 15 minutes
 * Date: 08/30/22
 */

#include <stdio.h>

int main() {
	FILE *ifptr = fopen("input.txt", "r");

	if (ifptr == NULL) {
		fprintf(stderr, "File does not exist.\n");
		return 1;
	}

	// Read from input.txt
	int num;
	while (fscanf(ifptr, "%d", &num) == 1) {
		fprintf(stdout, "Input value read: num = %d\n", num);
	}
	fclose(ifptr);

	ifptr = fopen("output.txt", "w");

	// Write to output.txt
	fprintf(ifptr, "I wrote to output.txt!\n");
	fclose(ifptr);
}
