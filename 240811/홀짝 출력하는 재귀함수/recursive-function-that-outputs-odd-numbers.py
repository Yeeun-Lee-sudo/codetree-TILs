n = int(input())

def p(n):
    if n%2 == 1:
        for i in range(1, n+1, 2):
            print(i, end=" ")
    else:
        for i in range(2, n+1, 2):
            print(i, end=" ")

p(n)