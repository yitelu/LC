nums = [0,0,1,1,1,2,2,3,3,4]

def solution(num):

    prev = None
    ptr = 0

    for num in nums:
        if num != prev:

            nums[ptr] = num
            ptr += 1
            prev = num

    return ptr

print(solution(nums))


