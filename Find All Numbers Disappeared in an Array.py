class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        num_set = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in num_set:
                ans.append(i)
        return ans