class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0
        for p in prices:
            profit = max(p - lowest, profit)
            lowest = min(p, lowest)
        
        return profit

            

            
