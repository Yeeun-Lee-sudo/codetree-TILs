n = int(input())
l = list(map(int, input().split()))

def size(l):
    for i in range(n):
        l[i] = abs(l[i])

size(l)
print(*l)