class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        sp大神的解法 我用python实现
        https://leetcode.com/problems/trapping-rain-water/discuss/17364/7-lines-C-C++
        其实是下面链接这种方法的优雅版 思想是一样的
        https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.
        """
        left, right, level,  water = 0, len(height)-1, 0, 0
        while left < right:
            cur = 0
            if height[left] < height[right]:
                cur = height[left]
                left += 1
            else:
                cur = height[right]
                right -= 1
            level = max(level, cur)
            water += level - cur
        return water


class Solution_00:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        我估计是sp大神在jianchao.li.fighter大神的解法上修改的
        https://leetcode.com/problems/trapping-rain-water/discuss/17403/8-lines-CC++JavaPython-Solution
        """
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water


class Solution_0:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        解法来自以前自己的c++的方案
        """
        stack, res = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack[-1]
                stack.pop()
                res += 0 if not stack else ((
                    min(height[i], height[stack[-1]])-height[bottom])*(i - stack[-1] - 1))
            stack.append(i)
        return res
