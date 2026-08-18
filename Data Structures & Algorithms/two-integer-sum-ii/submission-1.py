class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers, start=1):
            diff = target - n 
            if diff not in seen:
                seen[n] = i 
            else:
                return [seen[diff], i]
