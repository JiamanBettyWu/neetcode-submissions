class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        counter = {}
        max_freq = 0

        for r, c in enumerate(s):
            counter[c] = counter.get(c, 0) + 1
            max_freq = max(max_freq, counter[c])

            length = r - l + 1
            if length - max_freq > k:
                counter[s[l]] = counter[s[l]] - 1
                l+=1
        
        return r-l+1
