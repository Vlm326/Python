def count_social_animals(cluster):
    social_count = 0
    non_social_count = 0
    for i, animal in enumerate(cluster):
        neighbors = 0
        for j, other_animal in enumerate(cluster):
            if i != j:
                distance = ((animal[0] - other_animal[0])**2 + \
                            (animal[1] - other_animal[1])**2)**0.5
                if distance <= 0.1:
                    neighbors += 1
        if neighbors >= 14 and 1 <= animal[0] <= 3 and 1 <= animal[1] <= 2:
            social_count += 1
        elif neighbors < 14 and 1 <= animal[0] <= 3 and 1 <= animal[1] <= 2:
            non_social_count += 1
        else:
            pass
    return social_count, non_social_count


with open(fr"C:\Users\vladm\Downloads\27_A.txt") as f:
    lst = [tuple(map(float, line.replace(',','.').split())) for line in f]


first_group = []
second_group = []


for i in lst:
    if 0.9 <= i[0] <= 3.1 and 0.9 <= i[1] <= 2.1:
        first_group.append(i)
    

K, S = count_social_animals(first_group)
print(K, S)









def count_social_animals(cluster):
    social_count = 0
    non_social_count = 0
    for i, animal in enumerate(cluster):
        neighbors = 0
        for j, other_animal in enumerate(cluster):
            if i != j:
                distance = ((animal[0] - other_animal[0])**2 + \
                            (animal[1] - other_animal[1])**2)**0.5
                if distance <= 0.1:
                    neighbors += 1
        if neighbors >= 14 and 2 <= animal[0] <= 4 and 3 <= animal[1] <= 4:
            social_count += 1
        elif neighbors >= 14 and 3 <= animal[0] <= 4 and 2 <= animal[1] <= 3:
            social_count += 1
        elif neighbors < 14 and 2 <= animal[0] <= 4 and 3 <= animal[1] <= 4:
            non_social_count += 1
        elif neighbors < 14 and 3 <= animal[0] <= 4 and 2 <= animal[1] <= 3:
            non_social_count += 1    
        else:
            pass
    return social_count, non_social_count



with open(fr"C:\Users\vladm\Downloads\27_B.txt") as f:
    lst = [tuple(map(float, line.replace(',','.').split())) for line in f]


group = []


for i in lst:
    if 1.9 <= i[0] <= 4.1 and 2.9 <= i[1] <= 4.1:
        group.append(i)
    if 2.95 <= i[0] <= 4.1 and 1.9 <= i[1] <= 3:
        group.append(i)

K, S = count_social_animals(group)
print(K, S)