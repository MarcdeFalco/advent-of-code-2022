"""Advent of Code 2022, jour 21.

Chaque singe est une feuille (un nombre) ou un nœud (singe, opération,
singe) d'un arbre d'expression.
Partie 1 : évaluation récursive de la racine.
Partie 2 : l'inconnue est la feuille `humn`. L'évaluation renvoie une
Fraction pour les sous-arbres sans inconnue et l'arbre (gauche, op, droite)
sinon. On résout ensuite « expression = valeur » en épluchant l'arbre : à
chaque nœud, on applique l'opération inverse au membre de droite et l'on
descend du côté de l'inconnue. Les fractions rendent les divisions exactes.
"""
from fractions import Fraction

OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}
INVERSE = {'+': '-', '-': '+', '*': '/', '/': '*'}


def lire_donnees(nom_fichier='input.txt'):
    singes = {}
    for ligne in open(nom_fichier).read().strip().split('\n'):
        mots = ligne.split()
        nom = mots[0][:-1]
        if len(mots) == 2:
            singes[nom] = int(mots[1])
        else:
            singes[nom] = (mots[1], mots[2], mots[3])
    return singes


def partie1(singes):
    def evaluer(nom):
        if isinstance(singes[nom], int):
            return singes[nom]
        gauche, op, droite = singes[nom]
        a, b = evaluer(gauche), evaluer(droite)
        if op == '/':
            return a // b
        return OPERATIONS[op](a, b)

    return evaluer('root')


def partie2(singes):
    def evaluer(nom):
        if nom == 'humn':
            return 'humn'
        if isinstance(singes[nom], int):
            return Fraction(singes[nom])
        gauche, op, droite = singes[nom]
        a, b = evaluer(gauche), evaluer(droite)
        if isinstance(a, Fraction) and isinstance(b, Fraction):
            return OPERATIONS[op](a, b)
        return (a, op, b)  # sous-arbre contenant l'inconnue

    def resoudre(expression, valeur):
        """Valeur de l'inconnue telle que expression = valeur."""
        if expression == 'humn':
            return valeur
        gauche, op, droite = expression
        if isinstance(droite, Fraction):
            # gauche op droite = valeur  =>  gauche = valeur op^-1 droite
            return resoudre(gauche, OPERATIONS[INVERSE[op]](valeur, droite))
        if op in '+*':
            # opération commutative : droite = valeur op^-1 gauche
            return resoudre(droite, OPERATIONS[INVERSE[op]](valeur, gauche))
        # gauche - droite = valeur  =>  droite = gauche - valeur (idem pour /)
        return resoudre(droite, OPERATIONS[op](gauche, valeur))

    gauche, _, droite = singes['root']
    e1, e2 = evaluer(gauche), evaluer(droite)
    # on suppose l'inconnue à gauche de la racine
    return int(resoudre(e1, e2))


singes = lire_donnees()
print('Partie 1 :', partie1(singes))
print('Partie 2 :', partie2(singes))
