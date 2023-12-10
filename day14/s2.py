import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(14)

below = 0

m = defaultdict(bool)

mX = 10000000
MX = 0

for path in aoc.data.split('\n'):
    points = [ tuple(map(int, point.split(','))) for point in path.split(' -> ') ]
    below = max(below, max(p[1] for p in points))
    MX = max(MX, max(p[0] for p in points))
    mX = min(mX, min(p[0] for p in points))

    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        if x1 == x2:
            if y1 > y2:
                y2, y1 = y1, y2
            for y in range(y1, y2 + 1): m[x1,y] = True
        else:
            if x1 > x2:
                x2, x1 = x1, x2
            for x in range(x1, x2 + 1): m[x,y1] = True

from copy import copy
minit = copy(m)

from PIL import Image
extent = 331, 669
w = extent[1] - extent[0] + 1

def ppi(i):
    im = Image.new('L', (w, below+3), 255)
    for x, y in m:
        c = 128 if m[x,y] else 200
        if (x,y) in minit:
            c = 0
        im.putpixel((x-extent[0], y), c)
    for x in range(w):
        im.putpixel((x, below+2), 0)
    im.save('test%06d.png' % i)

def pp():
    for y in range(below+1):
        s = ''
        for x in range(mX, MX+1):
            if m[x,y]:
                s += '#'
            else:
                s += '.'
        print(s)

last = 0
ans = 0

def get(x, y):
    if y == below+2:
        return True
    return m[x,y]

while True:
    x, y = 500, 0

    rest = False
    #pp()
    if ans % 100 == 0:
        ppi(ans // 100)

    while not rest: # and y <= below:
        if get(x,y+1):
            if get(x-1,y+1):
                if get(x+1,y+1):
                    rest = True
                else:
                    x, y = x+1, y+1
            else:
                x, y = x-1, y +1
        else:
            x, y = x, y+1

    m[x,y] = True

    if not rest:
        break

    ans += 1

    if (x,y) == (500,0):
        break

mX, MX = 10000000, 0
for x, y in m:
    mX = min(mX,x)
    MX = max(MX,x)

print(mX,MX)
aoc(ans)
