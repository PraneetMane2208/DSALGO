# def fun(r,c):
#     if(r==0):
#         return
#     if(r>c):
#         print("*",end=" ")
#         fun(r,c+1)
#     else:
#         print('')
#         fun(r-1,0)
# d=fun(4,0)
# print(d)

def fun2(r,c):
    if(r==0):
        return
    if(r>c):

        fun2(r,c+1)
        print("*", end=" ")
    else:

        fun2(r-1,0)
        print('')
e=fun2(4,0)
print(e)