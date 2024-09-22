n = int(input())

def f(n):
    if n == 2:
        return 2
    if n == 1:
        return 1

    return n + f(n-2)

print(f(n))