n, k, t = input().split()
n = int(n)
k = int(k)
arr = []
for i in range(n):
    arr.append(input())

arr.sort()
cnt = 0
for i in range(n):
    if t == arr[i][:len(t)]:
        cnt += 1
        
    if cnt == k:
        print(arr[i])
        break