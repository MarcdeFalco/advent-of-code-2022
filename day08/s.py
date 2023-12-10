from itertools import permutations, product, combinations
from collections import defaultdict, Counter
import sys
sys.path.append("..")
from speedaoc import AOC

submit = False
if 'submit' in sys.argv:
    submit = True
part = 1
if '2' in sys.argv:
    part = 2

print(submit, part)

aoc = AOC(8)
si = aoc.input
s = aoc.example

if submit:
    s = si

ans = 0

########
m = s.strip().split('\n')
m = [ list(map(int,v)) for v in m ]
w = len(m)
h = len(m[0])
print(w,h)
best_score = 0
for x in range(w):
    for y in range(h):
        v = m[x][y]
        visibles = False
        total = 1
        for d in [(0,1),(0,-1),(1,0),(-1,0)]:
            visible = True
            score = 0
            px = x + d[0]
            py = y + d[1]
            while 0 <= px < w and 0 <= py < h:
                score += 1
                if m[px][py] >= v:
                    visible = False
                    break
                px = px + d[0]
                py = py + d[1]
            visibles = visibles or visible
            total = score*total
        if visibles:
            ans += 1
        if total > best_score:
            best_score = total

ans = best_score
########

if submit:
    aoc.submit(part, ans)
else:
    print(ans)
