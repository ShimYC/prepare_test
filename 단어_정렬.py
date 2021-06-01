import sys
N=int(input())
_list=[]
for _ in range(N):
    _list.append(sys.stdin.readline().rstrip())
_list.sort(key=lambda x:(len(x),x))
for i in range(len(_list)):
    if i>0 and _list[i]==_list[i-1]:
        pass
    else:
        print(_list[i])