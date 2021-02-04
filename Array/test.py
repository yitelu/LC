nums = [-4,-1,0,3,10]

'''
def twoPtr(nums):

        leftPtr=0
        rightPtr = len(nums)-1
        newList = []

        while leftPtr <= rightPtr:
            if nums[leftPtr]**2 > nums[rightPtr]**2:
                newList.append(nums[leftPtr]**2)
                leftPtr += 1
            else:
                newList.append(nums[rightPtr]**2)
                rightPtr -= 1
        return sorted(newList)

print(twoPtr(nums))
'''

'''
def solutions(nums):

	newList = [n**2 for n in nums]
	return sorted(newList)
'''

def addTwo(nums):

    return(sorted([n+2 for n in nums]))
    
print(addTwo(nums))

#print(solutions(nums))