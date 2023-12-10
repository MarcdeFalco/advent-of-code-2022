
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(16)

g = {}
f = {}

for l in aoc.data.split('\n'):
    t = l.split()
    valve = t[1]
    flow = int(t[4][5:-1])
    if 'valves' in t:
        i = t.index('valves')
    else:
        i = t.index('valve')
    v = t[i+1:]
    g[valve] =  [ e.replace(',','') for e in v ]
    f[valve] = flow
        
d = {}
s = list(d.keys())
def best_bad(cur, opened, t):
    if t <= 0:
        v = 0
    else:
        v = 0
        for neigh in g[cur]:
            cv = best(neigh, opened, t-1)
            opened.append(cur)
            cv2 = t*f[cur] + best(neigh, opened, t-2)
            opened.pop()
            v = max(v, cv, cv2)
    return v

if False:
    prio = [('AA',0,[])]
    t = 30
    while prio != [] and t > 0:
        mi = 0
        for i in range(1,len(prio)):
            if prio[mi][1] < prio[i][1]:
                mi = i
        x, w, op = prio[mi]
        print(x,w,op)

        del prio[mi]

        if x not in op:
            prio.append( (x,w+t*f[x],op+[x]) )
        for y in g[x]:
            found= False
            for p in prio:
                if p[0] == y:
                    found = True
                    if p[1] < w:
                        j = prio.index(p)
                        prio[j] = (p[0],w,op)
                    break
            if not found:
                prio.append( (y, w, op) )

        t = t-1

d = {}
s = list(d.keys())

actions = {}

def best_old(cur, t, seen):
    if (cur, t, seen) in d:
        return d[cur,t,seen]

    if t <= 0:
        v = 0
    else:
        v = 0
        tp = t-2
        seen2 = seen
        if f[cur] == 0 or cur in seen:
            tp = t-1
        else:
            seen2 = seen + (cur,)

        mn = None
        for neigh in g[cur]:
            cv = best(neigh, tp, seen2)
            if v < cv:
                v = cv
                mn = neigh

        if tp == t-1:
            actions[cur,t] = ('->',mn,v)
        else:
            actions[cur,t] = ('Open',cur,v+(t-1)*f[cur])
            actions[cur,t-1] = ('->',mn,v)

        v = v + (t-1) * f[cur]
    d[cur, t] = v

    return v

rv = []
for x in f:
    if f[x] != 0:
        rv.append(x)
rvi = { rv[i]:i for i in range(len(rv)) }

def opened(s,v):
    if v not in rvi:
        return True
    i = rvi[v]
    return (s >> i) % 2 == 1

def best(cur, t, seen):
    if (cur, t, seen) in d:
        return d[cur,t,seen]

    if t <= 0:
        v = 0
    else:
        if opened(seen,cur):
            v = -1
            mv = None
        else:
            seen2 = seen + (1 << rvi[cur])
            v = (t-1)*f[cur] + best(cur,t-1,seen2)
            mv = ('Open',cur) 

        for neigh in g[cur]:
            cv = best(neigh, t-1, seen)
            if v < cv:
                v = cv
                mv = ('Move',neigh)

        actions[cur,t,seen] = mv

    d[cur, t, seen] = v

    return v

from copy import copy
vs = list(g.keys())

real = len(rv)
def popcount(s):
    return sum(1 for x in range(real) if (s >> x) % 2 == 1)
def count(s):
    v = 0
    for x in vs:
        if opened(s, x):
            v += f[x]
    return v

