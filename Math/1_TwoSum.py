

class Solution:

    nums =[2,7,11,3,6,1,33,4,8]
    target = 13

    def twoSum(nums, target):

        dict = {}

        for i in range(len(nums)):

            if nums[i] in dict:

                print(dict[nums[i]], i)

            else:
                #mark the other pair that would add up to be the total of 9
                #
                dict[target-nums[i]] = i

        print(dict)

    twoSum(nums, target)