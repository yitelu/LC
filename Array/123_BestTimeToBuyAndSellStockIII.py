prices = [3,3,5,0,0,3,1,4]

def solution(prices):

    low_buy1 = float('inf')
    profit1 = 0
    low_buy2 = float('inf')
    profit2 = 0

    for price in prices:
        low_buy1 = min(low_buy1, price)
        profit1 = max(profit1, price - low_buy1)

        low_buy2 = min(low_buy2, price - profit1)
        profit2 = max(profit2, price - low_buy2)

    return profit2

print(solution(prices))

#TC: O(n) , n is length of prices

#SC: O(1), constant, no new data structure.

