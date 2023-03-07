/* Title: struct-array.c
 * Abstract: This program reads student records from an input file, calculates the averages, and displays a report. 
 * Author: Eamon Tracey
 * Email: etracey@nd.edu
 * Estimate: 1 hour
 * Date: 09/06/2022 
 */

typedef struct Student {
	char name[50];
	int id;
	float scores[5];
	float average;
} Student;

#include <stdio.h>
#include <stdlib.h>

float average(float *, int);
void display_report(Student *, int);
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

	// Determine number of students.
	int n_students;
	fscanf(fp, "%d", &n_students);

	// Load student records.
	int i;
	Student *students = (Student *)malloc(n_students * sizeof(Student));
	Student *s;

	for (i = 0; i < n_students; ++i) {
		s = &students[i];
		// Format for a record is name, id, scores 1-5.
		// Read all these values in with one fscanf statement.
		fscanf(
			fp,
			"%s %d %f %f %f %f %f",
			s->name, &s->id, &s->scores[0], &s->scores[1], &s->scores[2], &s->scores[3], &s->scores[4]
		);
		// Calculate average.
		s->average = average(s->scores, 5);
	}
	fclose(fp);

	sep();
	fprintf(stdout, "Course Report: Quiz Average\n");
	sep();
	display_report(students, n_students);
	sep();

	// Free memory.
	free(students);

	return 0;
}

// This function calculates the average of an array of floats.
float average(float *floats, int sz) {
	int i;
	float sum = 0;
	for (i = 0; i < sz; ++i) {
		sum += floats[i];
	}
	return sum / (float)sz;
}

// This functions displays student names and their respectives IDs and averages.
void display_report(Student *students, int sz) {
	int i;
	Student s;
	for (i = 0; i < sz; ++i) {
		s = students[i];
		fprintf(stdout, "%s (%d): %g\n", s.name, s.id, s.average);
	}
}

// This functions prints a line separator to stdout.
void sep() {
	fprintf(stdout, "--------------------------------------------------\n");
}
