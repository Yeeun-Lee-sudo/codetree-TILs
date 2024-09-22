n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = 0
for i in range(n):
    temp = arr[i] + arr[len(arr)-1-i]
    if temp > m:
        m = temp
    
print(m)