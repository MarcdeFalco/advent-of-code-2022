import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(15)

sensors = []
for l in aoc.data.split('\n'):
    t = l.split()
    xs = int(t[2][2:-1])
    ys = int(t[3][2:-1])
    xb = int(t[-2][2:-1])
    yb = int(t[-1][2:])
    sensors.append((xs,ys,xb,yb))

if aoc.submit:
    w = 4000000
    tgt = 2000000
else:
    w = 20
    tgt = 10

if aoc.part == 1:
    safe = set()

    for s in sensors:
        xs, ys, xb, yb = s
        d = abs(xs-xb)+abs(ys-yb)
        dx = d - abs(ys-tgt)
        min_xs = xs-dx
        max_xs = xs+dx
        for x in range(min_xs,max_xs+1):
            if yb != tgt or x != xb:
                safe.add(x)

    ans = len(safe)
else:
    for tgt in range(w+1):
        intx = [ [0,w] ]
        for s in sensors:
            xs, ys, xb, yb = s
            d = abs(xs-xb)+abs(ys-yb)
            dx = d - abs(ys-tgt)
            if dx <= 0:
                continue
            min_xs = xs-dx
            max_xs = xs+dx
            nintx = []

            for (x0,x1) in intx:
                if min_xs <= x0 <= x1 <= max_xs:
                    pass
                elif x0 <= min_xs <= max_xs <= x1:
                    if x0 < min_xs:
                        nintx.append( (x0,min_xs-1) )
                    if x1 > max_xs:
                        nintx.append( (max_xs+1,x1) )
                elif x0 <= min_xs <= x1:
                    if x0 < min_xs:
                        nintx.append( (x0,min_xs-1) )
                elif x0 <= max_xs <= x1:
                    if x1 > max_xs:
                        nintx.append( (max_xs+1,x1) )
                else:
                    nintx.append( (x0, x1) )

            intx = nintx
            if len(intx) == 0:
                break

        if len(intx) != 0:
            ans = (intx[0][0], tgt)
            break

    ans = ans[0] * 4000000 + ans[1]

#aoc(ans)
