#27889
f = open('27-B_demo (1).txt')
n = int(f.readline())
a = [list(map(int, i.split())) for i in f]
summ = 0
raznost = []
for i in a:
    summ += min(i)
    if (max(i) - min(i)) % 3 != 0:
        raznost.append(max(i) - min(i))
if summ % 3 != 0:
    print(summ)
else:
    print(summ + min(raznost))

#b 200157478


#27424
f = open('27-A_demo.txt')
n = f.readline()
a = [list(map(int,i.split())) for i in f]
raznosti = []
summa = 0
for i in a:
    summa += max(i)
    if (max(i) - min(i)) % 3 != 0:
        raznosti.append(max(i) - min(i))
if summa % 3 != 0:
    print(summa)
else:
    print(summa - min(raznosti))
#b 399762080
#a 127127


#9848
f = open('27_B_9848.txt')
K = int(f.readline())
N = int(f.readline())
a = [int(x) for x in f]
a_summs = []
summa = 0
min_back = 100**10000
for i in a:
    summa += i
    a_summs.append(summa)
max_ocenka = 0
for i in range(K+1,len(a_summs)):
    min_back = min(min_back, a_summs[i - K - 1])
    max_ocenka = max(max_ocenka, a_summs[i] - min_back)
print(max_ocenka)

