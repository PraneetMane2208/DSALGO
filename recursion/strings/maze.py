def maze(r,c):
    if(r==1 or c==1):
        return 1
    left=maze(r-1,c)
    right=maze(r,c-1)
    return left+right

d=maze(5,5)
print(d)