comp = 0
def best2(c1, c2, t, seen):
    global comp
    if t <= 1: #or real - popcount(seen) >= t+1:
        return 0

    if (c1, c2, t, seen) in d:
        return d[c1,c2,t,seen]
    if (c2, c1, t, seen) in d:
        return d[c2,c1,t,seen]

    mv1 = copy(g[c1])
    mv2 = copy(g[c2])
    if not opened(seen, c1):
        mv1.append('Open')
    if not opened(seen, c2):
        mv2.append('Open')

    v = -1
    mv = None

    for m1, m2 in product(mv1, mv2):
        seen2 = seen
        if c1 == c2:
            if m1 == 'Open' and m2 == 'Open':
                continue
            if m1 != 'Open' and m2!= 'Open' and m1 < m2:
                continue

        if m1 == 'Open':
            seen2 = seen2 + (1 << rvi[c1])
            c1p = c1
        else:
            c1p = m1
        if m2 == 'Open':
            seen2 = seen2 + (1 << rvi[c2])
            c2p = c2
        else:
            c2p = m2

        #print(real, popcount(seen2), 27-t)
        cv = count(seen2) + best2(c1p,c2p,t-1,seen2)

        if v < cv:
            v = cv
            if t == 25:
                print(comp,cv)
            #mv = (m1,m2)

    #actions[c1,c2,t,seen] = mv

    comp += 1
    #if comp % 1000 == 0:
    #    print(comp, v, c1, c2, t, seen, popcount(seen))
    d[c1,c2, t, seen] = v

    return v

def best2tab():
    tab = []
    for i1 in range(len(vs)):
        t1 = []
        for i2 in range(len(vs)):
            t2 = []
            for t in range(27):
                #l = [ 0 ] * (1 << real)
                t2.append( {} )
            t1.append(t2)
        tab.append(t1)

    #for i1 in range(len(vs)):
    #    for i2 in range(len(vs)):
    #        for s in range(1 << real):
    #            tab[i1][i2][2][s] = count(s)
    #            tab[i1][i2][1][s] = count(s)

    print('Allocated')

    for t in range(1, 27):
        for seen in range(1 << real):
            if real - popcount(seen) >= t+2:
                continue
            print(t, seen)
            for i1, c1 in enumerate(vs):
                for i2, c2 in enumerate(vs):
                    mv1 = copy(g[c1])
                    mv2 = copy(g[c2])
                    if not opened(seen, c1):
                        mv1.append('Open')
                    if not opened(seen, c2):
                        mv2.append('Open')

                    v = -1
                    mv = None

                    for m1, m2 in product(mv1, mv2):
                        seen2 = seen
                        cv = 0
                        if c1 == c2:
                            if m1 == 'Open' and m2 == 'Open':
                                continue
                            elif m2 == 'Open':
                                continue
                            elif m1 < m2:
                                continue
                        if m1 == 'Open':
                            seen2 = seen2 + (1 << rvi[c1])
                            c1p = i1
                        else:
                            c1p = vs.index(m1)

                        if m2 == 'Open':
                            seen2 = seen2 + (1 << rvi[c2])
                            c2p = i2
                        else:
                            c2p = vs.index(m2)

                        cv = tab[c1p][c2p][t-1].get(seen2, 0)

                        if v < cv:
                            v = cv

                    v += count(seen)

                    if v != 0:
                        tab[i1][i2][t][seen] = v

    return tab[0][0][26][0]


ans = best2('AA','AA',26,0)
#ans = best2tab()
#pos = ('AA','AA',0)

if False:
    for i in reversed(range(1,27)):
        c1,c2,s = pos
        m1,m2 = actions[c1,c2,i,s]
        print(27-i,m1,m2)
        if m1 == 'Open':
            s = s + (1 << rvi[c1])
        else:
            c1 = m1
        if m2 == 'Open':
            s = s + (1 << rvi[c2])
        else:
            c2 = m2
        pos = (c1,c2,s)

if False:
    pos = ['AA',30,0]
    while pos[1] > 0:
        ac, a = actions[tuple(pos)]
        print(ac, a)
        if ac == 'Open':
            pos[2] += 1 << rvi[pos[0]]
        else:
            pos[0] = a
        pos[1] -= 1

aoc(ans)
