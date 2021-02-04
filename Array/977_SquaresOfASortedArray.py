#nums = [-4,-1,0,3,10]
nums = [-7, -3, 2, 3, 11]

#generator solution



def solution(nums):

    newNums = (n ** 2 for n in nums)
    myList = list(newNums)
    myList.sort()
    return myList

print(solution(nums))


'''

#TC: N log N -> O(N)
#SC: O(N)


#two pointer solutions:

def solutions(nums):

    leftptr = 0
    rightptr = len(nums)-1
    newList = []

    while leftptr <= rightptr:

        leftValue = nums[leftptr] ** 2
        rightValue = nums[rightptr] ** 2

        if leftValue > rightValue:
            newList.append(leftValue)
            leftptr += 1
        else:
            newList.append(rightValue)
            rightptr -= 1


    newList.sort()
    return newList

print(solutions(nums))

#use two-pointer
#the TC: O(N)
#the SC: O(N)

'''