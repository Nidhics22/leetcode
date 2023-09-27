class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        pos = len(res) - 1
        num1 = num1[::-1]
        num2 = num2[::-1]

        for n1 in num1:
            temp = pos
            for n2 in num2:
                res[temp] += int(n1) * int(n2)
                res[temp - 1] += res[temp] // 10
                res[temp] %= 10
                temp -= 1
            pos -= 1

        beg = 0
        while beg < len(res) - 1 and res[beg] == 0:
            beg += 1
        return ''.join(map(str, res[beg:]))
