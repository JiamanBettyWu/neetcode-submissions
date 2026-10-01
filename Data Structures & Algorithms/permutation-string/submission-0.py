class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        target = Counter(s1)
        k = len(s1)

        for left in range(len(s2) - k + 1):
            window = s2[left:left+k]

            if Counter(window) == target:
                return True
        
        return False