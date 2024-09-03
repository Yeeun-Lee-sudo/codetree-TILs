n1, n2 = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def isPart(cnt, l1i):
    #print(cnt, l1i)
    if cnt == n2-1:
        print("Yes")
        return True
    elif l1i == n1-1:
        print("No")
        return False

    if l1[l1i] == l2[cnt]:
        isPart(cnt+1, l1i+1)
    else:
        isPart(0, l1i+1)

isPart(0, 0)