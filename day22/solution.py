"""Advent of Code 2022, jour 22.

La carte est gardée telle quelle, avec pour chaque ligne et chaque colonne
les bornes des cases présentes (`xlim`, `ylim`). On suit les instructions
pas à pas ; un mur arrête le déplacement en cours.
Partie 1 : sortir d'un côté fait réapparaître à l'autre borne.
Partie 2 : la carte est le patron d'un cube de côté 50. La case est
rattachée à une face et chaque sortie de face est traitée par un cas écrit
à la main (nouvelle position et nouvelle direction). Ces recollements ne
valent que pour la forme du patron de l'entrée :
       12
       3
      45
      6
"""

COTE = 50
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # droite, bas, gauche, haut


def lire_donnees(nom_fichier='input.txt'):
    lignes = open(nom_fichier).read().split('\n')
    while lignes[-1] == '':
        lignes.pop()
    instructions = lignes[-1]
    carte = lignes[:-2]

    w = max(len(ligne) for ligne in carte)
    h = len(carte)
    xlim = []
    for ligne in carte:
        presents = [i for i, c in enumerate(ligne) if c != ' ']
        xlim.append((min(presents), max(presents)))
    ylim = []
    for i in range(w):
        presents = [j for j, ligne in enumerate(carte)
                    if i < len(ligne) and ligne[i] != ' ']
        ylim.append((min(presents), max(presents)))

    # instructions : nombres de pas et rotations 'R' / 'L'
    mouvements = []
    i = 0
    while i < len(instructions):
        j = i
        while j < len(instructions) and instructions[j] not in 'RL':
            j += 1
        mouvements.append(int(instructions[i:j]))
        if j < len(instructions):
            mouvements.append(instructions[j])
        i = j + 1
    return carte, xlim, ylim, mouvements


def recoller_cube(x, y, x2, y2, f, xlim, ylim):
    """Position et direction après la sortie de la face par (x2, y2)."""
    sz = COTE
    if y < sz:
        face = x // sz
    elif y < 2 * sz:
        face = 3
    elif y < 3 * sz:
        face = 4 + x // sz
    else:
        face = 6

    if face == 1:
        if y2 < ylim[x][0]:   # haut de 1 -> gauche de 6
            return 0, 3 * sz + x2 % sz, 0
        return 0, 2 * sz + (sz - y2 % sz - 1), 0  # gauche de 1 -> gauche de 4
    if face == 2:
        if y2 < ylim[x][0]:   # haut de 2 -> bas de 6
            return x2 % sz, 4 * sz - 1, 3
        if y2 > ylim[x][1]:   # bas de 2 -> droite de 3
            return 2 * sz - 1, sz + x2 % sz, 2
        # droite de 2 -> droite de 5
        return 2 * sz - 1, 2 * sz + (sz - y2 % sz - 1), 2
    if face == 3:
        if x2 < xlim[y][0]:   # gauche de 3 -> haut de 4
            return y2 % sz, 2 * sz, 1
        return 2 * sz + y2 % sz, sz - 1, 3  # droite de 3 -> bas de 2
    if face == 4:
        if x2 < xlim[y][0]:   # gauche de 4 -> gauche de 1
            return sz, sz - y2 % sz - 1, 0
        return sz, sz + x2 % sz, 0  # haut de 4 -> gauche de 3
    if face == 5:
        if x2 > xlim[y][1]:   # droite de 5 -> droite de 2
            return 3 * sz - 1, sz - y2 % sz - 1, 2
        return sz - 1, x2 % sz + 3 * sz, 2  # bas de 5 -> droite de 6
    # face 6
    if x2 > xlim[y][1]:       # droite de 6 -> bas de 5
        return sz + y2 % sz, 3 * sz - 1, 3
    if x2 < xlim[y][0]:       # gauche de 6 -> haut de 1
        return sz + y2 % sz, 0, 1
    return 2 * sz + x2 % sz, 0, 1  # bas de 6 -> haut de 2


def marcher(carte, xlim, ylim, mouvements, cube):
    x, y, f = xlim[0][0], 0, 0
    for mouvement in mouvements:
        if mouvement == 'R':
            f = (f + 1) % 4
        elif mouvement == 'L':
            f = (f - 1) % 4
        else:
            for _ in range(mouvement):
                dx, dy = DIRECTIONS[f]
                x2, y2, f2 = x + dx, y + dy, f
                sorti = not (xlim[y][0] <= x2 <= xlim[y][1]
                             and ylim[x][0] <= y2 <= ylim[x][1])
                if sorti and not cube:
                    if x2 < xlim[y][0]:
                        x2 = xlim[y][1]
                    if x2 > xlim[y][1]:
                        x2 = xlim[y][0]
                    if y2 < ylim[x][0]:
                        y2 = ylim[x][1]
                    if y2 > ylim[x][1]:
                        y2 = ylim[x][0]
                elif sorti:
                    x2, y2, f2 = recoller_cube(x, y, x2, y2, f, xlim, ylim)
                if carte[y2][x2] == '#':
                    break
                x, y, f = x2, y2, f2
    return 1000 * (y + 1) + 4 * (x + 1) + f


carte, xlim, ylim, mouvements = lire_donnees()
print('Partie 1 :', marcher(carte, xlim, ylim, mouvements, False))
print('Partie 2 :', marcher(carte, xlim, ylim, mouvements, True))
