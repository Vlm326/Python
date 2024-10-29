def f1(s, m):
    if s >= 30:
        return m % 3 == 0
    if m == 3:
        return 0
    h = [f1(s + 1, m  + 1), f1(s * 2, m + 1)]
    return any(h)
print('19', [x for x in range(1,30) if f1(x, 0)])#4



import sys
sys.setrecursionlimit(100000000)
def f1(s, m):
    if s >= 30:
        return m % 2 == 0
    h = [f1(s + 1, m  + 1), f1(s * 2, m + 1)]
    if m % 3 == 0 or m % 3 == 2:
        return any(h)
    return all(h)

print('20', [x for x in range(1,30) if f1(x,0)])


import sys
sys.setrecursionlimit(100000000)
def f1(s, m):
    if s >= 30:
        return m == 4
    h = [f1(s + 1, m  + 1), f1(s * 2, m + 1)]
    if m % 3 == 0 or m % 3 == 1:
        return any(h)
    return all(h)

print('21', len([x for x in range(1,30) if f1(x,0)]))