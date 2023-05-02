class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        val = 1
        zeroCounter = 0
        for i in range(len(nums)):
            if (nums[i]==0):
                zeroCounter+=1
            else:
                val = val * nums[i]

        for i in range(len(nums)):
            if (zeroCounter>=2):
                ans.append(0)
            elif (zeroCounter==1):
                if(nums[i]==0):
                    ans.append(val)
                else:
                    ans.append(0)
            else:
                finalVal = val // nums[i]
                ans.append(finalVal)
        return ans


