c = list(input())
ch = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}
cl = ['+', '-', '*']
#print(c)
ans = -1000000

def calc():
    n = ch[c[0]]
    s = 0

    for i in c[1:]:
        if i in cl:
            match(i):
                case '+':
                    s = 1
                case '-':
                    s = 2
                case '*':
                    s = 3
        else:
            match(s):
                case 1:
                    n = n + ch[i]
                case 2:
                    n = n - ch[i]
                case 3:
                    n = n * ch[i]

    return n

def choose(cnt):
    global ans
    lists = ['a', 'b', 'c', 'd', 'e', 'f']

    if cnt == 6:
        ans = max(ans, calc())
        #print(ans)
        return

    for i in range(1, 5):
        ch[lists[cnt]] = i
        choose(cnt+1)
        ch[lists[cnt]] = 0
    return

choose(0)
print(ans)