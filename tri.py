from operator import add, sub, mul,truediv
operations = {add:'+', sub:'-', mul:'*', truediv:'/'}
a,b,c = map(int, input().split(' '))
for op in operations.keys():
    try:
        bopc = op(b,c)
    except:
        bopc = None
    try:
        aopb = op(a,b)
    except:
        aopb = None
    if bopc and a == bopc:
        print("%s=%s%s%s" % (a, b, operations[op], c))
        break
    elif aopb and c == aopb:
        print("%s%s%s=%s" % (a, operations[op], b, c))
        break