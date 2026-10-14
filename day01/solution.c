// Advent of Code 2022, jour 1.
// Somme des calories de chaque bloc (blocs séparés par une ligne vide) dans
// un tableau d'accumulateurs, puis tri décroissant avec qsort : le premier
// élément donne la partie 1, les trois premiers la partie 2.

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_ELVES 500
#define BUF_SIZE 200

int compare_int(const void *a, const void *b)
{
    return *(int*)b - *(int*)a;
}

int main(void)
{
    int calories[MAX_ELVES];
    int nelves = 1;
    calories[0] = 0;

    FILE *fp = fopen("input", "r");

    while (true) {
        char buf[BUF_SIZE];
        if (fgets(buf, BUF_SIZE, fp) == NULL)
            break; // plus de lignes

        if (buf[0] == '\n') {
            calories[nelves] = 0;
            nelves++;
        } else {
            int cal = atoi(buf);
            calories[nelves-1] += cal;
        }
    }

    // tri décroissant avec qsort
    qsort(calories, nelves, sizeof(int), compare_int);

    printf("Partie 1 : %d\n", calories[0]);
    printf("Partie 2 : %d\n",
            calories[0] + calories[1] + calories[2]);
    fclose(fp);
}
