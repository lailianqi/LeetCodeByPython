class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        python的解法 来自sp大神
        https://leetcode.com/problems/search-for-a-range/discuss/14707/9-11-lines-O(log-n)
        """
        def search(n):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right)//2
                if nums[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            return left
        left = search(target)
        return [left, search(target+1)-1] if target in nums[left:left+1] else [-1, -1]
