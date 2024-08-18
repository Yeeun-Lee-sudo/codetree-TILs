n = int(input())
a = 0

for i in range(n):
    a = i+1
    for j in range(n):
        print(a, end=" ")
        a = a * 2
    print()