import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(14)

below = 0

m = defaultdict(bool)

for path in aoc.data.split('\n'):
    points = [ tuple(map(int, point.split(',')))
              for point in path.split(' -> ') ]
    below = max(below, max(p[1] for p in points))

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

last = 0
ans = 0

def get(x, y):
    if aoc.part == 2 and y == below+2:
        return True
    return m[x,y]

while True:
    x, y = 500, 0

    rest = False

    while not rest and (aoc.part == 2 or y <= below):
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

aoc(ans)












