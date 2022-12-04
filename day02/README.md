Day 02
======

Un chifoumi avec des caractères, ici, l'erreur serait
de garder les caractères, en passant tout avec des 
entiers 0, 1 ou 2, on peut raisonner simplement
sur la différence modulo 3 pour savoir si une partie
est gagnante, perdante ou une égalité.

En effet, si Rock=0, Paper=1, Scissors=2 on constate
que `X+1 [3]` donne celui qui nous bat et `X-1 [3]`
celui qu'on bat.

* `Python` : 
    * `solution1l.py` un one-liner (ça ne va pas être possible longtemps)
    * `solution.py` une solution très naïve gardant des caractères

