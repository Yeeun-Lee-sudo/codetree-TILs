target = list(input()) #알파벳단위 list는 split 사용 x
find =  list(input())

def findIndex(slist):
    #print(slist)
    cnt = 0
    for i in range(len(target) - len(slist)+1): # +1 안해주면 탐색 범위에서 하나가 배제된다 
        #print(target[i], slist[0])
        if target[i] == slist[0]:
            cnt += 1
            #print(i)
            for j in range(1, len(slist)):
                #print(i, j)
                if not target[i+j] == slist[j]:
                    i = i + j
                    cnt = 0
                    break
                cnt += 1
            if cnt == len(slist):
                return i
    return -1

print(findIndex(find))