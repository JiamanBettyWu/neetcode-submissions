class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        left_max, right_max, water = 0, 0, 0

        while L < R:
            left_max = max(left_max, height[L])
            right_max = max(right_max, height[R])

            if left_max <= right_max:
                water+=left_max - height[L]
                L+=1
            else:
                water+=right_max - height[R]
                R-=1
        return water 

