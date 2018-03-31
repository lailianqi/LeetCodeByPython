
class Solution:
    # https://leetcode.com/problems/regular-expression-matching/discuss/5665/My-concise-recursive-and-DP-solutions-with-full-explanation-in-C++
    # https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(0, m+1):
            for j in range(1, n+1):
                if(p[j-1] != '*'):
                    dp[i][j] = (i > 0 and dp[i-1][j-1]) and (s[i-1]
                                                             == p[j-1] or p[j-1] == '.')
                else:  # p[0] cannot be '*' so no need to check "j > 1" here
                    dp[i][j] = dp[i][j-2] or (i > 0 and dp[i - 1][j]
                                              and (s[i-1] == p[j-2] or p[j-2] == '.'))
        return dp[m][n]


l = [[True] + [False] *8]
print(l)