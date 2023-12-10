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
    _, Rr, Cr, Or, Oc, Gr, Go = costs

    #actions[time,robots,res] = 'I'
    if R >= Gr and O >= Go:
        robots2 = ex(robots,3,1)
        res2 = (R+r-Gr,C+c,O+o-Go,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            actions[time,robots,res] = 'G'
    elif R >= Or and C >= Oc and o < Go:
        robots2 = ex(robots,2,1)
        res2 = (R+r-Or,C+c-Oc,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            actions[time,robots,res] = 'O'
    elif R >= Cr and c < Oc:
        robots2 = ex(robots,1,1)
        res2 = (R+r-Cr,C+c,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            actions[time,robots,res] = 'C'
    if R >= Rr and r < max(Rr,Cr,Or,Gr):
        robots2 = ex(robots,0,1)
        res2 = (R+r-Rr,C+c,O+o,G+g)
        v2 = calc(time-1,robots2,res2,costs,cache,actions)
        if v2 > v:
            v = v2
            actions[time,robots,res] = 'R'
    else:
        v2 = calc(time-1,robots,(R+r,C+c,O+o,G+g),costs,cache,actions)
        if v2 > v:
            v = v2
            actions[time,robots,res] = 'I'
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

ans = 0
for k, l in enumerate(aoc.data.split('\n')):
    t = l.split()
    v = (t[1][:-1],t[6],t[12],t[18],t[21],t[27],t[30])
    v = tuple(map(int, v))

    d = {}
    ac = {}

    g = calc(32,(1,0,0,0),(0,0,0,0),v,d,ac)
    print(g)
    ans += g* v[0]

    
    R,C,O,G,r,c,o,g = 0,0,0,0,1,0,0,0
    _, Rr, Cr, Or, Oc, Gr, Go = v
    print(0,R,C,O,G,r,c,o,g)
    for i in reversed(range(1,32+1)):
        va = ac[i,(r,c,o,g),(R,C,O,G)]
        R += r
        C += c
        G += g
        O += o

        if va == 'I':
            pass
        elif va == 'R':
            r += 1
            R -= Rr
        elif va == 'C':
            c += 1
            R -= Cr
        elif va == 'O':
            o += 1
            R -= Or
            C -= Oc
        elif va == 'G':
            g += 1
            R -= Gr
            O -= Go

        print(i,va,R,C,O,G,r,c,o,g)

    break

#print(ans)
#if ans > 3200:
#    aoc(ans)
