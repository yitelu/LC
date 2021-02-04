
nums=[10, 5, 2, 6]
k = 100

def solution(nums, k: int) -> int:

    left = 0
    count = 0
    prod = 1 #any array number if only 1 number and it would be itself

    for right in range (len(nums)):
        prod *= nums[right]

        while prod >= k and left <= right:

            prod /= nums[left]
            left += 1

        count += right - left +1

    return count

print(solution(nums, k))

#TimeComplexity: two for loops, 0(N) -> num length

#SpaceComplexity: o(1) constant


