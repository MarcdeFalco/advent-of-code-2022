# one-liner
print(*(map(sum,zip(*[(ip+1+3*((ip-io+1)%3),ip*3+1+(io+ip-1)%3) for c in map(str.split,open('input')) if ((io := ord(c[0])-ord('A')), (ip := ord(c[1])-ord('X')))]))))


# sur plusieurs lignes
print(*(map(sum,zip(*[
    (ip+1+3*((ip-io+1)%3), # part 1 scoring
     ip*3+1+(io+ip-1)%3) # part 2 scoring 
     # split couples
     for c in map(str.split,open('input')) 
     # A->0,B->1,C->2
     if ((io := ord(c[0])-ord('A')),
     # X->0,Y->1,Z->2
        (ip := ord(c[1])-ord('X')))
    ]))))
