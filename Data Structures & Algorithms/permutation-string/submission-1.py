class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        target = Counter(s1)
        k = len(s1)
        left = 0 

        window_count = {}

        for right, c in enumerate(s2):

            window_count.setdefault(c, 0)
            window_count[c] += 1

            if window_count == target:
                return True
            
            if right - left + 1 == k:
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:  del window_count[s2[left]]
                left+=1

        return False



