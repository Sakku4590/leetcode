class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        
        if i > j:
            i, j = j, i  
        
        opt1 = j + 1
        
        opt2 = n - i
        
        opt3 = (i + 1) + (n - j)
        
        return min(opt1, opt2, opt3)