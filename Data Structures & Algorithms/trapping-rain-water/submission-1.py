class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = []
        max_right = []
        for i, n in enumerate(height):
           ml = max(n, max_left[i-1]) if i > 0 else height[i] 
           mr = max(max_right[i-1], height[-i-1]) if i > 0 else height[-1]  

           max_left.append(ml)
           max_right.append(mr)
        max_right = max_right[::-1]  
        water = []
        for i, h in enumerate(height):
            water.append(min(max_left[i], max_right[i]) - h)
   
        return sum(water)



