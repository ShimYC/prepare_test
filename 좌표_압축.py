import sys
N=int(input()) #전체 개수

a=list(map(int,sys.stdin.readline().split()))
b=list(set(a))
b.sort()
dic={}
_list=[]
for i in range(len(b)):
    dic[b[i]]=i
for j in a:
    _list.append(dic[j])
print(*_list)