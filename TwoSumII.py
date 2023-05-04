class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while (i < j):
            sum = numbers[i] + numbers[j]
            if (sum > target):
                j -= 1
            elif (sum < target):
                i += 1
            else:
                return (i + 1, j + 1)
        return []