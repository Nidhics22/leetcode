class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        length = min(len(word1), len(word2))
        for i in range(length):
            res += word1[i] + word2[i]
        return res + word1[length:] + word2[length:]
