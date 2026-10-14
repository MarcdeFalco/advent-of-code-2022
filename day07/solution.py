"""Advent of Code 2022, jour 7.

On rejoue le journal de commandes en identifiant chaque répertoire par son
chemin complet (terminé par '/') : `taille` contient la taille des fichiers
directement présents, `sous_reps` la liste des sous-répertoires. Les
tailles sont ensuite cumulées en traitant les chemins par profondeur
décroissante (nombre de '/'), ce qui revient à un parcours postfixe de
l'arbre.
"""

ESPACE_TOTAL = 70000000
ESPACE_NECESSAIRE = 30000000


def lire_donnees(nom_fichier='input.txt'):
    commandes = open(nom_fichier).read().strip().split('\n')
    taille = {}
    sous_reps = {}
    fichiers = {}
    cwd = None
    i = 0
    while i < len(commandes):
        c = commandes[i]
        if cwd is not None and cwd not in taille:
            taille[cwd] = 0
            sous_reps[cwd] = []
            fichiers[cwd] = []
        if c == '$ cd /':
            cwd = '/'
            i += 1
        elif c.startswith('$ cd ..'):
            # on retire le dernier composant du chemin
            cwd = cwd[:cwd[:-1].rindex('/') + 1]
            i += 1
        elif c.startswith('$ cd '):
            cwd += c[len('$ cd '):] + '/'
            i += 1
        elif c.startswith('$ ls'):
            i += 1
            while i < len(commandes) and commandes[i][0] != '$':
                info, nom = commandes[i].split()
                if info == 'dir':
                    if cwd + nom + '/' not in sous_reps[cwd]:
                        sous_reps[cwd].append(cwd + nom + '/')
                elif cwd + nom not in fichiers[cwd]:
                    taille[cwd] += int(info)
                    fichiers[cwd].append(cwd + nom)
                i += 1

    # cumul des tailles, des répertoires les plus profonds vers la racine
    reps = sorted(taille, key=lambda chemin: -chemin.count('/'))
    for rep in reps:
        for sous_rep in sous_reps[rep]:
            taille[rep] += taille[sous_rep]
    return taille


def partie1(taille):
    return sum(t for t in taille.values() if t <= 100000)


def partie2(taille):
    libre = ESPACE_TOTAL - taille['/']
    a_liberer = ESPACE_NECESSAIRE - libre
    return min(t for t in taille.values() if t >= a_liberer)


taille = lire_donnees()
print('Partie 1 :', partie1(taille))
print('Partie 2 :', partie2(taille))
