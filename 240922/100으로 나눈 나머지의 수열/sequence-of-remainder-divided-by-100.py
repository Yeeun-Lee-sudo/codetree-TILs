n = int(input())

def arr(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return arr(n-2) * arr(n-1) % 100

print(arr(n))