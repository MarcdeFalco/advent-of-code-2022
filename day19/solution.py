"""Advent of Code 2022, jour 19 (brouillon : résultat non garanti).

Recherche récursive mémoïsée sur (temps restant, robots, ressources), avec
des élagages heuristiques : construire un robot géode dès que possible,
sinon un robot obsidienne, sinon un robot argile (chaîne de elif), en ne
dépassant pas le coût maximal de la ressource correspondante ; puis, soit
construire un robot minerai (si l'on en a moins que le plus grand coût en
minerai), soit attendre.
Ces règles réduisent fortement l'espace mais ne garantissent pas l'optimum :
sur cette entrée, la partie 2 est juste mais la partie 1 sous-estime
un plan (10 géodes au lieu de 11), d'où une réponse fausse. Voir aussi la
recherche aléatoire de recherche_aleatoire.c.
"""
import re

# ressources et robots : (minerai, argile, obsidienne, géode)


def lire_donnees(nom_fichier='input.txt'):
    # numéro, coût du robot minerai (minerai), du robot argile (minerai),
    # du robot obsidienne (minerai, argile),
    # du robot géode (minerai, obsidienne)
    return [tuple(map(int, re.findall(r'\d+', ligne)))
            for ligne in open(nom_fichier).read().strip().split('\n')]


def geodes(temps, robots, ressources, couts, cache):
    if temps <= 0:
        return ressources[3]
    cle = (temps, robots, ressources)
    if cle in cache:
        return cache[cle]

    R, C, O, G = ressources
    r, c, o, g = robots
    _, cout_r, cout_c, cout_o_r, cout_o_c, cout_g_r, cout_g_o = couts
    # ressources après une minute de production
    apres = (R + r, C + c, O + o, G + g)

    v = 0
    if R >= cout_g_r and O >= cout_g_o:
        v = max(v, geodes(temps - 1, (r, c, o, g + 1),
                          (apres[0] - cout_g_r, apres[1],
                           apres[2] - cout_g_o, apres[3]),
                          couts, cache))
    elif R >= cout_o_r and C >= cout_o_c and o < cout_g_o:
        v = max(v, geodes(temps - 1, (r, c, o + 1, g),
                          (apres[0] - cout_o_r, apres[1] - cout_o_c,
                           apres[2], apres[3]),
                          couts, cache))
    elif R >= cout_c and c < cout_o_c:
        v = max(v, geodes(temps - 1, (r, c + 1, o, g),
                          (apres[0] - cout_c,) + apres[1:],
                          couts, cache))
    if R >= cout_r and r < max(cout_r, cout_c, cout_o_r, cout_g_r):
        v = max(v, geodes(temps - 1, (r + 1, c, o, g),
                          (apres[0] - cout_r,) + apres[1:],
                          couts, cache))
    else:  # attendre
        v = max(v, geodes(temps - 1, robots, apres, couts, cache))
    cache[cle] = v
    return v


def partie1(plans):
    return sum(plan[0] * geodes(24, (1, 0, 0, 0), (0, 0, 0, 0), plan, {})
               for plan in plans)


def partie2(plans):
    produit = 1
    for plan in plans[:3]:
        produit *= geodes(32, (1, 0, 0, 0), (0, 0, 0, 0), plan, {})
    return produit


plans = lire_donnees()
print('Partie 1 :', partie1(plans))
print('Partie 2 :', partie2(plans))
