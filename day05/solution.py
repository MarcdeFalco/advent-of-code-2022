"""Advent of Code 2022, jour 5.

L'état initial est lu ligne par ligne (une caisse tous les quatre
caractères), puis chaque pile est retournée pour avoir le sommet en fin de
liste : les piles sont des listes Python. Partie 1 : les caisses sont
déplacées une à une (append/pop) ; partie 2 : un bloc est déplacé d'un coup
avec des tranches.
"""


def lire_donnees(nom_fichier='input.txt'):
    fichier = open(nom_fichier)
    piles = None
    for ligne in fichier:
        if ligne == '\n':
            break
        if piles is None:
            npiles = (len(ligne) + 1) // 4
            piles = [[] for _ in range(npiles)]
        if ligne[:3] == ' 1 ':  # ligne des numéros de piles
            continue
        for i in range(npiles):
            case = ligne[4 * i:4 * i + 4]
            if case[0] != ' ':
                piles[i].append(case[1])
    for pile in piles:
        pile.reverse()

    instructions = []
    for ligne in fichier:
        mots = ligne.split()
        nombre, depart, arrivee = int(mots[1]), int(mots[3]), int(mots[5])
        instructions.append((nombre, depart - 1, arrivee - 1))
    return piles, instructions


def sommets(piles):
    return ''.join(pile[-1] for pile in piles)


def partie1(piles, instructions):
    piles = [list(pile) for pile in piles]
    for nombre, depart, arrivee in instructions:
        for _ in range(nombre):
            piles[arrivee].append(piles[depart].pop())
    return sommets(piles)


def partie2(piles, instructions):
    piles = [list(pile) for pile in piles]
    for nombre, depart, arrivee in instructions:
        bloc = piles[depart][-nombre:]
        piles[depart] = piles[depart][:-nombre]
        piles[arrivee] += bloc
    return sommets(piles)


piles, instructions = lire_donnees()
print('Partie 1 :', partie1(piles, instructions))
print('Partie 2 :', partie2(piles, instructions))
