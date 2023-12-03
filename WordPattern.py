class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split_s = s.split(' ')
        count = {}

        if len(pattern) != len(split_s):
            return False

        for i in range(len(split_s)):
            if pattern[i] not in count:
                if split_s[i] not in count.values():
                    count[pattern[i]] = split_s[i]
                else:
                    return False
            else:
                if count[pattern[i]] != split_s[i]:
                    return False
        return True