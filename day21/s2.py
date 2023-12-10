from itertools import cycle
for l in cycle(open('example.txt').readlines()):
    try:
        exec(l.replace(':','='))
        print(root)
        break
    except NameError: pass
