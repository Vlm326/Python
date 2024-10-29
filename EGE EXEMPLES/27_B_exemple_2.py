def center(cluster: list) -> int:
    min_s = float('inf')
    for cluster_center in cluster:
        s = 0
        for star in cluster:
            s += ((cluster_center[0] - star[0])**2 + (cluster_center[1] - star[1])**2)**0.5
        if s < min_s:
            min_s = s
            coord = cluster_center
    return coord
with open(fr"C:\Users\vladm\Downloads\27_B_17916.txt") as file:
    trash = file.readline()
    lst = [tuple(map(float, line.replace(',','.').split())) for line in file]
    file.close()

first_cluster = []
second_cluster = []
third_cluster = []
fourth_cluster = []
fifth_cluster = []

for i in lst:
    x, y = i
    if y > 14:
        first_cluster.append(i)
    elif 9 < y < 13:
        second_cluster.append(i)
    elif 6 < y < 9:
        third_cluster.append(i)
    elif 2 < y < 4:
        fourth_cluster.append(i)
    else:
        fifth_cluster.append(i)
px = ((center(first_cluster)[0] + center(second_cluster)[0] + center(third_cluster)[0] + center(fourth_cluster)[0] + center(fifth_cluster)[0]) / 5) * 10000
py = ((center(first_cluster)[1] + center(second_cluster)[1] + center(third_cluster)[1] + center(fourth_cluster)[1] + center(fifth_cluster)[1]) / 5) * 10000
print(px, py)