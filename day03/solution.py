"""Advent of Code 2022, jour 3.

Partie 1 : chaque ligne est coupée en deux moitiés et l'on cherche les
caractères communs par des tests d'appartenance. Partie 2 : par groupes de
trois lignes, intersection de trois ensembles. La priorité d'une lettre se
déduit de son code ASCII.
"""


def priorite(c):
    if ord(c) < ord('a'):  # majuscule
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def lire_donnees(nom_fichier='input.txt'):
    return [ligne.strip() for ligne in open(nom_fichier)]


def partie1(sacs):
    score = 0
    for sac in sacs:
        n = len(sac)
        gauche, droite = sac[:n // 2], sac[n // 2:]
        communs = ''
        for c in gauche:
            if c in droite and c not in communs:
                score += priorite(c)
                communs += c
    return score


def partie2(sacs):
    score = 0
    for i in range(len(sacs) // 3):
        a, b, c = map(set, sacs[3 * i:3 * i + 3])
        commun = list(a.intersection(b).intersection(c))[0]
        score += priorite(commun)
    return score


sacs = lire_donnees()
print('Partie 1 :', partie1(sacs))
print('Partie 2 :', partie2(sacs))
