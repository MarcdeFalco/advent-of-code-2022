# Advent of Code 2022, jour 21, partie 1 : curiosité.
# Chaque ligne « nom: expression » devient l'affectation Python
# « nom = expression », exécutée avec exec. On parcourt les lignes en boucle
# (itertools.cycle) : une affectation qui utilise un nom pas encore défini
# lève NameError et sera retentée au passage suivant. On s'arrête dès que
# `root` est défini. La division est celle des flottants.
from itertools import cycle

for ligne in cycle(open('input.txt').readlines()):
    try:
        exec(ligne.replace(':', '='))
        print(int(root))
        break
    except NameError:
        pass
