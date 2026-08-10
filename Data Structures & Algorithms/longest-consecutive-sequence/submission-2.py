class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_set = sorted(set(nums))

        if sorted_set:
            longest = 1
        else:
            return 0
        count = 1
        for i in range(len(sorted_set) - 1):
            if sorted_set[i + 1] - sorted_set[i] == 1:
                count += 1
            else:
                count = 1
            if count > longest:
                longest = count

        return longest
