def f(n):
    if n % 2 == 1:
        return "No"
    else:
        if ((n%10) + (n//10)) % 5 == 0:
            return "Yes"
        else:
            return "No"

n = int(input())
print(f(n))