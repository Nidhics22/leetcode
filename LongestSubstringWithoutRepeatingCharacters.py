class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        i = 0
        ans = 0
        for j in range(len(s)):
            while s[j] in s_set:
                s_set.remove(s[i])
                i+=1
            s_set.add(s[j])
            ans = max(ans, len(s_set))
        return ans