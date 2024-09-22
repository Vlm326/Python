def count_balanced_amounts(file_path):
    with open(file_path, 'r') as file:
        N = int(file.readline())
        lst = [int(x) for x in file] 
    balance = 0
    balance_count = {0: 1} 
    answer = 0

    for n in range(N):
        num = lst[n]
        if num > 0:
            balance += 1
        elif num < 0:
            balance -= 1
        answer += balance_count.get(balance, 0)
        balance_count[balance] = balance_count.get(balance, 0) + 1
    return answer

file_A_count = count_balanced_amounts(fr"C:\Users\vladm\Downloads\27-A_11567.txt")
file_B_count = count_balanced_amounts(fr"C:\Users\vladm\Downloads\27-B_11567.txt")

print(file_A_count, file_B_count)