# modify "the input array in-place" means use "pointer"


nums = [3,2,2,3]
val = 3

def solution(nums):

    ptr = 0

    for num in nums:
        if num != val:
            nums[ptr] = num
            ptr += 1

    return(nums)

print(solution(nums))

