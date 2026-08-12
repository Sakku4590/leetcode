class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Add nums[right]
            count[nums[right]] = count.get(nums[right], 0) + 1

            # If window is invalid, move left
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            # Update maximum length
            max_length = max(max_length, right - left + 1)

        return max_length