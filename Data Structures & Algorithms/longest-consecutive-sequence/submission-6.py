class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if not nums_set:
            return 0

        longest = 1
        for num in nums_set:
            prev = num - 1
            if prev in nums_set:
                continue
            
            current = num
            count = 0
            while current in nums_set:
                count+=1
                current+=1
                if count > longest:
                    longest = count                   

        return longest


