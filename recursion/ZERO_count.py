count=0
def count_zero(n):
    global count
    if(n%10==n):
        return count
    rem=n%10
    if(rem==0):
        count+=1
        return count_zero(n // 10)
    else:
        return count_zero(n // 10)

a=count_zero(1200030340890)
print(a)
