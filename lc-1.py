#!/usr/bin/python3


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        retlst = []
        for x, xnum in enumerate(nums):
            for y, ynum in enumerate(nums):
                if y != x:
                    if (xnum + ynum) == target:
                        retlst.append(x)
                        retlst.append(y)
                        return retlst


nums = [3, 3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
