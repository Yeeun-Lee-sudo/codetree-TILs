def prints(n):
    a = 1
    for i in range(n):
        for j in range(n):
            print(a, end=" ")
            a += 1
            if a == 10:
                a = 1
        print("")

n = int(input())
prints(n)