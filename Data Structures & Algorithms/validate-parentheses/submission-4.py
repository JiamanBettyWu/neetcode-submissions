class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        closer = ["}","]", ")"]
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
           
            if c not in closer:
                seen.append(c) 
                continue

            if seen: last = seen.pop()
            else: return False

            if last != pairs[c]: return False
            
        return not seen


                    
