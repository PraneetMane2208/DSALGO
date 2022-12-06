# for i in range(4):
#     print('#'*(4-i))
def pattern(r,c):
    if(r==0):
        return
    if(r>c):
        print("#",end=" ")
        pattern(r,c+1)
    else:
        print()
        pattern(r-1,0)

def pattern1(r,c):
    if(r==0):
        return
    if(r>c):

        pattern1(r,c+1)
        print("#", end=" ")
    else:

        pattern1(r-1,0)
        print()


def bubble(arr,r,c):
    if(r==0):
        return
    if(r>c):
        if(arr[c]>arr[c+1]):
            temp=arr[c]
            arr[c]=arr[c+1]
            arr[c+1]=temp
        bubble(arr,r,c+1)
    else:
        bubble(arr,r-1,0)
    return arr


def selection(arr,r,c,max):
    if(r==0):
        return
    if(r>c):
        if(arr[c]>arr[max]):
            selection(arr,r,c+1,c)
        else:
            selection(arr,r,c+1,max)
    else:
        temp=arr[max]
        arr[max]=arr[r-1]
        arr[r-1]=temp
        selection(arr,r-1,0,0)
    return arr

# arr=[4,3,2,1]
arr=[3,1,5,2,4]
# a=pattern(4,0)
# b=pattern1(4,0)
# c=bubble(arr,3,0)
d=selection(arr,5,0,0)
# print(a)
# print(b)
# print(c)
print(d)