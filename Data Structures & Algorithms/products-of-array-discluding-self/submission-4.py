class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        prefix = []
        suffix = []
        for i, n in enumerate(nums):
            prefix.append(math.prod(nums[:i])) 
            suffix.append(math.prod(nums[i+1:]))

        return [a * b for a, b in zip(prefix, suffix)]