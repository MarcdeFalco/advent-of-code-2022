def prio(c):
    if ord(c) < ord('a'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1
    
score = 0
for l in open('input.txt'):
    n = len(l)
    a, b = l[:n//2], l[n//2:]
    s = 0
    common = ''
    for c in a:
        if c in b and c not in common:
            s += prio(c)
            common += c
    score += s
print('Part 1', score)

elves = [ l.strip() for l in open('input.txt').readlines() ]
nelves = len(elves)
s = 0
for i in range(nelves//3):
    a, b, c = elves[3*i:3*i+3]
    a = set(a)
    b = set(b)
    c = set(c)
    c = list(a.intersection(b).intersection(c))[0]
    s += prio(c)
print('Part 2', s)
