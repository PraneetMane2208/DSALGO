# sum=0
# def palindrome(n):
#     temp=n
#     global sum
#     if(n>0):
#         rem=n%10
#         sum=sum*10+rem
#         palindrome(n//10)
#     return sum
# def checK(n):
#     a=palindrome(n)
#     if (a==n):
#         print("palindrome")
#
#     print("no")
# c=checK(222)
# print(c)

rev_num=0
def reverse_num(n):
    global rev_num
    if(n>0):
        rem=n%10
        rev_num=(rev_num*10)+rem
        reverse_num(n//10)
    return rev_num
def bool(n):
    return n==reverse_num(n)
c=bool(121)
print(c)