from itertools import *
count = 0
for i in product('0123456', repeat = 7):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('6') + s.count('4') + s.count('2') + s.count('0') == 2:
            count += 1
print(count)