import sys
n=int(input())
L=[]
ans=[]
for i in range(n):
    a,b,c,d=sys.stdin.readline().rstrip().split() # input()보다 훨씬 빠름
    L.append((a,int(b),int(c),int(d)))  # 정확한 정렬을 위해 x를 int 형태로 바꿔주어야함
L.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in L:
    print(i[0])