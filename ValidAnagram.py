class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sDict = {}
        for i in s:
            if i not in sDict:
                sDict[i] = 1
            else:
                sDict[i] += 1

        for i in t:
            if i not in sDict or sDict[i] == 0:
                return False
            else:
                sDict[i] -= 1
        return True