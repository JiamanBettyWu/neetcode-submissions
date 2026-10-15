from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        l = 0
        s2_count = {}

        for i, r in enumerate(s2):
            
            s2_count[r] = s2_count.setdefault(r, 0) + 1

            if s1_count == s2_count:
                return True
            
            if i - l + 1 == len(s1):

                s2_count[s2[l]]-=1
                if s2_count[s2[l]] == 0: del s2_count[s2[l]]
                l+=1
      
        return False
            

