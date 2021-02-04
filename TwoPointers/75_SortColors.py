
num= [2, 0, 2, 1, 1, 0]

def solution(num):

    left =0
    right = len(num)-1
    i=0

    while i<=right:
        if num[i] == 0:
            num[i], num[left] = num[left], num[i]
            i += 1
            left += 1
        elif num[i] == 2:
            num[i], num[right] = num[right], num[i]
            right -=1
        else:
            i += 1

    return(num)

print(solution(num))

#TC: O(N)
#SC: O(1) constant due to no data structure