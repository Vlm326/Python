with open(fr"C:\Users\vladm\Downloads\17.txt", 'r') as file:
    lst = [int(x) for x in file]

max_endswith_221 = max([x for x in lst if str(abs(x)).endswith('221')])
ans = []

for i in range(len(lst) - 2):
    x, y, z = lst[i], lst[i + 1], lst[i + 2]
    two_digit_count = (len(str(abs(x))) == 2) + (len(str(abs(y))) == 2) + (len(str(abs(z))) == 2)
    if two_digit_count <= 2:
        odd_second_last_count = (
            (len(str(abs(x))) > 1 and int(str(abs(x))[-2]) % 2 != 0) +
            (len(str(abs(y))) > 1 and int(str(abs(y))[-2]) % 2 != 0) +
            (len(str(abs(z))) > 1 and int(str(abs(z))[-2]) % 2 != 0)
        )
        if odd_second_last_count == 2:
            if x + y + z > max_endswith_221:
                ans.append(x + y + z)


print(len(ans), min(ans))
