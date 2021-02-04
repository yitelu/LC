# "continuous subarray" means it could be use for the two pointer

nums = [2,6,4,8,10,9,15]

def solution(nums):

    left = 0
    right = len(nums) -1
    subarray_min = float('inf')
    subarray_max = float('-inf')

    while left < right and nums[left] <= nums[left +1]:
        left += 1

    #edge check
    if left == right:
        return 0

    while right > 0 and nums[right] >= nums[right -1]:
        right -=1

    for i in range (left, right +1):
        subarray_min = min(subarray_min, nums[i])
        subarray_max = max(subarray_max, nums[i])

    while left > 0 and nums[left -1] > subarray_min:
        left -= 1

    while right < len(nums) -1 and nums[right +1 ] < subarray_max:
        right += 1

    return (right - left +1)

print(solution(nums))





