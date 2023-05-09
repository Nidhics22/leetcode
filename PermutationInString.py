class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for i in range(len(s1)):
            s1_index = ord(s1[i]) - ord('a')
            s2_index = ord(s2[i]) - ord('a')
            count_s1[s1_index] += 1
            count_s2[s2_index] += 1

        l = 0
        r = len(s1)
        while (r < len(s2)):
            if count_s1 == count_s2:
                return True
            back = ord(s2[l]) - ord('a')
            front = ord(s2[r]) - ord('a')
            count_s2[back] -= 1
            count_s2[front] += 1
            l += 1
            r += 1
        return count_s1 == count_s2