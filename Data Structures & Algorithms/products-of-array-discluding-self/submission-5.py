class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        prefix = []
        suffix = []
        for i, n in enumerate(nums):
            pre_v = prefix[i-1] * nums[i-1] if i != 0 else 1
            prefix.append(pre_v)

            suf_v = suffix[i-1] * nums[-i] if i != 0 else 1
            suffix.append(suf_v)

        suffix = suffix[::-1]
        return [a * b for a, b in zip(prefix, suffix)]