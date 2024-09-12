n = int(input())

def upper(num):
    if num == 0:
        return
    
    print(n - num + 1, end=" ")
    upper(num-1)

def lower(num):
    if num == 0:
        return

    print(num, end=" ")
    lower(num-1)

upper(n)
print()
lower(n)