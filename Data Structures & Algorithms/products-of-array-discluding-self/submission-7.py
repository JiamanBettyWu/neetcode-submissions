class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
        results = []
        m = 1
        for i in range(len(nums)):
            results.append(m)
            m *= nums[i]
        m = 1
        for i in range(len(nums)-1, -1, -1):            
            results[i] *= m
            m *= nums[i]
        
        return results