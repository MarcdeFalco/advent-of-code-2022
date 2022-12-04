prio = lambda c: ic-38 if (ic:=ord(c)) and ic < 97 else ic-96
print(sum(prio(a.intersection(b).pop()) for (a,b) in map(lambda l: (set(l[:len(l)//2]),set(l[len(l)//2:])), open('input.txt'))))
print(((l := list(map(str.strip,open('input.txt').readlines()))), sum(prio(set(a).intersection(set(b)).intersection(set(c)).pop()) for (a,b,c) in (l[p:p+3] for p in range(0,len(l),3))))[1])
