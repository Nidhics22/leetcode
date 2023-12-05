class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_substring = len(needle)

        for i in range(len(haystack)):
            if haystack[i: i + len_substring] == needle:
                return i
        return -1




