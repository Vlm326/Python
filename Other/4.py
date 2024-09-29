from math import prod

with open(fr"C:\Users\vladm\Downloads\17.16_14653.txt", 'r') as file:
    lst = [int(x) for x in file]

max_endswith_69 = max([x for x in lst if f'{x}'.endswith('69')]) ** 2
sum_min_kratn_17 = ([x for x in lst if x % 17 == 0][0] + [x for x in lst if x % 17 == 0][1]) 

ans = []
for i in range(0, len(lst) - 3):
    x, y, z, w = lst[i], lst[i + 1], lst[i + 2], lst[i + 3]
    condition_1 = ((len(f'{x}') == 3) + (len(f'{y}') == 3) + (len(f'{z}') == 3) + (len(f'{w}') == 3)) == 2
    condition_2 = ((x % 18 == 0) and (y % 18 == 0) and (z % 18 == 0) and (w % 18 == 0)) == 1
    condition_3 = (x + y + z + w) % sum_min_kratn_17 == 0
    condition_4 = prod([x, y, z, w]) <= max_endswith_69
    if all([condition_1, condition_2, condition_3, condition_4]):
        ans.append((x + y + z + w) ** 2)

print(len(ans), min(ans))