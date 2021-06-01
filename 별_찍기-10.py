def star(matrix,n,mode): # n=3^k
    if n<=9 and mode==1:
        return '*'
    elif n<=9 and mode==0:
        return ' '
    else:
        matrix


n=int(input())
matrix=[[] for i in range(n)]