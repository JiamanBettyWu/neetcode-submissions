class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        # for l in range(len(heights)-1):
        max_area = 0 
        while r > l:
            area = min(heights[l], heights[r]) * (r-l)
            if heights[l] < heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1
            elif heights[l] == heights[r]:
                l+=1
                r-=1
            if area > max_area:
                max_area = area
        return max_area
        
        