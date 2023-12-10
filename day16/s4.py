import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(16)

g = {}
f = {}

vs = []
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
    vs.append(valve)

vsi = { vs[i]:i for i in range(len(vs)) }
gr = {}
pred = {}
visit = deque()
visit.append('AA')

n = len(vs)
infinity = 1000000 
m = [ [ infinity ] * n for _ in range(n) ]
for i in range(n):
    m[i][i] = 0
    for j in range(n):
        if vs[j] in g[vs[i]]:
            m[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            m[i][j] = min(m[i][j], m[i][k] + m[k][j])

for v in vs:
    if f[v] == 0 and v != 'AA':
        continue

    gr[v] = []
    for v2 in vs:
        d = m[vsi[v]][vsi[v2]] 
        if f[v2] != 0 and d != infinity:
            gr[v].append( (d+1,v2) )
    if len(gr[v]) == 0:
        del gr[v]

cache = {}

vs = list(gr.keys())
vs.sort()
vsi = { vs[i]:i for i in range(len(vs)) }

def isop(s,v):
    if v == 'AA':
        return True
    i = vsi[v] - 1
    return (s >> i) % 2 == 1

def op(s,v):
    i = vsi[v] - 1
    return s + (1 << i)

def best(c1,t1,c2,t2,s):
    if (c1,t1,c2,t2,s) in cache:
        return cache[(c1,t1,c2,t2,s)]

    v = 0
    if t1 > 1 or t2 > 1:
        values = []

        if t1 > 1:
            values.append(best(c1,1,c2,t2,s))
            for d, c1p in gr[c1]:
                if t1-d >= 1 and not isop(s, c1p):
                    values.append(
                            (t1-d)*f[c1p] + \
                                best(c1p,t1-d,c2,t2,op(s,c1p)))
        else:
            c1 = 'AA'
            for d, c2p in gr[c2]:
                if t2-d >= 1 and not isop(s, c2p):
                    values.append(
                            (t2-d)*f[c2p] + \
                                best(c1,t1,c2p,t2-d,op(s,c2p)))

        if len(values) > 0:
            v = max(values)

    cache[c1,t1,c2,t2,s] = v

    return v


ans = best('AA',26,'AA',26,0)
print(ans)
print(len(cache))
