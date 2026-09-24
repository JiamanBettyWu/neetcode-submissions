class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, n, best = 0, 0, 0, 0
        counts = {}

        while r < len(s):
            
            c = s[r]
            counts[c] = counts.get(c, 0) + 1
            n = len(s[l:r]) + 1
            
            if k < (n - max(counts.values())):
                counts[s[l]] = counts[s[l]] - 1
                l+=1
                r+=1
            else:
                r+=1
        return len(s) - l

            
