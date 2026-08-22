class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = 0 

        b, s = 0, 1
        while s < len(prices):
            if prices[b] < lowest: lowest = prices[b]

            if prices[b] > prices[s]:
                b+=1
                s+=1
            else:
                p = prices[s] - prices[b]
                profit = max(profit, p)
                s+=1

            if (s < len(prices)) and (prices[s] <= lowest):
                b = s
                s+=1
        return profit
            

            
