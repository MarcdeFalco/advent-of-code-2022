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

aoc = AOC(7)
si = aoc.input
s = aoc.get_example(1)

if submit:
    s = si

ans = 12

import re
#f = 'test.txt'
#f = 'input.txt'
#commands = [ l.strip() for l in open(f).readlines() ]

commands = s.strip().split('\n')

size = {}
subdir = {}
files = {}

cwd = None
i = 0
while i < len(commands):
    c = commands[i]
    print(c)
    if cwd is not None and cwd not in size:
        size[cwd] = 0
        subdir[cwd] = []
        files[cwd] = []
    if c == '$ cd /':
        cwd = '/'
        i = i+1
    elif c.startswith('$ cd ..'):
        i = i+1
        cwd = cwd[:cwd[:-1].rindex('/')+1]
    elif c.startswith('$ cd '):
        cwd += c[len('$ cd '):] + '/'
        i = i+1
    elif c.startswith('$ ls'):
        i = i+1
        while i < len(commands) and not commands[i][0] == '$':
            length, f = commands[i].split()
            if length == 'dir':
                if f not in subdir[cwd]:
                    subdir[cwd].append(cwd + f + '/')
            else:
                if f not in files[cwd]:
                    size[cwd] += int(length)
                    files[cwd].append(cwd + f + '/')
            i = i+1

dirs = list(size.keys())
dirs.sort(key=lambda x: -x.count('/'))
for d in dirs:
    for sd in subdir[d]:
        print(d, sd)
        size[d] += size[sd]
t = 0
for d in size:
    if size[d] < 100000:
        t += size[d]


ans = t

dirs.sort(key=lambda x: size[x])
free = 70000000-size['/'] 
need = 30000000-free
for d in dirs:
    if size[d] >= need:
        print(d, size[d])
        break


if submit:
    aoc.submit(part, ans)
else:
    print(ans)
