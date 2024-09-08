n = int(input())
l = []

l = list(map(int, input().split()))

def f(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

f(l)
print(*l)