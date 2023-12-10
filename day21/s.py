
import sys
sys.path.append("..")
from speedaoc import *
from fractions import Fraction

aoc = AOC(21)

t = {}
for l in aoc.data.split('\n'):
    tok = l.split()
    m = tok[0][:-1]
    if len(tok) == 2:
        t[m] = int(tok[1])
    else:
        t[m] = (tok[1],tok[2],tok[3])

def evalm(m):
    if type(t[m]) == int:
        return t[m]
    mg,op,md = t[m]
    if op == '/':
        op = '//'
    v = eval(str(evalm(mg)) + op + str(evalm(md)))
    t[m] = v
    return v

#ans = evalm('root')

def evalm(m):
    if m == 'humn':
        return 'you'
    if type(t[m]) == int:
        return Fraction(t[m],1)
    mg,op,md = t[m]
    eg = evalm(mg)
    ed = evalm(md)
    if type(eg) == Fraction and type(ed) == Fraction:
        #if op == '/':
        #    op = '//'
        v = eval(repr(eg) + op + repr(ed))
    else:
        v = (eg, op, ed) 
    t[m] = v
    return v

t1, _, t2 = t['root']
e1 = evalm(t1)
e2 = evalm(t2)

def pp(m):
    if type(m) == Fraction:
        return str(m)
    if type(m) == int:
        return str(m)
    if type(m) == float:
        return str(m)
    if type(m) == str:
        return m
    a,b,c = m
    return '(' + pp(a) + b + pp(c) +')'

def red(e1,e2):
    if e1 == 'you':
        return e2
    (eg,op,ed) = e1
    inv = { '+' : '-', '-' : '+', 
           '*' : '/', '/' : '*' }
    #print(pp(eg),op,pp(ed),e2)
    if type(ed) == Fraction:
        ev = eval(repr(e2)+inv[op]+repr(ed))
        v = red(eg, ev)
    elif op in ['+','*']:
        ev = eval(repr(e2)+inv[op]+repr(eg))
        v = red(ed, ev)
    else:
        ev = eval(repr(eg)+op+repr(e2))
        v = red(ed, ev)
    print(pp(eg),op,pp(ed),e2,ev,v)
    return v

f = red(e1,e2)
print(float(f))
print(repr(f))
ans = int(f)

aoc(ans)
