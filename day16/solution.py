"""Advent of Code 2022, jour 16.

1. Floyd-Warshall donne les distances entre toutes les vannes ; on garde un
   graphe compressé entre AA et les vannes de débit non nul, chaque arête
   coûtant distance + 1 minute (le déplacement puis l'ouverture).
2. `meilleur` explore récursivement, avec mémoïsation sur (position et temps
   restant de chaque agent, masque des vannes ouvertes), les choix du
   premier agent puis, quand il s'arrête, ceux du second : une vanne ouverte
   avec t minutes restantes rapporte t * débit.
Partie 1 : un seul agent pendant 30 minutes (le second n'a pas de temps).
Partie 2 : deux agents pendant 26 minutes.
"""
INFINI = 1000000


def lire_donnees(nom_fichier='input.txt'):
    voisins = {}
    debit = {}
    for ligne in open(nom_fichier).read().strip().split('\n'):
        mots = ligne.split()
        vanne = mots[1]
        debit[vanne] = int(mots[4][5:-1])  # 'rate=13;'
        i = mots.index('valves') if 'valves' in mots else mots.index('valve')
        voisins[vanne] = [v.replace(',', '') for v in mots[i + 1:]]
    return voisins, debit


def graphe_compresse(voisins, debit):
    vannes = list(voisins)
    indice = {v: i for i, v in enumerate(vannes)}
    n = len(vannes)

    # Floyd-Warshall
    dist = [[INFINI] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for v in voisins[vannes[i]]:
            dist[i][indice[v]] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    graphe = {}
    for v in vannes:
        if debit[v] == 0 and v != 'AA':
            continue
        graphe[v] = []
        for v2 in vannes:
            d = dist[indice[v]][indice[v2]]
            if debit[v2] != 0 and d != INFINI:
                graphe[v].append((d + 1, v2))  # déplacement + ouverture
        if len(graphe[v]) == 0:
            del graphe[v]
    return graphe


def resoudre(voisins, debit, t1, t2):
    graphe = graphe_compresse(voisins, debit)
    # bit i - 1 du masque pour la i-ème vanne (dans l'ordre alphabétique) ;
    # AA, la première, est considérée comme ouverte
    noms = sorted(graphe)
    rang = {v: i for i, v in enumerate(noms)}

    def est_ouverte(masque, v):
        if v == 'AA':
            return True
        return (masque >> (rang[v] - 1)) % 2 == 1

    def ouvrir(masque, v):
        return masque + (1 << (rang[v] - 1))

    cache = {}

    def meilleur(c1, t1, c2, t2, masque):
        """Gain maximal, l'agent i étant en ci avec ti minutes restantes."""
        cle = (c1, t1, c2, t2, masque)
        if cle in cache:
            return cache[cle]
        v = 0
        if t1 > 1 or t2 > 1:
            valeurs = []
            if t1 > 1:
                # le premier agent s'arrête là...
                valeurs.append(meilleur(c1, 1, c2, t2, masque))
                # ... ou va ouvrir une autre vanne
                for d, c1p in graphe[c1]:
                    if t1 - d >= 1 and not est_ouverte(masque, c1p):
                        valeurs.append((t1 - d) * debit[c1p]
                                       + meilleur(c1p, t1 - d, c2, t2,
                                                  ouvrir(masque, c1p)))
            else:
                # le premier agent a fini : c'est au tour du second
                c1 = 'AA'
                for d, c2p in graphe[c2]:
                    if t2 - d >= 1 and not est_ouverte(masque, c2p):
                        valeurs.append((t2 - d) * debit[c2p]
                                       + meilleur(c1, t1, c2p, t2 - d,
                                                  ouvrir(masque, c2p)))
            if len(valeurs) > 0:
                v = max(valeurs)
        cache[cle] = v
        return v

    return meilleur('AA', t1, 'AA', t2, 0)


def partie1(voisins, debit):
    return resoudre(voisins, debit, 30, 0)


def partie2(voisins, debit):
    return resoudre(voisins, debit, 26, 26)


voisins, debit = lire_donnees()
print('Partie 1 :', partie1(voisins, debit))
print('Partie 2 :', partie2(voisins, debit))
