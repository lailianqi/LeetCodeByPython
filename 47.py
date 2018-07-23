class Solution:

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        https://leetcode.com/problems/permutations-ii/discuss/18596/A-simple-C++-solution-in-only-20-lines
        """
        res = []

        def helper(left):
            if left == len(nums)-1:
                res.append(nums.copy())
                return
            dir = {}
            for i in range(left, len(nums)):
                if nums[i] not in dir:
                    nums[left], nums[i] = nums[i], nums[left]
                    helper(left+1)
                    nums[left], nums[i] = nums[i], nums[left]
                dir[nums[i]] = 1
        helper(0)
        return res

s = Solution()
l = [1,1,2]
s.permuteUnique(l)
