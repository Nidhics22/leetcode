class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        rmv = -1

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = rmv
            rmv = max(rmv, arr[i])
        return ans