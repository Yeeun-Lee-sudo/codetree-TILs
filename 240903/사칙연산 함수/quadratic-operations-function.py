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

print("%d %c %d = " %(a, o, c), end="")
if o == "+":
    print(plus(a, c))
elif o == "-":
    print(minus(a, c))
elif o == "*":
    print(multiply(a, c))
elif o == "/":
    print(divide(a, c))
else:
    print("False")