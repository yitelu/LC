A = [3, 1, 2, 4]

def sortArrayByParity(A):

    #edge check
    if not A:
        return []

    ptr = 0

    for i in range(len(A)):

        if A[i] % 2 == 0:
            A[ptr], A[i] = A[i], A[ptr]
            ptr += 1

    return A

print(sortArrayByParity(A))

#TC: O(n) due to n length of A
#SC: O(1)