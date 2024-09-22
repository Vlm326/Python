def center(cluster: list) -> int:
    min_s = float(1000000000000.0)
    for cluster_center in cluster:
        s = 0
        for star in cluster:
            s += ((cluster_center[0] - star[0])**2 + (cluster_center[1] - star[1])**2)**0.5
        if s < min_s:
            min_s = s
            coord = cluster_center
    return coord


with open(fr"C:\Users\vladm\Downloads\27_B_17834.txt") as file:
    trash = file.readline()
    lst = [tuple(map(float, line.replace(',','.').split())) for line in file]
    file.close()

first_cluster = []
second_cluster = []
third_cluster = []

for i in lst:
    x, y = i
    if y < 2:
        first_cluster.append(i)
    elif y > 2 and x < 4:
        second_cluster.append(i)
    else:
        third_cluster.append(i)

first_center = center(first_cluster)
second_center = center(second_cluster)
third_center = center(third_cluster)

px = ((first_center[0] + second_center[0] + third_center[0])/3)*100
py = ((first_center[1] + second_center[1] + third_center[1])/3)*100
print(px,py)