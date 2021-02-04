prices= [7, 1, 5, 3, 6, 4]

def solutions(prices):

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price- min_price)

    return max_profit

#TC O(N)
#SC: O(1)

    '''
        #brute force
        #TC O(N^2)

        max_profit= 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit
    '''

print(solutions(prices))