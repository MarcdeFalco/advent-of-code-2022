import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(11)

class Monkey:
    def __init__(self, n):
        self.n = n

l = aoc.data.split('\n')

i = 0
monkeys = []
testers = []
while i < len(l):
    n = int(l[i].split()[1][:-1])
    m = Monkey(n)
    m.items = deque([ int(i) for i in l[i+1][l[i+1].find(':')+1:].split(', ')])
    toks = l[i+2].split()
    m.ope = (toks[-2], toks[-1])
    m.div = int(l[i+3].split()[-1])
    m.gotrue = int(l[i+4].split()[-1])
    m.gofalse = int(l[i+5].split()[-1])
    testers.append(m.div)
    monkeys.append(m)
    i += 7

from math import prod
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

N = testers[0]
for t in testers[1:]:
    N *= (t//gcd(N, t))

inspected = [ 0 for _ in range(len(monkeys)) ]
rounds = 21 if aoc.part == 1 else 10001

for rd in range(1,rounds):
    for m in monkeys:
        while len(m.items) > 0:
            inspected[m.n] += 1
            p = m.items.popleft()
            ope, arg = m.ope
            if arg == 'old':
                arg = p
            else:
                arg = int(arg)
            if ope == '+':
                p = arg + p
            else:
                p = arg * p
            if aoc.part == 1:
                p //= 3
            p = p % N
            if p % m.div == 0:
                monkeys[m.gotrue].items.append(p)
            else:
                monkeys[m.gofalse].items.append(p)

inspected.sort()

#aoc(inspected[-1] * inspected[-2])
