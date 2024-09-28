f = open('24_16388.txt').readline()
count = 1
max_count = 1

for i in range(len(f)):
    if f[i-1:i+1] not in 'KLMNK':
        max_count = max(max_count, count)
        count = 1
    else:
        count += 1


print(max_count)


f = open("24_15339.txt").readline()

count = 1
max_count = 1

for i in 'ABC':
    f = f.replace(i, '+')
for j in '6789':
    f = f.replace(j,'*')

for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        count += 1
        max_count = max(max_count,count)
    else:
        count = 1


print(max_count)




f = open('24_13715.txt').readline()
f = f.replace('AB', 'AB ')
f = f.split()

max_l = 0
for i in range(len(f)):
    s = ''.join(f[i:i+51])
    if s[-2] == 'AB':
        s = s[:-1]

    max_l = max(max_l, len(s))

print(max_l)




f = open('24_12254.txt').readline()

max_count = 1
count = 1

for i in range(len(f)):
    if f[i-1:i+1] not in 'RSQR':
        max_count = max(max_count, count)
        count = 1
    else:
        count += 1

print(max_count)


f = open('24_10105.txt').readline()
f = f.replace('T', 'T ')
f = f.split()
max_len = 0
for i in range(len(f)):
    s = ''.join(f[i:i + 101])
    if s[-1] == 'T':
        s = s[:-1]
    max_len = max(max_len, len(s))
print(max_len)


f = open('24_9845.txt').readline()
count = 1
max_count = 1

for i in '89':
    f = f.replace(i, '+')
for i in 'ABC':
    f = f.replace(i, '*')

for i in range(len(f) - 1):
    if f[i] != f[i + 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)



f = open('24_9791.txt').readline()
for c in 'QWRTYUIOPSGHJKLZXVNM':
    f = f.replace(c, ' ')
print(max(f.split(), key = len))
print(len('49EFABAE774DE5B21C7C8'))


f = open('24_9753.txt').readline()

max_len = 0

f = f.replace('Y','Y ')
f = f.split()
for i in range(len(f)):
    s = ''.join(f[i:i + 151])
    if s[-1] == 'Y':
        s = s[:-1]
    max_len = max(max_len, len(s))

print(max_len)
'''
########################################################################################
########################################################################################
########################################################################################

Решение методом двух указателей
'''
f = open('24_9753.txt').readline()
Y_count = l = 0
mx = 0
for r in range(len(f)):
    if f[r] == 'Y':
        Y_count += 1
    while Y_count > 150:
        if f[l] == 'Y':
            Y_count -= 1
        l += 1
    mx = max(mx, r - l + 1)
print(mx)




s = open('24_11954.txt').readline()

k = l = 0
m = 10**100
for r in range(len(s)):
    k += s[r] == 'X'
    if s[r] == 'Y':
        l = r + 1
        k = 0
    while k - (s[l] == 'X') >= 500:
        k -= s[l] == 'X'
        l += 1
    if k >= 500:
        m = min(m, r - l + 1)

print(m)


f = open('24_3763.txt').readline()

mapp = {'A': 0, 'B': 0, 'C': 0}
l = count = 0

for r in range(len(f)):
    mapp[f[r]] += 1
    while mapp['A'] * mapp['B'] * mapp['C'] > 0:
        mapp[f[l]] -= 1
        l += 1
    if r - l > 1:
        count += r - l-1

print(count)
#https://www.youtube.com/watch?v=mr7m-2F_UsM

'''

########################################################################################
########################################################################################
########################################################################################
'''
from itertools import *
f = open('24_8510.txt').readline()
h = []
count = 1
max_count = 1
for x in product('NOP', repeat = 2):
    s = ''.join(x)
    h.append(s)
for i in range(len(f) - 1):
    if (f[i] + f[i + 1]) not in h:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1


print(max_count)

s = open('24_6757.txt').readline()
s = s.replace('CFE', '*').replace('FCE', '*')
for x in 'CFE':
    s = s.replace(x,' ')
print(max(len(x) for x in s.split()))


f = open('24_6054.txt').readline()
f = f.replace('BBA', '+')
f = f.replace('BCA', '+')
f = f.replace('CCA', '+')
f = f.replace('CBA', '+')
for i in 'ABC':
    f = f.replace(i, ' ')

print(max(len(x) for x in f.split())*3)




f = open('24_2251.txt').readline()
f = f.replace('D','D ')
f = f.split()
max_len = 0
for i in range(len(f)):
    s = ''.join(f[i:i + 3])
    if s[-1] == 'D':
        s = s[:-1]
    max_len = max(max_len, len(s))

print(max_len)


f = open('24_17563.txt').readline()
for i in ('**', '--', '*-', '-0', '*0', '-*'):
    f = f.replace(i, '!')
f = f.replace('!', '! ')
f = f.split()
print(max(len(i) for i in f if i[0] not in '+*') - 1)



'''
##########################################################################################
Самое сложное 24, плохой алгоритм O(n**2) 
'''
s = open('24_17641.txt').readline().strip()
for i in ('++', '**', '*+', '+*'):
    s = s.replace(i, 'W')

for k in '23456789':
    s = s.replace(k, '1')
max_len = 0
for x in s.split('W'):
    if len(x) > max_len:
        for i in range(len(x) - 1):
            if x[i] not in ('+', '*') and x[i] + x[i + 1] not in ['00', '01']:
                sub_str = x[i]
                for j in range(i + 1, len(x)):
                    sub_str += x[j]
                    if sub_str[-1] not in '+*' and eval(sub_str) == 0:
                        max_len = max(max_len, len(sub_str))


print(max_len)
'''################################################################################################################'''

'''
GOOD SOLUTION 
'''

s = open('24_17641.txt').readline().strip()
s = s.replace('*0', '*!').replace('+0', '+!')
for i in ('++', '**', '*+', '+*'):
    s = s.replace(i, 'W')
lines = [x.strip('+*').split('+') for x in s.split('W')]
max_len = 0
for frag in lines:
    l = -1
    for sub in frag:
        if '!' in sub:
            l += len(sub) + 1
        elif '0*' in sub:
            l = len(sub[sub.index('0*'):])
        elif len(sub) > 0 and sub[-1] == '0':
            l = 1
        else:
            l = -1
        max_len = max(l, max_len)
print(max_len)

import itertools as it

f = open('24_8567.txt').readline().strip()
permutations = []
for i in it.product('ABCD', repeat=3):
    i = ''.join(i)
    permutations.append(i)

count = 2
mx = 2
for i in range(2, len(f)):
    if f[i - 2:i + 1] not in permutations:
        count += 1
        mx = max(mx, count)
    else:
        count = 2
print(mx)




with open(fr"C:\Users\vladm\Downloads\24_7600.txt", "r") as f:
    string = f.readline()

for i in 'QRS':
    string = string.replace(i, '*')

max_len = float('-inf')
count = 1
for i in range(len(string) - 1):
    if string[i] == '*' and string[i + 1] == '*':
        count = 1
        
    else:
        count += 1
        max_len = max(max_len, count)

print(max_len)



with open(fr"C:\Users\vladm\Downloads\24_7272.txt", 'r') as f:
    string = f.readline()

for i in ('AB', 'CB'):
    string = string.replace(i, '*')

count = 0
max_len = float('-inf')
for i in string:
    if i == '*':
        count += 1
        max_len = max(max_len, count)
    else:
        count = 0


print(max_len)