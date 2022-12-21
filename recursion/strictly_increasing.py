def increasing(n,st,res):
    if(n==0):
        print(res)
        return
    for i in range(st,10):
        val=res+str(i)
        increasing(n-1, i+1,val)


a=increasing(2,1,"")