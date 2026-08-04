class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 

        counts = Counter(nums)

        return [n for n, _ in counts.most_common(k)]