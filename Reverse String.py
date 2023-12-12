class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new_s = ""
        i = 0
        j = len(s) - 1
        while i < j:
            new_s = s[i]
            s[i] = s[j]
            s[j] = new_s
            i += 1
            j -= 1
