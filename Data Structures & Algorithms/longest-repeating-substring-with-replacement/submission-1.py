class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts ={}
        l = 0
        best = 1
        for r in range(len(s)):
            
            counts.setdefault(s[r], 0)
            counts[s[r]]+=1

            wind_size = r+1 - l
            
            replace = wind_size - max(counts.values())

            if replace <= k:
                best = max(best, wind_size)
            else:
                counts[s[l]]-=1
                l+=1

        return best
            



            









