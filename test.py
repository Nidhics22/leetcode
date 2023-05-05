def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    if len(s1) > len(s2):
        return False

    s1CharCount = [0] * 26
    s2CharCount = [0] * 26

    for i in range(len(s1)):
        s1Idx = ord(s1[i]) - ord('a')
        s2Idx = ord(s2[i]) - ord('a')
        s1CharCount[s1Idx] += 1
        s2CharCount[s2Idx] += 1

    l = 0
    r = len(s1)

    while (r < len(s2)):
        if (s1CharCount == s2CharCount):
            return True
        back = ord(s2[l]) - ord('a')
        front = ord(s2[r]) - ord('a')

        s2CharCount[back] -= 1
        s2CharCount[front] += 1

        l += 1
        r += 1

    return s1CharCount == s2CharCount


class Solution(object):
    checkInclusion("ab", "eidbaooo")