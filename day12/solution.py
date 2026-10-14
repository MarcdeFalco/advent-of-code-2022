"""Advent of Code 2022, jour 12.

Parcours en largeur (file deque) sur la grille, où l'on peut monter d'au
plus un niveau à chaque pas ; le parcours s'arrête dès qu'il atteint
l'arrivée E. Partie 1 : depuis S. Partie 2 : le parcours est relancé depuis
chaque case de hauteur 'a' et l'on garde la plus petite distance.
"""
from collections import deque


def lire_donnees(nom_fichier='input.txt'):
    lignes = open(nom_fichier).read().strip().split('\n')
    grille = [list(ligne) for ligne in lignes]
    depart, arrivee = None, None
    departs_possibles = []
    for x in range(len(grille)):
        for y in range(len(grille[0])):
            if grille[x][y] == 'S':
                depart = (x, y)
                departs_possibles.append((x, y))
            elif grille[x][y] == 'a':
                departs_possibles.append((x, y))
            elif grille[x][y] == 'E':
                arrivee = (x, y)
    # S est à la hauteur 'a', E à la hauteur 'z'
    for x, y in departs_possibles:
        grille[x][y] = 'a'
    grille[arrivee[0]][arrivee[1]] = 'z'
    return grille, depart, arrivee, departs_possibles


def distance(grille, depart, arrivee):
    """Longueur du plus court chemin, ou None si l'arrivée est inaccessible."""
    w, h = len(grille), len(grille[0])
    dist = [[None] * h for _ in range(w)]
    x0, y0 = depart
    dist[x0][y0] = 0
    file = deque([depart])
    while len(file) > 0:
        x, y = file.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xv, yv = x + dx, y + dy
            if (0 <= xv < w and 0 <= yv < h and dist[xv][yv] is None
                    and ord(grille[xv][yv]) - ord(grille[x][y]) <= 1):
                dist[xv][yv] = dist[x][y] + 1
                if (xv, yv) == arrivee:
                    return dist[xv][yv]
                file.append((xv, yv))
    return None


def partie1(grille, depart, arrivee):
    return distance(grille, depart, arrivee)


def partie2(grille, arrivee, departs_possibles):
    distances = [distance(grille, d, arrivee) for d in departs_possibles]
    return min(d for d in distances if d is not None)


grille, depart, arrivee, departs_possibles = lire_donnees()
print('Partie 1 :', partie1(grille, depart, arrivee))
print('Partie 2 :', partie2(grille, arrivee, departs_possibles))
