n1, n2, n3 = map(int, input().split())

def ans(num):
    if num < 10:
        return num 
    return ans(num // 10) + (num % 10)

print(ans(n1*n2*n3))