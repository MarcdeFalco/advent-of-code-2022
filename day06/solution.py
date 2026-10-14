"""Advent of Code 2022, jour 6.

On fait glisser une fenêtre de taille k sur le signal et l'on s'arrête à la
première fenêtre dont les caractères sont tous distincts, testé par
len(set(fenetre)) == k : k = 4 pour la partie 1, k = 14 pour la partie 2.
"""


def premier_marqueur(signal, k):
    """Nombre de caractères lus à la fin de la première fenêtre valide."""
    for i in range(len(signal) - k + 1):
        if len(set(signal[i:i + k])) == k:
            return i + k


signal = open('input.txt').read().strip()
print('Partie 1 :', premier_marqueur(signal, 4))
print('Partie 2 :', premier_marqueur(signal, 14))
