class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        while True:
            product = 0
            product = k*i 
            if product not in nums:
                return product
                break
            i += 1
