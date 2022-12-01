#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

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

    FILE *fp = fopen("input","r");

    while (true) {
        char buf[BUF_SIZE];
        if (fgets(buf, BUF_SIZE, fp) == NULL)
            break; // no more lines
         
        if (buf[0] == '\n') {
            calories[nelves] = 0;
            nelves++;
        } else {
            int cal = atoi(buf);
            calories[nelves-1] += cal;
        }
    }

    // use stdlib sort to sort in decreasing order
    qsort(calories, nelves, sizeof(int),
            compare_int);

    printf("Part 1 : %d\n", calories[0]);
    printf("Part 2 : %d\n", 
            calories[0]+calories[1]+calories[2]);
    fclose(fp);
}
