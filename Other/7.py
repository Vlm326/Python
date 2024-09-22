f = open(fr"C:\Users\vladm\Downloads\9_10711.txt")

ans = 0

for i in f:
    a = [int(x) for x in i.split()]
    repeats_twice = [x for x in a if a.count(x) == 2]
    non_repeating = [x for x in a if a.count(x) == 1]
    max_of_the_string = max(a)
    if len(repeats_twice) == 4  and len(non_repeating) == 3 and max_of_the_string not in repeats_twice:
        ans = sum(a)
        break
    
print(ans)