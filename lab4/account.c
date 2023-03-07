/* Title: account.c
 * Abstract: Manipulate singly linked list of structs.
 * Author: Eamon Tracey 
 * Email: etracey@nd.edu
 * Estimate: 1 hour
 * Date: 09/13/2022
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct Account {
	char name[50];
	int dollars;
	int cents;
} Account;

typedef struct slnode {
	Account account;
	struct slnode *next;
} slnode;

typedef struct sllist {
	slnode *head;
} sllist;

void display_all(sllist *list) {
	slnode *node = list->head;
	while (node != NULL) {
		fprintf(stdout, "%s %d %d\n", node->account.name, node->account.dollars, node->account.cents);
		node = node->next;
	}
}

void display_nth(sllist *list, int n) {
	slnode *node = list->head;

	int i = 1;
	while (i < n) {
		node = node->next;
		++i;
	}

	fprintf(stdout, "%s %d %d\n", node->account.name, node->account.dollars, node->account.cents);
}

void append_head(sllist *list, Account acc) {
	slnode *ah_node = (slnode *)malloc(sizeof(slnode));
	ah_node->account = acc;
	ah_node->next = list->head;
	list->head = ah_node;
}

void append_tail(sllist *list, Account acc) {
	slnode *at_node = (slnode *)malloc(sizeof(slnode));
	at_node->account = acc;
	at_node->next = NULL;

	if (list->head == NULL) {
		list->head = at_node;
		return;
	}

	slnode *node = list->head;
	while (node->next != NULL) {
		node = node->next;
	}

	node->next = at_node;
}

void append_nth(sllist *list, Account acc, int n) {
	if (n == 1) {
		append_head(list, acc);
		return;
	}

	slnode *an_node = (slnode *)malloc(sizeof(slnode));
	an_node->account = acc;

	slnode *node = list->head;
	int i;
	for (i = 1; i < n - 1; ++i) {
		node = node->next;
	}

	an_node->next = node->next;
	node->next = an_node;
}

void delete_head(sllist *list) {
	if (list->head == NULL) {
		return;
	}

	slnode *tmp = list->head;
	list->head = list->head->next;

	free(tmp);
}

void delete_tail(sllist *list) {
	if (list->head == NULL) {
		return;
	}

	if (list->head->next == NULL) {
		free(list->head);
		list->head = NULL;
		return;
	}

	slnode *node = list->head;
	while (node->next->next != NULL) {
		node = node->next;
	}

	free(node->next);
	node->next = NULL;
}

void delete_nth(sllist *list, int n) {
	if (n == 1) {
		delete_head(list);
		return;
	}

	slnode *node = list->head;
	int i;
	for (i = 1; i < n - 1; ++i) {
		node = node->next;
	}
	
	slnode *tmp = node->next;
	node->next = node->next->next;

	free(tmp);
}

int main() {
	FILE *fp;
	char filename[100];
	int n_records;

	fprintf(stdout, "Enter input file: ");
	fscanf(stdin, "%s", filename);

	fp = fopen(filename, "r");
	fscanf(fp, "%d", &n_records);

	sllist *list = (sllist *)malloc(sizeof(sllist));
	list->head = NULL;

	int i;
	Account acc;
	for (i = 0; i < n_records; ++i) {
		fscanf(fp, "%s %d %d", acc.name, &acc.dollars, &acc.cents);
		append_tail(list, acc);
	}

	fclose(fp);

	fprintf(stdout, "Records entered into a singly linked list.\n");
	fprintf(stdout, "Here is a list of the operations on the singly linked list:\n");
	fprintf(stdout, "\t1. Display all records\n");
	fprintf(stdout, "\t2. Display nth record\n");
	fprintf(stdout, "\t3. Append a new record (H/T)\n");
	fprintf(stdout, "\t4. Append a new record in the nth position\n");
	fprintf(stdout, "\t5. Delete a record (H/T)\n");
	fprintf(stdout, "\t6. Delete a record in the nth position\n");

	int op;
	char cont;
	int n;
	char ht;
	do {
		fprintf(stdout, "\nEnter your option: ");
		fscanf(stdin, "%d", &op);

		switch (op) {
		case 1:
			display_all(list);
			break;
		case 2:
			fprintf(stdout, "Enter n: ");
			fscanf(stdin, "%d", &n);
			display_nth(list, n);
			break;
		case 3:
			fprintf(stdout, "Append to head or tail? (H/T): ");
			getc(stdin);
			fscanf(stdin, "%c", &ht);
			fprintf(stdout, "Enter name: ");
			fscanf(stdin, "%s", acc.name);
			fprintf(stdout, "Enter dollars: ");
			fscanf(stdin, "%d", &acc.dollars);
			fprintf(stdout, "Enter cents: ");
			fscanf(stdin, "%d", &acc.cents);
			if (ht == 'H') append_head(list, acc);
			if (ht == 'T') append_tail(list, acc);
			break;
		case 4:
			fprintf(stdout, "Enter n: ");
			fscanf(stdin, "%d", &n);
			fprintf(stdout, "Enter name: ");
			fscanf(stdin, "%s", acc.name);
			fprintf(stdout, "Enter dollars: ");
			fscanf(stdin, "%d", &acc.dollars);
			fprintf(stdout, "Enter cents: ");
			fscanf(stdin, "%d", &acc.cents);
			append_nth(list, acc, n);
			break;
		case 5:
			fprintf(stdout, "Delete from head or tail? (H/T): ");
			getc(stdin);
			fscanf(stdin, "%c", &ht);
			if (ht == 'H') delete_head(list);
			if (ht == 'T') delete_tail(list);
			break;
		case 6:
			fprintf(stdout, "Enter n: ");
			fscanf(stdin, "%d", &n);
			delete_nth(list, n);
			break;
		default:
			break;
		}

		fprintf(stdout, "\nContinue? (Y/N): ");
		getc(stdin);
		fscanf(stdin, "%c", &cont);
	} while (cont == 'Y');

	slnode *node = list->head;
	slnode *tmp;
	while (node != NULL) {
		tmp = node;
		node = node->next;
		free(tmp);
	}
	free(list);

	return 0;
}
