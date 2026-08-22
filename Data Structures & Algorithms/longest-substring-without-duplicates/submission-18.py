class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = {}

        left, right = 0, 0
        while right < len(s):
            if s[right] not in seen:
                seen[s[right]] = right
            else:
                p = seen[s[right]] 
                left = max(p + 1, left)
                seen[s[right]] = right
            
            right += 1
            longest = max(longest, (right - left))
            
        return longest
