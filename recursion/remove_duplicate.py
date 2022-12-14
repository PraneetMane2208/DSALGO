# def remove(arr,d):

#     if(len(arr)<2):
#         return d+str(arr)
#
#     if(arr[0]==arr[1]):
#         return remove(arr[1:],d)
#     else:
#
#         return remove(arr[1:],d+str(arr[0]))
#     # d.append(arr)
# arr="aaaabbb"
# a=remove(arr,"")
# print(a)

# def substring(p,up):
#     if(len(up)==0):
#         print(p)
#         return
#     substring(p+up[0],up[1:])
#     substring(p,up[1:])
# c=substring("","abc")
# # print(c)

def sub(arr):
    i=1
    j=1
    while(i<=len(arr)):
        j=1
        while(j<=len(arr)):
            print(arr[0:j])
            j+=1
        arr=arr[i:]
        i=0
        i+=1
c=sub("abc")

