#include <stdio.h>

#define NPAIRS 2000

int main(void)
{
    int elves[NPAIRS * 4];
    int i = 0;
    while(scanf("%d-%d,%d-%d",
        &elves[4*i],
        &elves[4*i+1],
        &elves[4*i+2],
        &elves[4*i+3]) != EOF) {
        i++;
    }

    int countains = 0;
    int overlaps = 0;
    for(int k = 0; k < i; k++) {
        int a = elves[4*k];
        int b = elves[4*k+1];
        int c = elves[4*k+2];
        int d = elves[4*k+3];
        if ((a <= c && d <= b) 
            || (c <= a && b <= d))
            countains++;
        if ((a <= c && c <= b)
            || (c <= a && a <= d))
            overlaps++;
    }

    printf("Part 1: %d\n", countains);
    printf("Part 2: %d\n", overlaps);
}
