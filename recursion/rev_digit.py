rev_num=0
def reverse_num(n):
    global rev_num
    if(n>0):
        rem=n%10
        rev_num=(rev_num*10)+rem
        reverse_num(n//10)
    return rev_num

c=reverse_num(121)
print(c)