/* Title: dll-accounts.c
 * Abstract: This program creates a doubly linked list to store structs representing bank accounts. Multiple operations on the doubly linked list are implemented including push (head/tail), pop (head/tail), display all, max, min, etc.
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 5 hours
 * Date: 09/19/2022
 */

#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dll-accounts.h"

int main() {
	int n;
	FILE *fp;
	char filepath[50];

	// Read input filepath from user.
	// If the file does not exist, exit with an error message.
	fprintf(stdout, "Enter input file: ");
	fscanf(stdin, "%s", filepath);
	fp = fopen(filepath, "r");
	if (fp == NULL) {
		fprintf(stderr, "File %s does not exist.", filepath);
		return 1;
	}

	// Initialize an empty doubly linked list.
	dllist *list = (dllist *)malloc(sizeof(dllist));
	list->head = NULL;
	list->tail = NULL;

	// Read how many accounts are in the input file.
	fscanf(fp, "%d", &n);
	fgetc(fp);

	int i;
	Account acc;
	for (i = 0; i < n; ++i) {
		fscanf(fp, "%s %d %d", acc.name, &acc.dollars, &acc.cents);
		append_tail(list, acc);
	}

	// Close the file.
	fclose(fp);

	fprintf(stdout, "Operations on doubly linked list:\n\t1. Display all nodes\n\t2. Display nth record\n\t3. Append a new record - Head or Tail? (H/T)\n\t4. Append a new record in the Nth position\n\t5. Delete a record - Head or Tail? (H/T)\n\t6. Delete Nth record\n\t7. Find a record\n\t8. Add money to account\n\t9. Average all amounts\n\t10. Display the records of people with more than n.m (n=dollars, m=cents) in their account\n\t11. Find max amount\n\t12. Find min amount\n\t13. Check for duplicates\n\t14. Get number of records\n\t15. Display even numbered records\n");

	// Main loop of the function asks the user to enter options.
	// The requested option is applied accordingly.
	int op;
	char cont = 'Y';
	while (cont == 'Y') {
		fprintf(stdout, "Enter option: ");
		fscanf(stdin, "%d", &op);

		switch (op) {
		case 1:
			displayAll(list);
			break;
		case 2:
			displayNth(list);
			break;
		case 3:
			append(list);
			break;
		case 4:
			appendNthPosition(list);
			break;
		case 5:
			deleteRecord(list);
			break;
		case 6:
			deleteNthNode(list);
			break;
		case 7:
			find(list);
			break;
		case 8:
			addMoney(list);
			break;
		case 9:
			average(list);
			break;
		case 10:
			displayAmountGreaterThan(list);
			break;
		case 11:
			findMax(list);
			break;
		case 12:
			findMin(list);
			break;
		case 13:
			hasDuplicates(list);
			break;
		case 14:
			getNumberOfRecords(list);
			break;
		case 15:
			displayEven(list);
			break;
		default:
			break;
		}

		fprintf(stdout, "Continue? (Y/N): ");
		getc(stdin);
		fscanf(stdin, "%c", &cont);
	}

	// Free all dynamically allocated memory.
	dlnode *curr = list->head;
	dlnode *ref;
	while (curr != NULL) {
		ref = curr;
		curr = curr->next;
		free(ref);
	}
	free(list);

	return 0;
}

/*
 * Append to the head of a doubly linked list.
 */
void append_head(dllist *list, Account acc) {	
	dlnode *node = (dlnode *)malloc(sizeof(dlnode));
	node->acc = acc;
	node->prev = NULL;
	node->next = NULL;

	if (list->head == NULL) {
		list->head = node;
		list->tail = node;
		return;
	}

	node->next = list->head;
	list->head->prev = node;
	list->head = node;
}

/*
 * Append to the tail of a doubly linked list.
 */
void append_tail(dllist *list, Account acc) {	
	dlnode *node = (dlnode *)malloc(sizeof(dlnode));
	node->acc = acc;
	node->prev = NULL;
	node->next = NULL;

	if (list->head == NULL) {
		list->head = node;
		list->tail = node;
		return;
	}

	node->prev = list->tail;
	list->tail->next = node;
	list->tail = node;
}

