'''
def f(a,m):
    if a >= 301:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+3,m-1),f(a*5,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19',[s for s in range(1,301) if f(s,2)])
print('20',[s for s in range(1,301) if not(f(s,1)) and f(s,3) ])
print('21',[s for s in range(1,301) if not(f(s,2)) and f(s,4)])
'''

def f(a,m):
    if a >= 435:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+5,m-1),f(a*3,m-1)]
    return any(h) if m % 2 != 0 else all(h)
print('19',[s for s in range(1,435) if f(s,2)])
print('20', [s for s in range(1,435) if not(f(s,1)) and f(s,3)])
print('20', [s for s in range(1,435) if not(f(s,2)) and f(s,4)])