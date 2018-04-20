class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
        """
        nums.sort()
        results = []
        for i in range(len(nums)-3):
            if i == 0 or nums[i] != nums[i-1]:
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results

    def threeSum(self, nums, target):
        """
        第15题
        :type nums: List[int]
        :rtype: List[List[int]]
        https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution
        https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time)
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if(i == 0 or nums[i] != nums[i-1]):
                left, right = i+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] == target-nums[i]:
                        res.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left, right = left + 1,  right - 1
                    elif nums[left] + nums[right] < target-nums[i]:
                        left += 1
                    else:
                        right -= 1
        return res


class Solution_0:
    def fourSum(self, nums, target):
        """
        leetcode上面递归的写法 在提交通过的的柱状图里面的代码
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rt = []
        nums.sort()
        self.nSum(nums, target, 4, [], rt)
        return rt

    def nSum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if target < nums[0] * N or target > nums[-1] * N:
            return

        if N == 2:
            p1 = 0
            p2 = len(nums) - 1
            while p2 > p1:
                if nums[p1] + nums[p2] == target:
                    results.append(result + [nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    while p2 > p1 and nums[p1] == nums[p1 - 1]:
                        p1 += 1
                    while p2 > p1 and nums[p2] == nums[p2 + 1]:
                        p2 -= 1
                elif nums[p1] + nums[p2] < target:
                    p1 += 1
                else:
                    p2 -= 1

        else:
            for i in range(len(nums)-N+1):
                if i == 0 or nums[i] != nums[i-1]:
                    self.nSum(nums[i+1:], target-nums[i], N -
                              1, result + [nums[i]], results)
