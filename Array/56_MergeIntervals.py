intervals = [[1,3], [2,6], [8,10], [15,18]]

def solution(intervals):

    intervals.sort()   #O(n log n) - sorting
    i = 1 # use i-1 to find the 1st position

    while i < len(intervals):  #O(n), n is length of the intervals
        if intervals[i][0] <= intervals[i -1][1]:

            intervals[i -1][1] = max(intervals[i -1][1], intervals[i][1])

            intervals.pop(i)

        else:
            i +=1

    return intervals

print(solution(intervals))


#TC: O(n log n)
#SC: pythong sorting is like merge sort O(n)