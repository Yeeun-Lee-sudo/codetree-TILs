n, m = map(int, input().split())
listA = list(map(int, input().split()))
listm = [[0, 0] for _ in range(m)]
for i in range(m):
    listm[i][0], listm[i][1] = map(int, input().split())

def f(pairs):
    
    for i in range(len(pairs)):
        ans = 0
        for j in range(pairs[i][0]-1, pairs[i][1]):
            ans += listA[j]
        print(ans)

f(listm)