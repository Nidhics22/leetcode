class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = set()
        for i in range(len(nums)):
            if nums[i] not in val:
                val.add(nums[i])
            else:
                val.remove(nums[i])

        ans = 0
        for final_val in val:
            ans = final_val
        return ans