i=0
def permutations(p,up):
    if(len(up)==0):
        # list=[]
        # list.append(p)
        print(p)
        return
    ch=up[0]
    # ans=[]

    for i in range(0,len(p)):
        f=p[0:i]
        s=p[i:len(p)]
        permutations(f+ch+s,up[1:])
        # i+=1
    # return ans
a=permutations(" ","abc")
# print(a)