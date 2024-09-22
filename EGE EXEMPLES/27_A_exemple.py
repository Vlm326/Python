def center(cluster: list):
    min_s = float('inf')
    for star_center in cluster:
        s = 0
        for star in cluster:
            s += ((star_center[0] - star[0]) ** 2 + (star_center[1] - star[1]) ** 2)**0.5
        if s < min_s:
            min_s = s
            coord = star_center
    return coord


with open(fr"C:\Users\vladm\Downloads\27_A_17834.txt") as file:
    trash = file.readline()
    lst = []
    for line in file:
        line = line.replace(',','.')
        lst.append(list(map(float,line.strip().split())))
    file.close()
first_cluster = []
second_cluster = []
for i in lst:
    if i[0] < 6.0:
        first_cluster.append(i)
    else:
        second_cluster.append(i)

coordinates_first = center(first_cluster)
coordinates_second = center(second_cluster)
px = ((coordinates_first[0] + coordinates_second[0]) / 2) * 100
py = ((coordinates_first[1] + coordinates_second[1]) / 2) * 100
print(px,py)