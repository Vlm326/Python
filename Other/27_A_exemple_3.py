def center(cluster):
    min_s = float('inf')
    for cluster_center in cluster:
        s = 0
        for star in cluster:
            s += ((cluster_center[0] - star[0]) ** 2 + (cluster_center[1] - star[1])**2)**0.5
        if s < min_s:
            min_s = s
            coord = cluster_center
    return coord

with open(fr"C:\Users\vladm\Downloads\27_A_17915.txt") as file:
    trash = file.readline()
    lst = [tuple(map(float, line.replace(',','.').split())) for line in file]
    file.close()

cluster_1 = []
cluster_2 = []
cluster_3 = []
for i in lst:
    if i[0] < 6:
        cluster_1.append(i)
    elif i[0] > 6 and i[1] < 22:
        cluster_2.append(i)
    else:
        cluster_3.append(i)

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

px = ((center_1[0] + center_2[0] + center_3[0])/3)*10000
py = ((center_1[1] + center_2[1] + center_3[1])/3)*10000
print(px, py)