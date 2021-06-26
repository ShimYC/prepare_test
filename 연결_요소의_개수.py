## pypy3 는 통과, python3는 시간초과 나옴.

import sys
# 정점의 개수, 간선의 개수 입력
N,M=map(int,input().split())

# 정점 방문 여부 리스트
visited=[0]*(N+1)

# 간선 데이터 입력
L=[]
for line in range(M):
    a,b=map(int,sys.stdin.readline().split())
    # dic[a]=b
    L.append((a,b))

stack=[]
cnt=0
for i in range(1,N+1):
    
    # 이미 방문했던 노드인 경우 통과.
    if visited[i]==1:
        continue
    
    # 탐색을 시작할 노드를 스텍에 넣고 방문처리
    stack.append(i)
    visited[i]=1

    # 새로운 연결요소의 시작이므로 카운트 증가.
    cnt+=1
    
    while stack: # 스텍이 비어있지 않은 동안

        # 스텍에서 하나의 노드를 빼서
        x=stack.pop()

        # 그 노드와 인접하면서 방문한적 없는 노드를 모두 스텍에 넣는다.
        dellist=[]
        for a,b in L:
            if a==x and visited[b]==0:
                stack.append(b)
                visited[b]=1
                dellist.append((a,b))
            elif b==x and visited[a]==0:
                stack.append(a)
                visited[a]=1
                dellist.append((a,b))

        # 고려가 끝난 간선은 제거
        while dellist:
            L.remove(dellist.pop())

        # 스텍이 비면 모든 연결노드를 탐색한것이 됨.

print(cnt)