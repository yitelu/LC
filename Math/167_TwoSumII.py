#two pointer

#Easy:
#starting question


"""
class Solution:

    nums =[2,7,11,15]
    target = 9

    def twoSum(nums, target):

        dict = {}

        for i in range(len(nums)):

            if nums[i] in dict:

                print(dict[nums[i]]+1, i+1)

            else:
                #mark the other pair that would add up to be the total of 9
                #
                dict[target-nums[i]] = i

        print(dict)

    twoSum(nums, target)
"""
nums = [2, 7, 11, 15]
target = 9


def twoSumII(nums, target):

    L = 0
    R = len(nums)-1

    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        elif nums[L] + nums[R] == target:
            print(L+1, R+1)
            break

twoSumII(nums, target)