def mypow(x,n):
    if(n==0):
        return 1
    if(n<0):
        return float(1/x) * mypow(x,n+1)
    if(n>0):
        return float(x * mypow(x,n-1))

c=mypow(2.0,-4)
print(c)
print(float(1.000/4))