"""Advent of Code 2022, jour 4.

Pour deux intervalles [a, b] et [c, d] : inclusion si a <= c <= d <= b ou
l'inverse (partie 1), chevauchement si a <= c <= b ou c <= a <= d
(partie 2). Python permet d'enchaîner les comparaisons.
"""


def lire_donnees(nom_fichier='input.txt'):
    paires = []
    for ligne in open(nom_fichier):
        e1, e2 = ligne.split(',')
        a, b = map(int, e1.split('-'))
        c, d = map(int, e2.split('-'))
        paires.append((a, b, c, d))
    return paires


def partie1(paires):
    return sum(1 for a, b, c, d in paires
               if a <= c <= d <= b or c <= a <= b <= d)


def partie2(paires):
    return sum(1 for a, b, c, d in paires
               if a <= c <= b or c <= a <= d)


paires = lire_donnees()
print('Partie 1 :', partie1(paires))
print('Partie 2 :', partie2(paires))
