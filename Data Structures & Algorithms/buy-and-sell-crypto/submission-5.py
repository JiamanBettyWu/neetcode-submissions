class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cheapest_so_far = None
        best = 0

        for p in prices:
            if cheapest_so_far is not None: cheapest_so_far = min(cheapest_so_far, p)
            else: cheapest_so_far = p

            profit = max(p - cheapest_so_far, 0)

            best = max(best, profit)
            print(f"{p} {cheapest_so_far}")
        
        return best 

