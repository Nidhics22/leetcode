class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        LEETCODE #128
        """
        if (len(nums) == 0):
            return 0
        nums = sorted(nums)
        i = 0
        j = i + 1
        currentCounter = 1
        maxCounter = 0
        while (j < len(nums)):
            val = nums[j] - nums[i]
            i += 1
            j += 1
            if (val == 1):
                currentCounter += 1
            elif (val == 0):
                continue
            else:
                maxCounter = max(currentCounter, maxCounter)
                currentCounter = 1
        return (max(currentCounter, maxCounter))




