from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:

    ans = []
    if len(temperatures) == 0:
        return ans
    for i in range(len(temperatures) - 1):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                ans.append(j - i)
                break
            else:
                j += 1
            if j == len(temperatures):
                ans.append(0)
    ans.append(0)
    print(ans)
    return ans


class Solution:
    dailyTemperatures([73, 69, 68])
