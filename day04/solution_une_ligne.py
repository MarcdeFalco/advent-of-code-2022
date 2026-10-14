# Advent of Code 2022, jour 4, en une ligne (exercice de style).
# Les deux compteurs sont cumulés dans une seule somme : la partie 1 compte
# des unités, la partie 2 des multiples de 10000 ; % et // les séparent.
import re

f = 'input.txt'

# Découpée logiquement
print((lambda s: (s % 10000, s // 10000))(sum([
    (1 if a <= c <= d <= b or c <= a <= b <= d else 0) \
    + (10000 if a <= c <= b or c <= a <= d else 0)
    for a,b,c,d in map(lambda s:
    map(int, re.match(r'(\d+)-(\d+),(\d+)-(\d+)',s).groups()),
        open(f))])))

# La ligne
print((lambda s: (s % 10000, s // 10000))(sum([(1 if a <= c <= d <= b or c <= a <= b <= d else 0)+(10000 if a <= c <= b or c <= a <= d else 0)for a,b,c,d in map(lambda s:map(int,re.match(r'(\d+)-(\d+),(\d+)-(\d+)',s).groups()),open(f))])))
