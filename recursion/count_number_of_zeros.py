count=0
def count_zeros(n):
    global count
    if(n>0):
        rem=n%10
        if(rem==0):
            count+=1
        count_zeros(n//10)
    return count
c=count_zeros(204507000)
print(c)