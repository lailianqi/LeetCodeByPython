class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        参考了LeetCode官方的答案
        https://leetcode.com/problems/multiply-strings/discuss/17615/Simple-Python-solution-18-lines
        """
        m, n = len(num1), len(num2)
        res = [0]*(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i+j+1] += int(num1[i])*int(num2[j])
                res[i+j] += res[i+j+1]//10
                res[i+j+1] %= 10
        while len(res) > 1 and res[0] == 0:
            res.pop(0)
        return ''.join(map(str, res))


class Solution_0:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        作弊的方法
        """
        return str(int(num1)*int(num2))
