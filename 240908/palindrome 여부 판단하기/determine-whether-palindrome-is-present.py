arr = input()

def f(st):
    for i in range(len(st)):
        if not st[i] == st[len(st)-1-i]:
            return "No"
    return "Yes"

print(f(arr))