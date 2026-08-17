class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s)-1

        while left < right:
            lc = s[left]
            while not lc.isalnum() and left < right:
                left+=1
                lc = s[left]
               

            rc = s[right]
            while not rc.isalnum() and left < right:
                right-=1
                rc = s[right]
                
            if rc.lower() != lc.lower():
                return False
            left+= 1
            right-=1
        return True







        