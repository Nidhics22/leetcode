class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for char in strs:
            temp = ''.join(sorted(char))
            if temp not in result:
                result[temp] = [char]
            else:
                result[temp].append(char)
        return result.values()
