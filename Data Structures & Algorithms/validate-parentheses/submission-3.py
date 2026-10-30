class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        closer = ["}","]", ")"]
        for c in s:

           
            
            if c not in closer:
                seen.append(c) 
                continue

            if seen: last = seen.pop()
            else: return False
            
            if last  == '(': need = ')'
            elif last == '[': need = ']'
            elif last == '{': need = '}'

            if c != need: return False
            

            
        if seen:
            return False
        return True


                    
