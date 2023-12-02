class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        ans = 0

        for char in text:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        word = "balloon"
        while True:
            for char in word:
                if char in count and count[char] > 0:
                    count[char] -= 1
                else:
                    return ans
            ans += 1

        return ans