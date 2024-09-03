a, b = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def sumOfPrime(num1, num2):
    sum = 0
    for i in range(num1, num2+1):
        if isPrime(i):
            sum += i
    
    return sum 

print(sumOfPrime(a, b))