class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = []
        st = ""
        for i in range(len(digits)):
            st = st + str(digits[i])
        n = int(st) + 1
        st = str(n)
        for i in st:
            s = int(i)
            nums.append(s)
        return nums
