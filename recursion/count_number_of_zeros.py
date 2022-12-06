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

def cont(n,total):

    rem=n%10
    if(rem==n):
        return total
    if(rem==0):
        return cont(n//10,total+1)
    return cont(n//10,total)

c=cont(50003070,0)
print(c)

# special example to return same value to above funcn calls