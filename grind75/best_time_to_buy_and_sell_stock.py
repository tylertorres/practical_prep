from math import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit by selling when the stock is higher than when bought
        profit = 0
        smallest_stock = math.inf

        for stock_price in prices:
            if stock_price < smallest_stock:
                smallest_stock = stock_price
            profit = max(profit, stock_price - smallest_stock)

        return profit






"""
[7,1,5,3,6,4]
[8, 3, 5, 7, 1, 6, 19]

[2,1]
B = 7
S = 1
P = 0

- No negative profits
- Everytime a smaller number is done, no extra processing done 
- if not smallest, check the current profit
1. Check if smaller
2. If not ; get the max (current profit, new_profit)
"""
