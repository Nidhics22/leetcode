class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for val in range(len(strs) - 1):
            a = ans
            b = strs[val + 1]
            i = 0
            j = 0
            ans = ''
            while i < len(a) and j < len(b):
                if a[i] != b[j]:
                    break
                else:
                    ans = ans + a[i]
                    i += 1
                    j += 1
        return ans