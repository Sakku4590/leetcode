class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        ans = []
        freq = {}
        for i in nums1:
            freq[i] = freq.get(i,0)+1
        
        for num in nums2:
            if num in freq and freq[num] > 0:
                ans.append(num)
                freq[num] -= 1
        return ans