class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet=set()
        for i in range(len(nums)):
            if nums[i] not in numsSet:
                numsSet.add(nums[i])
            else:
                return True
        return False