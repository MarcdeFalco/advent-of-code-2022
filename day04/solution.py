f = 'input.txt'
countains = 0
overlaps = 0
for l in open(f):
    e1, e2 = l.split(',')
    a,b = map(int, e1.split('-'))
    c,d = map(int, e2.split('-'))
    if a <= c <= d <= b or c <= a <= b <= d:
        countains += 1
    if a <= c <= b or c <= a <= d:
        overlaps += 1
print('Part 1', countains) 
print('Part 2', overlaps) 
