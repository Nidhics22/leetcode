class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = {}
        for char in strs:
            temp = ''.join(sorted(char))
            if temp not in result:
                result[temp] = [char]
            else:
                result[temp].append(char)
        return result.values()

