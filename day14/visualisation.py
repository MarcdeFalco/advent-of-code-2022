"""Advent of Code 2022, jour 14 : images de la partie 2.

Enregistre une image tous les 100 grains (sable000000.png, ...) : roche en
noir, sable en gris, sol en noir. Nécessite PIL (Pillow).
"""
from PIL import Image

from solution import lire_donnees, faire_couler

occupe, bas = lire_donnees()
roche = set(p for p in occupe if occupe[p])
# en partie 2 le tas forme un triangle de demi-largeur bas + 2 sous la source
xmin, xmax = 500 - bas - 3, 500 + bas + 3
w = xmax - xmin + 1


def enregistrer(nb_grains):
    if nb_grains % 100 != 0:
        return
    im = Image.new('L', (w, bas + 3), 255)
    for (x, y), plein in list(occupe.items()):
        if plein and xmin <= x <= xmax:
            im.putpixel((x - xmin, y), 0 if (x, y) in roche else 128)
    for x in range(w):
        im.putpixel((x, bas + 2), 0)
    im.save('sable%06d.png' % (nb_grains // 100))


faire_couler(occupe, bas, True, enregistrer)
