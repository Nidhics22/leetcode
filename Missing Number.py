class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        val = 0
        missing_number = 0
        for i in range(len(nums)+1):
            sum = sum + i
        for i in range(len(nums)):
            val = val + nums[i]
        missing_number = sum - val
        return missing_number