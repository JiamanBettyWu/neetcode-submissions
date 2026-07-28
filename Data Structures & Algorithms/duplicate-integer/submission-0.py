class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set(nums)

        if len(unique_num) == len(nums):
            return False
        else:
            return True