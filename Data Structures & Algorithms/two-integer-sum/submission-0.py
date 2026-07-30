class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            first_num = nums[i]
            need = target - first_num
            search_start = i + 1
            if need in nums[search_start:]:
                j = nums[i+1:].index(need) + search_start
                return [i, j]
        