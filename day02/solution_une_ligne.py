# Advent of Code 2022, jour 2, en une ligne (exercice de style).
# Coups codés 0, 1, 2 : (joueur - adversaire + 1) % 3 vaut 0, 1 ou 2 pour
# défaite, égalité, victoire ; l'opérateur := nomme les deux coups.
# Affiche les réponses des parties 1 et 2.
print(*(map(sum,zip(*[(ip+1+3*((ip-io+1)%3),ip*3+1+(io+ip-1)%3) for c in map(str.split,open('input')) if ((io := ord(c[0])-ord('A')), (ip := ord(c[1])-ord('X')))]))))


# La même ligne, découpée et commentée
print(*(map(sum, zip(*[
    (ip+1+3*((ip-io+1) % 3),  # score de la partie 1
     ip*3+1+(io+ip-1) % 3)    # score de la partie 2
    # découpe des couples
    for c in map(str.split, open('input'))
    # A -> 0, B -> 1, C -> 2
    if ((io := ord(c[0])-ord('A')),
        # X -> 0, Y -> 1, Z -> 2
        (ip := ord(c[1])-ord('X')))
    ]))))
