import re

f = 'input.txt'

# Split logically 
print((lambda s: (s % 10000, s // 10000))(sum([ 
    (1 if a <= c <= d <= b or c <= a <= b <= d else 0) \
    + (10000 if a <= c <= b or c <= a <= d else 0)
    for a,b,c,d in map(lambda s: 
    map(int, re.match(r'(\d+)-(\d+),(\d+)-(\d+)',s).groups()),
        open(f))])))

# The line
print((lambda s: (s % 10000, s // 10000))(sum([(1 if a <= c <= d <= b or c <= a <= b <= d else 0)+(10000 if a <= c <= b or c <= a <= d else 0)for a,b,c,d in map(lambda s:map(int,re.match(r'(\d+)-(\d+),(\d+)-(\d+)',s).groups()),open(f))])))

