
def sum_of_digit(n):

    if(n==0):
        return 0

    return n%10+int(sum_of_digit(n/10))
c=sum_of_digit(2323)
print(c)

# def product_of_digit(n):
#
#     if(n%10==n):
#         return n
#
#     return n%10*int(sum_of_digit(n/10))
# d=product_of_digit(1342)
# print(d)