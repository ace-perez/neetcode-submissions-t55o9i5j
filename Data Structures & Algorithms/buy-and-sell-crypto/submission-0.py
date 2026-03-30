class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        if len(prices) == 1:
            return 0

        left, right = 0, 1
        profit_max = 0

        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            profit_max = max(profit_max, cur_profit)

            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                right += 1
 

        return profit_max