/*
 * Delete from the head of a doubly linked list.
 */
void delete_head(dllist *list) {
	if (list->head == NULL) {
		return;
	}

	dlnode *ref = list->head;

	if (list->head == list->tail) {
        list->head = NULL;
        list->tail = NULL;
        free(ref);
        return;
	}

	list->head = ref->next;
	list->head->prev = NULL;

	free(ref);
}

/*
 * Delete from the tail of a doubly linked list.
 */
void delete_tail(dllist *list) {
	if (list->head == NULL) {
		return;
	}
    
    if (list->head == list->tail) {
        free(list->head);
        list->head = NULL;
        list->tail = NULL;
        return;
    }
    
    dlnode *ref = list->tail;
    list->tail = ref->prev;
    list->tail->next = NULL;

    free(ref);
}

/*
 * Print an Account struct formatted cleanly.
 */
void display_acc(Account acc) {
	fprintf(stdout, "%-15s%-10d%d\n", acc.name, acc.dollars, acc.cents);
}

/*
 * Count the number of accounts in a doubly linked list.
 */
int count_accs(dllist *list) {
	int n = 0;
	dlnode *curr = list->head;

	while (curr != NULL) {
		++n;
		curr = curr->next;
	}

	return n;
}

/*
 * Determine if a string exists in an array of strings.
 * Max string length of 15 reflects the max length of an Account name.
 */
int contains(char arr[][15], char *str, int sz) {
	int i;
	for (i = 0; i < sz; ++i) {
		if (!strcmp(arr[i], str)) {
			return 1;
		}
	}
	return 0;
}

/*
 * Display all Accounts in a doubly linked list.
 */
void displayAll(dllist *list) {
	dlnode *curr = list->head;
	while (curr != NULL) {
		display_acc(curr->acc);
		curr = curr->next;
	}
}

/*
 * Display the nth account in a doubly linked list.
 */
void displayNth(dllist *list) {
	int n;

	// Read n from user.
	fprintf(stdout, "Enter n: ");
	fscanf(stdin, "%d", &n);

	// When n is 1, display the head.
	// Note that n starts at 1.
	if (n == 1) {
		display_acc(list->head->acc);
		return;
	}

	// Loop through list until reaching the nth position.
	dlnode *curr = list->head->next;
	int i;
	for (i = 1; i < n - 1; ++i) {
		curr = curr->next;
	}
	
	display_acc(curr->acc);
}

/*
 * Prompt to add a new Account to the head/tail.
 */
void append(dllist *list) {
	char ht;
	char money[20];
	Account acc;

	// Ask whether to append to the head or tail.
	fprintf(stdout, "Append to head or tail? (H/T): ");
	getc(stdin);
	fscanf(stdin, "%c", &ht);

	// Get account from user.
	// Use strtok to parse double into dollars and cents.
	fprintf(stdout, "Enter name: ");
	fscanf(stdin, "%s", acc.name);
	fprintf(stdout, "Enter money (n.m): ");
	fscanf(stdin, "%s", money);
	acc.dollars = atoi(strtok(money, "."));
	acc.cents = atoi(strtok(NULL, "."));

	if (ht == 'H') {
		append_head(list, acc);
	} else if (ht == 'T') {
		append_tail(list, acc);
	}

	displayAll(list);
}

/*
 * Append an account to the nth position of a doubly linked list.
 */
