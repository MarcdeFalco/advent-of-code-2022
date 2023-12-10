
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(22)

def dprint(*args):
    if not aoc.submit:
        print(*args)
m = aoc.rawdata().split('\n')

inst = m[-2]
m = m[:-3]

w = max(len(l) for l in m)
h = len(m)

xlim = []
ylim = []

for l in m:
    xm, xM =  w-1, 0
    for i in range(len(l)):
        x = l[i]
        if x != ' ':
            xm = min(xm,i)
            xM = max(xM,i)
    xlim.append( (xm, xM) )

for i in range(w):
    ym, yM =  h-1, 0
    for j, l in enumerate(m):
        if i >= len(l):
            continue
        y = l[i]
        if y != ' ':
            ym = min(ym,j)
            yM = max(yM,j)
    ylim.append( (ym, yM) )
    
i = 0
moves = []
while i < len(inst):
    j = i
    while j < len(inst) and inst[j] not in 'RLUD':
        j += 1
    a = int(inst[i:j])
    moves.append( a )
    if j < len(inst):
        d = inst[j]
        moves.append(d)
    i = j+1

x, y, f = xlim[0][0], 0, 0
d = [ (1,0), (0,1), (-1,0), (0,-1) ]
ds = [ '>','v','<','^' ]

print(xlim)
print(ylim)
sz = 50 if aoc.submit else 4
print(sz)

imc = 0
from PIL import Image, ImageDraw

def aff(m):
    global imc
    if imc % 4 != 0:
        imc += 1
        return
    zz = 1
    im = Image.new( 'RGB', (zz*w, zz*h) )
    for y in range(h):
        for x in range(xlim[y][0], xlim[y][1]+1):
            c = m[y][x]
            col = {
                    '#' : (0,0,0),
                    '.' : (50,50,50),
                    '>' : (255,255,0),
                    '<' : (0,0,255),
                    '^' : (255,0,255),
                    'v' : (0,255,0)
                    }
            col = col[c]
            for a in range(zz):
                for b in range(zz):
                    im.putpixel( (a+zz*x,b+zz*y), col)
    im.save('test_%05d.png' % imc)
    imc += 1


