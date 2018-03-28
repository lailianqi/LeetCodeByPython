class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dir = dict()
        for i in range(len(nums)):
            if(target - nums[i] in dir):
                return [dir[target - nums[i]], i]
            dir[nums[i]] = i
        return [-1,-1]
