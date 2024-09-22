from math import ceil
for i in range(1, 500):
    if ceil(575 * 9 * i) > 100 * 1024 * 8:
        if i:
            print(i)    
            break

