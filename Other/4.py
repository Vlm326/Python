from first_twenty_seven import max_length, min_length


with open(fr"C:\Users\vladm\Downloads\27-21b.txt", "r") as file:
    trash = file.readline()
    lst = [tuple(map(float, line.replace(',','.').split())) for line in file]

cluster_1 = []
cluster_2 = []
cluster_3 = []
for x, y in lst:
    if 8 <= x <= 10:
        cluster_3.append((x, y))
    if 2 <= x <= 5 and 2 <= y <= 4:
        cluster_2.append((x, y))
    if 1 <= x <= 4 and 6 <= y <= 8:
        cluster_1.append((x, y))
        
print(int(min([min_length(cluster_1, cluster_2), min_length(cluster_1, cluster_3), min_length(cluster_2, cluster_3)]) * 10000), \
        int(max([max_length(cluster_1, cluster_2), max_length(cluster_1, cluster_3), max_length(cluster_2, cluster_3)]) * 10000))  
        