class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        参考自sp大神的解法
        https://leetcode.com/problems/next-permutation/discuss/13921/1-4-11-lines-C++
        """
        k = len(nums) - 1
        index = k
        while index > 0 and nums[index-1] >= nums[index]:
            index -= 1
        j = index
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
        if index > 0:
            index -= 1
            k = index+1
            while nums[k] <= nums[index]:
                k += 1
            nums[index], nums[k] = nums[k], nums[index]
