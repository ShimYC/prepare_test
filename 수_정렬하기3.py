import sys
n=int(input())
_list=[0 for _ in range(10000)]
for i in range(n):
    _list[int(sys.stdin.readline().rstrip())-1]+=1
for j in range(10000):
    if _list[j]==0:
        pass
    else:
        for k in range(_list[j]):
            print(j+1)