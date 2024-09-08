a = input()
l = []

def moreThanTwo(string):
    for i in string:
        if i in l:
            continue
        else:
            l.append(i)
    if len(l)>=2:
        return "Yes"
    else:
        return "No"

print(moreThanTwo(a))