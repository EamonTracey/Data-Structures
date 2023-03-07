/* Title: dll-accounts.h
 * Abstract: This header file declares structs and function prototypes for dll-accounts.c
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 20 minutes
 * Date: 09/19/2022
 */

/*
 * Define an Account struct.
 * Account stores a name and money value (dollars and cents).
 */
typedef struct Account {
        char name[15];
        int dollars;
        int cents;
} Account;

 /*
 * Define a doubly linked node.
 * dlnode stores an Account, the previous node, and the next node.
 */
typedef struct dlnode {
        Account acc;
        struct dlnode *prev;
        struct dlnode *next;
} dlnode;

/*
 * Define a doubly linked list.
 * dllist stores the tail and head of the list.
 */
typedef struct dllist {
        dlnode *tail;
 	dlnode *head;
} dllist;

/*
 * Below are non-required yet useful functions.
 */
void append_head(dllist *, Account);
void append_tail(dllist *, Account);
void delete_head(dllist *);
void delete_tail(dllist *);
void display_acc(Account);
int count_accs(dllist *);
int contains(char[][15], char *, int);

/*
 * Below are functions required to be implemented.
 * Note: I disagree with the inconsistent naming scheme,
 * but I have used the same function names as provided in the assignment.
 */
void displayAll(dllist *);
void displayNth(dllist *);
void append(dllist *);
void appendNthPosition(dllist *);
void deleteRecord(dllist *);
void deleteNthNode(dllist *);
void find(dllist *);
void addMoney(dllist *);
void average(dllist *);
void displayAmountGreaterThan(dllist *);
void findMax(dllist *);
void findMin(dllist *);
void hasDuplicates(dllist *);
void getNumberOfRecords(dllist *);
void displayEven(dllist *);