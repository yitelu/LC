arr = [17, 18, 5, 4, 6, 1]


def replaceElements(arr):

    #edge check
    if not arr:
        return []

    max_seen = 0
    curr_max = arr[-1]
    arr[-1] = -1

    for i in range(len(arr) -2, -1, -1):

        max_seen = max(arr[i], curr_max)
        arr[i] = curr_max
        curr_max = max_seen

    return arr

    arr.

print(replaceElements(arr))