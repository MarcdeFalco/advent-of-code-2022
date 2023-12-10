
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(23)

elves = []
for y, l in enumerate(aoc.data.split('\n')):
    for x, c in enumerate(l):
        if c == '#':
            elves.append( (x,y) )


def pp(elves,mx,Mx,my,My):
    me = defaultdict(bool)
    for x,y in elves: me[x,y] = True
    for y in range(my,My+1):
        s = ''
        for x in range(mx,Mx+1):
            if me[x,y]: s += '#'
            else: s += '.'
        print(s)

#pp(elves, -4, 10, -3, 10)
#print()
    
dir_list = 'NSWE'
#for r in range(10):
r = -1
while True:
    r = r + 1
    me = defaultdict(bool)
    for x,y in elves: me[x,y] = True
    moves = []
    count = defaultdict(int)
    nelves = []
    for x,y in elves:
        voisins = [ (x+dx,y+dy) for (dx,dy) in product([-1,0,1],repeat=2) if
                   (dx,dy) != (0,0) and me[x+dx,y+dy] ]
        if voisins == []:
            moves.append( (x,y) )
            continue
        did_move = False
        for k in range(4):
            d = dir_list[ (r+k) % 4 ]
            vois = { 'S' : [(x-1,y+1),(x,y+1),(x+1,y+1)],
                    "N" :  [(x-1,y-1),(x,y-1),(x+1,y-1)],
                    "W" :  [(x-1,y-1),(x-1,y),(x-1,y+1)],
                    "E" :  [(x+1,y-1),(x+1,y),(x+1,y+1)] }[d]
            if all([c not in voisins for c in vois]):
                did_move = True
                moves.append( vois[1] )
                break
        if not did_move:
            moves.append( (x,y) )
        count[moves[-1]] += 1

    for i, (x,y) in enumerate(elves):
        mx, my = moves[i]
        if count[mx,my] == 1:
            nelves.append( (mx,my) )
        else:
            nelves.append( (x,y) )

    
    if nelves == elves:
        break
    elves = nelves

    #pp(elves, -3, 10, -3, 10)
    #print()

if aoc.part == 1:
    elvesx = [ x for x,y in elves ]
    elvesy = [ y for x,y in elves ]
    w = max(elvesx) - min(elvesx) + 1
    h = max(elvesy) - min(elvesy) + 1

    ans = w * h - len(elves)
else:
    ans = r+1

aoc(ans)
