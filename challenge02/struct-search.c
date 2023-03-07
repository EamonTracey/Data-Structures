/* Title: struct-search.c
 * Abstract: This program reads customer records from an input file and displays relevant records given a name. 
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 25 minutes
 * Date: 09/06/2022 
 */

typedef struct Customer {
	char name[50];
	int account;
	float balance;
} Customer;

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void display_report(Customer *, int, char *);
void sep();

int main() {
	// Prompt for filename.
	char filename[100];
	fprintf(stdout, "Enter an input file: ");
	fscanf(stdin, "%s", filename);

	// Open file.
	FILE *fp = fopen(filename, "r");
	if (fp == NULL) {
		fprintf(stderr, "Fail. The file %s does not exist.\n", filename);
		return 1;
	}

	// Determine number of cutomers.
	int n_customers;
	fscanf(fp, "%d", &n_customers);

	// Load student records.
	int i;
	Customer *customers = (Customer *)malloc(n_customers * sizeof(Customer));
	Customer *c;

	for (i = 0; i < n_customers; ++i) {
		c = &customers[i];
		// Format for a record is name, account, balance.
		// Read all values with one fscanf call.
		fscanf(
			fp,
			"%s %d %f",
			c->name, &c->account, &c->balance
		);
	}
	fclose(fp);

	char cont;
	char name[50];
	do {
		sep();
		fprintf(stdout, "Record Finder – Enter a customer name: ");
		fscanf(stdin, "%s", name);
		sep();
		display_report(customers, n_customers, name);
		fprintf(stdout, "Do you want to continue? (y/n): ");
		getc(stdin);
		fscanf(stdin, "%c", &cont);
	// Continue reading values until the user enters anything except 'y'.
	} while (cont == 'y');

	fprintf(stdout, "Bye!\n");

	// Free memory.
	free(customers);

	return 0;
}

// This functions displays the given customer name's name(s), account(s), and balance(s)
void display_report(Customer *customers, int sz, char *name) {
	int i;
	Customer c;
	int found = 0;
	for (i = 0; i < sz; ++i) {
		c = customers[i];
		// Use strcmp to detect whether the given name matches the current name in the iteration.
		if (!strcmp(name, c.name)) {
			fprintf(stdout, "Name: %s\nAccount: %d\nBalance: %g\n\n", c.name, c.account, c.balance);
			++found;
		}
	}
	if (found == 0) {
		fprintf(stdout, "Fail. %s doesn't exist.\n\n", name);
	}
}

// This functions prints a line separator
void sep() {
	fprintf(stdout, "--------------------------------------------------\n");
}
