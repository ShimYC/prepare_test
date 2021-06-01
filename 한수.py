def han_number(n):
    ans=99
    if n<100:
        return n
    else:
        for i in range(100,n+1):
            i_str=str(i)
            k=len(str(i))
            j=0
            while j<k-1:
                det=int(i_str[j])-int(i_str[j+1])
                if j>0 and det!=det2:
                    break
                det2=det
                j+=1
                if j==k-1:
                    ans+=1
        return ans

print(han_number(int(input())))