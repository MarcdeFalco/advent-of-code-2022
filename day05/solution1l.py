n = 3
from functools import reduce
print(((l:=open('input.txt').readlines()),''.join(map(lambda s:s[0],reduce(lambda d,i:[d[j]if j+1 not in [i[1],i[2]]else d[j][i[0]:]if j+1 == i[1]else''.join(reversed(d[i[1]-1][:i[0]]))+d[j]for j in range(len(d))],[list(map(int,[ll[1],ll[3],ll[5]]))for ll in map(str.split,l[10:])],[''.join(ll[4*i+1][:-1]).strip()for i in range(9)if(ll:=list(zip(*l[:9])))]))))[1])
