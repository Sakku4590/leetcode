class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1 way of solve this problem
        # my_set = set()
        # for i in nums1:
        #     if i in nums2:
        #         my_set.add(i)
        # return (list(my_set))

        # 2 way of solve this problem
        my_set = set(nums1)
        ans = []
        for i in set(nums2):
            if i in my_set:
                ans.append(i)
        return ans