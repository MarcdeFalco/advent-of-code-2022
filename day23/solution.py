"""Advent of Code 2022, jour 23.

Automate à deux phases : chaque elfe entouré d'au moins un voisin propose
une case (l'ordre des directions N, S, W, E tourne avec le numéro du tour),
un compteur de propositions est rempli, puis seuls ceux dont la case est
proposée une seule fois se déplacent.
Partie 1 : cases vides du rectangle englobant après 10 tours.
Partie 2 : numéro du premier tour où personne ne bouge.
"""
from collections import defaultdict
from itertools import product

ORDRE = 'NSWE'


def lire_donnees(nom_fichier='input.txt'):
    elfes = []
    for y, ligne in enumerate(open(nom_fichier).read().strip().split('\n')):
        for x, c in enumerate(ligne):
            if c == '#':
                elfes.append((x, y))
    return elfes


def tour(elfes, r):
    """Positions après le tour numéro r (à partir de 0)."""
    occupe = defaultdict(bool)
    for x, y in elfes:
        occupe[x, y] = True
    propositions = []
    nb_propositions = defaultdict(int)
    for x, y in elfes:
        voisins = [(x + dx, y + dy) for dx, dy in product([-1, 0, 1], repeat=2)
                   if (dx, dy) != (0, 0) and occupe[x + dx, y + dy]]
        if voisins == []:  # personne autour : l'elfe ne bouge pas
            propositions.append((x, y))
            continue
        a_propose = False
        for k in range(4):
            d = ORDRE[(r + k) % 4]
            # les trois cases du côté d, celle du milieu étant la destination
            cotes = {'N': [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1)],
                     'S': [(x - 1, y + 1), (x, y + 1), (x + 1, y + 1)],
                     'W': [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1)],
                     'E': [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]}[d]
            if all(c not in voisins for c in cotes):
                a_propose = True
                propositions.append(cotes[1])
                break
        if not a_propose:
            propositions.append((x, y))
        nb_propositions[propositions[-1]] += 1

    nouveaux = []
    for (x, y), case in zip(elfes, propositions):
        if nb_propositions[case] == 1:
            nouveaux.append(case)
        else:
            nouveaux.append((x, y))
    return nouveaux


def partie1(elfes):
    for r in range(10):
        elfes = tour(elfes, r)
    xs = [x for x, _ in elfes]
    ys = [y for _, y in elfes]
    w = max(xs) - min(xs) + 1
    h = max(ys) - min(ys) + 1
    return w * h - len(elfes)


def partie2(elfes):
    r = 0
    while True:
        nouveaux = tour(elfes, r)
        if nouveaux == elfes:
            return r + 1
        elfes = nouveaux
        r += 1


elfes = lire_donnees()
print('Partie 1 :', partie1(elfes))
print('Partie 2 :', partie2(elfes))
