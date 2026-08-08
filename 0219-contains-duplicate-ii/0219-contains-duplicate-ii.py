class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last_seen = {}

        for i, num in enumerate(nums):
            # If we've seen this number before
            if num in last_seen:
                # Check if the indices are within k
                if i - last_seen[num] <= k:
                    return True

            # Update the last seen index
            last_seen[num] = i

        return False
        