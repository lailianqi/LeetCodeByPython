import bisect



# 这题对于lower_bound 和 uppper_lower的理解非常的有帮助
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        暴力的解法
        """
        return len([x for x in nums if x < target])


class Solution_0:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        lower_bound的方法
        """
        return bisect.bisect_left(nums, target)


class Solution_1:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        lower_bound的方法
        https://leetcode.com/problems/search-insert-position/discuss/15081/Python-one-liner-48ms
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
