import random
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(19)

def ex(t,i,d):
    l = list(t)
    l[i] += d
    return tuple(l)

def calc(time,robots,res,costs,cache,actions):
    if time <= 0:
        return res[3]
    if (time,robots,res) in cache:
        return cache[time,robots,res]

    R,C,O,G = res
    r,c,o,g = robots

    values = []

    v = 0
    for k in range(1,time):
        res2 = (R+k*r,C+k*c,O+k*o,G+k*g)
        v = max(v,calc(time-k,robots,res2,costs,cache,actions))
    _, Rr, Cr, Or, Oc, Gr, Go = costs
    #actions[time,robots,res] = 'I'
    do_ore = True
    if R >= Gr and O >= Go:
        do_ore = False
        robots2 = ex(robots,3,1)
        res2 = (R+r-Gr,C+c,O+o-Go,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            #actions[time,robots,res] = 'G'
    if do_ore and R >= Or and C >= Oc:
        do_ore = False
        robots2 = ex(robots,2,1)
        res2 = (R+r-Or,C+c-Oc,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            #actions[time,robots,res] = 'O'
    if do_ore and R >= Cr:
        robots2 = ex(robots,1,1)
        res2 = (R+r-Cr,C+c,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            #actions[time,robots,res] = 'C'
    if do_ore and R >= Rr:
        robots2 = ex(robots,0,1)
        res2 = (R+r-Rr,C+c,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            #actions[time,robots,res] = 'R'
    cache[time,robots,res] = v
    return v

def glouton(time,robots,res,costs):
    R,C,O,G = res
    r,c,o,g = robots
    _, Rr, Cr, Or, Oc, Gr, Go = costs

    hist = []
    while time > 0:
        R += r
        C += c
        O += o
        G += g
        
        t = [ (R,C,O,G,r,c,o,g) ]

        if R-r >= Gr and O-o >= Go:
            t = [(R-Gr,C,O-Go,G,r,c,o,g+1)]
        elif R-r >= Or and C-c >= Oc:
            t = [(R-Or,C-Oc,O,G,r,c,o+1,g)]
        elif R-r >= Cr:
            t = [(R-Cr,C,O,G,r,c+1,o,g)]
        elif R-r >= Rr:
            t = [(R-Rr,C,O,G,r+1,c,o,g)]
        R,C,O,G,r,c,o,g = random.choice(t)
        #hist.append((r,c,o,g,R,C,O,G))

        time = time-1

    #if G == 12:
    #    for v in hist:
    #        print(v)
    return G

   
def rand(time,robots,res,costs):
    R,C,O,G = res
    r,c,o,g = robots
    _, Rr, Cr, Or, Oc, Gr, Go = costs

    hist = []
    while time > 0:
        R += r
        C += c
        O += o
        G += g
        
        wg, wo, wc, wr, wi = 10,10,5,3,1
        wg, wo, wc, wr, wi = 1,1,1,1,1
        wg, wo, wc, wr, wi = 10,10,1,1,10
        wg, wo, wc, wr, wi = 10,10,2,2,1

        t = [ (R,C,O,G,r,c,o,g) ] * wi

        if R-r >= Gr and O-o >= Go:
            t += [(R-Gr,C,O-Go,G,r,c,o,g+1)] * wg
        if R-r >= Or and C-c >= Oc:
            t += [(R-Or,C-Oc,O,G,r,c,o+1,g)] * wo
        if R-r >= Cr:
            t += [(R-Cr,C,O,G,r,c+1,o,g)] * wc
        if R-r >= Rr:
            t += [(R-Rr,C,O,G,r+1,c,o,g)] * wr
        R,C,O,G,r,c,o,g = random.choice(t)
        #hist.append((r,c,o,g,R,C,O,G))

        time = time-1

    #if G == 12:
    #    for v in hist:
    #        print(v)
    return G

best = {
    1 : 11,
    2 : 21,
    3 : 17
}
bestv = {
    1 : 0,
    2 : 1,
    3 : 0,
    4 : 0,
    5 : 1,
    6 : 2,
    7 : 2,
    8 : 11,
    9 : 0,
    10 : 12,
    11 : 0,
    12 : 0,
    13 : 0,
    14 : 0,
    15 : 0,
    16 : 3,
    17 : 0,
    18 : 2,
    19 : 3,
    20 : 5,
    21 : 2,
    22 : 2,
    23 : 4,
    24 : 1,
    25 : 9,
    26 : 12,
    27 : 3,
    28 : 0,
    29 : 4,
    30 : 0
}

ans = 1
for l in aoc.data.split('\n')[:3]:
    t = l.split()
    v = (t[1][:-1],t[6],t[12],t[18],t[21],t[27],t[30])
    v = tuple(map(int, v))
    d = {}
    ac = {}
    #g = calc(24,(1,0,0,0),(0,0,0,0),v,d,ac)
    #print(g)

    target = int(sys.argv[3][1:])
    if v[0] != target:
        continue
    essais = int(sys.argv[4][1:])
    print(target,essais)
    
    g = 0
    if v[0] in best:
        #print('Glouton', glouton(24,(1,0,0,0),(0,0,0,0),v))
        g = best[v[0]]
        #print('Best',v[0],g)
        #print('Glouton', glouton(24,(1,0,0,0),(0,0,0,0),v))
    for essai in range(essais):
        r = rand(32,(1,0,0,0),(0,0,0,0),v)
        if r == g:
            print('Again',v[0],r)
        if r > g:
            print('Mieux',v[0],r)
            g = r
    print('Best',v[0],g)

    #ans += v[0] * g
    ans *= g


    R,C,O,G = (0,0,0,0)
    r,c,o,g = (1,0,0,0)
    _, Rr, Cr, Or, Oc, Gr, Go = v
    if False:
        for m in range(1,25):
            print(m)
            a = ac[24-m+1,(r,c,o,g),(R,C,O,G)]

            R += r
            C += c
            O += o
            G += g
            if a == 'R':
                r += 1
                R -= Rr
                print('Build 1 ore robot')
            if a == 'O':
                o += 1
                R -= Or
                C -= Oc
                print('Build 1 obsidian robot')
            if a == 'C':
                c += 1
                R -= Cr
                print('Build 1 clay robot')
            if a == 'G':
                g += 1
                R -= Gr
                O -= Go
                print('Build 1 geode robot')
            print(r,c,o,g)
            print(R,C,O,G)

    #for k in sorted(d.keys()):
    #    print(k,d[k])

if ans > 3200:
    aoc(ans)
