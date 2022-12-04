p = { 'Z' : 3, 'Y' : 2, 'X' : 1 }

wins = [ ('A', 'Y'), ('B', 'Z'), ('C', 'X') ]
loses = [ ('A', 'Z'), ('B', 'X'), ('C', 'Y') ]

score = 0
for l in open('input'):
    a, b = l.split()
    score += p[b]
    if (a,b) in wins:
        score += 6
    elif (a,b) in loses:
        score += 0
    else:
        score += 3

print('Part 1', score)

score = 0 
for l in open('input'):
    a, b = l.split()
    r = None
    if b == 'X':
        score += 0
        for c in loses:
            if c[0] == a:
                score += p[c[1]]
                break
    if b == 'Z':
        score += 6
        for c in wins:
            if c[0] == a:
                score += p[c[1]]
                break
    if b == 'Y':
        r = chr(ord('X')+ord(a)-ord('A'))
        score += 3 + p[r]

print('Part 2', score)
