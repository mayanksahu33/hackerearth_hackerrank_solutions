import sys
n = int(sys.stdin.readline().strip())
l = map(int,sys.stdin.readline().strip().split(' '))
if n%2!=0: print('NO')
elif l.count(0)==0 and n==1: print('NO')
elif l.count(0)>0 and n!=1: print('NO')
elif l.count(0)>0 and n==1: print('YES')
elif (n==len(filter(lambda x: x%2==0,l))): print('YES')
elif (n==len(filter(lambda x: x%2!=0,l))): print('YES')
else: print('NO')