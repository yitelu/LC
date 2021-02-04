nums1 = [1,2,3,0,0,0]
m=3

nums2 = [2,5,6]
n=3


def solution(nums1, nums2):

    # use 3 pointer
    ptr_a = m -1
    ptr_b = n -1
    last = m+n -1

    #use ">=" because list index is to zero
    while ptr_a >=0 and ptr_b >= 0:

        if nums1[ptr_a] > nums2[ptr_b]:
            nums1[last] = nums1[ptr_a]
            ptr_a -= 1
        else:
            nums1[last] = nums2[ptr_b]
            ptr_b -= 1
        last -= 1

    #merge the rest of the nums2 into nums1 if it's not ready reaches it's end
    while ptr_b >= 0:
        nums1[last] = nums2[ptr_b]
        ptr_b -= 1
        last -= 1

    return(nums1)

print(solution(nums1, nums2))




