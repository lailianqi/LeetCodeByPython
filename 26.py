class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        自己的第一种解法
        """
        if len(nums) == 0:
            return 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
        return length


class Solution_0:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        上面的的稍微的改进
        """
        length = 0
        for i in range(0, len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                nums[length] = nums[i]
                length += 1
        return length
