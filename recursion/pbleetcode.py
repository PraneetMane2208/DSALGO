def merge(nums1, m, nums2, n):

    i = 0
    k = 0
    j = 0
    arr = []
    while (i < m and j < n):

        if (nums1[i] > nums2[j]):
            arr[k] = nums2[j]
            j += 1


        elif (nums1[i] <= nums2[j]):
            arr[k] = nums1[i]
            i += 1


        # else:
        #     arr[k] = nums1[i]
        #     k += 1
        #     arr[k] = nums2[j]
        #     i += 1
        #     j += 1
        k += 1
    while (i < m):
        arr[k] = nums1[i]
        k += 1
        i += 1
    while (j < n):
        arr[k] = nums2[j]
        k += 1
        j += 1

    return arr
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
a=merge(nums1,nums2,'3','3')
print(a)