class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCounter = 0
        oneCounter = 0
        twoCounter = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCounter += 1
            elif nums[i] == 1:
                oneCounter += 1
            else:
                twoCounter += 1

        c = 0
        while zeroCounter > 0:
            nums[c] = 0
            c += 1
            zeroCounter -= 1

        while oneCounter > 0:
            nums[c] = 1
            c += 1
            oneCounter -= 1
        while twoCounter > 0:
            nums[c] = 2
            c += 1
            twoCounter -= 1