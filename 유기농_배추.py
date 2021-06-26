
import sys

T=int(input())
# M: 가로 길이, N: 세로 길이, K: 배추가 심어진 위치의 개수.
for t in range(T):
    M,N,K=map(int,input().split())
    maps=[[0]*M for _ in range(N)]
    L=[]

    # 초기 조건 설정
    for _ in range(K):
        Y,X=map(int,sys.stdin.readline().split())
        maps[X][Y]=1

    cnt=0
    for i in range(N): #행
        for j in range(M): # 열
        
            # 배추가 없거나 이미 고려한 경우 통과.
            if maps[i][j]==0 or maps[i][j]==-1:
                continue
        
            if maps[i][j]==1:
                L.append((i,j))
                maps[i][j]=-1
                while L:
                    x,y=L.pop()
                    if x>0 and maps[x-1][y]==1:
                        L.append((x-1,y))
                        maps[x-1][y]=-1
                    if y>0 and maps[x][y-1]==1:
                        L.append((x,y-1))
                        maps[x][y-1]=-1
                    if x+1<N and maps[x+1][y]==1:
                        L.append((x+1,y))
                        maps[x+1][y]=-1
                    if y+1<M and maps[x][y+1]==1:
                        L.append((x,y+1))
                        maps[x][y+1]=-1

            # DFS 끝나면 카운트 증가.
                cnt+=1
    print(cnt)
    