def max_length(cluster1: list, cluster2: list):
    lst = []
    for star1 in cluster1:
        s = 0
        for star2 in cluster2:
            s += ((star1[0] - star2[0])**2 + (star1[1] - star2[1])**2)**0.5
            lst.append(s)
            s = 0
    return max(lst)
            
    return ans
def min_length(cluster1: list, cluster2: list):
    lst = []
    for star1 in cluster1:
        s = 0
        for star2 in cluster2:
            s += ((star1[0] - star2[0])**2 + (star1[1] - star2[1])**2)**0.5
            lst.append(s)
            s = 0
    return min(lst)

with open(fr"C:\Users\vladm\Downloads\27-21a.txt", "r") as file:
    trash = file.readline()
    lst = [tuple(map(float, line.replace(',','.').split())) for line in file]

cluster_1 = []
cluster_2 = []

for x, y in lst:
    if x < 5 and y < 6:
        cluster_1.append((x, y))
    if x > 5:
        cluster_2.append((x, y))


print(int(min_length(cluster_1, cluster_2) * 10000), int(max_length(cluster_1, cluster_2) * 10000))