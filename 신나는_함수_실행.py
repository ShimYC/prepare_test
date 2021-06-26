import sys

string=sys.stdin.readlines()

def w(a,b,c):
    if (a,b,c) in dic.keys():
        return dic[(a,b,c)]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            dic[(a,b,c)]=1
            return 1
        elif a > 20 or b > 20 or c > 20:
            dic[(a,b,c)]=w(20,20,20)
            return dic[(a,b,c)]
        elif a < b and b < c:
            dic[(a,b,c)]=w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dic[(a,b,c)]
        else:
            dic[(a,b,c)]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dic[(a,b,c)]

# for문 밖으로 빼면 한번 저장한 값을 다음 test case에서도 적용가능
dic={}

for i in string:
    a,b,c=map(int,i.split())
    
    if (a,b,c) == (-1,-1,-1):
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
        