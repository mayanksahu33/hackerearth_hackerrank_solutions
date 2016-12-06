from sys import stdin,stdout
class Trie(object):
    def __init__(self, val):
        self.children = [None]*10
        self.end = False
        self.val = val
    def insert(self, s, i):
        if len(s)==i and any(self.children):
            return False
        if self.end:
            return False
        if len(s)==i:
            self.end = True
            return True
        c = s[i]
        ic = int(c)
        if not self.children[ic]:
            self.children[ic] = Trie(c)
        return self.children[ic].insert(s, i+1)
def func(x):
    phone = stdin.readline().strip()
    res = trie.insert(phone, 0)
    return res
t = int(stdin.readline().strip())
for i in range(t):
    trie = Trie(None)
    n = int(stdin.readline().strip())
    res = map(func, range(n))
    if all(res):
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')
        