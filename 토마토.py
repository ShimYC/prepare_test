# BFS를 위해 deque를 import
from collections import deque
import sys
# 상자 크기 입력
# 2 <= M,N <= 1000 이므로 맵 전체를 점검하는데 최대 1백만번 연산 필요. but, 한번만 하면 되서 상관없음.
M,N=map(int,input().split()) # M이 가로, N이 세로

# 상자조건 입력
maps=[]
for m in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))

# 날짜 초기화
day=0

# 큐 생성
queue=deque()

#초기조건
for i in range(M): # 열
    for j in range(N): # 행
        if maps[j][i]==1:
            queue.append((j,i))

# 큐에 뭔가 들어가있으면(=익은 토마토가 존재하면) day-=1 해줘야함. (마지막 popleft에 day+=1 되는거 보정)            
if queue:
    day-=1

# BFS 
while queue:
    qlen=len(queue)
    for pop in range(qlen):

        j,i=queue.popleft()
        # 위쪽
        if j-1>=0 and maps[j-1][i]==0:
            maps[j-1][i]=1
            queue.append((j-1,i))

        # 아래쪽
        if j+1<=N-1 and maps[j+1][i]==0:
            maps[j+1][i]=1
            queue.append((j+1,i))

        # 왼쪽
        if i-1>=0 and maps[j][i-1]==0:
            maps[j][i-1]=1
            queue.append((j,i-1))
    
        # 오른쪽
        if i+1<=M-1 and maps[j][i+1]==0:
            maps[j][i+1]=1
            queue.append((j,i+1))
    
    # 진행 확인용 출력
    # for a in maps:
    #     print(a)
    # print()

    # 하루가 지났습니다.....
    day+=1

# 작업 끝나고 익지 않은 토마토가 있는지 확인.
# 처음부터 아무 토마토도 익지 않은 경우 BFS를 생략하고 여기에서 -1로 변환됨
for i in range(M): # 열
    for j in range(N): # 행
        if maps[j][i]==0:
            day=-1
            break
            
# 정답 출력
print(day)

