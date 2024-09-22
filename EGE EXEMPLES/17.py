'''

a = [int(x) for x in open('../17.16_14653.txt')]
ans = []
trio = [x for x in range(100, 1000)]
b = sorted([x for x in a if x > 0 and x % 17 == 0])
max_na_69_square = (max([x for x in a if str(x).endswith('69')]))**2
dlya_c_3 = b[0] + b[1]
for i in range(len(a) - 3):
    x, y, z, w = a[i], a[i+1], a[i + 2], a[i+ 3]
    c_1 = (abs(x) in trio) + (abs(y) in trio) + (abs(z) in trio) + (abs(w) in trio) == 2
    c_2 = (x % 18 == 0) + (y % 18 == 0) + (z % 18 == 0) + (w % 18 == 0) == 1
    c_3 = (x + y + z + w) % dlya_c_3 == 0
    c_4 = (x * y * z * w) <= max_na_69_square
    if c_1 and c_2 and c_3 and c_4:
        ans.append((x + y + z + w)**2)
print(len(ans),min(ans))
'''


a = [int(x) for x in open('17_16383.txt')]
dlya_usl = [x for x in a if str(x).endswith('21') and len(str(abs(x))) == 5]
max_na_21 = max([x for x in a if str(x).endswith('21') and len(str(abs(x))) == 5])
ans = []

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    c1 = (str(x).endswith('21') and x in dlya_usl)
    c2 = (str(y).endswith('21') and y in dlya_usl)
    if (c1 + c2 == 1) and (c1 * c2 == 0):
        if (x ** 2 + y ** 2) > max_na_21**2:
            ans.append(x + y)
print(len(ans),max(ans))
