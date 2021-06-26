comp=int(input())
link=int(input())
visited=[0]*(comp+1)
L=[]
for _ in range(link):
    a,b=map(int,input().split())
    L.append((a,b))

stack=[1]
visited[1]=1
cnt=-1
while stack:
    x=stack.pop()
    cnt+=1
    for a,b in L:
        if a==x and visited[b]==0:
            stack.append(b)
            visited[b]=1
        elif b==x and visited[a]==0:
            stack.append(a)
            visited[a]=1
print(cnt)