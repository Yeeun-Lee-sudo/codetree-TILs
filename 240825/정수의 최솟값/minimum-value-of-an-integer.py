a, b, c = map(int, input().split())

def f(a, b, c):
    min = 200
    if a < min:
        min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min

print(f(a, b, c))