class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        top_k = Counter(nums).most_common(k)

        return [keys for keys, values in top_k]