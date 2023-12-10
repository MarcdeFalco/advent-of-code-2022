import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(9, offset=3)
s = aoc.data
if aoc.part == 1:
    ropelength = 2
else:
    ropelength = 10

def fix(a,b):
    x,y=a
    xt,yt=b
    ddx = max(1,abs(x-xt))
    ddy = max(1,abs(y-yt))
    if ddx > 1 or ddy > 1:
        xt += (x-xt)//ddx
        yt += (y-yt)//ddy
    return (xt,yt)

def g(rope, d):
    x, y = rope[0]
    dx, dy = d
    rope[0] = (x+dx,y+dy)
    for i in range(1,ropelength):
        rope[i] = fix(rope[i-1],rope[i]) 
    return rope

tails = set()
rope = [ (0,0) ] * ropelength
for l in s.strip().split('\n'):
    move, k = l.split()
    k = int(k)
    delta = {
        'R' : (1,0), 'L' : (-1,0),
        'U' : (0,1), 'D' : (0,-1)
        }
    for _ in range(k):
        g(rope, delta[move])
        tails.add(rope[-1])

aoc(len(tails))
