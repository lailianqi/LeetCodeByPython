class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        自己一行的解法
        """
        return nums.index(target) if target in nums else -1


class Solution_0:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        来自LeetCode的解法 这个解法的由来的版本有个bug 列表不能为空 现在已经修复
        https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14425/Concise-O(log-N)-Binary-search-solution
        """
        if not nums:
            return -1
        midIndex = self.findMinIndex(nums)
        if nums[midIndex] == target:
            return midIndex
        m = len(nums)
        left = midIndex if target <= nums[m-1] else 0
        right = midIndex if target > nums[m-1] else m-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid - 1
        return -1

    def findMinIndex(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return left


class Solution_1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
        https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search
        """
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid-1
        return -1
