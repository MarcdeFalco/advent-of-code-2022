#include <stdio.h>

// Rock = 0
// Paper = 1
// Scissors = 2

char strong(char a)
{
    // caution (a-1) % 3 might be negative
    return (a+2) % 3;
}

char weak(char a)
{
    return (a+1) % 3;
}

char point(char a)
{
    return 1+a;
}

char outcome(char o, char p)
{
    if (weak(o) == p)
        return 6;
    if (o == p)
        return 3;
    return 0;
}

int main(void)
{
    int score1 = 0;
    int score2 = 0;

    char o, p;
    while(scanf("%c %c\n", &o, &p) != EOF) {
        o -= 'A';
        p -= 'X';
        score1 += outcome(o, p) + point(p);
        if (p == 2)
            score2 += 6 + point(weak(o));
        else if (p == 1)
            score2 += 3 + point(o);
        else
            score2 += point(strong(o));
    }

    printf("Part 1 : %d\n", score1);
    printf("Part 2 : %d\n", score2);
}
