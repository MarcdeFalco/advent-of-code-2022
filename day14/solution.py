"""Advent of Code 2022, jour 14.

Les segments de roche sont tracés dans une grille creuse (defaultdict
indexé par couples). Chaque grain part de (500, 0) et descend en testant les
cases dessous, en bas à gauche puis en bas à droite. Partie 1 : on s'arrête
au premier grain qui passe sous la roche la plus basse. Partie 2 : un sol
infini est ajouté à `bas + 2` et l'on s'arrête quand la source est bouchée.
"""
from collections import defaultdict

SOURCE = (500, 0)


def lire_donnees(nom_fichier='input.txt'):
    occupe = defaultdict(bool)
    bas = 0
    for chemin in open(nom_fichier).read().strip().split('\n'):
        points = [tuple(map(int, point.split(',')))
                  for point in chemin.split(' -> ')]
        bas = max(bas, max(y for _, y in points))
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    occupe[x1, y] = True
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    occupe[x, y1] = True
    return occupe, bas


def faire_couler(occupe, bas, avec_sol, apres_grain=None):
    """Nombre de grains au repos ; `occupe` est modifié en place.
    `apres_grain(n)` est appelé après chaque grain (pour la visualisation)."""

    def plein(x, y):
        if avec_sol and y == bas + 2:
            return True
        return occupe[x, y]

    nb_grains = 0
    while True:
        x, y = SOURCE
        au_repos = False
        while not au_repos and (avec_sol or y <= bas):
            if not plein(x, y + 1):
                y += 1
            elif not plein(x - 1, y + 1):
                x, y = x - 1, y + 1
            elif not plein(x + 1, y + 1):
                x, y = x + 1, y + 1
            else:
                au_repos = True
        occupe[x, y] = True
        if not au_repos:  # le grain tombe dans le vide (partie 1)
            return nb_grains
        nb_grains += 1
        if apres_grain is not None:
            apres_grain(nb_grains)
        if (x, y) == SOURCE:  # la source est bouchée (partie 2)
            return nb_grains


def partie1(nom_fichier='input.txt'):
    occupe, bas = lire_donnees(nom_fichier)
    return faire_couler(occupe, bas, False)


def partie2(nom_fichier='input.txt'):
    occupe, bas = lire_donnees(nom_fichier)
    return faire_couler(occupe, bas, True)


if __name__ == '__main__':
    print('Partie 1 :', partie1())
    print('Partie 2 :', partie2())
