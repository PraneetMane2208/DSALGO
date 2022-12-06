def subseq(p,up):
    if(len(up)==0):
        list().append(p)
        return list
    ch=up[0]
    left=subseq(p+ch,up[1:])
    right=subseq(p,up[1:])

    left=left+right
    return left

c=subseq("","abc")
print(c)