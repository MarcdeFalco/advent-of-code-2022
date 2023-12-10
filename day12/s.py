import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(12)

M = [ list(l) for l in aoc.data.split('\n') ]

w, h = len(M), len(M[0])
x0, y0 = None, None
xE, yE = None, None
targets = [] 
for x in range(w):
    for y in range(h):
        if M[x][y] == 'S':
            x0, y0 = x, y
            targets.append( (x, y) )
        if M[x][y] == 'a':
            targets.append( (x, y) )
        if M[x][y] == 'E':
            xE, yE = x, y

for x, y in targets:
    M[x][y] = 'a'
M[xE][yE] = 'z'

def getstep(x0,y0):
    d = [ [ None ] * h for _ in range(w) ]
    p = deque([(x0,y0)])
    d[x0][y0] = 0

    while len(p) > 0:
        x, y = p.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            xv, yv = x+dx, y+dy
            if 0 <= xv < w and 0 <= yv < h:
                c = M[xv][yv]
                if ord(c) - ord(M[x][y]) <= 1 and d[xv][yv] is None:
                    d[xv][yv] = 1 +  d[x][y]
                    if (xv,yv) == (xE,yE):
                        return d[xv][yv]
                    p.append((xv,yv))

if aoc.part == 1:
    ans = getstep(x0,y0)
else:
    l = [getstep(x,y) for (x,y) in targets]
    ans = min([ x for x in l if x is not None])

aoc(ans)
