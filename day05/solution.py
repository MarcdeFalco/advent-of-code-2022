
f = 'input.txt'
objects = None
fo = open(f)
for l in fo:
    if l == '\n':
        instructions = fo.readlines()
        break
    if objects is None:
        # initialize
        nobjects = (len(l)+1) // 4
        objects = [ [] for _ in range(nobjects) ]
    if l[:3] == ' 1 ':
        continue
    for i in range(nobjects):
        s = l[4*i:4*i+4]
        if s[0] == ' ': continue
        print(repr(s))
        c = s[1]
        objects[i].append(c)

for l in objects:
    l.reverse()

for instr in instructions:
    print(objects)
    instr = instr.split()
    a, b, c = map(int, [instr[1], instr[3], instr[5]])
    # Part 1
    #for _ in range(a):
    #    objects[c-1].append(objects[b-1].pop())
    # Part 2
    l = objects[b-1][-a:]
    objects[b-1] = objects[b-1][:-a]
    objects[c-1] += l
    print(objects)

print(''.join(o[-1] for o in objects))
