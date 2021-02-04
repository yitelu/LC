nums = [1,0,2,3,0,4,5,0]

def solution(nums):

    length = len(nums)

    i =0

    while i < len(nums):

        if nums[i] != 0:
            i += 1
        elif nums[i] == 0:
            nums.insert(i+1, 0)
            i += 2
            nums.pop()

    print(nums)

solution(nums)