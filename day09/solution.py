"""Advent of Code 2022, jour 9.

La corde est une liste de positions ; à chaque pas la tête avance d'une case
puis chaque nœud suit le précédent (`suivre`). Les positions de la queue
sont accumulées dans un ensemble. Seule la longueur change : 2 nœuds pour la
partie 1, 10 pour la partie 2.
"""

DEPLACEMENTS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def suivre(meneur, suiveur):
    """Nouvelle position de `suiveur` après le déplacement de `meneur`."""
    x, y = meneur
    xs, ys = suiveur
    vx, vy = x - xs, y - ys
    # diviser par max(1, |v|) donne le signe de l'écart sur chaque axe :
    # le suiveur avance d'au plus une case par axe, en ligne ou en diagonale
    dx, dy = max(1, abs(vx)), max(1, abs(vy))
    if dx > 1 or dy > 1:
        return xs + vx // dx, ys + vy // dy
    return xs, ys


def deplacer_corde(corde, delta):
    x, y = corde[0]
    dx, dy = delta
    corde[0] = (x + dx, y + dy)
    for i in range(1, len(corde)):
        corde[i] = suivre(corde[i - 1], corde[i])


def lire_donnees(nom_fichier='input.txt'):
    mouvements = []
    for ligne in open(nom_fichier).read().strip().split('\n'):
        direction, k = ligne.split()
        mouvements.append((direction, int(k)))
    return mouvements


def positions_queue(mouvements, longueur):
    corde = [(0, 0)] * longueur
    queues = set()
    for direction, k in mouvements:
        for _ in range(k):
            deplacer_corde(corde, DEPLACEMENTS[direction])
            queues.add(corde[-1])
    return len(queues)


if __name__ == '__main__':
    mouvements = lire_donnees()
    print('Partie 1 :', positions_queue(mouvements, 2))
    print('Partie 2 :', positions_queue(mouvements, 10))
