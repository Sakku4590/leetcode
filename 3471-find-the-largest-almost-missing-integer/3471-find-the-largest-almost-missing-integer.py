class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        # Check every subarray of size k
        for i in range(len(nums) - k + 1):

            # Unique elements in this subarray
            unique = set(nums[i:i + k])

            # Count this subarray for every unique element
            for x in unique:
                count[x] = count.get(x, 0) + 1

        # Find the largest number appearing in exactly one subarray
        ans = -1

        for x, freq in count.items():
            if freq == 1:
                ans = max(ans, x)

        return ans