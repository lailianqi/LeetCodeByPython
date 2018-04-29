class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        解法来自我的c++方案
        下面LeetCode的解法和我的c++方案思想差不多
        https://leetcode.com/problems/wildcard-matching/discuss/17812/My-java-DP-solution-using-2D-table
        https://leetcode.com/problems/wildcard-matching/discuss/17845/Python-DP-solution
        """
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != "*":
                    dp[i][j] = i > 0 and dp[i-1][j -
                                                 1] and (s[i-1] == p[j-1] or p[j-1] == "?")
                else:
                    dp[i][j] = dp[i][j-1] or (i > 0 and dp[i-1][j])
        return dp[m][n]


class Solution_0:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        双重指针的写法
        解法来自LeetCode的题解 在评论里面
        https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
        """
        m, n = len(s), len(p)
        i = j = 0
        star = match = None
        while i < m:
            if j < n and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                star = j
                j += 1
                match = i
            elif star is not None:
                j = star+1
                match += 1
                i = match
            else:
                return False
        return all(p[k] == '*' for k in range(j, n))
