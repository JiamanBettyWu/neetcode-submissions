class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        counter = {}

        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1

            length = r - l + 1
            if length - max(counter.values()) > k:
                counter[s[l]] = counter[s[l]] - 1
                l+=1
        
        return r-l+1
