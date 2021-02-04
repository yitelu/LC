height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trap(height):

    water = 0
    peak_idx =0
    left_most_bar =0
    right_most_bar = 0

    for i in range (len(height)):
        if height[i] > height[peak_idx]:
            peak_idx = i

    for i in range(peak_idx):
        if height[i] > left_most_bar:
            left_most_bar = height[i]
        else:
            water = water + left_most_bar - height[i]

    for i in range(len(height) -1, peak_idx -1, -1):
        if height[i] > right_most_bar:
            right_most_bar = height[i]
        else:
            water = water + right_most_bar - height[i]

    return water

print(trap(height))