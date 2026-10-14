"""Advent of Code 2022, jour 1.

L'entrée est découpée en blocs séparés par une ligne vide ; on somme chaque
bloc. Partie 1 : le plus grand total ; partie 2 : la somme des trois plus
grands (obtenus par un tri).
"""


def lire_donnees(nom_fichier='input'):
    blocs = open(nom_fichier).read().strip().split('\n\n')
    return [sum(map(int, bloc.split('\n'))) for bloc in blocs]


def partie1(totaux):
    return max(totaux)


def partie2(totaux):
    return sum(sorted(totaux)[-3:])


totaux = lire_donnees()
print('Partie 1 :', partie1(totaux))
print('Partie 2 :', partie2(totaux))
