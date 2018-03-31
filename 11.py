

class Solution:
    # https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C++C-with-explanation
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            veticalHeight = min(height[i], height[j])
            res = max(res, (j-i)*veticalHeight)
            while i < j and height[i] <= veticalHeight:
                i += 1
            while i < j and height[j] <= veticalHeight:
                j -= 1
        return res


class Solution1:
    # https://leetcode.com/problems/container-with-most-water/discuss/6090/Simple-and-fast-C++C-with-explanation
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            veticalHeight = min(height[i], height[j])
            res = max(res, (j-i)*veticalHeight)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
