import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(12)

M = [ list(l) for l in aoc.data.split('\n') ]

w, h = len(M), len(M[0])
x0, y0 = None, None
xE, yE = None, None
targets = [] 
for x in range(w):
    for y in range(h):
        if M[x][y] == 'S':
            x0, y0 = x, y
            targets.append( (x, y) )
        if M[x][y] == 'a':
            targets.append( (x, y) )
        if M[x][y] == 'E':
            xE, yE = x, y

for x, y in targets:
    M[x][y] = 'a'
M[xE][yE] = 'z'

from PIL import Image
im = Image.new('RGB', (h, w), (255,255,255))
for x in range(w):
    for y in range(h):
        c = 10 * (ord(M[x][y]) - ord('a'))
        im.putpixel((y, x), (c,c,c))

def getstep(x0,y0):
    d = [ [ None ] * h for _ in range(w) ]
    par = [ [ None ] * h for _ in range(w) ]
    p = deque([(x0,y0)])
    d[x0][y0] = 0

    while len(p) > 0:
        x, y = p.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            xv, yv = x+dx, y+dy
            if 0 <= xv < w and 0 <= yv < h:
                c = M[xv][yv]
                if ord(c) - ord(M[x][y]) <= 1 and d[xv][yv] is None:
                    d[xv][yv] = 1 +  d[x][y]
                    par[xv][yv] = (x,y)
                    if (xv,yv) == (xE,yE):
                        return d[xv][yv], par
                    p.append((xv,yv))

v, par = getstep(x0,y0)
x, y = xE, yE
z = 4
im = im.resize((z*h,z*w)) 
b = False
while par[x][y] is not None:
    if b:
        col = (255,0,0)
    else:
        col = (0,255,0)
    b = not b
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            im.putpixel((z*y+dy,z*x+dx), col)
    x, y = par[x][y]
im.save('travel.png')

