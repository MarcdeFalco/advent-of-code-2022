
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(24)

lines = aoc.data.split('\n')
h = len(lines)
w = len(lines[0])
blizzards = []
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c in '><^v':
            blizzards.append( (x,y,c) )

blizzards = set(blizzards)
ans = 0

bh = []
bv = []
for t in range(h-2):
    m = [ [ False] * w for _ in range(h) ]
    for xb,yb,c in blizzards:
        if c in '<>': continue
        dx, dy = { '>' : (1,0),
                   '<' : (-1,0),
                  'v' : (0,1),
                  '^' : (0,-1) }[c]
        xb = 1 + (xb - 1 + t * dx) % (w-2) 
        yb = 1 + (yb - 1 + t * dy) % (h-2) 
        m[yb][xb] = True
    bv.append(m)
for t in range(w-2):
    m = [ [ False] * w for _ in range(h) ]
    for xb,yb,c in blizzards:
        if c in '^v': continue
        dx, dy = { '>' : (1,0),
                   '<' : (-1,0),
                  'v' : (0,1),
                  '^' : (0,-1) }[c]
        xb = 1 + (xb - 1 + t * dx) % (w-2) 
        yb = 1 + (yb - 1 + t * dy) % (h-2) 
        m[yb][xb] = True
    bh.append(m)

def pp(pt):
    m = [ [ '.' ]  * w for _ in range(h) ] 
    for x in range(w):
        m[0][x] = m[h-1][x] = '#'
    for y in range(h):
        m[y][0] = m[y][w-1] = '#'
    x,y,t = pt
    m[y][x] = 'E'

    for y,l in enumerate(bv[t%(h-2)]):
        for x,c in enumerate(l):
            if c:
                m[y][x] = 'H'
    for y,l in enumerate(bh[t%(w-2)]):
        for x,c in enumerate(l):
            if c:
                m[y][x] = 'V'

    for l in m:
        print(''.join(l))
    print()

from queue import PriorityQueue


def dist(x,y):
    xg, yg = goal
    return (xg-x)*(xg-x) + (yg-y)*(yg-y)

#tovisit = PriorityQueue()
#tovisit.put( (dist(1,0), (1,0,0)) )

def compute(start, goal, t):
    x0,y0 = start
    tovisit = deque()
    tovisit.append( (x0,y0,t) )

    visited = defaultdict(bool)
    last = 0
    best = 1000000
    while len(tovisit) != 0: #not tovisit.empty():
        #d, (x0,y0,t) = tovisit.get()
        x0,y0,t = tovisit.popleft()
        pos = x0,y0
        #if t > last:
        #    print(t)
        #    last = t
        #pp( (x0,y0,t) )
        if pos == goal:
            return t
        if False:
            occ = defaultdict(bool)
            for xb,yb,c in blizzards:
                dx, dy = { '>' : (1,0),
                           '<' : (-1,0),
                          'v' : (0,1),
                          '^' : (0,-1) }[c]
                xb = 1 + (xb - 1 + (t+1) * dx) % (w-2) 
                yb = 1 + (yb - 1 + (t+1) * dy) % (h-2) 
                occ[xb,yb] = True

        def test(x,y,t):
            if y == 0 or y == h-1:
                return True
            if (x,y,t%(w-2),t%(h-2)) in visited:
                return False
            return not (bh[t%(w-2)][y][x] or bv[t%(h-2)][y][x])

            for c in '<>^v':
                dx, dy = { '>' : (1,0),
                           '<' : (-1,0),
                          'v' : (0,1),
                          '^' : (0,-1) }[c]
                xb = 1 + (x - 1 - t * dx) % (w-2) 
                yb = 1 + (y - 1 - t * dy) % (h-2) 
                if (xb,yb,c) in blizzards:
                    return False
            return True

        if test(x0,y0,t+1):
            #tovisit.put( (dist(x0,y0), (x0,y0,t+1)) )
            visited[x0,y0,(t+1)%(w-2),(t+1)%(h-2)] = True
            tovisit.append( (x0,y0,t+1) )
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            x2,y2 = x0+dx,y0+dy
            if ((x2,y2) == goal or (1 <= x2 < w-1 and 1 <= y2 < h-1)) \
                    and test(x2,y2,t+1):
                #tovisit.put( (dist(x2,y2),(x2,y2,t+1)) )
                visited[x2,y2,(t+1)%(w-2),(t+1)%(h-2)] = True
                tovisit.append( (x2,y2,t+1) )

s = (0,1)
g = (w-2,h-1)

t1 = compute( s, g, 0 )
t2 = compute( g, s, t1 )
t3 = compute( s, g, t2 )

ans = t3

aoc(ans)
