class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution
        https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if(i == 0 or nums[i] != nums[i-1]):
                left, right = i+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1,  right - 1
                    elif nums[left] + nums[right] < -nums[i]:
                        left += 1
                    else:
                        right -= 1
        return res
