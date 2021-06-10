import sys
N,card_number,M,card_to_find=int(input()),list(map(int,sys.stdin.readline().split())),int(input()),list(map(int,sys.stdin.readline().split()))

dic={}
for i in card_number:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
L=[]
for j in card_to_find:
    if j in dic.keys():
        L.append(dic[j])
    else:
        L.append(0)
print(*L)