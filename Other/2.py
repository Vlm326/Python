from fnmatch import fnmatch
def dividers(n):
    divider = set()
    for i in range(1, int(n**0.5)+ 1):
        if n % i == 0:  
            divider.add(i)
            divider.add(n//i)
    return list(filter(lambda x: x % 2 == 0, divider))

breaker = 0
for i in range(65000,650000):
    if fnmatch(f'{i}', '6*97*5?') and len(dividers(i)) >= 4:
        print(i, sum(dividers(i)))
        breaker += 1
        if breaker == 7:
            break
