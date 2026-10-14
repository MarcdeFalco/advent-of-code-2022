"""Advent of Code 2022, jour 17.

La pile est une liste de lignes de 7 cases. Chaque pièce est décrite colonne
par colonne par un intervalle de hauteurs [bas, haut[ ; on alterne poussée
latérale et chute tant que la position reste valide.
Partie 1 : simulation directe de 2022 pièces.
Partie 2 (10^12 pièces) : on repère un cycle grâce à une signature (numéro
de pièce modulo 5, position dans les jets, profil du sommet relatif à la
hauteur maximale) : quand une signature revient, on connaît la longueur du
cycle et le gain de hauteur par cycle, et il suffit de simuler le début.
Les constantes du cycle sont détectées par le programme.
"""
from itertools import cycle

# pour chaque pièce : bas et haut (exclu) de chaque colonne
PIECES = [
    ((0, 0, 0, 0), (1, 1, 1, 1)),  # barre horizontale
    ((1, 0, 1), (2, 3, 2)),        # croix
    ((0, 0, 0), (1, 1, 3)),        # L à l'envers
    ((0,), (4,)),                  # barre verticale
    ((0, 0), (2, 2)),              # carré
]

LARGEUR = 7


def simuler(jets, nb_pieces, detecter_cycle=False):
    """Renvoie la liste des hauteurs après 0, 1, 2, ... pièces ; avec
    `detecter_cycle`, s'arrête au premier cycle et renvoie aussi
    (debut, longueur, gain de hauteur)."""
    pile = []          # pile[y][x] vaut 1 si la case est occupée
    profil = [0] * LARGEUR  # hauteur de chaque colonne
    hauteur = 0
    nb_jets = 0
    vus = {}
    hauteurs = []
    flux = cycle(jets)

    for numero, (bas, haut) in enumerate(cycle(PIECES)):
        signature = (numero % 5, nb_jets % len(jets),
                     tuple(hauteur - p for p in profil))
        if detecter_cycle and signature in vus:
            debut, hauteur_debut = vus[signature]
            return hauteurs, (debut, numero - debut, hauteur - hauteur_debut)
        vus[signature] = (numero, hauteur)
        hauteurs.append(hauteur)
        if numero == nb_pieces:
            return hauteurs, None

        w = len(bas)
        h = max(haut)
        x, y = 2, hauteur + 3
        pile += [[0] * LARGEUR for _ in range(3 + h)]

        def est_valide(dx, dy):
            for cx in range(w):
                for cy in range(bas[cx], haut[cx]):
                    x1, y1 = x + cx + dx, y + cy + dy
                    if x1 < 0 or y1 < 0 or x1 >= LARGEUR:
                        return False
                    if pile[y1][x1] != 0:
                        return False
            return True

        for jet in flux:
            nb_jets += 1
            dx = -1 if jet == '<' else 1
            if est_valide(dx, 0):
                x += dx
            if est_valide(0, -1):
                y -= 1
            else:
                break

        for cx in range(w):
            for cy in range(bas[cx], haut[cx]):
                profil[x + cx] = max(profil[x + cx], y + cy + 1)
                pile[y + cy][x + cx] = 1
        hauteur = max(hauteur, y + h)
        del pile[hauteur:]  # on retire les lignes vides du dessus


def partie1(jets):
    hauteurs, _ = simuler(jets, 2022)
    return hauteurs[2022]


def partie2(jets, n=1000000000000):
    hauteurs, (debut, longueur, gain) = simuler(jets, n, detecter_cycle=True)
    nb_cycles, reste = divmod(n - debut, longueur)
    return hauteurs[debut + reste] + nb_cycles * gain


jets = open('input.txt').read().strip()
print('Partie 1 :', partie1(jets))
print('Partie 2 :', partie2(jets))
