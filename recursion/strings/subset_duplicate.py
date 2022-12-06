def subset_dup(arr):
    outer=[[]]
    st=0
    end=0
    n=len(arr)
    for i in range(n):
        st=0
        if(i>0 and arr[i]==arr[i-1]):
            st=end+1
        end=len(outer)-1
        m=len(outer)
        for j in range(st,m):
            internal=outer[j]
            internal=internal+[arr[i]]
            outer=outer+[internal]
    return outer

arr=[1,2,2]
a=subset_dup(arr)
print(a)
