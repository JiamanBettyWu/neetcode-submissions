class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for l, n in enumerate(nums):
            if (l > 0) and (nums[l-1] == n):
                continue
            
            m = l + 1
            r = len(nums) - 1 

            target = -n

            while m < r:
                s = nums[m] + nums[r]
                if s > target:
                    r-=1
                    
                elif s < target:
                    m+=1
                  
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m+=1 
                    r-=1
                
                    while (m < r) and (nums[r+1] == nums[r]):
                        r-=1
                    while (m < r) and (nums[m-1] == nums[m]):
                        m+=1
        return res


