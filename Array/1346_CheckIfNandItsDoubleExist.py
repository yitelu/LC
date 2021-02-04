#nums = [10,2,5,3]
#nums = [7,1,14,11]
#nums = [3,1,7,11]
#nums = [-2,0,10,-19,4,6,-8] #false
#nums = [-20,8,-6,-14,0,-19,14,4]
nums = [0, 0] #true

def solution(nums):

    seen = set()

    for num in nums:
        if num *2 in seen or num / 2 in seen:
            return True
        seen.add(num)

    return False

print(solution(nums))