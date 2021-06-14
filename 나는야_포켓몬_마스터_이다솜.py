import sys
N,M=map(int,input().split())
# N:포켓몬 개수
# M:문제 개수

# ^ o^)ㅗ "쓸데없이 서론이 긴 문제네요 ㅎㅎ~"
name=dict()
num=dict()
for i in range(1,N+1):
    p_name=sys.stdin.readline().rstrip()
    name[i]=p_name
    num[p_name]=i
for j in range(M):
    problem=sys.stdin.readline().rstrip()
    if problem.isdigit():
        print(name[int(problem)])
    else:
        print(num[problem])