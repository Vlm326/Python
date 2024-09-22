import sys
sys.setrecursionlimit(1000000)
def f(n):
    if n <= 3:
        return 2025
    return 3 * (n - 1) * f(n - 2)
print(int(f(2027)/f(2023)))