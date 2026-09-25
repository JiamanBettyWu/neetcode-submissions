class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r, best = 0, 0, 0

        for r, c in enumerate(s):
            n = r - l
            if c not in seen.keys() or (seen[c] < l):
                seen[c] = r
                n+=1
            else:
                last_seen = seen[c]
                l = last_seen + 1
                seen[c] = r
                
            best = max(best, n)
        
        return best 
