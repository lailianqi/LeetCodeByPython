class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        https://leetcode.com/problems/count-and-say/discuss/16043/C++-solution-easy-understand
        https://leetcode.com/problems/count-and-say/discuss/16044/Simple-Python-Solution
        """
        res = "1"
        for _ in range(n-1):
            counter, cur = 1, ""
            m = len(res)
            for i in range(m):
                if i < m-1 and res[i] == res[i+1]:
                    counter += 1
                else:
                    cur = cur + str(counter)+res[i]
                    counter = 1
            res = cur
        return res


import itertools
class Solution_0:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions
        sp大神的解法 暂时没办法理解
        """
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in itertools.groupby(s))
        return s
