nums = [1, 0, -1, 0, -2, 2]
target=0

def solution(nums, target):

    nums.sort()

    length = len(nums)
    res = []

    #edge check

    if length < 4:
        return []

    #-3 for the j and L & R pointer
    for i in range (0, length -3):
        if i > 0 and nums[i] == nums[i -1]:
            continue

        #-2 for the L and R pointer
        for j in range (i +1, length -2 ):
            if j > i +1 and nums[j] == nums[j - 1]:
                continue
            left = j +1
            right = length -1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left +1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -=1
                    left += 1
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return res


print(solution(nums, target))