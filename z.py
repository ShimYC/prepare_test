# 첫째 줄에 정수 N, r, c가 주어진다.
N,r,c=map(int,input().split())

# *****왜인지는 몰라도 이 문제는 0행 0열부터 센다.*****

# 직접 Z행렬을 구할 경우 아래와 같이 하면 됨.
# def dividing(x1,x2,y1,y2,st,cnt):
#     if x1==x2:
#         m[x1][y1]+=st
#         return
#     xmid=(x1+x2)//2
#     ymid=(y1+y2)//2
#     #1st
#     dividing(x1,    xmid,    y1,     ymid,    st,          cnt//4)
#     #2nd
#     dividing(x1,    xmid,    ymid+1,  y2,     st+cnt//4,   cnt//4)
#     #3rd
#     dividing(xmid+1, x2,     y1,     ymid,    st+2*cnt//4, cnt//4)
#     #4th
#     dividing(xmid+1, x2,     ymid+1,  y2,     st+3*cnt//4, cnt//4)

def dividing(r,c,x1,x2,y1,y2,st,cnt):
    if x1==x2:
        return st-1
    xmid=(x1+x2)//2
    ymid=(y1+y2)//2
    #1st
    if xmid>=r and ymid>=c:
        st=dividing(r,c,x1,    xmid,    y1,     ymid,    st,          cnt//4)
    #2nd
    elif xmid>=r and ymid<c:
        st=dividing(r,c,x1,    xmid,    ymid+1,  y2,     st+cnt//4,   cnt//4)
    #3rd
    elif xmid<r and ymid>=c:
        st=dividing(r,c,xmid+1, x2,     y1,     ymid,    st+2*cnt//4, cnt//4)
    #4th
    else:
        st=dividing(r,c,xmid+1, x2,     ymid+1,  y2,     st+3*cnt//4, cnt//4)
    return st

# 각 파트 시작 숫자.
st=1

# 각 파트의 개수
cnt=4**N

# 시작 index
x1=0
y1=0

# 끝 index
x2=2**N-1
y2=2**N-1

ans=dividing(r,c,x1,x2,y1,y2,st,cnt)
print(ans)