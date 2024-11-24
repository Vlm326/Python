def find_min_distance(cluster1, cluster2):
    min_distance = float('inf')
    closest_dots = None

    for star1 in cluster1:
        for star2 in cluster2:
            distance = ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_dots = (star1, star2)

    return closest_dots

with open(fr"C:\Users\vladm\Downloads\27A_18031.txt") as file:
    lst = [tuple(map(float, line.replace(',', '.').split())) for line in file]

cluster_1 = []
cluster_2 = []

for x, y in lst:
    if x < 1:
        cluster_1.append((x, y))
    else:
        cluster_2.append((x, y))

dot1, dot2 = find_min_distance(cluster_1, cluster_2)

Sx = (dot1[0] + dot2[0]) * 1000
Sy = (dot1[1] + dot2[1]) * 1000

print(int(Sx), int(Sy))
