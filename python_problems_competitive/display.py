d={}
d[('0',1)] = '+---+'
d[('0',2)] = '|   |'
d[('0',3)] = '|   |'
d[('0',4)] = '+   +'
d[('0',5)] = '|   |'
d[('0',6)] = '|   |'
d[('0',7)] = '+---+'

d[('1',1)] = '    +'
d[('1',2)] = '    |'
d[('1',3)] = '    |'
d[('1',4)] = '    +'
d[('1',5)] = '    |'
d[('1',6)] = '    |'
d[('1',7)] = '    +'

d[('2',1)] = '+---+'
d[('2',2)] = '    |'
d[('2',3)] = '    |'
d[('2',4)] = '+---+'
d[('2',5)] = '|    '
d[('2',6)] = '|    '
d[('2',7)] = '+---+'

d[('3',1)] = '+---+'
d[('3',2)] = '    |'
d[('3',3)] = '    |'
d[('3',4)] = '+---+'
d[('3',5)] = '    |'
d[('3',6)] = '    |'
d[('3',7)] = '+---+'

d[('4',1)] = '+   +'
d[('4',2)] = '|   |'
d[('4',3)] = '|   |'
d[('4',4)] = '+---+'
d[('4',5)] = '    |'
d[('4',6)] = '    |'
d[('4',7)] = '    +'

d[('5',1)] = '+---+'
d[('5',2)] = '|    '
d[('5',3)] = '|    '
d[('5',4)] = '+---+'
d[('5',5)] = '    |'
d[('5',6)] = '    |'
d[('5',7)] = '+---+'

d[('6',1)] = '+---+'
d[('6',2)] = '|    '
d[('6',3)] = '|    '
d[('6',4)] = '+---+'
d[('6',5)] = '|   |'
d[('6',6)] = '|   |'
d[('6',7)] = '+---+'

d[('7',1)] = '+---+'
d[('7',2)] = '    |'
d[('7',3)] = '    |'
d[('7',4)] = '    +'
d[('7',5)] = '    |'
d[('7',6)] = '    |'
d[('7',7)] = '    +'

d[('8',1)] = '+---+'
d[('8',2)] = '|   |'
d[('8',3)] = '|   |'
d[('8',4)] = '+---+'
d[('8',5)] = '|   |'
d[('8',6)] = '|   |'
d[('8',7)] = '+---+'

d[('9',1)] = '+---+'
d[('9',2)] = '|   |'
d[('9',3)] = '|   |'
d[('9',4)] = '+---+'
d[('9',5)] = '    |'
d[('9',6)] = '    |'
d[('9',7)] = '+---+'

d[(':',1)] = ' '
d[(':',2)] = ' '
d[(':',3)] = 'o'
d[(':',4)] = ' '
d[(':',5)] = 'o'
d[(':',6)] = ' '
d[(':',7)] = ' '
s = input().strip()
while s!='end':     
    for i in range(1, 8):
        l=[]
        for c in s:
            l.append(d[(c,i)])
        print ('  '.join(l))
    print ('\n')
    s = input().strip()
print ('end')