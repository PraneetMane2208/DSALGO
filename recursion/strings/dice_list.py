def dice_list(p,target):
    if(target==0):
        list=[]
        list.append(p)
        return list
    i=1
    ans=[]
    while(i<=6 and i<=target):
        ans = ans + dice_list(p + str(i), target - i)
        i+=1
    return ans


d=dice_list("",4)

print(d)