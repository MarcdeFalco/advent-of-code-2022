
import sys
sys.path.append("..")
from speedaoc import *

aoc = AOC(18)

Mx,My,Mz = 0,0,0
mx,my,mz = 100,100,100
cubes = []
s = set()
for cube in aoc.data.split('\n'):
    x,y,z = map(int, cube.split(','))
    cubes.append( (x,y,z) )
    s.add( (x,y,z) )
    mx = min(mx,x)
    my = min(my,y)
    mz = min(mz,z)
    Mx = max(Mx,x)
    My = max(My,y)
    Mz = max(Mz,z)

def ex(t,i,d):
    l = list(t)
    l[i] += d
    return tuple(l)

def inside(t):
    m = [mx,my,mz]
    M = [Mx,My,Mz]
    return all( m[i] <= t[i] <= M[i] for i in range(3))

from PIL import Image

air = []
bugs = []
pockets = 0

#print(mx,my,mz)
for cube in product(range(mx,Mx+1),range(my,My+1),range(mz,Mz+1)):
    if cube in s:
        continue
    #print(cube)
    trapped = True
    if True:
        for i,d in product(range(3),[-1,1]):
            cube2 = cube
            t = False
            while inside(cube2):
                #print('Test',cube2)
                if cube2 in s:
                    t = True
                    break
                cube2 = ex(cube2,i,d)
            trapped = trapped and t
            #print(i,d,t)

    trapped2 = trapped
    trapped = True
    tovisit = deque([ cube ])
    visited = set()
    visited.add(cube)
    while len(tovisit) > 0:
        c = tovisit.popleft()
        if not inside(c):
            trapped = False
            break
        for i,d in product(range(3),[-1,1]):
            c2 = ex(c,i,d)
            if c2 not in s and c2 not in visited:
                visited.add(c2)
                tovisit.append(c2)

    if trapped:
        for c in visited:
            s.add(c)
            air.append( (c,pockets) )
        pockets += 1
    else:
        pass
        #for c in visited:
        #    if inside(c):
        #        s.add(c)
        #        air.append( (c,pockets) )
        #pockets += 1

    if trapped2 and not trapped:
        bugs.append(cube)

dx = Mx-mx+1
dy = My-my+1
dz = Mz-mz+1
im = Image.new( 'RGB', (dx,dy*dz), (255,255,255) )

for z in range(dz):
    for x, y in product(range(dx),range(dy)):
        im.putpixel( (x,y+z*dy), (200,200,200) if z % 2 == 0 else (255,255,255) )

cols = []
from random import randint
for p in range(pockets):
    cols.append( (randint(0,128)+128, randint(0,128)+128, randint(0,256)) )

for x,y,z in cubes:
    im.putpixel( (x-mx,y-my + (z-mz) * dy), (0,0,0) )
for (x,y,z), p in air:
    im.putpixel( (x-mx,y-my + (z-mz) * dy), cols[p] )
#for x,y,z in bugs:
#    im.putpixel( (x-mx,y-my + (z-mz) * dy), (0,255,0) )
im.save('debug.png')

#raise ValueError

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

for zlim in range(mz,Mz+1):
    axes = [dx, dy, dz]
    dc = np.zeros(axes, dtype=bool)
    for x,y,z in cubes:
        if z > zlim: continue
        dc[x-mx, y-my, z-mz] = True
    dair = np.zeros(axes, dtype=bool)
    for (x,y,z),_ in air:
        if z > zlim: continue
        dair[x-mx, y-my, z-mz] = True

    colors = np.empty(axes + [4], dtype=np.float32)
    colors[:] = [0.3, 0.3, 0.3, 0.8]  # red
    colorsa = np.empty(axes + [4], dtype=np.float32)
    colorsa[:] = [0.5, 0.5, 1.0, 1.0]  # red

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(dc, facecolors=colors)
    ax.voxels(dair, facecolors=colorsa)
    #ax.voxels(dbug, facecolors=colorsb)

    plt.savefig('out%02d.png' % zlim)

ans = 0
for cube in cubes:
    sides = 6
    for i,d in product(range(3),[-1,1]):
        if ex(cube,i,d) in s:
            sides -= 1
    ans += sides



#aoc(ans)
