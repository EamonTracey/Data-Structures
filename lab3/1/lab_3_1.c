#include <stdio.h>

typedef struct Student {
	char name[30];
	float score1;
	float score2;
	float average;
} Student;

int main() {
	char filepath[100];
	fprintf(stdout, "Enter students filepath: ");
	fscanf(stdin, "%s", filepath);

	Student s1;
	Student s2;

	FILE *fp = fopen(filepath, "r");
	fscanf(fp, "%s %f %f %s %f %f", s1.name, &s1.score1, &s1.score2, s2.name, &s2.score1, &s2.score2);
	s1.average = (s1.score1 + s1.score2) / 2.0;
	s2.average = (s2.score1 + s2.score2) / 2.0;
	fclose(fp);

	fprintf(stdout, "%s's average: %.1f\n", s1.name, s1.average);
	fprintf(stdout, "%s's average: %.1f\n", s2.name, s2.average);

	if (s1.average == s2.average) {
		fprintf(stdout, "%s and %s have the same score.\n", s1.name, s2.name);
	} else if (s1.average > s2.average) {
		fprintf(stdout, "%s has a better score than %s.\n", s1.name, s2.name);
	} else {
		fprintf(stdout, "%s has a better score than %s.\n", s2.name, s1.name);
	}
}
