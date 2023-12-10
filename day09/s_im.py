from itertools import permutations, product, combinations
from collections import defaultdict, Counter
import sys
sys.path.append("..")
from speedaoc import AOC

submit = False
if 'submit' in sys.argv:
    submit = True
part = 1
if '2' in sys.argv:
    part = 2

print(submit, part)

aoc = AOC(9)
si = aoc.input
s = aoc.example

if submit:
    s = si

ans = 0

########

if part == 1:
    ropelength = 2
else:
    ropelength = 10

ropelength = 100

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

def pr(rope):
    for y in reversed(range(6)):
        s = ''
        for x in range(6):
            c = '.'
            for i in range(ropelength):
                if (x,y) == rope[i]:
                    c = str(i)
                    break
            s += c
        print(s)
    print()

tails = set()
rope = [ (0,0) ] * ropelength

xm, xM, ym, yM = (0,0,0,0)

ropes = [ rope.copy() ]

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
        ropes.append(rope.copy())
        for x,y in rope:
            xm = min(xm,x)
            ym = min(ym,y)
            xM = max(xM,x)
            yM = max(yM,y)


ans = len(tails)

########

print(xm, xM, ym, yM)
w = xM - xm + 1
w = w + w%2
h = yM - ym + 1
h = h + h%2
print(w,h)
from PIL import Image

plots = []
for i, rope in enumerate(ropes):
    im = Image.new('RGB', (w, h), (255,255,255))
    for x, y in plots:
        im.putpixel((x-xm, y-ym), (128,128,128))
    for j, (x, y) in enumerate(rope):
        im.putpixel((x-xm, y-ym), (255,2*j,2*j))
    plots.append(rope[-1])
    im.save("out%07d.png" % i)

