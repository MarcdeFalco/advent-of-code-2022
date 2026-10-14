"""Advent of Code 2022, jour 15.

La zone couverte par un capteur est une boule pour la distance de
Manhattan ; sa trace sur la ligne y est l'intervalle [xs - dx, xs + dx] avec
dx = d - |ys - y|. Partie 1 : les abscisses couvertes de la ligne 2000000
sont accumulées dans un ensemble. Partie 2 : pour chaque ligne, on part de
[0, 4000000] et l'on soustrait les intervalles des capteurs ; la ligne où il
reste quelque chose contient la case cherchée (balayage ligne par ligne,
lent en Python : plusieurs minutes).
La partie 1 exclut toutes les balises situées sur la ligne, et la partie 2
garde un capteur qui ne couvre qu'une seule case de la ligne (seul `dx < 0`
est écarté).
"""

LIGNE = 2000000
TAILLE = 4000000


def lire_donnees(nom_fichier='input.txt'):
    capteurs = []
    for ligne in open(nom_fichier).read().strip().split('\n'):
        mots = ligne.split()
        xs = int(mots[2][2:-1])
        ys = int(mots[3][2:-1])
        xb = int(mots[-2][2:-1])
        yb = int(mots[-1][2:])
        capteurs.append((xs, ys, xb, yb))
    return capteurs


def partie1(capteurs, y=LIGNE):
    balises = {(xb, yb) for _, _, xb, yb in capteurs}
    couvertes = set()
    for xs, ys, xb, yb in capteurs:
        d = abs(xs - xb) + abs(ys - yb)
        dx = d - abs(ys - y)
        for x in range(xs - dx, xs + dx + 1):
            if (x, y) not in balises:
                couvertes.add(x)
    return len(couvertes)


def soustraire(intervalles, a, b):
    """Retire [a, b] de chaque intervalle [x0, x1] de la liste."""
    resultat = []
    for x0, x1 in intervalles:
        if b < x0 or x1 < a:  # disjoints
            resultat.append((x0, x1))
        else:
            if x0 < a:
                resultat.append((x0, a - 1))
            if x1 > b:
                resultat.append((b + 1, x1))
    return resultat


def partie2(capteurs, taille=TAILLE):
    for y in range(taille + 1):
        libres = [(0, taille)]
        for xs, ys, xb, yb in capteurs:
            d = abs(xs - xb) + abs(ys - yb)
            dx = d - abs(ys - y)
            if dx < 0:  # le capteur ne touche pas cette ligne
                continue
            libres = soustraire(libres, xs - dx, xs + dx)
            if len(libres) == 0:
                break
        if len(libres) != 0:
            x = libres[0][0]
            return x * 4000000 + y


capteurs = lire_donnees()
print('Partie 1 :', partie1(capteurs))
print('Partie 2 :', partie2(capteurs))
