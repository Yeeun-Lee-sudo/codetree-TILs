n, m, k = map(int, input().split())
l = []
for i in range(n):
    l.append(list(input()))

#print(l)

for i in range(n):
    for p in range(k):
        for j in range(m):
            #print("")
            print(l[i][j] * k, end="")
        print("")