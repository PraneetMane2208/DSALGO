def subset_str(p,up):
    if(len(up)==0):
        print(p)
        return

    cha=up[0]
    subset_str(p+cha,up[1:])
    subset_str(p,up[1:])



c=subset_str(" ","abc")
print(c)