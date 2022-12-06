def permutations(p,up):
    if(len(up)==0):
        return 1


    ch=up[0]
    ans=0

    for i in range(0,len(p)):
        f=p[0:i]
        s=p[i:len(p)]
        ans=ans+permutations(f+ch+s,up[1:])
    return ans
    # return ans
a=permutations(" ","abc")
print(a)