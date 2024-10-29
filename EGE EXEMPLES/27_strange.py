def good_line(lst: list):
    lst_1 = []
    for line in lst:
        # Проверяем наличие необходимых данных и корректность зарплат
        if len(line) == 9:
            min_salary = line[4].strip()
            max_salary = line[5].strip()
            min_salary = int(min_salary) if min_salary.isdigit() else None
            max_salary = int(max_salary) if max_salary.isdigit() else None
            if min_salary is not None and max_salary is not None and min_salary > max_salary:
                continue
            
            # Пропускаем строки с отсутствующими обязательными полями
            if all([line[0], line[1], line[2], line[3], line[6], line[7], line[8]]):
                lst_1.append(line)
    return lst_1


def solution(file_path):
    with open(file_path, 'r') as file:
        trash = file.readline()
        lst = [tuple(line.strip().split(';')) for line in file]
    lst = good_line(lst)
    lst = list(set(lst))

    group1 = []

    for line in lst:
        min_salary = int(line[4]) if line[4].isdigit() else 0
        max_salary = int(line[5]) if line[5].isdigit() else 0
        mid_salary = (min_salary + max_salary) // 2 if max_salary != 0 else min_salary

        if 100000 < mid_salary < 300000:
            group1.append(line)
    K, S = 0, 0
    for line in group1:
        if 'Python' in line[8]:
            K += 1
        else:
            S += 1

    return K, S


file_path = fr"C:\Users\vladm\Downloads\27_A.txt"
K, S = solution(file_path)
print(K, S)
