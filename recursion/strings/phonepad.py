def phonepad(p,up):
    if (len(up) == 0):

        # list=[]
        # list.append(p)
        print(p)
        return 1
    digit= int(int(up[0]))
    count=0
    for i in range((digit-1)*3,digit*3):
        ch=chr(ord('a')+i)
        count=count+phonepad(p+ch,up[1:])
    return count

a=phonepad("","1234")
print(a)