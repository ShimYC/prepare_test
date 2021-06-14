import sys
N,M=map(int,input().split())
Nset=set()
Mset=set()
for i in range(N):
    Nset.add(sys.stdin.readline().rstrip())
for j in range(M):
    Mset.add(sys.stdin.readline().rstrip())

final_set:set = Nset & Mset

final:list = sorted(list(final_set))
print(len(final))
for k in final:
    print(k)