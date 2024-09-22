n = int(input())

def f(num):
    if num < 10:
        return num ** 2
    
    return f(num//10) + (num%10) ** 2

print(f(n))