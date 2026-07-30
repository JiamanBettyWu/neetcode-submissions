class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            letters = "".join(sorted(word))
            print(letters)

            if letters in seen:
                seen[letters].append(word)
            
            else:
                seen[letters] = [word]
        return list(seen.values())

