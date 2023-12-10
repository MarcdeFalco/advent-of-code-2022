import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(13)

l = aoc.data.split('\n\n')
pairs = [ tuple(map(eval,v.split('\n'))) for v in l ]

def compare(l1,l2):
    if l1 == [] and l2 == []:
        return None
    if l1 == []:
        return True
    if l2 == []:
        return False
    a, b = l1[0], l2[0]
    if isinstance(a, list) and isinstance(b, list):
        v = compare(a,b)
        if v is None:
            return compare(l1[1:], l2[1:])
        else:
            return v
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        if a > b:
            return False
        return compare(l1[1:], l2[1:])
    if isinstance(a, int):
        l1 = [[a]]+l1[1:]
    if isinstance(b, int):
        l2 = [[b]]+l2[1:]
    return compare(l1,l2)

ans = 0

from functools import cmp_to_key

compare([[1],[2,3,4]], [1,[2,[3,[4,[5,6,0]]]],8,9])

packets = [ [[2]], [[6]] ]
for i, (l1, l2) in enumerate(pairs):
    if compare(l1,l2):
        ans += i+1
    packets += [l1,l2]

if aoc.part == 1:
    aoc(ans)

def cmp(l1, l2):
    val = { True : 1, False : -1, None : 0 }
    v = compare(l1,l2)
    return val[v]

packets.sort(key=cmp_to_key(cmp))
packets.reverse()
i2 = packets.index([[2]])
i6 = packets.index([[6]])

if aoc.part == 2:
    aoc((i2+1)*(i6+1))
