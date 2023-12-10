
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(25)

S = 0
for l in aoc.data.split('\n'):
    s = 0
    d = '=-012'
    b = 1
    for c in reversed(l):
        s += (d.index(c)-2) * b
        b *= 5
    S = S + s

s = ''
while S > 0:
    c = '=-012'[ (S+2) % 5 ]
    s = c + s
    S = (S+2) // 5
ans = s

aoc(ans)
