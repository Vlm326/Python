def dividers(n):
    new_set = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            new_set.add(i)
            new_set.add(n//i)
    return sorted(new_set)

count = 0
for i in range(700001,800000):
    dividers_of_num = list(dividers(i))
    minimal = [x for x in dividers_of_num if f'{x}'.endswith('7') and x != 7 and x != i]
    if len(minimal) > 0:
        print(i, min(minimal))
        count += 1
        if count == 5:
            break 