"""Advent of Code 2022, jour 18.

Partie 1 : pour chaque cube, on compte les six faces dont le voisin n'est
pas dans l'ensemble des cubes.
Partie 2 : chaque case vide de la boîte englobante lance un parcours en
largeur ; s'il ne sort pas de la boîte, la composante est une poche d'air
et elle est ajoutée aux cubes, ce qui supprime ses faces du décompte. On
recompte alors comme en partie 1.
"""
from collections import deque
from itertools import product

FACES = list(product(range(3), [-1, 1]))  # (axe, sens)


def voisin(cube, axe, sens):
    c = list(cube)
    c[axe] += sens
    return tuple(c)


def lire_donnees(nom_fichier='input.txt'):
    return [tuple(map(int, ligne.split(',')))
            for ligne in open(nom_fichier).read().strip().split('\n')]


def surface(cubes, pleins):
    return sum(1 for cube in cubes for axe, sens in FACES
               if voisin(cube, axe, sens) not in pleins)


def partie1(cubes):
    return surface(cubes, set(cubes))


def partie2(cubes):
    pleins = set(cubes)
    mini = [min(c[i] for c in cubes) for i in range(3)]
    maxi = [max(c[i] for c in cubes) for i in range(3)]

    def dans_boite(c):
        return all(mini[i] <= c[i] <= maxi[i] for i in range(3))

    for case in product(*(range(mini[i], maxi[i] + 1) for i in range(3))):
        if case in pleins:
            continue
        piegee = True
        a_visiter = deque([case])
        vues = {case}
        while len(a_visiter) > 0:
            c = a_visiter.popleft()
            if not dans_boite(c):  # on est sorti : pas une poche d'air
                piegee = False
                break
            for axe, sens in FACES:
                c2 = voisin(c, axe, sens)
                if c2 not in pleins and c2 not in vues:
                    vues.add(c2)
                    a_visiter.append(c2)
        if piegee:  # on bouche la poche d'air
            pleins |= vues

    return surface(cubes, pleins)


cubes = lire_donnees()
print('Partie 1 :', partie1(cubes))
print('Partie 2 :', partie2(cubes))
