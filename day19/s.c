#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>


int main(int argc, char **argv)
{
    int costs1[] = { 4, 4, 4, 14, 3, 16 };
    int costs2[] = { 3, 3, 2, 19, 2, 12 };
    int costs3[] = { 4, 4, 4, 9, 4, 16 };

    int *costss[] = { costs1, costs2, costs3 };

    int i = atoi(argv[1]);

    int *costs = costss[i];

    //int costs[] = { 4, 2, 3, 14, 2, 7 };
    int bestG = 0;

    srand(time(0));

    while(true) {
        int R=0,C=0,O=0,G=0;
        int r=1,c=0,o=0,g=0;

        for(int t = 0; t < 32; t++) {
            int dR=r;
            int dC=c;
            int dO=o;
            int dG=g;

            int w[] = { 10, 10, 2, 2, 1 };
            int e[25] = {};
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
