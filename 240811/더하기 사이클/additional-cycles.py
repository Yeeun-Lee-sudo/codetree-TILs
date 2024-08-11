n = int(input())
num = n
n1 = (num % 10) + (num // 10)
n2 = (num % 10) * 10 + (n1 % 10)
num = n2

ans = 1
while(True):
    if num == n:
        break
    
    n1 = (num % 10) + (num // 10)
    n2 = (num % 10) * 10 + (n1 % 10)
    num = n2
    ans += 1
    #print(num)

print(ans)