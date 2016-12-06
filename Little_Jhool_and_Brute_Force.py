import sys
from bisect import bisect_left
taxicab = [1729,4104,13832,20683,32832,39312,40033,46683,64232,65728,110656,110808,134379,149389,165464,171288,195841,216027,216125,262656,314496,320264,327763,373464,402597,439101,443889,513000,513856,515375,525824,558441,593047,684019,704977]
t=int(sys.stdin.readline().strip())
while t>0:
    n = int(sys.stdin.readline().strip())
    res = taxicab[bisect_left(taxicab, n)-1]
    if res<n: print(res)
    else: print(-1)
    t-=1

            