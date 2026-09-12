class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        res = []
        i = 0

        while i < len(nums):
            
            n = nums[i]
            need = -n 

        

            l = i+1
            r = len(nums) - 1
            while l < r:
                l_n = nums[l]
                r_n = nums[r]

                if l_n + r_n > need:
                    r-=1
                    while l < r and r_n == nums[r]:
                        r-=1
                    

                elif l_n + r_n < need:
                    l+=1
                    while l < r and l_n == nums[l]:
                        l+=1
                
                else:
                    
                    res.append([n, nums[l], nums[r]])
                    r-=1
                    l+=1
                    while l < r and r_n == nums[r]:
                        r-=1
                    
                    while l < r and l_n == nums[l]:
                        l+=1
            i+=1
            while i < len(nums) and nums[i] == n:
                i+=1

        
        return res