totals = [
    sum(map(int, v.split('\n')))
    for v in open('input').read().strip().split('\n\n')
    ]

print('Part 1', max(totals))
print('Part 2', sum(sorted(totals)[-3:]))
