s=input()
new=''
ans=''
stack=0
mode=0 # 0 :삭제모드 1: 입력모드
breaking=1
for i in s:
    if i !='0':
        breaking=0
        break
for i in s:
    if breaking==1:
        new='0'
        break
    if i=='0' and mode==0:
        pass
    elif i=='0' and mode==2:
        new+=i
        mode=0
    elif i=='0' and mode==1:
        new+=i
    elif i!='0' and i!='+' and i!='-': #숫자인 경우
        if len(new)>1 and new[-1]=='0':
            if new[-2]=='-' or new[-2]=='+':
                new=new[:-1]
        new+=i
        mode=1
    elif i=='+' or i=='-':
        new+=i
        mode=2
#print(new)
for j in new:
    if j!='-':
        ans+=j
    elif j=='-' and stack==0:
        ans+='-('
        stack=1
    elif j=='-' and stack==1:
        ans+=')-('
if stack==1:
    ans+=')'
#print(ans)
print(eval(ans))