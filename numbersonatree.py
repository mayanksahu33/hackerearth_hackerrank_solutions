from sys import stdin,stdout
inp = stdin.readline().strip().split(' ')
h = inp[0]
path = inp[1] if len(inp) > 1 else []
h = 2**(int(h)+1)
i = 1
for c in path:
    if c == 'L':
        i=2*i
    else:
        i=2*i+1
stdout.write(str(h - i))