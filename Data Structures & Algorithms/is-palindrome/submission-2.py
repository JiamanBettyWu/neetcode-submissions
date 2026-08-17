class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join(l.lower() for l in s if l.isalnum())
        l = len(cleaned_s)
        if (l%2) != 0:
            center_id = l//2
            first_half = cleaned_s[:center_id]
            second_half = cleaned_s[center_id+1:][::-1]

        if (l%2) == 0:
            center_id = int(l/2)
            first_half = cleaned_s[:center_id]
            second_half = cleaned_s[center_id:][::-1]

        if first_half == second_half:
            return True
        else:
            return False



        