from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = deque()
        res = []
        for i in range(len(nums)):
            while dp and (nums[i] > nums[dp[-1]]):
                dp.pop()

            dp.append(i)

            if i >= k-1:
                res.append(nums[dp[0]])
            
            # prep for next iter
            if dp[0] < i-k+2:
                dp.popleft()
        
        return res





