"""Advent of Code 2022, jour 24.

Les blizzards horizontaux reviennent à leur place après w - 2 instants, les
verticaux après h - 2 : on précalcule les grilles occupées pour chaque
instant de chaque période (`horiz`, `vert`). Un parcours en largeur explore
l'espace-temps (position, instant), où attendre est un coup comme un autre ;
un état est repéré par (x, y, t mod (w - 2), t mod (h - 2)).
Partie 1 : un aller. Partie 2 : aller, retour, aller, chaque parcours
partant de l'instant d'arrivée du précédent.
"""
from collections import deque

SENS = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}


def lire_donnees(nom_fichier='input.txt'):
    lignes = open(nom_fichier).read().strip().split('\n')
    h, w = len(lignes), len(lignes[0])
    blizzards = [(x, y, c) for y, ligne in enumerate(lignes)
                 for x, c in enumerate(ligne) if c in SENS]

    def grilles(symboles, periode):
        resultat = []
        for t in range(periode):
            occupe = [[False] * w for _ in range(h)]
            for xb, yb, c in blizzards:
                if c not in symboles:
                    continue
                dx, dy = SENS[c]
                # les blizzards circulent dans l'intérieur [1, w-2] x [1, h-2]
                xb = 1 + (xb - 1 + t * dx) % (w - 2)
                yb = 1 + (yb - 1 + t * dy) % (h - 2)
                occupe[yb][xb] = True
            resultat.append(occupe)
        return resultat

    return w, h, grilles('<>', w - 2), grilles('^v', h - 2)


def traversee(w, h, horiz, vert, depart, arrivee, t):
    """Instant d'arrivée en partant de `depart` à l'instant t."""
    vus = set()

    def libre(x, y, t):
        if y == 0 or y == h - 1:  # case de départ ou d'arrivée
            return True
        if (x, y, t % (w - 2), t % (h - 2)) in vus:
            return False
        return not (horiz[t % (w - 2)][y][x] or vert[t % (h - 2)][y][x])

    file = deque([(depart[0], depart[1], t)])
    while len(file) != 0:
        x, y, t = file.popleft()
        if (x, y) == arrivee:
            return t
        if libre(x, y, t + 1):  # attendre sur place
            vus.add((x, y, (t + 1) % (w - 2), (t + 1) % (h - 2)))
            file.append((x, y, t + 1))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x2, y2 = x + dx, y + dy
            if (((x2, y2) == arrivee or (1 <= x2 < w - 1 and 1 <= y2 < h - 1))
                    and libre(x2, y2, t + 1)):
                vus.add((x2, y2, (t + 1) % (w - 2), (t + 1) % (h - 2)))
                file.append((x2, y2, t + 1))


w, h, horiz, vert = lire_donnees()
depart, arrivee = (1, 0), (w - 2, h - 1)
t1 = traversee(w, h, horiz, vert, depart, arrivee, 0)
t2 = traversee(w, h, horiz, vert, arrivee, depart, t1)
t3 = traversee(w, h, horiz, vert, depart, arrivee, t2)
print('Partie 1 :', t1)
print('Partie 2 :', t3)
