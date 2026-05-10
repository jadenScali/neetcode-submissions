class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0

        for j in range(len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
        
        return max_profit