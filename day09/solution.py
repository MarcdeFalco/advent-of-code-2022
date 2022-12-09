s = open('input.txt').read()
ropelength = 10

def fix(leader,follower):
    x, y = leader
    xt, yt = follower
    vx, vy = x-xt, y-yt
    dx, dy = max(1,abs(vx)), max(1,abs(vy))
    if dx > 1 or dy > 1:
        return xt+vx//dx, yt+vy//dy
    else:
        return xt, yt

def move_rope(rope, delta):
    x, y = rope[0]
    dx, dy = delta
    rope[0] = (x+dx,y+dy)
    for i in range(1,ropelength):
        rope[i] = fix(rope[i-1],rope[i]) 
    return rope

tails = set()
rope = [ (0,0) ] * ropelength
for l in s.strip().split('\n'):
    move, k = l.split()
    k = int(k)
    delta = {
        'R' : (1,0), 'L' : (-1,0),
        'U' : (0,1), 'D' : (0,-1)
        }
    for _ in range(k):
        move_rope(rope, delta[move])
        tails.add(rope[-1])

print(len(tails))

