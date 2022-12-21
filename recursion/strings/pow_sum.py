
def pow(target,index,):

    if (target == 0):
        # print(" 1", end=" ")
        return 1


    if (target < 0):
        return
    j=index
    while((target -j**2>=0)):

        total+= pow(target - j ** 2,index+1,total)
        j+=1
    return total

            # global count+=1



    # for j in range(i,target):
    #     if(i**2 >target):
    #         return
    #     if(target==0):
    #         count+=1
    #         return
    #     return pow(target-i**2,i,count)
    #
    # return count

a=pow(100,1,0)
print(a)