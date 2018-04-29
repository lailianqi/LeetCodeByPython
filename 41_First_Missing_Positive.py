class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这题的python的关键是直接交换 不能直接swap
        """
        m = len(nums)
        for i in range(m):
            while nums[i] > 0 and nums[i] <= m and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]-1
                # nums[i], nums[nums[i]-1] = nums[nums[i] - 1], nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

        for i in range(m):
            if nums[i] != i+1:
                return i+1
        return m+1


a = [3, 4, -1, 1]
s = Solution()
s.firstMissingPositive(a)
