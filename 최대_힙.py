import sys
import heapq
N=int(input())
L=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        if len(L)==0:
            print(0)
        else:
            print('ans!',-heapq.heappop(L))
    else:
        heapq.heappush(L,-num)

