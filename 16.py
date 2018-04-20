class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
        https://leetcode.com/problems/3sum-closest/discuss/7873/A-n2-Solution-Can-we-do-better?page=1
        """
        answer = nums[0] + nums[1] + nums[2]
        sortlist = sorted(nums)
        for i in range(len(sortlist)):
            left, right = i+1, len(sortlist)-1
            while left < right:
                sum = sortlist[i] + sortlist[left] + sortlist[right]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(answer - target):
                    answer = sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return answer
