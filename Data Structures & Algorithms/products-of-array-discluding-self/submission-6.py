class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = []
        right_left = []
        results = []
        for i in range(len(nums)):
            m = (left_right[-1] * nums[i-1]) if i > 0 else 1
            left_right.append(m)
        for i in range(len(nums)-1, -1, -1):
            m = (right_left[-1] * nums[i+1]) if i < (len(nums)-1) else 1
            right_left.append(m)
        right_left = right_left[::-1]
        
        for i in range(len(nums)):
            results.append(left_right[i] * right_left[i])
        
        return results
