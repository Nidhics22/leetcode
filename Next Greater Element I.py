class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        ans = []

        for idx, val in enumerate(nums2):
            count[val] = idx

        for i in range(len(nums1)):
            if nums1[i] in count:
                j = count[nums1[i]]
                if j + 1 > len(nums2) - 1:
                    ans.append(-1)
                elif nums2[j + 1] > nums2[j]:
                    ans.append(nums2[j + 1])
                else:
                    k = j + 1
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            ans.append(nums2[k])
                            break
                        k += 1
                        if k == len(nums2):
                            ans.append(-1)
        return ans