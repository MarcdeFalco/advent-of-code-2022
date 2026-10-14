"""Advent of Code 2022, jour 13.

Comparaison récursive de listes imbriquées à trois issues : True (dans
l'ordre), False (dans le désordre) ou None (égalité, on continue). On
compare les premiers éléments puis le reste ; un entier comparé à une liste
est remplacé par la liste [entier]. Partie 1 : somme des indices des paires
dans l'ordre. Partie 2 : tri de tous les paquets avec cmp_to_key, puis
produit des positions des deux paquets séparateurs.
"""
import json
from functools import cmp_to_key


def lire_donnees(nom_fichier='input.txt'):
    blocs = open(nom_fichier).read().strip().split('\n\n')
    return [tuple(map(json.loads, bloc.split('\n'))) for bloc in blocs]


def compare(l1, l2):
    if l1 == [] and l2 == []:
        return None
    if l1 == []:
        return True
    if l2 == []:
        return False
    a, b = l1[0], l2[0]
    if isinstance(a, list) and isinstance(b, list):
        v = compare(a, b)
        if v is None:
            return compare(l1[1:], l2[1:])
        return v
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        if a > b:
            return False
        return compare(l1[1:], l2[1:])
    # un entier face à une liste : l'entier devient une liste à un élément
    if isinstance(a, int):
        l1 = [[a]] + l1[1:]
    if isinstance(b, int):
        l2 = [[b]] + l2[1:]
    return compare(l1, l2)


def partie1(paires):
    return sum(i + 1 for i, (l1, l2) in enumerate(paires) if compare(l1, l2))


def partie2(paires):
    paquets = [[[2]], [[6]]]
    for l1, l2 in paires:
        paquets += [l1, l2]

    def cmp(l1, l2):
        return {True: -1, False: 1, None: 0}[compare(l1, l2)]

    paquets.sort(key=cmp_to_key(cmp))
    i2 = paquets.index([[2]])
    i6 = paquets.index([[6]])
    return (i2 + 1) * (i6 + 1)


paires = lire_donnees()
print('Partie 1 :', partie1(paires))
print('Partie 2 :', partie2(paires))
