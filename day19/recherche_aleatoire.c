// Advent of Code 2022, jour 19, partie 2 : recherche aléatoire (Monte-Carlo).
// Pour le plan numéro argv[1] (0, 1 ou 2), on simule indéfiniment des
// parties de 32 minutes où, à chaque minute, l'action est tirée au hasard
// parmi les robots constructibles (poids 10 pour géode et obsidienne, 2 pour
// argile et minerai, 1 pour attendre), et l'on affiche chaque record.
// Aucune garantie d'optimalité : on arrête le programme à la main.
// Utilisation : ./a.out 0

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main(int argc, char **argv)
{
    // Coûts des robots du plan numéro argv[1] (0, 1 ou 2), lus dans input.txt :
    // on saute le numéro du plan et on garde les 6 nombres suivants.
    int costs[6];
    int i = atoi(argv[1]);
    FILE *fp = fopen("input.txt", "r");
    if (!fp) { printf("input.txt introuvable\n"); return 1; }
    char line[1000];
    for (int k = 0; k <= i; k++)
        if (fgets(line, sizeof line, fp) == NULL) { fclose(fp); return 1; }
    fclose(fp);
    int nums[7], n = 0;
    for (char *p = line; *p && n < 7; ) {
        if (*p >= '0' && *p <= '9') nums[n++] = (int)strtol(p, &p, 10);
        else p++;
    }
    for (int k = 0; k < 6; k++)
        costs[k] = nums[k+1];

    int bestG = 0;

    srand(time(0));

    while(true) {
        // ressources (majuscules) et robots (minuscules) :
        // minerai, argile, obsidienne, géode
        int R=0,C=0,O=0,G=0;
        int r=1,c=0,o=0,g=0;

        for(int t = 0; t < 32; t++) {
            int dR=r;
            int dC=c;
            int dO=o;
            int dG=g;

            // tirage pondéré : e contient chaque action autant de fois que
            // son poids, e[0] = 0 (attendre)
            int w[] = { 10, 10, 2, 2, 1 };
            int e[25] = {0};
            int ne = 1;
            if (R >= costs[4] && O >= costs[5])
                for (int j = 0; j < w[0]; j++) {
                    e[ne] = 4;
                    ne++;
                }
            if (R >= costs[2] && C >= costs[3])
                for (int j = 0; j < w[1]; j++) {
                    e[ne] = 3;
                    ne++;
                }
            if (R >= costs[1])
                for (int j = 0; j < w[2]; j++) {
                    e[ne] = 2;
                    ne++;
                }
            if (R >= costs[0])
                for (int j = 0; j < w[3]; j++) {
                    e[ne] = 1;
                    ne++;
                }
            int i = rand() % ne;
            if (e[i] == 1)
            {
                r += 1;
                R -= costs[0];
            }
            if (e[i] == 2)
            {
                c += 1;
                R -= costs[1];
            }
            if (e[i] == 3)
            {
                o += 1;
                R -= costs[2];
                C -= costs[3];
            }
            if (e[i] == 4)
            {
                g += 1;
                R -= costs[4];
                O -= costs[5];
            }

            R += dR;
            C += dC;
            O += dO;
            G += dG;
        }

        if (G > bestG)
        {
            printf("Mieux %d\n", G);
            bestG = G;
        }
    }
}
