class Solution:
    def trap(self, height: List[int]) -> int:

        left_highest = []
        for h in height:
            if left_highest and h < left_highest[-1]:
                 left_highest.append(left_highest[-1])
            else:
                left_highest.append(h)

        right_highest = []
        for h in height[::-1]:
            if right_highest and h < right_highest[-1]:
                 right_highest.append(right_highest[-1])
            else:
                right_highest.append(h)
        
        right_highest = right_highest[::-1]
        
        water = 0
        for i, h in enumerate(height):
            l = left_highest[i]
            r = right_highest[i]

            water+= min(l, r) - h
        
        return water