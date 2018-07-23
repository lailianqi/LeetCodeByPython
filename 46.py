import itertools
# 来自sp大神的解法
# https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return nums and [p[:i]+[nums[0]]+p[i:] for p in self.permute(nums[1:]) for i in range(len(nums))] or [[]]


class Solution_0:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums))