void appendNthPosition(dllist *list) {
	int n;
	char money[20];
	Account acc;

	// Read n from user.
	fprintf(stdout, "Enter n: ");
	fscanf(stdin, "%d", &n);

	// Get account from user.
	// Use strtok to parse double into dollars and cents.
	fprintf(stdout, "Enter name: ");
	fscanf(stdin, "%s", acc.name);
	fprintf(stdout, "Enter money (n.m): ");
	fscanf(stdin, "%s", money);
	acc.dollars = atoi(strtok(money, "."));
	acc.cents = atoi(strtok(NULL, "."));

	// If n = 1, append to the head.
	if (n == 1) {
		append_head(list, acc);
		return;
	}

	// Loop through list until reaching the (n - 1)th position.
	dlnode *curr = list->head;
	int i;
	for (i = 1; i < n - 1; ++i) {
		curr = curr->next;
	}

	// If we have reached the end of the list, append to the tail.
	if (curr->next == NULL) {
		append_tail(list, acc);
		return;
	}

	dlnode *node = (dlnode *)malloc(sizeof(dlnode));
	node->acc = acc;
	node->prev = NULL;
	node->next = NULL;

	dlnode *ref = curr->next;
	node->next = ref;
	ref->prev = node;
	curr->next = node;
	node->prev = curr;

	displayAll(list);
}

/*
 * Prompt to delete an Account to the head/tail.
 */
void deleteRecord(dllist *list) {
	char ht;

	// Ask whether to delete from the head or tail.
	fprintf(stdout, "Delete from head or tail? (H/T): ");
	getc(stdin);
	fscanf(stdin, "%c", &ht);

	if (ht == 'H') {
		delete_head(list);
	} else if (ht == 'T') {
		delete_tail(list);
	}

	displayAll(list);
}

/*
 * Delete an account from the nth position of a doubly linked list.
 */
void deleteNthNode(dllist *list) {
	int n;

	// Read n from user.
	fprintf(stdout, "Enter n: ");
	fscanf(stdin, "%d", &n);

	// If n = 1, delete from the head.
	if (n == 1) {
		delete_head(list);
		return;
	}

	// Loop through list until reaching the (n - 1)th position.
	dlnode *curr = list->head;
	int i;
	for (i = 1; i < n - 1; ++i) {
		curr = curr->next;
	}

	// If we have reached the end of the list, delete from the tail.
	if (curr->next->next == NULL) {
		delete_tail(list);
		return;
	}

	dlnode *ref = curr->next;
	curr->next = ref->next;
	ref->next->prev = curr;
	free(ref);

	displayAll(list);
}

/*
 * Find and display the Account matching a name in a doubly linked list.
 * If the name matches multiple Accounts, display all relevant accounts.
 */
void find(dllist *list) {
	char name[15];

	fprintf(stdout, "Enter name: ");
	fscanf(stdin, "%s", name);

	dlnode *curr = list->head;
	while (curr != NULL) {
		if (!strcmp(curr->acc.name, name)) {
			display_acc(curr->acc);
		}
		curr = curr->next;
	}
}

/*
 * Add money to an Account matching a name in a doubly linked list.
 * If the name matches multiple Accounts, add money to all relevant accounts. 
 */
void addMoney(dllist *list) {
	char name[15];
	char money[20];
	int dol;
	int cen;

	// Read name from user.
	fprintf(stdout, "Enter name: ");
	fscanf(stdin, "%s", name);

	// Use strtok to parse double into dollars and cents.
	fprintf(stdout, "Enter money (n.m): ");
	fscanf(stdin, "%s", money);
	dol = atoi(strtok(money, "."));
	cen = atoi(strtok(NULL, "."));

	dlnode *curr = list->head;
	while (curr != NULL) {
		if (!strcmp(curr->acc.name, name)) {
			curr->acc.dollars += dol;
			curr->acc.cents += cen;

			// If the cents value is greater than 100, add 1 dollar and remove 100 cents.
			if (curr->acc.cents >= 100) {
				++curr->acc.dollars;
				curr->acc.cents -= 100;
			}
		}
		curr = curr->next;
	}

	displayAll(list);
}

/*
 * Compute and display the average Account balance of a doubly linked list.
 */
void average(dllist *list) {
	if (list->head == NULL) {
		return;
	}

	int dol = 0;
	int cen = 0;
	float tot;
	float average;

	int n = 0;
	dlnode *curr = list->head;
	while (curr != NULL) {
		dol += curr->acc.dollars;
		cen += curr->acc.cents;
		curr = curr->next;
		++n;
	}

	tot = (float)dol + (float)cen * 0.01;
	average = tot / (float)n;

	fprintf(stdout, "The average is $%.2f.\n", average);
}

