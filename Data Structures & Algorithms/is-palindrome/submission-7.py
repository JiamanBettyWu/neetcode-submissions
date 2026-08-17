class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(s)-1

        while left < right:
            lc = s[left]
            while not lc.isalnum():
                left+=1
                try:
                    lc = s[left]
                except IndexError:
                    lc = ""

            rc = s[right]
            while not rc.isalnum():
                right-=1
                try: 
                    rc = s[right]
                except IndexError:
                    rc = ""
            if rc.lower() != lc.lower():
                return False
            left+= 1
            right-=1
        return True







        