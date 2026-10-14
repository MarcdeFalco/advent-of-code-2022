"""Advent of Code 2022, jour 9 : animation d'une corde de 100 nœuds.

Produit une image PNG par pas (out0000000.png, ...) : la corde en rouge
(plus clair vers la queue), les positions passées de la queue en gris.
Nécessite PIL (Pillow) ; assembler ensuite les images en GIF ou en vidéo.
"""
from PIL import Image

from solution import DEPLACEMENTS, deplacer_corde, lire_donnees

LONGUEUR = 100

corde = [(0, 0)] * LONGUEUR
cordes = [list(corde)]
for direction, k in lire_donnees():
    for _ in range(k):
        deplacer_corde(corde, DEPLACEMENTS[direction])
        cordes.append(list(corde))

xs = [x for c in cordes for x, _ in c]
ys = [y for c in cordes for _, y in c]
xmin, ymin = min(xs), min(ys)
w = max(xs) - xmin + 1
h = max(ys) - ymin + 1
w, h = w + w % 2, h + h % 2  # dimensions paires pour l'encodage vidéo

traces = []
for i, c in enumerate(cordes):
    im = Image.new('RGB', (w, h), (255, 255, 255))
    for x, y in traces:
        im.putpixel((x - xmin, y - ymin), (128, 128, 128))
    for j, (x, y) in enumerate(c):
        im.putpixel((x - xmin, y - ymin), (255, 2 * j, 2 * j))
    traces.append(c[-1])
    im.save('out%07d.png' % i)
