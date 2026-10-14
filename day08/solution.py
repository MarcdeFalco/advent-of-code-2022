"""Advent of Code 2022, jour 8.

Pour chaque arbre, on avance dans les quatre directions jusqu'au bord ou
jusqu'au premier arbre au moins aussi haut. Une seule boucle donne les deux
parties : l'arbre est visible s'il atteint le bord dans une direction
(partie 1) et son score est le produit des distances parcourues
(partie 2). Coût O(n^3) pour une grille n x n.
"""

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def lire_donnees(nom_fichier='input.txt'):
    lignes = open(nom_fichier).read().strip().split('\n')
    return [list(map(int, ligne)) for ligne in lignes]


def resoudre(grille):
    w, h = len(grille), len(grille[0])
    nb_visibles = 0
    meilleur_score = 0
    for x in range(w):
        for y in range(h):
            hauteur = grille[x][y]
            visible_quelque_part = False
            score = 1
            for dx, dy in DIRECTIONS:
                visible = True
                distance = 0
                px, py = x + dx, y + dy
                while 0 <= px < w and 0 <= py < h:
                    distance += 1
                    if grille[px][py] >= hauteur:
                        visible = False
                        break
                    px, py = px + dx, py + dy
                visible_quelque_part = visible_quelque_part or visible
                score *= distance
            if visible_quelque_part:
                nb_visibles += 1
            meilleur_score = max(meilleur_score, score)
    return nb_visibles, meilleur_score


nb_visibles, meilleur_score = resoudre(lire_donnees())
print('Partie 1 :', nb_visibles)
print('Partie 2 :', meilleur_score)
