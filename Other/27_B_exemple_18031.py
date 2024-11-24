def find_min_distance(cluster1, cluster2):
    min_distance = float('inf')
    closest_points = None

    for star1 in cluster1:
        for star2 in cluster2:
            distance = ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                closest_points = (star1, star2)

    return min_distance, closest_points

with open(fr"C:\Users\vladm\Downloads\27B_18031.txt") as file:
    lst = [tuple(map(float, line.replace(',', '.').split())) for line in file]

clusters = [[] for _ in range(5)]

for x, y in lst:
    if x > 13:
        clusters[0].append((x, y))
    elif y < 4 and x < 12:
        clusters[1].append((x, y))
    elif 9 > y > 6 and x < 12:
        clusters[2].append((x, y))
    elif 10 < y < 13 and x < 12:
        clusters[3].append((x, y))
    else:
        clusters[4].append((x, y))

min_distance = float('inf')
closest_pair = None

for i in range(len(clusters)):
    for j in range(i + 1, len(clusters)):
        distance, closest_points = find_min_distance(clusters[i], clusters[j])
        if distance < min_distance:
            min_distance = distance
            closest_pair = closest_points

point1, point2 = closest_pair
Sx = (point1[0] + point2[0]) * 1000
Sy = (point1[1] + point2[1]) * 1000

print(int(Sx), int(Sy))
