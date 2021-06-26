import sys
N=input()
M= sys.stdin.readlines()
maps=[]
for i in M:
    maps.append(i.split())
    
x1=0
x2=len(maps)-1
y1=0
y2=len(maps)-1

def sol(x1,x2,y1,y2):
    if x1==x2:
        return maps[x1][y1]
    # 0123 4567
    
    # q2|q1
    # q3|q4

    q2=sol( x1   ,          (x1+x2)//2,      y1,            (y1+y2)//2)
    q3=sol((x1+x2)//2+1,     x2,             y1,            (y1+y2)//2)
    q1=sol( x1,             (x1+x2)//2,     (y1+y2)//2+1,    y2       )
    q4=sol((x1+x2)//2+1,     x2,            (y1+y2)//2+1,    y2       )

    # 프로그래머스 문제에서도 그랬지만, (q1=='1' or q1=='0')부분이 핵심.
    if q1==q2 and q2==q3 and q3==q4 and (q1=='1' or q1=='0'):
        return q1
    else:
        return q1+q2+q3+q4
string:str=sol(x1,x2,y1,y2)
print(string.count('0'))
print(string.count('1'))