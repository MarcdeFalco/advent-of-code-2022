// Advent of Code 2022, jour 2.
// Coups codés 0 (pierre), 1 (feuille), 2 (ciseaux) : le coup qui bat a est
// (a + 1) % 3, celui que a bat est (a + 2) % 3. Lecture sur l'entrée
// standard : ./a.out < input

#include <stdio.h>

// coup que a bat
char strong(char a)
{
    // attention : (a - 1) % 3 peut être négatif en C
    return (a+2) % 3;
}

// coup qui bat a
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
    while (scanf("%c %c\n", &o, &p) != EOF) {
        o -= 'A';
        p -= 'X';
        score1 += outcome(o, p) + point(p);
        // partie 2 : p donne l'issue voulue (0 perdre, 1 nul, 2 gagner)
        if (p == 2)
            score2 += 6 + point(weak(o));
        else if (p == 1)
            score2 += 3 + point(o);
        else
            score2 += point(strong(o));
    }

    printf("Partie 1 : %d\n", score1);
    printf("Partie 2 : %d\n", score2);
}
