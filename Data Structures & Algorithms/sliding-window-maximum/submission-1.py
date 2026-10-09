class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        res = []

        for i, n in enumerate(nums):

            while (len(dq) > 0) and (nums[dq[-1]] <= n):
                dq.pop()

            dq.append(i)

            if i + 1 >= k:
                res.append(nums[dq[0]])
            
            if i - k + 1 >= dq[0]:
                dq.popleft()

        return res

        
