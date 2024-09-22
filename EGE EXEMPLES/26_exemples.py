class exemples:
    def f8512(self) -> None:
        f = open('26_8512.txt')
        K = int(f.readline())
        N = int(f.readline())
        a = [list(map(int, i.split())) for i in f]
        a = sorted(a)
        kol_client = 0
        last_cell = 0
        cells = [0] * K
        for i in a:
            for j in range(len(cells)):  # отчистка ячеек от багажа, который уже забрали
                if i[0] >= cells[j]:
                    cells[j] = 0
                if 0 in cells:
                    last_cell = cells.index(0) + 1
                    cells[cells.index(0)] = i[1] + 1
                    kol_client += 1
        print(kol_client, last_cell)


def f9793(self) -> None:
    f = open('26_9793.txt')
    N = int(f.readline())
    detali = []
    lenta = [0] * 2 * N
    nomer = 0
    for i in f:
        b = list(map(int, f.readline().split()))
        nomer += 1
        if b[0] > b[1]:
            detali.append([b[1], 'O', nomer])
        else:
            detali.append([b[0], 'SH', nomer])
    detali = sorted(detali)
    for i in detali:
        if i[1] == 'SH':
            lenta[lenta.index(0)] = i
        else:
            for j in range(len(lenta) - 1, -1, -1):
                if lenta[j] == 0:
                    lenta[j] = i
                    break
    count = 0
    print(lenta)


def f163335(self) -> None:
    f = open('26_16335.txt')
    amount = int(f.readline())
    all_types = [int(x) for x in f]
    all_types.sort(reverse=True)
    ans = [all_types[0]]
    for i in all_types:
        if ans[-1] - i >= 4:
            ans.append(i)
    print(len(ans), ans[-1])


def f9847(self) -> None:
    # https://www.youtube.com/watch?v=FSOOYbL-Z3k
    f = open('26_9847 (1).txt')
    n = int(f.readline())
    a = {}
    for i in range(n):
        x1, x2 = [int(x) for x in f.readline().split()]
        a[x1] = 1 if x1 not in a else a[x1] + 1
        a[x2] = -1 if x2 not in a else a[x2] - 1

    a = dict(sorted(a.items()))
    people_inside = [0]
    for k in a:
        if a[k] != 0:
            people_inside.append(people_inside[-1] + a[k])
    print(people_inside.count(max(people_inside)), max(people_inside))


def f9793(self) -> None:
    f = open('26_9793.txt')
    n = int(f.readline())
    details = []
    lent = [0] * n
    last = 0
    count_shl = 0
    for i in range(n):
        shl, okr = map(int, f.readline().split())
        if shl < okr:
            details.append([shl, 'shl', i + 1])
        else:
            details.append([okr, 'okr', i + 1])
    details.sort()
    for i in range(n):
        time, type, num = details[i]
        if type == 'shl':
            lent[lent.index(0)] = i
            last = num
            count_shl += 1
        else:
            for j in range(n - 1, -1, -1):
                if lent[j] == 0:
                    lent[j] = i
                    last = num
                    break

    print(f'last: {last}, last shl: {count_shl - 1}')

def f8512(self) ->None:
    # https://www.youtube.com/watch?v=XjbnBvx0zAw
    f = open('26_8512.txt')
    k = int(f.readline())
    n = int(f.readline())
    a = []
    for i in range(n):
        start, end = map(int, f.readline().split())
        a.append([start, end])
    lastcell = 0
    a.sort()
    count = 0
    cell = [-1] * k
    for i in range(n):
        start, end = a[i]
        for j in range(k):
            if start >= cell[j] + 1:
                cell[j] = end
                count += 1
                lastcell = j + 1
                break

    print(count, lastcell)
def f4205(self) -> None:
    f = open('26_4205.txt')
    n = int(f.readline())
    ps = [[int(x) for x in f.readline().split()] for _ in range(n)]
    ps.sort(key=lambda x: (-x[0], x[1]))
    for a, b in zip(ps, ps[1:]):
        if a[0] == b[0] and b[1] - a[1] == 14:
            print(a[0], a[1] + 1)
            break



