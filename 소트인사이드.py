a=input()
C_list=[0 for _ in range(10)]
for i in a:
    C_list[int(i)]+=1
ans=''
for j in range(10):
    if C_list[j]!=0:
        for k in range(C_list[j]):
            ans=str(j)+ans
print(ans)