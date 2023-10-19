class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_val = nums.count(val)
        final_val = len(nums) - new_val
        i = 0
        while i < final_val:
            if nums[i] == val:
                nums.append(nums.pop(i))
            else:
                i += 1
        return final_val