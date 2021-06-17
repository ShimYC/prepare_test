import sys
from collections import deque
X,Y=map(int,sys.stdin.readline().split())

# 지도 정보 구현
maps=[]
for i in range(X):
    maps.append(list(map(int,list(sys.stdin.readline().rstrip()))))

# BFS를 위한 큐 생성
queue=deque()

# 이동
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 처음위치 삽입
queue.append([0,0])

while queue: # 큐가 빌 때 까지

    # 현재 위치 추출
    x,y=queue.popleft()

    # 현재위치 기준 상,하,좌,우 4방향 탐색
    for i in range(4):
        # next x, next y 설정
        nx = x+dx[i]
        ny = y+dy[i]

        # 범위를 넘어간 경우 통과
        if nx<0 or ny<0 or nx>=X or ny>=Y:
            continue
        
        # 벽인 경우 통과
        if maps[nx][ny]==0:
            continue

        # 새로 방문한 지점인 경우 큐에 삽입
        if maps[nx][ny]==1:
            queue.append([nx,ny])
            maps[nx][ny]=maps[x][y]+1
        
        # 이전에 방문한 지점인 경우 BFS에서는 고려하지 않아도 됨

# 항상 도착가능한 경우만 주어지므로 (N, M)의 위치의 값을 출력하면 됨.
print(maps[X-1][Y-1])
