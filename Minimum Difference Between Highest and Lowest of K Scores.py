class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums = sorted(nums)
        res = float('inf')
        for i in range(len(nums) - k + 1):
            j = i + k - 1
            val = nums[j] - nums[i]
            res = min(res, val)
            i += 1
        return res