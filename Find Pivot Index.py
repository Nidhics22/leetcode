class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        for idx, val in enumerate(nums):
            right_sum -= val
            if left_sum == right_sum:
                return idx
            else:
                left_sum += val
        return -1