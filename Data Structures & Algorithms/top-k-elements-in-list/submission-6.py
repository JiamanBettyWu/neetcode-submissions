class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in counts.items():
            buckets[value].append(key)
        
        res_l = []
        for i in buckets[::-1]:
            if i: res_l.append(i)
            res_f = [v for res in res_l for v in res]
            if len(res_f) == k:
                return res_f

