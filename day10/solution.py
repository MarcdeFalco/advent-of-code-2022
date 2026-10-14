"""Advent of Code 2022, jour 10.

Petit interprète : `noop` dure un cycle, `addx` deux cycles, le registre x
n'étant modifié qu'à la fin du second. Partie 1 : somme des cycle * x aux
cycles 20, 60, 100, ... (cycle % 40 == 20). Partie 2 : à chaque cycle, le
pixel courant de l'écran 40 x 6 est allumé si x est à distance au plus 1 de
sa colonne ; on affiche l'image obtenue.
"""


def executer(instructions):
    cycle = 1
    x = 1
    score = 0
    ecran = [[' '] * 40 for _ in range(6)]

    def dessiner():
        colonne = (cycle - 1) % 40
        if x - 1 <= colonne < x - 1 + 3:
            ecran[(cycle - 1) // 40][colonne] = '#'

    for instruction in instructions:
        if cycle % 40 == 20:
            score += cycle * x
        mots = instruction.split()
        if mots[0] == 'noop':
            dessiner()
            cycle += 1
        elif mots[0] == 'addx':
            dessiner()
            cycle += 1
            if cycle % 40 == 20:
                score += cycle * x
            dessiner()
            cycle += 1
            x += int(mots[1])
    return score, '\n'.join(''.join(ligne) for ligne in ecran)


instructions = open('input.txt').read().strip().split('\n')
score, image = executer(instructions)
print('Partie 1 :', score)
print('Partie 2 :')
print(image)
