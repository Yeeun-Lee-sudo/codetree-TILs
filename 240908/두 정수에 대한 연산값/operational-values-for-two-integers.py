a, b = map(int, input().split())

def f(a, b):
    if a >= b:
        a = a + 25
        b = b * 2
    else:
        b = b + 25
        a = a * 2
    
    return a, b

a, b = f(a, b)
print(a, b)