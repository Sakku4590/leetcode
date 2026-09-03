class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')
        cnt_odd = 0
        cnt_even = 0
        
        for x in nums1:
            if x % 2 == 1:
                cnt_odd += 1
                min_odd = min(min_odd, x)
            else:
                cnt_even += 1
                min_even = min(min_even, x)
        
        # Target: all even
        all_even_possible = (cnt_odd == 0)
        
        # Target: all odd
        all_odd_possible = (cnt_even == 0) or (cnt_odd >= 1 and min_odd < min_even)
        
        return all_even_possible or all_odd_possible