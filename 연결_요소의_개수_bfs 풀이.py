# *****문제조건***** 
#
# pypy3로는 통과, python3는 시간초과.
# 같은 간선은 한 번만 주어진다.
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)

import sys
from collections import deque
# 정점의 개수, 간선의 개수 입력
N,M=map(int,input().split())

# 정점 방문 여부 리스트
visited=[0]*(N+1)

# 간선 데이터 입력
# dic=dict()
L=deque()
for line in range(M):
    a,b=map(int,sys.stdin.readline().split())
    # dic[a]=b
    L.append((a,b))

queue=deque()
cnt=0
for i in range(1,N+1):

    # 이미 방문한 경우 건너뛴다.
    if visited[i]!=0:
        continue
    # i번 노드 방문처리, 카운트 증가, queue에 BFS용 원소 추가.
    visited[i]=1
    cnt+=1
    queue.append((0,i)) # 0은 아무런 영향도 주지 않는다.


    while queue:
        # 기준을 y로 잡는다.
        x,y=queue.popleft()
        connected_node=y

        # connected_node 와 연결된 모든 노드를 찾아서 큐에 집어넣고 방문처리.
        for a,b in L:
            if connected_node == a and visited[b]==0:
                queue.append((a,b))
                visited[b]=1
            elif connected_node==b and visited[a]==0:
                queue.append((b,a))
                visited[a]=1
            
        
    #     print(queue,'queue!')
    # print(visited,'visited!')
print(cnt)    
