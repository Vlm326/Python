def center(cluster):
    min_s = float('inf')
    for cluster_center in cluster:
        s = 0
        for star in cluster:
            s += ((cluster_center[0] - star[0])**2 \
                  + (cluster_center[1] - star[1])**2)**0.5
        if s < min_s:
            min_s = s 
            coord = cluster_center
    return coord



with open(fr"C:\Users\vladm\Downloads\27_A_17882.txt") as file:
    lst = [tuple(map(float, line.replace(',','.').split())) for\
           line in file]
    file.close

first_cluster = []
second_cluster = []


for i in lst:
    if i[0] < 1:
        first_cluster.append(i)
    else:
        second_cluster.append(i)


px = ((center(first_cluster)[0] + center(second_cluster)[0])/2) * 10000
py = ((center(first_cluster)[1] + center(second_cluster)[1])/2) * 10000
print(px, py)