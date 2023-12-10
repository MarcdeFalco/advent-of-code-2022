from itertools import cycle
from copy import deepcopy
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(17)

h = [ 0 ] * 7
mh = 0

col = [ ]

rocks = [
    ( (0,0,0,0), (1,1,1,1) ),
    ( (1,0,1), (2,3,2) ),
    ( (0,0,0), (1,1,3) ),
    ( (0,), (4,) ),
    ( (0,0), (2,2) )
    ]

commands = cycle(aoc.data)

if False:
    col = [ 0 ] * 7
    count= 0


    for rock in cycle(rocks):
        count += 1
        if count > 2022:
            break
        low, high = rock
        w = len(low)
        h = max(high)
        mh = max(col)
        x, y = 2, mh+3

        def is_valid(dx, dy):
            #print(x,y,dx,dy)
            if y+dy < 0:
                return False
            for cx in range(w):
                if x+cx+dx < 0 or x+cx+dx >= 7:
                    return False
                if col[x+cx+dx] > y+dy+low[cx]:
                    #print('Hit',col,x+dx+cx,y+dy+low[cx])
                    return False
            return True

        def place(col,x,y):
            p = max(col[x+cx] for cx in range(w))
            for cx in range(w):
                col[x+cx] = max(col[x+cx],p+high[cx])
             
        for e in commands:
            #print(e)
            dx = -1 if e == '<' else 1
            if is_valid(dx, 0):
                x += dx
            if is_valid(0, -1):
                y -= 1
            else:
                break

        place(col,x,y)
        #print(col)

def pp(col):
    for l in reversed(col):
        s = ''
        for c in l:
            if c == 0:
                s += '.'
            elif c == 1:
                s += '#'
            else:
                s += '@'
        print(s)
    print('-'*7)

count= 0
countc = 0
ncommands = len(aoc.data)

seen = {}

if aoc.submit:
    cyc = 1725
    start = 328
    cych = 2734
else:
    cyc = 63-28
    start = 28
    cych = 102-49

n = 1000000000000
cycle_h = ((n-start)//cyc) * cych
tgt = start + (n-start) % cyc

prof = [ 0 ] * 7

table = []

for rock in cycle(rocks):
    dprof = tuple( mh-p for p in prof )
    sig = (count%5,countc%ncommands,dprof)

    #if sig in seen: #sig == (3, 1850, (2, 2, 0, 2, 3, 10, 8)):
    #    print(sig, seen[sig], count, prof, mh)

    seen[sig] = (count,mh)
    if sig == (3, 28, (2, 2, 0, 2, 3, 5, 7)):
        print(sig, seen[sig], count, prof, mh)

    table.append(mh)

    count += 1
    if count > tgt:
        break

    low, high = rock
    w = len(low)
    h = max(high)
    x0, y0 = 2, mh+3
    x, y = 2, mh+3

    col += [ [0] * 7 for _ in range(3 + h) ]

    def place(col,x,y,v=1):
        for cx in range(w):
            for cy in range(low[cx], high[cx]):
                x1 = x + cx
                y1 = y + cy
                prof[x1] = max(prof[x1],y1+1)
                col[y1][x1] = v

    def is_valid(dx, dy):
        for cx in range(w):
            for cy in range(low[cx], high[cx]):
                x1 = x + cx + dx
                y1 = y + cy + dy
                if 0 > x1 or 0 > y1 or x1 >= 7:
                    #print('Bord',x1,y1)
                    return False
                if col[y1][x1] != 0:
                    #print('Hit',x1,y1)
                    return False
        return True

    #col2 = deepcopy(col)
    #place(col2,x,y,2)
    #pp(col2)

    for e in commands:
        countc += 1
        #print(e)
        dx = -1 if e == '<' else 1
        if is_valid(dx, 0):
            x += dx
        if is_valid(0, -1):
            y -= 1
        else:
            break
        #col2 = deepcopy(col)
        #place(col2,x,y,2)
        #pp(col2)

    #if y+h < mh:
    #    col2 = deepcopy(col)
    #    place(col2,x0,y0,2)
    #    pp(col2)
    #    place(col2,x,y,1)
    #    pp(col2)
    place(col,x,y)
    mh = max(mh,y+h)
    col = col[:mh]

print(tgt,table[tgt],cycle_h,mh)
ans = mh+cycle_h

#for i, h in enumerate(table):
#    print(i,h)


aoc(ans)
