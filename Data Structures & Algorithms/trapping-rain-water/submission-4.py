class Solution:
    def trap(self, height: List[int]) -> int:
        
        l, r = 0, len(height) -1
        l_high, r_high, water  = 0, 0, 0
        while l < r:
            l_high = max(l_high, height[l])
            r_high = max(r_high, height[r])

            if l_high < r_high:
                water += l_high - height[l]
                l+=1
            else:
                water += r_high - height[r]
                r-=1
        
        return water
