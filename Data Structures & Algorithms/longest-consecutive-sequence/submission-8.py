class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        used = set()
        count, best = 0, 0

        for n in nums_set:
            if n not in used:
                used.add(n)
                count+=1
                follow = n + 1
                while follow in nums_set:
                    used.add(follow)
                    count+=1
                    follow+=1
                best = max(count, best)
                count = 0
        
        return best