/*
 * Display Accounts with more money than a certain amount.
 */
void displayAmountGreaterThan(dllist *list) {
	char money[20];
	int dol;
	int cen;

	// Use strtok to parse double into dollars and cents.
	fprintf(stdout, "Enter money (n.m): ");
	fscanf(stdin, "%s", money);
	dol = atoi(strtok(money, "."));
	cen = atoi(strtok(NULL, "."));

	dlnode *curr = list->head;
	while (curr != NULL) {
		// To compare money values, first check if dollars are greater.
		// If dollars are equal, check if cents are greater.
		if (curr->acc.dollars > dol || (curr->acc.dollars == dol && curr->acc.cents > cen)) {
			display_acc(curr->acc);
		}
		curr = curr->next;
	}
}

/*
 * Find and display the Account with the most money.
 * If multiple accounts tie for the most, display all relevant accounts.
 */
void findMax(dllist *list) {
	int dol = 0;
	int cen = 0;

	dlnode *curr = list->head;
	while (curr != NULL) {
		// To compare money values, first check if dollars are greater.
		// If dollars are equal, check if cents are greater.
		if (curr->acc.dollars > dol || (curr->acc.dollars == dol && curr->acc.cents > cen)) {
			dol = curr->acc.dollars;
			cen = curr->acc.cents;
		}
		curr = curr->next;
	}

	curr = list->head;
	while (curr != NULL) {
		if (curr->acc.dollars == dol && curr->acc.cents == cen) {
			display_acc(curr->acc);
		}
		curr = curr->next;
	}
}

/*
 * Find and display the Account with the least money.
 * If multiple accounts tie for the least, display all relevant accounts.
 */
void findMin(dllist *list) {
	int dol = INT_MAX;
	int cen = INT_MAX;

	dlnode *curr = list->head;
	while (curr != NULL) {
		// To compare money values, first check if dollars are lesser.
		// If dollars are equal, check if cents are lesser.
		if (curr->acc.dollars < dol || (curr->acc.dollars == dol && curr->acc.cents < cen)) {
			dol = curr->acc.dollars;
			cen = curr->acc.cents;
		}
		curr = curr->next;
	}

	curr = list->head;
	while (curr != NULL) {
		if (curr->acc.dollars == dol && curr->acc.cents == cen) {
			display_acc(curr->acc);
		}
		curr = curr->next;
	}
}

/*
 * Determine if a doubly linked list has duplicate names and display all duplicates.
 */
void hasDuplicates(dllist *list) {
	int n = count_accs(list);
	char names[n][15];
	int n_names = 0;
	char duplicates[n][15];
	int n_duplicates = 0;

	// Traverse list, adding each name to a names array if it's new
	// or to a duplicates array if it's already in the names array.
	dlnode *curr = list->head;
	while (curr != NULL) {
		if (contains(names, curr->acc.name, n_names)) {
			strcpy(duplicates[n_duplicates++], curr->acc.name);
		} else {
			strcpy(names[n_names++], curr->acc.name);
		}

		curr = curr->next;
	}

	// Display all accounts with names that are contained in the duplicates array.
	curr = list->head;
	while (curr != NULL) {
		if (contains(duplicates, curr->acc.name, n_duplicates)) {
			display_acc(curr->acc);
		}

		curr = curr->next;
	}
}

/*
 * Display the number of Accounts in a doubly linked list.
 */
void getNumberOfRecords(dllist *list) {
	int n = count_accs(list);
	fprintf(stdout, "There are %d records.\n", n);
}

/*
 * Display the evenly numbered accounts in a doubly linked list.
 */
void displayEven(dllist *list) {
	dlnode *curr = list->head;
	int n = 1;

	while (curr != NULL) {
		if (n++ % 2 == 0) {
			display_acc(curr->acc);
		}
		curr = curr->next;
	}
}