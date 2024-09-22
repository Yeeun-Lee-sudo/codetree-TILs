n = int(input())
arr = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(arr[i])
    if i % 2 == 0:
        l.sort()
        print(l[i//2], end=" ")