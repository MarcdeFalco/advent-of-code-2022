"""Advent of Code 2022, jour 11.

Simulation des échanges : les objets de chaque singe sont dans une file
(deque). En partie 2 les valeurs explosent ; comme seuls comptent les tests
de divisibilité par les diviseurs d_i, on réduit chaque valeur modulo
N = ppcm(d_i) (addition et multiplication sont compatibles avec la
réduction modulo N). La réduction est aussi faite en partie 1, après la
division par 3.
"""
from collections import deque


class Singe:
    def __init__(self, bloc):
        lignes = bloc.split('\n')
        self.numero = int(lignes[0].split()[1][:-1])
        objets = lignes[1][lignes[1].find(':') + 1:].split(', ')
        self.objets = [int(objet) for objet in objets]
        mots = lignes[2].split()
        self.operation = (mots[-2], mots[-1])  # ('+' ou '*', nombre ou 'old')
        self.diviseur = int(lignes[3].split()[-1])
        self.si_vrai = int(lignes[4].split()[-1])
        self.si_faux = int(lignes[5].split()[-1])


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lire_donnees(nom_fichier='input.txt'):
    return open(nom_fichier).read().strip().split('\n\n')


def niveau_activite(blocs, nb_tours, division_par_3):
    singes = [Singe(bloc) for bloc in blocs]
    files = [deque(singe.objets) for singe in singes]

    N = 1  # ppcm des diviseurs
    for singe in singes:
        N *= singe.diviseur // pgcd(N, singe.diviseur)

    inspections = [0] * len(singes)
    for _ in range(nb_tours):
        for singe in singes:
            file = files[singe.numero]
            while len(file) > 0:
                inspections[singe.numero] += 1
                valeur = file.popleft()
                operateur, argument = singe.operation
                argument = valeur if argument == 'old' else int(argument)
                if operateur == '+':
                    valeur = argument + valeur
                else:
                    valeur = argument * valeur
                if division_par_3:
                    valeur //= 3
                valeur %= N
                if valeur % singe.diviseur == 0:
                    files[singe.si_vrai].append(valeur)
                else:
                    files[singe.si_faux].append(valeur)

    inspections.sort()
    return inspections[-1] * inspections[-2]


def partie1(blocs):
    return niveau_activite(blocs, 20, True)


def partie2(blocs):
    return niveau_activite(blocs, 10000, False)


blocs = lire_donnees()
print('Partie 1 :', partie1(blocs))
print('Partie 2 :', partie2(blocs))
