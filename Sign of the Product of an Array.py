class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)):
            res *= nums[i]
        if res > 0:
            res = 1
        elif res < 0:
            res = -1
        else:
            res = 0
        return res
