class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        start = nums[0]
        end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                end = nums[i]
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+'->'+str(end))

                start = nums[i]
                end = nums[i]
                
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start)+'->'+str(end))
        return ans
