
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(20)
l = list(map(int,aoc.data.split('\n')))
dec = 811589153
#dec = 1
l = [ v*dec for v in l ]
n = len(l)

orig = list(l)
l = deque(range(n), maxlen=n)

print(len(set(orig)))
print(n)

def eprint(*args):
    if not aoc.submit:
        print(*args)

#lc = deque(list(l))
#log = []

nr = 10
for _ in range(nr):
    for k in range(n):
        d = l.index(k)

        #eprint(list(l))
        l.rotate(n=-d-1)
        #log.append(list(l))
        l.pop()
        di = orig[k]%(n-1)
        l.rotate(n=-di)
        l.append(k)
        #print(l)
        #print([ orig[k] for k in l])

    i = l.index(0)
    l.rotate(n=-i)

i = l.index(orig.index(0))
a = orig[l[(i+1000) % n]]
b = orig[l[(i+2000) % n]]
c = orig[l[(i+3000) % n]]
print(a,b,c)
ans= a+b+c

aoc(ans)