def test(x,y,f,moves):
    m2 = [ list(l) for l in m ]
    for move in moves:
        m2[y][x] = ds[f]
        #print('\n'.join([ ''.join(l) for l in m2 ]))
        #aff(m2)
        if type(move) == int:
            dx, dy = d[f]
            for k in range(move):
                x2,y2 = x+dx, y+dy
                if aoc.part == 1:
                    if x2 < xlim[y][0]: x2 = xlim[y][1]
                    if x2 > xlim[y][1]: x2 = xlim[y][0]
                    if y2 < ylim[x][0]: y2 = ylim[x][1]
                    if y2 > ylim[x][1]: y2 = ylim[x][0]
                    f2 = f
                else:
                    f2 = f
                    if not (xlim[y][0] <= x2 <= xlim[y][1] \
                            and ylim[x][0] <= y2 <= ylim[x][1]) \
                            and aoc.submit:
                        if y < sz:
                            face = x // sz
                        elif y < 2 * sz:
                            face = 3 
                        elif y < 3 * sz:
                            face = 4 + x // sz
                        else:
                            face = 6

                        #   12
                        #   3
                        #  45
                        #  6

                        if face == 1:
                            if y2 < ylim[x][0]:
                                #   ^2
                                #   3
                                #  45
                                #  >
                                #x2, y2, f2 = 3 * sz - 1, 3 * sz + x2 % sz, 2
                                x2, y2, f2 = 0, 3 * sz + x2 % sz, 0
                            else:
                                #   <2
                                #   3
                                #  >5
                                #  6
                                x2, y2, f2 = 0, 2*sz + (sz - y2 % sz - 1), 0
                        if face == 2:
                            if y2 < ylim[x][0]:
                                #   1^
                                #   3
                                #  45
                                #  ^
                                x2,y2,f2=x2%sz,4*sz-1,3
                            elif y2 > ylim[x][1]:
                                #   1v
                                #   <
                                #  45
                                #  6
                                x2, y2, f2 = 2*sz-1,sz+x2%sz,2 
                            else:
                                #   1>
                                #   3
                                #  4<
                                #  6
                                x2,y2,f2=2*sz-1,2*sz+(sz-y2%sz-1),2
                        if face ==3:
                            if x2 < xlim[y][0]:
                                #   12
                                #   <
                                #  v5
                                #  6
                                x2,y2,f2=y2%sz,2*sz,1
                            else:
                                #   1^
                                #   >
                                #  45
                                #  6
                                x2,y2,f2=2*sz+y2%sz,sz-1,3
                        if face == 4:
                            if x2 < xlim[y][0]:
                                #   >2
                                #   3
                                #  <5
                                #  6
                                x2, y2, f2 = sz, sz - y2 % sz - 1, 0
                            else:
                                #   12
                                #   >
                                #  ^5
                                #  6
                                x2,y2,f2=sz,sz+x2%sz,0
                        if face == 5:
                            if x2 > xlim[y][1]:
                                x2,y2,f2 = 3*sz-1,sz-y2%sz-1,2
                            else:
                                x2,y2,f2 = sz-1,x2%sz+3*sz,2
                        if face == 6:
                            if x2 > xlim[y][1]:
                                x2,y2,f2 = sz+y2%sz,3*sz-1,3
                            elif x2 < xlim[y][0]:
                                x2,y2,f2 = sz+y2%sz,0,1
                            else:
                                x2,y2,f2 = 2*sz+x2%sz,0,1


                    if not (xlim[y][0] <= x2 <= xlim[y][1] \
                            and ylim[x][0] <= y2 <= ylim[x][1]) \
                            and not aoc.submit:
                        if y < sz:
                            face = 1
                        elif y < 2 * sz:
                            face = 2 + (x // sz)
                        else:
                            face = 3 + (x // sz)
                        dprint(face, x2, xlim[y], y2, ylim[x])
                        if face == 4: # xoverflow right
                            # 6
                            x2, y2, f2 = 3 * sz + (sz - y2 % sz - 1), 2*sz, 1
                        if face == 6:
                            if y2 < ylim[x][0]:
                                # 4
                                x2, y2, f2 = 3 * sz - 1, sz + (sz - x2 % sz - 1), 2
                            elif y2 > ylim[x][1]:
                                # 2
                                x2, y2, f2 = 0, sz + (sz - x2 % sz - 1), 0
                            else:
                                # 1
                                x2, y2, f2 = 3*sz-1, sz - 1 - y2 % sz, 2
                        if face == 1:
                            if x2 < xlim[y][0]:
                                # 3
                                x2, y2, f2 = sz + y2, sz, 1
                            elif x2 > xlim[y][1]:
                                # 6
                                x2, y2, f2 = 4*sz-1, 2*sz + (sz - y2 % sz - 1), 2
                            else:
                                # 2
                                x2, y2, f2 = sz - x2 % sz - 1, sz, 1
                        if face == 2:
                            if y2 < ylim[x][0]:
                                # 1
                                x2, y2, f2 = 2 * sz + (sz - x2 % sz - 1), 0, 1
                            elif y2 > ylim[x][1]:
                                # 5
                                x2, y2, f2 = 2 * sz + (sz - x2 % sz - 1), 3 * sz - 1, 3
                            else:
                                # 6
                                x2, y2, f2 = 3*sz+(sz-y2%sz-1), 3*sz-1,3
                        if face == 3:
                            if y2 < ylim[x][0]:
                                # 1
                                x2,y2,f2=2*sz,x2%sz,0
                            else:
                                # 5
                                x2,y2,f2=2*sz,2*sz+(sz-x2%sz-1),0
                        if face == 5:
                            if x2 < xlim[y][0]:
                                # 3
                                x2,y2,f2=sz+sz-y2%sz-1,2*sz-1,3
                            else:
                                # 2
                                x2,y2,f2=sz-x2%sz-1,2*sz-1,3


                if m[y2][x2] == '#': break
                f = f2
                dx, dy = d[f]
                x, y = x2, y2
                m2[y][x] = ds[f]
                #aff(m2)
                dprint('\n'.join([ ''.join(l) for l in m2 ]))
                dprint()
        elif move == 'R':
            f = (f+1) % 4
        else:
            f = (f-1) % 4

    return x,y,f

if False:
    for y in range(0,h,sz):
        print('A',y)
        test(xlim[y][0], y, 2, [1])
        print('B',y)
        test(xlim[y][1], y, 0, [1])
if False:
    for x in range(0,w,sz):
        print('C',x)
        test(x, ylim[x][0], 3, [1])
        print('D',x)
        test(x, ylim[x][1], 1, [1])

x,y,f =test(xlim[0][0], 0, 0, moves)
#x,y,f =test(xlim[0][0]+10, 60, 3, [4*sz])
print(x,y,f)
ans = 1000 * (y+1) + 4 * (x+1) + f

aoc(ans)
