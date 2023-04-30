lass
Solution:


def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = []
    numsDict = {}
    val = 0
    for i in range(len(nums)):
        val = target - nums[i]
        if val not in numsDict:
            numsDict[nums[i]] = i
        else:
            ans.append(numsDict[val])
            ans.append(i)
            return ans
