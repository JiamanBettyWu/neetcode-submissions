class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        
        numbers =[num for num in nums if num != 0]
        product = math.prod(numbers) if (abs(len(numbers) - len(nums)) <= 1) else 0

        results = []
        for n in nums:
            if 0 in nums:
                try:
                    r = product/n
                    results.append(0)
                except:
                    results.append(product)
            else:
                results.append(int(product/n))

        return results