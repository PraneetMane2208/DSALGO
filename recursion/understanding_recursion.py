# def message():
#     print("Hello AWorld")
#     message1()
# def message1():
#     print("Hello BWorld")
#     message2()
#     print("praneet")
# def message2():
#     print("Hello CWorld")
#     message3()
# def message3():
#     print("Hello DWorld")
#     print("pavan")
# a=message()
# print(a)


# def printnum(n):
#     if(n==1):
#         print(n)
#         return
#
#     printnum(n-1)
#     print(n)
# a=printnum(6)
# print(a)

def fibbonaci(n):
    if n > 2:
        return fibbonaci(n - 1) + fibbonaci(n - 2)
    else:
        return 1


a = fibbonaci(4)
print(a)
