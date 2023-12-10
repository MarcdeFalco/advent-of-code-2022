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

aoc = AOC(10)
si = aoc.input
s = aoc.example

if submit:
    s = si

ans = 0

########
cycles = 1
x = 1
score = 0

image = [ list(' ' * 40) for _ in range(6) ]

def plot():
    global cycles, image, line, x
    xc = (cycles-1) % 40
    if x-1 <= xc < x-1 +oo 3:
        image[(cycles-1)//40][xc] = '#'

for i, instr in enumerate(s.strip().split('\n')):
    if cycles % 40 == 20:
        score += cycles * x
    tok = instr.split()
    if tok[0] == 'noop':
        plot()
        cycles += 1
    elif tok[0] == 'addx':
        plot()
        cycles += 1
        if cycles % 40 == 20:
            score += cycles * x
        plot()
        cycles += 1
        x += int(tok[1])

for l in image:
    print(''.join(l))

ans = score
########

if submit:
    aoc.submit(part, ans)
else:
    print(ans)
