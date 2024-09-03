import sys
def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 // num2

a, o, c = input().split()
a = int(a)
c = int(c)


if o == "+":
    ans = plus(a, c)
elif o == "-":
    ans = minus(a, c)
elif o == "*":
    ans = multiply(a, c)
elif o == "/":
    ans = divide(a, c)
else:
    print("False")
    exit()

print("%d %c %d = %d" %(a, o, c, ans), end="")