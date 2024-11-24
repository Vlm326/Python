def divisers(n):
    new_set = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            new_set.add(i)
            new_set.add(n // i)
    return sorted(new_set)

for i in range(1000):
    if len(divisers(i)) == 7:
        print(i, divisers(i))
        
#while True:
#    i = int(input('Введите число: '))
#    print(divisers(i), len(divisers(i)))