nums = [2, 7, 11, 15]
target = 9

def twoSumII(nums, target):

    Left = 0
    Right = len(nums)-1

    while Left < Right:

        if nums[Left] + nums[Right] == target:
            return (Left+1, Right+1)

        elif nums[Left] + nums[Right] > target:
            Right -=1
        else:
            Left +=1

print(twoSumII(nums, target))
