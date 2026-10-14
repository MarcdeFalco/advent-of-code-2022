"""Advent of Code 2022, jour 20.

Les valeurs pouvant se répéter, on manipule les indices d'origine dans une
deque : pour déplacer l'élément k, on le cherche (index, O(n)), on fait
tourner la file pour l'amener en fin, on le retire, on tourne de
valeur % (n - 1) (la liste privée de l'élément a n - 1 places) et on le
remet. Un tour de mélange coûte O(n^2).
Partie 1 : un tour, sans clé. Partie 2 : valeurs multipliées par la clé,
dix tours.
deque.rotate n'accepte pas d'argument nommé (n=...) dans les versions
récentes de Python.
"""
from collections import deque

CLE = 811589153


def melanger(valeurs, cle, nb_tours):
    orig = [v * cle for v in valeurs]
    n = len(orig)
    file = deque(range(n), maxlen=n)
    for _ in range(nb_tours):
        for k in range(n):
            d = file.index(k)
            file.rotate(-d - 1)   # k passe en dernière position
            file.pop()
            file.rotate(-(orig[k] % (n - 1)))
            file.append(k)
    i = file.index(orig.index(0))
    return sum(orig[file[(i + decalage) % n]]
               for decalage in (1000, 2000, 3000))


valeurs = list(map(int, open('input.txt').read().strip().split('\n')))
print('Partie 1 :', melanger(valeurs, 1, 1))
print('Partie 2 :', melanger(valeurs, CLE, 10))
