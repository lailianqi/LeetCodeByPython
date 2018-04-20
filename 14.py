import os
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        for i, e in enumerate(zip(*strs)):
            if len(set(e)) > 1:
                return strs[0][:i]
        return min(strs)


# a = [1, 3, 4, 5]
# b = [1, 2, 4, 6]
# c = [a, b]
# print(c)
# print(*zip(a, b))
# print(*zip(*c))
# print(*a)

class Solution_0:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        直接调用库的写法
        https://leetcode.com/problems/longest-common-prefix/discuss/7242/Already-implemented-in-Python
        """
        return os.path.commonprefix(strs)