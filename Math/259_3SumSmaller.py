class Solution:

    nums = [-2, 0, 1, 3]
    target = 2

    def threeSumSmaller(nums, target):

        res =0

        nums.sort()

        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[right] < target -nums[i]:
                    res += right - left
                    left += 1
                else:
                    right -= 1

        print(res)

    threeSumSmaller(nums, target)
