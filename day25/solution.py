"""Advent of Code 2022, jour 25.

Base 5 équilibrée : les chiffres '=-012' valent -2 à 2. La lecture somme les
chiffres multipliés par les puissances de 5 croissantes. Pour l'écriture, on
décale de 2 : le chiffre est CHIFFRES[(S + 2) % 5] et l'on continue avec
(S + 2) // 5, ce qui revient à une division euclidienne avec un reste dans
{-2, ..., 2}. Il n'y a qu'une partie ce jour-là.
"""

CHIFFRES = '=-012'


def lire_snafu(mot):
    valeur = 0
    puissance = 1
    for c in reversed(mot):
        valeur += (CHIFFRES.index(c) - 2) * puissance
        puissance *= 5
    return valeur


def ecrire_snafu(S):
    mot = ''
    while S > 0:
        mot = CHIFFRES[(S + 2) % 5] + mot
        S = (S + 2) // 5
    return mot


lignes = open('input.txt').read().strip().split('\n')
print('Partie 1 :', ecrire_snafu(sum(lire_snafu(ligne) for ligne in lignes)))
