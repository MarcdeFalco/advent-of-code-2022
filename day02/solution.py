"""Advent of Code 2022, jour 2.

Version naïve qui garde les caractères : les couples (adversaire, joueur)
gagnants et perdants sont listés explicitement. En partie 2, la seconde
lettre donne l'issue voulue et l'on cherche le coup qui la produit.
(La version C et `solution_une_ligne.py` codent les coups par 0, 1, 2 et
raisonnent modulo 3, voir README.md.)
"""

POINTS = {'X': 1, 'Y': 2, 'Z': 3}
GAGNANTS = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
PERDANTS = [('A', 'Z'), ('B', 'X'), ('C', 'Y')]


def lire_donnees(nom_fichier='input'):
    return [ligne.split() for ligne in open(nom_fichier)]


def partie1(parties):
    score = 0
    for adversaire, joueur in parties:
        score += POINTS[joueur]
        if (adversaire, joueur) in GAGNANTS:
            score += 6
        elif (adversaire, joueur) not in PERDANTS:
            score += 3  # égalité
    return score


def coup_pour(adversaire, couples):
    """Coup du joueur qui forme avec `adversaire` un couple de `couples`."""
    for a, joueur in couples:
        if a == adversaire:
            return joueur


def partie2(parties):
    score = 0
    for adversaire, issue in parties:
        if issue == 'X':  # il faut perdre
            score += POINTS[coup_pour(adversaire, PERDANTS)]
        elif issue == 'Z':  # il faut gagner
            score += 6 + POINTS[coup_pour(adversaire, GAGNANTS)]
        else:  # égalité : on joue le même coup (A -> X, B -> Y, C -> Z)
            meme_coup = chr(ord('X') + ord(adversaire) - ord('A'))
            score += 3 + POINTS[meme_coup]
    return score


parties = lire_donnees()
print('Partie 1 :', partie1(parties))
print('Partie 2 :', partie2(parties))
