class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_set = set()
        for i in nums1:
            if i in nums2:
                my_set.add(i)
        return (list(my_set))