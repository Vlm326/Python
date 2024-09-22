s = open('16375.txt')
count = 0
for i in s:
    a = [int(x) for x in i.split()]
    povt_2 = [x for x in a if a.count(x) == 2]
    nepovt = [x for x in a if a.count(x) == 1]
    nepovt = sorted(nepovt)
    if len(povt_2) == 2 and len(nepovt) == 5:
        if (nepovt[0] * nepovt[1] * nepovt[2]) > povt_2[0]**2:
            count += 1
print(count)
